import pandas as pd
import os


class TrickyParser():

    def __init__(self, file_path, output_folder=".", output_format="csv"):
        """
        Create a new instance of Parser, a simple way to parse and clean a specific format of a web data file
        :param file_path: The path of the file that needs to be parsed
        :param output_folder: The folder in which the files should be generated
        :param output_format: The format of the generated files [csv, json, excel]
        """

        # Check if file exists
        if not file_path:
            print("Ÿou need to provide a valid string path")
            return

        self.output_folder = output_folder
        self.output_format = output_format
        self.data_list = pd.read_html(file_path, header=0)

        # locations should be cleaned
        if len(self.data_list) == 3:
            self.df_locations = self.data_list[1][self.data_list[1]['LocationID'].apply(lambda x: str(x).isnumeric())]
            self.filters = self.extract_filters()
            self.transactions_df = self.data_list[2]

    def extract_filters(self):
        """
        A Helper method to extract the filters from the Location Sheet
        :return: A Pandas DataFrame Created from the filters dictionary
        """
        filters_dict = {}
        try:
            filters = self.data_list[1][self.data_list[1]['LocationID'].apply(lambda x: not str(x).isnumeric())]
            filters_dict = {
                "Locations": list(filters[filters["LocationID"] == "Locations"]["Name"]),
                "Date From": list(filters[filters["LocationID"] == "Date From"]["Name"])[0],
                "Date To": list(filters[filters["LocationID"] == "Date To"]["Name"])[0]
            }

        except Exception as err:
            print(err)

        return pd.DataFrame.from_dict(filters_dict)

    def check_create_output_folder(self):
        """
        Checks if output folder exists and creates one if it doesn't
        """
        # Check if output folder exists
        try:
            if self.output_folder != ".":
                if not os.path.exists(self.output_folder):
                    os.mkdir(self.output_folder)

        except Exception as err:
            print(err)

    def to_csv(self):
        """
        Generates 3 csv files for the locations, transactions and filters
        """
        self.check_create_output_folder()
        self.df_locations.to_csv(self.output_folder + "/locations.csv")
        self.transactions_df.to_csv(self.output_folder + "/transactions.csv")
        self.filters.to_csv(self.output_folder + "/filters.csv")

    def to_json(self):
        """
        Generates 3 json files for the locations, transactions and filters
        """
        self.check_create_output_folder()
        self.df_locations.to_json(self.output_folder + "/locations.json")
        self.transactions_df.to_json(self.output_folder + "/transactions.json")
        self.filters.to_json(self.output_folder + "/filters.json")

    def to_excel(self):
        """
        Generates 3 excel files for the locations, transactions and filters
        """
        self.check_create_output_folder()
        self.df_locations.to_excel(self.output_folder + "/locations.xlsx")
        self.transactions_df.to_excel(self.output_folder + "/transactions.xlsx")
        self.filters.to_excel(self.output_folder + "/filters.xlsx")

    def generate_clean_files(self):
        """
        Generates the cleaned files in the specified output_format
        """
        if self.output_format == "csv":
            self.to_csv()
        elif self.output_format == "json":
            self.to_json()
        elif self.output_format == "json":
            self.to_excel()
        else:
            print("{} is not supported".format(self.output_format))
