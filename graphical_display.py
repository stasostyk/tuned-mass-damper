import matplotlib.pyplot as plt
import json

data = []
with open("data.json", "r") as f:
    data = json.load(f)

# x1 = list(range(1, len(data[0])+1))
# y1 = data[0]
#
# plt.plot(x1, y1, label="x")
#
x2 = list(range(1, len(data[1])+1))
y2 = data[1]

plt.plot(x2, y2, label="y")
#
# x3 = list(range(1, len(data[2])+1))
# y3 = data[2]

# plt.plot(x3, y3, label="z")

plt.xlabel('time')

plt.ylabel('acceleration')

plt.title('Acceleration graph')

plt.legend()

plt.show()
