#!/usr/bin/env python


def city_count(city_dict: dict) -> list:
    if not isinstance(city_dict, dict):
        print(f"Didn't pass a dictionary.  Passed type { type(city_dict) }.  Exiting")
        exit()
    count_dict = {}
    city_counter = 0
    for state_key in city_dict.keys():
        city_counter += city_dict[state_key]["count"]
        city_list = city_dict[state_key]["cities"]
        for each_city in city_list:
            if each_city in count_dict:
                count_dict[each_city]["count"] += 1
                count_dict[each_city]["state_list"].append(state_key)
            else:
                count_dict[each_city] = {
                    "count": 1,
                    "state_list": [
                        state_key,
                    ],
                }
    count_dict["total_counter"] = city_counter
    sorted_dict = city_sort(count_dict)
    return count_dict


def city_sort(unsorted_dict: dict) -> list:
    counter = 0
    output_list = []
    while len(unsorted_dict) != 0:
        for city in unsorted_dict.keys():
            if unsorted_dict[city]["count"] == counter:
                output_list
        counter += 0


if __name__ == "__main__":
    import json

    with open("test.txt", "r") as test_data:
        test_dict = json.loads(test_data.read())
    city_dict = city_count(test_dict)
    print(city_dict)
