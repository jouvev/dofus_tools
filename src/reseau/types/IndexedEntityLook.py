from src.reseau.types.EntityLook import EntityLook

class IndexedEntityLook:
   def __init__(self,input):
      self.look = EntityLook(input)
      self._indexFunc(input)
   
   def _indexFunc(self,input) :
      self.index = input.readByte()
      if(self.index < 0) :
         raise RuntimeError("Forbidden value (" + str(self.index) + ") on element of IndexedEntityLook.index.")

   def resume(self):
      print("index :",self.index)
      self.look.resume()
