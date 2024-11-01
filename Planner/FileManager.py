import json
import csv

class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def blocks_csv_add_stack_size(csv_path_in, json_path, csv_path_out):
        from Planner import JSONReader
        # create: stack size 64 unless in list of items that have 1
        # minecraft: items.json -> 64 unless max_stack_size is specified

        create_mod_stack_one = ["create:builders_tea",
                                "create:goggles",
                                "create:superglue",
                                "create:wrench",
                                "create:linked_controller",
                                "create:wand_of_symmetry",
                                "create: empty_schematic",
                                "create:schematic_and_quill",
                                "create:schematic"]

        with open(csv_path_in,'r') as f, open(json_path,'r') as json_f, open(csv_path_out,'w',newline='') as new_csv:
            reader = csv.reader(f)
            json_data_mc = json.load(json_f)
            writer = csv.writer(new_csv,lineterminator="\n")

            writer.writerow(["ModName", "ModID", "ItemName", "ItemID", "MaxStackSize"])
            for row in reader:
                if row[1] == "minecraft":
                    max_stack = JSONReader.get_max_stack_from_json_by_id(
                        JSONReader.return_json(r"D:\MC_ResourcePlanner\Resources_new\Data Files\items.json"),
                        row[3])
                    print(row[3]) if max_stack == 1 else ""
                    writer.writerow(row + [str(max_stack)])
                elif row[1] == "create":
                    max_stack = 1 if row[3] in create_mod_stack_one else 64
                    print(row[3]) if max_stack == 1 else ""
                    writer.writerow(row + [str(max_stack)])


