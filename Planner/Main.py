import os

from Planner import FileManager, JSONReader, Recipe, DataManager, Resource

reader = JSONReader()
rm = DataManager()

all_items_data = r"D:\MC_ResourcePlanner\Resources_new\Data Files\mc_create_fulldata.csv"

rm.add_resources_from_csv(all_items_data)   # !!

recipes_path = r"D:\MC_ResourcePlanner\Resources_new\Recipes_old\minecraft"
for recipe in os.listdir(recipes_path):
    full_path = os.path.join(recipes_path, recipe)
    recipe_dict = reader.return_json(full_path)
    r = Recipe(recipe_dict, rm)
    print(r)
