def create_port(oEditor, oDesign):

    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "30mm",
            "YStart:=", "-1.5mm",
            "ZStart:=", "1.6mm",
            "Width:=", "3mm",
            "Height:=", "-1.6mm",
            "WhichAxis:=", "X"
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
             ["NAME:Name", "Value:=", "port"]
             ]
        ]
    ])

    oModule = oDesign.GetModule("BoundarySetup")

    oModule.AssignLumpedPort(
        [
            "NAME:1",
            "Objects:=", ["port"],
            "LumpedPortType:=", "Default",
            "DoDeembed:=", False,
            "ImpedanceType:=", "Impedance",
            [
                "NAME:Modes",
                [
                    "NAME:Mode1",
                    "ModeNum:=", 1,
                    "UseIntLine:=", True,
                    [
                        "NAME:IntLine",
                        "Coordinate System:=", "Global",
                        "Start:=", ["30mm","0mm","0mm"],
                        "End:=", ["30mm","0mm","1.6mm"]
                    ],
                    "CharImp:=", "Zpi",
                    "RenormImp:=", "50ohm"
                ]
            ],
            "Impedance:=", "50ohm"
        ])