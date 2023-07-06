def even_numbers():
    x= range(10)
    for i in x:
        if i%2==0:
            print(i)
even_numbers()

def odd_numers():
    odd=range(20)
    for i in odd:
        if i%2!=0:
            print(i)
odd_numers()

def divisible_by_five():
    y=range(20)
    for i in y:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")
divisible_by_five()

def multiple_comparisons():
    z = range(30)
    for i in z:
        if i%2==0:
            print(f"{i} is divisible by 2")
        elif i%3==0:
            print(f"{i} is divisible by 3")
        elif i%5==0:
            print(f"{i} is not divisible by 2, 3 or 5")
multiple_comparisons()

def divisible_by_two_and_three():
    x= range(30)
    for i in x:
        if i%2==0 and i%3==0:
            print(f"{i} is divisible by 2 and 3")
        elif i%2==0 or i%3==0:
            print(f"{i} is divisible by 2 or 3")
        else:
            print(f"{i} is not divisible by 2 or 3")
divisible_by_two_and_three()

def while_loop():
    x=1
    while x<10:
        print("Hello while")
        x+=1
while_loop()


def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break
break_statement()

def continue_statement():
    x=0
    while x<20:
        x+=1
        if x%2==0:
            continue
        print(x)
continue_statement()

def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)
        
even_numbers()

def concatenate_kwargs(**presidents):
    all_presidents = ""
    for key, value in presidents.items():
        all_presidents += (f"{key}: {value}")

        print(all_presidents)

concatenate_kwargs(Kenya= "Ruto", Uganda="Museveni", Tanzania="Samia",Somalia="Hassan", Rwanda="Kagame")