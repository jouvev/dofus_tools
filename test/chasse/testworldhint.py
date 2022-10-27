from src.chasse.worldhint import WorldHint

w = WorldHint.get_instance()
print(w.posToNode[(-22,-47)].get_hints())
print(w.get_hint(-17,-47,4,"Étoile en papier plié"))