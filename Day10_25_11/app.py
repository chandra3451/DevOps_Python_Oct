# =========================================================
#      Importing Classes From a Module (agent.py)
# =========================================================

# -------- Method 1: Import entire module (recommended) --------
import agent as ag

a1 = ag.Agent("Mario", 30)    # Access class using module alias
print(a1.info())


# -------- Method 2: Import only the class --------
from agent import Agent

a2 = Agent("Sam", 25)         # Direct access, no prefix needed
print(a2.info())
