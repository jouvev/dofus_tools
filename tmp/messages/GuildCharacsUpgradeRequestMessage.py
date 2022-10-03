class GuildCharacsUpgradeRequestMessage:
   def __init__(self,input):
      self._charaTypeTargetFunc(input)
   
   def _charaTypeTargetFunc(self,input) :
      self.charaTypeTarget = input.readByte()
      if(self.charaTypeTarget < 0) :
         raise RuntimeError("Forbidden value (" + self.charaTypeTarget + ") on element of GuildCharacsUpgradeRequestMessage.charaTypeTarget.")