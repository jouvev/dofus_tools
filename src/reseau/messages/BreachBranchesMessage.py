import src.reseau.TypesFactory as pf

class BreachBranchesMessage:
   def __init__(self,input):
      self.branches = []
      _id1 = 0
      _item1 = None
      _branchesLen = input.readUnsignedShort()
      for _i1 in range(0,_branchesLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.branches.append(_item1)

   def resume(self):
      for e in self.branches:
         e.resume()
