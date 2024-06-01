from g4f.client import Client
import g4f

import customtkinter
import threading as th
from PIL import ImageTk, Image

import pathlib, os.path

root = customtkinter.CTk()
root.geometry("500x500")
root.title("ChatGpt")
root.resizable(width=False, height=False)

appdir = pathlib.Path(__file__).parent.resolve()
root.iconbitmap(os.path.join(appdir,'icon.ico'))


lbl_title = customtkinter.CTkLabel(root, text="ChatGpt", font=customtkinter.CTkFont(family="Arial", weight="bold", size=60))
lbl_title.place(x=170, y=15)

image_logo = customtkinter.CTkImage(dark_image=Image.open(os.path.join(appdir,'icon.png')), size=(80, 80))
lbl_logo = customtkinter.CTkLabel(root, text="", image=image_logo)
lbl_logo.place(x=50, y=15)

TB_chat = customtkinter.CTkTextbox(root, width=500, font=customtkinter.CTkFont(family="Arial", weight="bold", size=15))
TB_chat.place(x=0, y=100)
TB_chat.configure(state="disabled")

Entry_TextUser = customtkinter.CTkEntry(root, width=250)
Entry_TextUser.place(x=50, y=350)

lbl_status = customtkinter.CTkLabel(root, text="", font=customtkinter.CTkFont(family="Arial", weight="bold", size=15))
lbl_status.place(x=30, y=400)


def send_mess():
    lbl_status.configure(text="Подождите, мы ждём пока ChatGpt напечатает сообщение...")

    textUser = Entry_TextUser.get()

    Btn_send.configure(state="disabled")
    Entry_TextUser.configure(state="disabled")

    TB_chat.configure(state="normal")
    TB_chat.insert(customtkinter.END, text=f"User: {textUser}\n\n")
    TB_chat.configure(state="disabled")
    client = Client()
    response = client.chat.completions.create(
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.Aichatos,
        messages=[{"role": "user", "content": f"{textUser}"}],
    )
    mess = response.choices[0].message.content
    print(mess)

    TB_chat.configure(state="normal")
    TB_chat.insert(customtkinter.END, text=f"ChatGpt: {mess}\n\n")
    TB_chat.configure(state="disabled")

    lbl_status.configure(text="")
    Btn_send.configure(state="normal")
    Entry_TextUser.configure(state="normal")

    Entry_TextUser.delete(0, customtkinter.END)




Btn_send = customtkinter.CTkButton(root, text="Send", font=customtkinter.CTkFont(family="Arial", weight="bold", size=20), command=lambda: th.Thread(target=send_mess).start())
Btn_send.place(x=320, y=350)
Entry_TextUser.bind('<Return>', command=lambda event: th.Thread(target=send_mess).start())

root.mainloop()