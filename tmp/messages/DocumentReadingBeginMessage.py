class DocumentReadingBeginMessage:
   def __init__(self,input):
      self._documentIdFunc(input)
   
   def _documentIdFunc(self,input) :
      self.documentId = input.readVarUhShort()
      if(self.documentId < 0) :
         raise RuntimeError("Forbidden value (" + self.documentId + ") on element of DocumentReadingBeginMessage.documentId.")