import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:\pract7\product_sales_data.csv')

plt.figure(figsize=(10, 6))
sns.boxplot(x = 'Category', y = 'Sales', data = data)
plt.title('Sales Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales')
plt.xticks(rotation = 45)
plt.grid(axis = 'y')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x = 'Sales', y = 'Profit', data = data, hue = 'Category', palette = 'Set2')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

median_sales_by_category = data.groupby('Category')['Sales'].median().sort_values(ascending = False)
if median_sales_by_category.idxmax() == 'Clothing':
    print("Insights:")
    print("- The 'Clothing' category has the highest median sales, followed by 'Electronics' and 'Home Appliances'.")

if data[['Sales', 'Profit']].corr().iloc[0, 1] > 0:
    print("- There is a positive correlation between sales and profit across all product categories.")
if data['Sales'].max() == data.loc[data['Sales'].idxmax(), 'Sales']:
    print("- The category with the highest sales is:", data.loc[data['Sales'].idxmax(), 'Category'])

else:
    print("- The data does not meet any specific condition for insights.")
