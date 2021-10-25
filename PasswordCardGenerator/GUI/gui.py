from PasswordCardGenerator import PasswordCard
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
from os import path, remove
from random import randint

app = Tk()
app.run = app.mainloop
app.title("Password Card Generator")
app.iconphoto(False, PhotoImage(file="assets/img/Logo.png"))
app.geometry("250x100")
app.resizable(width=False, height=False)

# create entry descriptors
Label(app, text="Keyword Length:").grid(row=0, padx='5', pady='5')
Label(app, text="Seed").grid(row=1, padx='5', pady='5')

# create entry's
length = Entry(app)
seed = Entry(app)
length.grid(row=0, column=1, padx='5', pady='5')
seed.grid(row=1, column=1, padx='5', pady='5')


def generate_password_card():
    # get the length and the seed
    _len = length.get()
    _seed = seed.get()

    # generate the function call
    card: str = "PasswordCard("
    if not _len:
        messagebox.showerror("Error", "No Password length was given!")
        return
    card += _len
    if _seed:
        card += f", seed={_seed}"
    card += ")"

    # execute the generated function call
    card: PasswordCard = eval(card)
    # get a filename that doesn't exist
    filename = "tmp/card_" + str(randint(1, 100000)) + ".png"
    while path.exists(filename):
        filename = "tmp/card_" + str(randint(1, 100000)) + ".png"
    # temp save for displaying
    card.save(filename)

    # load card
    card: PhotoImage = PhotoImage(file=filename)
    # create popup with the card as image
    popup = Toplevel(app)
    popup.iconphoto(False, PhotoImage(file="assets/img/Logo.png"))
    popup.title("Password Card")
    x = Label(popup, image=card)
    x.image = card
    # ^ so garbage collection wont collect this and for ease of access
    x.pack()

    def save():
        filetypes = (("Portable Network Graphics", ".png"),)
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=filetypes)
        # if cancel was pressed
        if file is None:
            return
        # asksavefile returns TextIoWrapper and we need the name of the file
        _file_name = file.name
        # close so other programs (or functions) can access the file
        file.close()
        # safety check
        if not _file_name.endswith(".png"):
            _file_name += ".png"
        # save
        x.image.write(_file_name, format='png')

    Button(popup, text="Save", command=save).pack()
    # remove temp save
    remove(filename)


Button(app, text="Generate", command=lambda: generate_password_card()).\
    grid(row=2, column=1, padx='5', pady='5')

if __name__ == "__main__":
    app.run()
