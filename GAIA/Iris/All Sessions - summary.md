# Stellar Evolution — Complete Course Summary

**Compiled from all 10 sessions of Apollo notes.** Compact exam-prep reference — definitions, equations, procedures, and traps only. Refer back to the full session notes for derivations and explanatory prose.

---

## 1. Key Concepts

### 1.1 Introduction

- **H-R Diagram**: plot of $\log(L/L_\odot)$ vs $\log T_e$; **temperature axis increases leftward**. A stellar model (fixed $M,X,Y,Z$) maps to exactly one point.
- **Evolutionary track**: sequence of H-R points as one star ages.
- **Stellar model inputs**: mass $M$ and composition $(X,Y,Z)$, $X+Y+Z=1$. Sun: $X=0.70,Y=0.28,Z=0.02$.
- **Seven equations of stellar structure**: hydrostatic equilibrium, mass continuity, equation of state, energy source, radiative/convective transport, opacity, thermonuclear energy production.
- **Mean molecular weight $\mu$**: average particle mass (in $m_H$) in the gas; rises as H→He.
- **Perfect-gas thermoregulation**: $T\!\uparrow\Rightarrow P\!\uparrow\Rightarrow$ expansion $\Rightarrow T\!\downarrow$ — stabilizes burning.
- **Electron degeneracy**: Pauli exclusion fills all low-energy states; pressure becomes $T$-independent, density-only. Breaks thermoregulation (→ thermonuclear runaway) and resists compression (→ WD/core stability).
- **Virial theorem** ($2K+\Omega=0$): contraction converts half the released gravitational energy to heat, half is radiated — "negative heat capacity."
- **Kelvin-Helmholtz timescale**: how long gravity alone can power a star's luminosity; too short to explain the Sun's age → proves fusion powers the MS.
- **Convection / Schwarzschild criterion**: convection when the actual (radiative) temperature gradient exceeds the adiabatic one; convection mixes/homogenizes composition.
- **Nabla ($\nabla$) formalism**: $\nabla=d\log T/d\log P$; $\nabla_{ad}=0.4$ for monatomic ideal gas.
- **Opacity $\kappa$**: resistance to radiative flow (cm² g⁻¹); four processes — bound-bound (spectral lines), bound-free (photoionization), free-free (inverse bremsstrahlung), electron scattering (Thomson).
- **Kramers opacity law**: $\kappa\propto\rho T^{-3.5}$; He-II ionization hump near $T\sim4\times10^4$ K can trigger convection.
- **Nuclear binding energy / mass deficit**: binding energy per nucleon peaks at Fe ($A\approx56$) — fusion releases energy only up to iron.
- **PP chain, CNO cycle**: two H-burning channels; CNO uses C,N,O as catalysts (does not create them), N-14 accumulates because it is the bottleneck.
- **Triple-alpha process**: He→C via unstable Be-8 intermediate and the Hoyle resonance in C-12.
- **Alpha-capture, neutron-capture (s- and r-process)**: build elements beyond iron; s-process = slow capture (valley of stability); r-process = rapid capture (neutron-rich, far from stability).
- **Effective temperature $T_e$**: temperature at optical depth $\tau_v=2/3$; this is what's plotted on the H-R diagram.
- **Saha equation / Boltzmann equation**: govern ionization state and excitation level as functions of $T$, underlying spectral classification (O,B,A,F,G,K,M).
- **Equivalent width, curve of growth**: measure absorption-line strength and relate it to absorber column density (linear, saturated, damping regimes).
- **[El/H] notation**: logarithmic abundance ratio relative to solar; used for metallicity.
- **Helium problem / Big Bang Nucleosynthesis (BBN)**: stellar burning cannot produce the observed primordial $Y_p\approx0.24$; resolved by BBN in the first ~15 minutes. A=5 and A=8 mass gaps stop BBN at He (no stable nuclei there).

### 1.2 Pre-Main Sequence Evolution

- **Isochrone vs evolutionary track**: track = one star's full history; isochrone = same-age snapshot across many masses (what a cluster CMD actually shows).
- **Three timescales**: dynamical (free-fall, fastest) → thermodynamic (Kelvin-Helmholtz) → thermonuclear (slowest, sets MS lifetime).
- **Jeans mass/criterion**: minimum cloud mass for gravitational collapse; $M_J\propto T^{3/2}\rho^{-1/2}$. Cold, dense molecular clouds have small $M_J$ → favored star-forming sites.
- **Collapse triggers**: SN shocks, cloud-cloud collisions, spiral-arm compression, galaxy interactions.
- **Initial Mass Function (IMF)**: Salpeter power law $\Psi(M)=kM^{-2.35}$ for $M\gtrsim1M_\odot$; sets final-fate ratios and chemical-enrichment weighting.
- **Three evolutionary stages**: pre-MS (cloud→ZAMS) → MS (core H-burning) → post-MS (shell burning → giant → remnant).
- **Point A→B→C→E**: free-fall collapse → shock/luminosity spike → progressive hydrostatic equilibrium; point E = fully convective, hydrostatic, on the Hayashi track.
- **Hayashi track**: locus of fully-convective, hydrostatic models at fixed mass; nearly vertical on the H-R diagram.
- **Hayashi theorem**: no stable hydrostatic model exists to the right (cooler) of the Hayashi track — universal, applies at all evolutionary stages, not just pre-MS.
- **Radiative core development**: as $T_c$ rises, $\kappa$ drops (Kramers), core becomes radiative, star departs the Hayashi track and bends leftward.
- **ZAMS**: locus where $^3$He+$^3$He fully activates the pp chain and $L_g/L=0$ (purely nuclear-powered); a one-parameter (mass) family at fixed composition.
- **Perfect-gas thermostat**: extra nuclear energy → core expands/cools → reaction rate self-regulates; the basis of MS stability.

### 1.3 Main Sequence Evolution

- **ZAMS mass range**: $0.08\,M_\odot$ (brown dwarf cutoff) to $\sim90\,M_\odot$ (Eddington-limited cutoff).
- **Eddington luminosity**: $L_{Ed}=4\pi GMc/\kappa$ — the maximum luminosity compatible with hydrostatic equilibrium.
- **Transition mass 1.2 $M_\odot$**: pp chain dominates below, CNO cycle dominates above (CNO is far more $T$-sensitive: $T^{15}$ vs $T^{5}$).
- **Three ZAMS structural regimes**: $M>1.2M_\odot$ convective core/radiative envelope; $0.3<M<1.2M_\odot$ radiative core/convective envelope; $M<0.3M_\odot$ fully convective.
- **CNO's four downstream effects**: sets convective cores, limits $T_c$ growth with mass (hence lower $\rho_c$ at high mass, avoiding degeneracy), flattens the mass–luminosity slope, and produces the post-MS "hook."
- **Metallicity/He effects on ZAMS**: higher $Z$ → fainter, cooler, longer-lived (higher turnoff mass at fixed age); higher $Y$ → brighter, hotter, shorter-lived.
- **MS lifetime**: longest evolutionary phase; $t_{MS}\propto M^{-3}$ roughly (from $L\propto M^4$, fuel $\propto M$).
- **Points 1/2/3**: ZAMS (H-ignition) → core H-exhaustion ($X_c<0.05$) → H-shell ignition.
- **The "hook"**: gravitational contraction interlude between points 2 and 3 in convective-core (high-mass) stars, absent in low-mass (radiative-core) stars — direct observational proof of core convection.
- **Isothermal He core**: forms after point 3, $L(r)=0$ inside it, grows via shell deposition.
- **Schönberg-Chandrasekhar (SC) limit**: max core mass fraction ($q_0\approx0.08$–0.10) an isothermal perfect-gas core can support; set by chemical contrast between core and envelope.
- **Three post-MS core regimes** ($>6M_\odot$ no isothermal phase; $2.2$–$6M_\odot$ temporary isothermal core then SC-limited contraction; $<2.2M_\odot$ core degenerates before reaching SC limit) — the pivotal branch point for RGB development, helium flash, or direct ignition.

### 1.4 Post-MS: RGB, HB & AGB

- **Chemical dichotomy**: He-rich core ($\mu_i\approx1.33$) beneath H-rich envelope ($\mu_e\approx0.63$) forces envelope expansion once the H-shell is active — the physical origin of the giant branch.
- **Hertzsprung Gap**: sparsely populated CMD region where intermediate/high-mass stars cross segment 4–5 rapidly; becomes a populated Sub-Giant Branch for low-mass, old populations.
- **Red Giant Branch (RGB)**: powered entirely by the H-shell; $M_c^{He}$–$L$ relation links core growth to rising luminosity.
- **First Dredge-Up**: convective envelope brings CN-processed material (He, +N, −C) to the surface — the "CN anticorrelation."
- **RGB Bump**: H-shell crosses the dredge-up's composition discontinuity, briefly dims, producing a local luminosity-function peak and a slope change (both observed).
- **Transition mass 2.2 $M_\odot$**: below it, He-core degenerates → Helium Flash; above it, stable non-degenerate He ignition.
- **Helium Flash**: thermonuclear runaway in degenerate He core (no thermoregulation); occurs off-center (neutrino cooling); energy consumed lifting degeneracy, never reaches the surface (no observable brightening); universal ignition core mass $M_c^{He}\approx0.5M_\odot$ — basis of the TRGB standard candle.
- **RGB Tip / TRGB**: constant terminal RGB luminosity ($\log L/L_\odot\approx3.45$) for $M<2.2M_\odot$ — a primary distance indicator.
- **Reimers mass-loss law**: empirical, $\dot M\propto\eta L/(gR)$; dominant on RGB/AGB where $g$ is low.
- **Zero-Age Horizontal Branch (ZAHB)**: analog of ZAMS for core He-burning; position set by $q=M_c/M_E$ (evolutionary mass after RGB mass loss).
- **HB morphology & "second parameter" problem**: age, metallicity, He abundance, and mass loss all shift HB color; two same-age/metallicity clusters can still differ (unresolved second parameter).
- **EHB / AGB-manqué**: extremely thin H-envelope HB stars that skip the AGB — candidate source of the UV upturn in old populations.
- **Overshooting & semi-convection**: convective cells cross the formal Schwarzschild border; He-burning core grows self-drivingly as opacity rises (C,O accumulate); produces a 3-zone (convective/semi-convective/radiative) structure.
- **AGB structure**: double-shell burning (H-shell + He-shell) around an inert, contracting CO core.
- **$M^{up}=8M_\odot$**: below it, CO core degenerates (→ CO-WD via AGB+PN); above it, carbon ignites stably (→ Type II SN).
- **Second/Third Dredge-Up**: Second (E-AGB, $M>4$–5$M_\odot$) brings He+N to surface; Third (thermal-pulse AGB) brings C,O from the He-intershell — creates Carbon Stars (C/O>1).
- **Thermal Pulse AGB (TP-AGB)**: alternating H-/He-shell ignition; thin-shell instability drives runaway He-shell flashes despite only mild degeneracy.
- **s-process in AGB stars**: neutron sources $^{13}$C($\alpha,n$) and $^{22}$Ne($\alpha,n$); $^{14}$N is a neutron poison.
- **Hot Bottom Burning (HBB)**: in massive AGB ($M>6$–7$M_\odot$), H-burning at convective-envelope base boosts $L$, destroys surface C (prevents carbon stars), and produces Li via Cameron-Fowler.
- **NeNa/MgAl cycles**: HBB proton-capture cycles producing the O-Na and Mg-Al anticorrelations seen in globular clusters (multiple populations).
- **RGB/AGB Phase Transitions**: population age thresholds (~1–2 Gyr, ~200–300 Myr) where a well-populated RGB/AGB first appears — reshapes integrated light and colors of aging populations.

### 1.5 Pulsating Stars

- **Instability Strip**: narrow, nearly-vertical H-R band ($T_{eff}\approx6300$–7100 K) where radial pulsation is sustained.
- **Period-Luminosity (P-L) relation**: Leavitt's law; longer period ⇒ more luminous Cepheid — first rung of the cosmic distance ladder.
- **Radial pulsation**: $R$ and $T_e$ vary in anti-phase; luminosity variation dominated by $T_e^4$, so max $L$ ≈ max $T$ ≈ min $R$ (not exactly — see phase lag).
- **Phase lag**: observed max luminosity occurs slightly after minimum radius, due to the H-ionization layer delaying emergent luminosity.
- **Pulsation classes**: Classical Cepheids (Pop I), W Virginis (Pop II analog), RR Lyrae (Pop II, HB pulsators, near-constant luminosity → standard candles), δ Scuti, β Cephei, ZZ Ceti (WD, non-radial), LPVs/Miras (AGB).
- **Evolutionary crossings**: 1st crossing fast (few pulsators), 2nd crossing (He-burning/HB) slow — dominant source of observed pulsators, 3rd crossing fast again.
- **Standing-wave analogy / pulsation modes**: fundamental (no nodes) vs overtones (1, 2,… internal nodes); most Cepheids/W Vir pulsate fundamental, RR Lyrae fundamental or first overtone (or both = "double-mode").
- **κ-mechanism**: opacity increases (not decreases) under compression in partial-ionization zones — acts as a thermodynamic valve/piston that sustains oscillation.
- **γ-mechanism**: suppressed $\delta T$ in ionization zones reinforces the driving.
- **He-II ionization zone** ($T\approx4\times10^4$K): the real "piston" driving pulsation; **H ionization zone** ($T\approx1.5\times10^4$K): source of the phase lag, not the main driver.
- **Instability strip edges**: blue edge = ionization zones too shallow (insufficient driving mass); red edge = envelope convection damps the oscillation.
- **Period-density relation**: $\Pi\propto\rho^{-1/2}$ — physical basis of the P-L relation (luminous stars are giants = low density = long period).
- **Dynamical stability condition**: oscillation requires $\gamma>4/3$.
- **Period-Luminosity-Color (PLC) relation**: the more fundamental relation; simple P-L is PLC evaluated at mean Cepheid color — explains PL scatter.

### 1.6 White Dwarfs

- **Mass loss / superwind**: AGB terminates via superwind ($\dot M\sim10^{-4}M_\odot$/yr) driven by dust/radiation pressure and Mira-type pulsation; ends when envelope drops below $\sim10^{-3}M_\odot$.
- **Planetary Nebula (PN)**: proto-WD contracts at ~constant $L$, heats past $T\sim30{,}000$K, ionizes the ejected envelope. Very massive remnants transition too fast to form a visible PN.
- **White dwarf**: electron-degenerate CO (or He/ONe) remnant; extreme density (~$10^6$ g/cm³), extreme surface gravity, extremely faint ($L\sim10^{-3}L_\odot$), Galactic-only observability.
- **WD layered structure**: CO core (bulk of mass) + thin non-degenerate He layer ($\sim10^{-2}M_{WD}$) + thinner H layer ($\sim10^{-4}M_{WD}$).
- **Spectral types**: DA (H, ~80%, from gravitational settling), DB (He, ~8%), DC (featureless, ~14%).
- **Degenerate electron pressure**: $P\propto\rho^{5/3}$ (non-relativistic), $T$-independent — basis of WD stability and constant-radius cooling.
- **Mass-radius relation (non-rel.)**: $R\propto M^{-1/3}$ — more massive WDs are smaller (opposite of normal stars).
- **Chandrasekhar mass** $M_{Ch}=1.44M_\odot(1+X)^2$: maximum mass any electron-degenerate structure can support; combines $\hbar$ (quantum), $c$ (relativity), $G$ (gravity); applies to any degenerate substructure, not just WDs.
- **WD cooling**: no nuclear burning, no contraction possible; luminosity sourced purely from declining ionic thermal energy; cooling proceeds at **constant radius**.
- **Mestel cooling law**: $L(t)=L_0[1+\tfrac{5}{2}t/\tau_0]^{-7/5}$; more massive WDs cool more slowly (larger reservoir) — counterintuitively more luminous at fixed old age.
- **Crystallization**: CO ions form a lattice as $T_c$ drops, releasing latent heat and producing a luminosity-function plateau.
- **WD luminosity function (WDLF)**: sharp faint-end cutoff gives population age (cosmic chronometer), though less precise than MS-turnoff dating.
- **Slowly cooling WDs**: residual H layer above $10^{-4}M_{WD}$ (from AGB-skipping blue-HB progenitors) sustains stable H-burning, delaying cooling by up to ~1 Gyr — discovered via the M3–M13 "twin cluster" WD excess.
- **Density–mass scaling**: $\rho\propto M^2$ — small accreted mass greatly raises central density, relevant to Type Ia ignition.

### 1.7 Final Stages High Mass

- **Mildly-degenerate CO core regime ($7$–$11M_\odot$)**: Carbon Flash (off-center, analogous to He-flash) → convective flame propagates inward, erasing degeneracy → stable central C-burning → Super-AGB phase.
- **O-Ne WD vs Electron-Capture SN (EC-SN)**: outcome set by the race between mass loss (envelope stripped before core reaches $M_{Ch}$ → O-Ne WD) and core growth (reaches $M_{Ch}$ → EC-SN, leaves a neutron star).
- **Electron-capture collapse mechanism**: e⁻ capture on Mg/Ne removes pressure support → runaway contraction → semi-degenerate O-ignition/deflagration → NS.
- **Non-degenerate advanced burning ($M>11M_\odot$)**: staircase of C→Ne→O→Si burning, each stage shorter than the last because neutrino losses (∝$T^9$) drain energy faster than burning can replace it.
- **Neon burning**: photo-disintegration + alpha-capture, not direct fusion — occurs at lower $T$ than O-burning because photodisintegrating Ne is energetically easier than fusing two O nuclei.
- **Silicon burning**: photo-disintegration cascade to alpha particles, then alpha-capture rebuild to iron-peak — Nuclear Statistical Equilibrium (NSE).
- **$^{56}$Ni endpoint (not $^{56}$Fe)**: burning too fast for weak interactions to equilibrate n/p ratio.
- **Onion-shell structure**: H/He/C/O/Si shells surrounding an inert Fe core just before collapse.
- **Iron core collapse triggers**: electron capture on Fe-group nuclei, photo-disintegration of Fe (endothermic, absorbs ~124 MeV/nucleus), and the URCA process — all reduce pressure and Γ below 4/3.
- **Core bounce**: infall halts abruptly at nuclear density, rebounds, launches a shock.
- **Prompt shock failure**: shock loses energy to iron photo-disintegration and neutrino cooling, stalls at ~100–200 km.
- **Delayed neutrino-driven explosion**: neutrinos diffusing from the neutrinosphere deposit energy in the "gain region," reviving the stalled shock after ~100–500 ms.
- **Explosive nucleosynthesis**: shock-heated shells synthesize new elements on the fly (r-process innermost, $^{56}$Ni in Si/O shell, intermediate-mass elements in O shell) — distinct from pre-collapse iron, which stays locked in the remnant.
- **r-process**: rapid neutron capture, builds far off the valley of stability; peaks at $A\approx80,130,195$ (neutron magic numbers).
- **SN light curve stages**: shock breakout (brief UV/X-ray flash) → optical peak (H recombination front opacity drop) → plateau (Type II-P; constant recombination temperature) → radioactive tail ($^{56}$Co decay, $\tau_{1/2}=77.1$d).
- **SN classification tree**: II (H present) vs I (no H) → Ia (Si present, thermonuclear) vs Ib (He, no Si) vs Ic (no He, no Si) — spectroscopic labels reflecting progenitor envelope stripping, not explosion mechanism (Ib/Ic/II all core-collapse).
- **NS vs BH remnant threshold**: roughly $M<25M_\odot\to$NS, $M>25M_\odot\to$BH (approximate; density-gradient dependent); prompt vs fallback BH formation.

### 1.8 Binary Systems

- **Roche potential / equipotentials**: effective potential in the co-rotating frame (gravity of both stars + centrifugal term); gas in hydrostatic equilibrium follows equipotentials.
- **Lagrangian points**: $L_1$ (inner, unstable, gateway for mass transfer), $L_2,L_3$ (unstable), $L_4,L_5$ (stable, triangular).
- **Roche lobe**: largest closed equipotential surface bound to a star, passing through $L_1$; defines the maximum stellar size before Roche Lobe Overflow (RLOF).
- **Binary classes**: detached (neither fills Roche lobe), semidetached (one fills, mass transfer active), contact (both overflow, common envelope).
- **Accretion disk**: forms because infalling gas carries orbital angular momentum; co-rotates with the binary orbit.
- **Blue Straggler Stars**: rejuvenated (via mass transfer or merger) stars appearing brighter/bluer than the MS turnoff — direct observational proof of binary interaction.
- **Reduced mass / orbital angular momentum**: $\mu=M_1M_2/M$; $L=\mu\sqrt{GMa(1-e^2)}$ — the conserved quantity tracked during mass transfer.
- **Conservative mass transfer**: no mass or angular momentum lost from the system; orbital response depends on the sign of $(M_1-M_2)$ relative to who is donating.
- **Positive vs negative feedback in mass transfer**: donor more massive than accretor → orbit shrinks → runaway; donor less massive → orbit widens → self-regulating.
- **Accretion efficiency hierarchy**: WD ≪ H-burning (0.7% $mc^2$) ≪ NS (~15%) < BH (10–42%) — gravitational accretion onto compact objects vastly outperforms nuclear burning.
- **Cataclysmic Variables (CVs)**: WD + low-mass donor, low $\dot M$, disk-instability outbursts (dwarf novae), not thermonuclear.
- **Classical Novae**: degenerate H-shell thermonuclear runaway on a WD surface; recurrent (every $10^4$–$10^5$ yr); WD survives.
- **Type Ia SN progenitor channels**: single-degenerate (WD accretes from non-degenerate companion) vs double-degenerate (WD-WD merger); both converge on Chandrasekhar-mass carbon ignition.
- **Binary survival criterion after SN**: system remains bound only if ejected mass $\delta m < (M_1+M_2)/2$.
- **Common envelope (CE) evolution**: drastic orbital shrinkage via drag inside a shared envelope; ends in merger or envelope ejection — the mechanism that produces very tight compact binaries (CVs, Type Ia progenitors, compact NS/BH binaries) from wide initial orbits.

### 1.9 Supernovae & Neutron Stars

- **Type Ia explosion**: thermonuclear disruption of a CO-WD reaching $M_{Ch}$; no remnant left.
- **Deflagration vs detonation**: subsonic (deflagration) allows expansion, producing both Fe-peak and intermediate-mass elements; supersonic detonation alone would over-produce Ni (ruled out observationally).
- **W7 model / delayed detonation**: canonical deflagration benchmark; delayed detonation (deflagration→detonation transition) best matches observed mixed nucleosynthesis.
- **SN Ia light curve**: powered by $^{56}$Ni→$^{56}$Co→$^{56}$Fe radioactive decay chain; stretch-factor (Phillips relation) correction makes them standardizable candles.
- **[α/Fe]–[Fe/H] diagram**: plateau (Type II-only enrichment, early), knee (onset of Type Ia iron injection), descending slope; knee position/height encode the star-formation rate and IMF of the population — a "chemical DNA" fingerprint.
- **Stellar endpoint mass ladder**: $<0.08M_\odot$ brown dwarf; $0.08$–$0.5$ He-WD; $0.5$–$7$ CO-WD; $7$–$11$ ONe-WD or EC-SN; $>11$ Type II SN → NS ($11$–$25M_\odot$) or BH ($>25M_\odot$).
- **Neutron star**: supported by degenerate neutron pressure; $M\sim1.2$–$2.5M_\odot$, $R\sim10$–15 km; masses cluster near $M_{Ch}$ because that's the pre-collapse Fe-core mass scale.
- **NS internal layers**: outer crust (nuclei + degenerate e⁻, neutronization) → inner crust (neutron drip, $\rho\sim4\times10^{11}$) → interior (nuclei dissolve, n:p:e≈8:1:1) → core (superfluid n, superconducting p; exotic matter uncertain).
- **Oppenheimer-Volkoff limit**: $\sim2.5$–$3M_\odot$, the NS maximum mass; poorly constrained (unknown super-nuclear equation of state).
- **Collapse consequences**: ~factor-500 radius shrinkage (WD-core→NS) drives angular-momentum spin-up (birth periods ~ms) and magnetic-flux compression (fields $10^{13}$–$10^{14}$ G) — explains pulsar birth properties.
- **Pulsars**: rotating, highly magnetized NS; extremely regular period, secular spin-down ($\dot P\sim10^{-15}$); characteristic age $\tau=P/\dot P$.
- **Crab Pulsar/Nebula**: spin-down luminosity quantitatively matches the nebula's synchrotron output — proof pulsars are rotation-powered.
- **Pulsar emission mechanism**: induced surface E-field strips charges → curvature radiation → pair-production cascade → coherent beam.
- **Light cylinder**: radius where co-rotation speed would equal $c$; open vs closed field lines set the braking/emission geometry.
- **Beaming**: relativistic headlight effect + misaligned magnetic/rotation axes + fast rotation → lighthouse pulses.
- **Dispersion measure**: frequency-dependent pulse delay through ionized ISM → pulsar distance estimator.
- **P–$\dot P$ diagram**: young pulsars upper-left → spin down toward lower-right → "death line"/graveyard; magnetic field $\propto\sqrt{P\dot P}$.
- **Millisecond pulsars & recycling**: old, dead pulsars spun back up by accretion from an evolving companion (spin-up via the Alfvén/disruption radius); leaves MSP + He-WD binaries.
- **Black Widow pulsars**: MSP wind ablates/evaporates a low-mass companion, leaving an isolated MSP.
- **Bulge Fossil Fragments** (Terzan 5, Liller 1): massive bulge systems with multiple, widely-separated-age stellar populations — candidate surviving fragments of the hierarchical bulge assembly.

### 1.10 Black Holes & Gravitational Waves

- **Schwarzschild radius**: $R_s=2GM/c^2=3(M/M_\odot)$ km; the classical escape-velocity=$c$ radius, also the exact GR event-horizon radius.
- **Spacetime interval**: timelike/null/spacelike separations define causal structure; light cones tip toward the singularity as $r\to R_s$.
- **Schwarzschild metric**: exact GR solution outside a spherical mass; produces radial-distance dilation and gravitational time dilation, both diverging at $R_s$.
- **Event horizon**: one-way causal boundary; not a physical surface. **Singularity**: $r=0$, GR breaks down. **Cosmic censorship**: singularities are always hidden behind horizons (conjectured).
- **Compactness parameter $\xi_{2.5}$**: predicts successful SN (→NS) vs "failed SN" (direct BH collapse) at threshold $\approx0.2$.
- **Metallicity → BH mass**: metal-poor stars lose less wind mass and have larger CO cores → more massive BHs (up to $\sim60M_\odot$); at solar $Z$, single-star evolution cannot produce BHs $>25M_\odot$.
- **BH mass classes**: stellar-mass ($\lesssim$50–100$M_\odot$), intermediate-mass (IMBH, $10^2$–$10^5M_\odot$, unconfirmed), supermassive ($10^6$–$10^9M_\odot$).
- **Magorrian relation**: $M_{BH}\approx10^{-3}M_{gal}$ — links SMBH growth to host galaxy/bulge growth; IMBHs are candidate SMBH seeds.
- **IMBH signatures in globular clusters**: central stellar density cusp + Keplerian rise in velocity dispersion within the BH sphere of influence.
- **Gravitational waves**: quadrupolar spacetime ripples from accelerating mass; binaries are the archetypal source.
- **Strain $h_0$**: fractional length distortion; scales as product of each body's compactness ($R_{Si}/R$) divided by distance; extraordinarily small ($\sim10^{-22}$).
- **Chirp**: simultaneous rise in GW frequency ($\omega_{gw}=2\omega_{orbital}$) and amplitude as the binary inspirals.
- **Chirp mass**: the unique mass combination directly measurable from the waveform (frequency + its time-derivative) without knowing distance or mass ratio.
- **Mass-ratio degeneracy**: chirp mass alone under-determines $m_1,m_2$; equal-mass assumption gives the minimum total mass ($M_{tot}\geq2.3\,M_{chirp}$).
- **Coalescence condition**: merger begins when separation ≈ sum of Schwarzschild radii; sets total mass from the maximum observed GW frequency.
- **LIGO / Michelson interferometer**: differential arm-length stretch/compression from a passing GW breaks destructive interference; two widely-separated detectors needed to reject local noise and localize sources.
- **Redshift effects on GW observables**: detector-frame chirp mass and component masses are systematically boosted by $(1+z)$ relative to source-frame values.
- **GW150914**: first BH-BH merger detection; $m_1\approx36M_\odot,\ m_2\approx29M_\odot$, $D_L\approx410$ Mpc.
- **GW170817**: first NS-NS merger; multi-messenger event (GW + short GRB + kilonova); confirmed NS mergers as an r-process site (heavy elements: Au, Pt, lanthanides).
- **Kilonova**: optical/IR transient powered by radioactive decay of freshly r-process-synthesized nuclei in neutron-rich merger ejecta; spectral reddening over days tracks the growing lanthanide opacity.

---

## 2. Key Equations

### 2.1 Introduction

- Hydrostatic equilibrium: $\dfrac{dP}{dr}=-\dfrac{GM(r)}{r^2}\rho(r)$ — pressure gradient supports the weight of overlying layers.
- Mass continuity: $\dfrac{dM(r)}{dr}=4\pi r^2\rho(r)$ — links enclosed mass to the density profile.
- Equation of state: $P=P_{rad}+P_{gas}=\dfrac{aT^4}{3}+\dfrac{k\rho T}{\mu H}$ — total pressure; radiation term matters only in the most massive stars.
- Mean molecular weight: $\mu=\left(2X+\tfrac34 Y+\tfrac12 Z\right)^{-1}$ — sets gas pressure at given $\rho,T$.
- Electron degeneracy condition: $T/\rho^{2/3}<10^5$ (electrons degenerate below this line in the $\log T$–$\log\rho$ plane).
- Degenerate pressures: $P=k_1\rho^{5/3}$ (non-relativistic), $P=k_2\rho^{4/3}$ (relativistic) — density-only, no $T$ dependence.
- Energy conservation: $\dfrac{dL(r)}{dr}=4\pi r^2\rho(r)\,\epsilon$ — luminosity gradient set by local energy generation rate $\epsilon$.
- Virial theorem: $2K+\Omega=0\ \Rightarrow\ U=\Omega/2<0$ — governs all gravitationally-contracting phases.
- Kelvin-Helmholtz timescale: $t_{KH}=\dfrac{1}{2}\dfrac{GM^2}{LR}$ — how long gravity alone can power a star ($\sim1.5\times10^7$ yr for the Sun).
- Radiative temperature gradient: $\left.\dfrac{dT}{dr}\right|_{rad}=-\dfrac{3\kappa\rho}{4ac}\dfrac{L(r)}{4\pi r^2T^3}$ — steepens with high opacity or high flux.
- Nabla / Schwarzschild criterion: $\nabla\equiv d\log T/d\log P$; convection when $\nabla_{rad}>\nabla_{ad}$; $\nabla_{ad}=(\gamma-1)/\gamma=0.4$ for monatomic ideal gas.
- Kramers opacity laws: $\kappa_{BF}\propto Z(1+X)\rho/T^{3.5}$; $\kappa_{FF}\propto(X+Y)(1+X)\rho/T^{3.5}$; $\kappa_E=0.2(1+X)$ (electron scattering, $T,\rho$-independent).
- Nuclear binding energy: $E_B(Z,A)=[Zm_p+(A-Z)m_n-m_{nucl}]c^2$ — energy released depends on the mass deficit.
- Energy generation rates: $\epsilon_{pp}\propto\rho X^2T_6^{3.5-6}$; $\epsilon_{CN}\propto\rho XX_{CN}T_6^{13-20}$; $\epsilon_{3\alpha}\propto\rho^2Y^3T_8^{20-30}$ — steep $T$-sensitivity increases with burning stage.
- Effective temperature relation: $T^4=\tfrac34T_e^4(\tau_v+\tfrac23)$ — defines $T_e$ at $\tau_v=2/3$.
- Saha equation: $\log(N_{j+1}/N_j)=-0.176-\log P_e+\log[U_{j+1}(T)/U_j(T)]+2.5\log T-5040\chi_i/T$ — ionization balance.
- Boltzmann equation: $N_{ji}/N_j=(g_i/U_j(T))\,10^{-\chi_i(5040/T)}$ — excitation-level population.
- Doppler shift: $\Delta\lambda/\lambda_0=v_r/c$.
- Equivalent width: $W=\int(F_c-F_\lambda)/F_c\,d\lambda$ — proportional to absorber column density (curve of growth).
- Abundance notation: $[El/H]=\log(El/H)_*-\log(El/H)_\odot$.

### 2.2 Pre-Main Sequence Evolution

- Dynamical (free-fall) timescale: $T_d=\sqrt{2r^3/GM}=2600/\sqrt{\bar\rho}$ s — sets the fastest collapse phase.
- Jeans mass: $M_J\gtrsim10^{23}\,T^{3/2}\rho^{-1/2}$ g — collapse threshold in terms of observable $(T,\rho)$.
- Salpeter IMF: $\Psi(M)=kM^{-2.35}$.
- Pre-MS timescale scaling: $t_{PMS}\sim4\times10^7(M/M_\odot)^2(R_\odot/R)(L_\odot/L)$ yr.
- Hayashi-track physics: driven by $\kappa\propto\rho/T^{3.5}$ making $\nabla_{rad}\gg\nabla_{ad}$ at low $T$, forcing full convection.

### 2.3 Main Sequence Evolution

- Eddington luminosity: $L_{Ed}=4\pi GMc/\kappa$; numerically $L_{Ed}/L_\odot\approx3.8\times10^4(M/M_\odot)$.
- pp vs CNO energy generation: $\epsilon_{pp}\propto\rho X^2T_6^5$; $\epsilon_{CNO}\propto\rho XZ_{CNO}T_6^{15}$.
- Mass–luminosity relation (broken power law): $L\propto M^{3.6}$ (upper MS, CNO); $L\propto M^{4-4.5}$ (lower MS, pp); $L\propto M^{2.6}$ (very low mass).
- MS lifetime: $t_{MS}\cong10^{10}M^{-3}$ yr.
- Schönberg-Chandrasekhar limit: $q\leq q_0=0.37(\mu_e/\mu_{ic})^2\approx0.08$; equivalently $M_c\leq0.10\,M_{tot}$.
- Electron degeneracy (Fermi) condition: $T/\rho^{2/3}<D\approx10^5$; boundary line $\log T=\tfrac23\log\rho+5$.

### 2.4 Post-MS: RGB, HB & AGB

- Density-gradient ratio at core/envelope boundary: $(\mu_e/\mu_i)^2\times[(\alpha-\gamma\beta)/(\alpha-\beta)]$, with $\gamma=(1+u)\frac{1+X_e}{1+X_i}(\mu_e/\mu_i)^n$ — quantifies why the envelope must expand once the shell is active ($u>0$).
- Reimers mass-loss law: $\dot M=-4\times10^{-13}\eta\,L/(gR)\ M_\odot$yr$^{-1}$.
- Shell luminosity–$\mu$ sensitivity: $L_H\propto\mu^7$ — explains the RGB Bump dip.
- Helium-flash degeneracy-removal condition: $T/\rho^{2/3}>10^5$.
- Universal He-flash ignition mass: $M_c^{He}\approx0.5M_\odot$.
- TRGB standard candle: $\log(L/L_\odot)\approx3.45$, $M_I\approx-4.0$; $(m-M)_I=m_I+4.0$.
- ZAHB parameter: $q=M_c/M_E$ sets HB color (higher $q$ → bluer).
- Free-free opacity in He-burning core: $\kappa_{FF}=D_{FF}(Z)/u^3$, $D_{FF}\propto Z^2$ — drives convective-core growth as C,O accumulate.
- Overshooting parametrization: $\Lambda_{ov}$ (e.g. 1.25 = 25% extra mixing beyond the Schwarzschild border).

### 2.5 Pulsating Stars

- P-L relation: $M_V=-2.8\log P_{days}-1.43$.
- Distance via Cepheids: $(m-M)_V=\langle V\rangle-M_V=5\log d-5$ (uncorrected for reddening).
- Sound speed: $v_s=\sqrt{\gamma P/\rho}$.
- Period-density relation: $\Pi\approx\sqrt{3\pi/(2\gamma G\rho)}\ \propto\rho^{-1/2}$.
- One-zone model oscillator: $\ddot{(\delta R)}=-(3\gamma-4)(GM/R_0^3)\,\delta R$; stable oscillation requires $\gamma>4/3$.
- Full period-luminosity-color (PLC) relation: $M_V=-3.53\log P_{days}-2.13+2.13(B-V)$.

### 2.6 White Dwarfs

- Degenerate electron pressure: $P=\tfrac{(3\pi^2)^{2/3}}{5}\tfrac{\hbar^2}{m_e}\left[(Z/A)\rho/m_H\right]^{5/3}$ (non-relativistic).
- Mass–radius relation: $M^{1/3}R\sim3\times10^{19}$ cgs $\Rightarrow R\propto M^{-1/3}$.
- Relativistic degenerate pressure: $P=\tfrac{(3\pi^2)^{1/3}}{4}\hbar c\left[(Z/A)\rho/m_H\right]^{4/3}$.
- Chandrasekhar mass: $M_{Ch}=\tfrac{3\sqrt{2\pi}}{8}(\hbar c/G)^{3/2}[(Z/A)/m_H]^2=1.44(1+X)^2\,M_\odot$.
- WD luminosity–core temperature relation: $L=cT_c^{7/2}$.
- Mestel cooling law: $L(t)=L_0\left[1+\tfrac52 t/\tau_0\right]^{-7/5}$.
- Cooling time: $t_{cool}=8.8\times10^6(M/M_\odot)^{5/7}(L/L_\odot)^{-5/7}$ yr (canonical CO composition).
- Density–mass scaling: $\rho\propto M^2$.

### 2.7 Final Stages High Mass

- Timescale acceleration table (20$M_\odot$): H ($10^7$yr) → He ($10^6$yr) → C ($10^3$yr) → Ne (3 yr) → O (200 d) → Si (1 week) — driven by neutrino losses $\propto T^9$.
- Free-fall collapse timescale: $\tau_{FF}\propto\rho_0^{-1/2}$; $\tau_d\approx10$ ms at $\rho\sim10^{10}$ g/cm³.
- Gravitational energy released in collapse: $\Delta E_g\approx GM^2/R_f\approx10^{53}$ erg (mostly carried away by neutrinos; only $\sim10^{51}$ erg needed to unbind the envelope).
- Radioactive tail slope: $L\propto N_0e^{-0.693t/\tau_{1/2}}$; $dM_{bol}/dt\propto0.74/\tau_{1/2}$ — encodes the decaying isotope's half-life.

### 2.8 Binary Systems

- Roche potential: $\Phi_{eff}(\mathbf r)=-GM_1/|\mathbf r-\mathbf r_1|-GM_2/|\mathbf r-\mathbf r_2|-\tfrac12\omega^2|\mathbf r-\mathbf r_{cm}|^2$.
- Approximate Roche lobe radii: $l_1=a(0.5-0.227\log(M_2/M_1))$, $l_2=a(0.5+0.227\log(M_2/M_1))$, $l_1+l_2=a$.
- Orbital angular momentum: $L=\mu\sqrt{GMa(1-e^2)}$.
- Conservative mass-transfer orbital evolution: $\dfrac{1}{a}\dfrac{da}{dt}=\dfrac{2\dot M_1(M_1-M_2)}{M_1M_2}$.
- Kepler's third law (orbital frequency): $\omega^2=GM/a^3$.
- Accretion kinetic energy: $K=GMm/R$ per unit mass $m$ (compactness sets the yield: WD≪NS≪BH).
- Binary survival after SN: bound iff $\delta m<(M_1+M_2)/2$.

### 2.9 Supernovae & Neutron Stars

- $^{56}$Ni→$^{56}$Co→$^{56}$Fe decay chain: $\tau_{1/2}=6.1$ d then 77.1 d — powers both SN Ia and SN II late-time light curves.
- Abundance ratio: $[\text{el/H}]=\log(\text{el/H})_*-\log(\text{el/H})_\odot$.
- NS mass–radius relation: $MR_{NS}^3=$const; $R=14.6(10^{15}\,\text{g cm}^{-3}/\rho_c)^{1/6}$ km; $M=(15.2\,\text{km}/R)^3\,M_\odot$.
- Oppenheimer-Volkoff limit: $M_{NS}^{limit}\sim2.5$–$3M_\odot$.
- Collapse compaction ratio: $R_{pre}/R_{post}=(m_n/m_e)(Z/A)^{5/3}\approx500$.
- Spin-up from angular-momentum conservation: $P_{NS}=P_i(R_f/R_i)^2\approx4\times10^{-6}P_{pre-collapse}$.
- Magnetic flux conservation: $B_{NS}=B_{WD}(R_{WD}/R_{NS})^2$.
- Magnetic dipole radiation formula: $B^2=\dfrac{3Ic^3}{8\pi^2R^6}P\dot P\ \Rightarrow\ B\propto\sqrt{P\dot P}$.
- Characteristic pulsar age: $\tau=P/\dot P$.
- Rotational kinetic energy & spindown power: $K=2\pi^2I/P^2$; $dK/dt=-4\pi^2I\dot P/P^3$.
- Light cylinder radius: $R_{lc}=c/\omega=cP/2\pi$.
- Alfvén (magnetospheric) radius: $r_A=\left(B_s^4R^{12}/(2GM\dot M^2)\right)^{1/7}$; disruption radius $r_d\approx0.5\,r_A$.
- Spin-up rate: $\dot P/P=-\dfrac{P}{2\pi I}\sqrt{\alpha}\left(\dfrac{B_s^2R^6G^3M^3\dot M^6}{2}\right)^{1/7}$.
- Dispersion delay: $\Delta t\propto \text{DM}\,(1/\nu_2^2-1/\nu_1^2)$.

### 2.10 Black Holes & Gravitational Waves

- Schwarzschild radius: $R_s=2GM/c^2=3(M/M_\odot)$ km.
- Schwarzschild metric: $(ds)^2=[c\,dt\sqrt{1-R_s/r}]^2-[dr/\sqrt{1-R_s/r}]^2-r^2d\Omega^2$.
- Proper radial distance: $dL=dr/\sqrt{1-R_s/r}>dr$.
- Gravitational time dilation: $d\tau=dt\sqrt{1-R_s/r}<dt$.
- Coordinate speed of light: $dr/dt=c(1-R_s/r)\to0$ as $r\to R_s$.
- Compactness parameter: $\xi_M=(M/M_\odot)/(R(M)/1000\text{km})$; $\xi_{2.5}\gtrless0.2$ separates SN from failed SN.
- Mass-loss/metallicity scaling: $\dot M\propto Z^\alpha$, $\alpha\approx0.5$–0.9.
- IMBH sphere of influence: $r_{BH}=GM_{BH}/\sigma^2$.
- Magorrian relation: $M_{BH}\approx10^{-3}M_{gal}$.
- Kepler's law for binary orbit: $\omega_s^2=G(m_1+m_2)/R^3$.
- GW strain amplitude: $h_0=2(R_{S1}/r)(R_{S2}/R)$.
- GW frequency: $\omega_{gw}=2\omega_s$.
- Total orbital energy: $E_{tot}=-GM\mu/(2R)$.
- GW luminosity: $L=\tfrac{32}{5}(G/c^5)(\mu R^2\omega_s^3)^2$.
- Chirp mass (definition & observable form): $M_{chirp}=(m_1m_2)^{3/5}/(m_1+m_2)^{1/5}=\dfrac{c^3}{G}\left[\tfrac{5}{96}\pi^{-8/3}\nu_{gw}^{-11/3}\dot\nu_{gw}\right]^{3/5}$.
- Minimum total mass from mass-ratio degeneracy: $M_{tot}\geq2.3\,M_{chirp}$.
- Total mass from merger frequency: $M_{tot}=\dfrac{1}{\pi\sqrt8}\dfrac{c^3}{G\nu_{gw}^{max}}$.
- Distance estimate: $r=\dfrac{16}{\sqrt5}\dfrac{G}{c^4}\dfrac{\mu R^2\omega_s^2}{h_0}$.
- Redshift corrections: $\nu^{det}=\nu^s/(1+z)$; $\dot\nu^{det}=\dot\nu^s/(1+z)^2$; $M_{chirp}^{det}=(1+z)M_{chirp}^s$.

---

## 3. Key Algorithms / Procedures

1. **Placing a star on the H-R diagram (stellar-model flow chart).** (1) Fix $M,X,Y,Z$. (2) Solve the seven coupled structure equations simultaneously. (3) At each radius check the electron-degeneracy condition ($T/\rho^{2/3}$ vs $10^5$) and the Schwarzschild convection criterion ($\nabla_{rad}$ vs $\nabla_{ad}$) to select the correct EOS and energy-transport law. (4) Output is a unique $(L,T_e)$ point. (5) To evolve in time: update composition from nuclear burning, advance $t\to t+\Delta t$, and resolve the equations again — the sequence of points is the evolutionary track.

2. **Determining whether a stellar cloud collapses (Jeans criterion).** (1) Measure/estimate cloud $T$ and $\rho$. (2) Compute $M_J=10^{23}T^{3/2}\rho^{-1/2}$ g. (3) If the cloud's actual mass exceeds $M_J$, gravity wins and collapse proceeds; otherwise thermal pressure disperses the cloud. (4) If collapse occurs and $M\gg M_J$, the clump must fragment — this fragmentation, not single-cloud collapse, sets the stellar mass spectrum (IMF).

3. **Determining convective vs radiative zones (Schwarzschild criterion, applied at every radius and evolutionary time).** (1) Displace a gas parcel adiabatically by $dr$. (2) Compare its temperature to the surrounding medium at $r+dr$ (equivalently, compare $\nabla_{rad}$ to $\nabla_{ad}$). (3) If the parcel is hotter/less dense than its surroundings, it keeps rising → convection; otherwise it sinks back → radiative. (4) Convective zones homogenize composition; watch for triggers: high $\kappa$ (opacity bumps, e.g. He-II at $T\sim4\times10^4$K) or high concentrated flux (CNO burning in massive-star cores).

4. **Deriving a virial-theorem-based timescale or limit (used repeatedly: $t_{KH}$, SC limit, WD mass–radius, Chandrasekhar mass, NS mass–radius).** (1) Write hydrostatic equilibrium in an integral/energy form. (2) Identify the relevant pressure-supplying term (thermal, degenerate non-relativistic, or degenerate relativistic). (3) Balance it against the gravitational term via the virial relation $2K+\Omega=0$ (or its generalized subregion form). (4) Solve for the limiting mass, radius, or timescale; check which power of density/mass appears — this reveals whether a *maximum mass* (no free radius, e.g. Chandrasekhar/OV) or a *mass–radius relation* results.

5. **Tracing pre-MS evolution to the ZAMS.** (1) Free-fall collapse (dynamical timescale) until the growing core reaches hydrostatic equilibrium. (2) Envelope infall shock disperses gas, opacity drops, luminosity spikes. (3) Progressive hydrostatic equilibrium spreads outward; star lands on its Hayashi track, fully convective, contracting on the Kelvin-Helmholtz timescale (Virial theorem: half the released energy heats the core). (4) As $T_c$ rises, opacity falls (Kramers), $\nabla_{rad}$ drops below $\nabla_{ad}$ in the center → radiative core forms → track bends leftward off the Hayashi track. (5) Partial pp/CNO reactions ignite, gravitational luminosity fraction $L_g/L$ falls. (6) $^3$He+$^3$He fully activates → ZAMS reached, $L_g/L=0$.

6. **Assessing post-MS core fate (isothermal core → SC limit → degeneracy race).** (1) At H-exhaustion, check core mass regime: $M>6M_\odot$ (no isothermal phase, remains ideal gas, direct He ignition); $2.2$–$6M_\odot$ (temporary isothermal core, contracts once $q>q_0\approx0.08$–0.10, ideal-gas He ignition); $M<2.2M_\odot$ (core crosses the degeneracy boundary before the SC limit — long RGB ascent, He Flash). (2) Track $(\log\rho_c,\log T_c)$ against the degeneracy line $\log T=\tfrac23\log\rho+5$ to confirm which regime applies.

7. **The Helium Flash cascade (removing degeneracy).** (1) Ignition off-center (neutrino cooling creates an off-center temperature maximum). (2) Main flash drives convection, expands/lifts degeneracy in the shell above the ignition point. (3) A second, smaller flash ignites at the next inward degenerate/non-degenerate boundary. (4) Repeat progressively inward (~$10^6$ yr total) until the entire core is non-degenerate. (5) Post-flash adjustment (shell efficiency drops, star dims slightly) → settles on the ZAHB.

8. **Constructing a composite/master Cepheid light curve or using the P-L relation for distance.** (1) Obtain $P$ (time between successive maxima) and mean apparent magnitude $\langle V\rangle$. (2) Compute $M_V=-2.8\log P-1.43$ (or the full PLC form if color is available). (3) Compute distance modulus $(m-M)_V=\langle V\rangle-M_V$, correct for reddening if needed. (4) Solve $5\log d-5=(m-M)_0$ for distance.

9. **Determining GW source parameters from a detected chirp (as applied to GW150914).** (1) From the time–frequency spectrogram, measure successive $\Delta t$ between wave minima to get $\nu_{gw}(t)$ and $\dot\nu_{gw}(t)$. (2) Compute the chirp mass from the observable combination $\nu_{gw}^{-11/3}\dot\nu_{gw}$ (should be constant across the signal — internal consistency check). (3) Get a lower bound on total mass via $M_{tot}\geq2.3\,M_{chirp}$ (equal-mass case). (4) Read the maximum GW frequency at merger and use the coalescence condition to get an independent $M_{tot}$ (cross-check against step 3). (5) Combine chirp mass and total mass to solve for the mass ratio $\alpha$ and hence $m_1,m_2$. (6) Use the flux–luminosity relation with the measured $h_0$ to estimate the source distance. (7) If a redshift is independently known (host galaxy or cosmology), correct detector-frame masses by dividing by $(1+z)$.

10. **Reading the [α/Fe]–[Fe/H] diagram to infer a population's star-formation history.** (1) Identify the low-metallicity plateau value (set by the IMF — a top-heavy IMF raises the plateau). (2) Locate the "knee" metallicity where [α/Fe] begins to fall (set by the SFR: higher SFR → knee at higher [Fe/H], because more Type II SNe pollute the ISM with Fe-comparable α before Type Ia's ~30+ Myr delay expires). (3) Compare the descending-slope shape after the knee. (4) Cross-match against known environments (dwarf galaxy, halo, bulge) to identify the formation history/environment.

11. **Determining nuclear-abundance corrections from spectroscopy.** (1) Measure equivalent width $W$ of a spectral line. (2) Enter the curve of growth to obtain the column density $N_a$ of atoms in the active (observed) ionization/excitation state. (3) Apply the Boltzmann correction (divide by excited-level population fraction) to get the total in that ionization state, $N_j$. (4) Apply the Saha correction (sum over ionization states) to get $N_{TOT}$. (5) Convert to mass per unit area and compute $[El/H]$ relative to solar.

---

## 4. Watch Out For

**Introduction**
- "Contraction" (Kelvin-Helmholtz timescale) vs "collapse" (dynamical timescale) are not interchangeable — using the wrong word implies the wrong physical timescale.
- The H-R diagram's x-axis increases *leftward* — a constant source of sign/direction errors when describing tracks.
- Radiation pressure is usually negligible in stellar interiors *except* in the most massive, near-Eddington stars.
- "Degenerate gas" in this course always means *electron*-degenerate; protons/ions never degenerate under stellar conditions.
- The CNO cycle does not create C, N, O — it only catalyzes H-burning using pre-existing CNO nuclei; N-14 *accumulates* because it is the slow (rate-limiting) step, not because it's being produced net.
- Fusion beyond iron consumes energy rather than releasing it — this is *why*, not just a fact to memorize, the core must collapse once it is all iron.
- Big Bang nucleosynthesis stalls at He (plus trace Li/Be) because no stable nucleus exists at A=5 or A=8 — this is exactly what the triple-alpha "bridge" in stars later overcomes via the Be-8 near-equilibrium and the Hoyle resonance.

**Pre-Main Sequence**
- Evolutionary tracks and isochrones look completely different and are often confused: a track is one star over time; an isochrone connects different-mass stars at one age (what a real cluster CMD shows).
- The Hayashi Theorem is universal — it re-applies whenever a star approaches its Hayashi track later in life (e.g., ascending the RGB), not just during pre-MS.
- The Jeans mass for typical cold ISM conditions (~100$M_\odot$) is far larger than a single star — the cloud must fragment; a single collapsing Jeans mass does not equal one star.
- More massive stars have *shorter* pre-MS timescales despite the naive $M^2$ scaling in the approximate formula — this is because $L$ and $R$ grow even faster with mass, dominating the $L^{-1}R^{-1}$ factors.
- A brief negative $L_g/L$ episode (core expansion "absorbing" energy) occurs just before the ZAMS — don't assume $L_g/L$ decreases monotonically to zero.

**Main Sequence**
- The transition mass separating pp-dominance from CNO-dominance is a low $1.2\,M_\odot$ — not a round number, and easy to misremember as "a few solar masses."
- The MS "hook" appears only for convective-core (high-mass, $M>1.2M_\odot$) stars; low-mass stars transition smoothly from core to shell burning with no hook and no gravitational-contraction gap.
- Schönberg-Chandrasekhar limit value differs depending on formulation: $q_0\approx0.37(\mu_e/\mu_{ic})^2\approx0.08$ (mass fraction) vs the simpler often-quoted $M_c\lesssim0.10\,M_{tot}$ — know both and that they are approximately, not exactly, equivalent.
- Low central density in massive-star cores (not just high temperature) is why they avoid degeneracy — both effects (from CNO's temperature-limiting behavior) work together.

**Post-MS: RGB, HB & AGB**
- The chemical dichotomy ($\mu_e\ne\mu_i$) alone does *not* cause envelope expansion — the H-shell must also be *active* ($u>0$); expansion begins only after Point 3, not at Point 2.
- The Helium Flash releases enormous energy ($L\sim10^{11}L_\odot$) but produces **no observable brightening** at the surface — all of it is consumed removing degeneracy in the core. Don't assume "flash" implies a visible flare.
- Only stars with $M<2.2M_\odot$ undergo the He Flash; more massive stars ignite He stably and never reach the RGB tip at the same universal luminosity.
- TRGB standard candle requires the population to be older than ~1–2 Gyr — younger populations don't have stars in the right (low-mass, degenerate) regime yet.
- Mass-loss physics (Reimers $\eta$) is empirical and uncertain — do not treat it as derived from first principles.
- The HB "second parameter problem" is unsolved — don't state age+metallicity as sufficient to fully determine HB morphology.
- The RGB Bump causes a temporary *dimming*, not brightening, as the shell crosses the dredge-up discontinuity — the star briefly moves down before resuming its ascent (a subtlety students often get backwards).
- Second Dredge-Up is significant only for $M>4$–5$M_\odot$; Third Dredge-Up occurs on the AGB (different phase, different mechanism) — don't conflate the two.
- HBB actively *prevents* massive AGB stars from becoming carbon stars by converting dredged-up $^{12}$C back to $^{14}$N — a common trap is to assume all AGB stars with dredge-up become carbon stars.

**Pulsating Stars**
- Maximum luminosity does *not* coincide exactly with minimum radius — the phase lag (from the H-ionization zone) delays peak brightness slightly after minimum radius.
- The κ-mechanism requires opacity to *increase* under compression — opposite to the normal Kramers-law behavior ($\kappa\propto\rho T^{-3.5}$ decreases as $T$ rises); this reversal only happens in partial-ionization zones.
- The He-II zone is the true driving piston; the H-ionization zone is responsible for the phase lag, not the primary driving — don't swap their roles.
- Instability strip edges have two *different* physical causes (blue edge: insufficient overlying mass; red edge: convective damping) — not the same mechanism at both ends.
- The basic P-L relation is a special case of the more general Period-Luminosity-*Color* relation; ignoring color introduces the scatter seen in real P-L diagrams.
- Dynamical stability requires $\gamma>4/3$ — a $\gamma$ below this (e.g., from radiation-pressure domination or strong ionization) causes instability, not sustained pulsation.

**White Dwarfs**
- WD cooling proceeds at **constant radius** (not shrinking) because degenerate pressure is temperature-independent — a frequent error is to assume WDs continue contracting as they cool.
- Mass-radius relation is *inverted* relative to normal stars: more massive WDs are *smaller*.
- The Chandrasekhar mass is a general property of any electron-degenerate structure (also applies to pre-collapse Fe cores) — never equate it with a star's *initial* mass.
- At fixed old age, *more* massive WDs are *more* luminous (they cool more slowly, larger thermal reservoir) — the reverse of naive intuition.
- Not all WDs cool identically: "slowly cooling" WDs (thick residual H layer, from AGB-skipping blue-HB progenitors) can lag by ~1 Gyr — WD chronometry is not perfectly universal.
- Small mass additions to a WD cause large density increases ($\rho\propto M^2$) — relevant for accretion-driven Type Ia ignition, easy to underestimate the sensitivity.

**Final Stages High Mass**
- The boundary masses ($7M_\odot,\ 11M_\odot,\ 25M_\odot$) are approximate and model-dependent (convection, mass loss, nuclear rates) — don't treat them as sharp, universal cutoffs.
- Silicon burning produces $^{56}$Ni, *not* $^{56}$Fe directly — the iron only appears after the post-explosion decay chain; a common error is to assume Fe is synthesized promptly.
- The bulk of pre-collapse iron (from quiescent Si-burning) stays locked inside the remnant — the Fe seen in SN ejecta comes from *explosive* nucleosynthesis in the shock, not from the pre-collapse core.
- The prompt shock *always* stalls (photo-disintegration + neutrino losses) — successful explosions require the *delayed* neutrino-heating mechanism, not the initial bounce alone.
- SN spectral classification (II/Ib/Ic based on H/He presence) reflects progenitor envelope-stripping history, *not* a different explosion mechanism — Ib, Ic, and II are all core-collapse.
- 99% of a Type II SN's total energy escapes as neutrinos — optical luminosity is a tiny (~$10^{-4}$) fraction of the total energy budget; don't judge explosion energy from brightness alone.

**Binary Systems**
- The Roche lobe overflow direction and orbital response depend on *which* star is currently more massive, not on the *original* ZAMS masses — mass ratios invert during transfer.
- Positive vs negative feedback in mass transfer is set by the sign of $(M_1-M_2)$ at the *current* moment, requiring care in multi-stage binary histories (e.g., WD accretor cases).
- A classical nova does *not* destroy the WD — it's a surface event; only Type Ia (reaching $M_{Ch}$) fully disrupts the white dwarf.
- Binary survival after a SN depends on the *ejected mass* relative to *half the total system mass*, not on the ejecta velocity or explosion energy directly.
- Accretion efficiency onto compact objects (especially NS/BH) vastly exceeds nuclear burning efficiency — a common oversight when comparing energy budgets of accretion-powered vs fusion-powered sources.

**Supernovae & Neutron Stars**
- Type Ia and Type II are powered by *completely different* mechanisms (thermonuclear disruption vs core collapse) despite superficially similar peak kinetic energies (~$10^{51}$ erg) — don't conflate spectroscopic similarity with physical similarity.
- A pure detonation model over-produces $^{56}$Ni and is ruled out by observed intermediate-mass elements in Type Ia spectra — real events require deflagration (at least initially).
- Millisecond pulsars are *old*, not young, despite having young-pulsar-like short periods — the recycling scenario (accretion spin-up) resolves this apparent paradox; don't estimate MSP age from $P$ alone.
- The characteristic age $\tau=P/\dot P$ is only a rough estimate and specifically breaks down for recycled (millisecond) pulsars.
- Neutron star masses cluster near $M_{Ch}\approx1.4M_\odot$ for a physical reason (progenitor core mass), not coincidence.
- The Oppenheimer-Volkoff limit, unlike the Chandrasekhar mass, is *not* precisely known — it depends on the poorly-constrained super-nuclear equation of state.

**Black Holes & Gravitational Waves**
- The Newtonian derivation of the Schwarzschild radius gives the numerically correct answer for the wrong physical reason — don't present it as a rigorous GR derivation.
- The event horizon is not a physical/material surface — infalling observers notice nothing special locally when crossing it (for large BHs).
- From a distant observer's perspective, infalling matter never appears to actually cross the horizon (infinite time dilation); this contrasts with the infalling observer's own finite proper time — both descriptions are correct in their respective frames.
- Chirp mass alone cannot determine the individual component masses — an additional measurement (max frequency at merger, or independent EM data) is required to break the mass-ratio degeneracy.
- Detector-frame GW masses are systematically *larger* than source-frame masses by $(1+z)$ — must be corrected using an independently known redshift.
- At solar metallicity, single-star evolution cannot produce BHs above $\sim25M_\odot$ — the massive BHs seen by LIGO essentially require metal-poor progenitors.
- IMBHs remain observationally unconfirmed — treat claimed detections (velocity-dispersion cusps) as evidence, not proof.
