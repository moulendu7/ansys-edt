def initialize(oDesktop):
    oDesktop.RestoreWindow()

    oProject = oDesktop.SetActiveProject("temporary")
    oDesign = oProject.SetActiveDesign("HFSSDesign1")
    oEditor = oDesign.SetActiveEditor("3D Modeler")

    return oProject, oDesign, oEditor