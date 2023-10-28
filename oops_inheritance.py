class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
            print (self.name)
            print (self.idnumber)

    def __init__(self,name,idnumber,post,salary):
        self.post =post
        self.salary =salary
    def details(self):
        print ('my name is {}'.format(self.name))
        print ('my idnumber is {}'.format(self.idnumber))
        print ('my post in the company is {}'.format (self.post))
        a = ('ashutosh',124589037,'junior software automator')
        a.display()
        a.details()
        print (a.display())
        print (a.details())