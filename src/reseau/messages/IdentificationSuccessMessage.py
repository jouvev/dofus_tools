from src.reseau.types.AccountTagInformation import AccountTagInformation

class IdentificationSuccessMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._loginFunc(input)
      self.accountTag = AccountTagInformation(input)
      self._accountIdFunc(input)
      self._communityIdFunc(input)
      self._secretQuestionFunc(input)
      self._accountCreationFunc(input)
      self._subscriptionElapsedDurationFunc(input)
      self._subscriptionEndDateFunc(input)
      self._havenbagAvailableRoomFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.hasRights = bool(bin(_box0)[2:].zfill(8)[0])
      self.hasConsoleRight = bool(bin(_box0)[2:].zfill(8)[1])
      self.wasAlreadyConnected = bool(bin(_box0)[2:].zfill(8)[2])
      self.isAccountForced = bool(bin(_box0)[2:].zfill(8)[3])
   
   def _loginFunc(self,input) :
      self.login = input.readUTF()
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of IdentificationSuccessMessage.accountId.")
   
   def _communityIdFunc(self,input) :
      self.communityId = input.readByte()
      if(self.communityId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.communityId) + ") on element of IdentificationSuccessMessage.communityId.")
   
   def _secretQuestionFunc(self,input) :
      self.secretQuestion = input.readUTF()
   
   def _accountCreationFunc(self,input) :
      self.accountCreation = input.readDouble()
      if(self.accountCreation < 0 or self.accountCreation > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.accountCreation) + ") on element of IdentificationSuccessMessage.accountCreation.")
   
   def _subscriptionElapsedDurationFunc(self,input) :
      self.subscriptionElapsedDuration = input.readDouble()
      if(self.subscriptionElapsedDuration < 0 or self.subscriptionElapsedDuration > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.subscriptionElapsedDuration) + ") on element of IdentificationSuccessMessage.subscriptionElapsedDuration.")
   
   def _subscriptionEndDateFunc(self,input) :
      self.subscriptionEndDate = input.readDouble()
      if(self.subscriptionEndDate < 0 or self.subscriptionEndDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.subscriptionEndDate) + ") on element of IdentificationSuccessMessage.subscriptionEndDate.")
   
   def _havenbagAvailableRoomFunc(self,input) :
      self.havenbagAvailableRoom = input.readUnsignedByte()
      if(self.havenbagAvailableRoom < 0 or self.havenbagAvailableRoom > 255) :
         raise RuntimeError("Forbidden value (" + str(self.havenbagAvailableRoom) + ") on element of IdentificationSuccessMessage.havenbagAvailableRoom.")

   def resume(self):
      print("login :",self.login)
      print("accountId :",self.accountId)
      print("communityId :",self.communityId)
      print("secretQuestion :",self.secretQuestion)
      print("accountCreation :",self.accountCreation)
      print("subscriptionElapsedDuration :",self.subscriptionElapsedDuration)
      print("subscriptionEndDate :",self.subscriptionEndDate)
      print("havenbagAvailableRoom :",self.havenbagAvailableRoom)
      self.accountTag.resum()
