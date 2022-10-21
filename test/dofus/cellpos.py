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
        
    return (posx,posy)

print(get_cursor_pos(308))
print(get_cursor_pos(322))
print(get_cursor_pos(316))