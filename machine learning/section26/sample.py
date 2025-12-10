import matplotlib.pyplot as plt

x = [i for i in range(-10, 11)]
m1 = 0
m2 = 0
count = 1
xlist = []
ylist = []

plt.ion()

for i in range(0, 10):

    if count == 360:
        break

    y1 = [(m1 * i) for i in x]
    y2 = [(m2 * i) for i in x]

    m1 += 30
    m2 -= 30

    ylist.append(y1)
    ylist.append(y2)

    plt.clf()
    plt.grid(True)

    for j in range(len(ylist)):
        plt.plot(x, ylist[j])

    plt.grid(True)

    plt.xlim(-15, 15)
    plt.ylim(-360, 360)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1) 

    plt.show()
    plt.pause(10)
