import json
import csv
import os

class FileManager:
    resources_path = r"D:\MC_ResourcePlanner\Resources_new\Data Files"
    tags_path = r"D:\MC_ResourcePlanner\Resources_new\Tags"
    blocks_json = os.path.join(resources_path, "blocks.json")   # Expects blocks.json from Minecraft Reporting feature
    items_json =  os.path.join(resources_path, "items.json")    # Expects items.json from Minecraft Reporting feature
    fluids_json = os.path.join(resources_path, "fluids.json")   # Expects fluids.json from Minecraft Reporting feature
    all_resources_csv = os.path.join(resources_path, "mc_create_fulldata.csv")

    path_tags_create = os.path.join(tags_path, r"\Create 1.20.1 (Forge)\data")
    path_tags_minecraft = os.path.join(tags_path, r"\Minecraft 1.20.6\tags")

    def __init__(self):
        pass

    def blocks_csv_add_stack_size(self, csv_path_in, json_path, csv_path_out):
        from Planner import JSONReader

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
                        JSONReader.return_json(self.items_json),
                        row[3])
                    print(row[3]) if max_stack == 1 else ""
                    writer.writerow(row + [str(max_stack)])
                elif row[1] == "create":
                    max_stack = 1 if row[3] in create_mod_stack_one else 64
                    print(row[3]) if max_stack == 1 else ""
                    writer.writerow(row + [str(max_stack)])

    def read_tags_folders(self):
        pass

    @staticmethod
    def find_json_files(directory):
        json_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".json"):
                    json_files.append(os.path.join(root, file))
        return json_files

