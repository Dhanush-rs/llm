


class Users():
    user_dict={}
    def __init__(self,name, email, phone_number) -> None:
        self.name=name
        self.email=email
        self.phone_number=phone_number
        self.balances = {} # user_id:money owed

    
    