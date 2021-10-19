#!/user/bin/env python

import cred_parser
import json
import requests


def get_state_initials(api_keys):
    api_url = (
        "https://parseapi.back4app.com/classes/Usabystate_States?count=1&limit=10000"
    )

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

    if data["count"] != 50:
        print("oops.  Exiting")
        exit()

    list_of_state_abbrevs = []
    for item in data["results"]:
        list_of_state_abbrevs.append(item["postalAbreviation"])

    if len(list_of_state_abbrevs) == 50:
        return list_of_state_abbrevs

    else:
        print("oops.  Exiting")
        exit()


if __name__ == "__main__":
    keys = cred_parser.parser()
    state_abbrevs = get_state_initials(keys)
    print(state_abbrevs)
