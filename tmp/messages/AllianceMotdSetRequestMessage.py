from tmp.messages.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage

class AllianceMotdSetRequestMessage(SocialNoticeSetRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._contentFunc(input)
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()

   def resume(self):
      super().resume()
      print("content :",self.content)
