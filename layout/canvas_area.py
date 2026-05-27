import tkinter as tk
import ttkbootstrap as ttk

def build_canvas_area(parent):
  frame = ttk.Frame(parent)
  frame.pack(side="right", fill="both", expand=True)

  canvas_title = ttk.Label(
    frame,
    text="Main Drawing Area",
    # style="MainArea.TLabel"
  )

  canvas_title.pack(pady=(10, 0))
  
  style = ttk.Style()
  colors = style.colors

  # style.configure("Footer.Text", background="#d35400")
  # style.configure(
  #   "Footer.TMenubutton",
  #   background="#d35400",
  #   foreground="white",
  #   padding=(2, 10),
  #   font="-size 11"
  # )
  # footer.configure(style="Footer.TText")

  canvas = tk.Canvas(frame)
  canvas.pack(
    fill="both", 
    expand=True,
    padx=20,
    pady=20   
  )
  
  canvas.configure(
    background=colors.light, 
  )