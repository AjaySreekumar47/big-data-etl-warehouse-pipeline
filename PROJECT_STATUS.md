# Project Status

This repository is a portfolio-scale data engineering and MLOps project. It combines completed notebook/script workflows with deployment templates for cloud MLOps.

## Implemented

- Synthetic enterprise log generation
- MongoDB Atlas ingestion workflow
- PySpark ETL from MongoDB-style collections
- Partitioned Parquet warehouse outputs
- Star-schema-style warehouse modeling
- SCD Type 1 and Type 2 product dimension modeling
- Spark SQL analytics query examples
- Vertex-compatible trainer script using Feast-style feature retrieval
- Trainer packaging with `setup.py`

## Prototype / Template Stage

- GitHub Actions workflow for triggering Cloud Build
- Cloud Build template for packaging and future Vertex AI job submission
- Vertex AI model training/deployment workflow
- Feast feature store integration

## Notes

Some cloud-specific components require user-specific infrastructure before execution:

- GCP project ID
- GCS bucket
- Vertex AI API enabled
- Cloud Build API enabled
- IAM service account permissions
- GitHub repository secret: `GCP_CREDENTIALS`
- Feast feature repository configuration

The repository is best interpreted as an end-to-end architecture and implementation template rather than a fully portable one-command production deployment.