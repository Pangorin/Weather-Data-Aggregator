import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def run():
    print("Starting load process...")

    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_port = os.getenv("DB_PORT")

    # Input validation for environment variables
    if not all([db_host, db_user, db_password, db_name, db_port]):
        print(f"Error: Database credentials not found in .env file.")
        print(f"Please ensure your .env file is correctly set up.")
        return
    
    # Check processed data file
    processed_file_path = "data/processed/processed_weather_data.csv"
    if not os.path.exists(processed_file_path):
        print(f"Error: Processed file not found at '{processed_file_path}'.")
        print(f"Please run (or rerun) transform script.")
        return
    
    # Create database connection
    try:
        # Connection string format for SQLAlchemy with mysql-connector
        # dialect+driver://username:password@host:port/database
        connection_string = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        # Create engine database
        engine = create_engine(connection_string)

        # Test connection (prevent error I'm so fking tired)
        connection = engine.connect()
        print(f"Successfully connected to MySQL database.")
        connection.close()

    except Exception as e:
        print(f"Error connecting to database: {e}")
        return
    
    # Load data into database
    try:
        df = pd.read_csv(processed_file_path)

        if df.empty:
            print("Processed data file is empty. No data to load.")
            return
        
        # Define target table name
        table_name = "weather_readings"

        # pandas.to_sql to load the DF into the database
        # 'append': Add new data. If the table has history, it will be preserved.
        # index=False: Prevents pandas from writing the DF index as a column.
        df.to_sql(table_name, con=engine, if_exists='append', index=False)

        print("-" * 50)
        print(f"Successfully loaded {len(df)} records into the {table_name}.")

    except FileNotFoundError:
        print(f"Error: The file {processed_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred during the data loading process: {e}")

if __name__ == "__main__":
    run()