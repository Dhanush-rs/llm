
from entitites.questions import Question
from entitites.topics import Topics
class User:
    
    def __init__(self,name,profession=None) -> None:
        self.name=name 
        self.profession=profession
        self.questions=[]
        self.topics = []

    def create_question(self,question:Question):
        question_created= question
        self.questions.append(question_created)
        
    def get_topics(self):
        return self.get_topics
    
    def set_topic(self,topic):
        self.topics.append(topic)
        
    def remove_topic(self,topic):
        self.topics.remove(topic)