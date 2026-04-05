# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2025.2.0
# 17:49:41  Apr 03, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project2")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "0.4mm",
		"Height:="		, "1.8mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:dR",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:dL",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "150mm"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Cylinder1:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Radius",
					"Value:="		, "dR"
				],
				[
					"NAME:Height",
					"Value:="		, "dL"
				],
				[
					"NAME:Center Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-dL/2"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Cylinder1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "dipole"
				],
				[
					"NAME:Material",
					"Value:="		, "\"pec\""
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "dipole"
	])
oEditor.Paste()
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"dipole1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "gap"
				],
				[
					"NAME:Material",
					"Value:="		, "\"vacuum\""
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:gL",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"gap:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Height",
					"Value:="		, "gL"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"gap:CreateCylinder:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Center Position",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-gL/2"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "dipole",
		"Tool Parts:="		, "gap"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, True,
		"TurnOnNBodyBoolean:="	, True
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"gap"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Transparent",
					"Value:="		, 1
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Section(
	[
		"NAME:Selections",
		"Selections:="		, "gap",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SectionToParameters",
		"CreateNewObjects:="	, True,
		"SectionPlane:="	, "YZ",
		"SectionCrossObject:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"gap_Section1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "p1"
				],
				[
					"NAME:Transparent",
					"Value:="		, 1
				],
				[
					"NAME:Transparent",
					"Value:="		, 0.6
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["p1"],
		"LumpedPortType:="	, "Modal",
		"DoDeembed:="		, False,
		"ImpedanceType:="	, "Impedance",
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Coordinate System:="	, "Global",
					"Start:="		, ["0mm","0mm","-0.5mm"],
					"End:="			, ["0mm","0mm","0.5mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"Impedance:="		, "50ohm"
	])
oModule = oDesign.GetModule("ModelSetup")
oModule.CreateOpenRegion(
	[
		"NAME:Settings",
		"OpFreq:="		, "1GHz",
		"Boundary:="		, "PML",
		"ApplyInfiniteGP:="	, False
	])
