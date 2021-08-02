def rungeKutta(n: int, dt):  # calculate loop

    X = [0]
    Y = [0]
    Z = [0]
    T = [0]

    for i in range(n):
        # runge kutta
        Xprime = X[i] + ((-Y[i] - Z[i]) * dt * 0.5)
        Yprime = Y[i] + ((X[i] + (a * Y[i])) * dt * 0.5)
        Zprime = Z[i] + (b + (Z[i] * (X[i] - c))) * dt * 0.5

        Y.insert(i + 1, Y[i] + ((Xprime + (a * Yprime)) * dt))
        X.insert(i + 1, X[i] + ((-Yprime - Zprime) * dt))
        Z.insert(i + 1, Z[i] + (b + (Zprime * (Xprime - c))) * dt)

        T.insert(i + 1, T[i] + dT)

    return X, Y, Z, T


def createPlot(X, Y, Z, T):  # create plot by matplotlib package

    # plot X
    plt.subplot(3, 1, 1)
    plt.xlabel("T (s)")
    plt.ylabel("X")
    plt.plot(T, X, linewidth=1)

    # plot Y
    plt.subplot(3, 1, 2)
    plt.xlabel("T (s)")
    plt.ylabel("Y")
    plt.plot(T, Y, linewidth=1)

    # plot Z
    plt.subplot(3, 1, 3)
    plt.xlabel("T (s)")
    plt.ylabel("Z")
    plt.plot(T, Z, linewidth=1)

    plt.show()


def saveLists(X, Y, Z, T):  # save lists to file
    fileName = input("Please enter filename like this -> name.format ")

    file = open(fileName, "w")

    for i in range(len(X)):
        file.write(str(Z[i]) + "," + str(Y[i]) + "," + str(X[i]) + "," + str(T) + "\n")


if __name__ == '__main__':

    # def constants
    a = 0.1
    b = 0.1
    c = 6

    # get time values from user
    totalT = float(input("Please enter total time (s):\n"))
    dT = float(input("Please enter time step (s):\n"))

    n = int(totalT / dT)  # find loop range

    X, Y, Z, T = rungeKutta(n, dT)  # start calculate

    try:  # try to create plot by matplotlib

        import matplotlib.pyplot as plt

        createPlot(X, Y, Z, T)

    except ImportError as e:  # if can`t find matplotlib run this

        saveLists(X, Y, Z, T)
