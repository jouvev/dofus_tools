class ListenersOfSynchronizedStorageMessage:
   def __init__(self,input):
      self.players = []
      _val1 = None
      _playersLen = input.readUnsignedShort()
      for _i1 in range(0,_playersLen):
         _val1 = input.readUTF()
         self.players.append(_val1)