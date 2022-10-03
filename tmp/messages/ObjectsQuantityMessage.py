from tmp.types.ObjectItemQuantity import ObjectItemQuantity
class ObjectsQuantityMessage:
   def __init__(self,input):
      self.objectsUIDAndQty = []
      _item1 = None
      _objectsUIDAndQtyLen = input.readUnsignedShort()
      for _i1 in range(0,_objectsUIDAndQtyLen):
         _item1 = ObjectItemQuantity(input)
         self.objectsUIDAndQty.append(_item1)