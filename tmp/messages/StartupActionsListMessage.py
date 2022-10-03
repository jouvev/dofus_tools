from tmp.types.StartupActionAddObject import StartupActionAddObject
class StartupActionsListMessage:
   def __init__(self,input):
      self.actions = []
      _item1 = None
      _actionsLen = input.readUnsignedShort()
      for _i1 in range(0,_actionsLen):
         _item1 = StartupActionAddObject(input)
         self.actions.append(_item1)