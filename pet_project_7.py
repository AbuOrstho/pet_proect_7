# Импорт библиотек
import pywhatkit
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Spam'sApp")
root.geometry('360x300')
root.configure(bg='#293133')
root.resizable(False, False)


# Функция для отправки спам-сообщений
def spam():
    nom = spam_nom.get()
    sms = spam_sms.get()
    co = spam_count.get()
    try:
        for i in range(int(co)):
            pywhatkit.sendwhatmsg_instantly(nom, sms, 15, True, 2)
    except:
        print(0)


# Функция для создания окна спама
def spam_button():
    global spam_nom, spam_sms, spam_count

    Button(text='СПАМ', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0, command=spam_button).place(
        x=70, y=30)
    Button(text='РАССЫЛКА', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0,
           command=mailing_buttob).place(x=170, y=30)

    icon_image = PhotoImage(file='дополнения/icons8-whatsapp-240.png')
    root.iconphoto(False, icon_image)

    filling = Frame()
    filling.place(x=30, y=80)

    frame_image = PhotoImage(file="дополнения/icons8-whatsapp-500.png")
    frame_label = Label(filling, bg='#293133', image=frame_image)
    frame_label.pack()

    Label(root, text='Номер телефона', bg='#434B4D', fg='white').place(x=32, y=118)
    spam_nom = Entry(root, width=30, bd=0, highlightthickness=0)
    spam_nom.place(x=145, y=120)

    Label(root, text='Сообщение', bg='#434B4D', fg='white').place(x=32, y=158)
    spam_sms = Entry(root, width=30, bd=0, highlightthickness=0)
    spam_sms.place(x=145, y=160)

    Label(root, text='Кол-во сообщений', bg='#434B4D', fg='white').place(x=32, y=198)
    spam_count = Entry(root, width=30, bd=0, highlightthickness=0)
    spam_count.place(x=145, y=200)

    send_image = PhotoImage(file='дополнения/icons8-отправить-сообщение-50.png')
    start_spam = Button(root, image=send_image, bg='#434B4D', bd=0, highlightthickness=0, command=spam)
    start_spam.place(x=150, y=238)
    root.mainloop()


# Функция для создания окна рассылки
def mailing_buttob():
    global mailing_nom, mailing_sms

    Button(text='СПАМ', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0, command=spam_button).place(
        x=70, y=30)
    Button(text='РАССЫЛКА', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0,
           command=mailing_buttob).place(x=170, y=30)

    icon_image = PhotoImage(file='дополнения/icons8-whatsapp-240.png')
    root.iconphoto(False, icon_image)

    filling = Frame()
    filling.place(x=30, y=80)

    frame_image = PhotoImage(file="дополнения/icons8-whatsapp-500.png")
    frame_label = Label(filling, bg='#293133', image=frame_image)
    frame_label.pack()

    Label(root, text='Файл с номерами .txt', bg='#434B4D', fg='white').place(x=120, y=84)
    Button(root, text='▼', width=2, height=1, command=select_file1).place(x=280, y=107)
    mailing_nom = Entry(root, width=35, bd=0, highlightthickness=0)
    mailing_nom.place(x=62, y=110)
    mailing_nom.insert(END, "+71234567890,+71234567891...")

    Label(root, text='Сообщение', bg='#434B4D', fg='white').place(x=140, y=130)
    mailing_sms = Text(root, width=30, height=5, bd=0, highlightthickness=0)
    mailing_sms.place(x=62, y=156)

    send_image = PhotoImage(file='дополнения/icons8-отправить-сообщение-50.png')
    start_mailing = Button(root, image=send_image, bg='#434B4D', bd=0, highlightthickness=0, command=mailing)
    start_mailing.place(x=150, y=238)
    root.mainloop()


# Функция для обработки выбора файла с номерами для рассылки
def select_file1(*args):
    global filename1
    filename1 = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select',
                                           filetypes=(('TXT Files', '*.txt'),))
    if filename1:
        mailing_nom.delete(0, END)
        mailing_nom.insert(END, str(filename1))


# Функция для рассылки сообщений на список номеров
def mailing():
    nom = mailing_nom.get()
    sms = mailing_sms.get('1.0', END)

    crimefile = open(nom, 'r')
    yourResult = [line.split(',') for line in crimefile.readlines()]
    for i in range(len(yourResult[0])):
        send = pywhatkit.sendwhatmsg_instantly(yourResult[0][i], sms, 15, True, 2)


# Создание кнопок и элементов интерфейса
Button(text='СПАМ', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0, command=spam_button).place(
    x=70, y=30)
Button(text='РАССЫЛКА', fg='white', font=('Time New Roman', 15, 'bold'), bg='#293133', bd=0,
       command=mailing_buttob).place(x=170, y=30)

# Запуск основного цикла обработки событий
root.mainloop()
