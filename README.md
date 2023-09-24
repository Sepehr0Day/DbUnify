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

## SQLite

```python
# Example for SQLite
sqlite_db = DatabaseManager('sqlite', 'my_database.db')

# Creating a table
sqlite_db.create_table('students', [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('age', 'INTEGER')])

# Inserting a row
sqlite_db.insert_row('students', {'name': 'Alice', 'age': 25})

# Updating a row
sqlite_db.update_row('students', {'name': 'Alicia', 'age': 26}, 'name = ?', 'Alice')

# Deleting a row
sqlite_db.delete_row('students', 'name = ?', 'Alicia')

# Searching for one row
result = sqlite_db.search_one('students', 'name = ?', 'Alice')

# Searching for all rows
all_students = sqlite_db.search_all('students')
```

# MySQL
```python
# Example for MySQL
mysql_db = DatabaseManager('mysql', 'my_mysql_db', user='username', password='password', host='localhost')

# Creating a table
mysql_db.create_table('employees', [('id', 'INT AUTO_INCREMENT PRIMARY KEY'), ('name', 'VARCHAR(255)'), ('salary', 'DECIMAL(10, 2)')])

# Inserting a row
mysql_db.insert_row('employees', {'name': 'John', 'salary': 50000.0})

# Updating a row
mysql_db.update_row('employees', {'salary': 55000.0}, 'name = ?', 'John')

# Deleting a row
mysql_db.delete_row('employees', 'name = ?', 'John')

# Searching for one row
result = mysql_db.search_one('employees', 'name = ?', 'John')

# Searching for all rows
all_employees = mysql_db.search_all('employees')
```
# PostgreSQL
```python
# Example for PostgreSQL
postgresql_db = DatabaseManager('postgresql', 'my_postgresql_db', user='username', password='password', host='localhost')

# Creating a table
postgresql_db.create_table('products', [('id', 'SERIAL PRIMARY KEY'), ('name', 'TEXT'), ('price', 'DECIMAL(10, 2)')])

# Inserting a row
postgresql_db.insert_row('products', {'name': 'Laptop', 'price': 1000.0})

# Updating a row
postgresql_db.update_row('products', {'price': 1100.0}, 'name = ?', 'Laptop')

# Deleting a row
postgresql_db.delete_row('products', 'name = ?', 'Laptop')

# Searching for one row
result = postgresql_db.search_one('products', 'name = ?', 'Laptop')

# Searching for all rows
all_products = postgresql_db.search_all('products')
```

# MongoDB
```python
# Example for MongoDB
mongodb_db = DatabaseManager('mongodb', 'my_mongodb_db', host='localhost', port=27017)

# Creating a collection (equivalent to a table in MongoDB)
products_collection = mongodb_db.connection.my_mongodb_db.products

# Inserting a record (equivalent to a row in MongoDB)
products_collection.insert_one({'name': 'Phone', 'price': 500.0})

# Updating a record
products_collection.update_one({'name': 'Phone'}, {'$set': {'price': 550.0}})

# Deleting a record
products_collection.delete_one({'name': 'Phone'})

# Searching for one record
result = products_collection.find_one({'name': 'Phone'})

# Searching for all records
all_products = list(products_collection.find())
```

# SQL Server
```python
# Example for SQL Server
sqlserver_db = DatabaseManager('sqlserver', 'my_sqlserver_db', driver='{SQL Server}', server='localhost', database='my_db', uid='username', pwd='password')

# Creating a table
sqlserver_db.create_table('orders', [('id', 'INT IDENTITY(1,1) PRIMARY KEY'), ('customer_name', 'VARCHAR(255)'), ('total_amount', 'DECIMAL(10, 2)')])

# Inserting a record
sqlserver_db.insert_row('orders', {'customer_name': 'Jane', 'total_amount': 200.0})

# Updating a record
sqlserver_db.update_row('orders', {'total_amount': 250.0}, 'customer_name = ?', 'Jane')

# Deleting a record
sqlserver_db.delete_row('orders', 'customer_name = ?', 'Jane')

# Searching for one record
result = sqlserver_db.search_one('orders', 'customer_name = ?', 'Jane')

# Searching for all records
all_orders = sqlserver_db.search_all('orders')
```
---
*Your Database Management DbUnify, made easy with DbUnify.*<br>
<a href="https://pypi.org/project/DbUnify/"><img src="https://img.shields.io/badge/DbUnify-1.0.0-blue"></a> 

**By Sepehr0Day**

You can contact me on Telegram:
- Telegram ID: [@sepehr0day](https://t.me/sepehr0day)