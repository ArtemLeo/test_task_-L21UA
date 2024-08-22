import pandas as pd

# Завантаження файлів
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')
sellers_df = pd.read_csv('sellers.csv')

# Перегляд перших рядків кожного DataFrame
print("Customers Data:")
print(customers_df.head())
print("\nSales Data:")
print(sales_df.head())
print("\nProducts Data:")
print(products_df.head())
print("\nSellers Data:")
print(sellers_df.head())

# Перевірка загальної інформації
print("\nCustomers Data Info:")
print(customers_df.info())
print("\nSales Data Info:")
print(sales_df.info())
print("\nProducts Data Info:")
print(products_df.info())
print("\nSellers Data Info:")
print(sellers_df.info())

# Перевірка основних статистик
print("\nCustomers Data Statistics:")
print(customers_df.describe())
print("\nSales Data Statistics:")
print(sales_df.describe())
print("\nProducts Data Statistics:")
print(products_df.describe())
print("\nSellers Data Statistics:")
print(sellers_df.describe())

# Аналіз даних

# Клієнти
# Вік клієнтів
age_summary = customers_df['Age'].describe()
# Стать клієнтів
gender_distribution = customers_df['Gender'].value_counts()
# Місцезнаходження клієнтів
location_distribution = customers_df['Location'].value_counts()
# Оцінка лояльності
loyalty_score_summary = customers_df['LoyaltyScore'].describe()
# Дата реєстрації
registration_date_summary = customers_df['RegistrationDate'].describe()

print("\nCustomer Age Summary:")
print(age_summary)
print("\nCustomer Gender Distribution:")
print(gender_distribution)
print("\nCustomer Location Distribution:")
print(location_distribution)
print("\nCustomer Loyalty Score Summary:")
print(loyalty_score_summary)
print("\nCustomer Registration Date Summary:")
print(registration_date_summary)

# Продажі
# Кількість продажів
quantity_summary = sales_df['Quantity'].describe()
# Загальна сума продажів
total_amount_summary = sales_df['TotalAmount'].describe()
# Частота продажів за датами
sales_by_date = sales_df['SaleDate'].value_counts()
# Сума продажу за продуктом
sales_by_product = sales_df.groupby('ProductID')['TotalAmount'].sum()
# Сума продажу за продавцем
sales_by_seller = sales_df.groupby('SellerID')['TotalAmount'].sum()

print("\nSales Quantity Summary:")
print(quantity_summary)
print("\nTotal Sales Amount Summary:")
print(total_amount_summary)
print("\nSales by Date:")
print(sales_by_date)
print("\nSales by Product:")
print(sales_by_product)
print("\nSales by Seller:")
print(sales_by_seller)

# Товари
# Категорії товарів
category_distribution = products_df['Category'].value_counts()
# Ціна товарів
price_summary = products_df['Price'].describe()
# Кількість продуктів у кожній категорії
product_count_by_category = products_df['Category'].value_counts()

print("\nProduct Category Distribution:")
print(category_distribution)
print("\nProduct Price Summary:")
print(price_summary)
print("\nProduct Count by Category:")
print(product_count_by_category)

# Продавці
# Кількість продажів для кожного продавця
if 'SalesCount' in sellers_df.columns:
    sales_count_summary = sellers_df['SalesCount'].describe()
    # Загальна сума продажів для кожного продавця
    total_sales_amount_summary = sellers_df['TotalSalesAmount'].describe()
    print("\nSellers Sales Count Summary:")
    print(sales_count_summary)
    print("\nSellers Total Sales Amount Summary:")
    print(total_sales_amount_summary)
else:
    print("\nSellers data does not include 'SalesCount' or 'TotalSalesAmount' columns.")

# Збереження агрегованих даних для подальшої візуалізації
aggregated_data = {
    'Customer Age Summary': age_summary,
    'Customer Gender Distribution': gender_distribution,
    'Customer Location Distribution': location_distribution,
    'Customer Loyalty Score Summary': loyalty_score_summary,
    'Customer Registration Date Summary': registration_date_summary,
    'Sales Quantity Summary': quantity_summary,
    'Total Sales Amount Summary': total_amount_summary,
    'Sales by Date': sales_by_date,
    'Sales by Product': sales_by_product,
    'Sales by Seller': sales_by_seller,
    'Product Category Distribution': category_distribution,
    'Product Price Summary': price_summary,
    'Product Count by Category': product_count_by_category
}

# Збереження у CSV файли
for key, value in aggregated_data.items():
    if isinstance(value, pd.Series):
        value.to_csv(f'{key.replace(" ", "_").replace(":", "")}.csv')
    elif isinstance(value, pd.DataFrame):
        value.to_csv(f'{key.replace(" ", "_").replace(":", "")}.csv')

print("Aggregated data has been saved.")
