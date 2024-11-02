
from entitites.documents import Document
# from entitites.users import User

class DocumentService:
    
    def __init__(self) -> None:
        # self.users = {}
        self.documents = {}
        
    def create_document(self, owner, name, content):
        # if owner not in self.users:
            # user = User(owner)
            # self.users[owner] = user
        document = Document(name, content, owner)
        self.documents[name] = document
    
    def read_document(self, user, document_name):
        document = self.check_if_document_exists(document_name)
        if document:
            return document.get_content(user)

    def check_if_document_exists(self, document_name):
        if document_name in self.documents:
            return self.documents[document_name]
        print(f"document {document_name} does not exist")
    
    def update_document(self, user, document_name, content):
        document = self.check_if_document_exists(document_name)
        if document:
            return document.set_content(user, content)
    
    def delete_document(self, user, document_name):
        document = self.check_if_document_exists(document_name)
        if document:
            owner = document.get_owner()
            if user == owner:
                del self.documents[document_name]
            else:
                print(f"user {user} is not an owner, only owner can delete")
                
    def grant_read(self, user, document_name):
        document = self.check_if_document_exists(document_name)
        if document:
            document.set_read_permission(user)
    
    def grant_write(self, user, document_name):
        document = self.check_if_document_exists(document_name)
        if document:
            # grant read permission too when write is granted
            document.set_read_permission(user)
            document.set_write_permission(user)