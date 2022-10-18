import src.reseau.TypesFactory as pf

class QuestStepInfoMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.infos = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      self.infos.resume()
