import pandas as pd

class DataEncoder:
    def __init__(self, data):
        self.data = data
    
    def suggest_encoding(self):
        categorical_cols = []
        numeric_cols = []
        
        for col in self.data.columns:
            if self.data[col].dtype == 'object':
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
            num_unique_vals = self.data[categorical_cols].nunique()
            if (num_unique_vals / len(self.data)).mean() >= 0.5:
                print("Many categorical columns found. Suggesting One-Hot Encoding.")
                return 'one-hot'
            else:
                print("Few categorical columns found. Suggesting Binary Encoding.")
                return 'binary'
    
    def encode_data(self, encoding_type):
        if encoding_type == 'label':
            encoded_data = self.data.copy()
            for col in encoded_data.columns:
                if encoded_data[col].dtype == 'object':
                    encoded_data[col] = pd.factorize(encoded_data[col])[0]
            print("Label Encoding successful.")
            return encoded_data
        
        elif encoding_type == 'one-hot':
            encoded_data = pd.get_dummies(self.data)
            print("One-Hot Encoding successful.")
            return encoded_data
        
        elif encoding_type == 'binary':
            encoded_data = self.data.copy()
            for col in encoded_data.columns:
                if encoded_data[col].dtype == 'object':
                    binary_encoded = pd.get_dummies(encoded_data[col], prefix=col)
                    encoded_data = pd.concat([encoded_data, binary_encoded], axis=1)
                    encoded_data = encoded_data.drop(col, axis=1)
            print("Binary Encoding successful.")
            return encoded_data
        
        else:
            print("Invalid encoding type.")
            return None
