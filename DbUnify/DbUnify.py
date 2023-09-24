import sqlite3
import pymysql
import psycopg2
import pymongo
import pyodbc

class DatabaseManager:
    def __init__(self, db_type, db_name, password=None, **kwargs):
        """
        Initialize the DatabaseManager instance.

        Args:
            db_type (str): The type of the database ('sqlite', 'mysql', 'postgresql', 'mongodb', 'sqlserver').
            db_name (str): The name of the database or connection URI.
            password (str): The password for the database (if required).
            **kwargs: Additional keyword arguments specific to each database type.

        Raises:
            ConnectionError: If there is an error connecting to the database.
        """
        self.db_type = db_type
        self.db_name = db_name
        self.connection = None

        # Set the password if provided and supported by the database
        if password is not None and self.db_type in ['mysql', 'postgresql', 'sqlserver']:
            kwargs['password'] = password

        try:
            if db_type == 'sqlite':
                self.connection = sqlite3.connect(db_name)
            elif db_type == 'mysql':
                self.connection = pymysql.connect(database=db_name, **kwargs)
            elif db_type == 'postgresql':
                self.connection = psycopg2.connect(database=db_name, **kwargs)
            elif db_type == 'mongodb':
                self.connection = pymongo.MongoClient(**kwargs)
            elif db_type == 'sqlserver':
                self.connection = pyodbc.connect(**kwargs)
            else:
                raise ValueError(f"Unsupported database type: {db_type}")
        except Exception as e:
            raise ConnectionError(f"Error connecting to the database: {str(e)}")

        self.cursor = self.connection.cursor()

    def set_password(self, password):
        """
        Set a new password for the database user.

        Args:
            password (str): The new password.

        Raises:
            RuntimeError: If there is an error setting the password.
        """
        if self.db_type == 'mysql':
            # Change password in MySQL
            try:
                query = f"ALTER USER '{self.db_name}'@'localhost' IDENTIFIED BY '{password}';"
                self.execute_query(query)
            except Exception as e:
                raise RuntimeError(f"Error setting password: {str(e)}")
        elif self.db_type == 'postgresql':
            # Change password in PostgreSQL
            try:
                query = f"ALTER USER {self.db_name} WITH PASSWORD '{password}';"
                self.execute_query(query)
            except Exception as e:
                raise RuntimeError(f"Error setting password: {str(e)}")
        elif self.db_type == 'sqlserver':
            # Change password in SQL Server
            try:
                query = f"ALTER LOGIN {self.db_name} WITH PASSWORD = '{password}';"
                self.execute_query(query)
            except Exception as e:
                raise RuntimeError(f"Error setting password: {str(e)}")
            
    def transaction(self):
        """
        Start a database transaction.

        Returns:
            transaction: A database transaction object.

        Raises:
            RuntimeError: If there is an error starting the transaction.
        """
        if self.db_type == 'sqlite':
            # Start a transaction in SQLite
            try:
                self.connection.isolation_level = None  # Turn off automatic transactions
                transaction = self.connection.cursor()
                return transaction
            except Exception as e:
                raise RuntimeError(f"Error starting transaction: {str(e)}")
        else:
            raise ValueError(f"Transaction management not supported for {self.db_type}")

    def backup_database(self, backup_path):
        """
        Create a backup of the database.

        Args:
            backup_path (str): The path where the backup should be stored.

        Returns:
            bool: True if the backup was successful, False otherwise.

        Raises:
            RuntimeError: If there is an error creating the database backup.
        """
        if self.db_type == 'sqlite':
            try:
                import shutil
                shutil.copyfile(self.db_name, backup_path)
                return True
            except Exception as e:
                raise RuntimeError(f"Error creating database backup: {str(e)}")
        elif self.db_type == 'mongodb':
            try:
                self.connection.admin.command('copydb', fromdb=self.db_name, todb=backup_path)
                return True
            except Exception as e:
                raise RuntimeError(f"Error creating database backup: {str(e)}")
        else:
            raise ValueError(f"Database backup not supported for {self.db_type}")

    def restore_database(self, backup_path):
        """
        Restore the database from a backup.

        Args:
            backup_path (str): The path to the backup file.

        Returns:
            bool: True if the restore was successful, False otherwise.

        Raises:
            RuntimeError: If there is an error restoring the database.
        """
        if self.db_type == 'sqlite':
            try:
                import shutil
                shutil.copyfile(backup_path, self.db_name)
                return True
            except Exception as e:
                raise RuntimeError(f"Error restoring database: {str(e)}")
        elif self.db_type == 'mongodb':
            try:
                self.connection.admin.command('copydb', fromdb=backup_path, todb=self.db_name)
                return True
            except Exception as e:
                raise RuntimeError(f"Error restoring database: {str(e)}")
        else:
            raise ValueError(f"Database restore not supported for {self.db_type}")

    def execute_query(self, query, *args):
        """
        Execute a database query.

        Args:
            query (str): The SQL query to be executed.
            *args: Parameters to be passed to the query.

        Raises:
            RuntimeError: If there is an error executing the query.
        """
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise RuntimeError(f"Error executing query: {str(e)}")

    def fetch_all(self, query, *args):
        """
        Execute a query and fetch all results.

        Args:
            query (str): The SQL query to be executed.
            *args: Parameters to be passed to the query.

        Returns:
            list: List of fetched rows.

        Raises:
            RuntimeError: If there is an error fetching data.
        """
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()
        except Exception as e:
            raise RuntimeError(f"Error fetching data: {str(e)}")

    def create_table(self, table_name, columns):
        """
        Create a table in the database.

        Args:
            table_name (str): Name of the table to be created.
            columns (list): List of tuples containing column names and data types.

        Raises:
            RuntimeError: If there is an error creating the table.
        """
        try:
            if self.db_type == 'sqlite':
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns])})"
            elif self.db_type in ['mysql', 'postgresql', 'sqlserver']:
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns])})"
            else:
                raise ValueError(f"Table creation not supported for {self.db_type}")
            self.execute_query(query)
        except Exception as e:
            raise RuntimeError(f"Error creating table: {str(e)}")

    def drop_table(self, table_name):
        """
        Drop a table from the database.

        Args:
            table_name (str): Name of the table to be dropped.

        Raises:
            RuntimeError: If there is an error dropping the table.
        """
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.execute_query(query)
        except Exception as e:
            raise RuntimeError(f"Error dropping table: {str(e)}")

    def add_column(self, table_name, column_name, data_type):
        """
        Add a column to an existing table.

        Args:
            table_name (str): Name of the table to add the column to.
            column_name (str): Name of the column to be added.
            data_type (str): Data type of the column.

        Raises:
            RuntimeError: If there is an error adding the column.
        """
        try:
            query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}"
            self.execute_query(query)
        except Exception as e:
            raise RuntimeError(f"Error adding column: {str(e)}")

    def insert_row(self, table_name, values):
        """
        Insert a row into the table.

        Args:
            table_name (str): Name of the table to insert the row into.
            values (dict): Dictionary of column-value pairs for the row.

        Raises:
            RuntimeError: If there is an error inserting the row.
        """
        try:
            columns = ', '.join(values.keys())
            placeholders = ', '.join(['?' for _ in values])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.execute_query(query, *values.values())
        except Exception as e:
            raise RuntimeError(f"Error inserting row: {str(e)}")

    def delete_column(self, table_name, column_name):
        """
        Delete a column from the table.

        Args:
            table_name (str): Name of the table to delete the column from.
            column_name (str): Name of the column to be deleted.

        Raises:
            RuntimeError: If there is an error deleting the column.
        """
        try:
            query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
            self.execute_query(query)
        except Exception as e:
            raise RuntimeError(f"Error deleting column: {str(e)}")

    def delete_row(self, table_name, condition):
        """
        Delete a row from the table based on a condition.

        Args:
            table_name (str): Name of the table to delete the row from.
            condition (str): Condition for row deletion.

        Raises:
            RuntimeError: If there is an error deleting the row.
        """
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.execute_query(query)
        except Exception as e:
            raise RuntimeError(f"Error deleting row: {str(e)}")

    def update_row(self, table_name, values, condition):
        """
        Update a row in the table based on a condition.

        Args:
            table_name (str): Name of the table to update the row in.
            values (dict): Dictionary of column-value pairs to be updated.
            condition (str): Condition for row update.

        Raises:
            RuntimeError: If there is an error updating the row.
        """
        try:
            set_clause = ', '.join([f"{key} = ?" for key in values])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            self.execute_query(query, *values.values())
        except Exception as e:
            raise RuntimeError(f"Error updating row: {str(e)}")

    def search_one(self, table_name, condition):
        """
        Search for a single row in the table based on a condition.

        Args:
            table_name (str): Name of the table to search in.
            condition (str): Condition for row search.

        Returns:
            tuple: A tuple representing the fetched row.

        Raises:
            RuntimeError: If there is an error searching for a row.
        """
        try:
            query = f"SELECT * FROM {table_name} WHERE {condition} LIMIT 1"
            rows = self.fetch_all(query)
            if rows:
                return rows[0]
            return None
        except Exception as e:
            raise RuntimeError(f"Error searching for one row: {str(e)}")

    def search_all(self, table_name):
        """
        Search for all rows in the table.

        Args:
            table_name (str): Name of the table to search in.

        Returns:
            list: List of tuples representing the fetched rows.

        Raises:
            RuntimeError: If there is an error searching for rows.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            return self.fetch_all(query)
        except Exception as e:
            raise RuntimeError(f"Error searching for all rows: {str(e)}")

    def close(self):
        """
        Close the database connection.

        Raises:
            ConnectionError: If there is an error closing the connection.
        """
        try:
            self.connection.close()
        except Exception as e:
            raise ConnectionError(f"Error closing the database connection: {str(e)}")
