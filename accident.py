import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'road_accidents_india.csv'
data = pd.read_csv(file_path)

# Title for the dashboard
st.title('Road Accidents in India')



# Interactive widgets
st.sidebar.title('Filters')

# Filter by State
selected_state = st.sidebar.selectbox('Select State', data['State'].unique())

# Filter by City
cities_by_state = data[data['State'] == selected_state]['City'].unique()
selected_city = st.sidebar.selectbox('Select City', cities_by_state)

# Filter by Fatalities and Injuries
fatalities_slider = st.sidebar.slider('Filter by Fatalities', min_value=1, max_value=max(data['Fatalities']), value=(1, max(data['Fatalities'])))
injuries_slider = st.sidebar.slider('Filter by Injuries', min_value=1, max_value=max(data['Injuries']), value=(1, max(data['Injuries'])))

# Filtered data based on selections
filtered_data = data[(data['State'] == selected_state) & (data['City'] == selected_city) &
                     (data['Fatalities'] >= fatalities_slider[0]) & (data['Fatalities'] <= fatalities_slider[1]) &
                     (data['Injuries'] >= injuries_slider[0]) & (data['Injuries'] <= injuries_slider[1])]

# Display the dataset on the sidebar
if st.sidebar.checkbox('Show Dataset'):
    st.write(data)

# Show filtered data
if st.sidebar.checkbox('Show Filtered Dataset'):
    st.info('Filtered Data')
    st.write(filtered_data)


# Visualization - Fatalities vs Injuries Scatter Plot
fig = px.scatter(filtered_data, x='Fatalities', y='Injuries', title='Fatalities vs Injuries')
st.plotly_chart(fig)


# Fatalities distribution histogram
fig, ax = plt.subplots()
sns.histplot(data=filtered_data, x='Fatalities', kde=True, bins=10, ax=ax)
plt.title('Fatalities Distribution')
st.pyplot(fig)