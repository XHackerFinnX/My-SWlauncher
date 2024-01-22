from tkinter import *  
import webbrowser

def win_tk():
    window = Tk()  
    window.title("Приложение")  
    window.geometry('1000x100')
    lbl = Label(window, text="Приложение скачено на рабочем столе (окно можно закрыть)", font=("Arial Bold", 25))  
    lbl.grid(column=0, row=0)  
    window.mainloop()
    return


def callback(url):
    webbrowser.open_new(url)


def win_tk_java():
    root = Tk()
    root.geometry('900x200')
    root.title("Скачать java")
    link_w = Label(root, text="У вас не установлена 8-ая версия java", fg="red", font=("Arial Bold", 25))
    link_w.pack()
    link_wr = Label(root, text="Для правильной работы лаунчера скачайте java 8", fg="red", font=("Arial Bold", 25))
    link_wr.pack()
    link = Button(root, text="Скачать Java 8", fg="orange", cursor="hand2", font=("Arial Bold", 25))
    link.pack()
    link.bind("<Button-1>", lambda e: callback("https://stoneworldlauncher.netlify.app/java-1.8.zip"))
    root.mainloop()
    return


def win_tk_download_mods():
    window = Tk()  
    window.title("Загрузка модов")  
    window.geometry('500x135')
    lbl = Label(window, text="Сейчас идет загрузка модов.", font=("Arial Bold", 25))  
    lbl.pack()
    lbl1 = Label(window, text="Не закрывайте лаунчер!", font=("Arial Bold", 25))  
    lbl1.pack()
    lbl2 = Label(window, text="(Это окно можно закрыть)", font=("Arial Bold", 25))  
    lbl2.pack()
    window.mainloop()
    return