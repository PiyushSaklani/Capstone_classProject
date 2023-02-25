from Subtract import sub
from Add import add
from Division import div
from Multiplication import mul

ch = int(input("What you want to do:\n1. Subtract\n2. Add\n3. Multiplication\n4. Division\n"))
x,y = map(int,input("Enter number like(1 2): ").split())
if ch == 1:
    print(sub(x,y))
elif ch == 2:
    print(add(x,y))
elif ch == 3:
    print(mul(x,y))
elif ch == 4:
    print(div(x,y))
else:
    print(":O Wrong INPUT...\nInput Again.")

