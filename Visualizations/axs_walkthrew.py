import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[i**2 for i in x]
y2=[i**4 for i in x]
y3=[i**0.5 for i in x]

plt.plot(x,y1,label="x^2",color="blue")
plt.plot(x,y2,label="x^4",color="green")
plt.plot(x,y3,label="sqrt(x)",color="red")

plt.title("multi plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.grid()
plt.show()