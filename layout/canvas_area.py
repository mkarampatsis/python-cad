import tkinter as tk
import ttkbootstrap as ttk

def build_canvas_area(parent):
  frame = ttk.Frame(parent)
  frame.pack(side="left", fill="both", expand=True)

  canvas = tk.Canvas(frame, bg="#d3d3d3")
  canvas.pack(fill="both", expand=True)