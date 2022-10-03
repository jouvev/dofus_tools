class LockableUseCodeMessage:
   def __init__(self,input):
      self._codeFunc(input)
   
   def _codeFunc(self,input) :
      self.code = input.readUTF()