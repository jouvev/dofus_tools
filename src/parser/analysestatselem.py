import pickle
import json
from src.interface.choseInterface import ChoseInterface
import os

statselem = json.load(open('ressources\\mapelem.json'))
tfidf_inverse = json.load(open('ressources\\tfidf.json'))
#tfidf_inverse = dict()

"""for mid,tf in tfidf.items():
    for e,occ in tf.items():
        if(e in tfidf_inverse):
            tfidf_inverse[e][mid] = occ
        else:
            tfidf_inverse[e] = {mid:occ}"""


def max_elem(elem):
    res = 0
    for map,occ in tfidf_inverse[elem].items():
        res = max(res,occ)
    return res

sortstats = sorted(statselem.items(), key=lambda x: x[1])
print(len(sortstats))
print("EX: fer à cheval type 1: ", statselem["76221"],max_elem("76221"))
print("EX: crane dans un trou type 1: ", statselem["106216"],max_elem("106216"))
print("EX: champi type 1: ", statselem["106205"],max_elem("106205"))
print("EX: tombe inondé type 1: ", statselem["106423"],max_elem("106423"))
print("EX: tombe en sang type 1: ", statselem["106430"],max_elem("106430"))
print("EX: dofus en bois (je crois) type 1: ", statselem["106345"],max_elem("106345"))
print("EX: clé en or type 1: ", statselem["106323"],max_elem("106323"))
print("EX: clé en or type 2: ", statselem["106325"],max_elem("106325"))
print("EX: serrure en or type 1: ", statselem["106200"],max_elem("106200"))

sortstatsfilter = [s for s in sortstats if s[1] < 500 and s[1] > 100 and max_elem(s[0]) <= 3]

print(len(sortstatsfilter))

elemgfx = json.load(open("C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\elements.json"))["elements_map"]
gfxpath = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\gfx"
gfx = os.listdir(gfxpath)
imgpath = list(set([os.path.join(gfxpath, str(elemgfx[e[0]]["gfx_id"])+".png") for e in sortstatsfilter if 'gfx_id' in elemgfx[e[0]] and str(elemgfx[e[0]]["gfx_id"])+".png" in gfx]))
imgpath.sort()
print(len(imgpath))
poiname = list(json.load(open("ressources\\poi.json",encoding="utf-8")).values())
bind = dict()

def valid_callback(i):
    name = i.get_value()
    gfxid = i.get_img_path().split("\\")[-1][:-4]
    print(name,gfxid)
    bind[gfxid] = name
    i.next_img()

def load():
    try :
        return pickle.load( open( "tmp/backup.pkl", "rb" ) )
    except :
        return 0,dict()
    
i,bind = load()
interface = ChoseInterface(poiname,imgpath,valid_callback=valid_callback)
interface.set_i(i)

def save():
    pickle.dump( (interface.i,bind), open( "tmp/backup.pkl", "wb" ) )   
    interface.destroy()

interface.protocol("WM_DELETE_WINDOW", save)
interface.mainloop()

print(bind)