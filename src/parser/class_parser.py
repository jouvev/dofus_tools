import re

def parse(path,mode):
    with open(path) as f:
        lines = f.readlines()
        
    res = ""
        
    for l in lines:
        #rules
        lpython = re.sub("\s*}\s*","",l)
        lpython = re.sub("\s*{\s*","",lpython)
        lpython = re.sub(r"^   (.*)",r"\1",lpython)
        lpython = re.sub(r"(.*);$",r"\1",lpython)
        lpython = re.sub(r" ?: ?[a-zA-Z]+",r"",lpython)
        lpython = re.sub(r"\|\|",r"or",lpython)
        lpython = re.sub(r"&&",r"and",lpython)
        lpython = re.sub(r"package .*","",lpython)
        lpython = re.sub(r"import (.*)",r"",lpython)
        lpython = re.sub(r"(\s*)(override )?(public|private) function ([a-zA-Z_0-9]+)\(([a-zA-Z,0-9]+)\)",r"\1def \4(self,\5) :",lpython)
        lpython = re.sub(r"this.",r"self.",lpython)
        lpython = re.sub(r"super\(([^\)]*)\)",r"super().__init__(\1)",lpython)
        lpython = re.sub(r"super\.",r"super().",lpython)
        lpython = re.sub(r"var ",r"",lpython)
        lpython = re.sub(r" implements (.*)",r"",lpython)
        lpython = re.sub(r"public class ([a-zA-Z]+) (extends) ([a-zA-Z]+)",r"class \1(\3):",lpython)
        lpython = re.sub(r"public class ([a-zA-Z]+)",r"class \1:",lpython)
        lpython = re.sub(r"new ",r"",lpython)
        lpython = re.sub(r"NaN",r"None",lpython)
        lpython = re.sub(r"null",r"None",lpython)
        lpython = re.sub(r"push",r"append",lpython)
        lpython = re.sub(r"false",r"False",lpython)
        lpython = re.sub(r"true",r"True",lpython)
        
        res += lpython
        
    res = res.strip()
    #print(res)

    #init function
    d,f = dectecte_func(res,"deserializeAs_")
    init_f = "\n".join(res.split("\n")[d:f])
    funcs = [init_f]
    
    #other functions
    fnames = re.findall(r"self\.([^\(\.]+)\([^\)]+\)",init_f)
    for fname in fnames:
        d,f = dectecte_func(res,fname)
        funcs.append("\n".join(res.split("\n")[d:f]))
        
    #print('\n'.join(funcs))
        
    #make res    
    res = '\n'.join(res.split("\n")[0:1]+funcs)
    
    res = re.sub(r"def deserializeAs_([a-zA-Z]+)\(self,reader\):",r"def deserializeAs_\1(self,reader):",res)
    res = re.sub(r"def deserializeAs_([a-zA-Z]+)\(([a-zA-Z,]+)\) ?:",r"def __init__(\2):",res)
    res = re.sub(r"super\(\).deserialize",r"super().__init__",res)
    res = re.sub(r"ProtocolTypeManager.getInstance\(([a-zA-Z0-9]+),([_a-zA-Z0-9]+)\)",r"pf.TypesFactory.get_instance_id(\2,input)",res)
    res = re.sub(r"(.*).deserialize\([^\)]+\)\n",r"",res)
    res = re.sub(r"class ([a-zA-Z]+)\(NetworkMessage\)",r"class \1",res)
    res = re.sub(r"throw Error",r"raise RuntimeError",res)
    res = re.sub(r"(if\([^\n]+)",r"\1 :",res)
    res = re.sub(r"else",r"else :",res)
    res = re.sub(r"for\(([^=]+) = ([0-9]+); ?[^<]+ < ([^;]+); [^\)]+\)",r"for \1 in range(\2,\3):",res)
    res = re.sub(r"= ([A-Z][a-zA-Z]*)\(\)",r"= \1(input)",res)
    res = re.sub(r"BooleanByteWrapper.getFlag\(([^,]+),([0-9])\)",r"bool(bin(\1)[2:].zfill(8)[\2])",res)
    res = re.sub(r"PlayableBreedEnum.Feca",r"1",res)
    res = re.sub(r"PlayableBreedEnum.Ouginak",r"18",res)

    res = res.strip()

    #import
    if mode == "types":
        tmp_msg = []
        tmp_types = re.findall(r"= ([A-Z][a-zA-Z]*)\(input\)",res)+re.findall(r"class [a-zA-Z]+\(([a-zA-Z]+)\)",res)
    elif mode == "messages":
        tmp_msg = re.findall(r"class [a-zA-Z]+\(([a-zA-Z]+)\)",res)
        tmp_types = re.findall(r"= ([A-Z][a-zA-Z]*)\(input\)",res)
    
    extends = ""
    for t in tmp_msg:
        extends += "from tmp.messages."+t+" import "+t+"\n"
    for t in tmp_types:
        extends += "from tmp.types."+t+" import "+t+"\n"
        
    if("SubEntity" in path):
        extends = re.sub(r"from tmp.types.EntityLook import EntityLook",r"import tmp.types.EntityLook as et",extends)
        res = re.sub(r"EntityLook\(",r"et.EntityLook(",res)

    if(len(re.findall(r"pf.TypesFactory.get_instance_id",res))>0):
        extends = "import tmp.TypesFactory as pf\n"+extends
    
    if len(extends)>0:
        res = extends+"\n"+res
    
    #init list vide
    init_l = re.findall(r"(self\.[_a-zA-Z0-9]+)\.append",res)
    for i,l in enumerate(res.split("\n")):
        if("def __init__" in l):
            i_init_f = i
            break
        
    res = res.split("\n")
    res = "\n".join(res[:i_init_f+1]+["      "+l+" = []" for l in init_l]+res[i_init_f+1:])
    
    if(i_init_f==len(res.split("\n"))-1):
        res += "\n      pass"
        
    return res

def dectecte_func(res,fname):
    dectectend = False
    f=len(res.split("\n"))
    d=0
    for i,l in enumerate(res.split("\n")):
        if(dectectend and "def" in l):
            f = i
            break
        if(not dectectend and "def "+fname in l):
            d = i
            dectectend=True
    return d,f

