import pandas as pd

# Load dataset
df = pd.read_excel("P1Dataset_Cleaned.xlsx")

print("="*50)
print("DATASET OVERVIEW")
print("="*50)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


print("\n" + "="*50)
print("NUMERICAL STATISTICS")
print("="*50)

print(df[['Quantity','UnitPrice','ItemsInCart','TotalPrice']].describe())


print("\n" + "="*50)
print("PRODUCT ANALYSIS")
print("="*50)

print(df['Product'].value_counts())


print("\n" + "="*50)
print("REVENUE BY PRODUCT")
print("="*50)

product_revenue = (
    df.groupby('Product')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
)

print(product_revenue)


print("\n" + "="*50)
print("ORDER STATUS")
print("="*50)

print(df['OrderStatus'].value_counts())


print("\n" + "="*50)
print("PAYMENT METHODS")
print("="*50)

print(df['PaymentMethod'].value_counts())


print("\n" + "="*50)
print("REFERRAL SOURCES")
print("="*50)

print(df['ReferralSource'].value_counts())


print("\n" + "="*50)
print("COUPON ANALYSIS")
print("="*50)

print(df['CouponCode'].value_counts())


print("\n" + "="*50)
print("OUTLIER DETECTION (TOTAL PRICE)")
print("="*50)

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[
    (df['TotalPrice'] < lower_bound)
    |
    (df['TotalPrice'] > upper_bound)
]

print("Q1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)

print("Lower Bound =", lower_bound)
print("Upper Bound =", upper_bound)

print("Number of Outliers =", len(outliers))

print("\n" + "="*50)
print("CORRELATION MATRIX")
print("="*50)

print(
    df[['Quantity','UnitPrice','ItemsInCart','TotalPrice']]
    .corr()
)

print("\n" + "="*50)
print("TOP 10 HIGHEST VALUE ORDERS")
print("="*50)

print(
    df[['OrderID','Product','TotalPrice']]
    .sort_values(by='TotalPrice', ascending=False)
    .head(10)
)

print("\nEDA COMPLETED SUCCESSFULLY")