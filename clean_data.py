import pandas as pd

print("🚀 جاري تحميل البيانات للتنظيف...")
# قراءة ملف الإكسيل
df = pd.read_excel('online_retail.xlsx')

print(f"📊 عدد الصفوف قبل التنظيف: {len(df)}")

# 1. حذف القيم المفقودة في CustomerID
# (لأننا لا نستطيع تحليل سلوك عميل مجهول)
df.dropna(subset=['CustomerID'], inplace=True)

# 2. حذف الكميات السالبة (المرتجعات) والأسعار الصفرية
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# 3. تحويل CustomerID من رقم عشري إلى نص (لأنه هوية وليس رقماً للحساب)
df['CustomerID'] = df['CustomerID'].astype(int).astype(str)

# 4. هندسة البيانات (Feature Engineering): حساب إجمالي الفاتورة
# المعادلة: الكمية * السعر = الإجمالي
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# 5. تحويل التاريخ إلى صيغة نظيفة (DateTime)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

print(f"✅ عدد الصفوف بعد التنظيف: {len(df)}")
print("-" * 30)
print("عينة من البيانات النظيفة:")
print(df.head())

# حفظ الملف نظيفاً بصيغة CSV (أخف وأسرع للـ MySQL)
output_file = 'cleaned_online_retail.csv'
df.to_csv(output_file, index=False)
print(f"💾 تم حفظ الملف النظيف باسم: {output_file}")