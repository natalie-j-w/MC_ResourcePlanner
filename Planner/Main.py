from Planner import FileManager, JSONReader, ResourceManager, Resource

# reader = JSONReader()
# recipe_dict = reader.return_json(r"D:\MC_ResourcePlanner\Resources_new\Recipes\minecraft\acacia_fence_gate.json")
# print(recipe_dict["type"], recipe_dict["key"], recipe_dict["pattern"])
# keys = recipe_dict.get("key")
# pattern = "".join(recipe_dict.get("pattern"))
#
# if keys is not None:
#     for item in keys:
#         print(keys[item]['item'])
#         print(pattern.count(item))
all_items_data = r"D:\MC_ResourcePlanner\Resources_new\Data Files\mc_create_fulldata.csv"

def createAllDataFile():
    in_file = r"D:\MC_ResourcePlanner\Resources_new\Data Files\resources_mc_create_1.20.1.csv"

    json_file = r"D:\MC_ResourcePlanner\Resources_new\Data Files\items.json"

    rm = FileManager
    FileManager.blocks_csv_add_stack_size(in_file,json_file,all_items_data)

rm = ResourceManager()
rm.add_resources_from_csv(all_items_data)
for key in rm.resources:
    print(key, rm.resources[key])