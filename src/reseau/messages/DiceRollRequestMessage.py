class DiceRollRequestMessage:
   def __init__(self,input):
      self._diceFunc(input)
      self._facesFunc(input)
      self._channelFunc(input)
   
   def _diceFunc(self,input) :
      self.dice = input.readVarUhInt()
      if(self.dice < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dice) + ") on element of DiceRollRequestMessage.dice.")
   
   def _facesFunc(self,input) :
      self.faces = input.readVarUhInt()
      if(self.faces < 0) :
         raise RuntimeError("Forbidden value (" + str(self.faces) + ") on element of DiceRollRequestMessage.faces.")
   
   def _channelFunc(self,input) :
      self.channel = input.readByte()
      if(self.channel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.channel) + ") on element of DiceRollRequestMessage.channel.")

   def resume(self):
      print("dice :",self.dice)
      print("faces :",self.faces)
      print("channel :",self.channel)
