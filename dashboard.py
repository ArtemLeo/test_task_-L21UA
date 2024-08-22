import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib.dates

# Завантаження даних
customers_data = pd.read_csv('customers.csv')
sales_data = pd.read_csv('sales.csv')
products_data = pd.read_csv('products.csv')
sellers_data = pd.read_csv('sellers.csv')

# 1. Розподіл клієнтів за локацією
plt.figure(figsize=(8, 6))
sns.countplot(x='Location', data=customers_data)
plt.title('Розподіл клієнтів за локацією')
plt.xlabel('Локація')
plt.ylabel('Кількість клієнтів')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('location_distribution.png')
plt.show()

# 2. Розподіл клієнтів за статтю
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=customers_data)
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
sales_data['SaleDate'] = pd.to_datetime(sales_data['SaleDate'])  # Перетворення стовпця SaleDate у тип datetime
sales_by_date = sales_data['SaleDate'].value_counts().sort_index()

plt.figure(figsize=(14, 8))  # Збільшення розміру графіка
plt.bar(sales_by_date.index, sales_by_date.values, color='green', width=0.6)  # Зменшення ширини стовпців

plt.title('Динаміка продажів за датами')
plt.xlabel('Дата')
plt.ylabel('Кількість продажів')

# Форматування осі X для зменшення щільності відміток
plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=5))  # Відмітки кожні 5 днів
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('sales_by_date.png')
plt.show()

# 5. Розподіл продажів за категоріями продуктів
plt.figure(figsize=(8, 6))
sns.countplot(x='Category', data=products_data)
plt.title('Розподіл продажів за категоріями продуктів')
plt.xlabel('Категорія')
plt.ylabel('Кількість продуктів')
plt.tight_layout()
plt.savefig('category_distribution.png')
plt.show()
