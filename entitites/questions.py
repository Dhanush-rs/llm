from datetime import datetime
from entitites.topics import Topics
# from entitites.users import User
from typing import List



class Question:
    
    def __init__(self, name, description,
                 topics,
                 timestamp=datetime.now()
                 ) -> None:
        self.name=name
        self.description=description
        self.topics=[Topics(topic) for topic in topics]
        self.responses=[]
        self.timestamp=timestamp
        
    def get_topics(self):
        return self.topics
    
    def set_topic(self,topic):
        topic_obj=Topics(topic)
        self.topics.append(topic_obj)
    
    def get_responses(self):
        return self.get_responses
    
    def set_response(self,response):
        self.responses.append(response)
        
    def __str__(self) -> str:
        return self.name
        
        
    
        