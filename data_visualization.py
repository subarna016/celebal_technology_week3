import matplotlib.pyplot as plt

# Data
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']
populations = [1439323776, 1380004385, 331002651, 273523615, 220892340, 212559417, 206139589, 164689383, 145934462, 128932753]

# Create bar chart
plt.figure(figsize=(10, 5))
plt.bar(countries, populations)

# Add title and labels
plt.title('Population of Different Countries')
plt.xlabel('Country')
plt.ylabel('Population')

# Show the plot
plt.show()