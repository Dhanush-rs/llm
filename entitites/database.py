from entitites.tables import Table

class Database:
    
    def __init__(self) -> None:
        self.tables=[]
        
    def add_table(self,name,columns):
        table = Table(name)