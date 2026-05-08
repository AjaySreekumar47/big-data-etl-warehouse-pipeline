# Architecture

This project is organized as an end-to-end enterprise data engineering and MLOps workflow.

## End-to-End Data Pipeline

```mermaid
flowchart LR
    A[Synthetic Enterprise Logs] --> B[MongoDB Atlas Ingestion]
    B --> C[PySpark ETL]
    C --> D[Partitioned Parquet Warehouse]
    D --> E[Star Schema / Fact Table]
    E --> F[SCD Product Dimension]
    E --> G[Spark SQL Analytics]
    E --> H[Feature Store / ML Pipeline]
    H --> I[Model Training]
    I --> J[GCS Model Artifact]
    J --> K[Vertex AI Deployment Template]
```

## Warehouse Modeling

```mermaid
erDiagram
    FACT_SALES_ENRICHED {
        string sale_id
        string customer_id
        string product_id
        string region
        int quantity
        float price
        float line_revenue
        date sale_date
        int sale_year
        int sale_month
    }

    DIM_PRODUCT_HISTORY {
        string product_id
        string product_name
        string category
        string price_band
        boolean is_current
        date start_date
        date end_date
    }

    FACT_SALES_ENRICHED ||--o{ DIM_PRODUCT_HISTORY : product_id
```

## MLOps Template

```mermaid
flowchart LR
    A[GitHub Push] --> B[GitHub Actions]
    B --> C[Google Cloud Authentication]
    C --> D[Cloud Build]
    D --> E[Trainer Package]
    E --> F[Feast Feature Retrieval]
    F --> G[RandomForestRegressor Training]
    G --> H[model.joblib + metrics.json]
    H --> I[Vertex AI / GCS Template]
```

## Component Status

| Layer | Status |
|---|---|
| Synthetic data generation | Implemented and locally verified |
| Product ID alignment | Implemented |
| Warehouse sample rebuild | Implemented |
| Revenue analytics output | Implemented |
| MongoDB Atlas ingestion | Implemented, cloud-dependent |
| PySpark ETL notebooks | Implemented in notebook workflow |
| SCD Type 1 / Type 2 modeling | Implemented in notebook/data workflow |
| Feast + Vertex trainer | Prototype / template |
| GitHub Actions + Cloud Build | Template / cloud-dependent |