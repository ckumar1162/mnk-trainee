my_dictionary = {
    "key1": ["List"],
    "key2": "Value",
}
print(my_dictionary)

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][0])
travel_log["nested_list"] = ["A", "B", ["C", "D"]]
print(travel_log["nested_list"][2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["France"]["cities_visited"])
print(travel_log["France"]["cities_visited"][1])
print(travel_log["France"]["total_visits"])
