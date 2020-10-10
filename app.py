from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import math
# some useful fonts
font = ('Verdana',22,'bold')
keypadFont = ('Verdana',22)

# important functions
def iExit():
    iExit = messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit:
        window.destroy()
        return

def all_clear():
    textField.delete(0,END)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(END,ex)

def square_root():
    try:
        ex = textField.get()
        answer = math.sqrt(eval(ex))
        textField.delete(0,END)
        textField.insert(0,answer)
    except Exception as e:
        print("Error", e)
        showerror("Error", e)

def square():
    try:
        ex = textField.get()
        int_ex = int(ex) # converting string into integers
        answer = math.pow(int_ex, 2)
        textField.delete(0,END)
        textField.insert(0,answer)
    except Exception as e:
        print("Error", e)
        showerror("Error", e)

def click_btn_func(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            print("Error", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

#creating a window
window = Tk()
window.title("PyCalc [A simple tool for calculation]")
window.geometry('443x340') # setting dimensions of window, as width*height
# set window color
window.configure(bg='#F3F5F5')
window.resizable(width=False, height=False) # so that the window can't be maximized or increased

#=========================================Menu=============================================================
# creating the menubar
menubar = Menu(window)

# creating menubar options
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard")
filemenu.add_command(label="Scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View help")

window.configure(menu=menubar)

# picture label
pic = PhotoImage(file='calc1.png')
headingLabel = Label(window, image=pic) # for text use text="Pycalc"
headingLabel.pack(side=TOP,pady=5)

# heading label
headingText = Label(window,text="PyCalc",font=font, underline=0, bg='#F3F5F5')
headingText.pack(side=TOP)

# text field
textField = Entry(window, font=('Verdana',22),justify=RIGHT)
textField.place(x=10, y=90, width=420, height=35)

# creating button pad
buttonFrame = Frame(window, width=450, height=340)
buttonFrame.configure(bg='#F3F5F5')
buttonFrame.place(x=10,y=130)

# now adding buttons to frame
# btn1 = Button(buttonFrame,text="1",font=font)
# btn1.pack(side=LEFT)
"""temp = 1
beforeWidth = 0
beforeHeight = 0"""
keypadBtnWidth = 70
keypadBtnHeight = 50
"""
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame,text=str(temp),font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
        btn.place(x = beforeWidth, y = beforeHeight, width = keypadBtnWidth, height = keypadBtnHeight)
        temp += 1
        if i == 0 and j == 0:
            beforeWidth += 1*keypadBtnWidth
            beforeHeight += 0*keypadBtnHeight
        else:
            beforeWidth = j*keypadBtnWidth
            beforeHeight = i*keypadBtnHeight
        btn.bind('<Button-1>', click_btn_func)
"""
btn1 = Button(buttonFrame,text="1",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn1.place(x = 0, y = 0, width = keypadBtnWidth, height = keypadBtnHeight)
btn1.bind('<Button-1>',click_btn_func)

btn2 = Button(buttonFrame,text="2",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn2.place(x = 1*keypadBtnWidth, y = 0, width = keypadBtnWidth, height = keypadBtnHeight)
btn2.bind('<Button-1>',click_btn_func)

btn3 = Button(buttonFrame,text="3",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn3.place(x = 2*keypadBtnWidth, y = 0, width = keypadBtnWidth, height = keypadBtnHeight)
btn3.bind('<Button-1>',click_btn_func)

btn4 = Button(buttonFrame,text="4",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn4.place(x = 0, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn4.bind('<Button-1>',click_btn_func)

btn5 = Button(buttonFrame,text="5",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn5.place(x = 1*keypadBtnWidth, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn5.bind('<Button-1>',click_btn_func)

btn6 = Button(buttonFrame,text="6",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn6.place(x = 2*keypadBtnWidth, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn6.bind('<Button-1>',click_btn_func)

btn7 = Button(buttonFrame,text="7",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn7.place(x = 0, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn7.bind('<Button-1>',click_btn_func)

btn8 = Button(buttonFrame,text="8",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn8.place(x = 1*keypadBtnWidth, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn8.bind('<Button-1>',click_btn_func)

btn9 = Button(buttonFrame,text="9",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn9.place(x = 2*keypadBtnWidth, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)
btn9.bind('<Button-1>',click_btn_func)

zeroBtn = Button(buttonFrame,text="0",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
zeroBtn.place(x = 0, y = 3*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

dotBtn = Button(buttonFrame,text=".",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
dotBtn.place(x = 1*keypadBtnWidth, y = 3*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

percentBtn = Button(buttonFrame,text="%",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
percentBtn.place(x = 2*keypadBtnWidth, y = 3*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

# operational btn
picDivide = PhotoImage(file='divide.png')
divideBtn = Button(buttonFrame,text="/", image=picDivide,font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
divideBtn.place(x = 3*keypadBtnWidth, y = 0*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

picMultiply = PhotoImage(file='multiply.png')
multyBtn = Button(buttonFrame,text="*", image=picMultiply,font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
multyBtn.place(x = 3*keypadBtnWidth, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

picMinus = PhotoImage(file='minus.png')
minusBtn = Button(buttonFrame,text="-", image=picMinus,font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
minusBtn.place(x = 3*keypadBtnWidth, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

plusBtn = Button(buttonFrame,text="+",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
plusBtn.place(x = 3*keypadBtnWidth, y = 3*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)


picClear = PhotoImage(file='backspace.png')
clearBtn = Button(buttonFrame, image=picClear, font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5',command=clear)
clearBtn.place(x = 4*keypadBtnWidth, y = 0*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

startGroupBtn = Button(buttonFrame,text="(",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
startGroupBtn.place(x = 4*keypadBtnWidth, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

picSquare = PhotoImage(file='square.png')
squareBtn = Button(buttonFrame, image=picSquare,font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5', command=square)
squareBtn.place(x = 4*keypadBtnWidth, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

allClearBtn = Button(buttonFrame,text="AC",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5', command=all_clear)
allClearBtn.place(x = 5*keypadBtnWidth, y = 0*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

endGroupBtn = Button(buttonFrame,text=")",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
endGroupBtn.place(x = 5*keypadBtnWidth, y = 1*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

picRoot = PhotoImage(file='square-root.png')
rootBtn = Button(buttonFrame, image=picRoot,font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5', command=square_root)
rootBtn.place(x = 5*keypadBtnWidth, y = 2*keypadBtnHeight, width = keypadBtnWidth, height = keypadBtnHeight)

# equalsBtn
equalBtn = Button(buttonFrame,text="=",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
equalBtn.place(x = 4*keypadBtnWidth, y = 3*keypadBtnHeight, width = 2*keypadBtnWidth, height = keypadBtnHeight)

# binding all buttons
plusBtn.bind('<Button-1>', click_btn_func)
minusBtn.bind('<Button-1>', click_btn_func)
multyBtn.bind('<Button-1>', click_btn_func)
divideBtn.bind('<Button-1>', click_btn_func)
zeroBtn.bind('<Button-1>', click_btn_func)
dotBtn.bind('<Button-1>', click_btn_func)
percentBtn.bind('<Button-1>', click_btn_func)
startGroupBtn.bind('<Button-1>', click_btn_func)
endGroupBtn.bind('<Button-1>', click_btn_func)
equalBtn.bind('<Button-1>', click_btn_func)

# clearBtn.bind('<Button-1>',clear)
# allClearBtn.bind('<Button-1>',all_clear)

window.mainloop() # make window visible by looping it
