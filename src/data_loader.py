import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        # Load the original CSV file
        df = pd.read_csv(self.original_csv)

        # Basic processing: drop duplicates and handle missing values
        df.drop_duplicates(inplace=True)
        df.fillna("Unknown", inplace=True)

        # Save the processed data to a new CSV file
        df.to_csv(self.processed_csv, index=False)

        return df