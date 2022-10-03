class ServerOptionalFeaturesMessage:
   def __init__(self,input):
      self.features = []
      _val1 = 0
      _featuresLen = input.readUnsignedShort()
      for _i1 in range(0,_featuresLen):
         _val1 = input.readInt()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of features.")
         self.features.append(_val1)