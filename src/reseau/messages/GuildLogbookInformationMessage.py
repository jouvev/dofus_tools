import src.reseau.TypesFactory as pf

class GuildLogbookInformationMessage:
   def __init__(self,input):
      self.globalActivities = []
      self.chestActivities = []
      _id1 = 0
      _item1 = None
      _id2 = 0
      _item2 = None
      _globalActivitiesLen = input.readUnsignedShort()
      for _i1 in range(0,_globalActivitiesLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.globalActivities.append(_item1)
      _chestActivitiesLen = input.readUnsignedShort()
      for _i2 in range(0,_chestActivitiesLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.chestActivities.append(_item2)

   def resume(self):
      for e in self.globalActivities:
         e.resume()
      for e in self.chestActivities:
         e.resume()
