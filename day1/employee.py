employes=[]

def add_employee():
    name = input("enter name ")
    age = input("your age ? ")
    salary = int(input("enter your salary : "))
    data = {"name":name , "age":age, "salary": salary}
    return data

def show_employess(list):
    for employee in list :
        print(employee)


n_adds=input("enter n employess you want to add")