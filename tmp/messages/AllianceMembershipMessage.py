from tmp.messages.AllianceJoinedMessage import AllianceJoinedMessage
class AllianceMembershipMessage(AllianceJoinedMessage):
   def __init__(self,input):
      super().__init__(input)