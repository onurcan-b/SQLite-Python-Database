import math


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
    in_sqrt = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    )
    distance = EARTH_R_MI * 2 * math.asin(math.sqrt(in_sqrt))

    return distance
