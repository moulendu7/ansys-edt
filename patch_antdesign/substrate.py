def create_substrate(oEditor):
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XPosition:=", "-30mm",
            "YPosition:=", "30mm",
            "ZPosition:=", "0mm",
            "XSize:=", "60mm",
            "YSize:=", "-60mm",
            "ZSize:=", "1.6mm"
        ],
        [
            "NAME:Attributes",
            "Name:=", "substrate",
            "MaterialValue:=", "\"FR4_epoxy\""
        ])