import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
sales_2024 = [5, 7, 9, 12, 15]
sales_2025 = [3, 6, 8, 10, 13]

plt.figure()

plt.fill_between(x, sales_2024, label="Sales 2024", alpha=0.5)
plt.fill_between(x, sales_2025, label="Sales 2025", alpha=0.5)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Company Sales Comparison")

plt.legend()
plt.grid(True)

plt.show()