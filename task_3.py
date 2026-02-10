
#Task 3: Interactive Visualizations with Plotly

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

#Print the first and last 10 lines of the DataFrame.
print(df.head(10))
print(df.tail(10))

#2.Clean the data. You need to convert the 'strength' column to a float. 
# Use of str.replace() with regex is one way to do this, followed by type conversion.
df['strength']= df['strength'].str.replace(r"[^\d.]", "", regex=True).astype(float)

print(df.head())
print(df.tail())

#3.Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.

fig = px.scatter(df, x="strength", y="frequency", color="direction", title="Wind Strength vs Frequency " \
"by Direction")

fig.write_html("wind.html")

# Show plot
fig.show()
