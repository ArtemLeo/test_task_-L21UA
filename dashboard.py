import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Завантаження даних
customers_data = pd.read_csv('customers.csv')
sales_data = pd.read_csv('sales.csv')
products_data = pd.read_csv('products.csv')
sellers_data = pd.read_csv('sellers.csv')

# 1. Розподіл клієнтів за локацією
plt.figure(figsize=(8, 6))
sns.countplot(x='Location', data=customers_data, hue='Location', palette='viridis', legend=False)
plt.title('Розподіл клієнтів за локацією')
plt.xlabel('Локація')
plt.ylabel('Кількість клієнтів')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('location_distribution.png')
plt.show()

# 2. Розподіл клієнтів за статтю
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=customers_data, hue='Gender', palette='coolwarm', legend=False)
plt.title('Розподіл клієнтів за статтю')
plt.xlabel('Стать')
plt.ylabel('Кількість клієнтів')
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.show()

# 3. Розподіл лояльності клієнтів
plt.figure(figsize=(8, 6))
sns.histplot(customers_data['LoyaltyScore'], kde=True, color='teal')
plt.title('Розподіл лояльності клієнтів')
plt.xlabel('Рівень лояльності')
plt.ylabel('Кількість клієнтів')
plt.tight_layout()
plt.savefig('loyalty_distribution.png')
plt.show()

# 4. Динаміка продажів за датами
sales_by_date = sales_data['SaleDate'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sales_by_date.plot(kind='bar', color='coral')
plt.title('Динаміка продажів за датами')
plt.xlabel('Дата')
plt.ylabel('Кількість продажів')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_date.png')
plt.show()

# 5. Розподіл продажів за категоріями продуктів
plt.figure(figsize=(8, 6))
sns.countplot(x='Category', data=products_data, hue='Category', palette='pastel', legend=False)
plt.title('Розподіл продажів за категоріями продуктів')
plt.xlabel('Категорія')
plt.ylabel('Кількість продуктів')
plt.tight_layout()
plt.savefig('category_distribution.png')
plt.show()
