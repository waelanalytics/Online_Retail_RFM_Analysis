import pandas as pd
import mysql.connector

print("🚀 جاري قراءة ملف البيانات (قد يستغرق لحظات)...")
# قراءة الملف النظيف
df = pd.read_csv('cleaned_online_retail.csv')

# معالجة القيم الفارغة (NaN) لتصبح None ليفهمها SQL
df = df.where(pd.notnull(df), None)

print(f"📊 تم تحميل {len(df)} صف. جاري الاتصال بقاعدة البيانات...")

try:
    # الاتصال بـ MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="Online_Retail_DB"
    )
    cursor = conn.cursor()

    print("⚡ جاري إدخال البيانات... (هذه العملية قد تستغرق 5-10 دقائق، لكنها أضمن)")
    
    # جملة الإدخال
    sql = """INSERT INTO Transactions 
             (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country, TotalAmount) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # الدخول في حلقة لتخزين البيانات
    count = 0
    batch_size = 1000 # سنقوم بالحفظ كل 1000 صف
    
    for index, row in df.iterrows():
        val = (
            str(row['InvoiceNo']), 
            str(row['StockCode']), 
            str(row['Description']), 
            row['Quantity'], 
            row['InvoiceDate'], 
            row['UnitPrice'], 
            str(row['CustomerID']), 
            str(row['Country']), 
            row['TotalAmount']
        )
        cursor.execute(sql, val)
        count += 1
        
        # طباعة عداد كل 5000 صف لنعرف أن البرنامج يعمل
        if count % 5000 == 0:
            print(f"   ⏳ تم نقل {count} صف...")
            conn.commit() # حفظ جزئي

    conn.commit() # الحفظ النهائي
    print("-" * 30)
    print(f"✅ تمت العملية بنجاح! تم نقل {count} صف إلى قاعدة البيانات.")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"❌ حدث خطأ: {e}")