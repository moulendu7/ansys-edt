def assign_boundaries(oDesign):
    oModule = oDesign.GetModule("BoundarySetup")

    oModule.AssignPerfectE(
        [
            "NAME:PerfE1",
            "Objects:=", ["patch", "ground"],
            "InfGroundPlane:=", False
        ])