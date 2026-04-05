import ScriptEnv
import sys
import os

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()

oProject = oDesktop.GetActiveProject()


if oProject is None:
    oProject = oDesktop.NewProject()

try:
    oDesign = oProject.SetActiveDesign("HFSSDesign1")
except:
    oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
    oDesign = oProject.SetActiveDesign("HFSSDesign1")

oEditor = oDesign.SetActiveEditor("3D Modeler")

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from ground import create_ground
from substrate import create_substrate
from patch import create_patch
from port import create_port
from boundary import assign_boundaries


def main():

    create_ground(oEditor)
    create_substrate(oEditor)
    create_patch(oEditor)
    create_port(oDesign, oEditor)
    assign_boundaries(oDesign, oEditor)

    print("Design updated in existing project!")


if __name__ == "__main__":
    main()