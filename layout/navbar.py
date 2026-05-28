import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap_icons_bs import BootstrapIcon

# =========================================================
# HELPERS
# =========================================================
def add_item(menu, label, cmd=None): 
  menu.add_command( 
    label=label, 
    command=cmd, 
    background="#e0e0e0", 
    foreground="black", 
    activebackground="#c8c8c8", 
    activeforeground="black"
  )

def create_menu(mb, items):
  """
  Creates a tk.Menu from a list structure.

  Example:
  [
      ("New", callback),
      ("Open", callback),
      "---",
      ("Exit", callback)
  ]
  """

  menu = tk.Menu(mb,tearoff=0)

  for item in items:

    # Separator
    if item == "---":
      menu.add_separator(
        background="#e0e0e0"
      )

    # Normal menu item
    else:
      label, cmd = item

      add_item(
        menu,
        label,
        cmd
      )

  mb["menu"] = menu

# =========================================================
# NAVBAR
# =========================================================
def build_navbar(root):
  navbar = ttk.Frame(root, padding=5)
  navbar.pack(side="top", fill="x")

  # =====================================================
  # STYLE
  # =====================================================
  style = root.style
  colors = style.colors
  
  style.configure("Navbar.TFrame", background=colors.dark)
  style.configure(
    "Navbar.TMenubutton",
    background=colors.primary,
    foreground="white",
    padding=(2, 10),
    font="-size 11"
  )
  navbar.configure(style="Navbar.TFrame")
  
# =====================================================
# CENTER CONTAINER
# =====================================================
  center_frame = ttk.Frame(
    navbar,
    style="Navbar.TFrame"
  )

  center_frame.pack(
    anchor="center"
  )


  # =====================================================
  # MENU DEFINITIONS
  # =====================================================
  menus = {
    "File": {
      "icon": "folder-check",
      "items": [
        ("New", None),
        ("Open", None),
        ("Open without images", None),
        ("Save", None),
        ("Save as", None),
        ("Close", None),
        "---",
        ("Insert", None),
        ("Export Image", None),
        ("Plot to PDF", None),
        ("Plot", None),
        ("Purge", None),
        "---",
        ("Exit", root.destroy)
      ]
    },
    "Edit": {
      "icon": "credit-card-2-back",
      "items": [
        ("Undo", None),
        ("Redo", None),
        "---",
        ("Cut", None),
        ("Copy", None),
        ("Copy with Base Point", None),
        ("Paste", None),
        ("Paste to Original Coordinates", None),
        "---",
        ("Select", None),
        "---",
        ("Background colour", None),
        ("Encoding", None)
      ]
    },

    "View": {
      "icon": "eye",
      "items": [
        ("Zoom Window", None),
        ("Zoom All", None),
        ("Zoom Selection", None),
        ("Zoom Relative", None),
        ("Zoom Real Time", None),
        "---",
        ("Pan Relative", None),
        ("Pan Real Time", None),
        "---",
        ("Redraw", None),
        ("Regen", None)
      ]
    },
    "Image Format": {
      "icon": "file-earmark-image",
      "items": [
        ("Insert Raster Image", None),
        ("Insert GOI Frame", None),
        ("Import GeoTIFF", None),
        ("Import tfw/j2w Image", None),
        ("Import log Image", None),
        ("Import Cadastre", None),
        ("Import tiled Image", None),
        ("Import/convert TerraSAR Image", None),
        ("Scan Image", None),
        ("Image frame", None),
        "---",
        ("Unload images", None),
        ("Load images", None),
        ("Locate image file", None),
        ("Locate image directory", None),
        ("Embed images", None),
        "---",
        ("Clip image", None),
        ("Image Render", None)
      ]
    },
    "Format": {
      "icon": "filetype-css",
      "items": [
        ("Layer", None),
        ("Text Style", None),
        ("Dimension Style", None),
        ("Units", None)
      ]
    },
    "Tools": {
      "icon": "wrench-adjustable",
      "items": [
        ("Distance", None),
        ("Area", None),
        ("Angle", None),
        ("Id Point", None),
        ("List", None),
        ("Elevation", None),
        ("Elevation (higher imensions)", None),
        "---",
        ("Drafting Settings", None),
        ("Find text", None),
        "---",
        ("Find centroid", None),
        ("Find convex hull", None),
        ("Simplify line", None),
        ("Interpolate line", None),
        ("Optimum line", None),
        "---",
        ("Run script", None)
      ]
    },
    "Draw": {
      "icon": "pencil",
      "items": [
        ("Line", None),
        ("Rectangle", None),
        ("Polygon", None),
        ("Circle", None),
        ("Arc", None),
        ("Ellipse", None),
        ("Point", None),
        ("Text", None),
        ("Spline", None),
        "---",
        ("Named Point", None),
        ("Point from dist", None),
        ("Road", None),
        ("Boundary hatch", None),
        ("Hatch Open", None),
        "---",
        ("Dimension aligned", None),
        "---",
        ("To spline", None),
        ("To curve", None),
        ("Decurve", None),
        ("To polygon", None),
        ("BIM - Column", None)
      ]
    },
    "Engineering": {
      "icon": "gear",
      "items": [
        ("Grid", None),
        ("Trace", None),
        ("Fraw Greece", None),
        ("Global points", None),
        ("Export global points", None),
        "---",
        ("Geodetic Projection", None),
        ("Load DEMs", None),
        ("Manage DEMs", None),
        ("Locate DEM directory", None),
        ("Create DTM", None),
        ("DTM/DEM Z", None),
        ("Add Z to Points", None),
        ("Add Z to Lines", None),
        ("Triangulations", None),
        "---",
        ("Quick Profile", None),
        ("Isoclinal", None),
        ("Interchange", None),
        "---",
        ("Bio azimuth", None),             
        ("LOcate roads of slope", None),
        "---",
        ("Stairs", None)
      ]
    },
    "Photogrammetry": {
      "icon": "camera-video",
      "items": [
        ("INTERIOR ORIENTATION (mm)", None),
        ("INTERIOR ORIENTATION (pixels)", None),
        ("Camera management", None),
        "---",
        ("Rotate Image 90 deg counterclockwise", None),
        ("Rotate Image 180 deg", None),
        ("Rotate Image 270 deg counterclockwise", None),
        "---",
        ("Brighten Image (Gray+)", None),
        ("Darken Image (Gray-)", None),
        ("Reset Image brightness", None),
        "---",
        ("Toggle coordinates on/off (F6)", None),
        ("Toggle coordinates system (F7)", None),
        "---",
        ("Model definition", None)
      ]
    },
    "Modify": {
      "icon": "wrench-adjustable-circle",
      "items": [
        ("Erase", None),
        ("Rotate", None),
        ("Scale", None),
        ("Move", None),
        ("Copy", None),
        ("Mirror", None),
        ("Point Mirror", None),
        "---",
        ("Line", None),
        ("Offset", None),
        ("Break", None),
        ("Trim", None),
        ("Extend", None),
        ("Lengthen", None),
        ("Fillet", None),
        ("Explode", None),
        ("Reverse", None),
        ("Edit Text", None),
        ("Edit named Point", None),
        ("Convert to named Point", None),
        "---",
        ("Change layer", None),
        ("Change elevation", None),
        ("Change elevation (higher dim)", None),
        ("Change contour line elevation", None)
      ]
    },
    "Research": {
      "icon": "search",
      "items": [
        ("Mark Region", None),
        ("Edit Region", None),
        "---",
        ("Floor plan", None),
        ("Bio city plan", None),
        ("Show dfr coordinates", None),
        ("Εισαγωγή μετρήσεων θερμοϋγρόμετρου", None),
        "---",
        ("BIM Column Settings", None)
      ]
    },
    "Developer": {
      "icon": "file-code",
      "items": [
        ("Show font", None),
        ("Show dimensions", None),
        ("Save CMD text", None),
        ("Translation report", None),
        ("Show handles", None),
        "---",
        ("Fractal demo", None),
        "---",
        ("Run tests", None)
      ]
    },
    "Developer": {
      "icon": "file-code",
      "items": [
        ("Show font", None),
        ("Show dimensions", None),
        ("Save CMD text", None),
        ("Translation report", None),
        ("Show handles", None),
        "---",
        ("Fractal demo", None),
        "---",
        ("Run tests", None)
      ]
    },
    "Window": {
      "icon": "layout-text-window-reverse",
      "items": [
        ("ThanCad", None)
      ]
    },
    "Help": {
      "icon": "question-circle",
      "items": [
        ("Introduction", None),
        ("GPL", None),
        ("Language", None),
        ("About", None)
      ]
    }
  }
  
  # =====================================================
  # BUILD MENUS
  # =====================================================
  for label, config in menus.items():

    icon = BootstrapIcon(
      config["icon"],
      size=20,
      color="#ffffff"
    )

    mb = ttk.Menubutton(
      center_frame,
      text=label,
      image=icon,
      compound="left",
      style="Navbar.TMenubutton"
    )

    mb.image = icon

    mb.pack(side="left", padx=2)

    create_menu(mb, config["items"])