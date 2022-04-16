import csv
import sys


# This function reads the csv file specified in the command line, and classifies each row of data into one of
# two classes.
if __name__ == '__main__':
    # If the amount of arguments (plus the name of the program) is not 2, we will inform the user.
    if len(sys.argv) != 2:
        print("Error - invalid number of arguments (must specify the csv file)")
    else:
        try:
            # The second cmd argument is the csv file we have to open and retrieve data from
            with open(sys.argv[1]) as csv_file:
                read_data = csv.reader(csv_file)
                records = []  # The list of records
                read_data.__next__()  # We ignore the headers
                output_file = open("output.csv", "w", newline="")  # Puts the classified data into another csv file
                write_data = csv.writer(output_file)

                # Add each value of a record to a local list
                for record in read_data:
                    # We normalize each age by rounding them to the nearest 2 years
                    the_float = float(record[0].strip())
                    norm_age = round(the_float / 2) * 2

                    # We normalize each height by rounding them to the nearest 4 centimeters
                    the_float = float(record[1].strip())
                    norm_height = round(the_float / 4) * 4

                    # We normalize each tail length by rounding them to the nearest 2 units
                    the_float = float(record[2].strip())
                    norm_tail = round(the_float / 2) * 2

                    # We normalize each hair length by rounding them to the nearest 2 units
                    the_float = float(record[3].strip())
                    norm_hair = round(the_float / 2) * 2

                    # We normalize each bang length by rounding them to the nearest 2 units
                    the_float = float(record[4].strip())
                    norm_bang = round(the_float / 2) * 2

                    # We normalize each reach by rounding them to the nearest 2 units
                    the_float = float(record[5].strip())
                    norm_reach = round(the_float / 2) * 2

                    this_record = [norm_age, norm_height, norm_tail, norm_hair, norm_bang, norm_reach]
                    records.append(this_record)

                # Determine which class each record belongs to
                for record in records:
                    answer = 0  # If answer becomes positive class is Bhutan, else Assam

                    # Decision stump
                    if record[5] < 10:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[3] < 4:
                        answer -= 1
                    else:
                        answer += 1

                    # Decision stump
                    if record[4] < 2:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[0] < 40:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[1] < 120:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[0] < 28:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[3] < 6:
                        answer -= 1
                    else:
                        answer += 1

                    # Decision stump
                    if record[3] < 4:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[3] < 4:
                        answer += 1
                    else:
                        answer -= 1

                    # Decision stump
                    if record[2] < 4:
                        answer += 1
                    else:
                        answer -= 1

                    # We finally determine the class
                    if answer <= 0:
                        write_data.writerow(["-1"])
                    else:
                        write_data.writerow(["+1"])

            csv_file.close()
            output_file.close()

        # If the file is unable to be opened for whatever reason, we will inform the user.
        except OSError:
            print("Error - cannot open file " + sys.argv[1] + "'")
