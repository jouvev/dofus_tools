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
         raise RuntimeError("Forbidden value (" + self.major + ") on element of Version.major.")
   
   def _minorFunc(self,input) :
      self.minor = input.readByte()
      if(self.minor < 0) :
         raise RuntimeError("Forbidden value (" + self.minor + ") on element of Version.minor.")
   
   def _codeFunc(self,input) :
      self.code = input.readByte()
      if(self.code < 0) :
         raise RuntimeError("Forbidden value (" + self.code + ") on element of Version.code.")
   
   def _buildFunc(self,input) :
      self.build = input.readInt()
      if(self.build < 0) :
         raise RuntimeError("Forbidden value (" + self.build + ") on element of Version.build.")
   
   def _buildTypeFunc(self,input) :
      self.buildType = input.readByte()
      if(self.buildType < 0) :
         raise RuntimeError("Forbidden value (" + self.buildType + ") on element of Version.buildType.")