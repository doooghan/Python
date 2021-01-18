cities = {
    "xian": {
        "country": "china",
        "population": "2kw",
        "fact": "rou jia mo",
    },

    "beijing": {
        "country": "china",
        "population": "3kw",
        "fact": "gu gong",
    },

    "New York": {
        "country": "USA",
        "population": "3kw",
        "fact": "big city"
    },
}

for city, message in cities.items():
    # print(city)
    print(city + " is a big city, its country is " + message["country"] +
          ", it has a population of " + message['population'] +
          " and its specialty is " + message["fact"])
