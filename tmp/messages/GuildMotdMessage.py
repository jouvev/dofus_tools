from tmp.messages.SocialNoticeMessage import SocialNoticeMessage

class GuildMotdMessage(SocialNoticeMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
