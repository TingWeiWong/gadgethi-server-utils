# gadgethiServerUtils
This is the utility helper functions that can support the gadgethi server development. 

## Initial setup
Need to setup config_location parameter
```
config_location = "/opt/doday/doday-config/server-config.yaml"
```
and call generate_db_header

public pub pem key should be in /opt/doday/cert/* folder

## Database Operations
This is the documentation for ```db_operations.py``` file.

### Abstract Level

**db_operations** is the utility function used for performing low-level operations on database 

A python PostgreSQL operation may consists of two parts:

1. String query

	```
	sql = """SELECT * FROM order_table WHERE username = %s"""
	```

2. Execute entries

	```
	result = execute(sql,('Andrew))
	```
	
3. Result would be optional, since some operations are **POST** actions that do not require fetching data.


### Database Connection

PostgreSQL requires explicit functions to connect to database

#### Connection Psycopg2 ```connect_to_database```

This function connects to the POSTGRESQL database.

By passing in ```test``` argument = ```True```, the server connects to Test database.



### Generate Query 

There are four main query examples. We may find it painful if we have to type them all everytime. 

```
Select = '''SELECT * FROM queue_table WHERE order_id = %s ORDER BY priority,time;'''

Update = '''UPDATE queue_table SET base = %s, soup = %s, main = %s, food1 = %s, food2 = %s, food3 = %s, special = %s, price = %s, discounted_price = %s ,promotion = %s, promotion_key = %s, priority = %s, status = %s WHERE order_id = %s;'''

Delete = '''DELETE FROM queue_table WHERE order_id = %s ;'''

Insert = '''INSERT into queue_table (order_id, order_no, base, soup, main, food1, food2, food3, special, price, discounted_price, promotion, promotion_key, priority, status, time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
```

So Andrew wrote the ```generate_query``` series functions

#### Gerate Query Function ```generate_query``` 
This function generalizes the query statements.

```
generate_query(table, action, target_column_list, conditional_column_list = 'None', order_by_list = 'None', limit_number = 'None'):
```

	* required:
		- table: table to execute on (ex. 'order')
		- action: A valid psycopg2 command (ex. 'SELECT')
		- target_column_list: list of the column names after the ACTION statements (ex.['base','soup','food1']), SELECT * from order_tables means to select everything from order_table. In this case the target column list if the all_order_columns
	
	* optionals:
		- conditional_column_list: list of the column names after the WHERE statement (ex. [username, store_id]), WHERE username = %s, store_id = %s. In this case we want to find the arguments that match.
		- order_by_list: Order by what ascending/descending order (ex.[priority DESC, time ASC, _id ASC]) Which means ORDER BY priority DESC, time ASC, _id ASC. 
		- limit_number: the number of fetched data you want (ex.1) limit 1.
		 
	* Returns:
		- table_action_query: the query you want.

### Execute SQL

#### executeSql Function ```executeSql```

```
def executeSql(db_path, sql, entries, mode, debug_print=False, header=False):
```

	* required:
		- db_path: database path (ex.getDb('order))
		- sql: string generated from the previous generate_query function
		- entries: arguments matching the sql = %s parts, in tuple form
		- mode:
			mode = 0 -> normal execute
			mode = 1 -> execute with arguments
			mode = 2 -> with return values but without arguments
			mode = 3 -> with return values and with arguments	
	* optionals:
		- debug_print: True if development mode. Default False
		- header: description for the command generated. Default False
		 
	* Returns:
		- ret: Response of the execute command.

### Versioning

Gados-redbean-devel-v1.2.2

### Authors

* **Andrew Wong** 

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments
