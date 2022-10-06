import os
import shutil
from src.parser.class_parser import parse
import json
import re

def get_all_scripts(root_path):
    script_path = []
    for root, dirs, files in os.walk(root_path): 
        path = root.split(os.sep)
        for f in files:
            if(f.endswith(".as")):
                script_path.append(os.path.join(*path,f))
    return script_path

def parse_all_scripts(script_path,root_path_output,mode):
    for i,path in enumerate(script_path):
        print(i+1,"/",len(script_path),path)
        p = path.split("\\")[-1]
        res_python = parse(path,mode)
        output_path = os.path.join(root_path_output,p.replace(".as",".py"))
        with open(output_path,"w") as f:
            f.write(res_python)
            
def get_resources(script_path):
    idclass = {}
    for path in script_path:
        with open(path,"r") as f:
            res = f.read()
            try :
                classname = re.findall(r"class ([a-zA-Z0-9]+)",res)[0]
                classid = re.findall(r"protocolId:uint = ([0-9]+)",res)[0]
                if classid in idclass:
                    print("ERROR: id already exist",classid, classname, idclass[classid])
                else:
                    idclass[classid] = classname
            except IndexError:
                print("ERROR: no protocolId or classname found",path)
                continue
            
    return idclass
            
            
def parse_all(root_path,root_path_output,mode):
    script_path = get_all_scripts(root_path)
    print("nb script : "+str(len(script_path))+'\n')
    parse_all_scripts(script_path,root_path_output,mode)
    
def create_factory(scripts,ressources,root_path_output,mode):
    imports = []
    for path in scripts:
        p = path.split("\\")[-1]
        imports.append("from src.reseau."+mode+"."+p.replace(".as","")+" import "+p.replace(".as",""))
    res = "\n".join(imports)
    
    res += f"\nclass {mode.title()}Factory:\n"
    res += '    id_class = ' + re.sub(r"(\"[0-9]+\": )\"([a-zA-Z0-9]+)\"(,?)",r"\1\2\3",json.dumps(ressources,indent=4),flags=re.MULTILINE)
    res = re.sub(r"^\}","    }",res,flags=re.MULTILINE)
    
    res += f"""
    
    @classmethod
    def get_instance_id(cls,id,content):
        return cls.id_class[str(id)](content)
    """
    
    with open(os.path.join(root_path_output,f"{mode.title()}Factory.py"),"w") as f:
        f.write(res)


######################################## 
################# MAIN #################
########################################

root_path_types = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts_2\\com\\ankamagames\\dofus\\network\\types"
root_path_messages = "C:\\Users\\vincent\\Desktop\\dofus source\\scripts_2\\com\\ankamagames\\dofus\\network\\messages"
root_path_output = "D:\\Documents\\GitHub\\outils_dofus\\src\\reseau"
root_path_output_types = os.path.join(root_path_output,'types')
root_path_output_msg = os.path.join(root_path_output,'messages')

shutil.rmtree(root_path_output_types, ignore_errors=True)
shutil.rmtree(root_path_output_msg, ignore_errors=True)
os.mkdir(root_path_output_types)
os.mkdir(root_path_output_msg)

parse_all(root_path_types,root_path_output_types,"types")
parse_all(root_path_messages,root_path_output_msg,"messages")

types_scripts = get_all_scripts(root_path_types)
types_ressources = get_resources(types_scripts)
create_factory(types_scripts,types_ressources,root_path_output,"types")

msg_scripts = get_all_scripts(root_path_messages)
msg_ressources = get_resources(msg_scripts)
create_factory(msg_scripts,msg_ressources,root_path_output,"messages")