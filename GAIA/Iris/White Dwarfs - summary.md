# White Dwarfs — Summary

## 1. Key Concepts

- **$M_\mathrm{up}$ ($\approx 8\,M_\odot$):** mass boundary separating stars that end as WDs (degenerate CO core, no further burning) from stars that ignite carbon and beyond.
- **Reimers law regime / stellar wind:** empirical mass-loss prescription for RGB/AGB stars, parametrised by free efficiency parameter $\eta$.
- **Radiation-driven / dust-driven wind:** mass loss driven by radiation pressure on dust grains formed in cool, extended atmospheres.
- **Superwind:** extreme terminal AGB mass-loss phase ($\dot M \sim 10^{-4}\,M_\odot\,\mathrm{yr}^{-1}$) linked to MIRA pulsations; ends the AGB when envelope mass drops below $10^{-3}\,M_\odot$.
- **Planetary Nebula (PN):** UV-ionised ejected envelope, triggered once the contracting remnant reaches $T_\mathrm{eff}\approx 30{,}000$ K.
- **CO white dwarf:** the electron-degenerate carbon-oxygen remnant left after envelope ejection and cessation of nuclear burning.
- **Electron degeneracy:** quantum state where the Pauli exclusion principle sets the pressure, independent of temperature; condition $T/\rho^{2/3} < D = 1.3\times10^5$.
- **DA/DB/DC spectral classes:** WD atmosphere types (H-rich ~80%, He-rich ~8%, featureless ~14%), explained by gravitational settling of heavy elements under extreme surface gravity.
- **Mass-radius relation (non-relativistic):** $R \propto M^{-1/3}$ — WDs get smaller as they get more massive (opposite of normal stars).
- **Chandrasekhar mass ($M_\mathrm{Ch}$):** the unique maximum mass ($1.44\,M_\odot$) an electron-degenerate structure can support; applies generally, not only to WDs (also degenerate He cores, degenerate Fe cores).
- **Isothermal degenerate core:** highly efficient electron conduction (Pauli-blocked scattering → long mean free paths) flattens the temperature profile in the interior.
- **Degenerate/non-degenerate border:** the radius ($r/R_\mathrm{WD}\approx0.97$) where $T/\rho^{2/3}=D$ exactly; core temperature $T_c$ holds there since the core is isothermal.
- **Mestel cooling law (1952):** WD cooling model where luminosity is drawn purely from ionic thermal energy, giving $L\propto t^{-7/5}$ at late times.
- **Crystallisation:** CO ions form an ordered lattice as $T_c$ drops, releasing latent heat and producing a luminosity plateau in cooling curves.
- **WD luminosity function (WDLF):** number density of WDs vs. luminosity; its faint-end cutoff is used as a cosmic chronometer, though less precise than main-sequence turnoff (MS-TO) dating.
- **Slowly cooling WDs (Chen et al. 2021):** WDs with residual H-layer above $10^{-4}M_\mathrm{WD}$ that sustain stable H-burning, cooling more slowly than canonical models predict; linked to blue Horizontal Branch (E-HB) progenitors that skip the AGB and Third Dredge-Up.

## 2. Key Equations

- Surface gravity: $g = GM/R^2$ — governs binding of surface layers; drops ~5 orders of magnitude from MS to RGB, driving mass loss.
- General mass-loss scaling: $\dot M \propto LR/M$ — mass loss favoured by high luminosity, large radius, low mass.
- Reimers law: $\dot M = -4\times10^{-13}\eta\,L/(gR)\ [M_\odot\,\mathrm{yr}^{-1}]$ — empirical RGB/AGB mass-loss rate.
- Stefan-Boltzmann: $L = 4\pi\sigma R^2T^4$ — used to show post-AGB contraction at constant $L$ raises $T$, and (with $R$=const) gives WD cooling tracks slope 4 in $\log L$–$\log T_e$.
- Degeneracy condition: $T/\rho^{2/3} < D=1.3\times10^5$ (T in K, $\rho$ in g cm$^{-3}$) — tests whether a plasma is electron-degenerate.
- Electron number density: $n_e = (Z/A)\,\rho/m_H$ — used throughout degenerate-pressure derivations.
- Non-relativistic degenerate pressure: $P \sim \tfrac{1}{3}(\hbar^2/m_e)[(Z/A)\rho/m_H]^{5/3}$, exact form with $(3\pi^2)^{2/3}/5$ — valid while electrons are non-relativistic; $P\propto\rho^{5/3}$, $T$-independent (why WDs cool at constant $R$).
- Non-relativistic mass-radius relation: $M^{1/3}R \sim 3\times10^{19}$ [cgs] — more massive WD → smaller radius; breaks down once electrons go relativistic ($v\sim c/3$ at $\rho=10^6\,\mathrm{g\,cm^{-3}}$).
- Relativistic degenerate pressure: $P = \dfrac{(3\pi^2)^{1/3}}{4}\hbar c\,[(Z/A)\rho/m_H]^{4/3}$ — applies once electrons are ultra-relativistic; $P\propto\rho^{4/3}$.
- Chandrasekhar mass: $M_\mathrm{Ch} = \dfrac{3\sqrt{2\pi}}{8}(\hbar c/G)^{3/2}[(Z/A)/m_H]^2 = 1.44\,(1+X)^2\,M_\odot$ — the unique fixed mass where relativistic degenerate pressure balances gravity; no equilibrium above it.
- Luminosity-central temperature relation: $L = c\,T_c^{7/2}$, with $c = 7.3\times10^5\,(M_\mathrm{WD}/M_\odot)\,\mu/[Z(1+X)]$ — links observable $L$ to core temperature via the thin non-degenerate envelope (Kramers opacity).
- Thermal energy reservoir: $U = (M_\mathrm{WD}/Am_H)\,\tfrac{3}{2}kT_c$ — the sole energy source for WD luminosity ($\approx 2.5\times10^{47}$ erg for $1M_\odot$ at $T_c=10^7$K).
- Mestel cooling law: $L_\mathrm{WD}(t) = L_0\,[1+\tfrac{5}{2}t/\tau_0]^{-7/5}$, with $\tau_0=B/(cT_0^{5/2})$ — predicts $L\propto t^{-7/5}$ at late times, near-linear decline early on.
- Cooling-time formula: $t_\mathrm{cool} = 8.8\times10^6\,(M/M_\odot)^{5/7}(L/L_\odot)^{-5/7}$ yr (canonical CO, $A=12,\mu=2$) — more massive WDs take longer to cool to a given $L$.
- Density-mass relation: $\rho \propto M^2$ — small mass increase (e.g. accretion) drives a large density increase; key to Type Ia SN ignition as $M\to M_\mathrm{Ch}$.

## 3. Key Algorithms / Procedures

1. **Deriving degenerate electron pressure (order-of-magnitude):** get $n_e$ from composition and density → get momentum $p$ from Heisenberg uncertainty ($\Delta x\sim n_e^{-1/3}$) → get velocity $v=p/m_e$ (non-rel.) or $v=c$ (rel.) → combine via $P\sim\tfrac13 n_e pv$.
2. **Deriving the mass-radius relation / Chandrasekhar mass:** equate degenerate pressure to the virial/hydrostatic estimate $\tfrac23\pi G\rho^2R^2$ → substitute uniform-density $\rho=M/(\tfrac43\pi R^3)$ → in the non-relativistic case $R$-powers leave a residual $R^{-1}$ dependence (gives $M^{1/3}R=$const); in the relativistic case all $R$-dependence cancels (gives a fixed $M=M_\mathrm{Ch}$, no free radius).
3. **Deriving $L=cT_c^{7/2}$:** combine hydrostatic equilibrium and radiative gradient in the non-degenerate envelope → substitute Kramers opacity $\kappa=\kappa_0\rho T^{-3.5}$ and ideal-gas EOS → integrate from surface ($P\approx0$) to the degenerate border → impose $T=T_c$ and $T/\rho^{2/3}=D$ at that border → solve for $L$.
4. **Deriving the Mestel law:** equate envelope luminosity $L=cT_c^{7/2}$ to reservoir depletion $L=-B\,dT_c/dt$ → separate variables and integrate from $T_0$ at $t=0$ → obtain $T_c(t)$ then $L(t)$.
5. **WD chronometry method:** observe cluster/field WD population → build the WD luminosity function (WDLF) → identify the faint-end cutoff (oldest WDs) → convert cutoff luminosity to age via the Mestel/cooling-time formula.
6. **Testing for slow-cooling WDs (Chen et al. 2021 logic):** compare "twin" clusters of identical age/metallicity but different HB morphology → excess of bright WDs in the blue-HB cluster → attribute to AGB-skipping (E-HB) progenitors retaining $M_H>10^{-4}M_\mathrm{WD}$ → confirm via lower $N_\mathrm{AGB}/N_\mathrm{HB}$ ratio and via cooling models mixing standard + H-burning WDs to fit the observed WDLF.

## 4. Watch Out For

- $M_\mathrm{Ch}=1.44\,M_\odot$ is **not** the initial stellar mass — it is the mass of the electron-degenerate substructure only (applies equally to CO WDs, He WDs, and degenerate Fe cores in massive stars).
- Degenerate pressure is temperature-independent — this, not "no fuel," is the reason cooling occurs at constant radius (no structural adjustment when $T$ drops).
- Non-relativistic $M^{1/3}R=$const cannot be extrapolated to high mass; electrons become relativistic ($v\sim c/3$ already at $\rho=10^6\,\mathrm{g\,cm^{-3}}$), forcing the switch to $P\propto\rho^{4/3}$.
- At the Chandrasekhar limit the idealised $R\to0$; real physics intervenes via inverse beta decay/neutronisation before that, leading to a neutron star or (if via accretion) a Type Ia SN — not a literal point object.
- $T_c$ in the Mestel law is the **central**, not surface, temperature; the link to observable $T_\mathrm{eff}$ runs through the thin non-degenerate envelope only.
- Counterintuitive result: at **fixed age**, more massive WDs are **more luminous** (they cool slower, larger reservoir) — opposite of the fixed-$T_e$ comparison where more massive WDs are less luminous (smaller radius).
- The theoretical HR-diagram cooling track is a straight line, but the **observational CMD** shows a kink near $T_e\approx10{,}000$K from the H ionisation/opacity transition — not a real change in cooling physics.
- WD chronometry is systematically biased young if slow-cooling WDs (thick residual H, blue-HB progenitors) are present and uncorrected; the technique remains less precise than MS-TO dating even in ideal cases.
- $\rho\propto M^2$ means even small accreted mass causes a large density jump — the physical trigger connecting WD accretion to Type Ia SN ignition near $M_\mathrm{Ch}$.
- Only ~80% of WDs are DA (H atmosphere) despite virtually all retaining some H layer initially — gravitational settling, not composition alone, explains the spectral-type distribution.
