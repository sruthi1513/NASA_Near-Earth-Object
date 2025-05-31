#Count how many times each asteroid has approached Earth
query1 = """
SELECT neo_reference_id, COUNT(*) AS approach_count
FROM close_approach
GROUP BY neo_reference_id
ORDER BY approach_count DESC;
"""
#Average velocity of each asteroid over multiple approaches
query2 = """
SELECT neo_reference_id, AVG(relative_velocity_kmph) AS avg_velocity
FROM close_approach
GROUP BY neo_reference_id
ORDER BY avg_velocity DESC;
"""
#List top 10 fastest asteroids
query3 = """
SELECT id, name, MAX(relative_velocity_kmph) AS max_velocity
FROM asteroids a
JOIN close_approach c ON a.id = c.neo_reference_id
GROUP BY id, name
ORDER BY max_velocity DESC
LIMIT 10;
"""
#Find potentially hazardous asteroids that have approached Earth more than 3 times
query4 = """
SELECT id, name, COUNT(*) AS total_approaches
FROM asteroids a
JOIN close_approach c ON a.id = c.neo_reference_id
WHERE is_potentially_hazardous_asteroid = TRUE
GROUP BY id
HAVING total_approaches > 3
ORDER BY total_approaches DESC;
"""
#Find the month with the most asteroid approaches
query5 = """
SELECT MONTH(close_approach_date) AS approach_month, COUNT(*) AS approach_count
FROM close_approach
GROUP BY approach_month
ORDER BY approach_count DESC
LIMIT 1;
"""
#Get the asteroid with the fastest ever approach speed
query6 = """
SELECT a.name, MAX(ca.relative_velocity_kmph) AS max_speed
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
GROUP BY a.name
ORDER BY max_speed DESC
LIMIT 1;
"""
#Sort asteroids by maximum estimated diameter (descending)
query7 = """
SELECT name, estimated_diameter_max_km
FROM asteroids
ORDER BY estimated_diameter_max_km DESC;
"""
#An asteroid whose closest approach is getting nearer over time(Hint: Use ORDER BY close_approach_date and look at miss_distance). Select the asteroid with the most close approaches.
query8 = """
SELECT ca.neo_reference_id, a.name, ca.close_approach_date, ca.miss_distance_km
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE ca.neo_reference_id = (
    SELECT neo_reference_id
    FROM close_approach
    GROUP BY neo_reference_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY ca.close_approach_date ASC;
"""
#Display the name of each asteroid along with the date and miss distance of its closest approach to Earth.
query9 = """
SELECT a.name, ca.close_approach_date, ca.miss_distance_km
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE (a.id, ca.miss_distance_km) IN (
    SELECT neo_reference_id, MIN(miss_distance_km)
    FROM close_approach
    GROUP BY neo_reference_id
);
"""
#List names of asteroids that approached Earth with velocity > 50,000 km/h
query10 = """
SELECT DISTINCT a.name, ca.relative_velocity_kmph
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE ca.relative_velocity_kmph > 50000;
"""
#Count how many approaches happened per month
query11 = """
SELECT MONTH(close_approach_date) AS month, COUNT(*) AS approach_count
FROM close_approach
GROUP BY month
ORDER BY month;
"""
#Find asteroid with the highest brightness (lowest magnitude value)
query12 = """
SELECT name, absolute_magnitude_h
FROM asteroids
ORDER BY absolute_magnitude_h ASC
LIMIT 1;
"""
#Get number of hazardous vs non-hazardous asteroids
query13 = """
SELECT is_potentially_hazardous_asteroid, COUNT(*) AS count
FROM asteroids
GROUP BY is_potentially_hazardous_asteroid;
"""
#Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.
query14 = """
SELECT a.name, ca.close_approach_date, ca.miss_distance_lunar
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE ca.miss_distance_lunar < 1;
"""
#Find asteroids that came within 0.05 AU(astronomical distance)
query15 = """
SELECT a.name, ca.close_approach_date, ca.astronomical
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
WHERE ca.astronomical < 0.05;
"""
#How close hazardous asteroids come compared to non-hazardous
query16 = """
SELECT a.is_potentially_hazardous_asteroid,AVG(ca.miss_distance_km) AS avg_miss_distance_km
FROM close_approach ca
JOIN asteroids a ON ca.neo_reference_id = a.id
GROUP BY a.is_potentially_hazardous_asteroid;
"""
#Shows if asteroids approach faster in some months than others
query17="""
SELECT MONTH(close_approach_date) AS approach_month, AVG(relative_velocity_kmph) AS avg_velocity
FROM close_approach
GROUP BY approach_month
ORDER BY approach_month;
"""
#To see if asteroids are coming closer or farther away over month
query18="""
SELECT MONTH(close_approach_date) AS approach_month, AVG(miss_distance_km) AS avg_miss_distance_km
FROM close_approach
GROUP BY approach_month
ORDER BY approach_month;
"""
#Number of unique asteroids that have approached Earth per month
query19="""
SELECT MONTH(close_approach_date) AS month, COUNT(DISTINCT neo_reference_id) AS unique_asteroids
FROM close_approach
GROUP BY month
ORDER BY month;
"""
#Top 5 asteroids with the greatest variation in miss distance over approaches
query20="""
SELECT neo_reference_id, MAX(miss_distance_km) - MIN(miss_distance_km) AS miss_distance_range_km
FROM close_approach
GROUP BY neo_reference_id
ORDER BY miss_distance_range_km DESC
LIMIT 5;
"""
