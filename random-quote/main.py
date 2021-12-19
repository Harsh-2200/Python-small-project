import random
def master():
    

  f = open("random-quote\quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  
  print(quotes[rnd])
  

if __name__== "__main__":
  master()