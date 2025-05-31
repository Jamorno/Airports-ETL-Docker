import logging, psycopg2, os

class DataLoad:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    def load_data(self, df):
        try:
            cursor = self.conn.cursor()

            cursor.execute("DROP TABLE IF EXISTS airports_etl")

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS airports_etl
                (airport_name TEXT, airport_type TEXT, country_code TEXT, city TEXT, 
                latitude FLOAT, longitude FLOAT)"""
            )

            for _, row in df.iterrows():
                cursor.execute(
                    """INSERT INTO airports_etl 
                    (airport_name, airport_type, country_code, city, latitude, longitude) 
                    VALUES (%s, %s, %s, %s, %s, %s)""", (
                        row["airport_name"],
                        row["airport_type"],
                        row["country_code"],
                        row["city"],
                        row["latitude"],
                        row["longitude"]
                    )
                )

            self.conn.commit()
            logging.info(f"Loaded data to PostgresSQL {len(df)} completed.")

        except Exception as e:
            logging.error(f"DEBUG: Failed to load data to PostgresSQL: {e}")

        finally:
            cursor.close()
            self.conn.close()