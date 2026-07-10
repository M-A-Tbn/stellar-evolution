# Introduction — Summary

---

## 1. Key Concepts

- **Stellar evolution (course aim):** identify the physical processes producing structural changes in stars of different mass/composition over time; mechanistic, not descriptive.
- **Contraction vs. collapse:** "contraction" = change on the Kelvin–Helmholtz (thermal) timescale; "collapse" = change on the dynamical timescale.
- **H-R Diagram:** plot of $\log(L/L_\odot)$ (vertical) vs $\log T_e$ (horizontal, **increasing to the left**); one stellar model = one point; a star's life = an **evolutionary track**.
- **Chemical composition** $(X,Y,Z)$: hydrogen, helium, metal mass fractions, $X+Y+Z=1$. Solar: $X=0.70, Y=0.28, Z=0.02$.
- **Seven equations of stellar structure:** hydrostatic equilibrium, mass continuity, equation of state, energy source, radiative gradient/Schwarzschild criterion, opacity, thermonuclear energy production — solved vs. $r$ to yield $(L, T_e)$.
- **Hydrostatic equilibrium:** gravity balanced by pressure gradient at every layer, star neither collapses nor explodes.
- **Mean molecular weight $\mu$:** average particle mass (in units of $m_p$) in ionized gas; depends on $X,Y,Z$.
- **Thermoregulation:** negative feedback ($T\uparrow \Rightarrow P\uparrow \Rightarrow$ expansion $\Rightarrow T\downarrow$) that stabilizes normal (perfect) gas burning.
- **Electron degeneracy:** low-energy quantum states fully occupied (Pauli exclusion); pressure becomes density-only, destroying thermoregulation. Only electrons degenerate in practice (protons never do).
- **Thermonuclear runaway:** ignition in degenerate gas with no thermoregulation → explosive burning (e.g., helium flash).
- **Virial Theorem:** $2K+\Omega=0$ for hydrostatic equilibrium; underlies the "negative heat capacity" of self-gravitating gas (energy loss → contraction → heating).
- **Kelvin–Helmholtz timescale $t_{KH}$:** time gravitational contraction alone can power a star's luminosity; too short (∼15 Myr for Sun) to explain stellar ages ⇒ fusion is needed.
- **Convection:** bulk gas motion; a **mixing** process homogenizing composition; triggered when a displaced adiabatic gas parcel is buoyant relative to surroundings (Schwarzschild criterion).
- **Nabla ($\nabla$):** logarithmic temperature gradient $d\log T/d\log P$; $\nabla_\text{ad}=0.4$ for monatomic ideal gas ($\gamma=5/3$).
- **Opacity $\kappa$:** resistance of matter to radiation flow (cm$^2$ g$^{-1}$); four processes — bound-bound, bound-free, free-free, electron scattering — dominate in different regions/temperatures.
- **Kramers' laws:** analytic opacity approximations, $\kappa_{BF},\kappa_{FF}\propto \rho T^{-3.5}$; $\kappa_E$ = constant floor at high $T$.
- **He second-ionization opacity hump** ($T\sim40{,}000$ K): triggers stellar outer convection zones.
- **Binding energy $E_B$:** energy to fully disassemble a nucleus; peaks near $A\approx56$ (iron group) ⇒ fusion only releases energy up to iron.
- **Coulomb barrier / tunneling:** nuclei must quantum-tunnel through electrostatic repulsion to fuse at stellar (not classical) temperatures.
- **PP chains:** dominant H-burning at lower $T$; rate-limited by $p+p\to d+e^++\nu$ ($\beta^+$ inside collision, extremely slow, $t_{1/2}\sim1.4\times10^9$ yr) — sets the Sun's long lifetime.
- **CNO cycle:** catalytic H-burning using pre-existing C,N,O; steeper $T$-dependence than PP; dominates in hotter (more massive) cores; concentrates energy generation, driving core convection; N-14 accumulates (slow branch bottleneck).
- **Triple-alpha process:** He-burning via unstable Be$^8$ intermediate + Hoyle resonance in C$^{12}$; requires the Hoyle state to make carbon at all.
- **Advanced burning (C, Ne, O, Si):** sequential fusion stages in non-degenerate massive-star cores at increasing $T$; Si-burning is photodisintegration-driven, builds iron-group nuclei.
- **Alpha elements:** O, Ne, Mg, Si, S, Ar, Ca — built by alpha-capture; [α/Fe] traces core-collapse vs Type Ia SN enrichment history.
- **s-process / r-process:** neutron capture beyond iron; s = slow (capture < β⁻ decay rate, valley of stability); r = rapid (multiple captures before decay, produces neutron-rich isotopes, needs explosive neutron flux).
- **Photo-disintegration:** endothermic breakup of nuclei by energetic gammas; triggers iron-core collapse in massive stars.
- **Neutrino losses (plasma, photoneutrino, pair-annihilation):** bypass radiative diffusion, dramatically shorten advanced burning stages.
- **Effective temperature $T_e$:** temperature of the atmosphere layer at optical depth $\tau_v=2/3$ — the "surface temperature" plotted on the H-R diagram.
- **Optical depth $\tau_\lambda$:** dimensionless measure of atmosphere opacity along the line of sight; photons emerge from $\tau\approx1$.
- **Photosphere:** thin layer ($\tau\approx2/3\to0$) where continuum and absorption lines form.
- **Saha equation:** governs ionization equilibrium between successive ionization states as a function of $T$ and $P_e$.
- **Boltzmann equation:** governs the fractional population of excited levels within an ionization state as a function of $T$.
- **Spectral classification (O–M):** driven by $T$ via ionization/excitation state, from highly ionized (O) to molecular bands (M).
- **Equivalent width $W$:** measure of absorption line strength; proportional to the number of "active" absorbing atoms $N_a$.
- **Curve of growth:** relation of $\log W$ to $\log N_a$; linear → saturated (flat) → square-root (damping) regimes.
- **Square bracket notation [El/H]:** double-normalized (to H, then to solar) logarithmic abundance ratio; [Fe/H] is the standard metallicity proxy.
- **Helium Problem:** observed primordial $Y\approx0.24$ in oldest stars far exceeds what stellar nucleosynthesis alone could have produced by now.
- **Big Bang Nucleosynthesis (BBN):** early-universe production of most primordial He (and traces of Li/Be) using freely available neutrons before they decay.
- **A=5, A=8 bottleneck:** absence of stable nuclei at these mass numbers halts primordial nucleosynthesis at helium; stars bypass it via the triple-alpha process (transient Be$^8$ equilibrium + Hoyle resonance).

## 2. Key Equations

$$\frac{dP(r)}{dr} = -\frac{GM(r)}{r^2}\rho(r)$$
Hydrostatic equilibrium: pressure gradient balances gravity at every radius; always $<0$.

$$\frac{dM(r)}{dr} = 4\pi r^2 \rho(r)$$
Mass continuity: rate of enclosed-mass growth with radius from the density profile.

$$P = P_\text{rad}+P_\text{gas},\quad P_\text{rad}=\frac{aT^4}{3},\quad P_\text{gas}=\frac{k\rho T}{\mu H}$$
Equation of state; radiation pressure negligible except in very massive stars.

$$\mu = \frac{1}{2X+\frac34 Y+\frac12 Z}$$
Mean molecular weight of fully ionized gas from composition (solar $\mu\approx0.617$).

$$\frac{T}{\rho^{2/3}} < 10^5 \ \text{(electrons)}; \quad \frac{T}{\rho^{2/3}}<\frac{2.4\times10^{-22}}{m}\ \text{(general species)}$$
Electron-degeneracy onset condition; lighter particles degenerate more easily.

$$P=k_1\rho^{5/3}\ (\text{non-rel. degenerate}),\quad P=k_2\rho^{4/3}\ (\text{rel. degenerate})$$
Degenerate electron pressure — density-only, no thermoregulation.

$$\frac{dL(r)}{dr}=4\pi r^2\rho(r)\,\epsilon$$
Energy (luminosity) conservation with local generation rate $\epsilon$.

$$2K+\Omega=0;\quad U=\frac{\Omega}{2}<0$$
Virial theorem; contraction releases energy, half heats the gas, half is radiated.

$$t_{KH}=\frac{1}{2}\frac{GM^2}{LR}$$
Kelvin–Helmholtz timescale — max duration gravity alone can power luminosity (Sun: ~15 Myr).

$$\left.\frac{dT}{dr}\right|_\text{rad}=-\frac{3\kappa\rho}{4ac}\frac{L(r)}{4\pi r^2 T^3}$$
Radiative temperature gradient needed to carry flux $L(r)$ by photon diffusion.

$$\nabla\equiv\frac{d\log T}{d\log P};\qquad \nabla_\text{ad}=\frac{\gamma-1}{\gamma}=0.4\ \text{(monatomic gas)}$$
Schwarzschild criterion in log form: $\nabla_\text{rad}>\nabla_\text{ad}\Rightarrow$ convection.

$$\kappa_{BF}\propto Z(1+X)\rho T^{-3.5};\quad \kappa_{FF}\propto(X+Y)(1+X)\rho T^{-3.5};\quad \kappa_E\propto0.2(1+X)$$
Kramers opacity laws for bound-free, free-free, electron scattering.

$$E_B(Z,A)=\{Zm_p+(A-Z)m_n-m_\text{nucl}\}c^2$$
Nuclear binding energy from the mass deficit; per-nucleon curve peaks at $A\approx56$ (iron).

$$4\text{H}^1\to\text{He}^4+2e^++2\nu_e\ (+26.2\ \text{MeV, PP-I})$$
Net hydrogen-burning reaction via PP chains.

$$\epsilon_{pp}=\epsilon_1\rho X^2T_6^{3.5-6};\quad \epsilon_{CN}=\epsilon_2\rho X X_{CN}T_6^{13-20};\quad \epsilon_{3\alpha}=\epsilon_3\rho^2Y^3T_8^{20-30}$$
Approximate energy-generation-rate formulae; steep $T$ exponents drive core convection and instability under degeneracy.

$$T^4=\frac{3}{4}T_e^4\left(\tau_v+\frac{2}{3}\right)$$
Atmosphere temperature–optical-depth relation; defines $T_e$ at $\tau_v=2/3$.

$$\log\frac{N_{j+1}}{N_j}=-0.176-\log P_e+\log\frac{U_{j+1}(T)}{U_j(T)}+2.5\log T-\frac{5040}{T}\chi_i$$
Saha equation: ionization-state ratio vs. $T$ and $P_e$.

$$\frac{N_{ji}}{N_j}=\frac{g_i}{U_j(T)}10^{-\chi_i(5040/T)}$$
Boltzmann equation: excited-level population fraction vs. $T$.

$$\frac{\Delta\lambda}{\lambda_0}=\frac{v_r}{c}$$
Doppler shift → radial velocity from spectral line displacement.

$$W=\int\frac{F_c-F_\lambda}{F_c}\,d\lambda$$
Equivalent width — integrated absorption-line strength, proportional to active absorber count $N_a$.

$$\left[\frac{El}{\text{H}}\right]=\log\left(\frac{El}{\text{H}}\right)_*-\log\left(\frac{El}{\text{H}}\right)_\odot$$
Square-bracket abundance notation relative to solar (e.g. [Fe/H] = metallicity proxy).

## 3. Key Algorithms / Procedures

1. **Building one H-R point from a stellar model:** (1) fix inputs $M$ and $(X,Y,Z)$; (2) solve the seven coupled structure equations plus EOS as functions of $r$; (3) read off output $L$ and $T_e$; (4) plot as one point on the H-R diagram.
2. **Evolving a track over time:** at each timestep, update composition (nuclear burning changes $X,Y$ locally) → re-solve the seven equations with new composition → obtain new $(L,T_e)$ → repeat to trace the evolutionary track.
3. **Schwarzschild convection test at a given layer:** (1) compute $\nabla_\text{rad}$ from opacity, flux, $T$, $P$; (2) compute $\nabla_\text{ad}$ (0.4 for ideal monatomic gas); (3) if $\nabla_\text{rad}>\nabla_\text{ad}$, mark the layer convective (mixing occurs); else radiative.
4. **Determining stellar-core gas regime:** compute $T/\rho^{2/3}$; compare to $10^5$ (electrons) using the log $T$–log $\rho$ diagram to identify radiation-, perfect-gas-, or degeneracy-dominated pressure law, then select the correct EOS term.
5. **Deriving chemical abundance [El/H] from a spectrum:** (1) measure equivalent width $W$; (2) enter curve of growth to get $\log N_a$; (3) apply Boltzmann correction (excitation) to get $N_j$; (4) apply Saha correction (ionization) to get $N_\text{TOT}$; (5) convert to mass per area; (6) normalize to H and to solar ratio to get [El/H].
6. **Neutron-capture nucleosynthesis path:** determine if neutron-capture rate exceeds or is exceeded by β⁻ decay rate of the produced isotope → classify as r-process (multiple captures, then decay back to stability) or s-process (single capture, decay before next capture, walks the valley of stability).

## 4. Watch Out For

- Temperature axis on the H-R diagram increases **leftward** — a constant trap for mislabeling hot/cool sides.
- "Contraction" (KH timescale) vs. "collapse" (dynamical timescale) is a precise vocabulary distinction the exam explicitly tests.
- Only **electrons** degenerate under normal stellar conditions in this course — proton degeneracy boundary lies deep in the relativistic-electron-degenerate region and is never physically reached.
- Degenerate pressure depends on $\rho$ **only**, not $T$ — this is *why* thermoregulation fails, not just a formula to memorize.
- Ionic (proton/alpha) component of the EOS is **always** a perfect gas, even when electrons are degenerate.
- PP chain's rate-limiting step is a $\beta^+$ decay that is essentially impossible for a free proton but occurs with tiny probability inside a two-proton collision — don't confuse with free-neutron $\beta^-$ decay (fast, ~13 min half-life).
- CNO cycle does **not** create C, N, O — it only catalyzes; net effect over time is N-14 accumulation (slow branch bottleneck), not net CNO production.
- Triple-alpha absolutely depends on the Hoyle resonance in C$^{12}$ — without this fine-tuned nuclear coincidence, carbon (and life) would not form.
- Fusion **cannot** proceed past iron for energy gain; elements beyond Fe come only from neutron capture (s/r-process), never fusion.
- A=5 and A=8 have no stable nuclei — this, not lack of time or temperature, is why BBN stopped at He (with only trace Li/Be), while stars circumvent it via a transient Be$^8$ equilibrium population at higher $T,\rho$.
- Radiation pressure is negligible in most stars/stages but becomes significant in the most massive stars (Eddington limit) — don't assume it is always ignorable.
- The helium hump at $T\sim40{,}000$ K is a deviation from the Kramers $T^{-3.5}$ opacity trend, not part of it — it is caused by He$^+\to$He$^{2+}$ second ionization and can trigger convection zones.
- Convection is triggered by **either** high opacity or high energy flux — two independent physical routes to the same instability, not one mechanism.
- Effective temperature $T_e$ is defined at $\tau_v=2/3$, not at $\tau=0$ or $\tau=1$ — a precise, testable detail.
- Equivalent width $W$ tracks only "active" absorbing atoms $N_a$ (correct ionization + excitation state), not the total elemental abundance — Saha and Boltzmann corrections are both required to get $N_\text{TOT}$.
- The curve of growth has three distinct regimes (linear, flat/saturated, square-root/damping) with different $W$–$N_a$ scaling — using the wrong regime's relation gives wrong abundances.
- Neutrino losses are negligible for the Sun but dominate and *drastically accelerate* advanced burning stages (silicon burning can finish in days) — a major asymmetry in stellar-lifetime intuition.
- Kelvin–Helmholtz timescale is not obsolete once nuclear burning is understood — it remains the operative timescale during pre-main-sequence contraction and other nuclear-burning gaps.
