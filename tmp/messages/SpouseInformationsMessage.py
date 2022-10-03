import tmp.TypesFactory as pf
class SpouseInformationsMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.spouse = pf.TypesFactory.get_instance_id(_id1,input)