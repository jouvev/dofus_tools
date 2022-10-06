from tmp.messages.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage

class GuildListApplicationRequestMessage(PaginationRequestAbstractMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
