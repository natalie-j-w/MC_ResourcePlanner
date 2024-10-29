import os

from Planner import FileManager, JSONReader, Recipe, ResourceManager

reader = JSONReader()
rm = ResourceManager()

all_items_data = r"D:\MC_ResourcePlanner\Resources_new\Data Files\mc_create_fulldata.csv"

rm.add_resources_from_csv(all_items_data)   # !!

recipes_path = r"D:\MC_ResourcePlanner\Resources_new\Recipes\minecraft"
for recipe in os.listdir(recipes_path):
    full_path = os.path.join(recipes_path, recipe)
    recipe_dict = reader.return_json(full_path)
    r = Recipe(recipe_dict, rm)
    print(r)

# print(recipe_dict["type"], recipe_dict["key"], recipe_dict["pattern"])
# keys = recipe_dict.get("key")
# pattern = "".join(recipe_dict.get("pattern"))
#
# if keys is not None:
#     for item in keys:
#         print(keys[item]['item'])
#         print(rm.get_resource_by_id(keys[item]['item']))
#         print(pattern.count(item))
#     print(recipe_dict["result"]["item"])

#
# def create_all_data_file():
#     in_file = r"D:\MC_ResourcePlanner\Resources_new\Data Files\resources_mc_create_1.20.1.csv"
#
#     json_file = r"D:\MC_ResourcePlanner\Resources_new\Data Files\items.json"
#
#     FileManager.blocks_csv_add_stack_size(in_file,json_file,all_items_data)
#
# rm = ResourceManager()

# for key in rm.resources:
#     print(key, rm.resources[key])