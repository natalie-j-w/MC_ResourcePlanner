from Planner import FileManager, JSONReader

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

csv_file_in = r"D:\MC_ResourcePlanner\Resources_new\Data Files\resources_mc_create_1.20.1.csv"
csv_file_out = r"D:\MC_ResourcePlanner\Resources_new\Data Files\mc_create_fulldata.csv"
json_file = r"D:\MC_ResourcePlanner\Resources_new\Data Files\items.json"

fm = FileManager()
fm.blocks_csv_add_stack_size(csv_file_in, json_file, csv_file_out)