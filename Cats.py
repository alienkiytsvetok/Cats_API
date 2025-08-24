from tkinter import*
from PIL import Image, ImageTk
import requests
from io import BytesIO

from bottle import response


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status() # нужна для обработки исключений
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img) # если все ок, функция вернет картинку
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None  # если ошибка, то функция ничего не вернет


window = Tk()
window.title("Cats!")
window.geometry("600X480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
