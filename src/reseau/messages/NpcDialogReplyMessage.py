class NpcDialogReplyMessage:
   def __init__(self,input):
      self._replyIdFunc(input)
   
   def _replyIdFunc(self,input) :
      self.replyId = input.readVarUhInt()
      if(self.replyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.replyId) + ") on element of NpcDialogReplyMessage.replyId.")

   def resume(self):
      print("replyId :",self.replyId)
