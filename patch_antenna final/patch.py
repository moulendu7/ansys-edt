def create_patch(oEditor):
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "-16mm",
            "YStart:=", "12mm",
            "ZStart:=", "0mm",
            "Width:=", "32mm",
            "Height:=", "-22mm",
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "Rectangle1",
            "MaterialValue:=", "\"vacuum\""
        ])


    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            ["NAME:PropServers", "Rectangle1"],
            ["NAME:ChangedProps",
             ["NAME:Name", "Value:=", "patch"]
             ]
        ]
    ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            ["NAME:PropServers", "patch:CreateRectangle:1"],
            ["NAME:ChangedProps",
             ["NAME:Position", "X:=", "(-29.4/2) mm", "Y:=", "(-38/2) mm", "Z:=", "1.6mm"],
             ["NAME:XSize", "Value:=", "29.4mm"],
             ["NAME:YSize", "Value:=", "38mm"]
             ]
        ]
    ])