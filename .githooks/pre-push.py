#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Github pre-push hook based on Python to check test cases.
"""

import os
import sys
from unittest import defaultTestLoader as loader, TextTestRunner

PRJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, PRJ_DIR)

suite = loader.discover('tests')
runner = TextTestRunner()
passed = runner.run(suite).wasSuccessful()

if not passed:
    print ("""      dS$$S$S$S$S$S$S$$Sb                    
                   :$$S^S$S$S$S$S$S^S$$;                   
                   SSP   `^$S$S$^'   TSS                   
                   $$       `"'       $$                   
                  _SS ,-           -  SS_                  
                 :-.|  _    - .-   _  |.-;                 
                 :\(; ' "-._.'._.-" ` |)/;                 
                  \`|  , o       o .  |'/                  
                   ":     -'   `-     ;"                   
                     ;.              :  bug                
                     : `    ._.    ' ;                     
                   .sSb   ._____.   dSs.                   
                _.d8dSSb.   ._.   .SSbT8b._                
            _.oOPd88SSSS T.     .P SSSS888OOo.             
        _.mMMOOPd888SSSSb TSqqqSP dSSSS88OMOOOMm._         
     .oOMMMOMOOM8O8OSSSSSb TSSSP dSSSSS8OOMMOOMMOOOo._     
   .OOMMOOOMMOOMOOOO  "^SSSTSSP dSSS^"OOOOMMOOMMMOOMMMb.   
  dOOOMMMOMMOOOMOOOO      "^SSSS^"   :OOO8MMMOOMMOOMMOMMb  
 :MMMOOMMOMMOOMMO8OS         `P      8O8OPdMMOOMMOMMOMMMM; 
 MMMMOOMMMMMOOMbTO8S;               :8888MMMMMOMMOMMOMMMMM 
 OMMMMOOMMMMOOOMMOOOS        S     :O8OPdMOMMMOMOMMOOMMMMO 
:OMMMMOOMMOMMOOMbTObTb.     :S;   .PdOPdMOOMMMMMOMMOMMMMMO;
MOOMMMMOMMOMMOOMMMOObTSSg._.SSS._.PdOPdMOOMMMMOMMMMOMMMMOOM
MMOMMMMOMMMOMMOOMMbT8bTSSSSSSSSSPd8OPdOOOMMMMOOMMMMOMMMOOMM
MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM
    """)
    sys.exit(1)
else:
    print("""
          ,
   \  :  /
`. __/ \__ .'
_ _\     /_ _
   /_   _\
 .'  \ /  `.
   /  :  \    PUSHED 
    """)


