import os

def get_all_path(root_path):
    script_path = []
    for root, dirs, files in os.walk(root_path): 
        path = root.split(os.sep)
        for f in files:
            if(f.endswith(".dlm")):
                script_path.append(os.path.join(*path,f))
    return script_path

output_path = "C:/Users/vincent/Desktop/dofus_source/PyDofus-master/PyDofus-master/output/maps"
allpath = get_all_path("C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\input")
print(len(allpath))
for i,p in enumerate(allpath):
    p = p.replace("\\","/")
    print(f"{i}/{len(allpath)} => {p}")
    os.system(f"python C:/Users/vincent/Desktop/dofus_source/PyDofus-master/PyDofus-master/dlm_unpack.py {p} {output_path}")