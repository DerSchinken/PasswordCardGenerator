from PasswordCardGenerator import PasswordCard
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import Label, Entry, Button
from os import path, remove
from random import randint
from re import split as rsplit

app = Tk()
app.run = app.mainloop
app.title("Password Card Generator")

asset_path = "/".join(rsplit(r"[/\\]", __file__)[:-1]) + "/assets/"

app.iconphoto(False, PhotoImage(file=f"{asset_path}/img/Logo.png"))
app.geometry("250x100")
app.resizable(False, False)

# create entry descriptors
Label(app, text="Keyword Length:").grid(row=0, padx='5', pady='5')
Label(app, text="Seed").grid(row=1, padx='5', pady='5')

# create entry's
length = Entry(app)
seed = Entry(app)
length.grid(row=0, column=1, padx='5', pady='5')
seed.grid(row=1, column=1, padx='5', pady='5')


class ScrollableImage(Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = Scrollbar(self, orient='vertical', width=sw)
        self.h_scroll = Scrollbar(self, orient='horizontal', width=sw)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set,
                           yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows


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
        card += f", seed='{_seed}'"
    card += ")"

    # execute the generated function call
    card: PasswordCard = eval(card)
    # get a filename that doesn't exist
    filename = asset_path + "tmp/card_" + str(randint(1, 100000)) + ".png"
    while path.exists(filename):
        filename = asset_path + "tmp/card_" + str(randint(1, 100000)) + ".png"
    # temp save for displaying
    card.save_png(filename)

    # load card
    card: PhotoImage = PhotoImage(file=filename)
    # create popup with the card as image
    popup = Toplevel(app)
    popup.iconphoto(False, PhotoImage(file=f"{asset_path}/img/Logo.png"))
    popup.title("Password Card")

    x = ScrollableImage(popup, image=card, width=684 + 10, height=400)
    x.image = card
    # ^ so garbage collection wont collect this and for ease of access
    x.pack()

    popup.resizable(False, False)

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


Button(app, text="Generate", command=lambda: generate_password_card()).grid(row=2, column=1, padx='5', pady='5')

if __name__ == "__main__":
    app.run()
