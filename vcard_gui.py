from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk, ImageFilter
from tkinter import filedialog
import pytesseract
import os.path

root = Tk()
root.geometry('800x500')
root.maxsize(1000,500)
root.minsize(600,500)
root.title('Visiting card scanner')
root.iconbitmap('id-card.ico')
img = Image.open('credit-cards.png')
#img = img.resize((600,500), Image.ANTIALIAS)
img.putalpha(120)
img = ImageTk.PhotoImage(img)
bg = Label(root, image=img)
bg.place(relwidth=1, relheight=1)

def upload_file():
    global filename
    global start, last
    filename = filedialog.askopenfilename(initialdir='/Desktop',title='Select a card image', filetypes=(('jpeg files','*.jpg'),('png files','*.png')))
    if filename == '':
        t.delete(1.0,END)
        t.insert(1.0,'You have not provided any image to convert')
        tmsg.showwarning(title='Alert!',message='Please provide proper formatted image') 
        return
    else:
        p_label_var.set('Image uploaded successfully')
        l.config(fg='#0CDD19')
    if filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.PNG') or filename.endswith('.png'):
        filename_rev = filename[::-1]
        last = filename.index('.')
        start = len(filename) - filename_rev.index('/') - 1

def convert():
    try:
        c_label_var.set('Output...')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string(filename)
        t.delete(1.0,END)
        t.insert(1.0,text) 
        root1 = Toplevel()
        root1.title('Uploaded image')
        img1 = ImageTk.PhotoImage(Image.open(filename))
        Label(root1,image=img1).pack()
        root1.mainloop()
    except:
        t.delete(1.0,END)
        t.insert(1.0,'You have not provided any image to convert') 
        tmsg.showwarning(title='Alert!',message='Please provide proper formatted image')
        return
    f_name = filename[start+1:last]+'.txt' 
    f_name = os.path.join(r'Database',f_name)
    f = open(f_name,'w')
    f.write(text)
    f.close()

def contact():
    tmsg.showinfo(title='Contact info',message=('Email: mathurkartik1234@gmail.com', 'Mobile: +91-9587823004'))

mainmenu = Menu(root)
mainmenu.config(font=('Times', 29))
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='Scan/Upload Visiting or Bussiness cards and get all the text of cards',font=('Times', 13))
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Aim',menu=m1)
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='|| Electronics and Communication engineering student ||',font=('Times', 13))
m2.add_command(label='|| Coding Enthusiast ||',font=('Times', 13))
root.config(menu=mainmenu)
mainmenu.add_cascade(label='About us',menu=m2)
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label='E-mail: mathurkartik1234@gmail.com',font=('Times', 13))
m3.add_separator()
m3.add_command(label='Mobile: +91-9587823004',font=('Times', 13))
m3.add_separator()
m3.add_command(label='LinkedIn: https://www.linkedin.com/in/kartik-mathur-97a825160',font=('Times', 13))
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Contact us',menu=m3)

Label(text='Visiting card scanner',bg='#FAD2B8',fg='#39322D',font=('Times',18)).pack(fill='x')
Label(text='Python GUI',bg='#FAD2B8',fg='#39322D',font=('Times New Roman',12, 'italic')).pack(fill='x')

f1 = Frame()
f1.config(bg='white')
Label(f1,text='Browse photo to upload',width=20,font=('Times', 15),bg='white').pack(side='left')
Label(f1,text='format: png/jpeg',bg='white',width=30).pack(side='right',padx=5)
Button(f1,text='Upload card',bg='#F58D4B',font=('Times', 15),width=70,command=upload_file).pack(side='right')
f1.pack(pady=10,fill='x')
p_label_var = StringVar()
p_label_var.set('Please upload an image to scan')
l = Label(textvariable=p_label_var,fg='red',bg='white')
l.pack()

Button(text='Contact developer',border='3',relief='raised',bg='#1E71BB',fg='white', cursor='hand2',command=contact).pack(side='bottom',fill='x')
Label(text='©copyright 2020',bg='#433E3B',fg='white',font=('Times', 10)).pack(side='bottom',fill='x')
Label(text='Developer: Kartik Mathur',bg='#433E3B',fg='white',font=('Times', 10,' italic')).pack(side='bottom',fill='x')
t = Text(root, height='9',font=('Times', 13))
t.pack(side='bottom',fill='x')
t.insert(1.0,'Text of converted card will be shown here...',END)
c_label_var = StringVar()
c_label_var.set('Ready for conversion')
c_label = Label(textvariable=c_label_var)
c_label.pack(side='bottom',anchor='w')
Button(root,text='Scan and Convert',bg='#F58D4B',font=('Times', 15),width=70,command=convert).pack(pady='10',side='bottom')
root.mainloop()