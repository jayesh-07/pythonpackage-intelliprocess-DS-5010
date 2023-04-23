import unittest
import pandas as pd
import os
from data_encoder import DataEncoder


# Load json file outlining all file paths for datasets in Testing_Datasets directory
cwd = os.getcwd()
json_data = '/Testing_Datasets/testing_datasets.json'
full_path = cwd + json_data
json_data = open(full_path).read()
testing_datasets = json.loads(json_data)
df = pd.read_csv(path + str(testing_datasets["data"]["sonar"]["datafile"]))
    ip = IntelliProcess(df)
    print(ip.suggest_encoding())
    print(ip.encode_data('label'))


class TestDataEncoder(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'category': ['A', 'B', 'C', 'A', 'B', 'B'],
            'number': [1, 2, 3, 4, 5, 6]
        })
        self.encoder = DataEncoder(self.data)

    def test_suggest_encoding_all_numeric(self):
        data = pd.DataFrame({'number': [1, 2, 3]})
        encoder = DataEncoder(data)
        self.assertIsNone(encoder.suggest_encoding())

    def test_suggest_encoding_single_categorical(self):
        data = pd.DataFrame({'category': ['A', 'B', 'C']})
        encoder = DataEncoder(data)
        self.assertEqual(encoder.suggest_encoding(), 'label')

    def test_suggest_encoding_many_categorical(self):
        self.assertEqual(self.encoder.suggest_encoding(), 'binary')

    def test_suggest_encoding_few_categorical(self):
        data = pd.DataFrame({
            'category1': ['A', 'B', 'C'],
            'category2': ['D', 'E', 'F'],
            'number': [1, 2, 3]
        })
        encoder = DataEncoder(data)
        self.assertEqual(encoder.suggest_encoding(), 'one-hot')

    def test_encode_data_label(self):
        encoded_data = self.encoder.encode_data('label')
        self.assertEqual(encoded_data['category'].tolist(), [0, 1, 2, 0, 1, 1])

    def test_encode_data_one_hot(self):
        encoded_data = self.encoder.encode_data('one-hot')
        self.assertEqual(encoded_data.values.tolist(), [
            [1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 1]
        ])

    def test_encode_data_binary(self):
        encoded_data = self.encoder.encode_data('binary')
        self.assertEqual(encoded_data.columns.tolist(), ['number', 'category_A', 'category_B', 'category_C'])
        self.assertEqual(encoded_data.values.tolist(), [
            [1, 1, 0, 0],
            [2, 0, 1, 0],
            [3, 0, 0, 1],
            [4, 1, 0, 0],
            [5, 0, 1, 0],
            [6, 0, 1, 0]
        ])

    def test_encode_data_invalid(self):
        self.assertIsNone(self.encoder.encode_data('invalid'))
