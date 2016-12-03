import csv
import validator


def sort_and_write(file, data):
    # in place sort, make sure the row id is cast to int, otherwise string ordering is used
    data.sort(key=lambda row: int(row[0]))

    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['row_id', 'postcode'])

        for row in data:
            writer.writerow(row)


def validate_postcodes():
    with open('import_data.csv', newline='') as import_file:
        reader = csv.reader(import_file)
        succeeded = []
        failed = []

        # skip the first row with column names
        first_row = next(reader)

        for row in reader:
            post_code = row[1]
            match = validator.prog.match(post_code)
            # match = re.match(validator.pattern, post_code)

            if match is None:
                failed.append(row)
            else:
                succeeded.append(row)

        sort_and_write('failed_validation.csv', failed)
        sort_and_write('succeeded_validation.csv', succeeded)


validate_postcodes()
