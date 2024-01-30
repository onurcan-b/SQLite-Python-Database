import pytest
from parks_search.db import haversine_distance

# Testing Tips:
#  1) Remember, test functions must start with `test_` and have unique names.
#  2) Consider using `parametrize` as shown in notes.
#  3) Feel free to use these global variables as part of your testing.

cities = {
    "chicago": (41.8781, -87.6298),
    "cleveland": (41.5054, -81.6812),
    "nyc": (40.7128, -74.0060),
    "perth": (-31.953512, 115.857048),
    "quito": (0, -78.507751),  # latitude adjusted for testing
    "london": (51.509865, 0),  # longitude adjusted
}
distances = {
    "nyc": 711.7919194238542,
    "cleveland": 308.2599506721036,
    "perth": 10987.868273695185,
    "quito": 2952.071278779637,
    "london": 3956.5809365514624,
}

def test_haversine():
        chicago_lat, chicago_lon = cities["chicago"]
        target_lat, target_lon = cities["nyc"]
        assert(haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) < distances["nyc"] + .1 or
               haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) > distances["nyc"] - .1 )
        
def test_haversine_cleveland():
        chicago_lat, chicago_lon = cities["chicago"]
        target_lat, target_lon = cities["cleveland"]
        assert(haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) < distances["cleveland"] + .1 or
               haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) > distances["cleveland"] - .1 )
        
def test_haversine_perth():
        chicago_lat, chicago_lon = cities["chicago"]
        target_lat, target_lon = cities["perth"]
        assert(haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) < distances["perth"] + .1 or
               haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) > distances["perth"] - .1 )
        
def test_haversine_quito():
        chicago_lat, chicago_lon = cities["chicago"]
        target_lat, target_lon = cities["quito"]
        assert(haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) < distances["quito"] + .1 or
               haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) > distances["quito"] - .1 )
        
def test_haversine_london():
        chicago_lat, chicago_lon = cities["chicago"]
        target_lat, target_lon = cities["london"]
        assert(haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) < distances["london"] + .1 or
               haversine_distance(chicago_lat, chicago_lon, target_lat, target_lon) > distances["london"] - .1 )        

# Why These?
# Name your tests in a way where a failure instantly alerts you to what might be wrong.
#
# test_haversine_perth is not as meaningful as test_haversine_opposite_side_of_planet.
# Perth is chosen explicitly because it is on the "opposite quadrant" of the world,
# which might hide an interesting bug.
#
# Why are Quito and London chosen? Name those tests accordingly.
