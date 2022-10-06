from src.reseau.messages.SocialNoticeSetErrorMessage import SocialNoticeSetErrorMessage

class AllianceBulletinSetErrorMessage(SocialNoticeSetErrorMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
