import sqlite3
from .db import haversine_distance


def search_parks(params):
    """
    Search for parks based on the given parameters.

    Parameters
    ----------
    params : dict
        A dictionary of parameters to search for. The keys are the
        field names and the values are the values to search for.

        If a key is not present, it should not be used in the search.

        Keys:
            name: str
                If included, results should be filtered to only include parks that start with
                the provided string.  (Case-insensitive.)
            query_terms: list
                If included, a list of terms to search for in the park's description.
            zip_code: str
                If included, only parks with an address in the given zip code should be returned.
            open_at: tuple(str, str)
                If included, only parks that are open at the given time should be returned.

                A tuple of two strings, the first is the day of the week and the second is the
                time.  The day of the week will be "mon", "tue", "wed", "thu", "fri", "sat", or
                "sun".  The time will be a value between 0000 and 2359 representing a time.
            near: tuple(float, float, float)
                lat, lon, distance
                If included, only parks that are within the given distance (in miles) of the
                given latitude and longitude should be returned.

    Returns
    -------
    list
        A list of parks that match the given parameters.  Each park should be an instance of
        `sqlite.Row` with the appropriate fields (see "What attributes should be returned?"
         in the README).
    """
    connection = sqlite3.connect("./data/parks.db")
    connection.row_factory = sqlite3.Row
    connection.create_function("haversine_distance", 4, haversine_distance)
    cursor = connection.cursor()

    # Initialize the query partz
    select_statement = "SELECT DISTINCT parks.name, parks.address, parks.description, parks.history, parks.url"
    from_statement = " FROM parks JOIN park_times ON parks.id = park_times.park_id"
    where_clauses = []
    parameters = []

    # Append conditions to the WHERE clause based on the parameters provided
    if "near" in params:
        lat, lon, distance = params["near"]
        select_statement += (
            ", haversine_distance(latitude, longitude, ?, ?) AS distance"
        )
        where_clauses.append("distance <= ?")
        parameters.extend([lat, lon, distance])

    if "name" in params:
        where_clauses.append("LOWER(parks.name) LIKE LOWER(?)")
        parameters.append(params["name"] + "%")

    if "query_terms" in params:
        for term in params["query_terms"]:
            where_clauses.append("parks.tokens LIKE ?")
            parameters.append("% " + term + " %")

    if "zip_code" in params:
        where_clauses.append("parks.address LIKE ?")
        parameters.append("%" + params["zip_code"] + "%")

    if "open_at" in params:
        day, time = params["open_at"]
        select_statement += (
            ", park_times.day, park_times.open_time, park_times.close_time"
        )
        where_clauses.append(
            "park_times.day = ? AND park_times.open_time <= ? AND park_times.close_time >= ?"
        )
        parameters.extend([day, time, time])

    # Combine the query parts
    where_statement = " WHERE " + " AND ".join(where_clauses) if where_clauses else ""
    query = f"{select_statement}{from_statement}{where_statement};"

    # Execute the query
    cursor.execute(query, parameters)

    return cursor.fetchall()
