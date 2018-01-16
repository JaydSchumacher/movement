# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    z, q = direction
    x += z
    y += q
    if x > 9:
        hp -= 5
        x = 9
    if y > 9:
        hp -= 5
        y = 9
 
    return x, y, hp

print(move((1, 1, 10), (-1, 0)))