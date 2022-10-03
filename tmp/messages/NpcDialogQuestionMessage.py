class NpcDialogQuestionMessage:
   def __init__(self,input):
      self.dialogParams = []
      self.visibleReplies = []
      _val2 = None
      _val3 = 0
      self._messageIdFunc(input)
      _dialogParamsLen = input.readUnsignedShort()
      for _i2 in range(0,_dialogParamsLen):
         _val2 = input.readUTF()
         self.dialogParams.append(_val2)
      _visibleRepliesLen = input.readUnsignedShort()
      for _i3 in range(0,_visibleRepliesLen):
         _val3 = input.readVarUhInt()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of visibleReplies.")
         self.visibleReplies.append(_val3)
   
   def _messageIdFunc(self,input) :
      self.messageId = input.readVarUhInt()
      if(self.messageId < 0) :
         raise RuntimeError("Forbidden value (" + self.messageId + ") on element of NpcDialogQuestionMessage.messageId.")