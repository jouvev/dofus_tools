from src.reseau.types.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity

class StartupActionAddObject:
   def __init__(self,input):
      self.items = []
      _item6 = None
      self._uidFunc(input)
      self._titleFunc(input)
      self._textFunc(input)
      self._descUrlFunc(input)
      self._pictureUrlFunc(input)
      _itemsLen = input.readUnsignedShort()
      for _i6 in range(0,_itemsLen):
         _item6 = ObjectItemInformationWithQuantity(input)
         self.items.append(_item6)
      self._typeFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of StartupActionAddObject.uid.")
   
   def _titleFunc(self,input) :
      self.title = input.readUTF()
   
   def _textFunc(self,input) :
      self.text = input.readUTF()
   
   def _descUrlFunc(self,input) :
      self.descUrl = input.readUTF()
   
   def _pictureUrlFunc(self,input) :
      self.pictureUrl = input.readUTF()
   
   def _typeFunc(self,input) :
      self.type = input.readVarUhInt()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of StartupActionAddObject.type.")

   def resume(self):
      print("uid :",self.uid)
      print("title :",self.title)
      print("text :",self.text)
      print("descUrl :",self.descUrl)
      print("pictureUrl :",self.pictureUrl)
      print("type :",self.type)
      for e in self.items:
         e.resume()
