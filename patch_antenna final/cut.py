def create_cut(oEditor):
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "4mm",
            "YStart:=", "-4mm",
            "ZStart:=", "0mm",
            "Width:=", "10mm",
            "Height:=", "8mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "Rectangle1"
        ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            ["NAME:PropServers", "Rectangle1"],
            ["NAME:ChangedProps",
             ["NAME:Name", "Value:=", "cut"]
             ]
        ]
    ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            ["NAME:PropServers", "cut:CreateRectangle:1"],
            ["NAME:ChangedProps",
             ["NAME:Position", "X:=", "14.7mm", "Y:=", "-2.5mm", "Z:=", "1.6mm"],
             ["NAME:XSize", "Value:=", "-9.5mm"],
             ["NAME:YSize", "Value:=", "5mm"]
             ]
        ]
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