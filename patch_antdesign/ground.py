def create_ground(oEditor):
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "-30mm",
            "YStart:=", "-30mm",
            "ZStart:=", "0mm",
            "Width:=", "60mm",
            "Height:=", "60mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "ground"
        ])