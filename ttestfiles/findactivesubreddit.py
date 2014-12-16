def main():
  pvalfile = open('boston.txt','r')
  sigvals = open('newtownsigpvals.txt','w')

  for line in pvalfile:
    words = line.split('|')
    if (float(words[2].strip()) < .05 and float(words[2].strip()) > -.05):
      print(words[1].strip()+"\t"+words[2])

  pvalfile.close()
  sigvals.close()
main()
