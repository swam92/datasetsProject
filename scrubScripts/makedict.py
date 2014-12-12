from csv import reader
import os

def getheaders():
  lines = open('headers.txt','w');
  for file in os.listdir("data"):
    source = open('../data/'+file,'r');
    for line in reader(source):
      newline = ''
      for col in line:
        newline += col + '\t'
      newline += '\n'
      lines.write(newline)
      break

  lines.close()

def compareheaders():
  headerfile = open('headers.txt','r')
  headers = headerfile.readlines()
  i = 0
  for line in headers:
    if line != headers[0]:
      print(i)
    i += 1
  headerfile.close()

def makedict():
  filenames = open('filenames.txt','w');
  filenames.write('subreddits = {\n')
  for file in os.listdir("data"):
    source = open('data/'+file,'r');
    i=0
    for line in reader(source):
      if i==1:
        filenames.write("\t'{0}': '{1}',\n".format(line[14],file.split('.',1)[0]))
        break
      i += 1
  filenames.write('}')
  filenames.close()

def makelistfiles():
  filenames = open('datafiles.txt','w');
  for file in os.listdir("../data"):
    filenames.write(file+"\n")
  filenames.close()

def main():
  makelistfiles()
main()
