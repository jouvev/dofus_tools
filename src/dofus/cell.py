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

def get_cursor_pos_to_change_map(mapsrc,mapdst,cellid,direction,type):
    posx, posy = get_cursor_pos(cellid)
    paire = (cellid // NBPARLIGNE)%2 == 0
    if((type == 32 and Direction(direction) != Direction.unknown) or type == 8):
        return (posx,posy)
    
    if(Direction(direction) == Direction.unknown):
        xsrc,ysrc = MapPosition.get_pos(mapsrc)
        xdst,ydst = MapPosition.get_pos(mapdst)
        dx = xdst - xsrc
        dy = ydst - ysrc
        if(dx < 0):
            if(dy < 0):
                direction = Direction.left_up
            elif(dy > 0):
                direction = Direction.left_down
            else: #dy = 0
                direction = Direction.left
        elif(dx > 0):
            if(dy < 0):
                direction = Direction.right_up
            elif(dy > 0):
                direction = Direction.right_down
            else: #dy = 0
                direction = Direction.right
        else:
            if(dy < 0):
                direction = Direction.up
            if(dy > 0):
                direction = Direction.down
            else:
                raise Exception("same map")
            
    if(Direction(direction) == Direction.up):
        posy = YUP
    elif(Direction(direction) == Direction.down):
        posy = YDOWN  
    elif(Direction(direction) == Direction.left):
        posx = XLEFT
    elif(Direction(direction) == Direction.right):
        posx = XRIGHT
    elif(Direction(direction) == Direction.right_down):
        if(paire):
            posx += DIMX
            posy += DIMY/1.5
        else:
            posx += DIMX/2
            posy += DIMY/3
    elif(Direction(direction) == Direction.right_up):
        if(paire):
            posx += DIMX
            posy -= DIMY/3
        else:
            posx += DIMX/2
            posy -= DIMY/1.5
    elif(Direction(direction) == Direction.left_down):
        if(paire):
            posx -= DIMX/2
            posy += DIMY/1.5
        else:
            posx -= DIMX
            posy += DIMY/3
    elif(Direction(direction) == Direction.left_up):
        if(paire):
            posx -= DIMX/2
            posy -= DIMY/3
        else:
            posx -= DIMX
            posy -= DIMY/1.5
    else:
        raise ValueError("direction not found")
    
    return (int(posx),int(posy))