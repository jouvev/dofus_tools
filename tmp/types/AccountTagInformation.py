class AccountTagInformation:
   def __init__(self,input):
      self._nicknameFunc(input)
      self._tagNumberFunc(input)
   
   def _nicknameFunc(self,input) :
      self.nickname = input.readUTF()
   
   def _tagNumberFunc(self,input) :
      self.tagNumber = input.readUTF()