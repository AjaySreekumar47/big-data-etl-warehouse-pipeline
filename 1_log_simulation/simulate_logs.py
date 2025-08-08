from faker import Faker
import random

fake = Faker()

def generate_sales_log(n=100):
    return [{
        "sale_id": f"S{random.randint(100000, 999999)}",
        "customer_id": f"C{random.randint(100, 999)}",
        "product_id": f"P{random.randint(100, 999)}",
        "region": random.choice(["North", "South", "East", "West"]),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 100), 2),
        "timestamp": fake.date_time_this_year().isoformat()
    } for _ in range(n)]

def generate_user_activity_log(n=100):
    return [{
        "user_id": f"U{random.randint(100, 999)}",
        "action_type": random.choice(["click", "scroll", "purchase", "search"]),
        "page": random.choice(["home", "search", "product_detail", "checkout"]),
        "device": random.choice(["mobile", "desktop", "tablet"]),
        "timestamp": fake.date_time_this_year().isoformat()
    } for _ in range(n)]

def generate_inventory_events(n=100):
    return [{
        "product_id": f"P{random.randint(100, 999)}",
        "warehouse_id": f"W{random.randint(1, 20)}",
        "stock_level": random.randint(10, 200),
        "reorder_triggered": random.choice([True, False]),
        "timestamp": fake.date_time_this_year().isoformat()
    } for _ in range(n)]