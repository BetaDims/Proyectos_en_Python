#Write your code below this line 👇

def prime_checker(number):
    menores = []
    for i in range(1,number+1):
        menores.append(number%i)
    # print(menores)
    counter = menores.count(0)
    # print(counter)
    if counter == 2 or counter == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
