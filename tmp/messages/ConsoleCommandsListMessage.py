class ConsoleCommandsListMessage:
   def __init__(self,input):
      self.aliases = []
      self.args = []
      self.descriptions = []
      _val1 = None
      _val2 = None
      _val3 = None
      _aliasesLen = input.readUnsignedShort()
      for _i1 in range(0,_aliasesLen):
         _val1 = input.readUTF()
         self.aliases.append(_val1)
      _argsLen = input.readUnsignedShort()
      for _i2 in range(0,_argsLen):
         _val2 = input.readUTF()
         self.args.append(_val2)
      _descriptionsLen = input.readUnsignedShort()
      for _i3 in range(0,_descriptionsLen):
         _val3 = input.readUTF()
         self.descriptions.append(_val3)