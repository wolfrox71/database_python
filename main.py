class db:
    def __init__(self,database,table):
        import sqlite3 #import the module
        self.conn = sqlite3.connect(database,check_same_thread=False) # conn is connected to the database file
        self.c = self.conn.cursor()
        self.database = database #add the file to be changed to self
        self.table = table #add the table you are looking at to self
    
    def setup(self,*args):
        """Set up a table if it does not exist with a column for each argument passed in
        """
        self.to_write = f"CREATE TABLE IF NOT EXISTS {self.table} (" #if the table does not exist already
        for i in range(len(args)):
            self.to_write += f"{str(args[i])} characters(100)" #add each argument as a column of characters of length 100
            if i != len(args)-1: #if it not the last argumnet
                self.to_write += "," #add a comma showing that there will be another column
        self.to_write += ")"
        self.c.execute(self.to_write) #add to the table
        self.conn.commit() #commit the changes to the file

    def read(self):
        "Return an array of all the rows in the table"
        self.c.execute(f"SELECT * FROM {self.table}")
        self.conn.commit()
        self.lines = self.c.fetchall()
        return self.lines
    
    
    def insert(self,*args):
        """Insert into the table, data with each argument going in the corresponding column"""
        self.to_write = f"INSERT INTO {self.table} VALUES ("
        for i in range(len(args)):
            self.add = str(args[i]).replace("\"","'") # replace "  with ' to stop speach marks breaking the code
            self.to_write += f"\"{self.add}\"" #add speach marks around each argument to specify the start and end of argument
            if i != len(args)-1: #if it is not the last argument
                self.to_write += ","  # add a comma to show that there is another argument coming
        self.to_write += ")"
        self.c.execute(self.to_write) #execute the statement
        self.conn.commit() #commit the statement

    def columns(self):
        """Return the column names of the table as an array"""
        self.c.execute(f"PRAGMA table_info({self.table})")
        self.conn.commit()
        self.columns_values = []
        for x in self.c.fetchall(): # for each column in the column names
            self.columns_values.append(x[1]) # add it to an array
        return self.columns_values #return the array
    
    def drop(self):
        """Drop the table"""
        self.c.execute(f"DROP TABLE {self.table}")
        self.conn.commit()