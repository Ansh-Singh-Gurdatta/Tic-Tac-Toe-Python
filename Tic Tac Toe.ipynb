{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5bc6ebd5-9504-4543-af8d-34a25452d8b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#PRINTING THE BOARD\n",
    "from IPython.display import clear_output\n",
    "test_board=['#','X','O','X','O','X','O','X','O','X']\n",
    "def display_board(board):\n",
    "   clear_output()\n",
    "   print(board[7]+'|'+board[8]+'|'+board[9])\n",
    "   print(board[4]+'|'+board[5]+'|'+board[6])\n",
    "   print(board[1]+'|'+board[2]+'|'+board[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "28777bd0-8f50-46d5-9e25-6332189ced65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X|O|X\n",
      "O|X|O\n",
      "X|O|X\n"
     ]
    }
   ],
   "source": [
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ba30c4f-f8fc-4c5d-a6a6-2ce248bebc07",
   "metadata": {},
   "outputs": [],
   "source": [
    "def  player_input():\n",
    "    marker=' '\n",
    "    while not (marker=='X' or marker=='O'):\n",
    "        marker=input(\"Player 1, do you want X or O?\")\n",
    "    player1=marker\n",
    "    if(player1=='X'):\n",
    "        player2='O'\n",
    "        print(\"Then Player 2 is assigned O\")\n",
    "    else:\n",
    "        player2='X'\n",
    "        print(\"Then Player 2 is assigned X\")\n",
    "    return(player1, player2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f4ab7198-ea8a-4d05-9a43-d8776d119374",
   "metadata": {},
   "outputs": [],
   "source": [
    "def place_marker(board,marker,position):\n",
    "    board[position]=marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "16e12ffd-a206-4068-9e8c-d9f4941451ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board, mark):\n",
    "    return ((board[1]==mark and board[2]==mark and board[3]==mark) or \n",
    "            (board[4]==mark and board[5]==mark and board[6]==mark) or \n",
    "            (board[7]==mark and board[8]==mark and board[9]==mark) or \n",
    "            (board[7]==mark and board[4]==mark and board[1]==mark) or \n",
    "            (board[8]==mark and board[5]==mark and board[2]==mark) or \n",
    "            (board[9]==mark and board[6]==mark and board[3]==mark) or \n",
    "            (board[9]==mark and board[5]==mark and board[1]==mark) or \n",
    "            (board[7]==mark and board[5]==mark and board[3]==mark))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e7af5360-c814-4be1-a8aa-b325cdb9c93e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "def choose_first():\n",
    "    flip=random.randint(0,1)\n",
    "    if(flip==0):\n",
    "        return 'Player 2'\n",
    "    else:\n",
    "        return 'Player 1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f3ec0123-7411-4cd3-af16-f3b8eb0067fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "def space_check(board,position):\n",
    "    return board[position]==' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b053f81e-adbf-421c-9bd6-a7e26c7152e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "    for i in range(1,10):\n",
    "        if(space_check(board,i)):\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ddfce078-e4b0-4776-b90a-df168fc88c3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_choice(board):\n",
    "    position=0\n",
    "    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):\n",
    "        position=int(input(\"Choose a number between (1-9) to make your move\"))\n",
    "    return position"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "178c968e-6420-4a26-ab9f-ee30fd07d092",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "    choice=input(\"Play Again? Yes or No?\")\n",
    "    return choice==\"Yes\" or choice==\"yes\" or choice==\"YES\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7903b7a3-9cf8-4a53-b090-67c5853ab5f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X| | \n",
      "X|O|O\n",
      "X| | \n",
      "Congratulations! You have won the game\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Play Again? Yes or No? no\n"
     ]
    }
   ],
   "source": [
    "# print(\"Welcome to Tic Tac Toe\")\n",
    "while True:\n",
    "    the_board=[' ']*10\n",
    "    (player1_marker, player2_marker)=player_input()\n",
    "    turn=choose_first()\n",
    "    print(turn+\" will go first\")\n",
    "    play_game=input(\"Are you ready to play the game? Enter Yes or No\")\n",
    "    if(play_game.lower()[0]=='y'):\n",
    "        game_on=True\n",
    "    else:\n",
    "        game_on=False\n",
    "    while game_on:\n",
    "        if turn=='Player 1':\n",
    "            \n",
    "           display_board(the_board)\n",
    "           position=player_choice(the_board)\n",
    "           place_marker(the_board, player1_marker, position)\n",
    "           if(win_check(the_board, player1_marker)):\n",
    "                display_board(the_board)\n",
    "                print(\"Congratulations! You have won the game\")\n",
    "                game_on=False\n",
    "           else:\n",
    "                if full_board_check(the_board):\n",
    "                  \n",
    "                    display_board(the_board)\n",
    "                    print(\"The game is a draw\")\n",
    "                    break\n",
    "                else:\n",
    "                    turn='Player 2'\n",
    "        else:\n",
    "             display_board(the_board)\n",
    "             position=player_choice(the_board)\n",
    "             place_marker(the_board, player2_marker, position)\n",
    "             if win_check(the_board, player2_marker):\n",
    "                 display_board(the_board)\n",
    "                 print(\"Congratulations! You have won the game\")\n",
    "                 game_on=False\n",
    "             else:\n",
    "                 if full_board_check(the_board):\n",
    "                  \n",
    "                     display_board(the_board)\n",
    "                     print(\"The game is a draw\")\n",
    "                     break\n",
    "                 else:\n",
    "                     turn='Player 1'\n",
    "    if not replay():\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1854eaff-25f1-45d0-896e-557ee3925923",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
