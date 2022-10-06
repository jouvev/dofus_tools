from src.reseau.messages.SocialNoticeMessage import SocialNoticeMessage

class AllianceMotdMessage(SocialNoticeMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
