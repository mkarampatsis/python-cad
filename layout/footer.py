import ttkbootstrap as ttk
import tkinter as tk

def build_footer(parent):
  footer = ttk.Frame(parent, padding=5) 
  footer.pack(side="bottom", fill="x")

  style = ttk.Style()
  colors = style.colors

  ttk.Label(footer, text="Command:", font="-size 11").pack(anchor="w")

  text = ttk.Text(footer, height=5)  # multi-line
  text.pack(fill="x", expand=True)
  text.configure(
    background=colors.light, 
    foreground="white", 
    font="-size 11"
  )