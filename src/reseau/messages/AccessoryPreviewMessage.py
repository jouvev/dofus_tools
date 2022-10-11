from src.reseau.types.EntityLook import EntityLook

class AccessoryPreviewMessage:
   def __init__(self,input):
      self.look = EntityLook(input)

   def resume(self):
      self.look.resume()
