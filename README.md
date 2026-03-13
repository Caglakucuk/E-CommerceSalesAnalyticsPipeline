# 📊 E-Commerce Data Pipeline & Sales Analytics

### 📌 Project Overview
This project builds an end-to-end data pipeline to analyze e-commerce sales data.
Raw CSV datasets are processed using Python ETL, transformed into a star schema data warehouse in PostgreSQL, and visualized through Tableau dashboards for business insights.
The goal of the project is to simulate a real-world Business Intelligence workflow, including data ingestion, transformation, data modeling, and visualization.


### 🛠 Tech Stack
Python – Data extraction and transformation
Pandas – Data manipulation
PostgreSQL – Data warehouse
SQLAlchemy – Database connection
Tableau – Data visualization
Git & GitHub – Version control


### 🏗 Data Architecture
The pipeline follows a modern BI workflow:

Raw CSV Data

      ↓
      
Python ETL Pipeline

      ↓
      
PostgreSQL Data Warehouse

      ↓
      
Star Schema Modeling

      ↓
      
Tableau Dashboards


### ⭐ Data Model (Star Schema)

The data warehouse is designed using a Star Schema.
#### Fact Table

fact_sales

#### Dimension Tables

dim_customer
dim_product
dim_seller
dim_date

### 🔄 ETL Pipeline
The ETL process performs the following steps:

#### Extract
Data is loaded from raw CSV files.

Example datasets:
orders
order_items
customers
products
sellers

#### Transform
Data cleaning
Column selection
Table joins
Date dimension creation
Star schema transformation

#### Load
Processed data is loaded into PostgreSQL tables using SQLAlchemy.

### 📚 Dataset

Dataset used in this project:

Brazilian E-Commerce Public Dataset by Olist

It contains information about:

orders
products
sellers
customers
payments
reviews

