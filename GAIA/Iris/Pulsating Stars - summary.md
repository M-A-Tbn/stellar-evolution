# Pulsating Stars — Summary

## 1. Key Concepts

- **Pulsating star:** intrinsic periodic oscillation of stellar radius $R$ and effective temperature $T_e$, producing a periodic luminosity/light curve (not caused by eclipses).
- **Instability Strip:** near-vertical band in the HRD ($T_{\rm eff}\approx6300$–$7100$ K, $\delta T\sim600$–$1000$ K) where pulsation occurs; pulsation is a transient phase, not a permanent property.
- **Cepheids ($\delta$ Cephei prototype):** Population I radial pulsators, periods 1–50 days; historically the first-studied class.
- **Light curve:** periodic apparent-magnitude variation; classical Cepheids show fast rise, slow decline.
- **Leavitt's discovery / Period–Luminosity (P-L) relation:** more luminous Cepheids have longer periods (found using the SMC's common distance).
- **Cosmic Distance Ladder:** the P-L relation is its first rung — all extragalactic distances trace back to it.
- **Radial pulsation (Shapley 1914, mechanism by Eddington, zones by Zhevakin):** whole-star expansion/contraction; $R$ and $T_e$ vary in **anti-phase** (adiabatic heating/cooling).
- **Phase Lag:** observed delay — maximum luminosity occurs slightly *after* minimum radius, not simultaneously.
- **Pulsating star classes** (Table 14.1): LPVs, Classical Cepheids, W Virginis (Pop II Cepheid analogs), RR Lyrae (Pop II, HB), $\delta$ Scuti (MS, radial+non-radial), $\beta$ Cephei, ZZ Ceti (WD, non-radial).
- **Strip crossings:** 1st (post-MS expansion, fast), 2nd (He-burning/HB, slow — dominant source of observed pulsators), 3rd (toward AGB, fast).
- **RR Lyrae as standard candles:** near-constant HB luminosity ($M_V\approx+0.5$) regardless of period.
- **HB morphology / "second parameter" problem:** metallicity, He abundance, age, mass loss set whether a cluster's HB crosses the strip (hosts RR Lyrae) or lies entirely red/blue of it.
- **Standing acoustic wave modes:** fundamental (no interior node), first overtone (1 node), second overtone (2 nodes) — pipe-with-closed-center analogy; higher overtones = shorter period.
- **Period–Density relation:** $\Pi\propto\rho^{-1/2}$ — the physical root of the P-L relation.
- **Eddington valve / Carnot-engine analogy:** a driving layer must convert heat into mechanical work like a heat engine (clockwise P–V loop = driving).
- **$\kappa$-mechanism (Zhevakin):** in partially ionized zones, opacity rises on compression (opposite of Kramers' law), trapping/releasing heat in the right phase to drive oscillations.
- **$\gamma$-mechanism:** secondary driving effect — ionization absorbs energy, suppressing $\delta T$, encouraging extra heat inflow.
- **He II ionization zone ($T\approx4\times10^4$K):** the real "piston" driving pulsation.
- **H ionization zone ($T\approx1.5\times10^4$K):** does not drive strongly but produces the Phase Lag.
- **Blue edge / Red edge:** strip boundaries from two distinct causes — too little overlying mass (blue) vs. convective damping (red).
- **One-zone model:** toy model (all mass at center, thin shell) used to derive the dynamical-stability condition.
- **Dynamical stability condition:** oscillation requires $\gamma>4/3$.
- **Period–Luminosity–Color (PLC) relation:** the more fundamental relation; the simple PL relation is the PLC evaluated at mean Cepheid color.

## 2. Key Equations

- Stefan–Boltzmann (why $L$ varies): $$L=4\pi R^2\sigma T_e^4$$
- P-L relation (empirical, standard candle use): $$M_V=-2.8\log P_{\rm days}-1.43$$
- Distance modulus: $$(m-M)_V=\langle V\rangle-M_V,\qquad (m-M)_0=5\log d-5$$
- Pulsation period as acoustic crossing time: $$\Pi=2\int_0^R\frac{dr}{v_s}$$
- Adiabatic sound speed: $$v_s=\sqrt{\gamma P/\rho}$$ (from $B=-V(\partial P/\partial V)_{ad}=\gamma P$)
- Hydrostatic pressure in a uniform-density star: $$P(r)=\tfrac{2}{3}\pi G\rho^2(R^2-r^2)$$
- **Boxed period–density result** (from acoustic derivation): $$\Pi\approx\sqrt{\dfrac{3\pi}{2\gamma G\rho}}\ \Rightarrow\ \Pi\propto\rho^{-1/2}$$
- One-zone linearized equation of motion (SHM): $$\ddot{(\delta R)}=-(3\gamma-4)\dfrac{GM}{R_0^3}\delta R,\qquad \omega^2=(3\gamma-4)\dfrac{GM}{R_0^3}$$
- One-zone period (equivalent form): $$\boxed{P=\dfrac{2\pi}{\sqrt{\tfrac{4\pi}{3}G\rho_0}}}$$ — real oscillation requires $\omega^2>0\Rightarrow\gamma>4/3$.
- Period in terms of $M,L,T_{\rm eff}$: $$\boxed{\log P=-\tfrac12\log M+\tfrac34\log L-3\log T_{\rm eff}+c}$$
- Final PLC relations (period depends on **both** magnitude and color): $$\boxed{\log P=-0.239M_V+0.602(B-V)-0.456}$$ $$\boxed{M_V=-3.53\log P_{\rm days}-2.13+2.13(B-V)}$$

## 3. Key Algorithms / Procedures

1. **Cepheid distance determination:**
   1. From the light curve, measure period $P$ and mean apparent magnitude $\langle V\rangle$.
   2. Get $M_V$ from the P-L relation using $P$.
   3. Compute distance modulus $(m-M)_V=\langle V\rangle-M_V$ (correct for reddening if present), then solve $5\log d-5=(m-M)_0$ for $d$.
2. **Period–density derivation (acoustic wave method):** compute $v_s(r)$ from adiabatic sound speed → get $P(r)$ from hydrostatic equilibrium (uniform $\rho$) → substitute into $\Pi=2\int dr/v_s$ → integrate (substitution $x=r/R$, $\int_0^1 dx/\sqrt{1-x^2}=\pi/2$) → obtain $\Pi\propto\rho^{-1/2}$.
3. **$\kappa$-mechanism driving cycle (per partially ionized layer):** compression → temperature rise diverted into ionization → opacity increases → energy trapped; expansion → recombination releases stored energy → opacity drops → energy escapes. Net effect: heat absorbed when hot, released when cold → positive work → driving.
4. **PLC derivation chain:** period–density relation → substitute $\rho\propto M/R^3$ → eliminate $R$ via Stefan–Boltzmann → eliminate $M$ via the ZAMS mass–luminosity relation (shifted +1 mag for He-burning stage) → convert $M_{\rm bol}$ to $M_V,(B-V)$ via bolometric correction and $T_e$–color calibration → final PLC relation.

## 4. Watch Out For

- Luminosity variation is driven **mainly by $T_e^4$, not $R^2$** — radius changes only ~10%, but this is a common source of confused reasoning.
- Maximum luminosity coincides with maximum $T_e$ and **minimum radius** — but maximum *observed* luminosity lags slightly behind minimum radius (Phase Lag), caused by the **H-ionization zone**, not the He zone.
- Don't confuse the driving layer (**He II zone = piston**) with the phase-lag layer (**H zone**) — removing He II kills pulsation entirely; removing H just removes the phase lag.
- Kramers' opacity ($\kappa\propto\rho/T^{3.5}$) is normally **damping** (opacity drops when compressed/hot) — the $\kappa$-mechanism only works because partially ionized zones reverse this trend.
- Instability strip edges have **two different physical causes**: blue edge = ionization zones too shallow (mass problem), red edge = convection damping — do not attribute both edges to the same mechanism.
- Dynamical stability requires $\gamma>4/3$; if radiation pressure or ionization pushes $\gamma$ toward or below $4/3$, the star becomes unstable (collapse/explosion) rather than oscillatory.
- The "P-L relation" is an approximation of the more fundamental **P-L-Color (PLC) relation** — scatter in the classic PL diagram is largely due to ignoring color/metallicity differences.
- RR Lyrae work as standard candles because they share nearly the same HB luminosity — this only holds because they're all in the same evolutionary stage (core He-burning), not a universal property of pulsators.
- Whether a cluster hosts RR Lyrae depends on **HB morphology** (metallicity and He abundance shift HB stars red or blue of the strip) — a purely evolutionary/compositional effect, unrelated to the pulsation mechanism itself.
- Most Cepheids/RR Lyrae observed are in the **second (He-burning) strip crossing** because it is much slower than the first and third crossings — not because it's the only crossing that exists.
- Classical Cepheids and W Virginis pulsate in the **fundamental mode**; RR Lyrae can pulsate in fundamental, first overtone, or both (double-mode/beat) — know which classes allow overtone pulsation.
