with open("product.csv", "r") as fobj:
    content = fobj.read()
print(content)

name = input("Enter a new product name: ")
price = input("Enter a new product price: ")

with open("product.csv", "a") as fobj:
    fobj.write(f"\n{name}, {price}")
    print("New product added. ")


