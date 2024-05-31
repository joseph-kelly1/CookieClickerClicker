import pyautogui, time, customtkinter, tkinter
from pynput.mouse import Button, Controller

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x350")
img = tkinter.Image("photo", file="cookieclicker-removebg-preview.png")
root.tk.call('wm', 'iconphoto', root._w, img)
root.title("CookieClickerClicker")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Cookie Clicker Clicker",
                               font=customtkinter.CTkFont(size=20, weight="bold"))
label.pack(pady=12, padx=10)

sButton = customtkinter.CTkButton(master=frame, text="Start", font=customtkinter.CTkFont(size=15))
sButton.pack(pady=6, padx=10)

eButton = customtkinter.CTkButton(master=frame, text="Stop", font=customtkinter.CTkFont(size=15))
eButton.pack(pady=18, padx=10)

speedLabel = customtkinter.CTkLabel(master=frame, text="Speed", width=120, height=25, corner_radius=8)
speedLabel.pack(padx=10)
speedBar = customtkinter.CTkSlider(master=frame, from_=10, to=.5)
speedBar.pack(padx=10)

status = "Off"
label = customtkinter.CTkLabel(master=frame, text="Status: " + status, font=customtkinter.CTkFont(size=15), width=120,
                               height=25, corner_radius=8)
label.pack(pady=18, padx=10)

isPinned = tkinter.StringVar()
pinBox = customtkinter.CTkCheckBox(master=frame, text="Pin to Screen", variable=isPinned, onvalue="on", offvalue="off")
pinBox.pack(pady=6, padx=10)


def start_clicking():
    global clicking
    global status
    clicking = True
    status = "On"
    label.configure(text="Status: " + status)


def stop_clicking():
    global clicking
    global status
    clicking = False
    status = "Off"
    label.configure(text="Status: " + status)


sButton.configure(command=start_clicking)
eButton.configure(command=stop_clicking)

clicking = False

while True:
    if clicking:
        x, y = pyautogui.position()
        if 90 < x < 340 and 310 < y < 550:
            Controller().click(Button.left)
            speed = speedBar.get()
            time.sleep(0.005 * speed)

    isPinned = pinBox.get()
    if isPinned == "on":
        root.attributes('-topmost', True)
    if isPinned == "off":
        root.attributes('-topmost', False)

    root.update_idletasks()
    root.update()
