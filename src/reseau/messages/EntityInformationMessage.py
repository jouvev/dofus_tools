from src.reseau.types.EntityInformation import EntityInformation

class EntityInformationMessage:
   def __init__(self,input):
      self.entity = EntityInformation(input)

   def resume(self):
      self.entity.resume()
