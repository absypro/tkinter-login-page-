#!/usr/bin/python3



from tkinter import *
# import oop
# import sqlite




def main():

        root = Tk()

        root.title("absy app 1")
        root.eval("tk::PlaceWindow . center")
        
        root.eval("tk::PlaceWindow . center")
        f = Frame(root, width=100, height=50, bg="#66CCFF")
      
        f.grid(row=0 , column=0,sticky= "nesw")
        f.pack_propagate(False)

        # here we adding menu to our application
        #----------------------------------------------------------------------------------------------------------------

        # here we define the exit button
        b1 = Button(f, text="close", bg="black", fg="white", relief="raised", width=8, height=2,
                        font=("Verdana", 12, "bold"), command=exit, cursor="hand2", activebackground="#badee2",
                        activeforeground="black")
        b1.grid(row=5, column=4, pady=6, padx=2)

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # here  are the   buttons


        b2 = Button(f, text="Login",  bg="blue", fg="black", relief="raised", width=8,
                        height=2, font=("Verdana", 12, "bold"), cursor="hand2", activebackground="#badee2",
                        activeforeground="black")

        b2.grid(row=4, column=4, pady=6, padx=2)


        
        # here  are the Labels 
        l1 = Label(f, text="user name", bg="red", fg="white", relief="raised", width=18,
                        height=2, font=("Verdana", 12, "bold"), cursor="hand2", activebackground="#badee2",
                        activeforeground="black")

        l1.grid(row=1, column=1, pady=6, padx=2)
        
        
        l1 = Label(f, text="password", bg="red", fg="white", relief="raised", width=18,
                        height=2, font=("Verdana", 12, "bold"), cursor="hand2", activebackground="#badee2",
                        activeforeground="black")

        l1.grid(row=2, column=1, pady=6, padx=2)
        

        # here are the entry field
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        eBox1 = Entry(f, width=18,font=("Verdana", 12, "bold"))
        eBox1.grid(row=1, column=6, pady=6, padx=20)

        eBox2 = Entry(f, width=18,font=("Verdana", 12, "bold"))
        eBox2.grid(row=2, column=6, pady=6, padx=20)

        



        root.mainloop()

if __name__ == "__main__":
        main()

