class ChatCommunityChannelCommunityMessage:
   def __init__(self,input):
      self._communityIdFunc(input)
   
   def _communityIdFunc(self,input) :
      self.communityId = input.readShort()

   def resume(self):
      print("communityId :",self.communityId)
