import ttkbootstrap as ttk

def build_footer(parent):
  # footer = ttk.Frame(parent, padding=5)
  # footer.pack(fill="x")
  footer = ttk.Frame(parent, padding=5) 
  footer.pack(side="bottom", fill="x")

  ttk.Label(footer, text="Command:", font="-size 11").pack(anchor="w")

  text = ttk.Text(footer, height=3)  # multi-line
  text.pack(fill="x", expand=True)
