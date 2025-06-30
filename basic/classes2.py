class Person:
    def __init__(self,name):
       self.name = name 

    def talk(self):
        print(f"Hi, I am {self.name}")


ayushi = Person("Ayushi Jaiswal")
ayushi.talk()    

ishita = Person("Ishita Agarwal")
ishita.talk()