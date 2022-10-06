class GuildEmblem:
   def __init__(self,input):
      self._symbolShapeFunc(input)
      self._symbolColorFunc(input)
      self._backgroundShapeFunc(input)
      self._backgroundColorFunc(input)
   
   def _symbolShapeFunc(self,input) :
      self.symbolShape = input.readVarUhShort()
      if(self.symbolShape < 0) :
         raise RuntimeError("Forbidden value (" + str(self.symbolShape) + ") on element of GuildEmblem.symbolShape.")
   
   def _symbolColorFunc(self,input) :
      self.symbolColor = input.readInt()
   
   def _backgroundShapeFunc(self,input) :
      self.backgroundShape = input.readByte()
      if(self.backgroundShape < 0) :
         raise RuntimeError("Forbidden value (" + str(self.backgroundShape) + ") on element of GuildEmblem.backgroundShape.")
   
   def _backgroundColorFunc(self,input) :
      self.backgroundColor = input.readInt()

   def resume(self):
      print("symbolShape :",self.symbolShape)
      print("symbolColor :",self.symbolColor)
      print("backgroundShape :",self.backgroundShape)
      print("backgroundColor :",self.backgroundColor)
