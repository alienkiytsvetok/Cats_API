rom tkinter import*
from PIL import Image, ImageTk
import requests
from io import BytesIO
from bottle import response


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # нужна для обработки исключений
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # изменяем размер загружаемой картинки, чтобы окно вывода оставалось не большим.
        return ImageTk.PhotoImage(img) # если все ок, функция вернет картинку
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None  # если ошибка, то функция ничего не вернет


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


window = Tk()
window.title("Cats!")
window.geometry()

label = Label()
label.pack()

update_button = Button(text="обновить", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"

set_image() # чтобы появилась первая картинка при запуске проекта

window.mainloop()
