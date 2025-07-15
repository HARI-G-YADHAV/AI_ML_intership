import matplotlib.pyplot as plt

product = ["laptop","mobile","camera","headphones","tablet"]
sales = ["50","100","25","150","100"]


plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.barh(product,sales,color = "lightblue")
plt.title("product -sale bar plot")
plt.ylabel("products")
plt.xlabel("sales")
plt.grid(axis='x',linestyle = "--", alpha = 0.5)



plt.subplot(1,2,2)
colors = ["purple","green","gold","skyblue","yellow"]
plt.pie(sales, labels = product, colors = colors, autopct="%1.2f%%")

plt.tight_layout()

plt.show()