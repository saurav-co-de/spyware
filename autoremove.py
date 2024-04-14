import os
import time

for i in range(10):
    print("I will delete myself in " + str(10 - i) + " seconds.")
    time.sleep(1)

os.remove(__file__)
print("Goodbye")
