import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Завантаження даних
customers_data = pd.read_csv('customers.csv')
sales_data = pd.read_csv('sales.csv')
products_data = pd.read_csv('products.csv')
sellers_data = pd.read_csv('sellers.csv')

# 1. Розподіл клієнтів за локацією
plt.figure(figsize=(8, 6))
sns.countplot(x='Location', data=customers_data, hue='Location', palette='Set2', legend=False)
plt.title('Розподіл клієнтів за локацією')
plt.xlabel('Локація')
plt.ylabel('Кількість клієнтів')
plt.xticks(rotation=45)
for p in plt.gca().patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2, height, f'{int(height)}', ha="center", va="center")
plt.tight_layout()
plt.savefig('location_distribution.png')
plt.show()

# 2. Розподіл клієнтів за статтю
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=customers_data, hue='Gender', palette='pastel', legend=False)
plt.title('Розподіл клієнтів за статтю')
plt.xlabel('Стать')
plt.ylabel('Кількість клієнтів')
for p in plt.gca().patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2, height, f'{int(height)}', ha="center", va="center")
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.show()

# 3. Розподіл лояльності клієнтів
plt.figure(figsize=(8, 6))
sns.histplot(customers_data['LoyaltyScore'], kde=True, color='skyblue')
plt.title('Розподіл лояльності клієнтів')
plt.xlabel('Рівень лояльності')
plt.ylabel('Кількість клієнтів')
mean_loyalty = customers_data['LoyaltyScore'].mean()
plt.axvline(mean_loyalty, color='red', linestyle='--', label=f'Середнє значення: {mean_loyalty:.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('loyalty_distribution.png')
plt.show()

# 4. Динаміка сум продажів за датами
sales_data['SaleDate'] = pd.to_datetime(sales_data['SaleDate'])
sales_by_date = sales_data.groupby('SaleDate')['TotalAmount'].sum()
plt.figure(figsize=(19, 10))
plt.plot(sales_by_date.index, sales_by_date.values, marker='o', color='purple', label='Сума продажів')
plt.title('Динаміка сум продажів за датами')
plt.xlabel('Дата')
plt.ylabel('Сума продажів')
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
mean_sales = sales_by_date.mean()
min_sales = sales_by_date.min()
max_sales = sales_by_date.max()
plt.axhline(mean_sales, color='red', linestyle='--', label=f'Середнє значення: {mean_sales:.2f}')
plt.axhline(min_sales, color='blue', linestyle='--', label=f'Мінімум: {min_sales}')
plt.axhline(max_sales, color='green', linestyle='--', label=f'Максимум: {max_sales}')
plt.legend()
plt.tight_layout()
plt.savefig('sales_amount_by_date.png')
plt.show()

# 5. Сума продажів за категоріями продуктів
plt.figure(figsize=(8, 6))
category_sales = sales_data.merge(products_data, on='ProductID').groupby('Category')['TotalAmount'].sum()
colors = {
    'Аксесуари': 'dodgerblue',
    'Електроніка': 'orange',
    'Побутова техніка': 'green',
    'Інше': 'grey'  # Можна додати інші категорії тут
}
category_sales.plot(kind='bar', color=[colors.get(cat, 'grey') for cat in category_sales.index])
plt.title('Сума продажів за категоріями продуктів')
plt.xlabel('Категорія')
plt.ylabel('Сума продажів')
mean_category_sales = category_sales.mean()
min_category_sales = category_sales.min()
max_category_sales = category_sales.max()
plt.axhline(mean_category_sales, color='red', linestyle='--', label=f'Середнє значення: {mean_category_sales:.2f}')
plt.axhline(min_category_sales, color='blue', linestyle='--', label=f'Мінімум: {min_category_sales:.2f}')
plt.axhline(max_category_sales, color='green', linestyle='--', label=f'Максимум: {max_category_sales:.2f}')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('category_sales.png')
plt.show()

# 6. Сума продажів за продуктами
plt.figure(figsize=(12, 8))
product_sales = sales_data.groupby('ProductID')['TotalAmount'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar', color='orange')
plt.title('Сума продажів за продуктами')
plt.xlabel('Продукт')
plt.ylabel('Сума продажів')
mean_product_sales = product_sales.mean()
min_product_sales = product_sales.min()
max_product_sales = product_sales.max()
plt.axhline(mean_product_sales, color='red', linestyle='--', label=f'Середнє значення: {mean_product_sales:.2f}')
plt.axhline(min_product_sales, color='blue', linestyle='--', label=f'Мінімум: {min_product_sales}')
plt.axhline(max_product_sales, color='green', linestyle='--', label=f'Максимум: {max_product_sales}')
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('product_sales.png')
plt.show()

# 7. Сума продажів за продавцями
plt.figure(figsize=(12, 8))
seller_sales = sales_data.groupby('SellerID')['TotalAmount'].sum().sort_values(ascending=False)
seller_sales.plot(kind='bar', color='lightgreen')
plt.title('Сума продажів за продавцями')
plt.xlabel('Продавець')
plt.ylabel('Сума продажів')
mean_seller_sales = seller_sales.mean()
min_seller_sales = seller_sales.min()
max_seller_sales = seller_sales.max()
plt.axhline(mean_seller_sales, color='red', linestyle='--', label=f'Середнє значення: {mean_seller_sales:.2f}')
plt.axhline(min_seller_sales, color='blue', linestyle='--', label=f'Мінімум: {min_seller_sales}')
plt.axhline(max_seller_sales, color='green', linestyle='--', label=f'Максимум: {max_seller_sales}')
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('seller_sales.png')
plt.show()
