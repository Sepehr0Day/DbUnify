# DbUnify | Database Management DbUnify

**DbUnify** (Database Management DbUnify) is your all-in-one solution for simplifying database connectivity in Python projects. With DbUnify, you can effortlessly manage connections to various popular databases, streamlining your development process and saving valuable time.

## Key Features:

1. **Database Freedom**: DbUnify supports a wide range of database types, including SQLite, MySQL, PostgreSQL, MongoDB and SQL Server, providing a unified interface for all your database needs.

2. **Clean and Versatile API**: Enjoy the convenience of a clean and versatile API that ensures consistency across different database platforms. Say goodbye to scattered code and complexity.

3. **Password Management**: DbUnify simplifies password management by allowing you to update passwords for MySQL, PostgreSQL and SQL Server databases, enhancing security practices.

4. **Robust Exception Handling**: Database operations can be error-prone, but DbUnify excels in handling exceptions, offering clear and informative error messages for efficient troubleshooting.

5. **User-Friendly**: Whether you're a seasoned developer or a beginner, DbUnify offers a user-friendly experience. Initialize connections, execute queries, and manage passwords with ease.

6. **Cross-Platform Compatibility**: DbUnify is designed for seamless operation across different platforms, ensuring consistent behavior in your Python projects, regardless of your development environment.

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

### Method: `close`
Closes the database connection.

**Raises:**

- `ConnectionError`: If there is an error closing the connection.

### Method: `create_chart_table`

Creates a bar chart from data in a specified database table and saves it as an image.

**Parameters:**

- `table_name` (`str`): Name of the database table to retrieve data from.
- `x_column` (`int`): Index of the column to be used as the x-axis data.
- `y_column` (`int`): Index of the column to be used as the y-axis data.
- `x_label` (`str`): Label for the x-axis.
- `y_label` (`str`): Label for the y-axis.
- `title` (`str`): Title of the chart.
- `save_path` (`str`): Path to save the chart image.

**Raises:**

- `RuntimeError`: If there is an error creating the bar chart or saving it as an image.

**Description:**

This method generates a bar chart from data stored in a specified table of an SQLite database. It allows you to customize the x-axis and y-axis data by providing column indices (`x_column` and `y_column`), axis labels (`x_label` and `y_label`), and a chart title (`title`). The resulting chart is saved as an image at the specified `save_path`.

The method ensures that the chart image is saved and handles exceptions that may occur during chart creation or image saving.

**Usage:**

```python
db_manager = DatabaseManager('your_database.db')
table_name = 'your_table_name'
x_column = 0  # Index of the x-axis column
y_column = 1  # Index of the y-axis column
x_label = 'X Axis Label'
y_label = 'Y Axis Label'
title = 'Bar Chart for Table Data'
save_path = 'chart_image.png'  # Specify the path to save the chart image
db_manager.create_chart_table(table_name, x_column, y_column, x_label, y_label, title, save_path)
```
Replace 'your_database.db' with the path to your SQLite database, 'your_table_name' with the name of the table you want to visualize, and adjust other parameters accordingly.

This method is useful for creating customized bar charts to visualize specific data within a database table.

### Method: `create_chart_database`

Creates bar charts for all tables in the database and saves them as images.

**Parameters:**

- `output_directory` (`str`): The directory where the chart images will be saved.

**Raises:**

- `RuntimeError`: If there is an error creating bar charts or saving them as images.

**Description:**

This method generates bar charts for all tables present in the SQLite database. Each table's data is extracted and plotted as a bar chart. The resulting charts are saved as image files in the specified `output_directory`. The method ensures that the output directory exists and handles exceptions that may occur during chart creation or image saving.

The generated charts display data from each table in a clear and visual manner, making it easy to analyze and visualize the data stored in the database.

**Usage:**

```python
db_manager = DatabaseManager('your_database.db')
output_directory = 'bar_charts_output'  # Specify the directory to save the charts
db_manager.create_chart_database(output_directory)
```
Replace 'your_database.db' with the path to your SQLite database and 'bar_charts_output' with the desired directory where you want to save the chart images.

This method is particularly useful for exploring and summarizing data stored in multiple tables within the database.

## DatabaseManager Class Methods

### Method: `export_data_csv`

Exports data from a specified table to a CSV file.

**Parameters:**

- `table_name` (`str`): The name of the table to export data from.
- `csv_file_path` (`str`): The path to save the exported CSV file.

**Raises:**

- `Exception`: If there is an error during data export.

**Description:**

This method retrieves data from a specified table and exports it to a CSV file. It fetches all rows and columns from the table and writes them to the CSV file.

**Chart Like This**

![Alt Text](https://raw.githubusercontent.com/Sepehr0Day/DbUnify/main/my_table_bar_chart.png)

##
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
# Initialize a SQLite database connection
db = DatabaseManager(db_type='sqlite', db_name='my_database.db')

# Create a table
table_name = 'my_table'
columns = [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('age', 'INTEGER')]
db.create_table(table_name, columns)

# Insert rows into the table
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

for row in data:
    db.insert_row(table_name, row)

# Fetch and print all rows from the table
rows = db.search_all(table_name)
print("All rows in the table:")
for row in rows:
    print(row)

# Update a row
update_data = {'age': 32}
update_condition = "name = 'Alice'"
db.update_row(table_name, update_data, update_condition)

# Fetch and print the updated row
updated_row = db.search_one(table_name, update_condition)
print("Updated row:")
print(updated_row)

# Delete a row
delete_condition = "name = 'Bob'"
db.delete_row(table_name, delete_condition)

# Fetch and print all rows after deletion
rows_after_deletion = db.search_all(table_name)
print("All rows after deletion:")
for row in rows_after_deletion:
    print(row)

# Backup and restore the database
backup_path = 'my_database_backup.db'
db.backup_database(backup_path)
db.drop_table(table_name)  # Drop the table to demonstrate restoration
db.restore_database(backup_path)

# Close the database connection
db.close()
```

# MySQL
```python
# Initialize a MySQL database connection
db = DatabaseManager(db_type='mysql', db_name='my_database', user='your_username', password='your_password', host='localhost')

# Create a table
table_name = 'my_table'
columns = [('id', 'INT AUTO_INCREMENT PRIMARY KEY'), ('name', 'VARCHAR(255)'), ('age', 'INT')]
db.create_table(table_name, columns)

# Insert rows into the table
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

for row in data:
    db.insert_row(table_name, row)

# Fetch and print all rows from the table
rows = db.search_all(table_name)
print("All rows in the table:")
for row in rows:
    print(row)

# Update a row
update_data = {'age': 32}
update_condition = "name = 'Alice'"
db.update_row(table_name, update_data, update_condition)

# Fetch and print the updated row
updated_row = db.search_one(table_name, update_condition)
print("Updated row:")
print(updated_row)

# Delete a row
delete_condition = "name = 'Bob'"
db.delete_row(table_name, delete_condition)

# Fetch and print all rows after deletion
rows_after_deletion = db.search_all(table_name)
print("All rows after deletion:")
for row in rows_after_deletion:
    print(row)

# Close the database connection
db.close()
```
# PostgreSQL
```python
# Initialize a PostgreSQL database connection
db = DatabaseManager(db_type='postgresql', db_name='my_database', user='your_username', password='your_password', host='localhost', port='5432')

# Create a table
table_name = 'my_table'
columns = [('id', 'SERIAL PRIMARY KEY'), ('name', 'VARCHAR(255)'), ('age', 'INT')]
db.create_table(table_name, columns)

# Insert rows into the table
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

for row in data:
    db.insert_row(table_name, row)

# Fetch and print all rows from the table
rows = db.search_all(table_name)
print("All rows in the table:")
for row in rows:
    print(row)

# Update a row
update_data = {'age': 32}
update_condition = "name = 'Alice'"
db.update_row(table_name, update_data, update_condition)

# Fetch and print the updated row
updated_row = db.search_one(table_name, update_condition)
print("Updated row:")
print(updated_row)

# Delete a row
delete_condition = "name = 'Bob'"
db.delete_row(table_name, delete_condition)

# Fetch and print all rows after deletion
rows_after_deletion = db.search_all(table_name)
print("All rows after deletion:")
for row in rows_after_deletion:
    print(row)

# Close the database connection
db.close()
```

# MongoDB
```python
# Initialize a MongoDB connection
db = DatabaseManager(db_type='mongodb', host='localhost', port=27017)

# Create a collection
collection_name = 'my_collection'
collection = db.connection['my_database'][collection_name]

# Insert documents into the collection
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

collection.insert_many(data)

# Fetch and print all documents from the collection
documents = collection.find()
print("All documents in the collection:")
for doc in documents:
    print(doc)

# Update a document
update_data = {'$set': {'age': 32}}
update_condition = {'name': 'Alice'}
collection.update_one(update_condition, update_data)

# Fetch and print the updated document
updated_doc = collection.find_one(update_condition)
print("Updated document:")
print(updated_doc)

# Delete a document
delete_condition = {'name': 'Bob'}
collection.delete_one(delete_condition)

# Fetch and print all documents after deletion
documents_after_deletion = collection.find()
print("All documents after deletion:")
for doc in documents_after_deletion:
    print(doc)

# Close the database connection
db.connection.close()
```

# SQL Server
```python
# Initialize a SQL Server database connection
db = DatabaseManager(db_type='sqlserver', server='localhost', database='my_database', user='your_username', password='your_password')

# Create a table
table_name = 'my_table'
columns = [('id', 'INT IDENTITY(1,1) PRIMARY KEY'), ('name', 'NVARCHAR(255)'), ('age', 'INT')]
db.create_table(table_name, columns)

# Insert rows into the table
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

for row in data:
    db.insert_row(table_name, row)

# Fetch and print all rows from the table
rows = db.search_all(table_name)
print("All rows in the table:")
for row in rows:
    print(row)

# Update a row
update_data = {'age': 32}
update_condition = "name = 'Alice'"
db.update_row(table_name, update_data, update_condition)

# Fetch and print the updated row
updated_row = db.search_one(table_name, update_condition)
print("Updated row:")
print(updated_row)

# Delete a row
delete_condition = "name = 'Bob'"
db.delete_row(table_name, delete_condition)

# Fetch and print all rows after deletion
rows_after_deletion = db.search_all(table_name)
print("All rows after deletion:")
for row in rows_after_deletion:
    print(row)

# Close the database connection
db.close()
```
---
*Your Database Management DbUnify, made easy with DbUnify.*<br>
<a href="https://pypi.org/project/DbUnify/"><img src="https://img.shields.io/badge/DbUnify-1.0.2-blue"></a> 

**By Sepehr0Day**

You can contact me on Telegram:
- Telegram ID: [@sepehr0day](https://t.me/sepehr0day)