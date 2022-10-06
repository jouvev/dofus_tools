from src.reseau.messages.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage

class IdolsPresetSaveRequestMessage(IconPresetSaveRequestMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
