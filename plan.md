# General
*Input*: Schematic

**What do I want to know?**
x *How many* of each block are needed?
o *What resources* and how much of each resource are needed to get each block?
o Which *steps* and how many steps does it take to get each block?
o What's the most *efficient way* to get each resource?

# Steps
1. Get data
    **Mods**:
    - Create
    - Minecraft

    **Data**:
    - Blocks
        - ID
        - tag
        - Name
        - Tool required (by tag)
        - Mod
    - Items
        - ID
        - tag
        - Name
        - Which block?
        - Mod
    - Recipes
        - ID
        - Inputs (by tag) + input amounts
        - Outputs (by tag) + output amounts
        - Tools required (by tag)
        - Machines required (by tag)
    - Tags
        - Tag name
        - Items / Blocks (by tag)
2. Put all data for blocks, items, recipes and tags into respective files
3. Model data by tags
    - Blocks -> Items (Tools)
    - Items -> Blocks
    - Recipes -> Items, Blocks, Recipes, Tags
    - Tags -> Items, Blocks
4. Programmatically get all field names from one recipe 
5. Get all inputs and outputs for one recipe recursively