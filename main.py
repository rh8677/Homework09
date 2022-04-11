import csv
import math
import random
import sys


attr_array = [[]] * 6  # An array containing arrays for all values of each attribute
# The amount of random trees for each random forest iteration to test
stump_nums = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
folds = [[]] * 10  # The list containing arrays of data for each fold
split_num = 0  # The number of records (FROM EACH CLASS) to append to each fold


# This function will create the specified amount of random decision trees for a random forest
#
# argument 1 (tree_num) - the amount of tree stumps to make
def create_forest(tree_num):
    random_forest = open("HW_09_rh8677@g.rit.edu_Classifier.py", "w")
    random_forest.write("import csv\n")
    random_forest.write("import sys\n")
    random_forest.write("\n")
    random_forest.write("\n")
    random_forest.write("# This function reads the csv file specified in the command line, and classifies each row of "
                        "data into one of\n")
    random_forest.write("# two classes.\n")
    random_forest.write("if __name__ == '__main__':\n")
    random_forest.write("    # If the amount of arguments (plus the name of the program) is not 2, we will inform the "
                        "user.\n")
    random_forest.write("    if len(sys.argv) != 2:\n")
    random_forest.write("        print(\"Error - invalid number of arguments (must specify the csv file)\")\n")
    random_forest.write("    else:\n")
    random_forest.write("        try:\n")
    random_forest.write("            # The second cmd argument is the csv file we have to open and retrieve data "
                        "from\n")
    random_forest.write("            with open(sys.argv[1]) as csv_file:\n")
    random_forest.write("                read_data = csv.reader(csv_file)\n")


# This function will attempt 10-Fold Cross Validation for all values in the stump_nums global array
def cross_validate():
    best_stump = 0  # The number of stumps that resulted in the least amount of mistakes
    min_mistakes = math.inf  # The least amount of mistakes for all depths

    # Will perform cross validation for all numbers of stumps
    for stump in stump_nums:
        local_mistakes = 0  # The total amount of mistakes for this "depth"
        ran_attr = random.randint(0, 6)  # Select a random number from 0 to 6 that represents a certain attribute
        ran_hold = random.choice(attr_array[ran_attr])  # Select a random threshold value for the random attribute
        fold_count = 0  # The index of the current fold that we are training on

        while fold_count < 10:
            fold_count += 1


# This function reads the csv file specified in the command line, and separates data into either one
# of the ten different folds (for 10-Fold Cross Validation)
if __name__ == '__main__':
    # If the amount of arguments (plus the name of the program) is not 2, we will inform the user.
    if len(sys.argv) != 2:
        print("Error - invalid number of arguments (must specify the csv file)")
    else:
        try:
            # The second cmd argument is the csv file we have to open and retrieve data from
            with open(sys.argv[1]) as csv_file:
                assam_list = []  # The list of Assam records
                bhutan_list = []  # The list of Bhutan records
                read_data = csv.reader(csv_file)
                read_data.__next__()  # We ignore the headers
                total_counter = 0  # We want to determine the total amount of records there are

                # Add each value of a record to a local list
                for record in read_data:
                    # We normalize each age by rounding them to the nearest 2 years
                    the_float = float(record[0].strip())
                    norm_age = round(the_float / 2) * 2

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[0]:
                        attr_array[0] = [norm_age]
                    else:
                        attr_array[0].append(norm_age)

                    # We normalize each height by rounding them to the nearest 4 centimeters
                    the_float = float(record[1].strip())
                    norm_height = round(the_float / 4) * 4

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[1]:
                        attr_array[1] = [norm_height]
                    else:
                        attr_array[1].append(norm_height)

                    # We normalize each tail length by rounding them to the nearest 2 units
                    the_float = float(record[2].strip())
                    norm_tail = round(the_float / 2) * 2

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[1]:
                        attr_array[2] = [norm_tail]
                    else:
                        attr_array[2].append(norm_tail)

                    # We normalize each hair length by rounding them to the nearest 2 units
                    the_float = float(record[3].strip())
                    norm_hair = round(the_float / 2) * 2

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[1]:
                        attr_array[3] = [norm_hair]
                    else:
                        attr_array[3].append(norm_hair)

                    # We normalize each bang length by rounding them to the nearest 2 units
                    the_float = float(record[4].strip())
                    norm_bang = round(the_float / 2) * 2

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[1]:
                        attr_array[4] = [norm_bang]
                    else:
                        attr_array[4].append(norm_bang)

                    # We normalize each reach by rounding them to the nearest 2 units
                    the_float = float(record[5].strip())
                    norm_reach = round(the_float / 2) * 2

                    # Add the normalized value to the appropriate index of the list
                    if not attr_array[1]:
                        attr_array[5] = [norm_reach]
                    else:
                        attr_array[5].append(norm_reach)

                    # We convert each lobe value into an int
                    lobe = int(record[6].strip())

                    # We convert each class id into an int
                    class_id = int(record[8].strip())

                    this_record = [norm_age, norm_height, norm_tail, norm_hair, norm_bang, norm_reach, lobe, class_id]

                    # We append the record to the appropriate class list according to their class ids
                    if class_id == 1:
                        bhutan_list.append(this_record)
                    else:
                        assam_list.append(this_record)
                    total_counter += 1

                split_num = total_counter / 20
                fold_index = 0  # Current fold to account for
                record_count = 0  # Current record to append to the fold

                # We append to a total of 10 folds
                while fold_index < 10:

                    # We append the same amount of records to each fold
                    while record_count < split_num:
                        folds[fold_index].append(assam_list[record_count])  # Append a record from the Assam class
                        folds[fold_index].append(bhutan_list[record_count])  # Append a record from the Bhutan class
                        record_count += 1
                    fold_index += 1

                cross_validate()

            csv_file.close()

        # If the file is unable to be opened for whatever reason, we will inform the user.
        except OSError:
            print("Error - cannot open file " + sys.argv[1] + "'")
