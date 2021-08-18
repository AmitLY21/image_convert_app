import os
from tkinter import filedialog
from PIL import Image
import tkinter as tk

"""
In this project Ive learned while coding the tkinter library and pillow library.
Made an application that convert photos from png to jpg and jpg to png.
Added file explorer option and saved the converted photos to a different Directory
"""


class Counter:
    def __init__(self):
        self.counter = 1


counter = Counter()

changed_pic = ''


def browse_files():
    global changed_pic
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Image Files",
                                                                                             "*.png* *.jpg*"),
                                                                                            ("all files", "*.*")))
    changed_pic = filename
    change_text(label_changed, filename)


def jpg_convert(counter):
    if len(changed_pic) > 0:
        im = Image.open(changed_pic).convert('RGB')
        im.save(f'converted_images/converted{counter.counter}.jpg')
        msg = 'Converted to jpg\nSaved in converted_images_directory'
        change_text(txt=label_changed, msg=msg)
        counter.counter += 1
    else:
        change_text(txt=label_changed, msg='Choose Image to convert')


def png_convert(counter):
    if len(changed_pic) > 0:
        im = Image.open(changed_pic)
        im.save(f'converted_images/converted{counter.counter}.png')
        msg = 'Converted to png\nSaved in converted_images_directory'
        change_text(txt=label_changed, msg=msg)
        counter.counter += 1
    else:
        change_text(txt=label_changed, msg='Choose Image to convert')


def change_text(txt, msg):
    txt.config(text=msg)


def open_image_folder():
    path = 'C:\\Users\\user\\Desktop\\Game Dev\\ImageConverter\\converted_images'
    path = os.path.realpath(path)
    os.startfile(path)


# Creating window
window = tk.Tk()
window.title("Image Converter")
window.geometry('300x500')
bg_color = '#536162'
window.configure(bg=bg_color)

# images
icon = tk.PhotoImage(file='images/icon.png')
middle_convert_pic = tk.PhotoImage(file='images/resizing.png')
window.iconphoto(False, icon)

# creating frames
frame = tk.Frame(window)
frame.configure(bg=bg_color)
frame.pack()

# top - frame
top_frame = tk.Frame(frame)
top_frame.grid(row=0, column=0, pady=50)
top_frame.configure(bg=bg_color)

# center mid pic
panel = tk.Label(top_frame, image=middle_convert_pic)
panel.pack(side='top')
panel.configure(bg=bg_color)

# bottom - frame
bottom_frame = tk.Frame(frame)
bottom_frame.grid(row=1, column=0, pady=20)
bottom_frame.configure(bg=bg_color)

# inside bottom frame
b_frame_top = tk.Frame(bottom_frame)
b_frame_top.grid(row=0, column=0, pady=10)
b_frame_top.configure(bg=bg_color)
b_frame_bottom = tk.Frame(bottom_frame)
b_frame_bottom.grid(row=1, column=0, pady=10)
b_frame_bottom.configure(bg=bg_color)

# Creating buttons
button_color = '#F3F4ED'

# File explorer button
button_explore = tk.Button(b_frame_top, text="Browse Files", command=browse_files,
                           bg=button_color)
button_explore.pack(side='top')

# Label that alert to changes
label_changed = tk.Label(b_frame_top, text='Nothing changed yet', bg=bg_color, borderwidth=20)
label_changed.pack(side='bottom')

# Open folder btn
open_folder = tk.Button(b_frame_top, text='Open Folder', command=open_image_folder,
                        bg=button_color)
open_folder.pack(side='bottom', pady=20)

# Converting button and functions
convert_to_jpg = tk.Button(b_frame_bottom, text='Convert to JPG', command=lambda: jpg_convert(counter),
                           bg=button_color)
convert_to_jpg.grid(row=0, column=0)

convert_to_png = tk.Button(b_frame_bottom, text='Convert to PNG', command=lambda: png_convert(counter),
                           bg=button_color)
convert_to_png.grid(row=0, column=2, padx=10)

window.mainloop()
