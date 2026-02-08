import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap_icons_bs import BootstrapIcon

def set_min_width(menu, chars): 
  menu.update_idletasks() 
  menu.config(width=chars)

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

  # Override menu colors
  root.option_add("*Menu.background", "#e0e0e0")
  root.option_add("*Menu.foreground", "black")
  root.option_add("*Menu.activeBackground", "#c8c8c8")
  root.option_add("*Menu.activeForeground", "black")
  root.option_add("*Menu.relief", "flat")

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
      file_menu = tk.Menu(mb, tearoff=0)
      file_menu.add_command(label="New", command = None) 
      file_menu.add_command(label="Open", command = None) 
      file_menu.add_separator() 
      file_menu.add_command(label="Exit", command = root.destroy)
      # Force minimum width 
      # file_menu.config(postcommand=lambda m=file_menu: set_min_width(m, 50))
      file_menu.config(width=50)
      mb["menu"] = file_menu
    else:
      menu = tk.Menu(mb, tearoff=0)
      menu.add_command(label=f"{label} Option 1")
      menu.add_command(label=f"{label} Option 2")
      menu.add_separator()
      menu.add_command(label=f"{label} Settings")

      mb["menu"] = menu
