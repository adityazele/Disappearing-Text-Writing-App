import tkinter as tk

timer = None
user_text = ''


def start_calculating(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == 'BackSpace':
        user_text = user_text[0: len(user_text)-1]
    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)


def reset_app():
    global timer, user_text
    text_box.delete('1.0', 'end')
    user_text = ''
    timer = None


def save():
    global user_text
    if user_text == "":
        return
    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return


window = tk.Tk()
window.title('Disappearing Text Writing App')

heading = tk.Label(text='Let your words dance in magic, but keep the rhythm, for they fade if you pause for 5 seconds.', fg='#DAA520', bg='#E6E6FA')
heading.grid(row=0, column=0)
heading.config(width=103)

text_box = tk.Text()
text_box.grid(row=1, column=0)
text_box.config(width=90, height=25)

save_btn = tk.Button(text='save', width=102, command=save, bg='#40E0D0')
save_btn.grid(row=2, column=0)

text_box.bind('<KeyPress>', start_calculating)

window.mainloop()
