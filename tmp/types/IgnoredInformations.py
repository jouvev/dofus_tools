from tmp.types.AbstractContactInformations import AbstractContactInformations

class IgnoredInformations(AbstractContactInformations):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
