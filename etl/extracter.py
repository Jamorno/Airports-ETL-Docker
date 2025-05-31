import logging
import pandas as pd

class DataExtract:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def extract_data(self):
        try:
            df = pd.read_csv(self.csv_file)
            logging.info("Extracted csv data completed.")
            logging.info(f"Total rows extracted {len(df)}")
            return df

        except Exception as e:
            logging.info(f"DEBUG: Failed to extract csv from {self.csv_file}: {e}")
            return pd.DataFrame()