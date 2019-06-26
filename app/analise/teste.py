from database import Connection
from connectdb import Connection
from db_helper import *

connection = Connection.session()
 

print(all_users = connection.query(Mortalidade).all())