import csv

# open a csv in write mode
with open('create-csv-example.csv', 'w', newline='') as csvfile:

    # create a writer object
    writer = csv.writer(csvfile)

    # writer header row
    writer.writerow(['Name', 'Age', 'City'])

    #write data rows
    writer.writerow(['Karan Chauhan', 28, 'New York City'])
    writer.writerow(['Goku', 40, 'Las Vegas'])
    writer.writerow(['Vegeta', 40, 'San Francisco'])
    writer.writerow(['Piccolo', 40, 'New Orleans'])
