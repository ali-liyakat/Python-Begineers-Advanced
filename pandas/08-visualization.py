import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.DataFrame({
    'Quarter': ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 'Q1 2023'],
    'Fridge': [12.5, 11, 13.2, 16.4, 13.8],
    'Dishwasher': [8.0, 7.0, 9.0, 11.0, 9.5],
    'Washing Machine': [9.2, 8.5, 7.5, 7.6, 6.8]
})
print(df_sales)

# line chart

plt.figure(figsize=(10, 10))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="green", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="brown", label="Washing Machine")
plt.title("Product Sales")
plt.xlabel("Revenue")
plt.ylabel("Quarter")
plt.legend()
plt.show()


total_sales = df_sales[["Fridge", "Dishwasher", "Washing Machine"]].sum()
print(total_sales)


# pie charts

plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%", explode=(0.1,0,0), shadow=True, startangle=120)
plt.show()


# bar chart
df_sales.plot(kind='bar', x='Quarter')
plt.xticks(rotation=45)
plt.show()

df_sales2 = df_sales.set_index("Quarter")
print(df_sales2)

df_sales2.plot(kind='bar')
plt.xticks(rotation=45)
plt.show()

df_score = pd.DataFrame({
    'Name': ["Ali","Mohd", "Abass","Alam","Fahad","Thasin"],
    'Score': [90, 76, 58, 85, 49, 89]
})
print(df_score)

# Histogram

plt.hist(df_score["Score"])
plt.show()


# using seaborn
import seaborn as sns

sns.histplot(df_score["Score"], kde=True)
plt.show()

# scatter plot
df3 = pd.DataFrame({
    'area':[400, 650, 700, 340, 560, 250, 600, 120, 450, 800],
    'price': [80, 70, 40, 120, 90, 85, 79, 55, 40, 110]
})

sns.scatterplot(data=df3, x="area", y="price")
plt.show()