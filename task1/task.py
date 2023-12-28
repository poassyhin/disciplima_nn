import csv
import sys

def get_csv_cell(file_name, row_idx, col_idx):
    with open(file_name, newline='') as csvfile:
        data_reader = csv.reader(csvfile)
        for current_row, content in enumerate(data_reader):
            if current_row == row_idx:
                try:
                    return content[col_idx]
                except IndexError:
                    print("Column index out of range.")
                    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <filename> <row number> <column number>")
        sys.exit(1)

    filename = sys.argv[1]
    row_number = int(sys.argv[2]) - 1  # Adjusting for zero-based indexing
    column_number = int(sys.argv[3]) - 1  # Adjusting for zero-based indexing

    cell_value = get_csv_cell(filename, row_number, column_number)
    if cell_value is not None:
        print(cell_value)
    else:
        print("Row index out of range.")