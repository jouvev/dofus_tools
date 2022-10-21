from src.dofus.direction import Direction
XCELL0 = 364
YCELL0 = 40
DIMX = 88
DIMY = 44

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
    
    if(type == 8 or type == 32):
        return (posx,posy)
    
    if(Direction(direction) == Direction.up):
        posy -= DIMY//3
    elif(Direction(direction) == Direction.down):
        posy += DIMY//1.5
    elif(Direction(direction) == Direction.left):
        posx -= DIMX//1.5
    elif(Direction(direction) == Direction.right):
        posx += DIMX//1
    elif(Direction(direction) == Direction.right_down):
        posx += DIMX//1.5
        posy += DIMY//1.5
    elif(Direction(direction) == Direction.right_up):
        posx += DIMX//1.5
        posy -= DIMY//1.5
    elif(Direction(direction) == Direction.left_down):
        posx -= DIMX//1.5
        posy += DIMY//1.5
    elif(Direction(direction) == Direction.left_up):
        posx -= DIMX//1.5
        posy -= DIMY//1.5
    else:
        raise ValueError("direction not found")
    
    return (int(posx),int(posy))