from tkinter import *

# Супер простой GUI за 15 минут

work_status = False # При запуске программа должна быть выключена
def change_label_on_click():
    global work_status
    if work_status == False:
        label_status['text'] = 'Статус: Работает'
        btn_on_off['text'] = 'Остановить'
        work_status = True
    elif work_status == True:
        work_status = False
        label_status['text'] = 'Статус: Не работает'
        btn_on_off['text'] = 'Запустить'


window = Tk()
window.title('MyFirstBotGui')
window.geometry('250x250')

label_status = Label(window, text='Статус: Не работает',
                     font=('Arial Bold', 10))
label_status.place(x=62.5, y=10)

btn_on_off = Button(text='Запустить', background='#555', foreground='#ccc',
                    padx='20', pady='8', font='16', command=change_label_on_click)
btn_on_off.place(x=62.5, y=100)

window.mainloop()


