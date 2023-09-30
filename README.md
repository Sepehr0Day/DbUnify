# DbUnify | Database Management DbUnify

**DbUnify** (Database Management DbUnify) is your all-in-one solution for simplifying database connectivity in Python projects. With DbUnify, you can effortlessly manage connections to various popular databases, streamlining your development process and saving valuable time.

## Key Features:

1. **Database Freedom**: DbUnify supports a wide range of database types, including SQLite, MySQL, PostgreSQL, MongoDB and SQL Server, providing a unified interface for all your database needs.

2. **Clean and Versatile API**: Enjoy the convenience of a clean and versatile API that ensures consistency across different database platforms. Say goodbye to scattered code and complexity.

3. **Password Management**: DbUnify simplifies password management by allowing you to update passwords for MySQL, PostgreSQL and SQL Server databases, enhancing security practices.

4. **Robust Exception Handling**: Database operations can be error-prone, but DbUnify excels in handling exceptions, offering clear and informative error messages for efficient troubleshooting.

5. **User-Friendly**: Whether you're a seasoned developer or a beginner, DbUnify offers a user-friendly experience. Initialize connections, execute queries, and manage passwords with ease.

6. **Cross-Platform Compatibility**: DbUnify is designed for seamless operation across different platforms, ensuring consistent behavior in your Python projects, regardless of your development environment.

7. **JSON and XML Support**: Now you can work seamlessly with JSON and XML data formats, making DbUnify even more versatile for your projects.

8. **Data Visualization**: Easily create various charts directly from your database or table outputs, allowing you to present data visually.

9. **Export to PDF and Excel**: Generate and export reports in PDF and Excel formats effortlessly, simplifying collaboration and data sharing.

10. **Support From Base64**: DbUnify introduces support for Base64 encoding and decoding, making it easy to handle binary data, ensuring data integrity, and enhancing portability in Python projects.

## Get Started with DbUnify

Join the community of developers who have already embraced DbUnify to simplify their database interactions and improve productivity. Start coding efficiently and focus on building exceptional applications.

Don't miss out on the opportunity to simplify your database connectivity. Try DbUnify today and experience the difference it can make in your projects!

##

**Note!**

The project is in early versions and some codes may contain bugs. If you encounter a bug, please don't hesitate to send a message to my ID via [Telegram](https://t.me/sepehr0day).

#

# Supported Databases

DbUnify (Database Management DbUnify) library provides seamless connectivity to various popular databases. You can use DbUnify to interact with the following databases:

1. **SQLite**: A self-contained, serverless, and zero-configuration database engine, ideal for embedded systems and lightweight applications.

2. **MySQL**: A widely-used open-source relational Database Management system known for its performance, scalability, and robust feature set.

3. **PostgreSQL**: A powerful open-source relational database system known for its advanced features, extensibility, and reliability.

4. **MongoDB**: A NoSQL database that excels in flexibility and scalability, making it suitable for handling unstructured or semi-structured data.

5. **SQL Server**: A robust relational Database Management system developed by Microsoft, known for its enterprise-level capabilities.

DbUnify offers a unified interface for connecting to and managing these databases, streamlining your database-related tasks and enhancing your development experience.

Choose the database that best fits your project's requirements and harness the power of DbUnify to simplify your database connectivity.

## Install
```bash
pip3 install DbUnify
```

## Class: DatabaseManager

### Method: `__init__`
The constructor for the "DatabaseManager" class.

**Parameters:**

- `db_type` (`str`): The type of the database ('sqlite', 'mysql', 'postgresql', 'mongodb', 'sqlserver').
- `db_name` (`str`): The name of the database or connection URI.
- `password` (`str`): The password for the database (if required).
- `**kwargs`: Additional keyword arguments specific to each database type.

**Raises:**

- `ConnectionError`: If there is an error connecting to the database.

### Method: `set_password`
Sets a new password for the database user.

**Parameters:**

- `password` (`str`): The new password.

**Raises:**

- `RuntimeError`: If there is an error setting the password.

### Method: `transaction`
Starts a database transaction.

**Returns:**

- `transaction`: A database transaction object.

**Raises:**

- `RuntimeError`: If there is an error starting the transaction.

### Method: `backup_database`
Creates a backup of the database.

**Parameters:**

- `backup_path` (`str`): The path where the backup should be stored.

**Returns:**

- `bool`: True if the backup was successful, False otherwise.

**Raises:**

- `RuntimeError`: If there is an error creating the database backup.

### Method: `restore_database`
Restores the database from a backup.

**Parameters:**

- `backup_path` (`str`): The path to the backup file.

**Returns:**

- `bool`: True if the restore was successful, False otherwise.

**Raises:**

- `RuntimeError`: If there is an error restoring the database.

### Method: `execute_query`
Executes a database query.

**Parameters:**

- `query` (`str`): The SQL query to be executed.
- `*args`: Parameters to be passed to the query.

**Raises:**

- `RuntimeError`: If there is an error executing the query.

### Method: `fetch_all`
Executes a query and fetches all results.

**Parameters:**

- `query` (`str`): The SQL query to be executed.
- `*args`: Parameters to be passed to the query.

**Returns:**

- `list`: List of fetched rows.

**Raises:**

- `RuntimeError`: If there is an error fetching data.

### Method: `create_table`
Creates a table in the database.

**Parameters:**

- `table_name` (`str`): Name of the table to be created.
- `columns` (`list`): List of tuples containing column names and data types.

**Raises:**

- `RuntimeError`: If there is an error creating the table.

### Method: `drop_table`
Drops a table from the database.

**Parameters:**

- `table_name` (`str`): Name of the table to be dropped.

**Raises:**

- `RuntimeError`: If there is an error dropping the table.

### Method: `add_column`
Adds a column to an existing table.

**Parameters:**

- `table_name` (`str`): Name of the table to add the column to.
- `column_name` (`str`): Name of the column to be added.
- `data_type` (`str`): Data type of the column.

**Raises:**

- `RuntimeError`: If there is an error adding the column.

### Method: `insert_row`
Inserts a row into the table.

**Parameters:**

- `table_name` (`str`): Name of the table to insert the row into.
- `values` (`dict`): Dictionary of column-value pairs for the row.

**Raises:**

- `RuntimeError`: If there is an error inserting the row.

### Method: `delete_column`
Deletes a column from the table.

**Parameters:**

- `table_name` (`str`): Name of the table to delete the column from.
- `column_name` (`str`): Name of the column to be deleted.

**Raises:**

- `RuntimeError`: If there is an error deleting the column.

### Method: `delete_row`
Deletes a row from the table based on a condition.

**Parameters:**

- `table_name` (`str`): Name of the table to delete the row from.
- `condition` (`str`): Condition for row deletion.

**Raises:**

- `RuntimeError`: If there is an error deleting the row.

### Method: `update_row`
Updates a row in the table based on a condition.

**Parameters:**

- `table_name` (`str`): Name of the table to update the row in.
- `values` (`dict`): Dictionary of column-value pairs to be updated.
- `condition` (`str`): Condition for row update.

**Raises:**

- `RuntimeError`: If there is an error updating the row.

### Method: `search_one`
Searches for a single row in the table based on a condition.

**Parameters:**

- `table_name` (`str`): Name of the table to search in.
- `condition` (`str`): Condition for row search.

**Returns:**

- `tuple`: A tuple representing the fetched row.

**Raises:**

- `RuntimeError`: If there is an error searching for one row.

### Method: `search_all`
Searches for all rows in the table.

**Parameters:**

- `table_name` (`str`): Name of the table to search in.

**Returns:**

- `list`: List of tuples representing the fetched rows.

**Raises:**

- `RuntimeError`: If there is an error searching for rows.

### Method: `create_chart_database`

#### Supported 4 type chart
- bar
- line
- scatter
- histogram

Create charts for all tables in the database and save them as images.

#### Parameters:

- `output_directory` (`str`): The directory where chart images will be saved.
- `chart_type` (`str`, optional): The type of chart to create ('bar', 'line', 'scatter', 'histogram'). Default is 'bar'.
- `x_label` (`str`, optional): Label for the x-axis. Default is 'X Axis Label'.
- `y_label` (`str`, optional): Label for the y-axis. Default is 'Y Axis Label'.

#### Returns:

This method does not return any value.

#### Raises:

- `RuntimeError`: If there is an error creating charts or saving them as images.

#### Example Usage:

```python
db.create_chart_database(output_directory='charts_directory', chart_type='line', x_label='Time', y_label='Values')
```

### Method: `create_chart_table`

Create a chart from data in the database and save it as an image.

#### Supported 4 type chart
- bar
- line
- scatter
- histogram

#### Parameters:

- `table_name` (`str`): Name of the database table to retrieve data from.
- `x_column` (`int`): Index of the x-axis column in the retrieved data.
- `y_column` (`int`): Index of the y-axis column in the retrieved data.
- `x_label` (`str`, optional): Label for the x-axis. Default is 'X Axis Label'.
- `y_label` (`str`, optional): Label for the y-axis. Default is 'Y Axis Label'.
- `title` (`str`, optional): Title of the chart. Default is 'Chart Title'.
- `save_path` (`str`, optional): Path to save the chart image. Default is 'chart.png'.
- `chart_type` (`str`, optional): The type of chart to create ('bar', 'line', 'scatter', 'histogram'). Default is 'bar'.

#### Returns:

This method does not return any value.

#### Raises:

- `RuntimeError`: If there is an error creating the chart or saving it as an image.

#### Example Usage:

```python
db.create_chart_table(table_name='your_table', x_column=0, y_column=1, x_label='Time', y_label='Values', title='Value Trend', save_path='chart.png', chart_type='line')
```

**Charts Like This**

![Alt text](https://github.com/Sepehr0Day/DbUnify/blob/main/my_table_histogram_chart.png?raw=true)


![Alt text](https://github.com/Sepehr0Day/DbUnify/blob/main/my_table_line_chart.png?raw=true)

![Alt text](https://github.com/Sepehr0Day/DbUnify/blob/main/chart.png?raw=true)



##

### Method: `export_data_csv`

Exports data from a specified table to a CSV file.

**Parameters:**

- `table_name` (`str`): The name of the table to export data from.
- `csv_file_path` (`str`): The path to save the exported CSV file.

**Raises:**

- `Exception`: If there is an error during data export.

**Description:**

This method retrieves data from a specified table and exports it to a CSV file. It fetches all rows and columns from the table and writes them to the CSV file.

### Method: `create_json_table`

Creates a table to store JSON data.

**Parameters:**

- `table_name` (`str`): The name of the table.

**Description:**

This method creates a table with a structure to store JSON data. It is supported for SQLite, MySQL, and PostgreSQL databases. The table has two columns: `id` (INTEGER, primary key) and `json_data` (TEXT).

### Method: `create_xml_table`

Creates a table to store XML data.

**Parameters:**

- `table_name` (`str`): The name of the table.

**Description:**

This method creates a table with a structure to store XML data. It is supported for SQLite, MySQL, and PostgreSQL databases. The table has two columns: `id` (INTEGER, primary key) and `xml_data` (TEXT).

### Method: `insert_json_data`

Inserts JSON data into a JSON table.

**Parameters:**

- `table_name` (`str`): The name of the JSON table.
- `json_data` (`dict`): The JSON data to insert.

**Description:**

This method inserts JSON data into a JSON table. It serializes the JSON data into a string and inserts it into the `json_data` column of the table.

### Method: `insert_xml_data`

Inserts XML data into an XML table.

**Parameters:**

- `table_name` (`str`): The name of the XML table.
- `xml_data` (`str`): The XML data to insert as a string.

**Description:**

This method inserts XML data into an XML table. It directly inserts the XML data string into the `xml_data` column of the table.

### Method: `retrieve_json_data`

Retrieves JSON data from a JSON table.

**Parameters:**

- `table_name` (`str`): The name of the JSON table.
- `record_id` (`int`): The ID of the record to retrieve.

**Returns:**

- `dict`: The retrieved JSON data.

**Description:**

This method retrieves JSON data from a JSON table based on the provided record ID. It deserializes the stored JSON string back into a dictionary.

### Method: `retrieve_xml_data`

Retrieves XML data from an XML table.

**Parameters:**

- `table_name` (`str`): The name of the XML table.
- `record_id` (`int`): The ID of the record to retrieve.

**Returns:**

- `str`: The retrieved XML data as a string.

**Description:**

This method retrieves XML data from an XML table based on the provided record ID.

### Method: `export_to_pdf`

Export data from a database table to a PDF document with customizable styles.

**Parameters:**

- `table_name` (`str`): The name of the database table to export data from.
- `pdf_file_path` (`str`): The path to save the exported PDF file.
- `background_color` (`str`, optional): Background color for the table cells (e.g., 'lightblue').
- `text_color` (`str`, optional): Text color for the table cells (e.g., 'black').
- `font_name` (`str`, optional): Font name for the table text (e.g., 'Helvetica').
- `font_size` (`int`, optional): Font size for the table text.

**Raises:**

- `Exception`: If there is an error during data export.

**Description:**

This method retrieves data from a specified database table and exports it to a PDF document. You can customize various styles, including background color, text color, font name, and font size.

### Method: `insert_base64`

Insert base64 encoded data into a database table.

**Parameters:**

- `table_name` (`str`): Name of the table to insert data into.
- `data_dict` (`dict`): A dictionary where keys are column names, and values are data to be encoded and inserted.

**Raises:**

- `RuntimeError`: If there is an error inserting the data.

**Description:**

This method inserts base64 encoded data into a database table. It takes a dictionary of column names and corresponding base64 encoded data and inserts them into the specified table.

### Method: `read_base64`

Read and decode base64 encoded data from a database table.

**Parameters:**

- `table_name` (`str`): Name of the table to read data from.

**Returns:**

- `dict`: A dictionary where keys are column names, and values are decoded data as bytes.

**Raises:**

- `RuntimeError`: If there is an error selecting or decoding the data.

**Description:**

This method reads and decodes base64 encoded data from a database table. It returns the decoded data as a dictionary with column names as keys and decoded data as bytes.


### Method: `close`

Closes the database connection.

**Raises:**

- `ConnectionError`: If there is an error closing the connection.

**Description:**

This method closes the database connection established by the `DatabaseManager`.


---

*Note: The methods provided in this documentation are illustrative and may require modification based on your specific use case and database setup.*


## SQLite

```python
# Example usage with SQLite
db_sqlite = DatabaseManager('sqlite', 'my_database.db')

# Create a table
db_sqlite.create_table('my_table', [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT')])

# Insert a row
db_sqlite.insert_row('my_table', {'name': 'John'})

# Query data
result_sqlite = db_sqlite.fetch_all('SELECT * FROM my_table')
print(result_sqlite)

# Backup the database
db_sqlite.backup_database('backup.db')

# Restore the database
db_sqlite.restore_database('backup.db')

# Close the connection
db_sqlite.close()

# Other functions
db_sqlite.add_column('my_table', 'age', 'INTEGER')
db_sqlite.delete_column('my_table', 'age')
db_sqlite.create_chart_database(output_directory='charts_directory', chart_type='line', x_label='Time', y_label='Values')
db_sqlite.create_chart_table(table_name='your_table', x_column=0, y_column=1, x_label='Time', y_label='Values', title='Value Trend', save_path='chart.png', chart_type='line')
db_sqlite.export_data_csv('my_table', 'exported_data.csv')
db_sqlite.create_json_table('json_data_table')
db_sqlite.create_xml_table('xml_data_table')
db_sqlite.insert_json_data('json_data_table', {'data': 'value'})
db_sqlite.insert_xml_data('xml_data_table', '<data>value</data>')
db_sqlite.retrieve_json_data('json_data_table', 1)
db_sqlite.retrieve_xml_data('xml_data_table', 1)
db_sqlite.export_to_pdf('my_table', 'exported_data.pdf')
db_sqlite.insert_base64('base64_data_table', {'data': 'base64encodedstring'})
db_sqlite.read_base64('base64_data_table')
```

# MySQL
```python
# Example usage with MySQL
db_mysql = DatabaseManager('mysql', 'my_database', user='my_user', password='my_password', host='localhost')

# Create a table
db_mysql.create_table('my_table', [('id', 'INT AUTO_INCREMENT PRIMARY KEY'), ('name', 'VARCHAR(255)')])

# Insert a row
db_mysql.insert_row('my_table', {'name': 'John'})

# Query data
result_mysql = db_mysql.fetch_all('SELECT * FROM my_table')
print(result_mysql)

# Backup the database
db_mysql.backup_database('backup.sql')

# Restore the database
db_mysql.restore_database('backup.sql')

# Close the connection
db_mysql.close()

# Other functions
db_mysql.add_column('my_table', 'age', 'INT')
db_mysql.delete_column('my_table', 'age')
db_mysql.create_chart_database(output_directory='charts_directory', chart_type='line', x_label='Time', y_label='Values')
db_mysql.create_chart_table(table_name='your_table', x_column=0, y_column=1, x_label='Time', y_label='Values', title='Value Trend', save_path='chart.png', chart_type='line')
db_mysql.export_data_csv('my_table', 'exported_data.csv')
db_mysql.create_json_table('json_data_table')
db_mysql.create_xml_table('xml_data_table')
db_mysql.insert_json_data('json_data_table', {'data': 'value'})
db_mysql.insert_xml_data('xml_data_table', '<data>value</data>')
db_mysql.retrieve_json_data('json_data_table', 1)
db_mysql.retrieve_xml_data('xml_data_table', 1)
db_mysql.export_to_pdf('my_table', 'exported_data.pdf')
db_mysql.insert_base64('base64_data_table', {'data': 'base64encodedstring'})
db_mysql.read_base64('base64_data_table')
```
# PostgreSQL
```python
# Example usage with PostgreSQL
db_postgresql = DatabaseManager('postgresql', 'my_database', user='my_user', password='my_password', host='localhost')

# Create a table
db_postgresql.create_table('my_table', [('id', 'SERIAL PRIMARY KEY'), ('name', 'VARCHAR(255)')])

# Insert a row
db_postgresql.insert_row('my_table', {'name': 'John'})

# Query data
result_postgresql = db_postgresql.fetch_all('SELECT * FROM my_table')
print(result_postgresql)

# Backup the database
db_postgresql.backup_database('backup.sql')

# Restore the database
db_postgresql.restore_database('backup.sql')

# Close the connection
db_postgresql.close()

# Other functions
db_postgresql.add_column('my_table', 'age', 'INT')
db_postgresql.delete_column('my_table', 'age')
db_postgresql.create_chart_database(output_directory='charts_directory', chart_type='line', x_label='Time', y_label='Values')
db_postgresql.create_chart_table(table_name='your_table', x_column=0, y_column=1, x_label='Time', y_label='Values', title='Value Trend', save_path='chart.png', chart_type='line')
db_postgresql.export_data_csv('my_table', 'exported_data.csv')
db_postgresql.create_json_table('json_data_table')
db_postgresql.create_xml_table('xml_data_table')
db_postgresql.insert_json_data('json_data_table', {'data': 'value'})
db_postgresql.insert_xml_data('xml_data_table', '<data>value</data>')
db_postgresql.retrieve_json_data('json_data_table', 1)
db_postgresql.retrieve_xml_data('xml_data_table', 1)
db_postgresql.export_to_pdf('my_table', 'exported_data.pdf')
db_postgresql.insert_base64('base64_data_table', {'data': 'base64encodedstring'})
db_postgresql.read_base64('base64_data_table')
```

# MongoDB
```python
# Example usage with MongoDB
db_mongodb = DatabaseManager('mongodb', 'mongodb://localhost:27017/')

# Insert a document
db_mongodb.insert_json_data('my_collection', {'name': 'John', 'age': 30})

# Query data
result_mongodb = db_mongodb.search_all('my_collection')
print(result_mongodb)

# Create a backup of the database
db_mongodb.backup_database('backup_directory')

# Restore the database from a backup
db_mongodb.restore_database('backup_directory')

# Create a collection
db_mongodb.create_table('my_collection')

# Insert a document into the collection
db_mongodb.insert_json_data('my_collection', {'name': 'Alice', 'age': 25})

# Query all documents in the collection
result_mongodb = db_mongodb.search_all('my_collection')
print(result_mongodb)

# Update a document in the collection
db_mongodb.update_row('my_collection', {'name': 'Alice Updated'}, {'name': 'Alice'})

# Query all documents in the collection after the update
result_mongodb = db_mongodb.search_all('my_collection')
print(result_mongodb)

# Delete a document from the collection
db_mongodb.delete_row('my_collection', {'name': 'Alice Updated'})

# Query all documents in the collection after the delete
result_mongodb = db_mongodb.search_all('my_collection')
print(result_mongodb)

# Close the connection
db_mongodb.close()

```

# SQL Server
```python
# Example usage with SQL Server
db_sqlserver = DatabaseManager('sqlserver', 'Driver={SQL Server};Server=localhost;Database=my_database;UID=my_user;PWD=my_password')

# Create a table
db_sqlserver.create_table('my_table', [('id', 'INT PRIMARY KEY'), ('name', 'VARCHAR(255)')])

# Insert a row
db_sqlserver.insert_row('my_table', {'id': 1, 'name': 'John'})

# Query data
result_sqlserver = db_sqlserver.fetch_all('SELECT * FROM my_table')
print(result_sqlserver)

# Backup the database
db_sqlserver.backup_database('backup.bak')

# Restore the database
db_sqlserver.restore_database('backup.bak')

# Close the connection
db_sqlserver.close()

# Other functions
db_sqlserver.add_column('my_table', 'age', 'INT')
db_sqlserver.delete_column('my_table', 'age')
db_sqlserver.create_chart_database(output_directory='charts_directory', chart_type='line', x_label='Time', y_label='Values')
db_sqlserver.create_chart_table(table_name='your_table', x_column=0, y_column=1, x_label='Time', y_label='Values', title='Value Trend', save_path='chart.png', chart_type='line')
db_sqlserver.export_data_csv('my_table', 'exported_data.csv')
db_sqlserver.create_json_table('json_data_table')
db_sqlserver.create_xml_table('xml_data_table')
db_sqlserver.insert_json_data('json_data_table', {'data': 'value'})
db_sqlserver.insert_xml_data('xml_data_table', '<data>value</data>')
db_sqlserver.retrieve_json_data('json_data_table', 1)
db_sqlserver.retrieve_xml_data('xml_data_table', 1)
db_sqlserver.export_to_pdf('my_table', 'exported_data.pdf')
db_sqlserver.insert_base64('base64_data_table', {'data': 'base64encodedstring'})
db_sqlserver.read_base64('base64_data_table')

```
---
*Your Database Management DbUnify, made easy with DbUnify.*<br>
<a href="https://pypi.org/project/DbUnify/"><img src="https://img.shields.io/badge/DbUnify-1.0.2-blue"></a> 

**By Sepehr0Day**

You can contact me on Telegram:
- Telegram ID: [@sepehr0day](https://t.me/sepehr0day)