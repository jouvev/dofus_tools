import src.reseau.types.EntityLook as et

class SubEntity:
   def __init__(self,input):
      self._bindingPointCategoryFunc(input)
      self._bindingPointIndexFunc(input)
      self.subEntityLook = et.EntityLook(input)
   
   def _bindingPointCategoryFunc(self,input) :
      self.bindingPointCategory = input.readByte()
      if(self.bindingPointCategory < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bindingPointCategory) + ") on element of SubEntity.bindingPointCategory.")
   
   def _bindingPointIndexFunc(self,input) :
      self.bindingPointIndex = input.readByte()
      if(self.bindingPointIndex < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bindingPointIndex) + ") on element of SubEntity.bindingPointIndex.")

   def resume(self):
      print("bindingPointCategory :",self.bindingPointCategory)
      print("bindingPointIndex :",self.bindingPointIndex)
