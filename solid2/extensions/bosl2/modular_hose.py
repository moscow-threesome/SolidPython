from solid2.core.object_base import OpenSCADObject as _OpenSCADObject,                                    OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path
from .bosl2_mixin import Bosl2Mixin as _Bosl2Mixin

_extra_scad_include(f"{_Path(__file__).parent.parent / '../libs/BOSL2/modular_hose.scad'}", use_not_include=False)

_small_end = _OpenSCADConstant('_small_end')
_big_end = _OpenSCADConstant('_big_end')
_hose_waist = _OpenSCADConstant('_hose_waist')
class modular_hose(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose", {"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class modular_hose_radius(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, size=None, outer=None, **kwargs):
       super().__init__("modular_hose_radius", {"size" : size, "outer" : outer, **kwargs})

class modular_hose(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, size=None, type=None, clearance=None, waist_len=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("modular_hose", {"size" : size, "type" : type, "clearance" : clearance, "waist_len" : waist_len, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

