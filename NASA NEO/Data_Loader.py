import pymysql
from SQL_Query import *
def establish_connection():
    return pymysql.connect(host='127.0.0.1', user='root', passwd='Sruthi@666', db='Near_Earth_Objects',cursorclass=pymysql.cursors.DictCursor)
def fetch_query1():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query1)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query2():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query2)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query3():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query3)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query4():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query4)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query5():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query5)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query6():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query6)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query7():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query7)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query8():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query8)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query9():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query9)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query10():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query10)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query11():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query11)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query12():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query12)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query13():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query13)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query14():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query14)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query15():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query15)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query16():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query16)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query17():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query17)
    result = cursor.fetchall() 
    conn.close()
    return result
def fetch_query18():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query18)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query19():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query19)
    result = cursor.fetchall()  
    conn.close()
    return result
def fetch_query20():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute(query20)
    result = cursor.fetchall()  
    conn.close()
    return result
# Filter query with parameter placeholders
def fetch_filtered_data(
    min_mag,
    min_dia,
    max_dia,
    vel_min,
    vel_max,
    astro_unit,
    hazard_filter,
    start_date,
    end_date
):
    try:
        conn = establish_connection()
        cursor = conn.cursor()

        query = """
        SELECT 
            a.id, a.name, a.absolute_magnitude_h,
            a.estimated_diameter_min_km, a.estimated_diameter_max_km,
            a.is_potentially_hazardous_asteroid,
            ca.close_approach_date,
            ca.relative_velocity_kmph,
            ca.astronomical
        FROM asteroids a
        JOIN close_approach ca ON a.id = ca.neo_reference_id
        WHERE a.absolute_magnitude_h >= %s
          AND a.estimated_diameter_min_km >= %s
          AND a.estimated_diameter_max_km <= %s
          AND ca.relative_velocity_kmph BETWEEN %s AND %s
          AND ca.astronomical <= %s
          AND ca.close_approach_date BETWEEN %s AND %s
        """

        params = [
            float(min_mag),
            float(min_dia),
            float(max_dia),
            float(vel_min),
            float(vel_max),
            float(astro_unit),
            str(start_date),
            str(end_date)
        ]

        if hazard_filter == "Yes":
            query += " AND a.is_potentially_hazardous_asteroid = 1"

        # Debug
        print("Running SQL:", query)
        print("With Params:", params)

        cursor.execute(query, params)
        results = cursor.fetchall()
        return results

    except Exception as e:
        print("❌ Error:", e)
        return []

    finally:
        if 'conn' in locals():
            conn.close()