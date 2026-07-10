# Pre-Main Sequence Evolution — Summary

## 1. Key Concepts

- **Stellar evolution**: the macroscopic (not nuclear-microscopic) variation of a star's observable properties (L, T_e, R) with time.
- **H-R diagram**: plot of L vs. T_e; convention: log T_e axis increases **to the left** (hot on left).
- **Evolutionary track**: path of one star (fixed mass) through the H-R diagram over its entire life.
- **Isochrone**: curve connecting equal-age points across many different-mass tracks; what an observer sees in a real cluster.
- **Dynamical (free-fall) timescale** τ_d: set by gravity alone, pressure negligible; fastest regime.
- **Kelvin-Helmholtz (thermodynamic) timescale** τ_KH: virialized contraction, star shines on gravitational energy alone.
- **Thermonuclear timescale** τ_nuc: set by fuel supply at observed L; longest regime, defines the main-sequence lifetime.
- **Virial Theorem**: for a self-gravitating, quasi-static gas, 2K + Ω = 0; implies negative heat capacity (losing energy heats the gas).
- **Jeans mass/criterion**: minimum cloud mass at given (T, ρ) for gravity to overcome thermal pressure and collapse.
- **Initial Mass Function (IMF)**: mass spectrum of stars formed from a fragmenting cloud; Salpeter power law for M ≳ 1 M☉.
- **Points A, B, C, E**: landmark states of pre-MS collapse — A (initial cloud), B (core reaches HE, envelope still infalling), C (shock-driven luminosity peak), E (whole star first fully in hydrostatic equilibrium).
- **Hayashi track**: locus of models (fixed mass, composition) that are simultaneously in hydrostatic equilibrium and fully convective.
- **Hayashi Theorem**: no stable hydrostatic model can exist to the right (cooler) of the Hayashi track, at any evolutionary stage.
- **Schwarzschild criterion**: convective instability when ∇_rad > ∇_ad.
- **Kramers opacity law**: κ ∝ ρ/T^3.5 — opacity falls steeply as core heats, enabling the core to eventually turn radiative.
- **Points 1/2/3**: mass-dependent points where a track departs the Hayashi track (high/intermediate/low mass respectively); **Point 2** also marks first partial pp/CNO ignition; **Point 5**: nuclear energy overtakes gravity as the dominant power source.
- **Perfect-gas thermostat**: negative feedback — extra nuclear energy expands and cools the core, throttling the reaction rate; basis of MS stability.
- **ZAMS**: locus where ³He+³He fully activates, closing the pp chain, L_g/L = 0, full thermal + hydrostatic equilibrium.
- **Electron degeneracy branching point**: after He-burning, cores of M < 8 M☉ become degenerate (→ white dwarf); M > 8 M☉ stay non-degenerate (→ core-collapse SN).

## 2. Key Equations

- $L = 4\pi R^2\sigma T_e^4$ — Stefan-Boltzmann law; defines constant-radius diagonals on the H-R diagram.
- $T_d = \sqrt{2r^3/GM} = 2600/\sqrt{\bar\rho}\ \text{s}$ (ρ in g/cm³) — free-fall/dynamical timescale; denser → faster collapse.
- $2K+\Omega=0$ (Virial Theorem); $U=K+\Omega=\Omega/2<0$; contraction ($d\Omega<0$) gives $dK=-d\Omega/2>0$ and $dU=d\Omega/2<0$ — half of released gravitational energy heats the star, half is radiated.
- $L=|dU/dt|=\tfrac12|d\Omega/dt|$; integrating gives $t_{KH}=\dfrac{1}{2}\dfrac{GM^2}{LR}$ — time a star can shine on gravitational contraction alone (Sun: ~1.5×10⁷ yr, too short to explain Earth's age → motivates nuclear fusion).
- Collapse condition: $GMH/R \geq kT$ — gravitational binding energy per particle exceeds thermal energy per particle.
- Jeans mass: $M_J \geq 10^{23}\,T^{3/2}\rho^{-1/2}\ \text{g}$ (T in K, ρ in g/cm³) — clouds above $M_J$ collapse; explains why star formation favors cold, dense molecular clouds.
- IMF: $\Psi(M)=kM^{-s}$, Salpeter $s=2.35$ — number of stars formed per unit mass interval.
- $\kappa \propto \rho/T^{3.5}$ (Kramers) — governs both the Hayashi track's existence (high κ at low T forces full convection) and its departure (κ falls as T_c rises).
- $\left.\dfrac{dT}{dr}\right|_\text{rad} = -\dfrac{3\kappa\rho}{4\pi r^2}\dfrac{L(r)}{4acT^3}$ — radiative temperature gradient; steepens with κ, drives the Schwarzschild instability test $\nabla_\text{rad}>\nabla_\text{ad}$.
- $t_\text{PMS} \sim 4\times10^7 (M/M_\odot)^2 (R_\odot/R)(L_\odot/L)\ \text{yr}$ — pre-MS duration; the $M^2$ growth is overwhelmed by the steep rise of $L$ and $R$ with mass, so massive stars finish pre-MS fastest.
- ZAMS mass-luminosity relation $L\propto M^{3-4}$ ⟹ MS lifetime $\tau_\text{MS}\propto M/L \propto M^{-2\text{ to }-3}$ — basis of cluster age-dating via main-sequence turnoff.

## 3. Key Algorithms / Procedures

1. **Stellar model flow chart**: feed $[M,X,Y,Z]$ into the structure equations (hydrostatic equilibrium, mass continuity, energy generation, energy transport) → unique output $[L,T_e]$; at each timestep check (a) has the core gone degenerate, (b) is any region convectively unstable (Schwarzschild); update composition and repeat with $t=t+\Delta t$ to build an evolutionary track.
2. **Constructing an isochrone**: take evolutionary tracks for a range of masses formed at $t=0$; mark the point on each track tagged with the same age $t_0$; connect these points.
3. **Jeans stability test**: given cloud $(T,\rho)$, compute $M_J=10^{23}T^{3/2}\rho^{-1/2}$ g; cloud collapses only if its mass exceeds $M_J$.
4. **Pre-MS evolutionary sequence** (1 M☉ example): A (large cool cloud) → A–B free-fall, core reaches HE first (~10² yr) → B–C infalling envelope shocks the core, opacity drops, L spikes (~10 days) → C–E hydrostatic equilibrium propagates outward through envelope (~10⁵ yr) → E, fully convective, enters Hayashi track → descend Hayashi track via KH contraction (~10⁵–10⁶ yr) → core heats, κ falls, radiative core nucleates and grows, track bends left (Point 1/2/3 by mass) → partial pp/CNO ignition (Point 2) → nuclear luminosity overtakes gravity (Point 5) → core briefly expands/cools (perfect-gas thermostat) → ³He+³He fully activates → ZAMS ($L_g/L=0$).
5. **Post-He-burning fate test**: after He→C,O burning, check whether the next KH contraction drives $(\log\rho_c,\log T_c)$ into the degenerate region; if yes and $M<8\,M_\odot$ → white dwarf (staircase halts); if no and $M>8\,M_\odot$ → continue burning stages to Fe core → core-collapse supernova.

## 4. Watch Out For

- H-R diagram x-axis (log T_e) increases **leftward** — easy to misread tracks as running the wrong direction.
- A cluster's observed H-R diagram is always an **isochrone**, never a set of evolutionary tracks — the two look very different and are often confused.
- $t_{KH}$ is the time to *descend to* the main sequence, not the main-sequence lifetime — historically mistaken for the Sun's total age before nuclear fusion was discovered.
- Negative heat capacity is counterintuitive: a contracting self-gravitating gas gets **hotter** while **losing** total energy (half radiated, half retained as heat).
- The Jeans mass for typical cold ISM (~100 M☉) is far larger than a single star, so clouds must **fragment**; isolated field stars are cluster escapees, not the "natural" collapse product.
- The Hayashi Theorem is **universal** — it constrains red giants and all hydrostatic structures, not just pre-MS proto-stars.
- Model states relative to the Hayashi track: left = stable/partially convective, on = stable/fully convective, right = **no stable solution exists** (not just "unlikely").
- Departure point (1/2/3) ordering is mass-driven by *contraction speed* (τ_KH), not luminosity alone — more massive stars depart earlier and higher because they contract and heat faster.
- Point 2's partial pp/CNO reactions are **not** self-sustaining; only full activation of ³He+³He (the actual ZAMS criterion) closes the pp chain.
- Just before ZAMS, $\rho_c$, $T_c$, and even $L_g/L$ **dip** (briefly negative) due to core expansion — an easy point to mis-read as "contraction resuming" when it is actually the thermostat responding to new nuclear input.
- Pre-MS duration scales as $M^2 L^{-1}R^{-1}$: naive reasoning from the $M^2$ term alone gives the wrong trend (longer for massive stars); the dominant effect is that $L$ and $R$ grow faster with mass, making pre-MS **shorter** for massive stars.
- Final internal-structure convective zones at ZAMS split by mass: fully convective ($M\lesssim0.3\,M_\odot$), convective envelope + radiative core (~0.3–1.5 M☉), convective core + radiative envelope ($M\gtrsim1.5\,M_\odot$, driven by CNO's steep $T^{15}$ dependence) — do not assume one universal internal structure.
- The degeneracy branch point at $M=8\,M_\odot$ is the single most important fork in stellar fate (white dwarf vs. core-collapse supernova) — tie it explicitly to whether the post-He-burning core crosses into the degenerate regime.
