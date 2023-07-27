import pyarrow.parquet as pq
from prettytable import PrettyTable
import argparse

# Define a function to print the table metadata
def print_table_metadata(parquet_file):
    # Load the Parquet file
    table = pq.read_table(parquet_file)

    # Create a prettytable
    pt = PrettyTable()

    # Define the column headers
    pt.field_names = ["Column Name", "Type", "Description"]

    # Loop through each column in the schema
    for i in range(table.num_columns):
        # Get the column
        column = table.column(i)

        # Get the field (contains the metadata)
        field = table.schema.field(i)

        # Add a row to the table with the column name, type and full description
        pt.add_row([field.name, field.type, field.metadata[b'description'].decode('utf8')])

    # Print the table
    print(pt)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Print metadata from a Parquet file.')
parser.add_argument('input', type=str, help='Input Parquet file name')

args = parser.parse_args()

# Print the table metadata
print_table_metadata(args.input)
