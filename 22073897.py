import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame (Replace 'path/to/your/file.csv' with your file path)
file_path = r'C:/Users/heman/OneDrive/Desktop/varun_data.csv'  # Use raw string (r'...')
df = pd.read_csv(file_path)

# Display summary statistics
summary_stats = df.describe()
print(summary_stats)

# Data Visualization
fig, axs = plt.subplots(2, 2, figsize=(18, 12), facecolor='lightblue')  # Set the background color to light blue

# Line plot for CO2 emissions
line_plot, = axs[1, 1].plot(df['years'], df['World_co2'])
axs[1, 1].set_title('world trends over Time', color='black')
axs[1, 1].grid(True)  # Add grid
axs[1, 1].set_xlabel('Years')
axs[1, 1].set_ylabel('percentage/value')
axs[1, 1].legend([line_plot], ['World CO2 Emissions'])  # Add legend for the line plot

# Area plot for Agriculture land area with different line styles
area_plot = axs[0, 1].plot(df['years'], df['United_States_agricultureland'], label='United States', linestyle='-', marker='o')
area_plot += axs[0, 1].plot(df['years'], df['China_agricultureland'], label='China', linestyle='--', marker='s')
area_plot += axs[0, 1].plot(df['years'], df['India_agricultureland'], label='India', linestyle='-.', marker='^')
area_plot += axs[0, 1].plot(df['years'], df['Russian_agricultureland'], label='Russian Federation', linestyle=':', marker='D')
area_plot += axs[0, 1].plot(df['years'], df['World_agriculture'], label='World_agriculture', linestyle='-', marker='x')

axs[0, 1].set_title('Agriculture Land Area over Time', color='black')
axs[0, 1].legend(area_plot, ['United States_agricultureland', 'China_agricultureland', 'India_agricultureland', 'Russian Federation_agricultureland', 'World_agriculture'])  # Add legend for the area plot

# Donut chart for Agriculture land area by country
labels = ['United States', 'China', 'India', 'Russian Federation']
sizes = df.loc[df['years'] == 2020, ['United_States_agricultureland', 'China_agricultureland', 'India_agricultureland', 'Russian_agricultureland']].iloc[0]
colors = sns.color_palette('pastel')
# Use labels=None to remove default labels
axs[0, 0].pie(sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='black'))
# Create a separate legend with desired labels
axs[0, 0].legend(labels, loc='center left', bbox_to_anchor=(-0.2, 0.5))
axs[0, 0].set_title('Agriculture Land Area - Country Distribution (2020)', color='black')

# Comparison bar graph for CO2 emissions by countries with different colors and rotated x-axis labels
df_bar = df[df['years'] % 5 == 0]  # Filter data for every 5 years
bar_width = 0.35  # Width of each bar

bar_positions = np.arange(len(df_bar))  # Adjusted gap between bars

axs[1, 0].bar(bar_positions, df_bar['USA_co2'], width=bar_width, color='lightblue', label='USA')
axs[1, 0].bar(bar_positions + bar_width, df_bar['China_co2'], width=bar_width, color='lightgreen', label='China')
axs[1, 0].bar(bar_positions + 2 * bar_width, df_bar['Russian_Federation_co2'], width=bar_width, color='pink', label='Russian Federation')
axs[1, 0].bar(bar_positions + 3 * bar_width, df_bar['India_co2'], width=bar_width, color='orange', label='India')  # Add India bar plot
axs[1, 0].set_title(' Comparison of CO2 Emissions by Countries (1990 - 2020)', color='black')
axs[1, 0].set_xticks(bar_positions + 2 * bar_width)  # Set x-axis ticks at the center of each group of bars
axs[1, 0].set_xticklabels(df_bar['years'])  # Set x-axis labels
axs[1, 0].set_xlabel('Years')
axs[1, 0].set_ylabel('CO2 Emissions in million mertic tons')
axs[1, 0].legend(loc='upper left')  # Adjust the legend position
axs[1, 0].tick_params(rotation=45)

# Add the provided text at the bottom of the page
fig.text(0.5, 0.00, """
         The dashboard illustrates the dynamic patterns of climate change from 1990 to 2020, shedding light on the concurrent shifts in agriculture land.
Historically, the United States, India, and China have dominated agriculture land, but these patterns are evolving due to climate changes.
The documented increase in CO2 emissions underscores the rapid transformation in climate conditions, posing significant impacts on agriculture.
The fluctuations in agriculture land area are evident through the area plot, where each line style represents a different country. The graphs showing the story that how the climate change over time and effect agriculture land.
""", ha='center', fontsize=9, color='black', bbox=dict(facecolor='none', edgecolor='none'))

# Additional text in the bottom left corner in a box format
fig.text(0.08, 0.005, """
Name: Varun
Id.No: 22073897
""", ha='left', va='bottom', fontsize=12, color='black', bbox=dict(facecolor='lightpink', edgecolor='black', boxstyle='round,pad=0.5'))

# Add title with white background
fig.suptitle('Climate Change With other factors', fontsize=30, color='black', backgroundcolor='white', va='top')

plt.show()
