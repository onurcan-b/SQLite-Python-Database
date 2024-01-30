import sqlite3
import math

connection = sqlite3.connect("parks.db")
connection.row_factory = sqlite3.Row 
cursor =  connection.cursor()

cursor.execute('SELECT name, id FROM parks WHERE id = ?', (1,))
cursor.execute("SELECT name FROM parks WHERE name LIKE 'W%';")
cursor.execute("SELECT name, address FROM parks WHERE address LIKE '%60637%';")
cursor.execute("SELECT parks.name, parks.address, park_times.close_time FROM parks, park_times WHERE park_times.close_time > 2100 and parks.id == park_times.id; ")
cursor.execute("SELECT name, address FROM parks WHERE tokens LIKE '%basketball%';")
cursor.execute("SELECT name, address, description FROM parks JOIN park_times ON parks.id == park_times.id WHERE park_times.open_time <= 0500 and parks.tokens LIKE '%basketball%' and park_times.day LIKE '%sat%';")

##### TESTING QUERIES MANUALLY FOR DEBUGGING ########
EARTH_R_MI = 3963
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on a sphere (like Earth) in miles.

    https://en.wikipedia.org/wiki/Haversine_formula

    :param lat1: latitude of first point
    :param lon1: longitude of first point
    :param lat2: latitude of second point
    :param lon2: longitude of second point

    :return: distance in miles
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    in_sqrt = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    distance = EARTH_R_MI * 2 * math.asin(math.sqrt(in_sqrt))

    return distance
connection.create_function("haversine_distance", 4, haversine_distance)
cursor.execute(" SELECT DISTINCT parks.name, parks.address, parks.description, parks.history, parks.url, park_times.day, park_times.open_time, park_times.close_time, haversine_distance(latitude, longitude, 41.8781, -87.6298) AS distance FROM parks JOIN park_times ON parks.id = park_times.park_id WHERE park_times.day = 'mon' AND park_times.open_time <= 1900 AND park_times.close_time >= 1900 AND distance <= 1;")
cursor.execute("SELECT DISTINCT parks.name, parks.address, parks.description, parks.history, parks.url, haversine_distance(latitude, longitude, ?, ?) AS distance FROM parks JOIN park_times ON parks.id = park_times.park_id WHERE parks.tokens LIKE ? AND distance <= ?;")
#######################################################

rows = cursor.fetchall()
for row in rows:
    print(dict(row), "\n")

connection.close()