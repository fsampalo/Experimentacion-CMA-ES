# README gallery (optional)

GitHub renders images linked from the repository root `README.md` only if the files exist in the tree.

1. Run `cma_sampling.ipynb` once to generate figures under `imgs/comparisons/`.
2. Copy one or two representative PNGs here, for example:
   - `sphere_preview.png` from `Sphere_comparison.png`
   - `runtime_preview.png` from `runtime_comparison.png`
3. In the main `README.md`, add a gallery block such as:

```markdown
<p align="center">
  <img src="docs/gallery/sphere_preview.png" width="720" alt="Sphere: sampling comparison" />
</p>
```

Keep file sizes reasonable (compress PNGs if needed) so the repo stays fast to clone.
