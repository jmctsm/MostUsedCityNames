#!/usr/bin/env python


def city_count(city_dict):
    if not isinstance(city_dict, dict):
        print(f"Didn't pass a dictionary.  Passed type { type(city_dict) }.  Exiting")
        exit()
    count_dict = {}
    city_counter = 0
    for state_key in city_dict.keys():
        city_counter += city_dict[state_key]["count"]
        city_list = city_dict[state_key]["cities"]
        for each_city in city_list:
            print(each_city)
    print(city_counter)


if __name__ == "__main__":
    import json

    with open("test.txt", "r") as test_data:
        test_dict = json.loads(test_data.read())
    city_count(test_dict)
