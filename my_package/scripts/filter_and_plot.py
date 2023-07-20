import argparse

from my_package.data_processing import input_data
from my_package.plotting import molleweide_plot
from my_package.data_load import PULSAR_CSV_PATH


def main():
    # Create an argument parser so users can understand and use command line options
    parser = argparse.ArgumentParser(description='Process and filter an input CSV file and create a sky plot of the sources.')

    # Add arguments to the parser
    parser.add_argument(
        # A short version of the argument which is normally a single dash and a single letter
        '-i',
        # A long version of the argument which is normally two dashes and a word
        '--input',
        # The type of the argument that will be converted when it is read in
        type=str,
        # A description of what the argument does
        help='The path to the input csv file. If none provided, use the default pulsar data file',
        # The default value of the argument if none is provided
        default=PULSAR_CSV_PATH,
    )

    # Parse the arguments
    args = parser.parse_args()
    print(args.input)
    print("Reading the data")
    df = input_data(args.input)

    print("Plotting the data")
    molleweide_plot(df)

if __name__ == "__main__":
    main()