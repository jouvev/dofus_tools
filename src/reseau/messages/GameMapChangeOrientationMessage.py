from src.reseau.types.ActorOrientation import ActorOrientation

class GameMapChangeOrientationMessage:
   def __init__(self,input):
      self.orientation = ActorOrientation(input)

   def resume(self):
      self.orientation.resume()
