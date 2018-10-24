from datetime import datetime

#define class
#use __ (double underscore to define private methods or variables)
class Person:
    #initializer double underscore init
    #self refers to the actual object instance
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y")

    #define methods, use self to refer to instance
    def get_age(self):
        #calculate age using date time functions
        today = datetime.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))