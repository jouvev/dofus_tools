from tmp.types.JobBookSubscription import JobBookSubscription
class JobBookSubscriptionMessage:
   def __init__(self,input):
      self.subscriptions = []
      _item1 = None
      _subscriptionsLen = input.readUnsignedShort()
      for _i1 in range(0,_subscriptionsLen):
         _item1 = JobBookSubscription(input)
         self.subscriptions.append(_item1)