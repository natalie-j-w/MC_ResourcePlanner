import json


class JSONReader:
    @staticmethod
    def print_keys(json_file=str, indent=0) -> None:
        '''
        :param json_file: Path to json file
        :return: Recursively prints all keys in a json file with the appropriate hierarchy
        '''

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

    def populate_recipetypes_enum(self):
        pass