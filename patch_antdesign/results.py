def get_s11_data(oDesign):

    oModule = oDesign.GetModule("ReportSetup")

    data = oModule.GetSolutionDataPerVariation(
        "Modal Solution Data",
        "Setup1 : Sweep",
        [],                    
        ["Freq"],
        ["dB(S(1,1))"]
    )

    freq = data.GetSweepValues("Freq")
    s11 = data.GetRealDataValues("dB(S(1,1))")

    return list(freq), list(s11)


def calculate_bandwidth(freq, s11, threshold=-10):

    valid = []

    for f, s in zip(freq, s11):
        if s <= threshold:
            valid.append(f)

    if not valid:
        return 0, None, None

    f_low = min(valid)
    f_high = max(valid)

    bw = f_high - f_low

    return bw, f_low, f_high