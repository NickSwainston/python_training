from my_package.data_processing import input_data
from my_package.plotting import molleweide_plot


def main():
    print("Reading the data")
    df = input_data("pulsars.csv")

    print("Plotting the data")
    molleweide_plot(df)

if __name__ == "__main__":
    main()