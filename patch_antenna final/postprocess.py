# # -*- coding: utf-8 -*-

# import ScriptEnv
# ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

# oDesktop.RestoreWindow()

# oProject = oDesktop.GetActiveProject()
# oDesign = oProject.GetActiveDesign()

# oModule = oDesign.GetModule("ReportSetup")

# data = oModule.GetSolutionDataPerVariation(
#     "Modal Solution Data",
#     "Setup1 : Sweep",
#     [],
#     ["Freq:=", ["All"]],
#     ["dB(S(1,1))"]
# )

# data = data[0]

# freqs = data.GetSweepValues()
# s11 = data.GetRealDataValues("dB(S(1,1))")

# print "\n--- S11 DATA ---"
# for i in range(len(freqs)):
#     print "Freq:", freqs[i], "GHz | S11:", s11[i], "dB"

# threshold = -10
# band = []

# for i in range(len(freqs)):
#     if s11[i] <= threshold:
#         band.append(freqs[i])

# if len(band) > 0:
#     f_low = min(band)
#     f_high = max(band)
#     bw = f_high - f_low

#     print "\n--- BANDWIDTH ---"
#     print "Lower:", f_low, "GHz"
#     print "Upper:", f_high, "GHz"
#     print "Bandwidth:", bw, "GHz"
# else:
#     print "\nNo bandwidth below -10 dB"