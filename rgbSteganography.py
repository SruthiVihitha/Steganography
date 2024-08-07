from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import cv2
import hashlib

root = tk.Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#d1b3ff")

filename = ""
img = None
h, w, channels = 0, 0, 0
image_path = ""
password = ""
hashed_password = b''
msg = ""
encrypted_image_path = ""

def showimage():
    global filename, img, h, w, channels, image_path
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG File", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img
    img = cv2.imread(filename)
    h, w, channels = img.shape
    image_path = filename
    print(f"Image loaded: {filename}")

def get_password():
    global password, hashed_password
    password = password_entry.get()
    print("Entered password:", password)
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.digest()
    print("Password hashed for security.")

def get_message():
    global msg
    msg = message_entry.get()
    print("Entered secret message:", msg)

def encode():
    global img, msg, hashed_password
    msg += '\x00'  # Append a null character to mark the end of the message
    msg_bin = ''.join(format(ord(char), '08b') for char in msg)
    print("Message converted to binary.")

    data_len = len(msg_bin)
    data_index = 0

    for i in range(h):
        for j in range(w):
            for k in range(3):
                if data_index < data_len:
                    img[i, j, k] = int(bin(img[i, j, k])[:-1] + msg_bin[data_index], 2)
                    data_index += 1
                if data_index >= data_len:
                    break
            if data_index >= data_len:
                break
        if data_index >= data_len:
            break
    print("Message encoded into image.")

def decode(encrypted_image_path, password):
    img = cv2.imread(encrypted_image_path)
    if img is None:
        return "Image not found. Check the file path and make sure the image exists."

    height, width, channels = img.shape
    print(f"Image loaded for decoding: {encrypted_image_path}")

    msg_bin = ""
    for i in range(height):
        for j in range(width):
            for k in range(3):
                msg_bin += bin(img[i, j, k])[-1]

    msg = ""
    for i in range(0, len(msg_bin), 8):
        byte = msg_bin[i:i+8]
        msg += chr(int(byte, 2))
        if msg[-1] == '\x00':
            print("Message decoded successfully.")
            return msg[:-1]

    print("Message decoding completed.")
    return msg[:-1]

def Hide():
    global msg, img
    get_message()
    get_password()
    encode()
    save()
    print("Data hidden successfully!")

def Show():
    global password
    get_password()
    secret_message = decode(encrypted_image_path, password)
    if secret_message:
        text1.delete(1.0, END)
        text1.insert(END, secret_message)
        print("Secret message displayed.")
    else:
        text1.delete(1.0, END)
        text1.insert(END, "Incorrect password or no hidden message found.")
        print("Failed to retrieve message.")

def save():
    global encrypted_image_path, img
    encrypted_image_path = os.path.join(os.path.dirname(filename), "encryptedImage.png")
    cv2.imwrite(encrypted_image_path, img)
    print(f"Image saved to {encrypted_image_path}")

image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)
logo = PhotoImage(file="cyberlogo.png")
Label(root, image=logo, height=70, width=85, bg="#751aff").place(x=15, y=1)
Label(root, text="STEGANOGRAPHY", bg="#d1b3ff", fg="black", font="papyrus 25 bold").place(x=120, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

frame7 = Frame(root, bd=3, width=320, height=280, bg="white", relief=GROOVE)
frame7.place(x=360, y=80)

frame8 = Frame(root, bd=3, width=320, height=100, bg="white", relief=GROOVE)
frame8.place(x=360, y=80)

Label(frame8, text="Hidden Text:", fg="black", bg="white", font="papyrus 12 bold").place(x=0, y=0)

text1 = Text(frame8, font="palatino 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=20, width=321, height=295)

frame9 = Frame(root, bd=3, width=320, height=100, bg="white", relief=GROOVE)
frame9.place(x=360, y=170)

Label(frame9, text="Secret", bg="white", fg="black", font="papyrus 15 bold").place(x=4, y=5)
Label(frame9, text="Message:", fg="black", bg="white", font="papyrus 15 bold").place(x=4, y=40)

frame2 = Frame(root, bd=3, width=250, height=150, bg="white", relief=GROOVE)
frame2.place(x=470, y=185)

message_entry = tk.Entry(frame2)
message_entry.pack()

submit_button = tk.Button(frame2, text="SUBMIT", font="palatino 10 bold", command=get_message, width=27, height=2)
submit_button.pack()

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=150)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame6 = Frame(root, bd=3, width=320, height=95, bg="white", relief=GROOVE)
frame6.place(x=360, y=266)

Label(frame6, text="Password:", fg="black", bg="white", font="papyrus 20 bold").place(x=10, y=5)

frame5 = Frame(root, bd=3, width=300, height=300, bg="white", relief=GROOVE)
frame5.place(x=520, y=280)

password_entry = tk.Entry(frame5, show="*")
password_entry.pack()

submit_button = tk.Button(frame5, text="SUBMIT", font="palatino 10 bold", command=get_password, width=20, height=2)
submit_button.pack()

frame3 = Frame(root, bd=3, bg="#d1b3ff", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=1, font="papyrus 14 bold", command=showimage).place(x=10, y=30)
Button(frame3, text="Save Image", width=10, height=1, font="papyrus 14 bold", command=save).place(x=170, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#d1b3ff", fg="black", font="palatino 10 bold").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#d1b3ff", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=1, font="papyrus 14 bold", command=Hide).place(x=10, y=30)
Button(frame4, text="Show Data", width=10, height=1, font="papyrus 14 bold", command=Show).place(x=170, y=30)
Label(frame4, text="Hidden data retrieval", bg="#d1b3ff", fg="black", font="palatino 11 bold").place(x=20, y=5)

root.mainloop()
