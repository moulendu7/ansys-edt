def create_patch(oEditor):

    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "-14.7mm",
            "YStart:=", "-19mm",
            "ZStart:=", "1.6mm",
            "Width:=", "29.4mm",
            "Height:=", "38mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "patch"
        ])

    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "0mm",
            "YStart:=", "-1.5mm",
            "ZStart:=", "1.6mm",
            "Width:=", "30mm",
            "Height:=", "3mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "feed"
        ])

    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "14.7mm",
            "YStart:=", "-2.5mm",
            "ZStart:=", "1.6mm",
            "Width:=", "-9.5mm",
            "Height:=", "5mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "cut"
        ])

    oEditor.Subtract(
        [
            "NAME:Selections",
            "Blank Parts:=", "patch",
            "Tool Parts:=", "cut"
        ],
        [
            "NAME:SubtractParameters",
            "KeepOriginals:=", False
        ])

    oEditor.Unite(
        [
            "NAME:Selections",
            "Selections:=", "patch,feed"
        ],
        [
            "NAME:UniteParameters",
            "KeepOriginals:=", False
        ])