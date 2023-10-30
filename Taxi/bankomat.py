
from psycopg2 import connect

class DB:
    def __init__(self):
        self.connection  = connect(
            user = "postgres",
            database = "postgres",
            password = "S1824s1824",
        )


obj = DB()