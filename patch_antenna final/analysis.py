def setup_analysis(oDesign):
    oModule = oDesign.GetModule("AnalysisSetup")

    oModule.InsertSetup("HfssDriven",
        [
            "NAME:Setup1",
            "Frequency:=", "2.4GHz",
            "MaxDeltaS:=", 0.02
        ])

    oModule.InsertFrequencySweep("Setup1",
        [
            "NAME:Sweep",
            "RangeStart:=", "1GHz",
            "RangeEnd:=", "3GHz",
            "RangeStep:=", "0.01GHz"
        ])