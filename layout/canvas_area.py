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

  canvas = tk.Canvas(
    frame,
    background=colors.secondary,
    # DEFAULT BORDER
    bd=2,
    relief="solid",
    # BORDER SIZE
    highlightthickness=1,
    # BORDER COLOR
    highlightbackground="#444444",
    # FOCUS COLOR
    highlightcolor="#00d4ff"
  )

  canvas.pack(
    fill="both", 
    expand=True,
    padx=20,
    pady=(20,0)    
  )
  
  canvas.focus_set()