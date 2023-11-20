def addition(a,b):
    return a+b

print(addition(2,3))
#addition() is userdefined function
#there are several built-in function len(), print() , map() , reduce() , filter() , sum()

class student:
    def age_after_ten_years(self,current_age):
        return current_age + 10

student1=student()
age_after_ten_years=student1.age_after_ten_years(10)


print(age_after_ten_years)
#here age_after_ten_years() is a method of class student which can be called using statements object only
