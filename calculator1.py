from tkinter import *
root = Tk()

root.title('Calculator')

res = ''
b = 0
lbl = ''
c = 0
root.geometry("280x395")
operations = Frame(root, height = 340,width = 270)
results = Frame(root, height = 215, width = 270, bg = 'grey')

results.place(x = 5, y = 5)
operations.place(x = 5, y = 50)
def ashu(event):
    n = '('
    cal(n)
def jabu(event):
    n = ')'
    cal(n)
def cal(n):
    global res,b,lbl,c
    if n == 0:
        c += 1
        if c % 2 != 0:
            n = '('
        else:
            n = ')'
    lbl += n
    res = lbl
    result.config(text = lbl)
    print('n:',n)
    if n == '':
        lbl = lbl[:-1]
        res = lbl
        result.config(text = lbl)
    if n == '=':
        d = res[:-1]
        result.config(text = eval(d))
        
def dest():
    root.destroy()
result = Label(results, font = ('Arial','20','bold'))
result.place(x = 100,y = 5, height = 45, width = 100)
result.pack()
n7 = Button(operations, text = '7',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("7"))
n7.place(x = 0, y = 70, width = 60, height = 60)
n8 = Button(operations, text = '8',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("8"))
n8.place(x = 70, y = 70, width = 60, height = 60)
n9 = Button(operations, text = '9',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("9"))
n9.place(x = 140, y = 70, width = 60, height = 60)
n4 = Button(operations, text = '4',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("4"))
n4.place(x = 0, y = 140, width = 60, height = 60)
n5 = Button(operations, text = '5',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("5"))
n5.place(x = 70, y = 140, width = 60, height = 60)
n6 = Button(operations, text = '6',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("6"))
n6.place(x = 140, y = 140, width = 60, height = 60)
n1 = Button(operations, text = '1',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("1"))
n1.place(x = 0, y = 210, width = 60, height = 60)
n2 = Button(operations, text = '2',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("2"))
n2.place(x = 70, y = 210, width = 60, height = 60)
n3 = Button(operations, text = '3',bg = 'black',fg = 'white',font = ('Arial','20','bold'), command = lambda: cal("3"))
n3.place(x = 140, y = 210, width = 60, height = 60)
percentage = Button(operations, text = '()',font = ('Arial'