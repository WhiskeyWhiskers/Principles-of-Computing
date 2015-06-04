__author__ = 'Stephen'

"""
Merge function for 2048 game.
"""
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # Remove all 0s from list
    non_zero_tiles = filter(lambda e: e != 0, line)
    # Create a non_zero_tiles_merged list from merging equal and adjacent items in the non_zeros list
    non_zero_tiles_merged = []
    i = 0
    while i <= len(non_zero_tiles) - 1:
        if i == len(non_zero_tiles) - 1:
            non_zero_tiles_merged.append(non_zero_tiles[i])
            i += 1
        elif non_zero_tiles[i] == non_zero_tiles[i+1]:
            non_zero_tiles_merged.append(non_zero_tiles[i]*2)
            i += 2
        else:
            non_zero_tiles_merged.append(non_zero_tiles[i])
            i += 1
    # Append leftover zeros to end of non_zero_tiles_merged to create results list
    results = non_zero_tiles_merged
    num_zeros_leftover = len(line) - len(non_zero_tiles_merged)
    i = 0
    while i < num_zeros_leftover:
        results.append(0)
        i += 1
    return results

