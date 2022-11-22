# -------
# IMPORTS
# -------
import tkinter as tk
import tkmacosx as tkm  # using tkmacosx cause I am workin on mac and so I can change color of a button
import password_generator as pg
import ast  # to open the files
import encoding_and_decoding as ed

# ---------
# VARIABLES
# ---------
width = 800
height = 500
entered_text = ""
password_dictornary = {}

# ------
# COLORS
# ------
bg_color = '#333'
fg_color = '#FEC260'

# for buttons
bg_button_active = '#A12568'
bg_button_passive = '#333'
fg_button_active = '#A12568'
fg_button_passive = '#FEC260'
bg_button_hover = '#2A0944'

# for entrys
bg_color_entry = "#565656"


# -------
# TKINTER
# -------
class PasswordManager(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Passwordmanager by Wotan")
        self.geometry(f"{width}x{height}")
        container = tk.Frame(self)
        self.frames = {
            "title": Startmenu(self),
            "passdic": Dictonary(self),
            "generator": Generator(self)
        }
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.show_title()
        self.config(bg=bg_color)
        container.grid(row=0, column=0, stick="nsew")

    def show_frame(self, name):
        frame = self.frames[name]

        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_title(self):
        self.show_frame("title")

    def show_dic(self):
        self.show_frame("passdic")

    def show_generator(self):
        self.show_frame("generator")

    # makes a x by x grid
    def generate_grid(self, number, checking=False):
        for r in range(number):
            tk.Grid.rowconfigure(self, r, weight=1)
            for c in range(number):
                tk.Grid.columnconfigure(self, c, weight=1)
        if checking:
            show_grid(self, number)


class Startmenu(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        # creates a 9x9 grid with more or less same size
        PasswordManager.generate_grid(self, 10, )

        # changing bg of the frame
        self.config(bg=bg_color)
        # Label
        header(self, "Passwordmanager by Wotan", 0, 5, 30, "w")
        # tk.Label(self, text="You want to see or create passwords?", bg=bg_color, fg=fg_color).grid(row=1, column=0,
        # columnspan=5,
        # padx=30,
        # sticky="w")

        # Buttons
        tkm.Button(self, text="Create new password", command=lambda: root.show_generator(), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover, font=("Arial", 25, "roman"), pady=4).grid(row=2, column=5,
                                                                                             columnspan=3)
        tkm.Button(self, text="See old passwords", command=lambda: root.show_dic(), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover, font=("Arial", 25, "roman"), pady=4).grid(row=3, column=5,
                                                                                             columnspan=3)
        exit_button(self, "Exit", 8, 9, "s")


class Dictonary(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        global password_dictornary

        PasswordManager.generate_grid(self, 9)

        # changing bg of the frame
        self.config(bg=bg_color)

        # List to show passwords
        self.option_list = []
        if not password_dictornary:
            self.option_list.append("You have no password saved")
        else:
            for _ in password_dictornary:
                self.option_list.append(_)

        # Labels
        header(self, "Passwordmanager by Wotan", 0, 2, 24, "w")
        tk.Label(self, text="Website:", bg=bg_color, fg=fg_color).grid(row=2, column=2, sticky="e")
        tk.Label(self, text="Username:", bg=bg_color, fg=fg_color).grid(row=3, column=2, sticky="e")
        tk.Label(self, text="Password:", bg=bg_color, fg=fg_color).grid(row=4, column=2, sticky="e")
        self.name_website = tk.Label(self, text=f"www.example.com", bg=bg_color, fg=fg_color)
        self.name_username = tk.Label(self, text=f"example_username", bg=bg_color, fg=fg_color)
        self.name_password = tk.Label(self, text="example_password_1", bg=bg_color, fg=fg_color)

        # Buttons
        tkm.Button(self, text="Reload", command=lambda: self.add_option(), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover).grid(row=3, column=0, sticky="n")
        self.remove_button = tkm.Button(self, text="Remove", command=lambda: self.remove_pass(), bg=bg_button_passive,
                                        fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                                        overbackground=bg_button_hover)
        # Copy Buttons
        self.copy1 = tkm.Button(self, text="Copy", command=lambda: [copy_to_clipboard(self, self.name_website),
                                                                    self.refresh_button(self.copy1)],
                                bg=bg_button_passive,
                                fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                                overbackground=bg_button_hover)
        self.copy2 = tkm.Button(self, text="Copy", command=lambda: [copy_to_clipboard(self, self.name_username),
                                                                    self.refresh_button(self.copy2)],
                                bg=bg_button_passive,
                                fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                                overbackground=bg_button_hover)
        self.copy3 = tkm.Button(self, text="Copy", command=lambda: [copy_to_clipboard(self, self.name_password),
                                                                    self.refresh_button(self.copy3)],
                                bg=bg_button_passive,
                                fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                                overbackground=bg_button_hover)
        exit_button(self)
        back_button(self, root)

        # Variable for option menu
        self.variable = tk.StringVar(self)
        self.variable.set(self.option_list[0])

        # Option menu
        self.option_menu = tk.OptionMenu(self, self.variable, *self.option_list)
        self.option_menu.config(bg=bg_color, fg=fg_color)
        self.option_menu["menu"].config(bg=bg_color, fg=fg_color)
        self.option_menu.config(widt=20)
        self.option_menu.grid(row=2, column=0)

        # show old data
        self.add_option()

        # Trace
        self.variable.trace("w", self.callback)

        # Grid
        self.copy1.grid(row=2, column=4, sticky="w")
        self.copy2.grid(row=3, column=4, sticky="w")
        self.copy3.grid(row=4, column=4, sticky="w")
        self.remove_button.grid(row=3, column=0, sticky="s")
        self.name_website.grid(row=2, column=3, sticky="w")
        self.name_username.grid(row=3, column=3, sticky="w")
        self.name_password.grid(row=4, column=3, sticky="w")

    def callback(self, *args):
        self.add_option()
        self.name_website.config(text=self.variable.get())
        self.name_username.config(text=password_dictornary[self.variable.get()][0])
        self.name_password.config(text=password_dictornary[self.variable.get()][1])

    # todo: reloading the optionmenu box without reload button
    def update_option_menu(self):
        menu = self.option_menu["menu"]
        menu.delete(0, "end")
        for string in self.option_list:
            menu.add_command(label=string, command=lambda value=string: self.variable.set(value))

    def add_option(self):
        del self.option_list[:]
        for website in password_dictornary:
            self.option_list.append(website)
        self.update_option_menu()

    def remove_pass(self):

        # deletes the string
        del password_dictornary[self.variable.get()]
        self.add_option()

    # changes the text to 'copied' and back
    def refresh_button(self, button, time=1500, text1="Copy", text2="Copied"):
        def change_text():
            button.config(text=text1)

        button.config(text=text2)
        self.after(time, change_text)


class Generator(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        global password_dictornary

        # generates the grid, if you want to see these, only add True
        PasswordManager.generate_grid(self, 9)

        # vars for the class
        self.length_list = [_ for _ in range(1, 41)]
        self.variable = tk.StringVar(self)
        self.variable.set(self.length_list[15])
        self.get_length = 16

        # changing bg of the frame
        self.config(bg=bg_color)

        # Widgets to show website and username
        tk.Label(self, text="Website: ", bg=bg_color, fg=fg_color).grid(row=0, sticky="w")
        tk.Label(self, text="Username: ", bg=bg_color, fg=fg_color).grid(row=1, sticky="w")
        self.website = tk.Entry(self, bg=bg_color, fg=fg_color)
        self.website.config(highlightbackground=bg_color_entry, highlightcolor=bg_color_entry)
        self.website.insert(0, "www.example.com")
        self.website.grid(row=0, column=1)
        self.username = tk.Entry(self, bg=bg_color, fg=fg_color)
        self.username.config(highlightbackground=bg_color_entry, highlightcolor=bg_color_entry)
        self.username.insert(0, "example_username")
        self.username.grid(row=1, column=1)

        # option menu
        self.length = tk.OptionMenu(self, self.variable, *self.length_list)
        self.length.config(highlightbackground=bg_color_entry, highlightcolor=bg_color_entry)
        self.length.config(bg=bg_color, fg=fg_color)
        self.length["menu"].config(bg=bg_color, fg=fg_color)
        self.length.config(widt=3)
        self.length.grid(row=2, column=3, sticky="w")
        self.variable.trace("w", self.callback)

        # Widgets to show/generate passwords
        tk.Label(self, text="Your password: ", bg=bg_color, fg=fg_color).grid(row=2, sticky="w")
        var1 = tk.OptionMenu(self, self.variable, *self.length_list)

        tk.Label(self, text="Length:", bg=bg_color, fg=fg_color).grid(row=2, column=2)

        self.password = pg.create_password(int(self.get_length))
        self.pass_text = tk.Entry(self, bg=bg_color, fg=fg_color)
        self.pass_text.config(highlightbackground=bg_color_entry, highlightcolor=bg_color_entry)
        self.pass_text.insert(0, self.password)
        self.pass_text.grid(row=2, column=1)

        # Buttons
        tkm.Button(self, text="Generate new password",
                   command=lambda: self.generate_new_password(int(self.get_length)),
                   bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover).grid(row=3,
                                                        sticky="E")
        tkm.Button(self, text="Submit", command=lambda: self.submit(), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover).grid(row=3, column=1, )
        tkm.Button(self, text="Delete", command=lambda: self.website.delete(0, "end"), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover).grid(row=0, column=2, )
        tkm.Button(self, text="Delete", command=lambda: self.username.delete(0, "end"), bg=bg_button_passive,
                   fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
                   overbackground=bg_button_hover).grid(row=1, column=2, )

        exit_button(self)
        back_button(self, root)

    def generate_new_password(self, length):
        self.password = pg.create_password(length)
        self.pass_text.delete(0, "end")
        self.pass_text.insert(0, self.password)

    def submit(self):
        global password_dictornary
        pg.save_pass(password_dictornary, self.website.get(), self.pass_text.get(), self.username.get())
        n = 0
        self.website.delete(0, "end")
        for name in password_dictornary:
            n += 1
            print(
                f"Website_{n}: {name}\nUsername: {password_dictornary[name][0]}\nPassword: {password_dictornary[name][1]}\n")

    def callback(self, *args):
        self.get_length = self.variable.get()
        self.generate_new_password(int(self.get_length))


class Labels(tk.Label):
    def __init__(self, window, text: str, row: int = None, column: int = None, rowspan: int = 1, columnspan: int = 1,
                 height: int = None, width: int = None):
        super(Labels, self).__init__(window)

        self.tk.Label = tk.Label(window, height=height, width=width, text=text)
        self.tk.Label.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

    def change_label_text(self, new_text: str):
        self.tk.Label.configure(text=new_text)

    def change_label_font(self, font_name: str, size: int):
        self.tk.Label.config(font=(font_name, size))


# ---------
# FUNCTIONS
# ---------
def get_entered_text(TextBox):
    global entered_text
    # entered_text = TextBox.get("0.1", "end-1c") >>> only for Textfields
    entered_text = TextBox.get()
    TextBox.delete(0, "end")
    print(entered_text)
    return entered_text


def show_grid(root, number):
    for r in range(number):
        for c in range(number):
            tkm.Button(root, text="size").grid(row=r, column=c, sticky="nsew")


def exit_button(root, text="Exit", row=8, column=8, sticky="nw"):
    tkm.Button(root, text=text, command=lambda: root.quit(), bg=bg_button_passive,
               fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
               overbackground=bg_button_hover).grid(row=row, column=column, sticky=sticky)


def back_button(self, root, text="Back to menu", row=8, column=0):
    tkm.Button(self, text=text, command=lambda: root.show_title(), bg=bg_button_passive,
               fg=fg_button_passive, activebackground=bg_button_active, borderless=True,
               overbackground=bg_button_hover).grid(row=row, column=column, padx=25, sticky="n")


def header(self, text="Passwordmanager by Wotan", row=0, column=4, font_size=20, sticky=None, padx=0):
    tk.Label(self, text=text, font=("Arial underlined", font_size, "underline"), bg=bg_color, fg=fg_color).grid(row=row,
                                                                                                                column=column,
                                                                                                                columnspan=6,
                                                                                                                padx=padx,
                                                                                                                sticky=sticky)


# function to copy text to the clipboard
def copy_to_clipboard(root, widget):
    root.clipboard_clear()
    root.clipboard_append(widget["text"])


# saving old passwords (file isn't save yet, cause it will be saved as normal text (maybe use decrypting program))

def save_old():
    save_pass = {}

    # encodes the data
    for website in password_dictornary:
        save_pass[website] = [ed.encoding(password_dictornary[website][0]),
                              ed.encoding(password_dictornary[website][1])]
    passwords_file = open("passwords", "wt")
    passwords_file.write(str(save_pass))
    passwords_file.close()
    print(save_pass)


def read_file():
    global password_dictornary
    file = open("passwords", "r")

    contents = file.read()
    password_dictornary = ast.literal_eval(contents)
    file.close()
    # decodes the data
    for website in password_dictornary:
        password_dictornary[website] = [ed.decoding(password_dictornary[website][0]),
                                        ed.decoding(password_dictornary[website][1])]
    print(password_dictornary)


if __name__ == '__main__':
    read_file()

    App = PasswordManager()

    App.mainloop()

    save_old()
