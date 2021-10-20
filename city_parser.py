#!/usr/bin/env python

import json
import requests
import cred_parser


def get_cities(api_keys, state_code):
    api_url = f"https://parseapi.back4app.com/classes/Usabystate_{state_code}?count=1&limit=10000"

    headers = {
        "X-Parse-Application-Id": api_keys[
            "application_id"
        ],  # This is your app's application id
        "X-Parse-REST-API-Key": api_keys[
            "rest_api_key"
        ],  # This is your app's REST API key
    }

    data = json.loads(
        requests.get(api_url, headers=headers).content.decode("utf-8")
    )  # Here you have the data that you need

    city_count = data["count"]

    city_list = []

    for city_results in data["results"]:
        city_list.append(city_results["name"])

    if city_count == len(city_list):
        return city_list, city_count


if __name__ == "__main__":
    keys = cred_parser.parser()
    state_abbreviation = ["AL", "KY", "TX"]
    state_cities = {}
    for state in state_abbreviation:
        cities, count = get_cities(keys, state)
        state_cities[state] = {
            "cities": {},
            "count": {},
        }
        state_cities[state]["cities"] = cities
        state_cities[state]["count"] = count
    print(state_cities)
    with open("test.txt", "w") as json_output:
        json_output.write(json.dumps(state_cities))
