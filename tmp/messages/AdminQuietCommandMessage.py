from tmp.messages.AdminCommandMessage import AdminCommandMessage

class AdminQuietCommandMessage(AdminCommandMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
