import tkinter as tk
import ttkbootstrap as tb

from ttkbootstrap.constants import *


# =========================================================
# WINDOW
# =========================================================
app = tb.Window(themename="superhero")

app.title("TkBootstrap Layout")
app.geometry("1200x700")


# =========================================================
# COLORS
# =========================================================
MAIN_BG = "#df1e42"
FOOTER_BG = "#11151c"

MAIN_TEXT = "#ffffff"
FOOTER_TEXT = "#00d4ff"


# =========================================================
# STYLE
# =========================================================
style = tb.Style()

# IMPORTANT:
# Avoid names containing:
# Canvas, Button, Label, Frame, etc
# at the START of the style name.

style.configure(
    "MainArea.TFrame",
    background=MAIN_BG
)

style.configure(
    "MainArea.TLabel",
    background=MAIN_BG,
    foreground=MAIN_TEXT,
    font=("Segoe UI", 22, "bold")
)

style.configure(
    "Statusbar.TFrame",
    background=FOOTER_BG
)

style.configure(
    "Statusbar.TLabel",
    background=FOOTER_BG,
    foreground=FOOTER_TEXT,
    font=("Consolas", 11, "bold")
)


# =========================================================
# MENU BAR
# =========================================================
menubar = tk.Menu(app)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)

edit_menu.add_command(label="Settings")
edit_menu.add_command(label="Preferences")

# Add menus
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

app.config(menu=menubar)


# =========================================================
# MAIN LAYOUT
# =========================================================
main_container = tb.Frame(app)

main_container.pack(
    fill=BOTH,
    expand=True
)

# Grid configuration
main_container.columnconfigure(0, weight=1)
main_container.columnconfigure(1, weight=4)
main_container.rowconfigure(0, weight=1)


# =========================================================
# SIDEBAR
# =========================================================
sidebar = tb.Frame(
    main_container,
    bootstyle="dark"
)

sidebar.grid(
    row=0,
    column=0,
    sticky="nswe"
)

sidebar_title = tb.Label(
    sidebar,
    text="Sidebar",
    font=("Segoe UI", 16, "bold")
)

sidebar_title.pack(pady=20)

tb.Button(
    sidebar,
    text="Dashboard",
    bootstyle="primary"
).pack(fill=X, padx=10, pady=5)

tb.Button(
    sidebar,
    text="Projects",
    bootstyle="info"
).pack(fill=X, padx=10, pady=5)

tb.Button(
    sidebar,
    text="Settings",
    bootstyle="warning"
).pack(fill=X, padx=10, pady=5)


# =========================================================
# RIGHT CONTENT AREA
# =========================================================
main_area = tb.Frame(
    main_container,
    style="MainArea.TFrame"
)

main_area.grid(
    row=0,
    column=1,
    sticky="nswe"
)

main_title = tb.Label(
    main_area,
    text="Main Drawing Area",
    style="MainArea.TLabel"
)

main_title.pack(pady=20)


# =========================================================
# TK CANVAS
# =========================================================
drawing_canvas = tk.Canvas(
    main_area,
    bg=MAIN_BG,
    highlightthickness=0
)

drawing_canvas.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)

drawing_canvas.create_text(
    250,
    120,
    text="CAD / Drawing Canvas",
    fill=MAIN_TEXT,
    font=("Segoe UI", 24, "bold")
)


# =========================================================
# FOOTER
# =========================================================
footer = tb.Frame(
    app,
    style="Statusbar.TFrame",
    height=40
)

footer.pack(
    side=BOTTOM,
    fill=X
)

footer_label = tb.Label(
    footer,
    text="Status: Ready",
    style="Statusbar.TLabel"
)

footer_label.pack(
    side=RIGHT,
    padx=20,
    pady=8
)


# =========================================================
# START
# =========================================================
app.mainloop()