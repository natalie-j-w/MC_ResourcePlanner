import unittest

from numpy.ma.testutils import assert_equal

from Planner.Recipe import Recipe, RecipeItem
from Planner.DataManager import DataManager
from Planner.FileManager import FileManager
from Planner.Units import Units


class TestRecipeTypes(unittest.TestCase):
    def setUp(self):
        self.dm = DataManager()
        self.dm.add_resources_from_csv(FileManager.all_resources_csv)

    def test_shapeless_crafting(self):
        # TODO: Shapeless crafting test
        """Test processing for 'minecraft:crafting_shapeless' recipes."""
        data = {
            "type": "minecraft:crafting_shapeless",
            "category": "misc",
            "ingredients": [
                {
                    "item": "minecraft:bowl"
                },
                {
                    "item": "minecraft:beetroot"
                },
                {
                    "item": "minecraft:beetroot"
                },
                {
                    "item": "minecraft:beetroot"
                },
                {
                    "item": "minecraft:beetroot"
                },
                {
                    "item": "minecraft:beetroot"
                },
                {
                    "item": "minecraft:beetroot"
                }
            ],
            "result": {
                "item": "minecraft:beetroot_soup"
            }
        }

        pass

    def test_shaped_crafting(self):
        """Test processing for 'minecraft:crafting_shaped' recipes."""

        data = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "group": "stained_terracotta",
            "key": {
                "#": {
                    "item": "minecraft:terracotta"
                },
                "X": {
                    "item": "minecraft:black_dye"
                }
            },
            "pattern": [
                "###",
                "#X#",
                "###"
            ],
            "result": {
                "count": 8,
                "item": "minecraft:black_terracotta"
            },
            "show_notification": True
        }

        # Create recipe with minimal data -> input, output is determined with Recipe.set_input_output
        recipe_from_data = Recipe(data, self.dm)

        # Create recipe with input, output and recipe_type being given explicitly
        expected_input1 = RecipeItem(self.dm.get_resource_or_tag_by_id(data["key"]["#"]["item"]), 8)
        expected_input2 = RecipeItem(self.dm.get_resource_or_tag_by_id(data["key"]["X"]["item"]), 1)
        expected_output_amount = data["result"]["count"]
        expected_output = RecipeItem(self.dm.get_resource_or_tag_by_id(data["result"]["item"]), expected_output_amount)
        expected_recipe_type = data["type"]

        expected_recipe = Recipe(None, self.dm, expected_recipe_type,
                                 [expected_input1, expected_input2],
                                 [expected_output])

        # Test attributes
        self.assertEqual(recipe_from_data.recipe_type, expected_recipe.recipe_type, f"Recipe type doesn't match expected")
        self.assertEqual(recipe_from_data.inputs, expected_recipe.inputs, "Input doesn't match expected")
        self.assertEqual(recipe_from_data.outputs, expected_recipe.outputs, "Output doesn't match expected")

        # Test recipes
        self.assertEqual(recipe_from_data, expected_recipe, "Recipes don't match")

    def test_stonecutting(self):
        """Test processing for 'minecraft:stonecutting' recipes."""
        pass

    def test_smelting(self):
        """Test processing for 'minecraft:smelting' recipes."""
        pass

    def test_blasting(self):
        """Test processing for 'minecraft:blasting' recipes."""
        pass

    def test_campfire_cooking(self):
        """Test processing for 'minecraft:campfire_cooking' recipes."""
        pass

    def test_smoking(self):
        """Test processing for 'minecraft:smoking' recipes."""
        pass

    def test_smithing_transform(self):
        """Test processing for 'minecraft:smithing_transform' recipes."""
        pass

    def test_smithing_trim(self):
        """Test processing for 'minecraft:smithing_trim' recipes."""
        pass

    def test_milling(self):
        """Test processing for 'create:milling' recipes."""
        pass

    def test_pressing(self):
        """Test processing for 'create:pressing' recipes."""
        pass

    def test_splashing(self):
        """Test processing for 'create:splashing' recipes."""
        pass

    def test_emptying(self):
        """Test processing for 'create:emptying' recipes."""
        pass

    def test_filling(self):
        """Test processing for 'create:filling' recipes."""
        pass

    def test_crushing(self):
        """Test processing for 'create:crushing' recipes."""
        pass

    def test_mechanical_crafting(self):
        """Test processing for 'create:mechanical_crafting' recipes."""
        pass

    def test_sandpaper_polishing(self):
        """Test processing for 'create:sandpaper_polishing' recipes."""
        pass

    def test_item_application(self):
        """Test processing for 'create:item_application' recipes."""
        pass

    def test_mixing(self):
        """Test processing for 'create:mixing' recipes."""
        pass

    def test_sequenced_assembly(self):
        """Test processing for 'create:sequenced_assembly' recipes."""
        pass

    def test_cutting(self):
        """Test processing for 'create:cutting' recipes."""
        pass

    def test_deploying(self):
        """Test processing for 'create:deploying' recipes."""
        pass

    def test_compacting(self):
        """Test processing for 'create:compacting' recipes."""
        pass

    def test_haunting(self):
        """Test processing for 'create:haunting' recipes."""
        pass
