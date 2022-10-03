from tmp.types.LeagueFriendInformations import LeagueFriendInformations
class GameRolePlayArenaInvitationCandidatesAnswerMessage:
   def __init__(self,input):
      self.candidates = []
      _item1 = None
      _candidatesLen = input.readUnsignedShort()
      for _i1 in range(0,_candidatesLen):
         _item1 = LeagueFriendInformations(input)
         self.candidates.append(_item1)