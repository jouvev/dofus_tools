class TrustCertificate:
   def __init__(self,input):
      self._idFunc(input)
      self._hashFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of TrustCertificate.id.")
   
   def _hashFunc(self,input) :
      self.hash = input.readUTF()