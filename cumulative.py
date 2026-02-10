
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt



#Task 2: A Line Plot with Pandas

conn = sqlite3.connect("./db/lesson.db")
cursor = conn.cursor()
querry = ( """
        SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id;

        """)


#create a DataFrame with the order_id and the total_price for each order
df = pd.read_sql_query(querry, conn)
#print(df)

#2.Add a "cumulative" column to the DataFrame.
def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)
#print(df)

#3.Use Pandas plotting to create a line plot of cumulative revenue vs. order_id.

plt.plot(df['cumulative'], df['order_id'], linestyle='--', color='red', linewidth=2)

plt.title("Cumulative Revenue", fontsize=14, fontweight='bold')
plt.xlabel(" Cumulative Revenue ($)", fontsize=12)
plt.ylabel("Order_id", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()

conn.close()