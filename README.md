# Dofus Tools

Aide à la gestion du multi-comptes sur dofus

## Bugs
- touche alt "reste enfoncée" toute seule
    - module keyboard ? 
    - semble apparaître quand shift+tab
- virer moudule keyboard et mouse -> thread qui s'arrête pas (je crois) et full bugs façon
- pas d'interruption de chasse en cas de fin précoce
- 1e indice de la route deja jalonné  
- bug dans le graph [-33,-59]
- bug graph pandala 21 -30 (pb de zone je pense)
- si on descend puis on remonte on clique sur nous meme
- si l'indice n'est pas trouvé crash de toutes les chasses
- si path non trouvé, ne fonctionne plus

## à jouter:
- mise en vente prix auto -1k
    - à la connexion inventorycontentmessage
    - prix min message quand clique sur item
    - entre le prix automatiquement selon quantité dans l'inventaire 
- eviter les mobs goto 
- zaap traveler
- thread pour faire les actions de l'objet de dofus (par exemple quand on fait une action apres avoir recu un packet car pour l'instant c'est le thread du sniffer qui le fait)
