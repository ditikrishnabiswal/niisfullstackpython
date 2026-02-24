14.#compound interest
print("enter principal")
p=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
print("enter number of time compunded")
n=int(input())
CI=p*(1+r/n)**(n*t)-p
print("compund interest=",CI)