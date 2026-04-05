# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2025.2.0
# 18:34:44  Apr 03, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project2")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("S Parameter Plot1", "Modal Solution Data", "Rectangular Plot", "1GHz : 800mhz_1200mhz", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"dR:="			, ["Nominal"],
		"dL:="			, ["Nominal"],
		"gL:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	])
oProject.SaveAs("C:\\Users\\moule\\OneDrive\\Documents\\Ansoft\\dipole_ant.aedt", True)
oDesign.AnalyzeAll()
oModule.AddTraceCharacteristics("S Parameter Plot1", "XAtYVal", ["0"], ["Full"])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Y Value",
					"Value:="		, "-10"
				]
			]
		]
	])
oModule.AddTraceCharacteristics("S Parameter Plot1", "XAtYVal", ["0"], ["Full"])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Y Value",
					"Value:="		, "-10"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Start of Range",
					"Value:="		, "0.9GHz"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Start of Range",
					"Value:="		, "0.9GHz"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Start of Range",
					"Value:="		, "0.9GHz"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Trace Characteristics",
			[
				"NAME:PropServers", 
				"S Parameter Plot1:XAtYVal_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Range",
					"Value:="		, "Specified"
				],
				[
					"NAME:Start of Range",
					"Value:="		, "0.9GHz"
				]
			]
		]
	])
