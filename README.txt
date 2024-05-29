File Stats and Read Client
This is a small command-line tool written in Python to interact with a file storage service's REST API.
It only supports retrieving file stats and reading file content.

Installation
This script requires typer and requests libraries. You can install them using pip:

Bash
pip install typer requests

Usage
This script provides two commands:

stat: Retrieves statistics about a file.
read: Reads the content of a file.

General arguments:
uuid (str): The unique identifier of the file.
backend (str, optional): Currently only rest is supported (default: grpc).
base_url (str, optional): The base URL of the REST API server (default: http://localhost/).
default_output (str, optional): Where to store the output (default: - for standard output).

stat command:
stat <uuid> [--backend rest] [--base_url URL] [--default_output FILE]
This command displays information about a file, including name, size, MIME type, and creation date. The output can be written to a file or printed to the console.

read command:
read <uuid> [--backend rest] [--base_url URL] [--default_output FILE]
This command retrieves the content of a file. The content can be written to a file or printed to the console.

Note:
Currently, only the REST backend is supported.

Example
Bash
# Get stats of a file with id "1234" and write output to "stats.txt"
python cli_app.py stat 1234 --default_output=stats.txt

# Read the content of file "1234" and print it to the console
python cli_app.py read 1234