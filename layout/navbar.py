import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap_icons_bs import BootstrapIcon

def add_item(menu, label, cmd=None): 
  menu.add_command( 
    label=label, 
    command=cmd, 
    background="red", 
    foreground="black", 
    activebackground="#c8c8c8", 
    activeforeground="black" 
  )

def build_navbar(root):
  navbar = ttk.Frame(root, padding=5)
  # navbar.pack(fill="x")
  navbar.pack(side="top", fill="x")

  style = ttk.Style()
  style.configure("Navbar.TFrame", background="#d35400")
  style.configure(
    "Navbar.TMenubutton",
    background="#d35400",
    foreground="white",
    padding=(2, 10),
    font="-size 11"
  )
  navbar.configure(style="Navbar.TFrame")

  menu_items = [
    ("File", "folder-check"),
    ("Edit", "credit-card-2-back"),
    ("View", "eye"),
    ("Image Format", "file-earmark-image"),
    ("Tools", "wrench-adjustable"),
    ("Draw", "pencil"),
    ("Engineering", "gear"),
    ("Photogrammetry", "camera-video"),
    ("Modify", "wrench-adjustable-circle"),
    ("Research", "search"),
    ("Developer", "file-code"),
    ("Window", "layout-text-window-reverse"),
    ("Help", "question-circle")
  ]

  for label, icon_name in menu_items:
    icon = BootstrapIcon(icon_name, size=20, color="#ffffff")

    mb = ttk.Menubutton(
      navbar,
      text=label,
      image=icon,
      compound="left",
      style="Navbar.TMenubutton"
    )
    mb.image = icon
    mb.pack(side="left", padx=2)

    if label == "File":
      file_menu = tk.Menu(
        mb, 
        tearoff=0,
        bg="red", 
        fg="black", 
        activebackground="#c8c8c8", 
        activeforeground="black", 
        borderwidth=0
      )
      add_item(file_menu, "New") 
      add_item(file_menu, "Open") 
      add_item(file_menu, "Open without images") 
      add_item(file_menu, "Save") 
      add_item(file_menu, "Save as") 
      add_item(file_menu, "Close") 
      file_menu.add_separator() 
      add_item(file_menu, "Insert") 
      add_item(file_menu, "Export Image") 
      add_item(file_menu, "Plot to PDF") 
      add_item(file_menu, "Plot") 
      add_item(file_menu, "Purge") 
      file_menu.add_separator() 
      add_item(file_menu, "Exit", root.destroy) 
      mb["menu"] = file_menu
     
      # file_menu.add_command(label="New", command = None) 
      # file_menu.add_command(label="Open", command = None)
      # file_menu.add_command(label="Open without images", command = None)
      # file_menu.add_command(label="Save", command = None)
      # file_menu.add_command(label="Save as", command = None)
      # file_menu.add_command(label="Close", command = None)
      # file_menu.add_separator() 
      # file_menu.add_command(label="Insert", command = None)
      # file_menu.add_command(label="Export Image", command = None)
      # file_menu.add_command(label="Plot to PDF", command = None) 
      # file_menu.add_command(label="Plot", command = None) 
      # file_menu.add_command(label="Purge", command = None) 
      # file_menu.add_separator() 
      # file_menu.add_command(label="Exit", command = root.destroy)
      # mb["menu"] = file_menu
    elif label == "Edit":
      edit_menu = tk.Menu(mb, tearoff=0)
      edit_menu.add_command(label="Undo", command = None)
      edit_menu.add_command(label="Redo", command = None)
      edit_menu.add_separator()
      edit_menu.add_command(label="Cut", command = None)
      edit_menu.add_command(label="Copy", command = None)
      edit_menu.add_command(label="Copy with Base Point", command = None)
      edit_menu.add_command(label="Paste", command = None)
      edit_menu.add_command(label="Paste to Original Coordinates", command = None)
      edit_menu.add_separator()
      edit_menu.add_command(label="Select elements", command = None)
      edit_menu.add_command(label="Background colour", command = None)
      mb["menu"] = edit_menu
    else:
      menu = tk.Menu(mb, tearoff=0)
      menu.add_command(label=f"{label} Option 1")
      menu.add_command(label=f"{label} Option 2")
      menu.add_separator()
      menu.add_command(label=f"{label} Settings")

      mb["menu"] = menu
