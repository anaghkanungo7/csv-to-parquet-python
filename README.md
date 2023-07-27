# CSV to Parquet Conversion and Metadata Check

Python project to convert CSV to Parquet, and use an LLM to add metadata to the columns. 

This repository contains two Python scripts:
1. `csv_to_parquet.py`: Converts a CSV file to a Parquet file, dynamically generating metadata for the Parquet file based on the CSV data.
2. `check_parquet_metadata.py`: Reads a Parquet file and prints its metadata (column name, type, description).

## Description

- `csv_to_parquet.py`: This script reads a CSV file, generates a description of each column in the CSV file using OpenAI's GPT-3 model, converts the CSV file to a Parquet file, and writes the generated descriptions as metadata for the corresponding columns in the Parquet file.
  
- `check_parquet_metadata.py`: This script reads a Parquet file and prints a table with the column name, type, and description (retrieved from the metadata) of each column in the Parquet file.

## Usage

### Installation

First, install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Using the Scripts

#### `csv_to_parquet.py`

The `csv_to_parquet.py` script requires two command-line arguments:
- `input`: The name of the input CSV file.
- `output`: The name of the output Parquet file.

Here is how to use it:

```bash
python csv_to_parquet.py input.csv output.parquet
```

Remember to replace `input.csv` and `output.parquet` with your actual file names.

#### `check_parquet_metadata.py`

The `check_parquet_metadata.py` script requires one command-line argument:
- `input`: The name of the input Parquet file.

Here is how to use it:

```bash
python check_parquet_metadata.py input.parquet
```

Remember to replace `input.parquet` with your actual file name.

### OpenAI API Key

For the `csv_to_parquet.py` script to work, you need to provide your OpenAI API key. To do this, create a `.env` file in the project directory and add your OpenAI API key to it like this:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

### CSV File Delimiter

By default, the `csv_to_parquet.py` script assumes that the CSV delimiter is `,`. If your CSV file uses a different delimiter, remember to adjust the delimiter in the script.

## Example Files

This repository includes `example.csv` and `example_output.parquet` files that you can use to understand how the scripts work. 
Remember to replace all placeholders like `input.csv`, `output.parquet`, and `your_api_key_here` with your actual file names and API key.
