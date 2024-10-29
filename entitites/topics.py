
class Topics:
    
    def __init__(self,name) -> None:
        self.name=name
        self.questions=[]
    
    def get_questions(self):
        return self.questions
    
    def set_question(self,question):
        self.questions.append(question)
    
    def __repr__(self):
        return f"Topic(name={self.name})"