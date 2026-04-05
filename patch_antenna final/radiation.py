def create_radiation(oEditor, oDesign):

    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:=", "0mm",
            "YPosition:=", "-30mm",
            "ZPosition:=", "25mm",
            "XSize:=", "295797570mm",
            "YSize:=", "65mm",
            "ZSize:=", "-45mm"
        ],
        [
            "NAME:Attributes",
            "Name:=", "Box1",
            "MaterialValue:=", "\"vacuum\"",
            "SolveInside:=", True
        ])

    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                ["NAME:PropServers", "Box1"],
                ["NAME:ChangedProps",
                 ["NAME:Name", "Value:=", "radbox"],
                 ["NAME:Transparent", "Value:=", 1]
                 ]
            ]
        ])

    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                ["NAME:PropServers", "radbox"],
                ["NAME:ChangedProps",
                 ["NAME:Material", "Value:=", "\"air\""]
                 ]
            ]
        ])

    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DCmdTab",
                ["NAME:PropServers", "radbox:CreateBox:1"],
                ["NAME:ChangedProps",
                 ["NAME:Position", "X:=", "-40mm", "Y:=", "-40mm", "Z:=", "-20mm"],
                 ["NAME:XSize", "Value:=", "80mm"],
                 ["NAME:YSize", "Value:=", "80mm"],
                 ["NAME:ZSize", "Value:=", "40mm"]
                 ]
            ]
        ])

    oModule = oDesign.GetModule("BoundarySetup")

    oModule.AssignRadiation(
        [
            "NAME:Rad1",
            "Objects:=", ["radbox"]
        ])