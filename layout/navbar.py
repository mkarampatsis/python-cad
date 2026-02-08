import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap_icons_bs import BootstrapIcon

def add_item(menu, label, cmd=None): 
  menu.add_command( 
    label=label, 
    command=cmd, 
    background="#e0e0e0", 
    foreground="black", 
    activebackground="#c8c8c8", 
    activeforeground="black" 
  )

def build_navbar(root):
  navbar = ttk.Frame(root, padding=5)
  # navbar.pack(fill="x")
  navbar.pack(side="top", fill="x")

  style = ttk.Style()
  style.configure("Navbar.TFrame", background="#d35400")
  style.configure(
    "Navbar.TMenubutton",
    background="#d35400",
    foreground="white",
    padding=(2, 10),
    font="-size 11"
  )
  navbar.configure(style="Navbar.TFrame")

  menu_items = [
    ("File", "folder-check"),
    ("Edit", "credit-card-2-back"),
    ("View", "eye"),
    ("Image Format", "file-earmark-image"),
    ("Format", "filetype-css"),
    ("Tools", "wrench-adjustable"),
    ("Draw", "pencil"),
    ("Engineering", "gear"),
    ("Photogrammetry", "camera-video"),
    ("Modify", "wrench-adjustable-circle"),
    ("Research", "search"),
    ("Developer", "file-code"),
    ("Window", "layout-text-window-reverse"),
    ("Help", "question-circle")
  ]

  for label, icon_name in menu_items:
    icon = BootstrapIcon(icon_name, size=20, color="#ffffff")

    mb = ttk.Menubutton(
      navbar,
      text=label,
      image=icon,
      compound="left",
      style="Navbar.TMenubutton"
    )
    mb.image = icon
    mb.pack(side="left", padx=2)

    match label:
      case 'File':
        file_menu = tk.Menu(mb,tearoff=0)
        add_item(file_menu, "New", None) 
        add_item(file_menu, "Open", None) 
        add_item(file_menu, "Open without images", None) 
        add_item(file_menu, "Save", None) 
        add_item(file_menu, "Save as", None) 
        add_item(file_menu, "Close", None) 
        file_menu.add_separator(background="#e0e0e0") 
        add_item(file_menu, "Insert", None) 
        add_item(file_menu, "Export Image", None) 
        add_item(file_menu, "Plot to PDF", None) 
        add_item(file_menu, "Plot", None) 
        add_item(file_menu, "Purge", None) 
        file_menu.add_separator(background="#e0e0e0") 
        add_item(file_menu, "Exit", root.destroy) 
        mb["menu"] = file_menu
      case "Edit":
        edit_menu = tk.Menu(mb, tearoff=0)
        add_item(edit_menu, "Undo", None)
        add_item(edit_menu, "Redo", None)
        edit_menu.add_separator(background="#e0e0e0")
        add_item(edit_menu, "Cut", None)
        add_item(edit_menu, "Copy", None)
        add_item(edit_menu, "Copy with Base Point", None)
        add_item(edit_menu, "Paste", None)
        add_item(edit_menu, "Paste to Original Coordinates", None)
        edit_menu.add_separator(background="#e0e0e0")
        add_item(edit_menu, "Select elements", None)
        add_item(edit_menu, "Background colour", None)
        mb["menu"] = edit_menu
      case "View":
        view_menu = tk.Menu(mb, tearoff=0)
        add_item(view_menu, "Zoom Window", None)
        add_item(view_menu, "Zoom All", None)
        add_item(view_menu, "Zoom Selection", None)
        add_item(view_menu, "Zoom Relative", None)
        add_item(view_menu, "Zoom Real Time", None)
        view_menu.add_separator(background="#e0e0e0")
        add_item(view_menu, "Pan Relative", None)
        add_item(view_menu, "Pan Real Time", None)
        view_menu.add_separator(background="#e0e0e0")
        add_item(view_menu, "Redraw", None)
        add_item(view_menu, "Regen", None)
        mb["menu"] = view_menu        
      case "Image Format":
        img_menu = tk.Menu(mb, tearoff=0)
        add_item(img_menu, "Insert Raster Image", None)
        add_item(img_menu, "Import GeoTIFF", None)
        add_item(img_menu, "Import tfw Image", None)
        add_item(img_menu, "Import log Image", None)
        add_item(img_menu, "Import Cadastre", None)
        add_item(img_menu, "Import tiled Image", None)
        add_item(img_menu, "Scan Image", None)
        add_item(img_menu, "Image frame", None)
        img_menu.add_separator(background="#e0e0e0")
        add_item(img_menu, "Unload images", None)
        add_item(img_menu, "Locate image file", None)
        add_item(img_menu, "Locate image directory", None)
        add_item(img_menu, "Embed images", None)
        img_menu.add_separator(background="#e0e0e0")
        add_item(img_menu, "Clip image", None)
        add_item(img_menu, "Image &Render", None)
        mb["menu"] = img_menu
      case "Format":
        format_menu = tk.Menu(mb, tearoff=0)
        add_item(format_menu, "Layer", None)        
        add_item(format_menu, "Text Style", None)
        add_item(format_menu, "Units", None)
        mb["menu"] = format_menu
      case "Tools":   
        tools_menu = tk.Menu(mb, tearoff=0)
        add_item(tools_menu, "Distance", None)        
        add_item(tools_menu, "Area", None)
        add_item(tools_menu, "Angle", None)
        add_item(tools_menu, "Id Point", None)
        add_item(tools_menu, "List", None)
        add_item(tools_menu, "Elevation", None)
        add_item(tools_menu, "Elevation (higher imensions)", None)
        add_item(tools_menu, "Drafting Settings", None)
        add_item(tools_menu, "Find text", None)
        add_item(tools_menu, "Find centroid", None)
        add_item(tools_menu, "Find convex hull", None)
        add_item(tools_menu, "Simplify line", None)
        add_item(tools_menu, "Interpolate line", None)
        add_item(tools_menu, "Run script", None)
        mb["menu"] = tools_menu
      case "Draw":
        draw_menu = tk.Menu(mb, tearoff=0)
        add_item(draw_menu, "Line", None)
        add_item(draw_menu, "Rectangle", None)           
        add_item(draw_menu, "Polygon", None)
        add_item(draw_menu, "Circle", None)
        add_item(draw_menu, "Arc", None)
        add_item(draw_menu, "Ellipse", None)       
        add_item(draw_menu, "Point", None)
        add_item(draw_menu, "Text", None)
        add_item(draw_menu, "Spline", None)
        add_item(draw_menu, "Named Point", None)
        add_item(draw_menu, "Hatch Open", None)
        draw_menu.add_separator(background="#e0e0e0")
        add_item(draw_menu, "Dimension aligned", None)
        add_item(draw_menu, "To spline", None)
        add_item(draw_menu, "To curve", None)
        add_item(draw_menu, "Decurve", None)
        mb["menu"] = draw_menu
      case "Engineering":
        eng_menu = tk.Menu(mb, tearoff=0)
        add_item(eng_menu, "Structural Analysis", None)
        add_item(eng_menu, "Finite Element Analysis", None)   
        add_item(eng_menu, "Thermal Analysis", None)
        add_item(eng_menu, "Fluid Dynamics", None)
        add_item(eng_menu, "Material Properties", None)             
        mb["menu"] = eng_menu 
      case "Photogrammetry":
        photo_menu = tk.Menu(mb, tearoff=0)       
        add_item(photo_menu, "Image Alignment", None)         
        add_item(photo_menu, "Dense Point Cloud", None)
        add_item(photo_menu, "Mesh Generation", None)
        add_item(photo_menu, "Texture Mapping", None)
        add_item(photo_menu, "Orthophoto Generation", None)
        mb["menu"] = photo_menu
      case "Modify":
        modify_menu = tk.Menu(mb, tearoff=0)
        add_item(modify_menu, "Move", None)
        add_item(modify_menu, "Copy", None)
        add_item(modify_menu, "Rotate", None)
        add_item(modify_menu, "Scale", None)
        add_item(modify_menu, "Mirror", None)     
        add_item(modify_menu, "Trim", None)
        add_item(modify_menu, "Extend", None)         
        add_item(modify_menu, "Offset", None)           

        mb["menu"] = modify_menu
      case "Research":
        research_menu = tk.Menu(mb, tearoff=0)
        add_item(research_menu, "CAD Research Papers", None)
        add_item(research_menu, "CAD Datasets", None)
        add_item(research_menu, "CAD Tutorials", None)
        add_item(research_menu, "CAD Tools", None)      
        add_item(research_menu, "CAD Communities", None)
        mb["menu"] = research_menu        
      case "Developer":
        dev_menu = tk.Menu(mb, tearoff=0)
        add_item(dev_menu, "API Documentation", None)
        add_item(dev_menu, "Developer Tools", None)                     
        add_item(dev_menu, "Source Code", None)
        add_item(dev_menu, "Report a Bug", None)
        add_item(dev_menu, "Request a Feature", None)
        mb["menu"] = dev_menu     
      case "Window":
        window_menu = tk.Menu(mb, tearoff=0)
        add_item(window_menu, "Cascade", None)      
        add_item(window_menu, "Tile Horizontally", None)
        add_item(window_menu, "Tile Vertically", None)
        add_item(window_menu, "Arrange Icons", None)
        mb["menu"] = window_menu    
      case "Help":
        help_menu = tk.Menu(mb, tearoff=0)
        add_item(help_menu, "User Guide", None)
        add_item(help_menu, "Tutorials", None)
        add_item(help_menu, "FAQs", None)         
        add_item(help_menu, "Contact Support", None)
        add_item(help_menu, "About", None)
        mb["menu"] = help_menu