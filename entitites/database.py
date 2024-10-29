from entitites.tables import Table
from entitites.columns import Column
class Database:
    
    def __init__(self) -> None:
        self.tables=[]
        
    def create_table(self,name,columns):
        table = Table(name)
        for name, data_type, constraints in columns:
            table.add_column(name, data_type, constraints)
        self.tables[name]=table
            