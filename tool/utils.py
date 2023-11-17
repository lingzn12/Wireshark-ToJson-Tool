import yaml
import os
import json

from model.dataModel import *
from typing import Any
from ipaddress import IPv4Address
from colorama import Fore


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, IPv4Address):
            return str(obj)
        elif isinstance(obj, bytes):
            return str(obj)
        return super().default(obj)


def is_folder_empty(folder_path: str) -> bool:
    files = os.listdir(folder_path)

    if len(files) == 0:
        return True
    else:
        return False


def read_yaml(file_path: str) -> YAMLData:
    with open(file_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return YAMLData(**data)


def write_yaml_file(file_path: str, key_value_dict: Any) -> bool:
    try:
        with open(file_path, 'w') as file:
            yaml.dump(key_value_dict, file)

        return True
    except Exception as e:
        print(Fore.RED, f'error: {e}')
        return False


def get_files_in_folder(folder_path: str) -> List[str]:
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


def update_yaml_file(file_path: str, key_value_dict: dict) -> bool:
    try:
        with open(file_path) as file:
            yaml_data = yaml.safe_load(file)

        for key, value in key_value_dict.items():
            yaml_data[key] = value

        with open(file_path, 'w') as file:
            yaml.dump(yaml_data, file)

        return True
    except Exception as e:
        print(Fore.RED, f'error: {e}')
        return False


def convert_yaml_to_json(yaml_data: Any, json_file_path: str) -> bool:
    try:
        json_data = json.dumps(yaml_data, cls=CustomEncoder)

        for value in dict(json.loads(json_data)).values():
            pass

        with open(json_file_path, 'w') as file:
            file.write(json_data)

        print(Fore.GREEN, f"Converted YAML to JSON. Saved to \"{json_file_path}\"")

        return True
    except Exception as e:
        print(Fore.RED, f'error: {e}')
        return False
