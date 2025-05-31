import logging
import pandas as pd

class DataTransform:
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            select_columns = [
                "name",
                "type",
                "iso_country",
                "municipality",
                "latitude_deg",
                "longitude_deg"
            ]
            df = df[select_columns].copy()

            df = df.rename(columns={
                "name": "airport_name",
                "type": "airport_type",
                "iso_country": "country_code",
                "municipality": "city",
                "latitude_deg": "latitude",
                "longitude_deg": "longitude"
            })

            logging.info("Transformed data completed.")
            return df

        except Exception as e:
            logging.error(f"DEBUG: Failed to transform data: {e}")
            return pd.DataFrame()