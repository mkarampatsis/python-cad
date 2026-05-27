import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# -------------------------------------------------
# MAIN WINDOW
# -------------------------------------------------
app = tb.Window(themename="superhero")
app.title("TkBootstrap Desktop App")
app.geometry("1200x700")

# -------------------------------------------------
# CUSTOM COLORS
# -------------------------------------------------
CANVAS_BG = "#1b222c"
FOOTER_BG = "#0f1318"

CANVAS_TEXT = "#ffffff"
FOOTER_TEXT = "#00d4ff"

# -------------------------------------------------
# NAVBAR / MENU
# -------------------------------------------------
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

# Add dropdowns
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)

app.config(menu=menubar)

# -------------------------------------------------
# MAIN LAYOUT CONTAINER
# -------------------------------------------------
main_container = tb.Frame(app)
main_container.pack(fill=BOTH, expand=True)

# Configure grid
main_container.columnconfigure(0, weight=1)   # sidebar
main_container.columnconfigure(1, weight=4)   # canvas
main_container.rowconfigure(0, weight=1)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
sidebar = tb.Frame(main_container, bootstyle="dark")
sidebar.grid(row=0, column=0, sticky="nswe")

sidebar_title = tb.Label(
    sidebar,
    text="Sidebar",
    font=("Segoe UI", 16, "bold")
)
sidebar_title.pack(pady=20)

tb.Button(sidebar, text="Dashboard", bootstyle="primary").pack(
    fill=X, padx=10, pady=5
)

tb.Button(sidebar, text="Projects", bootstyle="info").pack(
    fill=X, padx=10, pady=5
)

tb.Button(sidebar, text="Settings", bootstyle="warning").pack(
    fill=X, padx=10, pady=5
)

# -------------------------------------------------
# CANVAS AREA
# -------------------------------------------------
canvas_frame = tb.Frame(
    main_container,
    style="Canvas.TFrame"
)
canvas_frame.grid(row=0, column=1, sticky="nswe")

canvas_title = tb.Label(
    canvas_frame,
    text="Main Canvas Area",
    style="Canvas.TLabel"
)
canvas_title.pack(pady=20)

# Example canvas
canvas = tk.Canvas(
    canvas_frame,
    bg=CANVAS_BG,
    highlightthickness=0
)
canvas.pack(fill=BOTH, expand=True, padx=20, pady=20)

canvas.create_text(
    200,
    100,
    text="Your Drawing Area",
    fill=CANVAS_TEXT,
    font=("Segoe UI", 24, "bold")
)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
footer = tb.Frame(app, style="Footer.TFrame", height=40)
footer.pack(fill=X, side=BOTTOM)

footer_label = tb.Label(
    footer,
    text="Status: Ready",
    style="Footer.TLabel"
)
footer_label.pack(side=RIGHT, padx=20, pady=8)

# -------------------------------------------------
# CUSTOM STYLES
# -------------------------------------------------
style = tb.Style()

# Canvas styles
style.configure(
    "Canvas.TFrame",
    background=CANVAS_BG
)

style.configure(
    "Canvas.TLabel",
    background=CANVAS_BG,
    foreground=CANVAS_TEXT,
    font=("Segoe UI", 22, "bold")
)

# Footer styles
style.configure(
    "Footer.TFrame",
    background=FOOTER_BG
)

style.configure(
    "Footer.TLabel",
    background=FOOTER_BG,
    foreground=FOOTER_TEXT,
    font=("Consolas", 11, "bold")
)

# -------------------------------------------------
# RUN
# -------------------------------------------------
app.mainloop()