from typing import SupportsFloat
import sympy as sp
from typing import Any

def nsolve(sys, vars: dict[sp.Basic, Any], nsolve_=sp.nsolve) -> dict[sp.Basic, Any]:
    syms, inits = zip(*vars.items())
    sol = nsolve_(sys, syms, inits)
    return dict(zip(syms, sol))
