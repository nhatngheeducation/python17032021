
def setWidgetCenter(root, width, height):
    """Canh giua man hinh"""
    root.geometry(f"{width}x{height}")  # widthxheight
    paddingWidth = int((root.winfo_screenwidth() - width) / 2)
    paddingHeight = int((root.winfo_screenheight() - height) / 2)
    root.geometry("+{}+{}".format(paddingWidth, paddingHeight))