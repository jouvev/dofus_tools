from tmp.messages.IdentificationFailedMessage import IdentificationFailedMessage
from tmp.types.Version import Version

class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
   def __init__(self,input):
      super().__init__(input)
      self.requiredVersion = Version(input)

   def resume(self):
      super().resume()
      self.requiredVersion.resum()
