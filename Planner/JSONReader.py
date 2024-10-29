from Planner import Resource
import json


class JSONReader:
    @staticmethod
    def return_json(json_file:str) -> dict:
        with open(json_file) as f:
            data = json.load(f)
        return data

    @staticmethod
    def print_keys(json_file:str, indent=0) -> None:
        """
        :param json_file: Path to json file
        :return: Recursively prints all keys in a json file with the appropriate hierarchy
        """

        with open(json_file) as f:
            blocks_data = json.load(f)
            JSONReader.print_keys_recursively(blocks_data, indent)

    @staticmethod
    def print_keys_recursively(json_file:dict, indent=0) -> None:
        for key, value in json_file.items():
            if key == 'states':
                continue

            if isinstance(value, dict):
                print(" " * indent + key)
                JSONReader.print_keys_recursively(value, indent + 2)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        print(" " * indent + key)
                        JSONReader.print_keys_recursively(item, indent + 2)
                    else:
                        print(" " * indent + str(item))

    @staticmethod
    def get_max_stack_from_json_by_id(json_dict, item_id:str) -> int:
        item_data = json_dict.get(item_id, {})
        return item_data.get("max_stack_size", 64)