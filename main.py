import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from layout.navbar import build_navbar
from layout.sidebar import build_sidebar
from layout.canvas_area import build_canvas_area
from layout.footer import build_footer

class CADApp:
  def __init__(self):
    self.root = ttk.Window(
      title="Engineering CAD",
      themename="superhero",
      size=(1570, 900)
    )

    # NAVBAR (top) 
    build_navbar(self.root) 
    
    # MAIN BODY (middle) 
    self.main = ttk.Frame(self.root) 
    self.main.pack(fill=BOTH, expand=True) 
    self.build_body() 
    
    # FOOTER (bottom) 
    build_footer(self.root) 
    
    self.root.mainloop()

  def build_body(self):
    body = ttk.Frame(self.main)
    body.pack(fill=BOTH, expand=True)

    # Left sidebar
    build_sidebar(body)

    # Canvas area
    build_canvas_area(body)

if __name__ == "__main__":
  CADApp()
