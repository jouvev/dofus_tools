from tmp.types.MountClientData import MountClientData

class MountDataMessage:
   def __init__(self,input):
      self.mountData = MountClientData(input)

   def resume(self):
      self.mountData.resum()
