from entitites.users import User
from entitites.questions import Question
from entitites.topics import Topics

def main():
    
    user1= User("dhanush","software engineer")
    print(user1.name,user1.profession)
    ques1= Question("add","addd to numbers",["python","java"])
    user1.create_question(ques1)
    ques1.set_topic("go")
    print([t.name for t in ques1.topics])
    print([u.name for u in user1.questions])
    t1=Topics("js")
    print(t1)


if __name__ == "__main__":
    main()