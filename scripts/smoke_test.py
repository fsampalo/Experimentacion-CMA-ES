#!/usr/bin/env python3
"""Lightweight check that the environment matches the notebook dependencies."""
from __future__ import annotations

import importlib
import sys


def main() -> int:
    for name in (
        "numpy",
        "pandas",
        "cma",
        "scipy",
        "scipy.stats",
        "matplotlib",
        "matplotlib.pyplot",
    ):
        importlib.import_module(name)

    from scipy.stats import qmc

    if not hasattr(qmc, "Sobol") or not hasattr(qmc, "LatinHypercube"):
        print("scipy.stats.qmc missing Sobol or LatinHypercube", file=sys.stderr)
        return 1

    import numpy as np

    rng = np.random.default_rng(0)
    z = rng.normal(size=(8, 4))
    assert z.shape == (8, 4)

    print("smoke_test: OK", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
