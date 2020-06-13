import unittest
from parser import TrickyParser
import os, os.path

tricky = TrickyParser("file.xls", "test_files")


class ParserTest(unittest.TestCase):
    def test_creation(self):
        self.assertIsInstance(tricky, TrickyParser)

    def test_parsed_file(self):
        # Test that number of data sheets = 3
        self.assertEqual(len(tricky.data_list), 3)

    def test_csv_generation(self):
        tricky.to_csv()
        files = [name for name in os.listdir(tricky.output_folder) if
                 os.path.isfile(tricky.output_folder + "/" + name) and name.lower().endswith(".csv")]
        files_count = len(files)
        self.assertEqual(files_count, 3)

    def test_json_generation(self):
        tricky.to_json()
        files_count = len([name for name in os.listdir(tricky.output_folder) if
                           os.path.isfile(tricky.output_folder + "/" + name) and name.lower().endswith(".json")])
        self.assertEqual(files_count, 3)

    def test_excel_generation(self):
        tricky.to_excel()
        files_count = len([name for name in os.listdir(tricky.output_folder) if
                           os.path.isfile(tricky.output_folder + "/" + name) and name.lower().endswith(".xlsx")])
        self.assertEqual(files_count, 3)


if __name__ == '__main__':
    unittest.main()
