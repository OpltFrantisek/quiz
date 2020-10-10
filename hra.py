from guizero import App, Text, TextBox, PushButton, Box


def update_score():
    global tym1_score, tym2_score, welcome_message, welcome_message2

    tmp = "Tým 1 má "+str(tym1_score) +" bodů"
    welcome_message.value = tmp
    tmp = "Tým 2 má "+str(tym2_score) +" bodů"
    welcome_message2.value = tmp


global tym1_score
global tym2_score
global welcome_message
global welcome_message2
tym1_score = 5
tym2_score = 6
app = App(title="Hello world", width=800, height=480)
title_box = Box(app, width="fill", align="top", layout="grid")
buttons_box = Box(app, width="fill", align="bottom")
cancel = PushButton(buttons_box, text="Konec", align="left")
ok = PushButton(buttons_box, text="Další", align="right")
scoreUp = PushButton(buttons_box, command=update_score, text="+1")
ok.bg = 'green'
ok.text_size= 16
cancel.bg = 'green'
cancel.text_size= 16
scoreUp.bg = 'green'
scoreUp.text_size= 16
welcome_message = Text(title_box, text="Tým 1 : ", size=16,
                       font="Times New Roman", color="blue",grid=[0,0])
welcome_message2 = Text(title_box, text="Tým 2 : ", size=16,
                        font="Times New Roman", color="red",grid=[0,1])
otazka = Text(app, text="Byl by někdo kdo by zvládl naskenovat\n co nejdetailněji díl na auto v délce do půl metru?", size=18,
                        font="Times New Roman", color="black")
odpoved = Text(app, text="Správná odpoveď : Ne", size=18,
                        font="Times New Roman", color="black")

app.display()
