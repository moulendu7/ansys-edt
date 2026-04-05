# -*- coding: utf-8 -*-
import ScriptEnv

def init_hfss():
    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

    oDesktop = ScriptEnv.GetDesktop()   

    oDesktop.RestoreWindow()

    oProject = oDesktop.NewProject()
    oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")

    oDesign = oProject.SetActiveDesign("HFSSDesign1")
    oEditor = oDesign.SetActiveEditor("3D Modeler")

    return oDesktop, oProject, oDesign, oEditor