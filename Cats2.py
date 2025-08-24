from tkinter import*
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


def open_new_window(): # название ф-ции нужно давать такое, что понятно что делает
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("картинка с котиком")
        new_window.geometry()
        label = Label(new_window, image=img)
        label.pack()
        label.image = img


def exit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry()

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


url = "https://cataas.com/cat"

window.mainloop()
