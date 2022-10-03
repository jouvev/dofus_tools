import regex as re
import json 

file_path = "C:\\Users\\vincent\\Desktop\\dofus source\\script2.65\\com\\ankamagames\\dofus\\network\\ProtocolTypeManager.as"
output_file = 'ressources\\id_protocol.json'

with open(file_path) as f:
    text = f.read()

exp = re.findall(r'_[^\[]*\[(\d+)\] = (\w+);',text)
imps = re.findall(r'import ([^;]*);',text)

res = dict()
for n,c in exp:
    for imp in imps:
        if(imp.endswith(c)):
            res[n] = imp

json_res = json.dumps(res,indent=4)
with open(output_file, 'w') as outfile:
    outfile.write(json_res)
    
file_path = "C:\\Users\\vincent\\Desktop\\dofus source\\script2.65\\com\\ankamagames\\dofus\\network\\MessageReceiver.as"
output_file = 'ressources\\id_class.json'

with open(file_path) as f:
    text = f.read()

exp = re.findall(r'_[^\[]*\[(\d+)\] = (\w+);',text)
imps = re.findall(r'import ([^;]*);',text)

res = dict()
for n,c in exp:
    for imp in imps:
        if(imp.endswith(c)):
            res[n] = imp

json_res = json.dumps(res,indent=4)
with open(output_file, 'w') as outfile:
    outfile.write(json_res)