def area(length,width):
    if length==width:
        return "This is a square."
    else:
        return length*width

length=eval(input("Enter the length : "))
width=eval(input("Enter the width : "))

result=area(length,width)

print("Area of reactangle : ",result)
