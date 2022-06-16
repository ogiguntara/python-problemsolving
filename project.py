from sqlalchemy import create_engine, MetaData, Table, select

#create engine
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
print(engine.table_names())

#reflect census table via engine
# metadata = MetaData()
# census = Table('census', metadata, autoload=True, autoload_with=engine)

#create select query
# stmt = select([census])
# #add a where to filter only new york
# stmt = stmt.where(census.column.state=='New York')
stmt = 'SELECT * FROM census'
# execute query
connection=engine.connect()
cursor= connection.cursor()
results = cursor.execute(stmt).fetchall()

for result in results:
    print(result.age, result.sex, result.pop2000)