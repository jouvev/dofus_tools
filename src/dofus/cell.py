from src.dofus.direction import Direction
from src.dofus.mapposition import MapPosition

XCELL0 = 364
YCELL0 = 40
DIMX = 88
DIMY = 44
XLEFT = 349
XRIGHT = 1574
YUP = 34 
YDOWN = 907

NBPARLIGNE = 14

def get_cursor_pos(cellid):
    if (cellid // NBPARLIGNE)%2 == 0 :#ligne paire on part de la cellule 0
        posx = XCELL0 + (cellid % (NBPARLIGNE)) * DIMX
        posy = YCELL0 + (cellid // (NBPARLIGNE*2)) * DIMY
    else:
        posx = XCELL0 + DIMX//2 + (cellid % (NBPARLIGNE)) * DIMX
        posy = YCELL0 + DIMY//2 + (cellid // (NBPARLIGNE*2)) * DIMY
        
    return (int(posx),int(posy))

def get_cursor_pos_to_change_map(cellid,direction,type):
    posx, posy = get_cursor_pos(cellid)
    paire = (cellid // NBPARLIGNE)%2 == 0
    
    if type == 32 or Direction(direction) == Direction.unknown or type == 8:
        return (posx,posy)
            
    if(Direction(direction) == Direction.up):
        posy = YUP
    elif(Direction(direction) == Direction.down):
        posy = YDOWN  
    elif(Direction(direction) == Direction.left):
        posx = XLEFT
    elif(Direction(direction) == Direction.right):
        posx = XRIGHT
    else:
        raise ValueError("direction not found")
    
    return (int(posx),int(posy))