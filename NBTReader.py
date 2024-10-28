import nbtlib
from collections import Counter


class NBTReader:
    def __init__(self):
        pass

    @staticmethod
    def nbt_get_block_counts(nbt_path: str) -> list[dict[str, int]]:
        """
        Counts the number of each block type in a Minecraft NBT structure file.

        Args:
            nbt_path (str): Path to the NBT file containing block data.

        Returns:
            list[dict[str, int]]: A list of dictionaries, each containing:
                - 'block' (str): The name of the block (e.g., "minecraft:oak_log").
                - 'count' (int): The number of occurrences of that block.

        Example:
            count_blocks_in_nbt("building.nbt")
            [
                {'block': 'minecraft:oak_log', 'count': 2},
                {'block': 'minecraft:stone', 'count': 5},
                {'block': 'minecraft:dirt', 'count': 3}
            ]
        """

        nbt_file = nbtlib.load(nbt_path)

        try:
            blocks = nbt_file['blocks']
            palette = nbt_file['palette']
        except Exception:
            raise KeyError("Couldn't find blocks or palette")

        block_to_index = {i: block['Name'] for i, block in enumerate(palette)}

        counter = Counter()
        for block in blocks:
            block_id = block['state']
            block_name = block_to_index[block_id]
            counter[block_name] += 1

        named_count_dict = [{"block": block, "count": count} for block, count in counter.items()]
        return named_count_dict
