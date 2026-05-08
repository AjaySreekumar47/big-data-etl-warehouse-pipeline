from faker import Faker
import random

fake = Faker()

PRODUCT_IDS = ["P101", "P102", "P103", "P104"]
REGIONS = ["North", "South", "East", "West"]
DEVICES = ["mobile", "desktop", "tablet"]
ACTIONS = ["click", "scroll", "purchase", "search"]
PAGES = ["home", "search", "product_detail", "checkout"]


def generate_sales_log(n=100):
    return [
        {
            "sale_id": f"S{random.randint(100000, 999999)}",
            "customer_id": f"C{random.randint(100, 999)}",
            "product_id": random.choice(PRODUCT_IDS),
            "region": random.choice(REGIONS),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(10, 100), 2),
            "timestamp": fake.date_time_this_year().isoformat(),
        }
        for _ in range(n)
    ]


def generate_user_activity_log(n=100):
    return [
        {
            "user_id": f"U{random.randint(100, 999)}",
            "action_type": random.choice(ACTIONS),
            "page": random.choice(PAGES),
            "device": random.choice(DEVICES),
            "timestamp": fake.date_time_this_year().isoformat(),
        }
        for _ in range(n)
    ]


def generate_inventory_events(n=100):
    return [
        {
            "product_id": random.choice(PRODUCT_IDS),
            "warehouse_id": f"W{random.randint(1, 20)}",
            "stock_level": random.randint(10, 200),
            "reorder_triggered": random.choice([True, False]),
            "timestamp": fake.date_time_this_year().isoformat(),
        }
        for _ in range(n)
    ]