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
                # count_dict[each_city]["count"] += 1
                # count_dict[each_city]["state_list"].append(state_key)
                count_dict[each_city]["state_set"].add(state_key)
                count_dict[each_city]["count"] = len(count_dict[each_city]["state_set"])
            else:
                # count_dict[each_city] = {
                #    "count": 1,
                #    "state_list": [
                #        state_key,
                #    ],
                # }
                count_dict[each_city] = {
                    "count": 1,
                    "state_set": {
                        state_key,
                    },
                }
    count_dict["total_counter"] = city_counter
    sorted_dict = city_sort(count_dict)
    return sorted_dict


def city_sort(unsorted_dict: dict) -> list:
    counter = 0
    total_in_first_list = len(unsorted_dict)
    output_list = []
    unsorted_dict.pop("total_counter", None)
    while len(unsorted_dict) != 0:
        highest_number_seen = 0
        largest_count = {}
        largest_city = "placeholder"
        for city in unsorted_dict.keys():
            if city == "total_counter":
                continue
            if unsorted_dict[city]["count"] > highest_number_seen:
                largest_count = unsorted_dict[city]
                largest_city = city
                highest_number_seen = largest_count["count"]
        counter += 1
        if largest_city == "placeholder" and counter == total_in_first_list:
            continue
        elif largest_city == "placeholder" and counter != total_in_first_list:
            print("Counter does not equal number in dict.  Exiting")
            print(f"{ counter= }")
            print(f"{ total_in_first_list= }")
            exit()
        else:
            output_list.append({largest_city: largest_count})
            unsorted_dict.pop(largest_city, None)
    return output_list


if __name__ == "__main__":
    import json

    with open("test.txt", "r") as test_data:
        test_dict = json.loads(test_data.read())
    city_dict = city_count(test_dict)
    print(f"{ city_dict= }")
