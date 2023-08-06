# Telegram Contact Extractor

The "Telegram Contact Extractor" is a Python script named `extractor.py` designed to extract contact information from a data file exported from Telegram Desktop application. The script reads the data from the provided JSON file (`result.json`), processes it, and then generates a CSV file (`contacts.csv`) containing a list of contacts with their names and phone numbers.

## Requirements

Before running the script, make sure you have the following requirements installed on your system:

- Python 3.x
- pandas library

You can install pandas using pip:

```bash
pip install pandas
```

## How to Use

1. Export Data from Telegram Desktop:
   - Open Telegram Desktop application.
   - Go to **Settings** > **Advanced** > **Export Telegram Data**.
   - Select the "Contact List" option and export the data to a file named `result.json`.

2. Place the Script and Data File:
   - Place the `extractor.py` script and the `result.json` file in the same directory.

3. Run the Script:
   - Open a terminal or command prompt in the directory where the script and data file are located.
   - Execute the following command to run the script:

   ```bash
   python extractor.py
   ```

4. Output:
   - The script will process the data from `result.json` and create a new CSV file named `contacts.csv`.
   - The CSV file will contain two columns: `Name` and `Phone`, representing the contact's full name and phone number, respectively.

## Note

- The `result.json` file must be in the correct format exported from Telegram Desktop. The script assumes that the JSON file follows the Telegram export format for contacts.
- The script uses the `pandas` library to handle data processing and exporting to CSV. Make sure you have installed this library before running the script.
- The script will create a new `contacts.csv` file each time it is executed. If you run the script multiple times, it will overwrite the previous `contacts.csv` file.

## Disclaimer

This script is provided as-is and without any warranty. Please use it responsibly and ensure that you have proper authorization to access and process the data from Telegram. The authors of this script are not responsible for any misuse or consequences resulting from its use.

## Contributions

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the project's repository. Your contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the script according to the terms of the MIT License.