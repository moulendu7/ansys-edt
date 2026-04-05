def create_feed(oEditor):
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "0mm",
            "YStart:=", "0mm",
            "ZStart:=", "1.6mm",
            "Width:=", "30mm",
            "Height:=", "-4mm",
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
             ["NAME:Name", "Value:=", "feed"]
             ]
        ]
    ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            ["NAME:PropServers", "feed:CreateRectangle:1"],
            ["NAME:ChangedProps",
             ["NAME:Position", "X:=", "0mm", "Y:=", "-1.5mm", "Z:=", "1.6mm"],
             ["NAME:YSize", "Value:=", "3mm"]
             ]
        ]
    ])