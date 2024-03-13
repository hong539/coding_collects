from sqlalchemy import create_engine, MetaData, Table, select

# Replace 'your_database_url' with the URL of your database
database_url = 'your_database_url'

# Replace 'your_value_to_search' with the value you want to find
value_to_search = '10.0.5.9'

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Reflect the database tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Iterate through all tables and search for the value
for table_name in metadata.tables:
    table = Table(table_name, metadata, autoload_with=engine)
    query = select([table]).where(table.c == value_to_search)
    result = engine.execute(query).fetchall()

    if result:
        print(f"Value '{value_to_search}' found in table '{table_name}'")
        for row in result:
            print(row)
    else:
        print(f"Value '{value_to_search}' not found in table '{table_name}'")