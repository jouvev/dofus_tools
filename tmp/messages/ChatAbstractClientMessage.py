class ChatAbstractClientMessage:
   def __init__(self,input):
      self._contentFunc(input)
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()