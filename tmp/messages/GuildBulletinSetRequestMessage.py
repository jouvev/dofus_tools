from tmp.messages.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage
class GuildBulletinSetRequestMessage(SocialNoticeSetRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._contentFunc(input)
      self._notifyMembersFunc(input)
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()
   
   def _notifyMembersFunc(self,input) :
      self.notifyMembers = input.readBoolean()