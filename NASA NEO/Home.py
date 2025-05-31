import streamlit as st
import pandas as pd
from Data_Loader import *
from datetime import date

st.set_page_config(page_title="NASA Asteroid Tracker", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🪐 Asteroid Approaches")
    menu = st.radio("", ["Filter Criteria", "Queries"])
st.markdown("### 🚀 **NASA Asteroid Tracker** :milky_way:")

# Filter Criteria 
if menu == "Filter Criteria":
    col1, col2 = st.columns(2)

    with col1:
        min_mag = st.slider("Min Magnitude", 13.8, 32.61, 13.8)

        dia_range = st.slider("Estimated Diameter Range (km)", 0.0, 10.33, (0.0, 5.0))
        min_dia, max_dia = dia_range

    with col2:
        vel_range = st.slider("Velocity Range (kmph)", 1418.21, 173071.83, (1418.21, 173071.83))
        astro_unit = st.slider("Astronomical Unit", 0.0, 0.5, 0.5)
        hazard_filter = st.selectbox("Potentially Hazardous?", ["No", "Yes"])
    start_date = st.date_input("Start Date", date(2024, 1, 1))
    end_date = st.date_input("End Date", date(2025, 4, 13))

    if st.button("Filter"):
        st.subheader("Filtered Asteroids")
        result = fetch_filtered_data(
            min_mag,
            min_dia,
            max_dia,
            vel_range[0],
            vel_range[1],
            astro_unit,
            hazard_filter,
            start_date,
            end_date
        )  
        if result:
            df = pd.DataFrame(result, columns=[
                "id", "name", "absolute_magnitude_h", "estimated_diameter_min_km",
                "estimated_diameter_max_km", "is_potentially_hazardous_asteroid",
                "close_approach_date", "relative_velocity_kmph", "astronomical"
            ])
            st.dataframe(df, use_container_width=True)
        else:
            st.error("🚫 No asteroids matched your filters. Try relaxing them slightly.")
            
# Queries
elif menu == "Queries": 
    st.subheader("Run Predefined Queries")

    queries = {
        "How many times each asteroid has approached Earth": fetch_query1,
        "Average velocity of each asteroid over multiple approaches": fetch_query2,
        "Top 10 Fastest Asteroids": fetch_query3,
        "Hazardous Asteroids (>3 Approaches)": fetch_query4,
        "Month with Most Approaches": fetch_query5,
        "Fastest Ever Approach": fetch_query6,
        "Asteroids by Max Diameter": fetch_query7,
        "Closest Misses Over Time (Most Frequent)": fetch_query8,
        "Closest Approach for Each Asteroid": fetch_query9,
        "Asteroids with Velocity > 50,000 km/h": fetch_query10,
        "Approaches per Month": fetch_query11,
        "Brightest Asteroid (Lowest Magnitude)": fetch_query12,
        "Hazardous vs Non-Hazardous Count": fetch_query13,
        "Asteroids Closer than Moon (< 1 LD)": fetch_query14,
        "Asteroids Within 0.05 AU": fetch_query15,
    	"Hazardous vs Non-Hazardous Asteroid Close Approach Distances": fetch_query16,
        "Monthly Variation in Asteroid Approach Speeds": fetch_query17,
        "Trend of Asteroid Miss Distances Over Months (Closer or Farther?)": fetch_query18,
        "Monthly Count of Unique Asteroids Approaching Earth": fetch_query19,
        "Top 5 Asteroids with Largest Variation in Close Approach Distances": fetch_query20,
    }

    selected_query = st.selectbox("Select a Query", list(queries.keys()))
    if st.button("Run Query"):
        result = queries[selected_query]()
        if result:
            df = pd.DataFrame(result)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No data returned from the query.")
