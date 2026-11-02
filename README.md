# y+ Calculator

Estimates the first-cell height and the number of inflation (prism) layers needed to resolve a turbulent flat-plate boundary layer at a target y+. Useful for sizing near-wall meshes in CFD.

The repo has two versions of the same calculation:

- **`index.html`**: a standalone web app that recalculates as you type, with air and water presets, validity warnings, and a to-scale drawing of the layer stack.
- **`yplus.py`**: a short Python script that prints the same results.

## Usage

### Web app

Open `index.html` in any browser. It has no dependencies and needs no build step or server.

### Python script

Requires Python 3 and NumPy.

```sh
pip install numpy
python yplus.py
```

To change the inputs, edit the variables at the top of the script (`rho`, `U`, `L`, `mu`, `yp_desired`, `growth`).

## Inputs

| Symbol | Description | Units |
|---|---|---|
| ρ | Fluid density | kg m⁻³ |
| U | Free-stream velocity | m s⁻¹ |
| L | Reference length | m |
| μ | Dynamic viscosity | kg m⁻¹ s⁻¹ |
| y+ | Target non-dimensional wall distance | – |
| g | Inflation layer growth rate (> 1) | – |

## Method

1. Reynolds number: `Re = ρ U L / μ`
2. Skin-friction coefficient (Schlichting, valid for Re < 10⁹): `Cf = (2 log₁₀ Re − 0.65)^−2.3`
3. Wall shear stress: `τw = ½ Cf ρ U²`
4. Friction velocity: `uτ = √(τw / ρ)`
5. First-cell height: `y_min = y+ μ / (ρ uτ)`
6. Turbulent boundary-layer thickness: `δ = 0.37 L / Re^0.2`
7. Number of layers whose geometric sum reaches δ: `n = ln(δ (g − 1) / y_min + 1) / ln g`

The web app also reports ⌈n⌉, the height of the final layer, and the total thickness of the rounded-up stack.

## Limitations

- Uses flat-plate, zero-pressure-gradient correlations. Treat the results as a starting estimate for complex geometries.
- Assumes turbulent flow. Below Re ≈ 5×10⁵ the flow may be laminar and the correlations may not apply.
- Growth rates above about 1.3 can degrade boundary-layer resolution.
