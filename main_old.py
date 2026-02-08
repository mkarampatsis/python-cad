import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap_icons_bs import BootstrapIcon

class CADApp:
  def __init__(self):
    self.root = ttk.Window(
      title="Engineering CAD",
      themename="superhero",
      size=(1500, 900)
    )
      

    # store icons to prevent garbage collection
    self.icons = {}

    self.build_navbar()
    # self.build_layout()

    self.root.mainloop()

  # ----------------------------------------------------
  # CUSTOM NAVBAR WITH ICONS
  # ----------------------------------------------------
  def build_navbar(self):
    navbar = ttk.Frame(self.root, padding=5)
    navbar.pack(fill=X)

    # Style for navbar
    style = ttk.Style()
    style.configure("Navbar.TFrame", background="#d35400")
    style.configure(
      "Navbar.TMenubutton",
      background="#d35400",
      foreground="white",
      padding=(2,10),
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
      self.icons[icon_name] = icon  # keep reference
      
      mb = ttk.Menubutton(
        navbar,
        text=label,
        image=icon,
        compound=LEFT,
        style="Navbar.TMenubutton"
      )
      mb.pack(side=LEFT, padx=2)

      menu = tk.Menu( 
        mb, 
        tearoff=0, 
        bg="#e0e0e0", 
        fg="black", 
        activebackground="#c8c8c8", 
        activeforeground="black", 
        borderwidth=0
      )
      menu.add_command(label=f"{label} Option 1")
      menu.add_command(label=f"{label} Option 2")
      menu.add_separator()
      menu.add_command(label=f"{label} Settings")
      mb["menu"] = menu

  # ----------------------------------------------------
  # MAIN LAYOUT
  # ----------------------------------------------------
  def build_layout(self):
    main = ttk.Frame(self.root)
    main.pack(fill=BOTH, expand=True)

    content = ttk.Frame(main)
    content.pack(fill=BOTH, expand=True)

    # -----------------------------
    # LEFT SIDEBAR WITH ICON BUTTONS
    # -----------------------------
    sidebar = ttk.Frame(content, padding=10)
    sidebar.pack(side=LEFT, fill=Y)

    ttk.Label(sidebar, text="Layer:", font="-size 12").pack(anchor=W)
    self.layer_var = tk.StringVar()
    ttk.Entry(sidebar, textvariable=self.layer_var, width=20).pack(pady=5)

    buttons = [
      ("Change Layer", "layers"),
      ("Circle", "circle"),
      ("Line", "minus"),
      ("Point", "dot")
    ]

    for text, icon_name in buttons:
      icon = BootstrapIcon(icon_name, size=16)
      self.icons[icon_name] = icon

      btn = ttk.Button(
        sidebar,
        text=text,
        image=icon,
        compound=LEFT,
        bootstyle=PRIMARY
      )
      btn.pack(fill=X, pady=5)

    # -----------------------------
    # CANVAS AREA (LIGHT GREY)
    # -----------------------------
    canvas_frame = ttk.Frame(content)
    canvas_frame.pack(side=LEFT, fill=BOTH, expand=True)

    self.canvas = tk.Canvas(canvas_frame, bg="#d3d3d3")  # light grey
    self.canvas.pack(fill=BOTH, expand=True)

    # -----------------------------
    # FOOTER COMMAND LINE
    # -----------------------------
    footer = ttk.Frame(main, padding=5)
    footer.pack(fill=X)

    ttk.Label(footer, text="Command:", font="-size 11").pack(side=LEFT)
    self.cmd_var = tk.StringVar()
    ttk.Entry(footer, textvariable=self.cmd_var).pack(
      side=LEFT, fill=X, expand=True, padx=5
    )

    ttk.Button(footer, text="Run", bootstyle=SUCCESS).pack(side=LEFT)


if __name__ == "__main__":
  CADApp()
