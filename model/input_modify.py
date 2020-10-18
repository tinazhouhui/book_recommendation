import pandas as pd


def convert_to_utf(path):
    data = pd.read_csv(path, encoding='latin-1')
    data.to_csv(path, encoding='utf-8', index=False)