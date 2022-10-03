class ProtocolRequired:
   def __init__(self,input):
      self._versionFunc(input)
   
   def _versionFunc(self,input) :
      self.version = input.readUTF()