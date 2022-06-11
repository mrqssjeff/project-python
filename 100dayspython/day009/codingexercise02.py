travel_log = [
    {
        "country": "Sweden",
        "visits": 12,
        "cities": ["Malmo", "Stockholm", "Uppsala"]
    },
    {
        "country": "United States",
        "visits": 5,
        "cities": ["Charlotte", "Portland", "Seattle"]
    },
]


def add_new_country(countries_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = countries_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    country = visits = cities = ''
    for items in travel_log:
        for key in items:
            if key == "country":
                country = items[key]
            elif key == "visits":
                visits = items[key]
            elif key == "cities":
                cities = items[key]
        print(f"\nYou've visited {country} {visits} times")
        print(f"You've been to ", end="")
        for city in cities:
            print(f"{city}", end=" ")


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

