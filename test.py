import ttkbootstrap_icons_bs 
import inspect 
print(ttkbootstrap_icons_bs.__file__) 
print(dir(ttkbootstrap_icons_bs))


import ttkbootstrap as tb
from ttkbootstrap_icons_bs import BootstrapIcon

app = tb.Window()
icon = BootstrapIcon("mic-mute-fill", size=64)
toggle = tb.Checkbutton(app, compound="image", bootstyle="toolbutton")
toggle.pack(padx=20, pady=20)

# Icon automatically switches to mic-fill when selected
icon.map(toggle, statespec=[("selected", {"name": "mic-fill"})])

app.mainloop()