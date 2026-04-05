def assign_boundaries(oDesign, oEditor):

    oModule = oDesign.GetModule("BoundarySetup")

    # ---------------- PERFECT E ----------------
    oModule.AssignPerfectE(
        [
            "NAME:PerfE1",
            "Objects:=", ["patch", "ground"]
        ])

    # ---------------- RADIATION BOX ----------------
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:=", "-40mm",
            "YPosition:=", "-40mm",
            "ZPosition:=", "-20mm",
            "XSize:=", "80mm",
            "YSize:=", "80mm",
            "ZSize:=", "40mm"
        ],
        [
            "NAME:Attributes",
            "Name:=", "radbox",
            "MaterialValue:=", "\"air\"",
            "Transparency:=", 0.8
        ])

    # ---------------- RADIATION BOUNDARY ----------------
    oModule.AssignRadiation(
        [
            "NAME:Rad1",
            "Objects:=", ["radbox"]
        ])