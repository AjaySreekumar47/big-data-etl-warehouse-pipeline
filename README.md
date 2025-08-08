# 🏭 Big Data ETL & Warehouse Modeling Pipeline

This project simulates a complete **enterprise-scale data pipeline** that ingests synthetic transactional logs, processes them using **PySpark**, models a **star schema warehouse** with **SCD dimension logic**, and performs **real-time ML deployment** using **Vertex AI**. All components are developed in **Google Colab** and leverage cloud-scale tools such as **MongoDB Atlas**, **Google Cloud Storage**, and **Vertex AI Pipelines**.

---

## 🔍 Project Highlights

### 1. 🔄 Synthetic Log Simulation
- Log types: `sales_logs`, `user_activity_logs`, `inventory_events`
- Generated using the `Faker` library
- Structured in JSON-like format for downstream NoSQL ingestion

### 2. ☁️ MongoDB Atlas Ingestion
- Logs are inserted into cloud-hosted **MongoDB Atlas**
- Collections are auto-created on insert
- Enables distributed NoSQL-backed ETL workflows

### 3. ⚙️ PySpark-Based ETL
- Logs extracted via **MongoDB Spark Connector**
- Cleaned, transformed, and stored as **partitioned Parquet files**
- Partitioning strategies:
  - Sales → by `region`
  - Activity → by `device`
  - Inventory → by `warehouse_id`

### 4. 🧱 Data Warehouse Modeling
- **Star Schema** architecture
- Tables:
  - `fact_sales`: transactional metrics
  - `dim_customer`, `dim_product`, `dim_region`, `dim_time`: surrogate keys
- **SCD Type 1 & Type 2** logic implemented on `dim_product`

### 5. 📊 SQL Analytics Layer
- Queries run via **Spark SQL temp views**
- KPIs:
  - Monthly revenue trends
  - Top products by revenue
  - Product-category performance

### 6. 🤖 Vertex AI ML Pipeline
- Trains a **regression recommender model**
- Saves and deploys using:
  - `joblib` for serialization
  - Google Cloud Storage for artifact storage
  - Vertex AI for model hosting
- Includes full CI/CD automation with:
  - GitHub Actions
  - Cloud Build
  - Conditional deployment via **Kubeflow Pipelines**

---

## 📁 Folder Structure

```

big\_data\_etl\_project/
├── 1\_log\_simulation/
│   └── simulate\_logs.py
├── 2\_mongo\_ingestion/
│   └── upload\_to\_mongo.py
├── 3\_pyspark\_etl/
│   ├── sales\_etl.py
│   ├── user\_activity\_etl.py
│   └── inventory\_etl.py
├── 4\_data\_warehouse/
│   └── warehouse/
│       ├── sales\_logs/
│       ├── user\_activity\_logs/
│       ├── inventory\_events/
│       └── fact\_sales\_enriched/
├── 5\_scd\_dimension\_modeling/
│   ├── dim\_product\_scd1.py
│   ├── dim\_product\_scd2.py
│   ├── product\_master.csv
│   └── dim\_product\_history.csv
├── 6\_analytics/
│   ├── query\_revenue\_by\_category.sql
│   ├── query\_top\_products.sql
│   └── query\_by\_region.sql
├── 7\_vertex\_ai\_ml\_pipeline/
│   ├── model/
│   │   └── model.joblib
│   ├── trainer/
│   │   ├── task.py
│   │   └── setup.py
│   └── .github/
│       └── workflows/
│           └── train\_and\_deploy.yml
├── notebooks/
│   └── etl\_pipeline\_colab.ipynb
└── README.md

```

---

## 🚀 Technologies Used

| Tool / Framework      | Role                                    |
|-----------------------|------------------------------------------|
| PySpark               | Distributed ETL and SQL queries          |
| MongoDB Atlas         | NoSQL ingestion of simulated logs        |
| Google Colab          | Interactive development + testing        |
| Google Drive          | Storage for partitioned Parquet files    |
| Google Cloud Storage  | Model artifact storage                   |
| Vertex AI             | Model deployment and endpoint serving    |
| Feast                 | Feature Store integration (ML pipelines) |
| GitHub Actions        | CI/CD automation                         |
| Cloud Build           | Trigger pipeline builds from GitHub      |

---

## 🧠 Skills Demonstrated

- 🔧 Data engineering (ETL, partitioning, PySpark)
- 🏗️ Warehouse modeling (star schema, SCD1 & SCD2)
- 🧮 Spark SQL for OLAP-style queries
- ☁️ End-to-end MLOps on Google Cloud
- 📦 CI/CD with GitHub Actions and Cloud Build
- 📊 Business insight generation from transactional data

---

## 👨‍💻 Author

**Ajay Sreekumar**  
AI Research Engineer | Data Science | MLOps  
🔗 [LinkedIn](https://www.linkedin.com/in/ajay-sreekumar-nmims/) | 🧠 [Projects Portfolio](https://ajaysreekumar47.github.io/)  
