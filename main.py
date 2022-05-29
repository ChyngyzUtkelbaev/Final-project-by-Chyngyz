import tkinter.ttk
from PIL import Image, ImageTk
import PIL.Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry('320x480')
root.title('Chyngyz Image Converter')
root.config(bg="#ffffff")


Label(root, text='Chyngyz \nImage Converter', font='Verdana 20 bold', fg='#404042', bg="#ffffff").pack()

width = IntVar()
height = IntVar()


Label(root, text='Size = ', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=10, y=280)
Label(root, text='X', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=166, y=280)
Label(root, text='Width', fg='#404042', bg="#ffffff").place(x=70, y=250)
Label(root, text='height', fg='#404042', bg="#ffffff").place(x=195, y=250)


Entry(root, textvariable=width, font='Verdana 10 bold', fg='#404042', bg="#ffffff", borderwidth=3, width=9).place(x=70, y=280)
Entry(root, textvariable=height, font='Verdana 10 bold', fg='#404042', bg="#ffffff", borderwidth=3, width=9).place(x=190, y=280)

Label(root, text='Select Target Format', font='Verdana 10 bold', fg='#404042', bg="#ffffff").place(x=10, y= 330)
from1 = StringVar()
jpgto = tkinter.ttk.Combobox(root, width=10, textvariable= from1)
jpgto['values'] = (' PNG', ' GIF', ' ICO')
jpgto.place(x=190, y=330)
jpgto.current(0)


def choose_file():
    global file
    file=filedialog.askopenfilename(initialdir="/", title="Select a File",
                                        filetypes=(("JPG File", "*.jpg*"), ("all files", "*.*")))
    label_file_explorer.configure(text="File : "+file)


def start_convert():
    width_size = width.get()
    height_size = height.get()

    name = file.split('/')
    finalname = name[-1].replace('.jpeg', '')

    with open(str(file), 'r+b') as f:
        with PIL.Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [width_size, height_size])
            cover.save(f'{finalname}.{from1.get().strip().lower()}', image.format)

    Label(root, text='Image Convert Successfully', fg='#404042', bg="#ffffff",font='Verdana 10 bold').place(x=57, y=410)


label_file_explorer = Label(root, text="File: ", width=50, height=4, fg="#404042", bg="#ffffff")
label_file_explorer.pack()


Button(root, text='Choose File', bg='orange', fg='#ffffff', font='Verdana 10 bold', command=choose_file).place(x=40, y=380)
Button(root, text='Start Convert', bg='green', fg='#ffffff', font='Verdana 10 bold', command=start_convert).place(x=180, y=380)
Label(root, text='Your resized image will be saved in the same directory \nwith your main.py file', fg='#404042',
      bg="#ffffff").place(x=57, y=430)
root.mainloop()