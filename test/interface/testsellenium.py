from src.chasse.chasse import DofusDB
import time

print("open")
d1 = DofusDB()
time.sleep(5)
print("close")

print("reopen")
d2 = DofusDB()
time.sleep(5)
print("close")
d2.driver.close()

