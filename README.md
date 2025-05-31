NASA Asteroid Tracker
----------------------
  A Streamlit app to explore Near Earth Object data fetched from NASA’s API and stored in a MySQL database.

Features:
  1. Fetches asteroid data via NASA API and stores in MySQL
  2. Filter asteroids by magnitude, size, velocity, date, and hazard status
  3. Run 20 predefined SQL queries for asteroid insights
  4. Interactive UI with filters and query results

Setup:
  1. Install Python packages: streamlit, pymysql, pandas, requests
  2. Use NASA API to populate the MySQL Near_Earth_Objects database
  3. Update MySQL connection info in Data_Loader.py
  4. Run the app:
         streamlit run Home.py

Data Extraction:
  The Near Earth Object data is fetched using NASA’s API in the near_earth_object.ipynb Jupyter notebook. This notebook handles:
    1. API requests to NASA’s Near Earth Object Web Service (NeoWs)
    2. Data extraction and transformation
    3. Loading cleaned data into the MySQL database
    4. Run this notebook first to populate your database before running the Streamlit app.

Structure:
  1. Data_Loader.py: DB connection and query execution
  2. SQL_Query.py: SQL query definitions
  3. Home.py: Streamlit app UI and logic
