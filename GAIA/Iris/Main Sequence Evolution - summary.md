# Main Sequence Evolution — Summary

## 1. Key Concepts

- **ZAMS**: locus of stars at the instant of core H-ignition; a snapshot across masses, not an evolutionary track. All ZAMS stars are chemically homogeneous.
- **Pre-MS / Hayashi track**: pre-ignition convective track that converges onto the ZAMS.
- **Brown dwarf**: object with $M<0.08\,M_\odot$; never ignites the pp chain; cools by radiating gravitational energy.
- **Eddington luminosity ($L_{ed}$)**: maximum luminosity a star of mass $M$ can sustain while remaining in hydrostatic equilibrium.
- **pp chain**: dominant H-burning mode for $M\lesssim1.2\,M_\odot$; moderate temperature sensitivity.
- **CNO cycle**: dominant H-burning mode for $M\gtrsim1.2\,M_\odot$; extreme temperature sensitivity; requires catalyst CNO nuclei.
- **Convective core / radiative envelope**: structure for $M>1.2\,M_\odot$, caused by centrally concentrated CNO energy release.
- **Radiative core / convective envelope**: structure for $0.3<M/M_\odot<1.2$ (e.g. the Sun), caused by high surface opacity and low $\nabla_{ad}$ from partial ionization.
- **Fully convective star**: $M<0.3\,M_\odot$; extreme version of the envelope-convection mechanism operating throughout the star.
- **Mass-luminosity relation**: broken power law $L\propto M^n$ with $n$ depending on which burning mode/mass regime applies.
- **Main sequence (evolutionary phase)**: interval of core H-burning, from Point 1 (ignition) to Point 2 ($X_c<0.05$); TAMS is the locus of all Point-2 positions.
- **Mean molecular weight $\mu$**: rises as H converts to He; drives the slow structural evolution during the MS.
- **Isothermal He core**: chemically inert, energy-generation-free He core with $dT/dr=0$, formed after Point 3.
- **Core mass fraction $q=M_c/M_{tot}$**: diagnostic of how much pressure the core must supply.
- **Schönberg–Chandrasekhar (SC) limit**: maximum mass an ideal-gas isothermal core can support against the envelope before contracting (Schönberg & Chandrasekhar, 1942).
- **Electron degeneracy**: state where all levels below the Fermi energy are filled; pressure becomes density-dependent only, decoupled from $T$.
- **"Hook" feature**: rapid track excursion at MS turnoff caused by a gravitational-contraction phase in high-mass stars with convective cores.
- **Kelvin–Helmholtz (thermal) timescale**: governs contraction when no nuclear energy source is available (post-Point-2 for high-mass stars, post-SC-limit for intermediate mass).
- **$\log\rho$–$\log T$ diagram**: divides stellar interiors into radiation-dominated, ideal-gas, and (non-)relativistic degenerate regions.

## 2. Key Equations

**Eddington luminosity** (max luminosity before radiation pressure disrupts hydrostatic equilibrium):
$$L_{ed} = \frac{4\pi G M c}{\kappa}, \qquad \frac{L_{ed}}{L_\odot}\approx 3.8\times10^4\,\frac{M}{M_\odot}\ \ (\kappa=0.34\ \text{cm}^2\text{g}^{-1},\ X=0.7)$$

**Opacity from electron scattering:** $\kappa = 0.2(1+X)$.

**Nuclear energy generation rates** (govern which chain dominates and whether the core convects):
$$\epsilon_{pp}\propto \rho X^2 T_6^{5}, \qquad \epsilon_{CNO}\propto \rho X Z_{CNO} T_6^{15}$$

**Convection criterion:** $\nabla_{rad}>\nabla_{ad}$, with
$$\left.\frac{dT}{dr}\right|_{rad} = -\frac{3\kappa\rho}{4acT^3}\frac{L_r}{4\pi r^2}$$
Large, concentrated $L_r$ (CNO case) drives $\nabla_{rad}>\nabla_{ad}$ in the core.

**Kramers opacity (relevant to convective envelopes):** $\kappa\propto T^{-3.5}$; $\nabla_{ad}=1-1/\gamma\to0$ in partial-ionization zones.

**MS lifetime scaling** (from $t_{MS}\propto M/L$, $L\propto M^4$):
$$t_{MS}\cong 10^{10}\,M^{-3}\ \text{yr}$$

**Mean molecular weight** (fully ionized gas):
$$\mu = \frac{1}{2X+\tfrac34 Y+\tfrac12 Z}, \qquad P=\frac{k\rho T}{\mu H}$$

**SC limit** (two equivalent forms):
$$q\le q_0 = 0.37\left(\frac{\mu_e}{\mu_{ic}}\right)^2 \approx 0.08, \qquad M_c\le M_{sc}=0.10\,M_{tot}$$

**Electron degeneracy condition:**
$$\frac{T}{\rho^{2/3}} < D\approx10^{5}\ \text{K cm}^2\text{g}^{-2/3}, \qquad \log T = \tfrac23\log\rho + 5.11\ \text{(boundary)}$$

## 3. Key Algorithms / Procedures

1. **Determine burning mode and structure from mass:** compare $M$ to $1.2\,M_\odot$ → CNO (convective core) vs pp (radiative core); compare to $0.3\,M_\odot$ → fully convective; this single branch point (mass → burning mode) propagates through structure, $T_c$–$M$ relation, mass–luminosity slope, and post-MS morphology (Section 14.2 "central organizing principle").
2. **Derive $L_{ed}$:** set the radiative pressure gradient equal to the hydrostatic gradient, cancel $\rho$ and $r^2$, solve for $L$.
3. **Derive the SC limit:**
   - Step 1: integrate hydrostatic equilibrium over the isothermal core to get a virial-like relation; maximize $P_{ic}$ over core radius to find $P_{ic}^{max}\propto 1/M_{ic}^2$.
   - Step 2: integrate hydrostatic equilibrium over the envelope (using $M_{ic}^2\ll M^2$) to estimate the envelope pressure on the core, $P_{env}\propto 1/M^2$.
   - Step 3: equate $P_{ic}^{max}=P_{env}$ and solve for $M_{ic}/M$; the coefficient depends on $(\mu_{env}/\mu_{ic})^2$.
4. **Determine post-MS pathway from mass (Section 13.1):** $M>6\,M_\odot$ → no isothermal phase, stays ideal gas, direct He ignition; $2.2<M/M_\odot<6$ → temporary isothermal core, hits SC limit, contracts, ignites He (small hook); $M<2.2\,M_\odot$ → core crosses the degeneracy line before the SC limit, grows without heating, long RGB ascent, helium flash.
5. **Track H-profile → Point-2/3 transition:** radiative core (low mass) gives smooth gradient → seamless shell ignition (Points 2≈3); convective core (high mass) gives flat/step profile that empties simultaneously → gravitational-contraction gap → hook → Point 3.

## 4. Watch Out For

- ZAMS ≠ evolutionary track — a common conflation; ZAMS is a snapshot across masses at $t=0$.
- The $90\,M_\odot$ upper limit is *not* rigorous — it is metallicity-dependent and stems from $L_\star$ approaching $L_{ed}$ (only a factor of ~3 away at $90\,M_\odot$).
- The pp/CNO transition mass is deceptively low ($\approx1.2\,M_\odot$) despite core temperatures differing only modestly — the $T^{15}$ vs $T^5$ exponent, not the absolute $T$, is what matters.
- Higher-mass stars have **lower** central density despite higher luminosity/temperature — this is why degeneracy is avoided at high mass and unavoidable at low mass (exam favorite: connect $\rho_c$ trend to degeneracy condition $T/\rho^{2/3}<D$).
- Mass–luminosity exponent is not a single number: $\approx3.6$ (upper MS, CNO), $4$–$4.5$ (lower MS, pp), $2.6$ (very low mass) — a broken power law, not one universal slope.
- Metallicity and helium effects can seem to pull in the same "brighter/hotter" direction but arise from different mechanisms and have **opposite** effects on turnoff mass at fixed age: higher $Z$ → longer lifetime → **larger** turnoff mass; higher $Y$ → shorter lifetime → **smaller** turnoff mass.
- Low-mass MS track shifts slightly up-and-left (hotter) during 1–2, while high-mass shifts up-and-right (cooler) — the sign of the $T_{eff}$ change flips because the burning region's spatial extent (20–30% vs ~10% of radius) determines whether core contraction can counteract envelope expansion. Do not assume both regimes redden or both bluen.
- Increasing $R$ does not automatically mean cooling — only if $R^2$ grows faster than $L$; in low-mass stars $L$ outpaces $R^2$, so $T_{eff}$ still rises.
- Two SC-limit numbers exist and are *not* interchangeable defaults: $q_0\approx0.08$–$0.10$ is compositional/derived; the commonly quoted round number $M_c\le0.10\,M_{tot}$ is the practical formulation.
- The textbook derivation of the SC limit yields a coefficient of 0.7, not the accepted 0.37 — the discrepancy is from approximations in $P_{env}$ and $R$; the $(\mu_{env}/\mu_{ic})^2$ scaling is the exact, examinable part.
- The hook is diagnostic of a **convective core** during the MS, not of high mass per se — it is observationally confirmed (NGC 1978 CMD) and only appears for $M\gtrsim1.2\,M_\odot$ (technically most visible in the $2.2$–$6\,M_\odot$ regime).
- Do not confuse "isothermal" with "unsupported" — the isothermal core still satisfies hydrostatic equilibrium via a density gradient, not a temperature gradient.
- The three post-MS regimes are separated by two different physical limits (SC limit vs. degeneracy boundary), not the same limit at different masses — know which boundary is crossed first for a given mass.
