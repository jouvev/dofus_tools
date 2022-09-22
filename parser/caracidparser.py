from calendar import c
import regex as re
import json

caracfile = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts\\damageCalculation\\tools\\StatIds.as"
output_file = "reseau\\caracid.json"

with open(caracfile, "r") as f:
    content = f.read()
    
truc = re.findall(r"public static var ([^:]+):int = (\d+);",content)

res = {id:n for n,id in truc}

json_res = json.dumps(res,indent=4)
with open(output_file, 'w') as outfile:
    outfile.write(json_res)