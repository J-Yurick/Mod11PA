# penguin_stats.py
# J. Andrew Yurick
# November 17, 2026
# Functions for calculating and classifying penguin statistics

def calculate_percentage(count, total):
    percentage = count / total * 100
    return percentage

def classify_species(percent):
    if percent < 25:
        size_category = "small"
    elif percent >= 25 and percent < 40:
        size_category = "medium"
    else:
        size_category = "large"
    return size_category

def get_position_description(
        selected_species,
        largest_species,
        smallest_species
):
    if selected_species == largest_species:
        position_description = "largest"
    elif selected_species == smallest_species:
        position_description = "smallest"
    else:
        position_description = "middle-sized"
    return position_description