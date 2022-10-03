class RemoveListenerOnSynchronizedStorageMessage:
   def __init__(self,input):
      self._playerFunc(input)
   
   def _playerFunc(self,input) :
      self.player = input.readUTF()