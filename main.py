from tool.utils import *
from typing import Dict

if __name__ == '__main__':
    path: str = './yaml'
    data: Dict[str, YAMLData] = {}

    if not is_folder_empty(path):
        file_list: list = get_files_in_folder(path)

        for file in file_list:
            if '.yaml' in file:
                yaml_data: YAMLData = read_yaml(file)
                data.update({
                    file: yaml_data
                })

        for index, value in data.items():
            file_name: str = index.split('\\')[1].replace('yaml', 'json')
            new_file_path: str = f".\\json\\{file_name}"
            convert_yaml_to_json(data[index].dict(), new_file_path)
