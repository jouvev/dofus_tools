from src.reseau.types.StartupActionAddObject import StartupActionAddObject

class StartupActionAddMessage:
   def __init__(self,input):
      self.newAction = StartupActionAddObject(input)

   def resume(self):
      self.newAction.resume()
