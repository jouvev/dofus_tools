class ActorRestrictionsInformations:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.cantBeAggressed = bool(bin(_box0)[2:].zfill(8)[0])
      self.cantBeChallenged = bool(bin(_box0)[2:].zfill(8)[1])
      self.cantTrade = bool(bin(_box0)[2:].zfill(8)[2])
      self.cantBeAttackedByMutant = bool(bin(_box0)[2:].zfill(8)[3])
      self.cantRun = bool(bin(_box0)[2:].zfill(8)[4])
      self.forceSlowWalk = bool(bin(_box0)[2:].zfill(8)[5])
      self.cantMinimize = bool(bin(_box0)[2:].zfill(8)[6])
      self.cantMove = bool(bin(_box0)[2:].zfill(8)[7])
      _box1 = input.readByte()
      self.cantAggress = bool(bin(_box1)[2:].zfill(8)[0])
      self.cantChallenge = bool(bin(_box1)[2:].zfill(8)[1])
      self.cantExchange = bool(bin(_box1)[2:].zfill(8)[2])
      self.cantAttack = bool(bin(_box1)[2:].zfill(8)[3])
      self.cantChat = bool(bin(_box1)[2:].zfill(8)[4])
      self.cantBeMerchant = bool(bin(_box1)[2:].zfill(8)[5])
      self.cantUseObject = bool(bin(_box1)[2:].zfill(8)[6])
      self.cantUseTaxCollector = bool(bin(_box1)[2:].zfill(8)[7])
      _box2 = input.readByte()
      self.cantUseInteractive = bool(bin(_box2)[2:].zfill(8)[0])
      self.cantSpeakToNPC = bool(bin(_box2)[2:].zfill(8)[1])
      self.cantChangeZone = bool(bin(_box2)[2:].zfill(8)[2])
      self.cantAttackMonster = bool(bin(_box2)[2:].zfill(8)[3])

   def resume(self):
      pass