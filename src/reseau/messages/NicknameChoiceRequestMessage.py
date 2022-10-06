class NicknameChoiceRequestMessage:
   def __init__(self,input):
      self._nicknameFunc(input)
   
   def _nicknameFunc(self,input) :
      self.nickname = input.readUTF()

   def resume(self):
      print("nickname :",self.nickname)
