from src.reseau.messages.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations

class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
   def __init__(self,input):
      super().__init__(input)
      self.alliance = BasicNamedAllianceInformations(input)

   def resume(self):
      super().resume()
      self.alliance.resume()
