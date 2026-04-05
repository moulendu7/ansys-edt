# -*- coding: utf-8 -*-
import ScriptEnv

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()

oModule = oDesign.GetModule("ReportSetup")

try:
    data = oModule.GetSolutionDataPerVariation(
        "Modal Solution Data",
        "Setup1 : Sweep",
        [],
        ["Freq"],
        ["dB(S(1,1))"]
    )

    freq = list(data.GetSweepValues("Freq"))
    s11 = list(data.GetDataValues("dB(S(1,1))"))

    valid = [f for f, s in zip(freq, s11) if s <= -10]

    if valid:
        bw = max(valid) - min(valid)
        print("Bandwidth:", bw)
        oDesktop.AddMessage("", "", 0, "Bandwidth: {} GHz".format(bw))
    else:
        print("No bandwidth found")

except:
    print("Error: Could not extract S11 data")