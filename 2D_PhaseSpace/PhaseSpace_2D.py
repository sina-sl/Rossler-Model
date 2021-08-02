def rungeKutta(n: int, dt):  # calculate loop

    X = [0]
    Y = [0]
    Z = 0

    for i in range(n):
        # runge kutta
        Xprime = X[i] + ((-Y[i] - Z) * dt * 0.5)
        Yprime = Y[i] + ((X[i] + (a * Y[i])) * dt * 0.5)
        Zprime = Z + (b + (Z * (X[i] - c))) * dt * 0.5

        Y.insert(i + 1, Y[i] + ((Xprime + (a * Yprime)) * dt))
        X.insert(i + 1, X[i] + ((-Yprime - Zprime) * dt))
        Z = Z + (b + (Zprime * (Xprime - c))) * dt

    return X, Y


def createPlot(X, Y):  # create plot by matplotlib package
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(X, Y, linewidth=1)

    plt.show()


def saveLists(X, Y):  # save lists to file
    fileName = input("Please enter filename like this -> name.format ")

    file = open(fileName, "w")

    for i in range(len(X)):
        file.write(str(Y[i]) + "," + str(X[i]) + "\n")


if __name__ == '__main__':

    # def constants
    a = 0.1
    b = 0.1
    c = 29

    # get time values from user
    T = float(input("Please enter total time (s):\n"))
    dT = float(input("Please enter time step (s):\n"))

    n = int(T / dT)  # find loop range

    X, Y = rungeKutta(n, dT)  # start calculate

    try:  # try to create plot by matplotlib

        import matplotlib.pyplot as plt

        createPlot(X, Y)

    except ImportError as e:  # if can`t find matplotlib run this

        saveLists(X, Y)
