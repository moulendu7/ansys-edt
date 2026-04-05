def create_ground(oEditor):
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "-0.4mm",
            "YStart:=", "0.3mm",
            "ZStart:=", "0mm",
            "Width:=", "0.9mm",
            "Height:=", "-0.6mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "Rectangle1",
            "MaterialValue:=", "\"vacuum\"",
            "SolveInside:=", True
        ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            ["NAME:PropServers", "Rectangle1"],
            ["NAME:ChangedProps",
             ["NAME:Name", "Value:=", "ground"],
             ["NAME:Color", "R:=", 255, "G:=", 128, "B:=", 0]
             ]
        ]
    ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            ["NAME:PropServers", "ground:CreateRectangle:1"],
            ["NAME:ChangedProps",
             ["NAME:Position", "X:=", "-30mm", "Y:=", "-30mm", "Z:=", "0mm"],
             ["NAME:XSize", "Value:=", "60mm"],
             ["NAME:YSize", "Value:=", "60mm"]
             ]
        ]
    ])