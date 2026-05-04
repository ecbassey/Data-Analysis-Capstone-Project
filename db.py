import pandas as pd
import sqlite3


class DatabaseManager:
    def __init__(self, df):
        self.df = df
    # def __init__(self, db_name = "Airline_delay.db"):
    #     self.conn = sqlite3.connect(db_name)
    #     self.cursor = self.conn.cursor()

    #def save_table(self, df, table_name):
    #    df.to_sql(table_name, self.conn, if_exists='replace', index=False)

    def query(self, sql_query):
        return pd.read_sql(sql_query, self.conn)
    
    def add_column(self, table_name, column_name, data_type):
        self.cursor.execute(f"""
        ALTER TABLE {table_name}
        ADD COLUMN {column_name} {data_type};
        """)
        self.conn.commit()
    
    def execute2(self, sql_query):
        self.cursor.execute(sql_query)
        self.conn.commit()

    def execute(self, sql_query, params=None):
        if params:
            self.cursor.execute(sql_query, params)
        else:
            self.cursor.execute(sql_query)
        self.conn.commit()

    def close(self):
        self.conn.close()