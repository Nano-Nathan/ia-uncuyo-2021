from csp import CSP
import time
N = [4,8,10,12,15]
aTimesB = []
aStatesB = []
aTimes = []
aStates = []
for n in N:
    #Backtracking
    csp = CSP(n)
    now = time.time()
    aStatesB.append(csp.backtracking())
    aTimesB.append(round(time.time() - now, 5))

    #Forward Checking
    csp = CSP(n)
    now = time.time()
    aStates.append(csp.forwardChecking())
    aTimes.append(round(time.time() - now, 5))
print("Backtracking")
print(aStatesB)
print(aTimesB, "\n")

print("Forward Checking")
print(aStates)
print(aTimes)