from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path
from .bosl2_mixin import Bosl2Mixin

extra_scad_include(f"{Path(__file__).parent.parent / '../libs/BOSL2/tripod_mounts.scad'}", use_not_include=False)

class manfrotto_rc2_plate(OpenSCADObject, Bosl2Mixin):
    def __init__(self, chamfer=None, anchor=None, orient=None, spin=None, **kwargs):
       super().__init__("manfrotto_rc2_plate", {"chamfer" : chamfer, "anchor" : anchor, "orient" : orient, "spin" : spin, **kwargs})
