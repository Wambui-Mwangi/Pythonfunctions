def hello(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer += number

    return answer

#Write a function that acccepts any number of intergers and returns the result of multiplying all of them
def multiply(*numbers):
    product= 1
    for number in numbers:
        product*=number

    return product  

def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}") 

def my_country(country="Burundi"):
    print(f"Hello from {country}")

def concatenate_args(*cities):
    all_cities = " "
    for city in cities:
        all_cities+=city
    print(all_cities)
        
concatenate_args("Nairobi", " Kisumu", " Mombasa", " Kigali", " Mogadishu" )

def concatenate_kwargs(**presidents):
    all_presidents = ""
    for key, value in presidents.items():
        all_presidents += (f"{key}: {value}")

        print(all_presidents)

concatenate_kwargs(Kenya= "Ruto", Uganda="Museveni", Tanzania="Samia",Somalia="Hassan", Rwanda="Kagame")
 


