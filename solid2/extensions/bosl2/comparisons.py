from solid2.core.object_base import OpenSCADObject as _OpenSCADObject,                                    OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path
from .bosl2_mixin import Bosl2Mixin as _Bosl2Mixin

_extra_scad_include(f"{_Path(__file__).parent.parent / '../libs/BOSL2/comparisons.scad'}", use_not_include=False)

class approx(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, a=None, b=None, eps=None, **kwargs):
       super().__init__("approx", {"a" : a, "b" : b, "eps" : eps, **kwargs})

class all_zero(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_zero", {"x" : x, "eps" : eps, **kwargs})

class all_nonzero(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonzero", {"x" : x, "eps" : eps, **kwargs})

class all_positive(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_positive", {"x" : x, "eps" : eps, **kwargs})

class all_negative(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_negative", {"x" : x, "eps" : eps, **kwargs})

class all_nonpositive(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonpositive", {"x" : x, "eps" : eps, **kwargs})

class all_nonnegative(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonnegative", {"x" : x, "eps" : eps, **kwargs})

class all_equal(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, vec=None, eps=None, **kwargs):
       super().__init__("all_equal", {"vec" : vec, "eps" : eps, **kwargs})

class is_increasing(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, strict=None, **kwargs):
       super().__init__("is_increasing", {"list" : list, "strict" : strict, **kwargs})

class is_decreasing(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, strict=None, **kwargs):
       super().__init__("is_decreasing", {"list" : list, "strict" : strict, **kwargs})

class _type_num(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, x=None, **kwargs):
       super().__init__("_type_num", {"x" : x, **kwargs})

class compare_vals(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("compare_vals", {"a" : a, "b" : b, **kwargs})

class compare_lists(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("compare_lists", {"a" : a, "b" : b, **kwargs})

class min_index(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, vals=None, all=None, **kwargs):
       super().__init__("min_index", {"vals" : vals, "all" : all, **kwargs})

class max_index(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, vals=None, all=None, **kwargs):
       super().__init__("max_index", {"vals" : vals, "all" : all, **kwargs})

class find_approx(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, val=None, list=None, start=None, all=None, eps=None, **kwargs):
       super().__init__("find_approx", {"val" : val, "list" : list, "start" : start, "all" : all, "eps" : eps, **kwargs})

class __find_approx(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, val=None, list=None, eps=None, i=None, **kwargs):
       super().__init__("__find_approx", {"val" : val, "list" : list, "eps" : eps, "i" : i, **kwargs})

class deduplicate(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, closed=None, eps=None, **kwargs):
       super().__init__("deduplicate", {"list" : list, "closed" : closed, "eps" : eps, **kwargs})

class deduplicate_indexed(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, indices=None, closed=None, eps=None, **kwargs):
       super().__init__("deduplicate_indexed", {"list" : list, "indices" : indices, "closed" : closed, "eps" : eps, **kwargs})

class unique(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, **kwargs):
       super().__init__("unique", {"list" : list, **kwargs})

class _unique_sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, l=None, **kwargs):
       super().__init__("_unique_sort", {"l" : l, **kwargs})

class unique_count(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, **kwargs):
       super().__init__("unique_count", {"list" : list, **kwargs})

class _valid_idx(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, idx=None, imin=None, imax=None, **kwargs):
       super().__init__("_valid_idx", {"idx" : idx, "imin" : imin, "imax" : imax, **kwargs})

class _group_sort_by_index(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, l=None, idx=None, **kwargs):
       super().__init__("_group_sort_by_index", {"l" : l, "idx" : idx, **kwargs})

class _group_sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, l=None, **kwargs):
       super().__init__("_group_sort", {"l" : l, **kwargs})

class _sort_scalars(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arr=None, **kwargs):
       super().__init__("_sort_scalars", {"arr" : arr, **kwargs})

class _sort_vectors(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arr=None, _i=None, **kwargs):
       super().__init__("_sort_vectors", {"arr" : arr, "_i" : _i, **kwargs})

class _sort_vectors(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arr=None, idxlist=None, _i=None, **kwargs):
       super().__init__("_sort_vectors", {"arr" : arr, "idxlist" : idxlist, "_i" : _i, **kwargs})

class _sort_general(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arr=None, idx=None, indexed=None, **kwargs):
       super().__init__("_sort_general", {"arr" : arr, "idx" : idx, "indexed" : indexed, **kwargs})

class _lexical_sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arr=None, **kwargs):
       super().__init__("_lexical_sort", {"arr" : arr, **kwargs})

class _indexed_sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, arrind=None, **kwargs):
       super().__init__("_indexed_sort", {"arrind" : arrind, **kwargs})

class sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("sort", {"list" : list, "idx" : idx, **kwargs})

class sortidx(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("sortidx", {"list" : list, "idx" : idx, **kwargs})

class group_sort(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("group_sort", {"list" : list, "idx" : idx, **kwargs})

class group_data(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, groups=None, values=None, **kwargs):
       super().__init__("group_data", {"groups" : groups, "values" : values, **kwargs})

class list_smallest(_OpenSCADObject, _Bosl2Mixin):
    def __init__(self, list=None, k=None, **kwargs):
       super().__init__("list_smallest", {"list" : list, "k" : k, **kwargs})

