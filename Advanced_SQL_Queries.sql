CREATE DATABASE Online_Retail_DB;
CREATE DATABASE InstaPay_Project;
CREATE DATABASE Egypt_Startups_DB;
CREATE DATABASE HR_Analytics_DB;

USE Online_Retail_DB;

-- إنشاء هيكل الجدول لاستقبال البيانات من بايثون
CREATE TABLE Transactions (
    InvoiceNo VARCHAR(50),
    StockCode VARCHAR(50),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10, 2),
    CustomerID VARCHAR(50),
    Country VARCHAR(50),
    TotalAmount DECIMAL(10, 2)
);

USE Online_Retail_DB;

-- استعراض قوة النسخة الجديدة باستخدام LAG و OVER
SELECT 
    Country, 
    SUM(TotalAmount) AS Current_Sales, 
    -- الدالة دي بتبص على السطر اللي فوق وتجيب الرقم بتاعه
    LAG(SUM(TotalAmount)) OVER (ORDER BY SUM(TotalAmount) DESC) AS Previous_Competitor_Sales,
    -- حساب الفرق بيني وبين اللي قبلي في الترتيب
    SUM(TotalAmount) - LAG(SUM(TotalAmount)) OVER (ORDER BY SUM(TotalAmount) DESC) AS Sales_Gap
FROM Transactions
GROUP BY Country
ORDER BY Current_Sales DESC
LIMIT 10;