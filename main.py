#!/usr/bin/env python

import state_parser
import cred_parser
import city_parser

if __name__ == "__main__":
    cred_keys = cred_parser.parser()
    states_list = state_parser.get_state_initials(cred_keys)
    state_cities = {}
    for state in states_list:
        cities, count = city_parser.get_cities(cred_keys, state)
        state_cities[state] = {
            "cities": {},
            "count": {},
        }
        state_cities[state]["cities"] = cities
        state_cities[state]["count"] = count

    print(state_cities)
