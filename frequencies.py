"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if item not in frequencies.keys():
            frequencies[item] = 1
        else:
            count = frequencies.get(item)
            frequencies.update({item:count+1})
    return frequencies
