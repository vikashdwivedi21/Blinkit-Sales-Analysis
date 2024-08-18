# Blinkit Sales Analysis Dashboard

## Overview
This project presents a comprehensive sales analysis dashboard for Blinkit, created using Power BI. The dashboard provides valuable insights into various sales metrics, helping to drive strategic decision-making and optimize business performance.

## Features
- **Total Sales**: Displays the total sales amount, which is $383.9K.
- **Number of Orders**: Shows the total number of orders, which is 2K.
- **Average Order Value**: Indicates the average value per order, which is $141.
- **Sales Over Time**: A line chart tracking total sales over a specified period.
- **Item Type Contribution**: Pie charts representing the contribution of different item types to total sales, with 'Fruits & Vegetables' having the largest share at $133.4K.
- **Top Items by Sale**: Bar charts showing the top-selling items.
- **Outlet Details**: Information on outlet establishment year and location.
- **Additional Metrics**: KPI cards displaying metrics like average basket size.

## Data Cleaning Process
1. **Import Libraries**: Use Python libraries such as Pandas and NumPy for data manipulation.
2. **Load Data**: Load the dataset into a Pandas DataFrame.
3. **Handle Missing Values**: Identify and fill or drop missing values.
4. **Remove Duplicates**: Check for and remove duplicate records.
5. **Data Transformation**: Convert data types, normalize data, and handle outliers.
6. **Export Cleaned Data**: Save the cleaned dataset to a CSV file.

## Storing Data in PostgreSQL
1. **Install psycopg2**: Install the PostgreSQL adapter for Python.
2. **Connect to PostgreSQL**: Establish a connection to the PostgreSQL server.
3. **Create Table**: Create a table to store the cleaned data.
4. **Insert Data**: Insert the cleaned data into the PostgreSQL table.

## Connecting to Power BI
1. **Connect to PostgreSQL**: Use Power BI's PostgreSQL connector to connect to the database.
2. **Load Data**: Load the data from the PostgreSQL table into Power BI.
3. **Create Visualizations**: Use Power BI to create interactive visualizations and dashboards.

## How to Use
1. **Open the Dashboard**: Load the Power BI file to view the dashboard.
2. **Interact with Visuals**: Use the interactive elements to filter and drill down into specific data points.
3. **Analyze Trends**: Utilize the visualizations to identify trends and insights in the sales data.

## Insights
- **Top-Selling Categories**: Fruits & Vegetables are the highest contributors to total sales.
- **Sales Trends**: The line chart helps in understanding the sales trends over time.
- **Outlet Performance**: Analyze the performance of different outlets based on their establishment year and location.

## Screenshot


## Conclusion
This dashboard is designed to provide a clear and concise view of Blinkit's sales performance, enabling better decision-making and strategic planning.
