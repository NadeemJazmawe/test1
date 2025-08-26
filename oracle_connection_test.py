from sqlalchemy import create_engine, text
import cx_Oracle
from langchain.sql_database import SQLDatabase  # Import SQLDatabase

try:
    # Initialize Oracle Client if not already done
    cx_Oracle.init_oracle_client(lib_dir="D:\\GingerPlay_off\\AQEGenAIService\\instantclient_19_9")

    # Connection string example
    engine = create_engine('oracle://GenAI_3UK_ABP:GenAI_ATT@illinabtsdbdev01:1521/ATSTSTDB')

    # Connect to the database
    with engine.connect() as connection:
        # Test the connection with a simple query
        result = connection.execute(text("SELECT 1 FROM DUAL"))
        for row in result:
            print(f"Connection Test Result: {row}")
        print("Connection established successfully!")
except Exception as e:
    print(f"Error connecting to the database: {e}")


# Define a mock or actual data_source_info object with required attributes
class DataSourceInfo:
    def __init__(self, config, db_filtered_tables, db_max_table_records):
        self.config = config
        self.db_filtered_tables = db_filtered_tables
        self.db_max_table_records = db_max_table_records

# Example initialization of data_source_info
data_source_info = DataSourceInfo(
    config="oracle://GenAI_3UK_ABP:GenAI_ATT@illinabtsdbdev01:1521/ATSTSTDB",
    db_filtered_tables=[],  # Replace with actual table names
    db_max_table_records=10  # Replace with the desired number of sample rows
)

connected_db = SQLDatabase.from_uri(data_source_info.config, include_tables=data_source_info.db_filtered_tables, sample_rows_in_table_info=data_source_info.db_max_table_records)

print(connected_db.dialect)