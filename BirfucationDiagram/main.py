import matplotlib.pyplot as plt


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# def constant
a = 0.2
b = 0.2
c = 5.7

sa = 0
ea = 0.4
da = 0.001
na = int((ea - sa) / da)

# time
T = 10000
dT = 0.01
n = int(T / dT)

X = 0
Y = 0
Z = 0

# poincare section lists
PX = []
Pa = []

for j in range(na):  # loop of "a" values

    printProgressBar(j + 1, na, prefix='Progress:', suffix='Complete', length=50)
    sa = sa + da

    for i in range(n):  # time loop

        Xprime = X + ((-Y - Z) * dT * 0.5)
        Yprime = Y + ((X + (sa * Y)) * dT * 0.5)
        Zprime = Z + (b + (Z * (X - c))) * dT * 0.5

        newY = Y + ((Xprime + (sa * Yprime)) * dT)
        newX = X + ((-Yprime - Zprime) * dT)
        newZ = Z + (b + (Zprime * (Xprime - c))) * dT

        if newY < 0 and Y > 0:
            Pa.append(sa)
            PX.append(abs(newX))

        X = newX
        Y = newY
        Z = newZ


try:
    import matplotlib.pyplot as plt
    plt.xlabel("a")
    plt.ylabel("X")
    plt.scatter(Pa, PX, s=0.1)

    plt.show()

except ImportError as e:
    fileName = input("Please enter filename like this -> name.format ")

    file = open(fileName, "w")

    for i in range(len(X)):
        file.write(str(PX[i]) + "," + str(Pa[i]) + "\n")
