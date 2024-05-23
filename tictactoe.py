from tkinter import*
from tkinter import messagebox
mansLogs=Tk()
mansLogs.title("TicTacToe")

speletajsx=True 
count=0 #aizpildīto rūtiņu skaits

def btnClick(button):
    global speletajsx,count
    if button["text"]==""and speletajsx==True:
        button["text"]="X"
        speletajsx=False
        count+=1 
        checkWinner()

    elif button["text"]==""and speletajsx==False:
        button["text"]="0"
        speletajsx=True
        count+=1 
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis.")

def disableButtons(): #izslēdz pogas
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0

def reset(): #izslēdz pogas
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=''
    btn2["text"]=''
    btn3["text"]=''
    btn4["text"]=''
    btn5["text"]=''
    btn6["text"]=''
    btn7["text"]=''
    btn8["text"]=''
    btn9["text"]=''


def checkWinner():
    global winner
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or
        btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or
        btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or
        btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" or
        btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" or
        btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" or
        btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" or
        btn7["text"]=="X" and btn5["text"]=="X" and btn3["text"]=="X"):
            winner=True
            disableButtons()
            messagebox.showinfo('TicTacToe','Spēlētājs X ir uzvarējis.')

    elif  (btn1["text"]=="0" and btn2["text"]=="0" and btn3["text"]=="0" or
        btn4["text"]=="0" and btn5["text"]=="0" and btn6["text"]=="0" or
        btn7["text"]=="0" and btn8["text"]=="0" and btn9["text"]=="0" or
        btn1["text"]=="0" and btn4["text"]=="0" and btn7["text"]=="0" or
        btn2["text"]=="0" and btn5["text"]=="0" and btn8["text"]=="0" or
        btn3["text"]=="0" and btn6["text"]=="0" and btn9["text"]=="0" or
        btn1["text"]=="0" and btn5["text"]=="0" and btn9["text"]=="0" or
        btn7["text"]=="0" and btn5["text"]=="0" and btn3["text"]=="0"):
            winner=True
            disableButtons()
            messagebox.showinfo('TicTacToe','Spēlētājs 0 ir uzvarējis.')
    elif count==9:
        winner==False
        disableButtons()
        messagebox.showinfo('TicTacToe','Neizšķirts.')
    return

btn1=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn9))

galvenaIzvelne=Menu(mansLogs) #izveido galveno izvēlni
mansLogs.config(menu=galvenaIzvelne) #pievieno galvenajam logam

#mazā izvēlne
opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)

btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)



mansLogs.mainloop()
