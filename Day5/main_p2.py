board = []
board_height = 8
board_width = 8
commands = []


def import_data(text):
    with open(text) as t:

        # ------ Initialize the board -------------------------#
        for i in range(0, board_height):
            line = t.readline()
            temp = []
            while len(line) > 0:
                test = line[:3].replace('\n', ' ')
                line = line[4:].replace('\n', ' ')
                if test == '    ' or test == '   ':
                    temp.append('spc')
                else:
                    temp.append(test)
            board.append(temp)

        # ------ Initialize commands ------------------------------------------#
        text = t.readlines()
        text = text[2:]
        for com in text:
            commands.append(com.strip().split())
        for i in range(len(commands)):
            commands[i] = [commands[i][1], commands[i][3], commands[i][5]]


def move(command: []):
    num_to_move = int(command[0])
    start_column = int(command[1]) - 1
    end_column = int(command[2]) - 1

    # -- Grab pieces to move and save to list -----------------------------------#
    move_pieces = [p[start_column] for p in board if p[start_column] != 'spc']
    while len(move_pieces) > num_to_move:
        move_pieces.pop(-1)  # ------------------- trying 0 vs -1
    # -- Replace the picked up pieces with 'spc' --------------------------------#
    count = 0
    for x, row in enumerate(board):
        if count < num_to_move:
            if row[start_column] != 'spc':
                board[x][start_column] = 'spc'
                count += 1
        # -- Do we need another row? ------------------------------------------------#
        spc_count = 0
        for r in board:
            if r[end_column] == 'spc':
                spc_count += 1
    # -- There are not enough rows ---------------------------------------------#
    while len(move_pieces) > spc_count:
        board.insert(0, ['spc' for _ in range(len(board[0]))])
        spc_count += 1
    # -- Place pieces from move_pieces to the correct spots --------------------#
    for r in board:
        if len(move_pieces) > 0:
            board[spc_count - 1][end_column] = move_pieces.pop(-1)
            spc_count -= 1


def output():
    end_state = []
    txt = ''

    for column in range(len(board[0])):
        for inc in range(len(board)):
            if board[inc][column] != 'spc':
                end_state.append(board[inc][column])
                break

    for block in end_state:
        txt += block[1]
    print(txt)


if __name__ == '__main__':
    import_data('input.txt')

    for c in commands:
        move(c)

    output()
