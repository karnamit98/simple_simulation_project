import random


NUM_LIGHTS=15
LIGHT_RADIUS=4



NE="northeast"
SE="southeast"
NW="northwest"
SW="southwest"
N="north"
S="south"
E="east"
W="west"


COLORS = [
    "#FF0000", # (Red)
    "#00FF00", # (Lime)
    "#0000FF", # (Blue)
    "#FFFF00", # (Yellow)
    "#FF00FF", # (Fuchsia)
    "#00FFFF", # (Aqua)
    "#FF6347", # (Tomato)
    "#FFFF00", # (Yellow)
    "#FF6347", # (Tomato)
    "#800080", # (Purple)
    "#008080", # (Teal)
    "#FFA500", # (Orange)
    "#FF7F50", # (Coral)
    "#DA70D6", # (Orchid)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#800080", # (Purple)
    "#008080", # (Teal)
    "#FFA500", # (Orange)
    "#FFC0CB", # (Pink)
    "#800000", # (Maroon)
    "#FF7F50", # (Coral)
    "#DA70D6", # (Orchid)
    "#DDA0DD", # (Plum)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
    "#20B2AA", # (LightSeaGreen)
]





def randomizeDirection(direction):
    final = ""
    # options = [N,NE,E,SE,S,SW,W,NW]
    if direction==N:
        final = random.choice([NW,N,NE])
    elif direction==NE:
        final = random.choice([N,NE,E])
    elif direction==E:
        final = random.choice([NE,E,SE])
    elif direction==SE:
        final = random.choice([E,SE,S])
    elif direction==S:
        final = random.choice([SE,S,SW])
    elif direction==SW:
        final = random.choice([S,SW,W])
    elif direction==W:
        final = random.choice([SW,W,NW])
    elif direction==NW:
        final = random.choice([W,NW,N])
    else:
        pass
    return final

def movement(initialPos, direction, speed):
    if direction==N:
        initialPos[1] += speed
    elif direction==NE:
        initialPos[0] += speed
        initialPos[1] += speed
    elif direction==E:
        initialPos[0] += speed
    elif direction==SE:
        initialPos[0] += speed
        initialPos[1] -= speed
    elif direction==S:
        initialPos[1] -= speed
    elif direction==SW:
        initialPos[0] -= speed
        initialPos[1] -= speed
    elif direction==W:
        initialPos[0] -= speed
    elif direction==NW:
        initialPos[0] -= speed
        initialPos[1] += speed
    else:
        pass    
    return initialPos
    
def reverseDirection(direction):
    final = ""
    if direction==N:
        final = S
    elif direction==NE:
        final = SW
    elif direction==E:
        final = W
    elif direction==SE:
        final = NW
    elif direction==S:
        final = N
    elif direction==SW:
        final = NE
    elif direction==W:
        final = E
    elif direction==NW:
        final = SE
    else:
        pass

    return final

