
# ^ -------------------------------------------------------------------------------^#
#!                          CREATING WATER DRINKING REMINDER
# ^ -------------------------------------------------------------------------------^#

import os
import pyttsx3 as ppy
import time
import pandas as pd

now = time.time()
cur_time = time.ctime(now)
# print(cur_time, type(cur_time))
curr = cur_time.split()
this_time = curr[3]
this_time = pd.Series(this_time)
excact = pd.to_datetime(this_time)
print(excact, type(excact))
