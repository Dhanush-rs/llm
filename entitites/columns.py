

class Column:
    
    def __init__(self, name, data_type, constraints) -> None:
        self.name =  name
        self.data_type = data_type
        self.constraints = constraints
    
    def validate_string_type(self, value):
        if "max_length" in self.constraints and len(value)>self.constraints['max_length']:
            raise ValueError(f'value {value} of data type {self.data_type} 
                             lenght can not be greater than {self.constraints['max_length']}')
    
    def validate_int_type(self, value):
        if "min_length" in self.constraints and len(value)<self.constraints["min_length"]:
            raise ValueError(f'value {value} of data type {self.data_type} 
                             lenght can not be lesser than {self.constraints['min_length']}')
            
            
    def validate_data_type(self, value):
        if self.data_type == "string":
            self.validate_string_type(value)
        elif self.data_type == "int":
            self.validate_int_type(value)
        else:
            raise ValueError("only string and integer type are accepted")
        
    def is_mandatory(self):
        return "not_null" in self.constraints
    
        
    
    
    
    