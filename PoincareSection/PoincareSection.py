def rungeKutta(n: int, dt):  # calculate loop

    X = 0
    Y = 0
    Z = 0

    PZ = []
    PX = []

    for i in range(n):
        # runge kutta
        Xprime = X + ((-Y - Z) * dt * 0.5)
        Yprime = Y + ((X + (a * Y)) * dt * 0.5)
        Zprime = Z + (b + (Z * (X - c))) * dt * 0.5

        newY = Y + ((Xprime + (a * Yprime)) * dt)
        newX = X + ((-Yprime - Zprime) * dt)
        newZ = Z + (b + (Zprime * (Xprime - c))) * dt

        if newY > 0 and Y < 0:
            PX.append(abs(newX))
            PZ.append(abs(newZ))

        Y = newY
        X = newX
        Z = newZ

    return PX, PZ


def createPlot(X, Z):  # create plot by matplotlib package

    # plot X
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.scatter(X, Z, s=1)

    plt.show()


def saveLists(X, Z):  # save lists to file
    fileName = input("Please enter filename like this -> name.format ")

    file = open(fileName, "w")

    for i in range(len(X)):
        file.write(str(Z[i]) + "," + str(X[i]) + "\n")


if __name__ == '__main__':

    # def constants
    a = 0.1
    b = 0.1
    c = 14

    # get time values from user
    totalT = float(input("Please enter total time (s):\n"))
    dT = float(input("Please enter time step (s):\n"))

    n = int(totalT / dT)  # find loop range

    X, Z = rungeKutta(n, dT)  # start calculate

    try:  # try to create plot by matplotlib

        import matplotlib.pyplot as plt

        createPlot(X, Z)

    except ImportError as e:  # if can`t find matplotlib run this

        saveLists(X, Z)
