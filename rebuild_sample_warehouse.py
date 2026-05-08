from pathlib import Path
import sys

import pandas as pd

sys.path.append("1_log_simulation")
from simulate_logs import generate_sales_log


ROOT = Path(__file__).resolve().parent
WAREHOUSE_DIR = ROOT / "4_data_warehouse" / "warehouse" / "fact_sales_enriched"
PRODUCT_HISTORY_PATH = ROOT / "5_scd_dimension_modeling" / "dim_product_history.csv"
OUTPUT_SUMMARY_PATH = ROOT / "6_analytics" / "sample_revenue_summary.csv"


def rebuild_fact_sales_enriched(n_sales: int = 1300) -> pd.DataFrame:
    sales_df = pd.DataFrame(generate_sales_log(n_sales))
    sales_df["timestamp"] = pd.to_datetime(sales_df["timestamp"])
    sales_df["sale_date"] = sales_df["timestamp"].dt.date
    sales_df["sale_year"] = sales_df["timestamp"].dt.year
    sales_df["sale_month"] = sales_df["timestamp"].dt.month

    product_history = pd.read_csv(PRODUCT_HISTORY_PATH)

    current_products = product_history[
        product_history["is_current"].astype(str).str.lower() == "true"
    ].copy()

    fact_sales = sales_df.merge(
        current_products,
        on="product_id",
        how="left",
    )

    fact_sales["line_revenue"] = fact_sales["quantity"] * fact_sales["price"]

    ordered_cols = [
        "sale_id",
        "customer_id",
        "product_id",
        "product_name",
        "category",
        "price_band",
        "region",
        "quantity",
        "price",
        "line_revenue",
        "timestamp",
        "sale_date",
        "sale_year",
        "sale_month",
        "is_current",
        "start_date",
        "end_date",
    ]

    return fact_sales[ordered_cols]


def write_outputs(fact_sales: pd.DataFrame) -> None:
    WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

    for old_file in WAREHOUSE_DIR.glob("*.parquet"):
        old_file.unlink()

    output_path = WAREHOUSE_DIR / "fact_sales_enriched_sample.parquet"
    fact_sales.to_parquet(output_path, index=False)

    summary = (
        fact_sales.groupby(["category", "region"], dropna=False)
        .agg(
            total_orders=("sale_id", "count"),
            total_units_sold=("quantity", "sum"),
            total_revenue=("line_revenue", "sum"),
            avg_order_value=("line_revenue", "mean"),
        )
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )

    summary["total_revenue"] = summary["total_revenue"].round(2)
    summary["avg_order_value"] = summary["avg_order_value"].round(2)
    summary.to_csv(OUTPUT_SUMMARY_PATH, index=False)

    print(f"Saved fact table: {output_path}")
    print(f"Saved revenue summary: {OUTPUT_SUMMARY_PATH}")
    print(f"Fact shape: {fact_sales.shape}")
    print("Product metadata null rates:")
    print(fact_sales[["product_name", "category", "price_band"]].isna().mean())
    print("Revenue by category:")
    print(
        fact_sales.groupby("category")["line_revenue"]
        .sum()
        .round(2)
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    fact = rebuild_fact_sales_enriched()
    write_outputs(fact)