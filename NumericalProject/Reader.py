class Reader:
   self.part = True # to decide which part
   self.list = [] # information container
   
   def __init__(self,part, list):
       self.part = part
       self.list = list
      
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
       f = open(abs, 'r')
       for line in f:
           self.list.append(f.readline)

       f.close()
       return




   