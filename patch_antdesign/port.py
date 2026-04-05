def create_port(oDesign, oEditor):

    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "30mm",
            "YStart:=", "-1.5mm",
            "ZStart:=", "0mm",
            "Width:=", "3mm",
            "Height:=", "1.6mm",
            "WhichAxis:=", "X"
        ],
        [
            "NAME:Attributes",
            "Name:=", "port"
        ])

    oModule = oDesign.GetModule("BoundarySetup")

    oModule.AssignLumpedPort(
        [
            "NAME:Port1",
            "Objects:=", ["port"],
            "Impedance:=", "50ohm",

            [
                "NAME:Modes",
                [
                    "NAME:Mode1",
                    "ModeNum:=", 1,
                    "UseIntLine:=", True,

                    [
                        "NAME:IntLine",
                        "Start:=", ["30mm","0mm","0mm"],
                        "End:=",   ["30mm","0mm","1.6mm"]
                    ]
                ]
            ]
        ])