import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

import os

oDesktop.RestoreWindow()

oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()

oModule = oDesign.GetModule("ReportSetup")

data = oModule.GetSolutionDataPerVariation(
    "Modal Solution Data",
    "Setup1 : Sweep",
    [],
    ["Freq:=", ["All"]],
    ["dB(S(1,1))"]
)

data = data[0]

freqs = data.GetSweepValues("Freq")
s11 = data.GetRealDataValues("dB(S(1,1))")

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "s11_data.csv")

f = open(file_path, "w")
f.write("Frequency_GHz,S11_dB\n")

for i in range(len(freqs)):
    f.write(str(freqs[i]) + "," + str(s11[i]) + "\n")

f.close()
