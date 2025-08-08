import pymongo
from simulate_logs import generate_sales_log, generate_user_activity_log, generate_inventory_events

mongo_uri = "mongodb+srv://AjaySreekumar47:<your-password>@big-data-etl.enmj4fc.mongodb.net/?retryWrites=true&w=majority&appName=Big-Data-ETL"
client = pymongo.MongoClient(mongo_uri)
db = client["enterprise_logs"]

sales_data = generate_sales_log(100)
activity_data = generate_user_activity_log(100)
inventory_data = generate_inventory_events(100)

db["sales_logs"].insert_many(sales_data)
db["user_activity_logs"].insert_many(activity_data)
db["inventory_events"].insert_many(inventory_data)

print("✅ All logs uploaded successfully.")