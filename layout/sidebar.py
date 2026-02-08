import ttkbootstrap as ttk
from ttkbootstrap_icons_bs import BootstrapIcon

def build_sidebar(parent):
  sidebar = ttk.Frame(parent, padding=10)
  sidebar.pack(side="left", fill="y")

  ttk.Label(sidebar, text="Layer:", font="-size 12").pack(anchor="w")

  layer_var = ttk.StringVar()
  ttk.Entry(sidebar, textvariable=layer_var, width=20).pack(pady=5)

  buttons = [
    ("Change Layer", "layers"),
    ("Circle", "circle"),
    ("Line", "dash"),
    ("Point", "dot")
  ]

  for text, icon_name in buttons:
    icon = BootstrapIcon(icon_name, size=16)
    btn = ttk.Button(
      sidebar,
      text=text,
      image=icon,
      compound="left",
      bootstyle="primary"
    )
    btn.image = icon
    btn.pack(fill="x", pady=5)
