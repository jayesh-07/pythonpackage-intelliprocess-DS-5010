class DataEncoder:
    """
    A class to suggest and perform encoding on categorical data in a pandas DataFrame.
    """

    def __init__(self, data):
        """
        Initializes a new instance of the DataEncoder class.

        Parameters:
            data (pandas.DataFrame): The input data to encode.
        """
        self.data = data

    def suggest_encoding(self):
        """
        Suggests the appropriate encoding method to use for the data.

        Returns:
            str: The suggested encoding method ('label', 'one-hot', or 'binary').
        """
        categorical_cols = []
        numeric_cols = []

        for col in self.data.columns:
            if isinstance(self.data[col][0], str):
                categorical_cols.append(col)
            else:
                numeric_cols.append(col)

        if len(categorical_cols) == 0:
            print("All columns are numeric. No encoding required.")
            return None

        elif len(categorical_cols) == 1:
            print("Single categorical column found. Suggesting Label Encoding.")
            return 'label'

        else:
            num_unique_vals = self.data[categorical_cols].apply(set).apply(len)
            if (num_unique_vals / len(self.data)).mean() >= 0.5:
                print("Many categorical columns found. Suggesting One-Hot Encoding.")
                return 'one-hot'
            else:
                print("Few categorical columns found. Suggesting Binary Encoding.")
                return 'binary'

    def encode_data(self, encoding_type):
        """
        Encodes the data using the specified encoding method.

        Parameters:
            encoding_type (str): The encoding method to use ('label', 'one-hot', or 'binary').

        Returns:
            pandas.DataFrame: The encoded data.
        """
        if encoding_type == 'label':
            encoded_data = self.data.copy()
            label_encoders = {}
            for col in encoded_data.columns:
                if isinstance(encoded_data[col][0], str):
                    labels = list(set(encoded_data[col]))
                    label_encoders[col] = {label: idx for idx, label in enumerate(labels)}
                    encoded_data[col] = encoded_data[col].apply(lambda x: label_encoders[col][x])
            print("Label Encoding successful.")
            return encoded_data

        elif encoding_type == 'one-hot':
            encoded_data = []
            for col in self.data.columns:
                if isinstance(self.data[col][0], str):
                    labels = list(set(self.data[col]))
                    for label in labels:
                        new_col = [int(x == label) for x in self.data[col]]
                        encoded_data.append(new_col)
                else:
                    encoded_data.append(list(self.data[col]))
            encoded_data = pd.DataFrame(encoded_data).transpose()
            print("One-Hot Encoding successful.")
            return encoded_data

        elif encoding_type == 'binary':
            encoded_data = self.data.copy()
            for col in encoded_data.columns:
                if isinstance(encoded_data[col][0], str):
                    labels = list(set(encoded_data[col]))
                    for label in labels:
                        new_col = [int(x == label) for x in encoded_data[col]]
                        new_col_name = col + '_' + label
                        encoded_data[new_col_name] = new_col
                    encoded_data = encoded_data.drop(col, axis=1)
            print("Binary Encoding successful.")
            return encoded_data

        else:
            print("Invalid encoding type.")
            return None
