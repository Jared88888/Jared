def div_2(number):
      halved = int(number/2)
      return halved

def odd_or_even(number):
      if (number % 2) == 1: #all odd numbers have remainder when divided by 2
            return "Odd"
      else:
            return "Even"

def prime(number):
    factors = 2 #1 and itself
    if odd_or_even(number) == "Even" and number != 2:
          return "Not prime" #if even and not 2, auto not prime
    if number <= 1:
          return "Not prime" #negative and 1 all not prime
    for i in range (3, div_2(number)):
          if number % i == 0: #no remainder
                factors += 1 #it is a factor

    if factors == 2: #should remain with the 2 factors of 1 and itself
          return "Prime"
    else:
          return "Not prime"
while True:
    whole_num = input("Enter a whole number: ")
    if whole_num.isdigit():
          break

print(f"{int(whole_num)} is {prime(int(whole_num))}")