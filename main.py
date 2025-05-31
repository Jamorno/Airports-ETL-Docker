import logging
from etl.extracter import DataExtract
from etl.transformer import DataTransform
from etl.loader import DataLoad

logging.basicConfig(
    filename="airport.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run():
    extract = DataExtract("data/airports.csv")
    raw_data = extract.extract_data()

    if raw_data is not None:
        transform = DataTransform()
        df = transform.transform_data(raw_data)

        if not df.empty:
            load = DataLoad()
            load.load_data(df)
        else:
            logging.warning("Dataframe is empty. Skipping to load step.")

    else:
        logging.warning("No data extracted. Skipping transform and load step.")

if __name__ == "__main__":
    run()