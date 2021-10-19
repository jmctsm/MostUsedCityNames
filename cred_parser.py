#!/usr/bin/env python

import yaml


def parser():
    with open("keys.yml", "r") as key_stream:
        try:
            return_dict = {}
            yaml_dict = yaml.safe_load(key_stream)
            return_dict["rest_api_key"] = yaml_dict[0]["keys"]["rest_api_key"]
            return_dict["application_id"] = yaml_dict[0]["keys"]["application_id"]
            return return_dict
        except yaml.YAMLError as ex:
            print(ex)
            exit()


if __name__ == "__main__":
    return_dict = parser()
    print(return_dict)
