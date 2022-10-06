import tmp.TypesFactory as pf

class InteractiveElement:
   def __init__(self,input):
      self.enabledSkills = []
      self.disabledSkills = []
      _id3 = 0
      _item3 = None
      _id4 = 0
      _item4 = None
      self._elementIdFunc(input)
      self._elementTypeIdFunc(input)
      _enabledSkillsLen = input.readUnsignedShort()
      for _i3 in range(0,_enabledSkillsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.enabledSkills.append(_item3)
      _disabledSkillsLen = input.readUnsignedShort()
      for _i4 in range(0,_disabledSkillsLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.disabledSkills.append(_item4)
      self._onCurrentMapFunc(input)
   
   def _elementIdFunc(self,input) :
      self.elementId = input.readInt()
      if(self.elementId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of InteractiveElement.elementId.")
   
   def _elementTypeIdFunc(self,input) :
      self.elementTypeId = input.readInt()
   
   def _onCurrentMapFunc(self,input) :
      self.onCurrentMap = input.readBoolean()

   def resume(self):
      print("elementId :",self.elementId)
      print("elementTypeId :",self.elementTypeId)
      print("onCurrentMap :",self.onCurrentMap)
      for e in self.enabledSkills:
         e.resume()
      for e in self.disabledSkills:
         e.resume()
