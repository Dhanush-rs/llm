from users import Users

class Balance():
    
    commands= ["EXACT","PERCENT","EQUAL"]
    def __init__(self) -> None:
        pass
    
    def update_balances(self, payee, users_ids, command, data):
        
        if command not in self.commands:
            raise ValueError("Command not recognizable")
        
        for user in users_ids:
            user_obj = 
        