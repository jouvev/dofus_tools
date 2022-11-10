from src.parser.class_parser import parse

path = "C:\\Users\\vincent\\Desktop\\dofus_source\\scripts\\com\\ankamagames\\dofus\\network\\messages\\game\\context\\roleplay\\MapRunningFightDetailsMessage.as"

res = parse(path,"messages")
print(res)