import matplotlib
import matplotlib.pyplot as plt

x_points = []

for place in range(-100, 100):
    x_points.append(place/100)

def kvadrat(tal):
    return tal **2

y_points = []
for xp in x_points:
    y_points.append(kvadrat(xp))

    plt.plot(x_points, y_points)
    plt.scatter(x_points, y_points)
    plt.show()