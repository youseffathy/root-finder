class Reader:
  
   def __init__(self):
       self.part = False
       self.list = []
      
   def setPart(self, part):
       self.part = part

   def setlist(self, list):
       self.list = list
   def getPart(self):
       return self.part 

   def getlist(self):
       return self.list 

   def read(self, absPath):
       absPath = absPath.replace("\\","\\\\") #to change \ to \\ in abs path
       f = open(absPath, 'r')
       for line in f:
           line = line.replace("\n","")   # as without it , at the end on each line will be new line char  ex: '---\n' 
           self.list.append(line)
       f.close()
       return 




   