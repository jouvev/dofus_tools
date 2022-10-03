class AuthenticationTicketMessage:
   def __init__(self,input):
      self._langFunc(input)
      self._ticketFunc(input)
   
   def _langFunc(self,input) :
      self.lang = input.readUTF()
   
   def _ticketFunc(self,input) :
      self.ticket = input.readUTF()