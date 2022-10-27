from src.chasse.dofusnoob import DofusNoob
import time

d = DofusNoob()
time.sleep(1)
print(d.get_hint(1,1,'left',"Clef dorée"))