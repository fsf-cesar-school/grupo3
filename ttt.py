def print_board(board):
    return '```'+ '\n'.join([' | '.join(row) + '\n' + "⎯" * 10 for row in board]) + '```'

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '⠀':
            return True

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '⠀':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '⠀':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '⠀':
        return True

    return False

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '⠀':
                empty_cells.append((row, col))
    return empty_cells

def yukas_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

@bot.command(aliases = ["tictactoe", "jogodavelha", "jdv", "hashtag", "#"])
async def ttt(ctx): 
    board = [['⠀' for _ in range(3)] for _ in range(3)]
    embed3 = discord.Embed(title="𐀔 Yuka's Tic Tac Toe Game!",
                           description="⎯ Let's play Tic Tac Toe!\n" + print_board(board), color=0xdb57e5)
    embed3.set_footer(text="⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀𐀔")
    await ctx.send(embed=embed3)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        await ctx.send("⎯ Enter a row and a column between 0 and 2 (separated by space).")
        try:
            row, col = map(int, (await bot.wait_for('message', check=check)).content.split())
            if board[row][col] == '⠀':
                board[row][col] = 'X'
            else:
                await ctx.send("⎯ Aw, that cell is already taken... Try again!")
                continue
        except (ValueError, IndexError):
            await ctx.send("⎯ Umm, that's an invalid input... Please enter row and column as two integers separated by space!")
            continue

        embed3.description = print_board(board)
        await ctx.send(embed=embed3)
        if check_winner(board):
            await ctx.send("⎯ Wow, congratulations! You won!! (you're cheating, aren't ya? >:/)")

            break
        
        if len(get_empty_cells(board)) == 0:
            await ctx.send("⎯ It's a draw, shall we try again??")
            break

        row, col = yukas_move(board)
        board[row][col] = 'O'

        embed3.description = print_board(board)
        await ctx.send("⎯ My move:", embed=embed3)
        if check_winner(board):
            await ctx.send("⎯ Aha! I won! Good luck next time uwo")
            break
        if len(get_empty_cells(board)) == 0:
            await ctx.send("⎯ It's a draw, shall we try again??")
            break
