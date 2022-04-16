from matplotlib import pyplot as plt
import csv
import math
import os
import random
import sys


# The amount of random trees for each random forest iteration to test
stump_nums = [1, 2, 4, 8, 10, 20, 25, 35, 50, 75, 100, 150, 200, 250, 300, 400]
stump_mistakes = []  # The amount of mistakes corresponding to each stump number above
attr_array = [[]] * 6  # An array containing arrays for all values of each attribute
folds = [[]] * 10  # The list containing arrays of data for each fold
split_num = 0  # The number of records (FROM EACH CLASS) to append to each fold


# This function will attempt 10-Fold Cross Validation for all values in the stump_nums global array
def cross_validate():
    best_stump = 0  # The number of stumps that resulted in the least amount of mistakes
    min_mistakes = math.inf  # The least amount of mistakes for all depths

    # Will perform cross validation for all numbers of stumps
    for stump in stump_nums:
        local_mistakes = 0  # The total amount of mistakes for this "depth"
        stump_count = 0  # The index of the current stump that we are creating

        # Create a classifier program with all the decision stumps that will be tested
        random_forest = open("HW_09_rh8677@g.rit.edu_Classifier.py", "w")
        random_forest.write("import csv\n")
        random_forest.write("import sys\n")
        random_forest.write("\n")
        random_forest.write("\n")
        random_forest.write(
            "# This function reads the csv file specified in the command line, and classifies each row of "
            "data into one of\n")
        random_forest.write("# two classes.\n")
        random_forest.write("if __name__ == '__main__':\n")
        random_forest.write(
            "    # If the amount of arguments (plus the name of the program) is not 2, we will inform the "
            "user.\n")
        random_forest.write("    if len(sys.argv) != 2:\n")
        random_forest.write("        print(\"Error - invalid number of arguments (must specify the csv file)\")\n")
        random_forest.write("    else:\n")
        random_forest.write("        try:\n")
        random_forest.write(
            "            # The second cmd argument is the csv file we have to open and retrieve data "
            "from\n")
        random_forest.write("            with open(sys.argv[1]) as csv_file:\n")
        random_forest.write("                read_data = csv.reader(csv_file)\n")
        random_forest.write("                records = []  # The list of records\n")
        random_forest.write("                read_data.__next__()  # We ignore the headers\n")
        random_forest.write("                output_file = open(\"output.csv\", \"w\", newline=\"\")  # Puts the "
                            "classified data into another csv file\n")
        random_forest.write("                write_data = csv.writer(output_file)\n")
        random_forest.write("\n")
        random_forest.write("                # Add each value of a record to a local list\n")
        random_forest.write("                for record in read_data:\n")
        random_forest.write("                    # We normalize each age by rounding them to the nearest 2 years\n")
        random_forest.write("                    the_float = float(record[0].strip())\n")
        random_forest.write("                    norm_age = round(the_float / 2) * 2\n")
        random_forest.write("\n")
        random_forest.write("                    # We normalize each height by rounding them to the nearest 4 "
                            "centimeters\n")
        random_forest.write("                    the_float = float(record[1].strip())\n")
        random_forest.write("                    norm_height = round(the_float / 4) * 4\n")
        random_forest.write("\n")
        random_forest.write("                    # We normalize each tail length by rounding them to the nearest 2 "
                            "units\n")
        random_forest.write("                    the_float = float(record[2].strip())\n")
        random_forest.write("                    norm_tail = round(the_float / 2) * 2\n")
        random_forest.write("\n")
        random_forest.write("                    # We normalize each hair length by rounding them to the nearest 2 "
                            "units\n")
        random_forest.write("                    the_float = float(record[3].strip())\n")
        random_forest.write("                    norm_hair = round(the_float / 2) * 2\n")
        random_forest.write("\n")
        random_forest.write("                    # We normalize each bang length by rounding them to the nearest 2 "
                            "units\n")
        random_forest.write("                    the_float = float(record[4].strip())\n")
        random_forest.write("                    norm_bang = round(the_float / 2) * 2\n")
        random_forest.write("\n")
        random_forest.write(
            "                    # We normalize each reach by rounding them to the nearest 2 units\n")
        random_forest.write("                    the_float = float(record[5].strip())\n")
        random_forest.write("                    norm_reach = round(the_float / 2) * 2\n")
        random_forest.write("\n")
        random_forest.write("                    this_record = [norm_age, norm_height, norm_tail, norm_hair, "
                            "norm_bang, norm_reach]\n")
        random_forest.write("                    records.append(this_record)\n")
        random_forest.write("\n")
        random_forest.write("                # Determine which class each record belongs to\n")
        random_forest.write("                for record in records:\n")
        random_forest.write("                    answer = 0  # If answer becomes positive class is Bhutan, else "
                            "Assam\n")
        random_forest.write("\n")

        # This loop will run until the specified number of stumps have been created
        while stump_count < stump:
            ran_attr = random.randint(0, 5)  # Select a random number from 0 to 6 that represents a certain attribute
            fold_count = 0  # The index of the current fold that we are testing
            min_fold_mistakes = math.inf  # The minimum amount of mistakes that a fold had created
            best_threshold = 0  # The threshold that best separates the data into different classes
            major_class = 0  # The majority of the class that is less than the best threshold

            # Will perform 10-fold Cross Validation for all 10 folds
            while fold_count < 10:
                ran_hold = random.choice(attr_array[ran_attr])  # Select a random threshold value for the attribute
                assam_count = 0  # The amount of Assams less than or equal to the random threshold
                bhutan_count = 0  # The amount of Bhutans less than or equal to the random threshold
                fold_mistakes = 0  # The amount of mistakes when testing on this fold
                local_count = 0  # The index of the current fold that we are training on

                # Train on the other 9 folds
                while local_count < 10:
                    # We skip the testing fold
                    if local_count == fold_count:
                        local_count += 1
                        continue

                    # We determine the majority class less than the threshold for 9 folds
                    for the_record in folds[local_count]:
                        if the_record[ran_attr] < ran_hold:
                            if the_record[7] == -1:
                                assam_count += 1
                            else:
                                bhutan_count += 1

                    local_count += 1

                # We assign the majority class based on our observations
                if assam_count > bhutan_count:
                    major_class = -1
                else:
                    major_class = 1

                # Test the accuracy of the classifier using the specified fold
                for da_record in folds[fold_count]:
                    if da_record[ran_attr] < ran_hold:
                        if da_record[7] == -major_class:
                            fold_mistakes += 1

                # If the amount of mistakes for the fold is less than previous ones, we update appropriate variables
                if fold_mistakes < min_fold_mistakes:
                    min_fold_mistakes = fold_mistakes
                    best_threshold = ran_hold

                fold_count += 1

            # If the major class is Bhutan, we print out this stump
            if major_class == 1:
                random_forest.write("                    # Decision stump\n")
                random_forest.write("                    if record[" + str(ran_attr) + "] < " + str(best_threshold) +
                                    ":\n")
                random_forest.write("                        answer += 1\n")
                random_forest.write("                    else:\n")
                random_forest.write("                        answer -= 1\n")
                random_forest.write("\n")

            # Otherwise, we print out this stump instead
            else:
                random_forest.write("                    # Decision stump\n")
                random_forest.write("                    if record[" + str(ran_attr) + "] < " + str(best_threshold) +
                                    ":\n")
                random_forest.write("                        answer -= 1\n")
                random_forest.write("                    else:\n")
                random_forest.write("                        answer += 1\n")
                random_forest.write("\n")

            stump_count += 1

        # We write the trailer of the classifier file
        random_forest.write("                    # We finally determine the class\n")
        random_forest.write("                    if answer <= 0:\n")
        random_forest.write("                        write_data.writerow([\"-1\"])\n")
        random_forest.write("                    else:\n")
        random_forest.write("                        write_data.writerow([\"+1\"])\n")
        random_forest.write("\n")
        random_forest.write("            csv_file.close()\n")
        random_forest.write("            output_file.close()\n")
        random_forest.write("\n")
        random_forest.write(
            "        # If the file is unable to be opened for whatever reason, we will inform the user.\n")
        random_forest.write("        except OSError:\n")
        random_forest.write("            print(\"Error - cannot open file \" + sys.argv[1] + \"'\")\n")
        random_forest.close()

        os.system("HW_09_rh8677@g.rit.edu_Classifier.py training.csv")  # We test the classifier using the training data

        training_class = []  # The list of classes from testing on the training data

        # We gather all the classifications of the training data
        with open("output.csv") as output_file:
            red_data = csv.reader(output_file)
            for data in red_data:
                training_class.append(int(data[0].strip()))
        output_file.close()

        # We determine how many mistakes in classifications the classifier made in training
        with open(sys.argv[1]) as training_file:
            red_data = csv.reader(training_file)
            red_data.__next__()  # We ignore the headers
            data_index = 0
            for data in red_data:
                the_class_id = int(data[8].strip())

                # If there is a mistake, we add a mistake
                if the_class_id != training_class[data_index]:
                    local_mistakes += 1

                data_index += 1
        training_file.close()

        stump_mistakes.append(local_mistakes)  # Append the number of mistakes to the global array

        # If the total amount of mistakes for this stump number is less than previous, we update appropriate variables
        if local_mistakes < min_mistakes:
            min_mistakes = local_mistakes
            best_stump = stump

    # Create the final classifier using the best number of stumps that we have found
    random_forest = open("HW_09_rh8677@g.rit.edu_Classifier.py", "w")
    random_forest.write("import csv\n")
    random_forest.write("import sys\n")
    random_forest.write("\n")
    random_forest.write("\n")
    random_forest.write(
        "# This function reads the csv file specified in the command line, and classifies each row of "
        "data into one of\n")
    random_forest.write("# two classes.\n")
    random_forest.write("if __name__ == '__main__':\n")
    random_forest.write(
        "    # If the amount of arguments (plus the name of the program) is not 2, we will inform the "
        "user.\n")
    random_forest.write("    if len(sys.argv) != 2:\n")
    random_forest.write("        print(\"Error - invalid number of arguments (must specify the csv file)\")\n")
    random_forest.write("    else:\n")
    random_forest.write("        try:\n")
    random_forest.write(
        "            # The second cmd argument is the csv file we have to open and retrieve data "
        "from\n")
    random_forest.write("            with open(sys.argv[1]) as csv_file:\n")
    random_forest.write("                read_data = csv.reader(csv_file)\n")
    random_forest.write("                records = []  # The list of records\n")
    random_forest.write("                read_data.__next__()  # We ignore the headers\n")
    random_forest.write("                output_file = open(\"output.csv\", \"w\", newline=\"\")  # Puts the "
                        "classified data into another csv file\n")
    random_forest.write("                write_data = csv.writer(output_file)\n")
    random_forest.write("\n")
    random_forest.write("                # Add each value of a record to a local list\n")
    random_forest.write("                for record in read_data:\n")
    random_forest.write("                    # We normalize each age by rounding them to the nearest 2 years\n")
    random_forest.write("                    the_float = float(record[0].strip())\n")
    random_forest.write("                    norm_age = round(the_float / 2) * 2\n")
    random_forest.write("\n")
    random_forest.write("                    # We normalize each height by rounding them to the nearest 4 "
                        "centimeters\n")
    random_forest.write("                    the_float = float(record[1].strip())\n")
    random_forest.write("                    norm_height = round(the_float / 4) * 4\n")
    random_forest.write("\n")
    random_forest.write("                    # We normalize each tail length by rounding them to the nearest 2 "
                        "units\n")
    random_forest.write("                    the_float = float(record[2].strip())\n")
    random_forest.write("                    norm_tail = round(the_float / 2) * 2\n")
    random_forest.write("\n")
    random_forest.write("                    # We normalize each hair length by rounding them to the nearest 2 "
                        "units\n")
    random_forest.write("                    the_float = float(record[3].strip())\n")
    random_forest.write("                    norm_hair = round(the_float / 2) * 2\n")
    random_forest.write("\n")
    random_forest.write("                    # We normalize each bang length by rounding them to the nearest 2 "
                        "units\n")
    random_forest.write("                    the_float = float(record[4].strip())\n")
    random_forest.write("                    norm_bang = round(the_float / 2) * 2\n")
    random_forest.write("\n")
    random_forest.write(
        "                    # We normalize each reach by rounding them to the nearest 2 units\n")
    random_forest.write("                    the_float = float(record[5].strip())\n")
    random_forest.write("                    norm_reach = round(the_float / 2) * 2\n")
    random_forest.write("\n")
    random_forest.write("                    this_record = [norm_age, norm_height, norm_tail, norm_hair, "
                        "norm_bang, norm_reach]\n")
    random_forest.write("                    records.append(this_record)\n")
    random_forest.write("\n")
    random_forest.write("                # Determine which class each record belongs to\n")
    random_forest.write("                for record in records:\n")
    random_forest.write("                    answer = 0  # If answer becomes positive class is Bhutan, else "
                        "Assam\n")
    random_forest.write("\n")

    stump_index = 0
    # This loop will run until the specified number of stumps have been created
    while stump_index < best_stump:
        ran_attr = random.randint(0, 5)  # Select a random number from 0 to 6 that represents a certain attribute
        fold_count = 0  # The index of the current fold that we are testing
        min_fold_mistakes = math.inf  # The minimum amount of mistakes that a fold had created
        best_threshold = 0  # The threshold that best separates the data into different classes
        major_class = 0  # The majority of the class that is less than the best threshold

        # Will perform 10-fold Cross Validation for all 10 folds
        while fold_count < 10:
            ran_hold = random.choice(attr_array[ran_attr])  # Select a random threshold value for the attribute
            assam_count = 0  # The amount of Assams less than or equal to the random threshold
            bhutan_count = 0  # The amount of Bhutans less than or equal to the random threshold
            fold_mistakes = 0  # The amount of mistakes when testing on this fold
            local_count = 0  # The index of the current fold that we are training on

            # Train on the other 9 folds
            while local_count < 10:
                # We skip the testing fold
                if local_count == fold_count:
                    local_count += 1
                    continue

                # We determine the majority class less than the threshold for 9 folds
                for the_record in folds[local_count]:
                    if the_record[ran_attr] < ran_hold:
                        if the_record[7] == -1:
                            assam_count += 1
                        else:
                            bhutan_count += 1

                local_count += 1

            # We assign the majority class based on our observations
            if assam_count > bhutan_count:
                major_class = -1
            else:
                major_class = 1

            # Test the accuracy of the classifier using the specified fold
            for da_record in folds[fold_count]:
                if da_record[ran_attr] < ran_hold:
                    if da_record[7] == -major_class:
                        fold_mistakes += 1

            # If the amount of mistakes for the fold is less than previous ones, we update appropriate variables
            if fold_mistakes < min_fold_mistakes:
                min_fold_mistakes = fold_mistakes
                best_threshold = ran_hold

            fold_count += 1

        # If the major class is Bhutan, we print out this stump
        if major_class == 1:
            random_forest.write("                    # Decision stump\n")
            random_forest.write("                    if record[" + str(ran_attr) + "] < " + str(best_threshold) +
                                ":\n")
            random_forest.write("                        answer += 1\n")
            random_forest.write("                    else:\n")
            random_forest.write("                        answer -= 1\n")
            random_forest.write("\n")

        # Otherwise, we print out this stump instead
        else:
            random_forest.write("                    # Decision stump\n")
            random_forest.write("                    if record[" + str(ran_attr) + "] < " + str(best_threshold) +
                                ":\n")
            random_forest.write("                        answer -= 1\n")
            random_forest.write("                    else:\n")
            random_forest.write("                        answer += 1\n")
            random_forest.write("\n")

        stump_index += 1

    # We write the trailer of the classifier file
    random_forest.write("                    # We finally determine the class\n")
    random_forest.write("                    if answer <= 0:\n")
    random_forest.write("                        write_data.writerow([\"-1\"])\n")
    random_forest.write("                    else:\n")
    random_forest.write("                        write_data.writerow([\"+1\"])\n")
    random_forest.write("\n")
    random_forest.write("            csv_file.close()\n")
    random_forest.write("            output_file.close()\n")
    random_forest.write("\n")
    random_forest.write(
        "        # If the file is unable to be opened for whatever reason, we will inform the user.\n")
    random_forest.write("        except OSError:\n")
    random_forest.write("            print(\"Error - cannot open file \" + sys.argv[1] + \"'\")\n")
    random_forest.close()

    # We want to plot a graph showcasing the relationship between number of stumps and mistakes
    plt.plot(stump_nums, stump_mistakes)
    plt.xlabel('Number of Stumps')
    plt.ylabel('Number of Mistakes')
    plt.title('Validation Error VS N_STUMPS')
    plt.show()


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

                cross_validate()  # We run 10-fold cross validation after the records have been analyzed

            csv_file.close()

        # If the file is unable to be opened for whatever reason, we will inform the user.
        except OSError:
            print("Error - cannot open file " + sys.argv[1] + "'")
