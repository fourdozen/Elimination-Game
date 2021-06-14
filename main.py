import elimgame as game

N = int(input("N:\n"))
game.N = N

game.print_empty_board(N)
critter_pos_list = list(map(int, input("Positions of critters (comma separated):\n").split(',')))
b = game.create_board(N, critter_pos)
game.print_board(b, N)

while not game.is_solved(b):

    hit_critter = int(input(f"Critter to hit (0-{N ** 2 - 1}):\n"))
    print(" ")
    b = game.critter_is_hit(b, hit_critter)
    game.print_board(b, N)

print("Complete")
