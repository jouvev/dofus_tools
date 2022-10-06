class AdditionalTaxCollectorInformations:
   def __init__(self,input):
      self._collectorCallerNameFunc(input)
      self._dateFunc(input)
   
   def _collectorCallerNameFunc(self,input) :
      self.collectorCallerName = input.readUTF()
   
   def _dateFunc(self,input) :
      self.date = input.readInt()
      if(self.date < 0) :
         raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of AdditionalTaxCollectorInformations.date.")

   def resume(self):
      print("collectorCallerName :",self.collectorCallerName)
      print("date :",self.date)
