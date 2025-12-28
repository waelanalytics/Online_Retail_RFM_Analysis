# Online_Retail_RFM_Analysis

# 🛒 Customer Segmentation & RFM Analysis (End-to-End)

![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-ETL-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Data%20Warehousing-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 📊 Project Overview
This project analyzes sales data from a UK-based online retailer to segment customers based on their purchasing behavior. I utilized **Python** for data cleaning (handling 400k+ records), **MySQL** for data warehousing, and **Power BI** for visualizing customer segments using the **RFM (Recency, Frequency, Monetary)** technique.

### 🎯 Key Objectives
*   **Data Cleaning:** Removing negative quantities (returns) and missing Customer IDs using Python.
*   **ETL Pipeline:** Automating data loading from CSV to MySQL using `mysql-connector`.
*   **Advanced Analysis:** Implementing **RFM Analysis** using SQL Views to classify customers.
*   **Visualization:** Using DAX in Power BI to create dynamic segments (VIP, Active, Lost).

---

## 📸 Dashboard Preview

![Dashboard Screenshot](dashboard_screenshot.png)

---

## 🧠 The RFM Logic (DAX & SQL)
I classified customers into 4 main segments:
1.  **VIP:** High spending (> $5,000) & Recent purchase (< 50 days).
2.  **Active:** Purchased within the last 30 days.
3.  **Lost:** Has not purchased in over 6 months (180 days).
4.  **Regular:** All other customers.

---

## 🛠️ Tech Stack

| Tool | Usage |
| :--- | :--- |
| **Python** | Data cleaning and handling large datasets (Pandas). |
| **MySQL** | Storing transaction logs and creating aggregated Views for RFM. |
| **Power BI** | Building the Scatter Plot and Treemaps for segmentation. |

---

## 👤 Author
**Wael Yousef**
*Data Analyst | Python | SQL | Power BI*

*   🌐 **Portfolio:** [waelanalytics.carrd.co](https://waelanalytics.carrd.co/)
*   💼 **LinkedIn:** [Wael Yousef](https://www.linkedin.com/in/wael-yousef-data-analyst/)
