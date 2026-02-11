
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
##the line plot is drawn with plt.plot(df['cumulative'], df['order_id'], ...), 
# which plots the cumulative revenue on the x-axis and order_id on the y-axis. The assignment 
# specifies a plot of cumulative revenue versus order_id, 
# meaning order_id should be on the x-axis and cumulative revenue on the y-axis. 
# Consider swapping the axes in your plot call so the chart reflects the intended relationship.



plt.plot(df['order_id'], df['cumulative'], linestyle='--', color='red', linewidth=2)

plt.title("Cumulative Revenue vs Order ID", fontsize=14, fontweight='bold')
plt.xlabel("Order ID", fontsize=12)
plt.ylabel("Cumulative Revenue ($)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()

conn.close()