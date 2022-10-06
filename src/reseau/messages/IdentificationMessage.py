from src.reseau.types.Version import Version

class IdentificationMessage:
   def __init__(self,input):
      self.credentials = []
      self.failedAttempts = []
      _val3 = 0
      _val9 = 0
      self.deserializeByteBoxes(input)
      self.version = Version(input)
      self._langFunc(input)
      _credentialsLen = input.readVarInt()
      for _i3 in range(0,_credentialsLen):
         _val3 = input.readByte()
         self.credentials.append(_val3)
      self._serverIdFunc(input)
      self._sessionOptionalSaltFunc(input)
      _failedAttemptsLen = input.readUnsignedShort()
      for _i9 in range(0,_failedAttemptsLen):
         _val9 = input.readVarUhShort()
         if(_val9 < 0) :
            raise RuntimeError("Forbidden value (" + _val9 + ") on elements of failedAttempts.")
         self.failedAttempts.append(_val9)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.autoconnect = bool(bin(_box0)[2:].zfill(8)[0])
      self.useCertificate = bool(bin(_box0)[2:].zfill(8)[1])
      self.useLoginToken = bool(bin(_box0)[2:].zfill(8)[2])
   
   def _langFunc(self,input) :
      self.lang = input.readUTF()
   
   def _serverIdFunc(self,input) :
      self.serverId = input.readShort()
   
   def _sessionOptionalSaltFunc(self,input) :
      self.sessionOptionalSalt = input.readVarLong()
      if(self.sessionOptionalSalt < -9007199254740992 or self.sessionOptionalSalt > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sessionOptionalSalt) + ") on element of IdentificationMessage.sessionOptionalSalt.")

   def resume(self):
      print("lang :",self.lang)
      print("serverId :",self.serverId)
      print("sessionOptionalSalt :",self.sessionOptionalSalt)
      self.version.resum()
      print("credentials :",self.credentials)
      print("failedAttempts :",self.failedAttempts)
