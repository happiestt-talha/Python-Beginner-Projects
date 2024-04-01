import random
import os
if (not os.path.exists('Talha')):
    os.mkdir("Talha")

for i in range(0, 10):
    os.rmdir(f"Talha/Tut{i+1}")
# print(os.listdir("/"))
