class Version:
   def __init__(self,input):
      self._majorFunc(input)
      self._minorFunc(input)
      self._codeFunc(input)
      self._buildFunc(input)
      self._buildTypeFunc(input)
   
   def _majorFunc(self,input) :
      self.major = input.readByte()
      if(self.major < 0) :
         raise RuntimeError("Forbidden value (" + str(self.major) + ") on element of Version.major.")
   
   def _minorFunc(self,input) :
      self.minor = input.readByte()
      if(self.minor < 0) :
         raise RuntimeError("Forbidden value (" + str(self.minor) + ") on element of Version.minor.")
   
   def _codeFunc(self,input) :
      self.code = input.readByte()
      if(self.code < 0) :
         raise RuntimeError("Forbidden value (" + str(self.code) + ") on element of Version.code.")
   
   def _buildFunc(self,input) :
      self.build = input.readInt()
      if(self.build < 0) :
         raise RuntimeError("Forbidden value (" + str(self.build) + ") on element of Version.build.")
   
   def _buildTypeFunc(self,input) :
      self.buildType = input.readByte()
      if(self.buildType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.buildType) + ") on element of Version.buildType.")

   def resume(self):
      print("major :",self.major)
      print("minor :",self.minor)
      print("code :",self.code)
      print("build :",self.build)
      print("buildType :",self.buildType)
