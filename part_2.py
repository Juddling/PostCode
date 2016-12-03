import csv
import validator

with open('import_data.csv', newline='') as import_file, open('failed_validation.csv', 'w', newline='') as failed:
    reader = csv.reader(import_file)
    writer = csv.writer(failed)

    # skip the first row with column names
    first_row = next(reader)
    writer.writerow(['row_id', 'postcode'])

    for row in reader:
        post_code = row[1]
        match = validator.prog.match(post_code)

        if match is None:
            writer.writerow(row)
