# -*- coding: utf-8 -*-

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project2")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

# ----------------------------------------------
# SAFE VARIABLE CREATION
# ----------------------------------------------
def create_variable_if_not_exists(name, value):
    try:
        oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:LocalVariableTab",
                ["NAME:PropServers", "LocalVariables"],
                [
                    "NAME:NewProps",
                    [
                        "NAME:" + name,
                        "PropType:=", "VariableProp",
                        "UserDef:=", True,
                        "Value:=", value
                    ]
                ]
            ]
        ])
        print(name + " created")
    except:
        print(name + " already exists")

# ----------------------------------------------
# SAFE VARIABLE UPDATE
# ----------------------------------------------
def set_variable(name, value):
    try:
        oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:LocalVariableTab",
                ["NAME:PropServers", "LocalVariables"],
                [
                    "NAME:ChangedProps",
                    ["NAME:" + name, "Value:=", value]
                ]
            ]
        ])
    except:
        print("Error updating " + name)

# ----------------------------------------------
# INITIALIZE VARIABLES (SAFE)
# ----------------------------------------------
def init_variables():

    create_variable_if_not_exists("dR", "0.1250mm")
    create_variable_if_not_exists("dL", "59.5833mm")
    create_variable_if_not_exists("gL", "0.2979mm")
    create_variable_if_not_exists("halfL", "(dL-gL)/2")

# ----------------------------------------------
# BUILD GEOMETRY (RUN ONLY ONCE)
# ----------------------------------------------
def build_geometry():

    # Avoid duplicate creation
    try:
        oEditor.GetObjectIDByName("arm_top")
        print("Geometry already exists")
        return
    except:
        pass

    # TOP ARM
    oEditor.CreateCylinder(
    [
        "NAME:CylinderParameters",
        "XCenter:=", "0mm",
        "YCenter:=", "0mm",
        "ZCenter:=", "gL/2",
        "Radius:=", "dR",
        "Height:=", "halfL",
        "WhichAxis:=", "Z"
    ],
    [
        "NAME:Attributes",
        "Name:=", "arm_top",
        "MaterialValue:=", "\"pec\"",
        "SolveInside:=", False
    ])

    # BOTTOM ARM
    oEditor.CreateCylinder(
    [
        "NAME:CylinderParameters",
        "XCenter:=", "0mm",
        "YCenter:=", "0mm",
        "ZCenter:=", "-(gL/2 + halfL)",
        "Radius:=", "dR",
        "Height:=", "halfL",
        "WhichAxis:=", "Z"
    ],
    [
        "NAME:Attributes",
        "Name:=", "arm_bottom",
        "MaterialValue:=", "\"pec\"",
        "SolveInside:=", False
    ])

    # GAP
    oEditor.CreateCylinder(
    [
        "NAME:CylinderParameters",
        "XCenter:=", "0mm",
        "YCenter:=", "0mm",
        "ZCenter:=", "-gL/2",
        "Radius:=", "dR",
        "Height:=", "gL",
        "WhichAxis:=", "Z"
    ],
    [
        "NAME:Attributes",
        "Name:=", "gap",
        "MaterialValue:=", "\"vacuum\"",
        "Transparency:=", 0.7,
        "SolveInside:=", True
    ])

    # SECTION
    oEditor.Section(
    [
        "NAME:Selections",
        "Selections:=", "gap",
        "NewPartsModelFlag:=", "Model"
    ],
    [
        "NAME:SectionToParameters",
        "CreateNewObjects:=", True,
        "SectionPlane:=", "YZ"
    ])

    oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            ["NAME:PropServers", "gap_Section1"],
            [
                "NAME:ChangedProps",
                ["NAME:Name", "Value:=", "port_face"]
            ]
        ]
    ])

# ----------------------------------------------
# ASSIGN PORT (SAFE)
# ----------------------------------------------
def assign_port():

    oModule = oDesign.GetModule("BoundarySetup")

    try:
        oModule.GetBoundaries()
        print("Port may already exist")
    except:
        pass

    oModule.AssignLumpedPort(
    [
        "NAME:LumpedPort1",
        "Objects:=", ["port_face"],
        "LumpedPortType:=", "Modal",
        [
            "NAME:Modes",
            [
                "NAME:Mode1",
                "ModeNum:=", 1,
                "UseIntLine:=", True,
                [
                    "NAME:IntLine",
                    "Start:=", ["0mm","0mm","-gL/2"],
                    "End:=", ["0mm","0mm","gL/2"]
                ],
                "CharImp:=", "Zpi",
                "RenormImp:=", "50ohm"
            ]
        ]
    ])

# ----------------------------------------------
# UPDATE FUNCTION (MAIN CONTROL)
# ----------------------------------------------
def update_dipole(length_mm, radius_mm, gap_mm):

    set_variable("dL", str(length_mm) + "mm")
    set_variable("dR", str(radius_mm) + "mm")
    set_variable("gL", str(gap_mm) + "mm")

    print("Updated Length=" + str(length_mm))

# ----------------------------------------------
# RUN EVERYTHING SAFELY
# ----------------------------------------------
init_variables()
build_geometry()
assign_port()

# Example
update_dipole(59.5833,  0.1250, 0.2979)