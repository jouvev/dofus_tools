import tmp.TypesFactory as pf
class AchievementListMessage:
   def __init__(self,input):
      self.finishedAchievements = []
      _id1 = 0
      _item1 = None
      _finishedAchievementsLen = input.readUnsignedShort()
      for _i1 in range(0,_finishedAchievementsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.finishedAchievements.append(_item1)