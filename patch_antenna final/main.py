import sys
import os
sys.path.append(os.path.dirname(__file__))

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")

oDesktop.RestoreWindow()

from boolean_ops import unite_patch_feed
from setup_env import initialize
from ground import create_ground
from substrate import create_substrate
from patch import create_patch
from feed import create_feed
from cut import create_cut
from port import create_port
from boundaries import assign_boundaries
from radiation import create_radiation
from analysis import setup_analysis

oProject, oDesign, oEditor = initialize(oDesktop)

create_ground(oEditor)
create_substrate(oEditor)

create_patch(oEditor)
create_feed(oEditor)
create_cut(oEditor)

unite_patch_feed(oEditor)  

create_port(oEditor, oDesign)

create_radiation(oEditor, oDesign)   

assign_boundaries(oDesign)          
setup_analysis(oDesign)