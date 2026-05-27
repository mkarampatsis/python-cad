import ttkbootstrap as tb


# =========================================================
# COLORS
# =========================================================
MAIN_BG = "#df1e42"
FOOTER_BG = "#11151c"

MAIN_TEXT = "#ffffff"
FOOTER_TEXT = "#00d4ff"


# =========================================================
# STYLE
# =========================================================
style = tb.Style()

# IMPORTANT:
# Avoid names containing:
# Canvas, Button, Label, Frame, etc
# at the START of the style name.

style.configure(
  "MainArea.TFrame",
  background=MAIN_BG
)

style.configure(
  "MainArea.TLabel",
  background=MAIN_BG,
  foreground=MAIN_TEXT,
  font=("Segoe UI", 22, "bold")
)

style.configure(
  "Statusbar.TFrame",
  background=FOOTER_BG
)

style.configure(
  "Statusbar.TLabel",
  background=FOOTER_BG,
  foreground=FOOTER_TEXT,
  font=("Consolas", 11, "bold")
)