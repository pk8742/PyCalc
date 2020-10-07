from tkinter import *
from tkinter.messagebox import *
# some useful fonts
font = ('Verdana',22,'bold')
keypadFont = ('Verdana',22)

# important functions
def all_clear():
    textField.delete(0,END)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(END,ex)

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
window.geometry('460x400') # setting dimensions of window, as width*height
#set window color
window.configure(bg='#F3F5F5')

# picture label
pic = PhotoImage(file='calc1.png')
headingLabel = Label(window, image=pic) # for text use text="Pycalc"
headingLabel.pack(side=TOP,pady=5)

# heading label
headingText = Label(window,text="PyCalc",font=font, underline=0, bg='#F3F5F5')
headingText.pack(side=TOP)

# text field
textField = Entry(window, font=('Verdana',22),justify=RIGHT)
textField.pack(side=TOP,fill=X,padx=10)

# creating button pad
buttonFrame = Frame(window)
buttonFrame.configure(bg='#F3F5F5')
buttonFrame.pack(side=TOP)

# now adding buttons to frame
# btn1 = Button(buttonFrame,text="1",font=font)
# btn1.pack(side=LEFT)
temp = 1
beforeWidth = 0
beforeHeight = 0
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
btn2.place(x = 70, y = 0, width = keypadBtnWidth, height = keypadBtnHeight)
btn2.bind('<Button-1>',click_btn_func)

btn3 = Button(buttonFrame,text="3",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn3.place(x = 140, y = 0, width = keypadBtnWidth, height = keypadBtnHeight)
btn3.bind('<Button-1>',click_btn_func)

btn4 = Button(buttonFrame,text="4",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn4.place(x = 0, y = 50, width = keypadBtnWidth, height = keypadBtnHeight)
btn4.bind('<Button-1>',click_btn_func)

btn5 = Button(buttonFrame,text="5",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn5.place(x = 70, y = 50, width = keypadBtnWidth, height = keypadBtnHeight)
btn5.bind('<Button-1>',click_btn_func)

btn6 = Button(buttonFrame,text="6",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn6.place(x = 140, y = 50, width = keypadBtnWidth, height = keypadBtnHeight)
btn6.bind('<Button-1>',click_btn_func)

btn7 = Button(buttonFrame,text="7",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn7.place(x = 0, y = 100, width = keypadBtnWidth, height = keypadBtnHeight)
btn7.bind('<Button-1>',click_btn_func)

btn8 = Button(buttonFrame,text="8",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn8.place(x = 70, y = 100, width = keypadBtnWidth, height = keypadBtnHeight)
btn8.bind('<Button-1>',click_btn_func)

btn9 = Button(buttonFrame,text="9",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
btn9.place(x = 140, y = 100, width = keypadBtnWidth, height = keypadBtnHeight)
btn9.bind('<Button-1>',click_btn_func)

zeroBtn = Button(buttonFrame,text="0",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
zeroBtn.place(x = 0, y = 150, width = keypadBtnWidth, height = keypadBtnHeight)

dotBtn = Button(buttonFrame,text=".",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
dotBtn.place(x = 70, y = 150, width = keypadBtnWidth, height = keypadBtnHeight)

equalBtn = Button(buttonFrame,text="=",font=keypadFont, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
equalBtn.place(x = 140, y = 150, width = keypadBtnWidth, height = keypadBtnHeight)

# operational btn
plusBtn = Button(buttonFrame,text="+",font=keypadFont, width=4, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
plusBtn.grid(row=0, column=3, padx=5)

minusBtn = Button(buttonFrame,text="-",font=keypadFont, width=4, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
minusBtn.grid(row=1, column=3, padx=5)

multyBtn = Button(buttonFrame,text="*",font=keypadFont, width=4, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
multyBtn.grid(row=2, column=3, padx=5)

divideBtn = Button(buttonFrame,text="/",font=keypadFont, width=4, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5')
divideBtn.grid(row=3, column=3, padx=5)

clearBtn = Button(buttonFrame,text="C",font=keypadFont, width=10, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5',command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame,text="AC",font=keypadFont, width=10, relief='groove',bg='#E7ECEB', activebackground='#F3F5F5', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all buttons
plusBtn.bind('<Button-1>', click_btn_func)
minusBtn.bind('<Button-1>', click_btn_func)
multyBtn.bind('<Button-1>', click_btn_func)
divideBtn.bind('<Button-1>', click_btn_func)
zeroBtn.bind('<Button-1>', click_btn_func)
dotBtn.bind('<Button-1>', click_btn_func)
equalBtn.bind('<Button-1>', click_btn_func)

# clearBtn.bind('<Button-1>',clear)
# allClearBtn.bind('<Button-1>',all_clear)

window.mainloop() # make window visible by looping it
