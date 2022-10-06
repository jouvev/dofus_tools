class StatedElement:
   def __init__(self,input):
      self._elementIdFunc(input)
      self._elementCellIdFunc(input)
      self._elementStateFunc(input)
      self._onCurrentMapFunc(input)
   
   def _elementIdFunc(self,input) :
      self.elementId = input.readInt()
      if(self.elementId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of StatedElement.elementId.")
   
   def _elementCellIdFunc(self,input) :
      self.elementCellId = input.readVarUhShort()
      if(self.elementCellId < 0 or self.elementCellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.elementCellId) + ") on element of StatedElement.elementCellId.")
   
   def _elementStateFunc(self,input) :
      self.elementState = input.readVarUhInt()
      if(self.elementState < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elementState) + ") on element of StatedElement.elementState.")
   
   def _onCurrentMapFunc(self,input) :
      self.onCurrentMap = input.readBoolean()

   def resume(self):
      print("elementId :",self.elementId)
      print("elementCellId :",self.elementCellId)
      print("elementState :",self.elementState)
      print("onCurrentMap :",self.onCurrentMap)
