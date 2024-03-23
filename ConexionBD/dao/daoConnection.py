class DaoCity:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM city'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM city WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    def insert(self, city):
        query = 'INSERT INTO city (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (city.name, city.status))
    
    def update(self, city):
        query = 'UPDATE city SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (city.name, city.status, city.id))
    
    def delete(self, id):
        query = 'DELETE FROM city WHERE id = %s'
        return self.connection.execute_query(query, (id,))
