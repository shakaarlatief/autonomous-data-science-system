"""Prototype V0 benchmark and experiment package.

The package initializer intentionally avoids importing executable submodules.
Keeping initialization side-effect free prevents ``python -m ads_v0.casegen``
from importing ``casegen`` once through the package and then executing it a
second time through ``runpy``. Public objects should be imported from their
own modules explicitly in prototype code and tests.
"""
