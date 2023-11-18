import pandas as pd

def preprocess_data(data):
    # Convert data to DataFrame and perform preprocessing steps
    df = pd.DataFrame(data)
    # Example preprocessing steps
    df.fillna(method='ffill', inplace=True)
    return df

# Example usage
# preprocessed_data = preprocess_data(raw_data)
