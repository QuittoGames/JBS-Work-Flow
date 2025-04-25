import os
import sys
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Wingets")))
from Wingets import Wingets

@dataclass
class winget_data:
    wingets = [Wingets(name = "Monitor De Sistema", path = os.path.abspath("Wingets/monitor_w.py"))]
