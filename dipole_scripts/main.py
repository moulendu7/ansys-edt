import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project2")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")



def safe_delete(names):
    try:
        oEditor.Delete(
            [
                "NAME:Selections",
                "Selections:=", ",".join(names)
            ])
    except:
        pass



def create_dipole(length="62mm", radius="0.5mm", gap="2mm"):

    # Clean old objects
    safe_delete(["arm1", "arm2", "port_sheet"])

    # Expressions (HFSS-safe)
    half_len = length + "/2"
    gap_half = gap + "/2"

   
    oEditor.CreateCylinder(
        [
            "NAME:CylinderParameters",
            "XCenter:=", "0mm",
            "YCenter:=", "0mm",
            "ZCenter:=", gap_half,
            "Radius:=", radius,
            "Height:=", half_len,
            "WhichAxis:=", "Z",
            "NumSides:=", "0"
        ],
        [
            "NAME:Attributes",
            "Name:=", "arm1",
            "MaterialValue:=", "\"pec\"",
            "SolveInside:=", False
        ])

   
    oEditor.CreateCylinder(
        [
            "NAME:CylinderParameters",
            "XCenter:=", "0mm",
            "YCenter:=", "0mm",
            "ZCenter:=", "-" + gap_half + " - " + half_len,
            "Radius:=", radius,
            "Height:=", half_len,
            "WhichAxis:=", "Z",
            "NumSides:=", "0"
        ],
        [
            "NAME:Attributes",
            "Name:=", "arm2",
            "MaterialValue:=", "\"pec\"",
            "SolveInside:=", False
        ])

   
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", "-" + radius,
            "YStart:=", "-" + radius,
            "ZStart:=", "0mm",
            "Width:=", "2*" + radius,
            "Height:=", "2*" + radius,
            "WhichAxis:=", "Z"
        ],
        [
            "NAME:Attributes",
            "Name:=", "port_sheet",
            "MaterialValue:=", "\"vacuum\"",
            "SolveInside:=", True
        ])

   
    oModule = oDesign.GetModule("BoundarySetup")

    try:
        oModule.DeleteBoundaries(["Port1"])
    except:
        pass

    oModule.AssignLumpedPort(
        [
            "NAME:Port1",
            "Objects:=", ["port_sheet"],
            "LumpedPortType:=", "Modal",
            "DoDeembed:=", False,
            [
                "NAME:Modes",
                [
                    "NAME:Mode1",
                    "ModeNum:=", 1,
                    "UseIntLine:=", True,
                    [
                        "NAME:IntLine",
                        "Start:=", ["0mm", "0mm", "-" + gap_half],
                        "End:=", ["0mm", "0mm", gap_half]
                    ]
                ]
            ],
            "Impedance:=", "50ohm"
        ])

  
    oModule2 = oDesign.GetModule("ModelSetup")

    try:
        oModule2.DeleteOpenRegion()
    except:
        pass

    oModule2.CreateOpenRegion(
        [
            "NAME:Settings",
            "OpFreq:=", "2.4GHz",
            "Boundary:=", "PML",
            "ApplyInfiniteGP:=", False
        ])



create_dipole(
    length="62mm",     # total dipole length
    radius="0.5mm",   # thickness
    gap="2mm"         # feed gap
)