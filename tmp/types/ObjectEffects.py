import tmp.TypesFactory as pf

class ObjectEffects:
   def __init__(self,input):
      self.effects = []
      _id1 = 0
      _item1 = None
      _effectsLen = input.readUnsignedShort()
      for _i1 in range(0,_effectsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.effects.append(_item1)

   def resume(self):
      for e in self.effects:
         e.resume()
