import time
startTime = time.time()

pi = 0
accuracy =1000000000
#int(input("input accuracy"))

for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))

print(pi)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
