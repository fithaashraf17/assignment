from click import echo
from django.template import Engine
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String

engine = create_engine('sqlite:///work.db',echo=True)
meta = MetaData()
workers =Table('workers',meta,
        Column('id',Integer,primary_key=True),
        Column('name',String),
        )

# meta.create_all(engine)
ins=workers.insert()
ins=workers.insert().values(name="fitha")
conn=engine.connect()
result=conn.execute(ins)