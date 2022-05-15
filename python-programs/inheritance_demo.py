# inheritance
class User :
    def login(self) :
        print("login successful")
    def register(self) :
        print("registration successful")
        
class Student(User) :
    def enroll(self) :
        print("enrollment successful")
    def review(self) :
        print("reviewed")
        
class Teacher(User) :
    def upload(self) :
        print("upload successful")
    def answer_doubts(self) :
        print("solved")

t1 = Teacher()

t1.login()
t1.register()
t1.upload()

st1 = Student()

st1.login()
st1.review()