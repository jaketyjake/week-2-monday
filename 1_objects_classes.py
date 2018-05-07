#assignment 1 Objects and Classes

#sonny and jordan
class Person:
    def __init__(self, name, email,phone, ):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        self.other_person = other_person
        print(f"Hello {self.other_person}, I am {self.name}!")
    
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friend):
        self.friends.append(friend)

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")  

#sonny.print_contact_info()

#sonny.greet(jordan.name)
#jordan.greet(sonny.name)

jordan.add_friend(sonny)
print(f"Jordan has {jordan.friends} in his friends")
#print(f"The contact info for {sonny.name} is {sonny.email} and {sonny.phone}")
#print(f"The contact info for {jordan.name} is {jordan.email} and {jordan.phone}")

#jordan.friends.append(sonny)
#sonny.friends.append(jordan)
#print(len(jordan.friends))

#jordan.friends.append(sonny)

#***** got stuck on this aprt and moved to another
#      assignment to try 










# vehicles
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
     

    def print_info(self):
        print(f"The vehicle is a {self.year} {self.make} {self.model}")
car = Vehicle("Nissan", "Leaf", "2015")
car.print_info()

