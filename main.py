import sqlalchemy
from sqlalchemy.orm import sessionmaker


SQLsystem = 'postgresql'
login = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432
db_name = "orm_homework"
DSN = f'{SQLsystem}://{login}:{password}@{host}:{port}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
