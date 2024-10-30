import os

from Planner import FileManager, JSONReader, Recipe, DataManager, Resource

reader = JSONReader()
rm = DataManager()

# all_items_data = r"D:\MC_ResourcePlanner\Resources_new\Data Files\mc_create_fulldata.csv"
# rm.add_resources_from_csv(all_items_data)   # !!
#
recipes_path = r"D:\MC_ResourcePlanner\Resources_new\Recipes_old\create"
Recipe.print_all_crafting_types(recipes_path)
