# PalmerPenguinsM11.py
# J. Andrew Yurick
# November 17, 2026
# Organize Palmer Penguin analysis using custom modules

# import modules
import math
from penguin import Penguin
import penguin_stats
from penguin_stats import calculate_percentage

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"
NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

# Retrieve a specified penguin observation from the CSV file.
def read_penguin_row(row_number):
    penguin_row = ""
    
    try:
        # open the CSV file and skip the header row
        with open("PalmerPenguins.csv", "r") as penguin_file:
            penguin_file.readline()

            current_row = 1

            # search for the requested data row
            for row in penguin_file:
                if current_row == row_number:
                    penguin_row = row.strip()
                    break

                current_row += 1
    except FileNotFoundError:
        print("Error: PalmerPenguins.csv was not found.")

    # Check if Row returns empty string
    if penguin_row == "":
        raise ValueError(
            f"Penguin observation {row_number} "
            f"could not be retrieved."
        )

    # return the requested row as a string
    return penguin_row

# Display each species with its count and percentage of the dataset.
def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(
            f"{species}: {counts[index]} "
            f"({percentages[index]:.2f}%)"
        )
    print()

# Display the formatted details of an individual penguin observation.
def display_penguin_observation(
        sample_number,
        species,
        bill_length,
        bill_depth,
        body_mass,
        sex
):
    print("\nSample Penguin Observation")
    print(f"{'Sample Number:':<15}{sample_number}")
    print(f"{'Species:':<15}{species}")
    print(f"{'Bill length:':<15}{bill_length} mm")
    print(f"{'Bill depth:':<15}{bill_depth} mm")
    print(f"{'Body mass:':<15}{body_mass} g")
    print(f"{'Sex:':<15}{sex}")

# Read and process a CSV observation, handling invalid or missing data.
def process_penguin_row(row_number):
    # retrieve sample penguin data
    try:
        penguin_row = read_penguin_row(row_number)

        print("\nSample dataset row:")
        print(penguin_row)

        # split the CSV row into individual values
        penguin_data = penguin_row.split(",")
        # DEBUG
        print(penguin_data)

        # retrieve and convert individual values
        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        bill_length = float(penguin_data[2])
        bill_depth = float(penguin_data[3])
        body_mass = int(penguin_data[5])
        sex = penguin_data[6]

        # display the penguin observation
        display_penguin_observation(
            sample_number,
            species,
            bill_length,
            bill_depth,
            body_mass,
            sex
        )
    except ValueError as excpt:
        print(f"Error: {excpt}")
    except IndexError:
        print("Error: The penguin observation is incomplete.")

# Perform dataset analysis and provide interactive species exploration.
def main():
    # lists containing related penguin data
    species_names = [SP_CHINSTRAP, SP_GENTOO, SP_ADELIE]
    species_counts = [NUM_CHINSTRAP, NUM_GENTOO, NUM_ADELIE]

    # calculate dataset statistics
    total_species = len(species_names)
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)
    chinstrap_percent = penguin_stats.calculate_percentage(
        species_counts[0],
        total_penguins
    )
    gentoo_percent = penguin_stats.calculate_percentage(
        species_counts[1],
        total_penguins
    )
    adelie_percent = penguin_stats.calculate_percentage(
        species_counts[2],
        total_penguins
    )

    # list containing the percentage of each species
    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    # determine largest and smallest species groups
    largest_count = max(species_counts)
    smallest_count = min(species_counts)
    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)
    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output the species names with introductory text
    print("Introducing the Palmer Penguins:")
    print()
    print(f"\t{species_names[0]}!")
    print(f"\t{species_names[1]}!")
    print("and last but not least...")
    print()
    print(f"\t{species_names[2]}!")
    print()

    # output dataset statistics
    print(
        f"There are a total of {total_species} "
        f"penguin species in this dataset."
    )
    print(
        f"There are a total of {total_penguins} "
        f"penguins in the dataset."
    )
    print(
        f"The average number of penguins per "
        f"species is " f"{average_penguins:.1f}."
    )
    print(
        f"The average rounded up is "
        f"{average_penguins_rounded_up} penguins."
    )

    # display species statistics using a loop
    display_species_statistics(species_names, \
        species_counts, species_percentages)

    # display the species with the most and fewest observations
    print(
        f"The species with the most observations is "
        f"{largest_species} with {largest_count} penguins."
    )
    print(
        f"The species with the fewest observations is "
        f"{smallest_species} with {smallest_count} penguins."
    )

    # Demonstrate calling a function imported directly from penguin_stats.    
    print("\nModule Import Demonstration")
    percentage = calculate_percentage(
        species_counts[0], total_penguins
        )
    print(f"Chinstrap percentage: {percentage:.2f}%")

    # Display the file path of the custom penguin_stats module.
    print("\nCustom Module Location")
    print(penguin_stats.__file__)

    # retrieve and process two sample observations
    process_penguin_row(1)
    process_penguin_row(153)
    print("\nException Handling Demonstration")
    process_penguin_row(999)

    # Create list to store body masses
    sample_rows = [1, 2, 3, 4, 5]

    # Create list to store Body Masses
    body_masses = []

    # Retrieve and Collect Body Masses
    for bmr_row in sample_rows:
        # retrieve the CSV row
        penguin_row = read_penguin_row(bmr_row)

        # split the row into individual values
        penguin_data = penguin_row.split(",")

        # convert the body mass to an integer
        body_mass = int(penguin_data[5])

        #append the body mass to the list
        body_masses.append(body_mass)

    print("\nSample Body Masses")
    print(body_masses)
    print()

    # Calculate SUmmary Statistics
    observations = len(body_masses)
    total_body_mass = sum(body_masses)
    smallest_body_mass = min(body_masses)
    largest_body_mass = max(body_masses)
    average_body_mass = float(total_body_mass / observations)

    # Print out Body Mass Summary
    print("Body Mass Summary")
    print(f"{'Observations:':<20}{observations}")
    print(f"{'Total body mass:':<20}{total_body_mass} g")
    print(f"{'Smallest body mass:':<20}{smallest_body_mass} g")
    print(f"{'Largest body mass:':<20}{largest_body_mass} g")
    print(f"{'Average body mass:':<20}{average_body_mass:.2f} g")
    print()

    # Create Dictionary of Species Counts
    species_dictionary = {
        SP_CHINSTRAP: NUM_CHINSTRAP,
        SP_GENTOO: NUM_GENTOO,
        SP_ADELIE: NUM_ADELIE
        }

    # Access and Display Dictionary Values 
    # Display Species Count
    print("Species Counts Using a Dictionary")
    for species_key in species_dictionary:
        count = species_dictionary[species_key]
        print(f"{species_key}: {count}")

    # Create a Penguin Object from CSV Data
    penguin_row = read_penguin_row(1)
    penguin_data = penguin_row.split(",")

    # Extract Penguin Attributes
    sample_number = int(penguin_data[0])
    species = penguin_data[1]
    body_mass = int(penguin_data[5])

    # Create Penguin Instance
    sample_penguin = Penguin(
        sample_number,
        species,
        body_mass
    )

    # Display Penguin Object Information
    print("\nPenguin Object Demonstration")
    sample_penguin.display_info()
    
    # Create an empty list for Penguin Objects
    penguin_objects = []

    for sample_row in sample_rows:
        # Retrieve and split the CSV row
        penguin_row = read_penguin_row(sample_row)
        penguin_data = penguin_row.split(",")
        # Create a penguin object
        penguin_object = Penguin(
            int(penguin_data[0]),
            penguin_data[1], 
            int(penguin_data[5])
        )
        # Append the object to penguin_objects
        penguin_objects.append(penguin_object)

    # Print the Penguin Object
    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    # Calculate Average Using Object Attributes
    total_object_mass = 0
    for penguin_object in penguin_objects:
        total_object_mass = total_object_mass + penguin_object.body_mass

    average_object_mass = total_object_mass / len(penguin_objects)

    # Display the Calculated Results
    print("\nObject-Based Body Mass Summary")
    print(f"Observations: {len(penguin_objects)}")
    print(f"Total body mass: {total_object_mass} g")
    print(f"Average body mass: {average_object_mass:.2f} g")


    # Counter for Valid Species
    valid_selections = 0

    # Explore a species based on user input
    print("\nExplore the Palmer Penguins")
    print("Enter Chinstrap, Gentoo, Adelie, Sample, or Done.")

    species_choice = input("\nEnter a species: ")

    # repeatedly prompt the user to explore species
    while species_choice != "Done":
        # validate species selection
        if species_choice == "Sample":
            try:
                sample_number = int(input("Enter a sample number: "))
                process_penguin_row(sample_number)
            except ValueError:
                print("Error: Please enter a valid integer sample number.")
            finally:
                print("Sample request completed.")
        
        elif species_choice not in species_names:
            print("That is not a valid species.")

        # Determine selected species
        else:
            # update the number of valid selections
            valid_selections += 1
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            # classify selected species
            size_category = penguin_stats.classify_species(selected_percent)

            # Determine species position
            position_description = penguin_stats.get_position_description(
                selected_species,
                largest_species,
                smallest_species
            )

            average_position = (
                "above" if selected_count > average_penguins else "below"
            )

            # Output selected species statistics
            print(f"\nSpecies: {selected_species}")
            print(f"Count: {selected_count}")
            print(f"Percentage: {selected_percent:.2f}%")
            print(
                f"This species represents a "
                f"{size_category} portion of the dataset."
            )
            print(
                f"It is the {position_description} species "
                f"in the dataset."
            )
            print(
                f"Its count is {average_position} "
                f"the average."
            )
                    
        species_choice = input("\nEnter another species: ")
        

    # display the exploration summary
    print(f"\nYou explored {valid_selections} valid penguin species.")
    print("\nExploration complete.")

# Run the main function only when this file is executed directly.
if __name__ == "__main__":
    main()