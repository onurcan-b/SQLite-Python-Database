from parks_search import search


def test_name_search():
    params = {"name": "washington"}
    parks = search.search_parks(params)
    assert len(parks) == 6


def test_name_search_no_results():
    params = {"name": "notapark"}
    parks = search.search_parks(params)
    assert len(parks) == 0


def test_query_terms_search():
    params = {"query_terms": ["pickle"]}
    parks = search.search_parks(params)
    if len(parks) == 3:
        raise AssertionError("'pickle' should not match 'pickleball'")
    assert len(parks) == 1


def test_query_terms_search_multiple():
    params = {"query_terms": ["basketball", "pool"]}
    parks = search.search_parks(params)
    assert len(parks) == 53


def test_zip_code_search():
    params = {"zip_code": "20001"}
    parks = search.search_parks(params)
    assert len(parks) == 0
    params = {"zip_code": "60637"}
    parks = search.search_parks(params)
    assert len(parks) == 14


def test_open_at_8am():
    params = {"open_at": ("mon", "0800")}
    parks = search.search_parks(params)
    assert len(parks) == 263


def test_open_at_2am():
    params = {"open_at": ("wed", "0200")}
    parks = search.search_parks(params)
    assert len(parks) == 7


def test_combined_search():
    params = {"query_terms": ["basketball", "pool"], "zip_code": "60618"}
    parks = search.search_parks(params)
    assert len(parks) == 3


def test_search_distance():
    # everything within 1 mile of a point
    params = {"near": (41.8781, -87.6298, 1)}
    parks = search.search_parks(params)
    assert len(parks) == 10


def test_combined_search2():
    params = {
        "query_terms": ["basketball", "pool"],
        "zip_code": "60618",
        "name": "Revere",
    }
    parks = search.search_parks(params)
    assert len(parks) == 1


def test_combined_search_with_open_at():
    params = {
        "query_terms": ["basketball", "pool"],
        "zip_code": "60618",
        "name": "Revere",
        "open_at": ("mon", "0900"),
    }
    parks = search.search_parks(params)
    assert len(parks) == 1


def test_combined_search_with_distance():
    params = {"query_terms": ["lake"], "near": (41.8781, -87.6298, 1)}
    parks = search.search_parks(params)
    assert len(parks) == 2


def test_combined_search_with_distance_and_open_at():
    params = {
        "query_terms": ["lake"],
        "near": (41.8781, -87.6298, 1),
        "open_at": ("mon", "1900"),
    }
    parks = search.search_parks(params)
    assert len(parks) == 1


def test_fields_basic_search():
    params = {"zip_code": "60637"}
    parks = search.search_parks(params)
    assert set(parks[0].keys()) == {
        "name",
        "description",
        "history",
        "address",
        "url",
    }


def test_fields_near_search():
    params = {
        "near": (41.8781, -87.6298, 1),
    }
    parks = search.search_parks(params)
    assert set(parks[0].keys()) == {
        "name",
        "description",
        "history",
        "address",
        "url",
        "distance",
    }


def test_fields_open_at_search():
    params = {
        "open_at": ("mon", "1900"),
    }
    parks = search.search_parks(params)
    assert set(parks[0].keys()) == {
        "name",
        "description",
        "history",
        "address",
        "url",
        "day",
        "open_time",
        "close_time",
    }


def test_fields_all():
    params = {
        "open_at": ("mon", "1900"),
        "near": (41.8781, -87.6298, 1),
    }
    parks = search.search_parks(params)
    assert set(parks[0].keys()) == {
        "name",
        "description",
        "history",
        "address",
        "url",
        "day",
        "open_time",
        "close_time",
        "distance",
    }
