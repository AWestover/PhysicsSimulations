# Alek Westover
# hundred boxes simulation

# libraries
import random
import matplotlib.pyplot as plt
import pdb

# simulation variables
maxBoxes = 200
numSims = 10**3

# generates a set of boxes with numbers in them randomly
def setBoxes(numBoxes):
    boxPts = []
    boxPtsLeft = list(range(0, numBoxes))
    for i in range(0, numBoxes):
        curChoice = boxPtsLeft.pop(random.randint(0, numBoxes - i - 1))
        boxPts.append(curChoice)
    return boxPts

# people do not choose randomly they use their heads a bit
def simulatePrisonGroup(numBoxes):
    boxPts = setBoxes(numBoxes)

    maxLoopSize = 0
    for prisoner in range (0, numBoxes):
        curBox = prisoner
        times = 0
        while boxPts[curBox] != prisoner:
            # print("curBox: {} \t boxContents: {}".format(curBox, boxPts[curBox]))
            times += 1
            curBox = boxPts[curBox]

        if times > maxLoopSize:
            maxLoopSize = times

        if times > numBoxes / 2:
            return 0, maxLoopSize

    return 1, maxLoopSize

# people choose randomly
def simulateStupidPrisonGroup(numBoxes):
    boxPts = setBoxes(numBoxes)

    maxLoopSize = 0
    for prisoner in range (0, numBoxes):
        curBox = prisoner
        times = 0
        while boxPts[curBox] != prisoner:
            times += 1
            curBox = random.randint(0, numBoxes - 1)

        if times > maxLoopSize:
            maxLoopSize = times

        if times > numBoxes / 2:
            return 0, maxLoopSize

    return 1, maxLoopSize


allWins = {"smart": [], "stupid": []}
allamls = {"smart": [], "stupid": []}

for numBoxes in range(0, maxBoxes):
    if numBoxes % 10 == 0:
        print(numBoxes)
    wins = {"smart": 0, "stupid": 0}
    avgMaxLengthSum = {"smart": 0, "stupid": 0}
    for simNum in range(0, numSims):
        curSmartSim = simulatePrisonGroup(numBoxes)
        wins["smart"] += curSmartSim[0] # 0 is a lose 1 is a win
        avgMaxLengthSum["smart"] += curSmartSim[1]

        curStupidSim = simulateStupidPrisonGroup(numBoxes)
        wins["stupid"] += curStupidSim[0]
        avgMaxLengthSum["stupid"] += curStupidSim[1]

    allWins["smart"].append(wins["smart"] / numSims)
    allWins["stupid"].append(wins["stupid"] / numSims)
    allamls["smart"].append(avgMaxLengthSum["smart"] / numSims)
    allamls["stupid"].append(avgMaxLengthSum["stupid"] / numSims)


fig = plt.figure()
ax = fig.add_subplot(211)
ax.set_title("Probability of a win")
ax.plot(list(range(0, maxBoxes)), allWins["smart"], c="k")
ax.plot(list(range(0, maxBoxes)), allWins["stupid"])
ax2 = fig.add_subplot(212)
ax2.set_title("Average max tries")
ax2.plot(list(range(0, maxBoxes)), allamls["smart"], c="k")
ax2.plot(list(range(0, maxBoxes)), allamls["stupid"])
plt.tight_layout()
plt.savefig("BoxesSimulation.png")
plt.show()
