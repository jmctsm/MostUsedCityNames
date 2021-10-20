#!/usr/bin/env python

import state_parser
import cred_parser
import city_parser
import time
import city_count

if __name__ == "__main__":
    cred_keys = cred_parser.parser()
    states_list = state_parser.get_state_initials(cred_keys)
    state_cities = {}
    sleep_counter = 0

    for state in states_list:
        cities, count = city_parser.get_cities(cred_keys, state)
        state_cities[state] = {
            "cities": {},
            "count": {},
        }
        state_cities[state]["cities"] = cities
        state_cities[state]["count"] = count
        sleep_counter += 1
        if sleep_counter >= 5:
            sleep_counter = 0
            time.sleep(1)

    city_count_dict = city_count.city_count(state_cities)

    print(city_count_dict)
