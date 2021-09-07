from tkinter import *
from tkinter import messagebox

#For gui
r=Tk()
r.geometry("700x700")
#355x380

player=1
bx1='1'
bx2='2'
bx3='3'
bx4='4'
bx5='5'
bx6='6'
bx7='7'
bx8='8'
bx9='9'
symbol='k'
cnt=0


label=Label(r,text="WELCOME",font=('Comics',20,'bold'))
label.grid(row=0,column=0)
labe2=Label(r,text="TO TIC-TAC-TOE",font=('Comics',20,'bold'))
labe2.grid(row=0,column=1)
labe3=Label(r,text=" GAME :)",font=('Comics',20,'bold'))
labe3.grid(row=0,column=2)
labe4=Label(r,text="DESIGNED",font=('Comics',20,'bold'))
labe4.grid(row=4,column=0)
labe5=Label(r,text="BY LIKHITH JSC",font=('Comics',20,'bold'))
labe5.grid(row=4,column=1)


#defining each button
def activate(box):
    global player
    global bx1
    global bx2
    global bx3
    global bx4
    global bx5
    global bx6
    global bx7
    global bx8
    global bx9
    global symbol
    global cnt
    cnt=cnt+1

    if box==1 and player==1:
        button1.configure(text="X",bg="red")
        player=2
        bx1='X'
    elif box==1 and player==2:
        button1.configure(text="O",bg="blue")
        player=1
        bx1='O'


    elif box == 2 and player == 1:
        button2.configure(text="X",bg="red")
        player = 2
        bx2 = 'X'
    elif box == 2 and player == 2:
        button2.configure(text="O",bg="yellow")
        player = 1
        bx2 = 'O'


    elif box == 3 and player == 1:
        button3.configure(text="X",bg="red")
        player = 2
        bx3 = 'X'
    elif box == 3 and player == 2:
        button3.configure(text="O",bg="yellow")
        player = 1
        bx3 = 'O'


    elif box == 4 and player == 1:
        button4.configure(text="X",bg="red")
        player = 2
        bx4 = 'X'
    elif box == 4 and player == 2:
        button4.configure(text="O",bg="yellow")
        player = 1
        bx4 = 'O'


    elif box == 5 and player == 1:
        button5.configure(text="X",bg="red")
        player = 2
        bx5 = 'X'
    elif box == 5 and player == 2:
        button5.configure(text="O",bg="yellow")
        player = 1
        bx5 = 'O'



    elif box == 6 and player == 1:
        button6.configure(text="X",bg="red")
        player = 2
        bx6 = 'X'
    elif box == 6 and player == 2:
        button6.configure(text="O",bg="yellow")
        player = 1
        bx6 = 'O'



    elif box == 7 and player == 1:
        button7.configure(text="X",bg="red")
        player = 2
        bx7 = 'X'
    elif box == 7 and player == 2:
        button7.configure(text="O",bg="yellow")
        player = 1
        bx7 = 'O'



    elif box == 8 and player == 1:
        button8.configure(text="X",bg="red")
        player = 2
        bx8 = 'X'
    elif box == 8 and player == 2:
        button8.configure(text="O",bg="yellow")
        player = 1
        bx8 = 'O'



    elif box == 9 and player == 1:
        button9.configure(text="X",bg="red")
        player = 2
        bx9 = 'X'
    elif box == 9 and player == 2:
        button9.configure(text="O",bg="yellow")
        player = 1
        bx9 = 'O'




    #For displaying the winner
    if bx1 == bx2 == bx3=='X' or bx4 == bx5 == bx6=='X' or bx7 == bx8 == bx9=='X' or bx1 == bx4 == bx7=='X' or bx2 == bx5 == bx8=='X' or bx3 == bx6 == bx9=='X':
        player=1
        symbol="X"
        messagebox._show("Game end",f"player {player} that is player {symbol} wins")
        exit(0)
    elif bx1 == bx2 == bx3=='O' or bx4 == bx5 == bx6 =='O' or bx7 == bx8 == bx9=='O' or bx1 == bx4 == bx7=='O' or bx2 == bx5 == bx8=='O' or bx3 == bx6 == bx9=='O':
        player=2
        symbol="O"
        messagebox._show("Game end",f"player {player} that is player {symbol} wins")
        exit(0)

    elif bx1 == bx5 == bx9 =="X" or bx3 == bx5 == bx7 =="X":
        player = 1
        symbol = "X"
        messagebox._show("Game end",f"player {player} that is player {symbol} wins")
        exit(0)
    elif bx1 == bx5 == bx9 =="O" or bx3 == bx5 == bx7 =="O":
        player = 2
        symbol = "O"
        messagebox._show("Game end",f"player {player} that is player {symbol} wins")
        exit(0)
    elif cnt==9:
        messagebox._show("Game end","Draw")
        exit(0)


#creating buttons in grid way for tictactie layout
button1=Button(r,text=' ',command= lambda:activate(1))
button1.grid(row=1,column=0,ipadx=90,ipady=90)
button2=Button(r,text=' ',command= lambda:activate(2))
button2.grid(row=1,column=1,ipadx=90,ipady=90)
button3=Button(r,text=' ',command= lambda:activate(3))
button3.grid(row=1,column=2,ipadx=90,ipady=90)
button4=Button(r,text=' ',command= lambda:activate(4))
button4.grid(row=2,column=0,ipadx=90,ipady=90)
button5=Button(r,text=' ',command= lambda:activate(5))
button5.grid(row=2,column=1,ipadx=90,ipady=90)
button6=Button(r,text=' ',command= lambda:activate(6))
button6.grid(row=2,column=2,ipadx=90,ipady=90)
button7=Button(r,text=' ',command= lambda:activate(7))
button7.grid(row=3,column=0,ipadx=90,ipady=90)
button8=Button(r,text=' ',command= lambda:activate(8))
button8.grid(row=3,column=1,ipadx=90,ipady=90)
button9=Button(r,text=' ',command= lambda:activate(9))
button9.grid(row=3,column=2,ipadx=90,ipady=90)




r.mainloop()