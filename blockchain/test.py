class student:
    def __init__(self, name,age,contact):
        self.name=name
        self.age=age
        self.contact=contact
        def __str__(self):
            return "THe name is {} .the age is {} and mobile no. is {}".format(self.name,self.age,self.contact);
if __name__=='__main__':
    s=student('rajeev',34,'9759153006')
    print(type(s.__str__()),type(s),s,s.name,s.age,s.contact)
