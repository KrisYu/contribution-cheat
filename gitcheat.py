from datetime import date
from random import randint
import sys
import subprocess
import os

def get_date_string(d):
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn

    
d1 = date(2016,9,26)
d2 = date(2016,9,27)

d3 = date(2016,10,2)
d4 = date(2016,10,3)
d5 = date(2016,10,4)
d6 = date(2016,10,5)

d7 = date(2016,10,9)
d8 = date(2016,10,10)       
d9 = date(2016,10,11) 
d10 = date(2016,10,12)
d11 = date(2016, 10,13)


d12 = date(2016, 10,17)
d13 = date(2016, 10,18)
d14 = date(2016, 10, 19)
d15 = date(2016, 10,20)
d16 = date(2016, 10,21)
d17 = date(2016, 10, 22)

d17 = date(2016, 10, 24)
d18 = date(2016, 10, 25)
d19 = date(2016, 10, 26)
d20 = date(2016, 10, 27)
d21 = date(2016, 10, 28)
d22 = date(2016, 10, 29)


d27 = date(2016, 10, 30)
d23 = date(2016, 10, 31)
d24 = date(2016, 11, 1)
d25 = date(2016, 11, 2)
d26 = date(2016, 11, 3)

d28 = date(2016, 11, 6)
d29 = date(2016, 11, 7)
d30 = date(2016, 11, 8)
d31 = date(2016, 11, 9)

d32 = date(2016, 11, 14)
d33 = date(2016, 11, 15)


def main():
  days = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33]
  for day in days:
    curdate = get_date_string(day)
    for commit in range(4):
      subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +
      "' > realwork.txt; git add realwork.txt; GIT_AUTHOR_DATE='" +
       curdate + "' GIT_COMMITTER_DATE='" + curdate
        + "' git commit -m 'update'; git push;")
    subprocess.call("git rm realwork.txt; git commit -m 'delete'; git push;")
        
if __name__ == "__main__":
	main()