from tkinter import *
from tkinter.messagebox import *
# some useful fonts
font = ('Verdana',22,'bold')

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

# picture label
pic = PhotoImage(file='calc1.png')
headingLabel = Label(window, image=pic) # for text use text="Pycalc"
headingLabel.pack(side=TOP,pady=5)

# heading label
headingText = Label(window,text="PyCalc",font=font, underline=0)
headingText.pack(side=TOP)

# text field
textField = Entry(window, font=('Verdana',22),justify=RIGHT)
textField.pack(side=TOP,fill=X,padx=10)

# creating button pad
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

# now adding buttons to frame
# btn1 = Button(buttonFrame,text="1",font=font)
# btn1.pack(side=LEFT)
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame,text=str(temp),font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
        btn.grid(row=i, column=j)
        temp += 1
        btn.bind('<Button-1>', click_btn_func)

dotBtn = Button(buttonFrame,text=".",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
dotBtn.grid(row=3, column=0)

zeroBtn = Button(buttonFrame,text="0",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
zeroBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame,text="=",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
equalBtn.grid(row=3, column=2)

# operational btn
plusBtn = Button(buttonFrame,text="+",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
plusBtn.grid(row=0, column=3, padx=5)

minusBtn = Button(buttonFrame,text="-",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
minusBtn.grid(row=1, column=3, padx=5)

multyBtn = Button(buttonFrame,text="*",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
multyBtn.grid(row=2, column=3, padx=5)

divideBtn = Button(buttonFrame,text="/",font=font, width=4, relief='ridge', activebackground='orange', activeforeground='white')
divideBtn.grid(row=3, column=3, padx=5)

clearBtn = Button(buttonFrame,text="<--",font=font, width=10, relief='ridge', activebackground='orange', activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame,text="AC",font=font, width=10, relief='ridge', activebackground='orange', activeforeground='white', command=all_clear)
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
