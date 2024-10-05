import streamlit as st
import pandas as pd

# Initial data
categories = ['Meat', 'Eggs and Milk', 'Fruits and Veggies', 'Drinks', 'Other']
avg_prices = [20, 10, 10, 25, 15]
amount_spent = [0] * len(categories)

# Title of the app
st.title("Grocery Store Budget")

# Editable inputs for the "Amount Spent" column
st.write("Enter the amount spent:")

# Store user inputs in a list
for i in range(len(categories)):
    amount_spent[i] = st.number_input(f"Amount spent on {categories[i]}", min_value=0.0, value=0.0, step=1.0)

# Create a DataFrame with the user inputs
df = pd.DataFrame({
    'Category': categories,
    'Average Price ($)': avg_prices,
    'Amount Spent ($)': amount_spent,
})

# Calculate the absolute difference between 'Average Price' and 'Amount Spent'
df['Difference ($)'] = (df['Average Price ($)'] - df['Amount Spent ($)'])

# Display the updated dataframe
st.write("Updated Grocery Budget")
st.dataframe(df)

# Display total difference
total_diff = df['Difference ($)'].sum()
st.write(f"Total Difference: ${total_diff:.2f}")
