import tmp.types.EntityLook as et
class SubEntity:
   def __init__(self,input):
      self._bindingPointCategoryFunc(input)
      self._bindingPointIndexFunc(input)
      self.subEntityLook = et.EntityLook(input)
   
   def _bindingPointCategoryFunc(self,input) :
      self.bindingPointCategory = input.readByte()
      if(self.bindingPointCategory < 0) :
         raise RuntimeError("Forbidden value (" + self.bindingPointCategory + ") on element of SubEntity.bindingPointCategory.")
   
   def _bindingPointIndexFunc(self,input) :
      self.bindingPointIndex = input.readByte()
      if(self.bindingPointIndex < 0) :
         raise RuntimeError("Forbidden value (" + self.bindingPointIndex + ") on element of SubEntity.bindingPointIndex.")