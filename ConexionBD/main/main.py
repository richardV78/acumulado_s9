import mysql.connector
import os
import dao.daoConnection as dao
import models.clases

#conectar bd
conex = dao.Connection("localhost", "root", "", "dbregisters")

#instanciar dao
daoCity = dao.DaoCity(conex)

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()
        
        
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
   
    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result



