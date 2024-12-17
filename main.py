import numpy as np

from fitting_models import Curve, PSD, MolarVolume, DistributionParameters
from utils import StokesRadiusCalculator, DiffusivityCalculator, Solvent

def main():
    molecular_weights = np.array([1000, 2000, 3000, 4000, 5000, 6000])
    rejections = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 0.95])
    errors = np.zeros_like(rejections)

    mwco_fitting = Curve(molecular_weights, rejections, errors)
    mw_range, fitted_curve, _, _, _ = mwco_fitting.fit_curve('boltzmann')

    print("MWCO Curve Fit:")
    print("Molecular Weights Range:", mw_range)
    print("Fitted Curve Values:", fitted_curve)

    x = np.linspace(1, 100, 100)  # Random pore sizes
    avg_radius = 50.0
    std_dev = 10.0
    psd = PSD.log_normal(x, avg_radius, std_dev)

    print("\nPore Size Distribution:")
    print("Pore sizes:", x)
    print("PSD values:", psd)

    diffusion_coefficient = 1e-5  # cm²/s
    stokes_radius = StokesRadiusCalculator.stokes_einstein_radius(diffusion_coefficient,298.15,0.543)
    
    print("\nStokes-Einstein Radius:")
    print("Radius (nm):", stokes_radius)

    solvent = Solvent.from_selection(1, 298.15, 0.001)  # Water
    diffusivity = DiffusivityCalculator.wilke_chang_diffusion_coefficient(18.015, 18.015, 298.15, solvent.viscosity, solvent.alpha)

    print("\nWilke-Chang Diffusivity Coefficient (for water):")
    print("Diffusivity:", diffusivity)

if __name__ == "__main__":
    main()
