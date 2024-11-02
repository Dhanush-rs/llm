
class Document:
    def __init__(self, name, content, owner) -> None:
        self.name = name
        self.content = content
        self.__owner = owner
        self.read_users = []
        self.write_users = []
        
    def get_content(self, user):
        if user in self.read_users:
            print(f"contents of {self.name} is {self.content} ")
        else:
            print(f"user {user} is not authorised to read")
    
    def set_content(self, user, content):
        if user in self.write_users:
            self.content = content
        else:
            print(f"user {user} does not have permission to write")
    
    def set_read_permission(self, user):
        self.read_users.append(user)
        
    def get_read_users(self):
        return self.read_users
    
    def set_write_permission(self, user):
        self.write_users.append(user)
        
    def get_write_users(self):
        return self.write_users
    
    def get_owner(self):
        return self.__owner
    