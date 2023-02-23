from Subtract import sub
from Add import add

ch = int(input("What you want to do:\n1. Subtract\n2. Add\n3. Multiplication\n4. Division"))
x,y = map(int,input().split())
if ch == 1:
    print(sub(x,y))
elif ch == 2:
    print("ADD")
elif ch == 3:
    print("MULT")
elif ch == 4:
    print("DIV")
else:
    print(":O Wrong INPUT...\nInput Again.")