import pandas as pd
import sqlite3
import matplotlib.pyplot as plt



#Task 1: Plotting with Pandas

#2.Load a DataFrame called employee_results using SQL
 
with sqlite3.connect("./db/lesson.db") as conn:

    conn.execute("PRAGMA foreign_keys = 1")
        
    cursor = conn.cursor()

    emp_result_query = ("""
                    SELECT last_name, SUM(price * quantity) AS revenue FROM employees e 
                    JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id 
                    JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
                     """)
    employee_result = pd.read_sql_query(emp_result_query, conn)
    #print(employee_result)



#Use the Pandas plotting functionality to create a bar chart where the x axis is the employee 
# last name and the y axis is the revenue.

plt.bar(employee_result['last_name'], employee_result['revenue'], width=0.5, edgecolor='black')
plt.title("Revenue by Employee", fontsize=14, fontweight='bold')
plt.xlabel("Employee Last name", fontsize=12)

plt.xticks(rotation=45, ha='right', fontsize=9)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
