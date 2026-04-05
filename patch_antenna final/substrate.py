def create_substrate(oEditor):
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:=", "-30mm",
            "YPosition:=", "30mm",
            "ZPosition:=", "0mm",
            "XSize:=", "60mm",
            "YSize:=", "-60mm",
            "ZSize:=", "10mm"
        ],
        [
            "NAME:Attributes",
            "Name:=", "Box1",
            "MaterialValue:=", "\"vacuum\"",
            "SolveInside:=", True
        ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            ["NAME:PropServers", "Box1"],
            ["NAME:ChangedProps",
             ["NAME:Name", "Value:=", "substrate"],
             ["NAME:Material", "Value:=", "\"FR4_epoxy\""]
             ]
        ]
    ])

    oEditor.ChangeProperty([
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            ["NAME:PropServers", "substrate:CreateBox:1"],
            ["NAME:ChangedProps",
             ["NAME:ZSize", "Value:=", "1.6mm"]
             ]
        ]
    ])