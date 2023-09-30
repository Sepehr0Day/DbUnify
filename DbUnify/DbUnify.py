import sqlite3 , pymysql , psycopg2 , pymongo , pyodbc , csv , json , matplotlib.pyplot as plt , xml.etree.ElementTree as ET , os , base64 , seaborn as sns 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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
            try:
                query = f"ALTER USER '{self.db_name}'@'localhost' IDENTIFIED BY '{password}';"
                self.execute_query(query)
            except Exception as e:
                raise RuntimeError(f"Error setting password: {str(e)}")
        elif self.db_type == 'postgresql':
            try:
                query = f"ALTER USER {self.db_name} WITH PASSWORD '{password}';"
                self.execute_query(query)
            except Exception as e:
                raise RuntimeError(f"Error setting password: {str(e)}")
        elif self.db_type == 'sqlserver':
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
            try:
                self.connection.isolation_level = None  
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

    def list_tables(self):
        """
        Get a list of all tables in the SQLite database.

        Returns:
            list: A list of table names.
        
        Raises:
            RuntimeError: If there is an error listing tables.
        """
        try:
            query = "SELECT name FROM sqlite_master WHERE type='table'"
            self.cursor.execute(query)
            tables = self.cursor.fetchall()
            return [table[0] for table in tables]
        except Exception as e:
            raise RuntimeError(f"Error listing tables: {str(e)}")

    def create_chart_database(self, output_directory, chart_type='bar', x_label='X Axis Label', y_label='Y Axis Label'):
        """
        Create charts for all tables in the database and save them as images.

        Args:
            output_directory (str): The directory where chart images will be saved.
            chart_type (str): The type of chart to create ('bar', 'line', 'scatter', etc.).
            x_label (str): Label for the x-axis.
            y_label (str): Label for the y-axis.

        Raises:
            RuntimeError: If there is an error creating charts or saving them as images.
        """
        try:
            os.makedirs(output_directory, exist_ok=True)
            tables = self.list_tables()

            for table_name in tables:
                data = self.search_all(table_name)
                x_values = [str(row[0]) for row in data] 
                y_values = [row[1] for row in data] 
                plt.figure(figsize=(8, 6))
                if chart_type == 'bar':
                    plt.bar(x_values, y_values)
                elif chart_type == 'line':
                    plt.plot(x_values, y_values, marker='o', linestyle='-')
                elif chart_type == 'scatter':
                    plt.scatter(x_values, y_values)
                elif chart_type == 'histogram':
                    plt.hist(y_values, bins='auto', edgecolor='k')
                else:
                    raise RuntimeError(f"Error, Type chart not found!")
                
                plt.xlabel(x_label)
                plt.ylabel(y_label)
                plt.title(f'{chart_type.capitalize()} Chart for Table: {table_name}')

                chart_filename = os.path.join(output_directory, f'{table_name}_{chart_type}_chart.png')
                plt.savefig(chart_filename)

                plt.close()

        except Exception as e:
            raise RuntimeError(f"Error creating charts: {str(e)}")

    def create_chart_table(self, table_name, x_column, y_column, x_label='X Axis Label', y_label='Y Axis Label', title='Chart Title', save_path='chart.png', chart_type='bar'):
        """
        Create a chart from data in the database and save it as an image.

        Args:
            table_name (str): Name of the database table to retrieve data from.
            x_column (int): Index of the x-axis column in the retrieved data.
            y_column (int): Index of the y-axis column in the retrieved data.
            x_label (str): Label for the x-axis.
            y_label (str): Label for the y-axis.
            title (str): Title of the chart.
            save_path (str): Path to save the chart image.
            chart_type (str): The type of chart to create ('bar', 'line', 'scatter', etc.).

        Raises:
            RuntimeError: If there is an error creating the chart or saving it as an image.
        """
        try:
            data = self.search_all(table_name)
            x_values = [row[x_column] for row in data]
            y_values = [row[y_column] for row in data]
            plt.figure(figsize=(8, 6))
            if chart_type == 'bar':
                plt.bar(x_values, y_values)
            elif chart_type == 'line':
                plt.plot(x_values, y_values, marker='o', linestyle='-')
            elif chart_type == 'scatter':
                plt.scatter(x_values, y_values)
            elif chart_type == 'histogram':
                plt.hist(y_values, bins='auto', edgecolor='k')
            else:
                raise RuntimeError(f"Error, Type chart not found!")
                
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.savefig(save_path)
            plt.close()

        except Exception as e:
            raise RuntimeError(f"Error creating chart: {str(e)}")

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
        
    def export_data_csv(self, table_name, csv_file_path):
        """
        Export data from a table to a CSV file.

        Args:
            table_name (str): The name of the table to export data from.
            csv_file_path (str): The path to save the exported CSV file.

        Raises:
            Exception: If there is an error during data export.
        """
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()

            with open(csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = [description[0] for description in self.cursor.description]
                csv_writer.writerow(header)
                csv_writer.writerows(rows)
        except Exception as e:
            raise Exception(f"Error exporting data: {str(e)}")

    def create_json_table(self, table_name):
        """
        Create a table to store JSON data.

        Args:
            table_name (str): The name of the table.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, json_data TEXT)"
                self.cursor.execute(query)
                self.connection.commit()
            else:
                raise NotImplementedError(f"JSON tables are not supported for {self.db_type}")
        except Exception as e:
            self.connection.rollback()
            raise e

    def create_xml_table(self, table_name):
        """
        Create a table to store XML data.

        Args:
            table_name (str): The name of the table.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, xml_data TEXT)"
                self.cursor.execute(query)
                self.connection.commit()
            else:
                raise NotImplementedError(f"XML tables are not supported for {self.db_type}")
        except Exception as e:
            self.connection.rollback()
            raise e

    def insert_json_data(self, table_name, json_data):
        """
        Insert JSON data into a JSON table.

        Args:
            table_name (str): The name of the JSON table.
            json_data (dict): The JSON data to insert.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                json_str = json.dumps(json_data)
                query = f"INSERT INTO {table_name} (json_data) VALUES (?)"
                self.cursor.execute(query, (json_str,))
                self.connection.commit()
            else:
                raise NotImplementedError(f"JSON data insertion is not supported for {self.db_type}")
        except Exception as e:
            self.connection.rollback()
            raise e

    def insert_xml_data(self, table_name, xml_data):
        """
        Insert XML data into an XML table.

        Args:
            table_name (str): The name of the XML table.
            xml_data (str): The XML data to insert as a string.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                query = f"INSERT INTO {table_name} (xml_data) VALUES (?)"
                self.cursor.execute(query, (xml_data,))
                self.connection.commit()
            else:
                raise NotImplementedError(f"XML data insertion is not supported for {self.db_type}")
        except Exception as e:
            self.connection.rollback()
            raise e

    def retrieve_json_data(self, table_name, record_id):
        """
        Retrieve JSON data from a JSON table.

        Args:
            table_name (str): The name of the JSON table.
            record_id (int): The ID of the record to retrieve.

        Returns:
            dict: The retrieved JSON data.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                query = f"SELECT json_data FROM {table_name} WHERE id = ?"
                self.cursor.execute(query, (record_id,))
                result = self.cursor.fetchone()
                if result:
                    return json.loads(result[0])
                else:
                    return None
            else:
                raise NotImplementedError(f"JSON data retrieval is not supported for {self.db_type}")
        except Exception as e:
            raise e

    def retrieve_xml_data(self, table_name, record_id):
        """
        Retrieve XML data from an XML table.

        Args:
            table_name (str): The name of the XML table.
            record_id (int): The ID of the record to retrieve.

        Returns:
            str: The retrieved XML data as a string.
        """
        try:
            if self.db_type in ['sqlite', 'mysql', 'postgresql']:
                query = f"SELECT xml_data FROM {table_name} WHERE id = ?"
                self.cursor.execute(query, (record_id,))
                result = self.cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
            else:
                raise NotImplementedError(f"XML data retrieval is not supported for {self.db_type}")
        except Exception as e:
            raise e

    def export_to_pdf(self, table_name, pdf_file_path,
                      background_color=None, text_color=None,
                      font_name=None, font_size=12):
        """
        Export data from a database table to a PDF document with customizable styles.

        Args:
            table_name (str): The name of the database table to export data from.
            pdf_file_path (str): The path to save the exported PDF file.
            background_color (str): Background color for the table cells (e.g., 'lightblue').
            text_color (str): Text color for the table cells (e.g., 'black').
            font_name (str): Font name for the table text (e.g., 'Helvetica').
            font_size (int): Font size for the table text.

        Raises:
            Exception: If there is an error during data export.
        """
        try:
            data = self.search_all(table_name)
            doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
            if font_name:
                pdfmetrics.registerFont(TTFont('CustomFont', font_name))
            table_data = [list(description[0] for description in self.cursor.description)] + [list(row) for row in data]
            table = Table(table_data)
            table_style = [
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), font_name or 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('GRID', (0, 1), (-1, -1), 1, colors.black),
            ]

            if background_color:
                table_style.append(('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(background_color)))

            if text_color:
                table_style.append(('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor(text_color)))

            table.setStyle(TableStyle(table_style))
            doc.build([table])
        except Exception as e:
            raise Exception(f"Error exporting data to PDF: {str(e)}")

    def insert_base64(self, table_name, data_dict):
        """
        Insert base64 encoded data into a database table.

        Args:
            table_name (str): Name of the table to insert data into.
            data_dict (dict): A dictionary where keys are column names, and values are data to be encoded and inserted.

        Raises:
            RuntimeError: If there is an error inserting the data.
        """
        try:
            encoded_data_dict = {column: base64.b64encode(data.encode()).decode() for column, data in data_dict.items()}
            columns = ', '.join(encoded_data_dict.keys())
            values = ', '.join(['?' for _ in encoded_data_dict])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.execute_query(query, *encoded_data_dict.values())
        except Exception as e:
            raise RuntimeError(f"Error inserting base64 data: {str(e)}")

    def read_base64(self, table_name):
        """
        Read and decode base64 encoded data from a database table.

        Args:
            table_name (str): Name of the table to read data from.

        Returns:
            dict: A dictionary where keys are column names, and values are decoded data as bytes.

        Raises:
            RuntimeError: If there is an error selecting or decoding the data.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            self.cursor.execute(query)
            row = self.cursor.fetchone()

            if row:
                column_names = [description[0] for description in self.cursor.description]
                decoded_data = {column_names[i]: base64.b64decode(row[i]) for i in range(len(row))}
                return decoded_data
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Error reading and decoding base64 data: {str(e)}")

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
