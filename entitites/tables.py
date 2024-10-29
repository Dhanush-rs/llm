from entitites.columns import Column
class Table:
    
    def __init__(self, name) -> None:
        self.name=name
        self.data = []
        self.columns = []
        
    def add_column(self, column_name, column_type, contraints):
        column = Column(column_name, column_type, contraints)
        self.columns[column_name]=column
    
    def insert_row(self, values):
        if len(values)!=self.columns:
            raise ValueError("no of clumns and values mismatch ")
        row_data ={}
        for i, (column_name,_) in enumerate(self.columns):
            value=values[i]
            self.columns[column_name].validate_data_type(value)
            if value is None and self.columns[column_name].is_mandatory():
                raise ValueError("Mandatory column cant be None")
            row_data[column_name] = value
        self.data.append(row_data)
    
    def print_all_recods(self):
        for row in self.data:
            print(row)
    
    def filter_records(self,column_name, value):
        filtered_records = [row for row in self.data if row[column_name] == value]
        return filtered_records
    
    def update_record(self):
        pass
    
    def delete_record(self):
        pass
        