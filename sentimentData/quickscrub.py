import os

for file in os.listdir("original"):
  newfile = open(file,'w')
  for l in open("original/"+file):
    nums = l.split('|')
    newfile.write(str(nums[1].strip())+" "+str(nums[2].strip())+"\n")

