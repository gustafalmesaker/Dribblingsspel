import csv

def read_csv(file_name):
    # Initialize lists to store exercise names and positions
    exercises = []
    positions = []

    # Read data from the CSV file
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Read each row of the CSV file
        for row in reader:
            #remove brackets and commas from the string
            row[1]=row[1].replace('[','')
            row[1]=row[1].replace(']','')
            row[1]=row[1].replace(',','')

            exercise = row[0]
            position_str = row[1]

            # Convert position string to list
            position = (position_str)

            # Append exercise name and position to respective lists
            exercises.append(exercise)
            positions.append(position)

    return exercises, positions