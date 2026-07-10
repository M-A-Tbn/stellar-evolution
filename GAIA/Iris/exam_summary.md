# Stellar Evolution — Exam Summary (Question-Aware Mode)

**Compiled:** 2026-07-05 | **Regenerated:** 2026-07-07 (Black Holes & Gravitational Waves section expanded for completeness) | **Exam date:** 2026-07-08 | **Cross-referenced against:** `Themis/question_bank.md` (71 Qs, real past oral-exam questions)

This is a compressed, exam-prioritized distillation of all Apollo session notes. Items marked with an **EXAM QUESTION** callout are proven high-value — they have been asked in real past exams, sometimes many times over. Topics with heavy repetition (neutron stars, Type II SN mechanism, ZAMS, white dwarfs, 1-vs-5-solar-mass tracks) should be your first priority.

---

## 1. Key Concepts

### 1.1 Foundations (stellar structure, opacity, nucleosynthesis basics)

**[Introduction]** A stellar model is fully specified by two inputs: total mass $M$ and composition $(X,Y,Z)$, $X+Y+Z=1$ (Sun: $X=0.70,Y=0.28,Z=0.02$). Solving the structure equations maps these to one $(L,T_e)$ point on the H-R diagram; as composition evolves, the point traces an **evolutionary track**.

**[Introduction]** H-R diagram axes: $\log(L/L_\odot)$ vertical, $\log T_e$ horizontal, **increasing to the left**.
> **EXAM QUESTION — Q41, Q65:** *"he was extremely persistent that the axes are logarithmic"* / *"Draw the HR Diagram, with its axes and some reference number on them"*

**[Introduction]** Hydrostatic equilibrium: pressure gradient exactly balances gravity at every layer — the condition making a star a stable, long-lived structure rather than collapsing or exploding.

**[Introduction]** Equation of state: total pressure = radiation + ion (perfect gas) + electron (perfect gas, or degenerate non-relativistic/relativistic depending on $T/\rho^{2/3}$).

**[Introduction]** Thermoregulation (perfect gas): $T\uparrow\Rightarrow P\uparrow\Rightarrow$ expansion $\Rightarrow T\downarrow$ — negative feedback stabilizing normal burning.

**[Introduction]** Electron degeneracy: occurs when quantum states below the Fermi level are all Pauli-blocked; pressure becomes density-only, **killing thermoregulation** (→ thermonuclear runaway, e.g. He flash, nova, Type Ia) and making the gas far less compressible (→ WD/NS stability). Only electrons degenerate under stellar conditions — protons never do.

**[Introduction]** Virial theorem / negative heat capacity: $2K+\Omega=0$; a contracting star radiates energy yet **heats up** — half the released gravitational energy heats the gas, half is radiated. Governs pre-MS contraction, RGB/AGB core contraction, and all gravity-dominated phases.

**[Introduction]** Kelvin–Helmholtz timescale: how long gravitational contraction alone could power a star; Sun: ~15 Myr — far short of the 4.5 Gyr geological age, proving fusion (not gravity) powers the MS.

**[Introduction]** Three energy-transport mechanisms: radiation (always active), convection (bulk mixing, homogenizes composition), conduction (negligible except in degenerate gas, where long electron mean free paths make it very efficient — underlies WD isothermal cores).

**[Introduction]** **Schwarzschild criterion**: a displaced gas parcel that arrives hotter (more buoyant) than its surroundings keeps rising → convection. Compares $\nabla_\text{rad}$ to $\nabla_\text{ad}=0.4$ (monatomic ideal gas).
> **EXAM QUESTION — Q11, Q20, Q46:** *"Radiative and convective core, differences"* / *"why the CNO cycle develops convective cores"*

**[Introduction]** Opacity $\kappa(\rho,T)$: resistance to radiation flow, from bound-bound, bound-free (dominant $10^4$–$10^6$K), free-free, and electron-scattering processes. Kramers laws: $\kappa\propto\rho/T^{3.5}$. The He II second-ionization "hump" near $T\sim4\times10^4$K is the key deviation from smooth Kramers decline and the trigger for convective envelopes/pulsation driving.

**[Introduction]** Nuclear binding energy per nucleon peaks at $A\approx56$ (iron) — fusion releases energy only up to iron; beyond it, fusion costs energy. This is the seed of why an iron core has no further energy source and must collapse (see §1.9).

**[Introduction]** PP-chain rate-limiting step ($p+p\to d+e^++\nu$, effective $\beta^+$ decay in a collision) is enormously slow ($t_{1/2}\sim1.4\times10^9$yr) — why the Sun burns for billions, not millions, of years. CNO-cycle bottleneck is $^{14}\text{N}(p,\gamma)$ — causes $^{14}$N to accumulate at the expense of C/O, the fingerprint later seen in dredge-up.

**[Introduction]** Triple-alpha / Hoyle resonance: $2\,^4\text{He}\leftrightarrow{}^8\text{Be}$ (quasi-equilibrium, lifetime $\sim10^{-17}$s), then $^8\text{Be}+{}^4\text{He}\to{}^{12}\text{C}$ — only viable due to the fine-tuned Hoyle resonance in $^{12}$C.

**[Introduction]** s-process (slow neutron capture, capture rate < β⁻ decay rate) walks the valley of stability; r-process (rapid capture, rate > β⁻ decay) builds far-from-stability neutron-rich nuclei that decay back after the flux ends — the only route to the heaviest elements.
> **EXAM QUESTION — Q14:** *"Enrichment of ISM"* (r-process channel)

**[Introduction]** BBN/He problem: stellar nucleosynthesis cannot explain the ~24% He seen even in the oldest, most metal-poor stars — resolved by Big Bang Nucleosynthesis (first ~15 min), giving primordial $Y_p\approx0.24$. The $A=5$/$A=8$ gap halts BBN at He; only the stellar triple-alpha bridge reaches carbon and beyond.

**[Introduction]** Square-bracket abundance notation: $[El/H]=\log(El/H)_*-\log(El/H)_\odot$; $[Fe/H]$ is the standard metallicity proxy — axis definition for the [α/Fe]-[Fe/H] diagnostic (§1.9).

### 1.2 Pre-Main-Sequence Contraction and the Hayashi Track

**[Pre-MS]** Three evolutionary timescales (increasing order): dynamical/free-fall $\tau_d$ (gravity unopposed), Kelvin–Helmholtz $\tau_{KH}$ (virialized, gravitational contraction powers $L$), thermonuclear $\tau_\text{nuc}$ (fusion balances gravity; longest, sets MS lifetime). For $1M_\odot$: $\tau_d\sim$min–$10^2$yr, $\tau_{KH}\sim10^7$yr, $\tau_\text{nuc}\sim10^{10}$yr.

**[Pre-MS]** Core evolution "staircase": alternating KH-contraction segments ($T_c$ rising) and flat nuclear-burning plateaus, for successive fuels H→He→C,O→Ne→O→Si→Fe. Onset of **electron degeneracy** after He-burning is the critical branch point: $M<8M_\odot$ → CO core degenerates, staircase cut off → white dwarf; $M>8M_\odot$ → avoids degeneracy, proceeds to Fe core → core-collapse SN.
> **EXAM QUESTION — Q22, Q28, Q34, Q43:** *"Final fate of stars with different masses"*

**[Pre-MS]** Jeans mass $M_J\propto T^{3/2}\rho^{-1/2}$: gravity beats thermal pressure above this mass. Cold, dense molecular clouds ($T\sim10$–50K) give $M_J\sim1$–$10M_\odot$ — the only ISM phase where star formation is viable; typical ISM $M_J\sim100M_\odot$, so clouds must **fragment** — why stars form in clusters, not isolation.

**[Pre-MS]** Collapse sequence: free-fall collapse (core reaches hydrostatic equilibrium first, envelope still falling) → shock as infalling envelope hits the core (opacity drops, luminosity spikes) → progressive hydrostatic equilibrium spreading outward → **point E**: entire star in HE, fully convective — entry onto the Hayashi track.

**[Pre-MS]** **Hayashi track**: nearly-vertical locus (one per mass) of fully-convective, hydrostatically-equilibrated models, existing because Kramers opacity is so large at low $T_\text{eff}$ that $\nabla_\text{rad}\gg\nabla_\text{ad}$ everywhere. **Hayashi theorem**: no stable HE model exists to the *right* of the track (forbidden zone) — a **universal** constraint at every fully-convective stage (pre-MS *and* giant-branch ascent alike).
> **EXAM QUESTION — Q23, Q65 item 6:** *"What are Hayashi tracks and what is the Hayashi theorem?"*

**[Pre-MS]** Departure from the Hayashi track is mass-dependent: as core $T_c$ rises during KH contraction, higher-mass stars eventually lower core opacity enough ($\kappa\propto T^{-3.5}$) to drop $\nabla_\text{rad}$ below $\nabla_\text{ad}$ centrally, developing a radiative core and bending the track leftward off the Hayashi track before the ZAMS. The lowest-mass stars ($M\lesssim0.3M_\odot$) never get hot enough — they reach the ZAMS still on the Hayashi track and remain fully convective throughout the MS.
> **EXAM QUESTION — Q23, Q41, Q65:** *"role of the Hayashi track"* / *"why stars with M<0.3 solar masses are fully convective"*

**[Pre-MS]** ZAMS reached exactly when $^3\text{He}+^3\text{He}\to{}^4\text{He}+2p$ fully activates (closes the pp chain, needs the highest $T$ of the pp-chain steps). At the ZAMS: $L_\text{nuc}=L_\text{surface}$, full hydrostatic equilibrium, $L_g/L=0$, chemically homogeneous (pre-MS convection mixed everything). Because mass and composition alone fix the structure here, the ZAMS is a clean one-parameter family — the only place a firm mass–luminosity relation holds.
> **EXAM QUESTION — Q17, Q19, Q23, Q41, Q46, Q57, Q64, Q65, Q69:** *"ZAMS: what is, cut-off masses, structure of stars along it"* — VERY FREQUENT, asked almost to everyone.

**[Pre-MS]** Pre-MS duration $t_\text{PMS}\sim4\times10^7(M/M_\odot)^2(R_\odot/R)(L_\odot/L)$ yr — massive stars finish pre-MS far faster ($10M_\odot$: ~$4\times10^4$yr vs $10^7$yr for $1M_\odot$) — explains why young clusters show massive ZAMS stars alongside still-contracting low-mass pre-MS stars.

### 1.3 The ZAMS and Main-Sequence Structure

**[Main Sequence]** ZAMS mass range $0.08$–$90\,M_\odot$, $T_\text{eff}\approx2700$–$53000$K (factor ~20 in $T$ vs factor >1000 in mass). Lower cutoff ($0.08M_\odot$): minimum $T_c$ for pp-chain ignition ($1.4\times10^7$K) — below it, **brown dwarfs**. Upper cutoff ($\approx90M_\odot$): Eddington-luminosity instability.
> **EXAM QUESTION — Q17, Q19, Q41, Q57, Q65, Q69:** *"What are the two cut-off masses on the ZAMS?"*

**[Main Sequence]** **Eddington luminosity** $L_\text{Ed}=4\pi GMc/\kappa$: maximum luminosity compatible with hydrostatic equilibrium ($\kappa\approx0.2(1+X)\approx0.34$ cm²/g, electron scattering). $L_\text{Ed}\approx3.8\times10^4(M/M_\odot)L_\odot$; at $90M_\odot$, actual $L$ is only ~3× below $L_\text{Ed}$ — radiation pressure destabilizes the envelope, driving heavy mass loss and preventing stable formation above ~90–100$M_\odot$.
> **EXAM QUESTION — Q41, Q57:** *"why stars with M>90-100 solar masses are unstable"*

**[Main Sequence]** Three ZAMS structural regimes (transition masses $0.3M_\odot$, $1.2M_\odot$): **$M>1.2M_\odot$** — CNO cycle, concentrated burning (~90% of $L$ in inner ~10% of radius) drives $\nabla_\text{rad}>\nabla_\text{ad}$ centrally → **convective core**/radiative envelope. **$0.3<M/M_\odot<1.2$** — pp chain, diffuse burning (~20–30% of radius) → **radiative core**; envelope convective from Kramers opacity + partial-ionisation suppression of $\nabla_\text{ad}$ (toward ~0.1). **$M<0.3M_\odot$** — **fully convective** throughout (never develops radiative core, Hayashi track ≈ ZAMS position).
> **EXAM QUESTION — Q11, Q17, Q19, Q20, Q23, Q41, Q46, Q57, Q64, Q65, Q69:** *"Structural differences during the main sequence for different masses"*

**[Main Sequence]** Convective-core mechanism in detail: CNO's extreme $T$-sensitivity ($\epsilon_\text{CNO}\propto T_6^{13-20}$) concentrates flux so steeply near the centre that the radiative gradient $\nabla_\text{rad}=\frac{3\kappa\rho}{4acT^3}\frac{L(r)}{4\pi r^2}$ is driven above $\nabla_\text{ad}\approx0.4$ — radiative diffusion alone cannot carry such concentrated flux without an unphysically steep gradient, so convection takes over.
> **EXAM QUESTION — Q46:** *"why the CNO cycle develops convective cores"*

**[Main Sequence]** Metallicity/He effects: higher $Z$ → higher opacity → fainter/cooler ZAMS, longer MS lifetime. Lower $Z$ → CNO suppressed, pp dominates to higher mass. Higher $Y$ → lower opacity but higher $\mu$ → net brighter/hotter, shorter lifetime.

**[Main Sequence]** MS phase = Point 1 (ZAMS) to Point 2 (H-exhaustion, $X_c<0.05$) — longest phase (H-burning most fuel-efficient). $t_\text{MS}\approx10^{10}M^{-3}$yr ($M$ in $M_\odot$) — stars $\lesssim0.8M_\odot$ formed at the Big Bang are still on the MS today.
> **EXAM QUESTION — Q65 item 5:** *"age-mass relation for stars along the ZAMS"*

### 1.4 Evolutionary Tracks: 1 vs. 5 Solar Masses (the most-repeated single topic pair)

**[Main Sequence]** Segment 1–2 track shape: **1$M_\odot$** (pp chain, radiative core, diffuse burning over ~20–30% of radius) — $\mu$-driven core contraction affects a large mass fraction, partially cancelling envelope expansion → track moves slightly **up-and-left**. **5$M_\odot$** (CNO, convective core, confined to inner ~10%) — localized contraction cannot oppose envelope expansion → $R$ grows substantially, $T_\text{eff}$ falls → track moves **up-and-right**. Root cause: different *spatial extent* of nuclear burning, not different total $L$.
> **EXAM QUESTION — Q2, Q25, Q47, Q59, Q65 item 7, Q69:** *"Evolutionary tracks for 1 and 5 solar masses, explain differences"* (×3 in bank — very frequent)

**[Main Sequence]** H-profile shape at point 2: radiative core → smooth gradient, shell already hot when centre exhausts H → **shell ignites immediately, no hook** (points 2≡3). Convective core → flat "step" profile, entire zone exhausted **simultaneously** → brief phase with **no burning anywhere** → gravitational (KH) contraction → **the "hook"** (temporary $T_\text{eff}$ rise) before shell ignites. Observationally confirmed: NGC 1978 CMD turnoff.
> **EXAM QUESTION — Q2, Q11, Q20, Q25, Q47, Q59:** *"reasons for the different shape between point 1 and 2"* / *"hook feature"*

**[Main Sequence]** **Schönberg–Chandrasekhar (SC) limit**: max mass an isothermal, perfect-gas core can support against the overlying envelope: $q_0=0.37(\mu_e/\mu_{ic})^2\approx0.08$, since $\mu_{ic}\approx1.33$ (He-rich core) $\gg\mu_e\approx0.63$ (H-rich envelope). Beyond it, the core contracts on the KH timescale.

**[Main Sequence]** Three post-MS core-fate regimes: **$M>6M_\odot$** — no isothermal phase, core stays ideal gas, ignites He directly. **$2.2$–$6M_\odot$** — temporary isothermal core reaches SC limit, contracts, ignites He non-degenerately (small hook, short RGB). **$M<2.2M_\odot$** — core crosses the electron-degeneracy boundary ($T/\rho^{2/3}<10^5$) *before* the SC limit → degenerate pressure lets the core grow without heating → long RGB ascent → eventual **helium flash**.
> **EXAM QUESTION — Q2, Q25, Q47, Q59:** *"RGB differences (5 vs 1 solar masses)"*

**[Main Sequence]** Point-by-point energy source tracing for a 5$M_\odot$ track to point 6: Point 1–2: CNO core H-burning. Point 2: no nuclear source anywhere (flat profile exhausted simultaneously). Segment 2–3 ("hook"): pure gravitational (KH) contraction. Point 3 onward: thick H-burning shell around inert He core. Segment 5–6: still H-shell, now pinned to Hayashi track, luminosity tracks growing $M_c$ via $L_H\propto\mu^7$. Point 6: quiet, non-degenerate triple-alpha ignition (no flash) plus continuing H-shell.
> **EXAM QUESTION — Q26:** *"just draw it until point 6 and then tell for every point which is the source of energy"*

**[Main Sequence]** Very massive stars (25–50$M_\odot$, Q70/Q71): qualitatively identical early evolution to the 5$M_\odot$ case (CNO convective core, up-and-right track, hook) but the core **never becomes electron-degenerate at any stage** through the full advanced-burning staircase — massive cores have far lower central density (and higher $T$) for a given burning stage. Each successive stage (He→C→Ne→O→Si) is dramatically shorter than the last, driven by escalating neutrino losses forcing KH contraction between stages (H: $\sim10^7$yr; Si: ~1 week).

### 1.5 Post-Main-Sequence: Subgiant Branch and RGB

**[RGB/HB/AGB]** Chemical dichotomy at Point 2: He-rich core ($\mu_i\approx1.33$) beneath unprocessed envelope ($\mu_e\approx0.63$, ratio $\approx2.11$) — the structural trigger for envelope expansion, subgiant branch, and RGB.

**[RGB/HB/AGB]** Envelope-expansion mechanism: continuity of $P,T,M$ at the core–envelope boundary plus the ideal-gas EoS gives a density ratio $\rho_i/\rho_e=\mu_i/\mu_e$; once the H-shell is active ($u>0.3$), the resulting density-gradient ratio falls below $\approx0.22$, forcing the envelope to expand by a factor $\gtrsim4$ — the fundamental origin of the giant branch. Requires **both** chemical dichotomy (point 2) **and** an active shell (point 3) — between them, little expansion occurs.
> **EXAM QUESTION — Q24, Q35:** *"Evolution of a 1 solar mass on the RGB"* / *"…with particular reference to the RGB-bump and 1st dredge-up"*

**[RGB/HB/AGB]** Hertzsprung gap vs. subgiant branch: rapid crossing ($10^5$–$10^7$yr) for $M\gtrsim2M_\odot$ → sparsely populated gap; slow (~$10^9$yr) for $1M_\odot$ → populated SGB — a direct age indicator.

**[RGB/HB/AGB]** RGB energy source: 100% from the thin H-burning shell; $L_H\propto\mu^7$ (extreme composition sensitivity); a near-linear $M_c^{He}$–$L$ relation ties rising core mass directly to rising luminosity. Once pinned to the Hayashi track (cannot move further right — Hayashi theorem), continued expansion can only be accommodated by rising $L$ → nearly-vertical RGB ascent.

**[RGB/HB/AGB]** **First Dredge-Up**: deepening convective envelope reaches CN-processed layers (not full CNO zone): surface $^{12}$C drops ~30%, $^{14}$N roughly doubles, He rises (CN anticorrelation). Leaves a sharp H-abundance discontinuity that the shell will later cross.
> **EXAM QUESTION — Q24, Q33, Q35, Q65:** *"Dredge-up, in particular the third one"* / *"…first dredge-up, RGB bump"*

**[RGB/HB/AGB]** **RGB Bump**: when the outward-moving shell crosses the dredge-up's H-discontinuity, it enters higher-$X$/lower-$\mu$ material; since $L_H\propto\mu^7$, luminosity briefly *drops*, producing a triple crossing of the same luminosity interval. Two independent, confirmed observational signatures: a local peak in the differential RGB luminosity function, and a slope change in the integrated luminosity function.
> **EXAM QUESTION — Q24, Q35, Q65:** *"…RGB-bump and 1st dredge-up"*

**[RGB/HB/AGB]** Electron-degeneracy boundary and the $M=2.2M_\odot$ transition: $M<2.2M_\odot$ crosses it before He ignition (degenerate He-core, delayed ignition, He flash, extended/populated RGB); $M>2.2M_\odot$ never degenerates in the He-core (quiet ignition, short/poorly-populated RGB). Stars $2.2$–$8M_\odot$ still degenerate later in the CO-core.
> **EXAM QUESTION — Q2, Q25, Q47, Q59, Q65, Q69:** *"…which differences appear in the RGB phase"*

### 1.6 The Helium Flash (very frequent topic)

**[RGB/HB/AGB]** **Helium Flash**: thermonuclear runaway of triple-alpha ($\epsilon_{3\alpha}\propto\rho^2Y^3T^{20-30}$) in a degenerate He core ($M<2.2M_\odot$): no ideal-gas thermostat, so heating self-amplifies. Peak internal power $\sim10^{11}L_\odot$ but fully absorbed lifting degeneracy — **never brightens the surface**. Ignites **off-centre** because neutrino cooling (plasma, photoneutrino, pair-annihilation processes) preferentially cools the true centre, creating a temperature inversion. A cascade of secondary sub-flashes works inward over $\sim10^6$yr (only ~5% of He→C converts), removing degeneracy via convection-driven expansion until $T/\rho^{2/3}>10^5$ everywhere. Universal ignition core mass $M_c\approx0.5M_\odot$ regardless of total stellar mass — basis of the TRGB standard candle.
> **EXAM QUESTION — Q6, Q21, Q52, Q58, Q64, Q65, Q69:** *"Helium flash"* / *"what mechanism removes the degeneracy [convection]"*

**[RGB/HB/AGB]** Analogous mechanism at higher mass: carbon ignition in the 7–11$M_\odot$ "mildly degenerate" core behaves like a flash and ignites off-centre for the same neutrino-cooling reason, then propagates inward as a convective flame front — the super-AGB analogue of the He flash (see §1.8).

### 1.7 Horizontal Branch, AGB, Dredge-Up, and Final Fate by Mass

**[RGB/HB/AGB]** **ZAHB and the $q$ parameter**: ZAHB is the He-burning analogue of the ZAMS; since $M_c\approx0.5M_\odot$ is universal, HB position is set by $q=M_c/M_E$ ($M_E$ = evolutionary mass = ZAMS mass minus RGB mass loss): higher $q$ (more mass loss, thinner envelope) → hotter/bluer; lower $q$ → cooler/redder. ZAHB luminosity is essentially fixed at given metallicity ($M_V\approx+0.5$ in metal-poor GCs).
> **EXAM QUESTION — Q52, Q65, Q69:** *"What quantity determines T on the horizontal branch [envelope mass]"* / *"the q parameter"*

**[RGB/HB/AGB]** Mass loss on the RGB — **Reimers law** $\dot M\propto LR/M$ (low surface gravity drives loss); typically 30–40% of initial mass lost by the RGB tip. Sets $M_E$, hence ZAHB position.

**[RGB/HB/AGB]** HB morphology & the "second parameter" problem: age, metallicity, He abundance, and mass loss all shift $M_E$ (hence $T_\text{eff}$); but clusters of matched age/metallicity show very different HB colours, proving at least one more hidden parameter (candidates: He spread, mass-loss efficiency) governs morphology — genuinely unsolved.

**[RGB/HB/AGB]** **EHB / AGB-manqué / UV upturn**: extreme-HB stars have envelopes too thin to sustain the AGB double-shell phase; they bypass it entirely: EHB → AGB-manqué → post-HB blue subdwarf → WD cooling track.
> **EXAM QUESTION — Q65, Q69:** *"What happens for very-low mass stars after the ZAHB? [AGB manqué]"*

**[RGB/HB/AGB]** Convective-core growth during He-burning is **opposite** of MS behaviour: as He→C,O, opacity *rises* (CO plasma more opaque than He), so the convective core *grows* over time (vs. shrinking during H-burning). Produces overshooting and a semi-convective zone between core and radiative He envelope.

**[RGB/HB/AGB]** AGB structure ($M^\text{up}=8M_\odot$ boundary): CO core / He-shell / He-intershell / H-shell / envelope, double-shell burning. $M<8M_\odot$: CO core degenerates → AGB + thermal pulses → planetary nebula → CO-WD. $M>8M_\odot$: CO core stays non-degenerate, carbon ignites stably → continues to Type II SN.

**[RGB/HB/AGB]** **Second Dredge-Up** (E-AGB, only $M>4$–$5M_\odot$): He-shell ignition switches off the H-shell; envelope deepens enough to bring CN-processed material (He, $^{14}$N up, $^{12}$C down) to the surface.

**[RGB/HB/AGB]** **TP-AGB thermal-pulse cycle**: H-shell deposits He into the intershell until a critical mass triggers a thermal pulse (He-shell runaway, $L_\text{He}\sim10^6$–$10^7L_\odot$ briefly), driving intershell convection and switching off the H-shell; He-shell fades, H-shell reignites, cycle repeats.

**[RGB/HB/AGB]** **Third Dredge-Up**: requires two *sequential* convective events — (1) intershell convection from the thermal-pulse flash enriches the intershell with fresh C, O; (2) *later*, separately-deepening envelope convection penetrates into that enriched intershell and carries C/O to the surface. Repeated episodes push surface C/O above 1 → **Carbon Star** (C₂, CN, CH bands). Also exposes s-process elements.
> **EXAM QUESTION — Q33:** *"Dredge-up, in particular the third one"*

**[RGB/HB/AGB]** s-process neutron sources: $^{22}\text{Ne}(\alpha,n)^{25}\text{Mg}$ (needs $T\sim3.5\times10^8$K, only $M>3M_\odot$ AGB) and $^{13}\text{C}(\alpha,n)^{16}\text{O}$ (needs $T\sim9\times10^7$K, requires protons mixed into the C-rich intershell after 3rd dredge-up). $^{14}$N is a severe neutron poison.

**[RGB/HB/AGB]** **Hot Bottom Burning (HBB)**, AGB $M>6$–$7M_\odot$: envelope-base CNO burning converts freshly dredged-up $^{12}$C back to $^{14}$N — **why the most massive AGB stars do NOT become carbon stars** despite vigorous 3rd dredge-up. Also produces Li via the Cameron–Fowler mechanism.

**[RGB/HB/AGB]** **Final fate by mass — complete table**: $<0.08M_\odot$ brown dwarf (never ignites H); $0.08$–$0.5M_\odot$ He never ignites → He-WD; $0.5$–$2.2M_\odot$ degenerate He-flash then degenerate CO-core → CO-WD; $2.2$–$7$–$8M_\odot$ quiet He ignition, CO-core degenerates later → CO-WD; $7$–$11M_\odot$ carbon flash → ONe-WD or electron-capture SN → NS; $11$–$25M_\odot$ full burning to Fe → Type II SN → NS; $>25M_\odot$ → Type II SN (or failed/fallback) → BH.
> **EXAM QUESTION — Q22, Q28, Q34, Q43, Q64, Q65, Q69, Q70, Q71:** *"Final fate/stages of evolution as a function of initial mass"* (professor "extremely persistent on exact mass values")

**[RGB/HB/AGB]** Full evolutionary sequence, low-mass star ($0.5<M/M_\odot<2.2$): ZAMS → SGB → RGB (Hayashi-pinned, 1st dredge-up, RGB bump, growing degeneracy) → He Flash (off-centre cascade, $M_c\approx0.5M_\odot$) → ZAHB → HB loop → E-AGB (2nd dredge-up if $M>4$–$5M_\odot$) → TP-AGB (thermal pulses, 3rd dredge-up, s-process, HBB if massive) → Planetary Nebula → CO White Dwarf.
> **EXAM QUESTION — Q35, Q65:** *"Evolution of a 1 solar mass star from the ZAMS till it's WD phase"*

### 1.8 Standard Candles

**[RGB/HB/AGB]** **TRGB (Tip of the RGB)**: fixed luminosity $\log(L/L_\odot)\approx3.45$, $M_I\approx-4.0$ for any population with $M<2.2M_\odot$ stars present (age $\gtrsim1$–2 Gyr) — a primary distance indicator for resolved nearby galaxies.
> **EXAM QUESTION — Q36, Q64:** *"Standard candles"* / *"RGB (could be used as standard candles)"*

**[Pulsating Stars]** **Cepheid Period-Luminosity relation**: $M_V=-2.8\log P_\text{days}-1.43$ (Leavitt, >2000 SMC Cepheids at common distance) — first rung of the cosmic distance ladder.

**[SNe & Neutron Stars]** **Type Ia SNe** as (secondary/calibrated) standard candles: peak $M_B\approx-19.6$, standardised via the Phillips/stretch-factor relation — the tool that discovered cosmic acceleration.

**[RGB/HB/AGB]** ZAHB luminosity is also an independent (fixed core mass) distance indicator; RR Lyrae stars (nearly constant $M_V\approx+0.5$) are another.
> **EXAM QUESTION — Q36:** *"which objects are used as standard candles"*

### 1.9 Advanced Burning Stages and Nucleosynthesis (High-Mass Stars)

**[Final Stages High Mass]** Mass-dependent core-degeneracy outcomes: $<0.5M_\odot$ permanently degenerate He core → He-WD; up to ~7$M_\odot$ degenerate CO core → CO-WD; **7–11$M_\odot$** mildly degenerate CO/ONe core → O-Ne WD or electron-capture SN; **>11$M_\odot$** non-degenerate Fe core → Type II core-collapse SN. $M^\text{up}\approx8M_\odot$ separates WD-forming from NS/BH-forming stars.

**[Final Stages High Mass]** Carbon ignition (7–11$M_\odot$, "mildly degenerate", $T\sim5$–$6\times10^8$K): behaves as a flash (partial degeneracy decouples $P$ from $T$), ignites **off-centre** (neutrino cooling), then propagates inward as a convective flame front until stable central burning is established. Super-AGB phase features 2nd dredge-up, He-shell thermal pulses, 3rd dredge-up, and "dredge-out."

**[Final Stages High Mass]** O-Ne WD vs. electron-capture SN: if winds strip the envelope before the O-Ne-Mg core reaches $M_\text{Ch}\approx1.4M_\odot$ → O-Ne WD (mass 1.0–1.2$M_\odot$, cools *faster* than CO-WD of equal mass due to larger mean atomic mass → smaller heat capacity); if the core reaches $M_\text{Ch}$ first → **electron-capture supernova**: electron capture on $^{24}$Mg/$^{20}$Ne removes pressure support → runaway → O ignites at $\rho\sim2.5\times10^{10}$g/cm³ as a semi-degenerate deflagration → collapse to NS (weak explosion, low $^{56}$Ni).
> **EXAM QUESTION — Q12, Q61:** *"WDs... CO;Ne;He WDs"*

**[Final Stages High Mass]** Advanced burning staircase ($M>11M_\odot$, all non-degenerate): H→He→C→Ne→O→Si→Fe(inert). Neon burning is **photodisintegration + alpha-capture** ($^{20}\text{Ne}+\gamma\to{}^{16}\text{O}+{}^4\text{He}$, then $^{20}\text{Ne}+{}^4\text{He}\to{}^{24}\text{Mg}+\gamma$), not direct fusion. Silicon burning is a **photo-disintegration cascade** feeding the alpha-capture chain up to the iron peak — **nuclear statistical equilibrium (NSE)**.
> **EXAM QUESTION — Q15:** *"Alpha capture chain"*

**[Final Stages High Mass]** Onion-shell structure at end of Si-burning (outside-in): H shell, He shell, C shell, O shell, Ne (vestigial), Si-burning shell, inert Fe core ($M\approx1.3$–$2.0M_\odot$).

**[SNe & Neutron Stars]** [α/Fe]–[Fe/H] diagram: α-elements (O, Mg, Ca, Si, Ti) come promptly from Type II SNe (<30 Myr); Fe comes with a substantial delay from Type Ia SNe (~30–35 Myr up to a Hubble time). **Plateau** height set by IMF (top-heavy → higher plateau); **knee** position set by SFR (higher SFR → knee at higher [Fe/H]). Dwarf galaxies (low SFR): knee [Fe/H]≈−1.5; Galactic halo: ≈−1.0; Galactic bulge (high SFR): ≈−0.3 to 0.0 — a "chemical DNA" fingerprint of star-formation history.
> **EXAM QUESTION — Q31, Q71:** *"What information can we derive from the alpha/Fe - Fe/H diagram?"*

**[SNe & Neutron Stars]** ISM enrichment channels: planetary nebulae (CNO/He-burning products, s-process, Li); novae (rare CNO isotopes, small mass); Type II SNe (α-elements, ~0.1$M_\odot$ Fe/event, ~1/3 of Galactic Fe, r-process from innermost ejecta); Type Ia SNe (~0.6$M_\odot$ Fe/event, ~2/3 of Galactic Fe, no α-enhancement); NS mergers/kilonovae (r-process heaviest elements, confirmed GW170817/AT2017gfo).
> **EXAM QUESTION — Q14:** *"Enrichment of ISM"*

### 1.10 Type II (Core-Collapse) Supernova Mechanism (single highest-priority mechanism in the course)

**[Final Stages / SNe & Neutron Stars]** **Why the iron core collapses**: iron sits at the peak of nuclear binding energy per nucleon — no fusion energy available. Three processes strip pressure support: **(1) electron capture** on Fe-group nuclei ($^{56}\text{Fe}+e^-\to{}^{56}\text{Mn}+\nu_e$) — reduces electron-degeneracy pressure, radiates neutrinos; **(2) photodisintegration** of iron at $T\sim5$–$10\times10^9$K ($^{56}\text{Fe}+\gamma\to13\,^4\text{He}+4n$), endothermic, absorbing ~124 MeV/nucleus — reverses the star's entire nucleosynthesis history; **(3) URCA process** ($p^++e^-\to n+\nu_e$) on liberated protons — named after a Rio de Janeiro casino because energy is lost with nothing returned. Combined neutrino luminosity ~$3\times10^{45}$erg/s for a 20$M_\odot$ core. Together these drop the effective adiabatic index $\Gamma$ below 4/3 → free-fall collapse.
> **EXAM QUESTION — Q3–Q10, Q13, Q18, Q29, Q30, Q37, Q42, Q45, Q48, Q53, Q56, Q60, Q64, Q65, Q68, Q69, Q70, Q71:** *"Photodisintegration and URCA process in SNe II"* / *"Neutron stars... physical reason for their existence"* / *"Mechanism of explosion of a type II SN"* / *"URCA process — describe the main steps"* — **the single most-repeated topic-set in the entire bank.**

**[SNe & Neutron Stars]** Free-fall collapse ($\tau_d\sim10$ms) from ~1000 km to nuclear density $\rho_\text{nuc}\approx2.4\times10^{14}$g/cm³. **Core bounce**: the strong nuclear force turns repulsive at $\rho_\text{nuc}$; inner core (~0.7$M_\odot$) overshoots and rebounds, launching an outward pressure wave that steepens into a shock at the sonic surface.
> **EXAM QUESTION — Q60:** *"focus on the process of rebound"*

**[SNe & Neutron Stars]** Why the prompt shock stalls: (1) photodisintegrating infalling iron layers costs ~$10^{51}$erg per 0.1$M_\odot$ traversed; (2) neutrino cooling from the compressed post-shock layer. Stalls at $r\sim100$–200 km within milliseconds.

**[SNe & Neutron Stars]** **Delayed neutrino-heating mechanism** (Wilson 1985): below the **neutrino-sphere**, neutrinos are trapped, diffusing slowly, carrying ~$3\times10^{53}$erg. In the **gain region** just above it, a small fraction is absorbed ($\nu_e+n\leftrightarrow e^-+p$, $\bar\nu_e+p\leftrightarrow n+e^+$), depositing ~$10^{51}$erg and reviving the shock 100–500 ms post-bounce — final ejecta KE ~$10^{51}$erg (1 Bethe). Only ~1% of the total energy budget emerges as kinetic/optical; ~99% is radiated as neutrinos (confirmed for SN1987A).
> **EXAM QUESTION — Q18, Q29, Q30, Q60, Q68:** *"Mechanism of explosion of a type II SN"*

**[SNe & Neutron Stars]** Iron is NOT ejected from pre-collapse fusion — that mass stays locked in the compact remnant. Ejected Fe (Type II's ~1/3 share of Galactic Fe) comes from **explosive** Si-burning in the shock ($^{56}\text{Ni}\to{}^{56}\text{Co}\to{}^{56}\text{Fe}$, half-lives 6.1d and 77.1d — this decay chain powers the late-time light curve).

### 1.11 SNe Classification and Type Ia Mechanism

**[SNe & Neutron Stars]** Two independent classification axes: **spectroscopic** (Type II = H present; Type I = no H, subdivided by Si [Ia] and He [Ib/Ic — Ib retains He, Ic has neither]) vs. **mechanistic** (Ia = thermonuclear WD disruption, no remnant; II/Ib/Ic = core collapse, leaves NS/BH). Spectroscopic Type I does **not** imply a common mechanism.
> **EXAM QUESTION — Q42, Q45, Q53, Q56:** *"SNe types"*

**[SNe & Neutron Stars]** SN Ia progenitors: **double-degenerate (DD)** — two CO-WDs from a primordial 5–9$M_\odot$ binary, two common-envelope episodes, GW-driven inspiral/merger once combined mass exceeds $M_\text{Ch}$; **single-degenerate (SD)** — CO-WD accretes H-rich material from a non-degenerate companion, viable only in a narrow intermediate-$\dot M$ window. **Key clarification**: reaching $M_\text{Ch}$ alone is not sufficient — the explosion requires **ignition of a degenerate fuel** (carbon, at $\rho\approx10^9$g/cm³).
> **EXAM QUESTION — Q62:** *"SNIa: specifically DD scenario"*

**[SNe & Neutron Stars]** Deflagration (subsonic, W7 model — produces layered Fe-peak/intermediate-mass ejecta matching observations reasonably) vs. detonation (supersonic, pure form ruled out — would produce only Ni, no Si/S/Ca) vs. **delayed detonation** (deflagration transitioning to detonation as the compression wave crosses lower-density outer layers) — best match to observed spectra/light curves.
> **EXAM QUESTION — Q56:** *"deflagration+detonation mechanism"*

### 1.12 Neutron Stars (single most-repeated topic in the whole bank)

**[SNe & Neutron Stars]** Neutron star properties: mass $1.2$–$2.5M_\odot$ (peak ~$1.4M_\odot$ = Chandrasekhar mass, since collapsing cores were degeneracy-supported pre-collapse and retain most of that mass); $R\approx10$–15 km; $\rho_c\approx10^{14}$–$10^{15}$g/cm³. Supported by **neutron degeneracy pressure**, inverse mass-radius relation (same physics as WD with $m_e\to m_n$); maximum mass = **Oppenheimer–Volkoff limit** ~2.5–3$M_\odot$ (poorly constrained — depends on unresolved super-nuclear equation of state).
> **EXAM QUESTION — Q3–Q10, Q51, Q63, Q64, Q65, Q69, Q70, Q71:** *"Neutron stars — what are they, what are the properties, what is the physical reason for their existence"* — asked as the literal same question **nine times** (Q3–Q10 + Q51), plus embedded in 6+ composite questions. **The single highest-priority topic in this entire course.**

**[SNe & Neutron Stars]** Internal layering: **outer crust** ($10^6$–$10^{11}$g/cm³, Coulomb lattice + relativistic degenerate electrons, "neutronization" — β⁻ decay forbidden by Pauli blocking); **inner crust** ($10^{11}$–$10^{12}$, beyond **neutron drip** at $\sim4\times10^{11}$g/cm³); **interior** ($\sim10^{14}$, nuclei dissolved, $n{:}p{:}e\approx8{:}1{:}1$); **exotic core** (>$4\times10^{14}$, superfluid neutrons, superconducting protons, possibly quark matter — genuinely unresolved physics).

**[SNe & Neutron Stars]** Collapse produces a **~500× radius reduction**, which via **conservation of angular momentum** (millisecond birth periods) and **conservation of magnetic flux** (amplification to $B\sim10^{13}$–$10^{14}$G) naturally produces the defining pulsar properties: fast rotation + enormous field.
> **EXAM QUESTION — Q3–Q10, Q63, Q71:** *"conservation of angular momentum"* / *"Differences btw WD and NS"*

**[SNe & Neutron Stars]** NS cooling: born $T\sim10^{11}$K, drops to $\sim10^8$K within ~100yr, $\sim10^6$K by $\sim10^5$yr (neutrino- then photon-dominated); isolated NSs mainly seen as pulsars (rotational, not thermal, power).

**[SNe & Neutron Stars]** **Pulsars** (1967, Bell): periods 0.2–2s typical (down to 1.6ms for MSPs), extraordinarily regular. Emission: induced surface E-field accelerates charged particles → curvature radiation → pair-production cascade → coherent beam. **Light cylinder** $R_\text{lc}=cP/2\pi$: field lines closing within it trap particles; those crossing it carry away energy/angular momentum (braking mechanism).

**[SNe & Neutron Stars]** **Crab Pulsar** proof-of-concept: spindown power $dK/dt\approx5\times10^{38}$erg/s exactly matches the Crab Nebula's synchrotron luminosity — definitive proof pulsars power their SN remnants via rotational energy loss.
> **EXAM QUESTION — Q51:** *"rotational kinetic energy... powers pulsar-wind nebulae such as the Crab"*

**[SNe & Neutron Stars]** **P–$\dot P$ diagram**: young pulsars upper-left (short $P$, high $\dot P$), evolve toward lower-right (spin-down, $B\propto\sqrt{P\dot P}$, constant-B lines diagonal) until crossing the **death line** ($P\approx2.42\times10^{-6}\sqrt B$ s) into the pulsar graveyard. Characteristic age $\tau=P/\dot P$.
> **EXAM QUESTION — Q51, Q65 item 17, Q71:** *"Draw the P-Pdot diagram"*

**[SNe & Neutron Stars]** **Millisecond pulsars (MSPs)**: paradox of very short $P$ *and* very low $\dot P$ resolved by the **recycling scenario** — an old, spun-down NS in a binary is spun back up by accreting mass/angular momentum from an evolving companion, leaving an MSP + stripped low-mass **He-WD** companion binary. Confirmed by PSR 1937+214 ($P=1.5$ms, $\tau\approx5\times10^8$yr). This is also **how He-WDs are observed at all** — isolated single-star He-WD progenitors ($M<0.5M_\odot$) have MS lifetimes exceeding the Hubble time.
> **EXAM QUESTION — Q4, Q10, Q51, Q65:** *"What are the millisecond pulsars?"* / *"How can we observe He WDs?"*

**[SNe & Neutron Stars]** "Weird question" reasoning (Q71): young pulsars showing *longer* periods than naive angular-momentum-conservation predicts — explained by progenitor mass loss (winds/RLOF carrying away disproportionate angular momentum), asymmetric fallback/kicks, or pre-collapse core spin-down via magnetic torques — this exceeds rote lecture content and rewards reasoned inference.
> **EXAM QUESTION — Q71:** *"why we observe young pulsars with longer periods than expected"*

**[Final Stages High Mass / Black Holes]** NS-vs-BH fate determinants beyond ZAMS mass: **(1) fallback** of SN ejecta (if ≥~1$M_\odot$ falls back, exceeds OV limit → BH; more likely $M>30M_\odot$); **(2) binary mass accretion/donation** (mass gainers favour BH; donors, stripped by RLOF, favour lower-mass NS); **(3) metallicity-dependent wind mass loss** ($\dot M\propto Z^{0.5-0.9}$ — metal-poor stars retain more mass → more massive remnants, why LIGO's massive BHs are thought metal-poor). Diagnostic: **compactness parameter** $\xi_{2.5}=(M/M_\odot)/(R(M)/1000\text{km})$: $<0.2$ → successful SN/NS; $>0.2$ → failed SN/direct BH (non-monotonic in mass: $<18M_\odot$ mostly explode, 18–26 mixed, >26 mostly fail).
> **EXAM QUESTION — Q71:** *"what phenomena can determine if a star ends up as a black hole or neutron star"*

### 1.13 White Dwarfs

**[White Dwarfs]** A white dwarf is the electron-degenerate remnant of $M\lesssim8M_\odot$: an AGB **superwind** ($\dot M\sim10^{-4}M_\odot$/yr) strips the envelope, exposing the hot core; once $T_\text{eff}\sim30{,}000$K the core ionises the ejected shell into a **planetary nebula**, then the remnant fades onto the WD cooling track.
> **EXAM QUESTION — Q12, Q44, Q55, Q61, Q67:** *"WDs, main characteristics"* / *"General properties of a WD"*

**[White Dwarfs]** Prototype **Sirius B** ($M\approx1.05M_\odot$, $R=5.5\times10^8$cm, $\rho\approx3\times10^6$g/cm³). $L_\text{WD}\sim10^{-3}L_\odot$ restricts observability to $d\lesssim14$kpc (Galaxy only), despite ~95% of all stars ending as WDs.

**[White Dwarfs]** Internal layering: dominant degenerate core (CO/ONe/He) → thin non-degenerate He layer ($M_\text{He}\sim10^{-2}M_\text{WD}$) → even thinner non-degenerate H layer ($M_\text{H}\sim10^{-4}M_\text{WD}$).

**[White Dwarfs]** Compositional classes: **CO-WD** (great majority, progenitors 0.5–8$M_\odot$; $3\,^4\text{He}\to{}^{12}\text{C}$ then $^{12}\text{C}+{}^4\text{He}\to{}^{16}\text{O}$, O typically dominant); **ONe-WD** (progenitors 7–11$M_\odot$, super-AGB channel); **He-WD** (progenitors <0.5$M_\odot$, only observed via binary stripping since MS lifetime exceeds Hubble time).
> **EXAM QUESTION — Q10, Q12, Q61, Q65, Q67:** *"CO;Ne;He WDs"* / *"how can we observe He WDs?"*

**[White Dwarfs]** Spectral classification (from gravitational settling under $\log g\approx8.4$): **DA** (~80%, H lines), **DB** (~8%, He lines), **DC** (~14%, featureless).

**[White Dwarfs]** **Mass–radius relation**: non-relativistically $P\propto\rho^{5/3}$, giving $M^{1/3}R\approx$const, i.e. $R\propto M^{-1/3}$ — **more massive WDs are smaller**, opposite of ordinary stars, because higher mass → higher density → tighter electron packing → higher degeneracy pressure per particle → smaller equilibrium radius.
> **EXAM QUESTION — Q12, Q39, Q44, Q49, Q55, Q61, Q63, Q67:** *"Mass-radius relation"* / *"why the mass-radius relation exists"*

**[White Dwarfs]** **Chandrasekhar mass** $M_\text{Ch}\approx1.44(1+X)^2M_\odot\approx1.44M_\odot$: in the ultra-relativistic limit ($v\to c$), degenerate pressure steepens to $P\propto\rho^{4/3}$, matching gravity's density scaling exactly at fixed mass — hydrostatic balance selects one unique mass, not a radius. **General result — NOT WD-specific**: applies to any electron-degenerate substructure (WD or a massive star's pre-collapse iron core); what matters is the mass of the degenerate substructure, never the progenitor's initial mass.
> **EXAM QUESTION — Q16:** *"Chandrasekhar-mass limit definition"*

**[White Dwarfs]** **Isothermal core**: Pauli blocking gives degenerate electrons very long mean free paths → extremely efficient thermal conduction → the entire degenerate core sits at one uniform $T_c\sim10^7$K; only the thin non-degenerate envelope shows a steep temperature drop.
> **EXAM QUESTION — Q50, Q55, Q69:** *"Temperature profile inside the WD"*

**[White Dwarfs]** WD cooling is pure cooling at constant radius — no burning, no contraction possible — powered by declining ionic thermal energy $U=(M_\text{WD}/Am_H)(3/2)kT_c$. **Mestel cooling law** governs it; **crystallisation** (CO ions freeze into a lattice, releasing latent heat) produces an observed plateau at $\log(L/L_\odot)\approx-4$.
> **EXAM QUESTION — Q34, Q39, Q40, Q44, Q49, Q55, Q61, Q67, Q69:** *"WDs cooling tracks"*

**[White Dwarfs]** **Slow-cooling white dwarfs** (Chen et al. 2021): M13 (blue/extended HB) shows a ~50% WD excess over "twin" cluster M3 (red HB) after RGB-normalisation. Cause: extreme-blue-HB progenitors have envelopes so thin they **skip the AGB phase** (and 3rd dredge-up), retaining $M_H>10^{-4}M_\text{WD}$ — thick enough to sustain stable residual pp/CNO burning, slowing cooling by up to ~1 Gyr. Confirmed also in M5, NGC 6752. Implication: WD cooling is **not** a perfectly universal chronometer — must correct for progenitor HB morphology.
> **EXAM QUESTION — Q40, Q65:** *"Slow cooling WDs"*

**[White Dwarfs]** WD accretion & Type Ia trigger: because $\rho\propto M^2$ (from $M^{1/3}R\approx$const), even small accreted mass drives a large central-density increase — the link between binary accretion and pushing a CO-WD toward degenerate carbon ignition at $M_\text{Ch}$.
> **EXAM QUESTION — Q38, Q62:** *"Mass accretion on a WD in a binary system"*

### 1.14 Pulsating Stars

**[Pulsating Stars]** Pulsating stars oscillate radially — $R$ and $T_e$ vary in anti-phase (compression heats, expansion cools); since $L=4\pi R^2\sigma T_e^4$ and $\Delta T_e/T_e$ (~15%) dominates $\Delta R/R$ (~10%) once raised to the 4th power, max luminosity ≈ max temperature ≈ min radius.
> **EXAM QUESTION — Q1, Q27, Q54, Q66:** *"Pulsating stars and why are they important"*

**[Pulsating Stars]** **Instability Strip**: narrow near-vertical HRD band ($T_\text{eff}\approx6300$–7100K), crossed by tracks of many masses. Classes by luminosity (faint→bright): δ Scuti (MS/near-MS, Pop I), RR Lyrae (HB core-He-burning, Pop II, nearly-fixed $M_V\approx+0.5$), W Virginis (Pop II Cepheid-analogue), Classical Cepheids (Pop I supergiants). Outside strip: ZZ Ceti (pulsating WDs), Miras/LPVs (cool AGB).
> **EXAM QUESTION — Q54:** *"careful with the position of the various classes along the H-R diagram"*

**[Pulsating Stars]** Stars cross the strip up to 3×: fast 1st crossing (post-MS expansion), **slow 2nd crossing** (core He-burning/HB — produces the bulk of observed pulsators), fast 3rd crossing (toward AGB).

**[Pulsating Stars]** Driving mechanism = **κ-mechanism** in partial-ionisation zones: compression → extra ionisation (not just heating) → opacity *rises* (traps heat); expansion → recombination → opacity *falls* (releases heat) — a thermodynamic valve. **He II→He III** ($T\approx4\times10^4$K) is the real **piston** — removing it kills pulsation entirely. **H/He I ionisation** ($T\approx1.5\times10^4$K) produces the observed **phase lag** (max luminosity slightly *after* min radius).
> **EXAM QUESTION — Q1, Q27, Q54, Q66, Q65:** *"what's the origin of pulsation"*

**[Pulsating Stars]** Instability strip edges: blue edge (~7100K) — ionisation zones too shallow to drive; red edge (~6300K) — surface convection sets in and damps the κ-mechanism. Dynamical stability requires $\gamma>4/3$.

**[Pulsating Stars]** The Period–Luminosity relation is really a **Period-Luminosity-Colour (PLC)** relation; the simple PL law is the PLC evaluated at mean Cepheid colour — mixing different-metallicity populations inflates scatter.

### 1.15 Binary Systems

**[Binary Systems]** Roche potential (co-rotating frame) = both stars' gravity + centrifugal term; equipotentials form a figure-eight at the critical (Roche-lobe) value passing through $L_1$ (saddle/unstable point). $L_2,L_3$ also unstable; $L_4,L_5$ stable if $M_1/M_2>25$.
> **EXAM QUESTION — Q32:** *"Binary Systems"*

**[Binary Systems]** Classification: detached (both smaller than Roche lobes, evolve independently) / semidetached (one fills lobe, mass flows through $L_1$, may form Keplerian accretion disk) / contact (both overflow, common envelope — inherently short-lived: merger or envelope ejection).

**[Binary Systems]** **Blue Straggler Stars**: appear brighter/bluer than the cluster MS-turnoff — forbidden for single-star evolution; formed via mass-transfer rejuvenation or direct MS-MS merger — direct observational proof binary interaction matters.

**[Binary Systems]** Accretion energetics: $K=GMm/R$ per unit mass — WD $\sim10^{17}$erg/g; NS $\sim10^{20}$erg/g (**30× H-burning's** $\sim6\times10^{18}$erg/g) — basis of X-ray binaries.
> **EXAM QUESTION — Q32:** *"Binary Systems"* (accretion energetics component)

**[Binary Systems]** Cataclysmic variables/novae: low $\dot M\sim10^{-11}M_\odot$/yr → disk-instability dwarf novae (no burning); $\dot M\sim10^{-8}$–$10^{-9}$ → classical novae: degenerate accreted H layer (~$10^{-4}M_\odot$) undergoes CNO-cycle thermonuclear runaway, ejects most of the envelope, repeats every $10^4$–$10^5$yr — WD survives.
> **EXAM QUESTION — Q38:** *"Mass accretion on a WD in a binary system"*

**[Binary Systems]** Binary survival after a SN kick: bound only if ejected mass $\delta m<(M_1+M_2)/2$ — prior RLOF stripping (leaving only a He/CO core to explode) is what makes bound NS/BH+companion systems (X-ray binaries, recycled pulsars) possible.
> **EXAM QUESTION — Q32, Q71:** *"fallback of SN ejecta, mass accretion in a binary system, mass loss"* (binary-survival component)

**[Binary Systems]** Common-envelope evolution: drag inside a shared envelope extracts orbital energy, shrinking separation drastically (e.g. HS 2231+2441: brown dwarf spiralling through and ejecting a giant's envelope, leaving a stripped He-WD in an extremely tight orbit).

### 1.16 Black Holes and Gravitational Waves

**[Black Holes & GW]** Newtonian precursor: setting escape velocity $\geq c$ (George Michell, 1784, "dark stars") gives the same numerical Schwarzschild radius as general relativity, but for the wrong physical reason — the true GR picture is not "gravity too strong to escape" but spacetime curved so severely that every future light cone points inward.

**[Black Holes & GW]** **Schwarzschild radius** $R_s=2GM/c^2=3(M/M_\odot)$ km — must be memorised; sets the compactness scale distinguishing a BH ($R=R_s$) from a WD ($R\sim10^4$ km) or NS ($R\sim10$ km) of comparable mass.

**[Black Holes & GW]** **Schwarzschild metric** (spacetime outside any static spherical mass) has two measurable consequences as $r\to R_s$: proper radial distance $dL=dr/\sqrt{1-R_s/r}>dr$ diverges (the interior is "infinitely far" as measured from outside), and gravitational time dilation $d\tau=dt\sqrt{1-R_s/r}<dt$ means a distant observer sees infalling clocks freeze asymptotically at the horizon, even though the infalling observer crosses it in finite proper time. Coordinate light speed $dr/dt=c(1-R_s/r)\to0$ at $r=R_s$ — light appears frozen at the horizon from outside.

**[Black Holes & GW]** **Event horizon** ($r=R_s$): not a physical surface — an infalling observer feels nothing crossing it locally. Geometrically, light cones tip progressively toward the centre approaching a BH; at $R_s$ the outward null ray lies exactly along the horizon; inside, the *entire* future light cone points toward the singularity — matter is not "pulled back," every possible future simply leads inward.

**[Black Holes & GW]** **Singularity & Cosmic Censorship**: GR predicts infinite curvature at $r=0$ — the theory predicting its own breakdown, signalling the need for quantum gravity. Cosmic Censorship (an unproven conjecture, though supported by all known exact collapse solutions) holds that singularities are always hidden behind an event horizon and are never directly ("naked") observable.

**[Black Holes & GW]** Black hole formation: once a CC-SN remnant exceeds the Oppenheimer–Volkoff limit (~2.5–3$M_\odot$, ZAMS mass ~25$M_\odot$ and up), neutron degeneracy pressure cannot halt collapse and total gravitational collapse to a BH follows.

**[Black Holes & GW]** **Compactness parameter** $\xi_{2.5}=(M/M_\odot)/(R(M)/1000\text{km})$, evaluated at Fe-core infall over the innermost $2.5M_\odot$ (PARSEC+MESA models): $\xi_{2.5}<0.2\Rightarrow$ successful SN/NS; $>0.2\Rightarrow$ failed SN/direct BH (no optical transient, the whole star swallowed). Non-monotonic in $M_\text{ZAMS}$: $<18M_\odot$ mostly explode; $18$–$26M_\odot$ a genuinely mixed regime; $>26M_\odot$ mostly fail.
> **EXAM QUESTION — Q71:** *"what phenomena can determine if a star ends up as a black hole or neutron star"*

**[Black Holes & GW]** Remnant mass vs. metallicity: radiation-driven winds on metal ions give $\dot M\propto Z^{0.5-0.9}$, so metal-poor stars retain more mass and build larger CO cores (up to $\sim65M_\odot$ at $Z\sim10^{-4}$ vs. $\sim20M_\odot$ at solar $Z$, same $M_\text{ZAMS}$) and hence more massive remnants. At solar metallicity, no remnant exceeds $25M_\odot$ for any $M_\text{ZAMS}$ up to $150M_\odot$ — the massive ($\sim30$–$60M_\odot$) BHs seen by LIGO must come from metal-poor progenitors (early Universe, metal-poor satellites, or dense dynamical environments), not solar-metallicity single-star evolution.

**[Black Holes & GW]** BH mass classes: **stellar-mass** ($\lesssim50$–$100M_\odot$, from CC-SN or mergers; X-ray binaries show $\sim5$–$15M_\odot$, LIGO shows $\sim10$–$60+M_\odot$); **intermediate-mass** (IMBH, $10^2$–$10^5M_\odot$, observationally unconfirmed); **supermassive** (SMBH, $10^6$–$10^9M_\odot$, in virtually all large-galaxy nuclei — Milky Way $\sim4\times10^6M_\odot$). The **Magorrian relation** $M_\text{BH}\approx10^{-3}M_\text{gal}$ links SMBH mass to host-bulge mass across ten orders of magnitude; extrapolated to globular-cluster masses it predicts IMBHs of $10^2$–$10^3M_\odot$ at GC centres — sought via a central stellar-density cusp plus a Keplerian ($v\propto r^{-1/2}$) rise in velocity dispersion within the sphere of influence $r_\text{BH}=GM_\text{BH}/\sigma^2$ (sub-arcsecond scale, needs adaptive-optics-assisted integral-field spectroscopy, e.g. NGC 6388). IMBHs matter because growing a $z>6$ quasar's $10^9M_\odot$ SMBH from stellar-mass seeds within $\lesssim1$ Gyr would need an implausible $>10^5$ mergers — IMBH seeds relax this constraint.

**[Black Holes & GW]** **Gravitational waves**: quadrupolar spacetime ripples generated by any accelerated mass/energy (spin-2 field — no monopole or dipole GW radiation, hence none from spherically or axially symmetric collapse). An inspiralling binary loses orbital energy $E_\text{tot}=-GM\mu/(2R)$ to radiation, shrinking $R$ and raising $\omega_s=\sqrt{GM/R^3}$ (Kepler); GW frequency is exactly twice orbital frequency, $\omega_\text{gw}=2\omega_s$, since the quadrupole moment repeats twice per orbit. Strain $h_0=2(R_{S1}/r)(R_{S2}/R)$ (the fractional length distortion $\Delta L/L$ a passing wave imprints on free test masses) is extraordinarily small ($h_0\sim10^{-22}$ for a NS–NS binary at 10 Mpc — changing the Earth–Sun distance by roughly one atom's width), which is why GW detection required decades of technology development.

**[Black Holes & GW]** GW luminosity $L=\frac{32}{5}\frac{G}{c^5}(\mu R^2\omega_s^3)^2\propto R^{-5}$ (using $\omega_s\propto R^{-3/2}$): negligible for ordinary wide binaries ($G/c^5\sim10^{-60}$) but diverges as the orbit tightens, driving the final runaway inspiral and merger — the amplitude and frequency rise together, producing the characteristic **"chirp."**

**[Black Holes & GW]** **Chirp mass**, the primary model-independent GW observable: $\mathcal{M}=(m_1m_2)^{3/5}/(m_1+m_2)^{1/5}=\frac{c^3}{G}[\frac{5}{96}\pi^{-8/3}\nu_\text{gw}^{-11/3}\dot\nu_\text{gw}]^{3/5}$, obtained purely from the observed GW frequency and its time-derivative (no distance or individual masses needed a priori) and constant throughout the inspiral (an internal consistency check). $\mathcal M$ alone cannot separate $m_1,m_2$: writing $m_1=\alpha M$, $m_2=(1-\alpha)M$, the ratio $M_\text{tot}=\mathcal M/[\alpha(1-\alpha)]^{3/5}$ is minimised at equal masses, giving the model-independent lower bound $M_\text{tot}\geq2.3\,\mathcal M$. An independent total mass comes from the maximum (coalescence) GW frequency, using $R_S=2GM/c^2$ as the merger separation: $M_\text{tot}=\frac{1}{\pi\sqrt8}\frac{c^3}{G\nu_\text{gw}^\text{max}}$; combining both pins down the mass ratio and hence $m_1,m_2$ individually, with distance following from the flux–luminosity relation $F=L/(4\pi r^2)$.
> **EXAM QUESTION — Q71:** *"Question on a merger of two black holes and gravitational waves"*

**[Black Holes & GW]** **GW150914** (first BH–BH merger, LIGO 2015): $\mathcal{M}_\text{chirp}\approx30M_\odot$, minimum total mass $69M_\odot$ (equal-mass bound) confirmed independently by $M_\text{tot}=70M_\odot$ (from $\nu_\text{gw}^\text{max}\approx330$ Hz), giving mass ratio $\alpha\approx0.6\Rightarrow m_1\approx42M_\odot$, $m_2\approx28M_\odot$, distance $\approx400$ Mpc, and $\sim3M_\odot c^2$ radiated as GWs in a fraction of a second (briefly exceeding the electromagnetic luminosity of the observable Universe).
> **EXAM QUESTION — Q71:** *"chirp mass ~30 Msun, total mass ~70 Msun, individual masses ~36 and 29 Msun, distance ~400 Mpc"*

**[Black Holes & GW]** **LIGO** = Michelson interferometer (4 km perpendicular arms, tuned so undisturbed light gives total destructive interference); a passing GW stretches one arm and compresses the other simultaneously, breaking the null and admitting light to the photodetector — reading the strain $h=\Delta L/L$ directly. Required sensitivity $h\sim10^{-22}$ ($\Delta L\sim10^{-18}$ m, 1000× smaller than a proton) needs Fabry–Pérot cavities, high-power lasers, and seismic isolation. Two widely separated sites (Hanford + Livingston, 3002 km apart) are essential: light-travel-time coincidence (≤10 ms) distinguishes a genuine signal from local noise and gives rough sky localisation (GW150914 showed a ~7 ms inter-site delay).

**[Black Holes & GW]** **Redshift corrections**: GW frequency and its derivative redshift like light, $\nu_\text{gw}^\text{det}=\nu_\text{gw}^s/(1+z)$, $\dot\nu_\text{gw}^\text{det}=\dot\nu_\text{gw}^s/(1+z)^2$, so all detector-frame masses are systematically inflated, $\mathcal M^\text{det}=(1+z)\mathcal M^s$. Since GWs carry no spectral lines, $z$ must come from an electromagnetic counterpart (host-galaxy redshift, as for GW170817) or from assumed cosmology applied to the GW luminosity distance; for GW150914 ($z\approx0.1$) this lowers the true source-frame masses by ~10% ($m_1^s\approx38M_\odot$, $m_2^s\approx25M_\odot$).

**[Black Holes & GW]** **GW170817** (NS–NS merger, 2017) — the first multi-messenger GW event: simultaneous gravitational-wave inspiral (Advanced LIGO+Virgo, ~10 s visible in-band, low $\mathcal M\approx1.19M_\odot$, $M_\text{tot}\approx2.74M_\odot$, $d\approx40$ Mpc, host galaxy NGC 4993), a short gamma-ray burst (GRB 170817A, detected by Fermi-GBM just 1.7 s after merger — consistent with a relativistic jet launched along the merger's polar axis), and a **kilonova** (optical/infrared transient AT2017gfo) powered by radioactive decay of freshly synthesised r-process nuclei. The kilonova's spectral evolution (blue at day 1.5 → progressively redder through day 11) tracks the transition from light r-process ejecta to lanthanide-rich, high-opacity ejecta — direct observational proof that NS mergers are a primary site of r-process nucleosynthesis (Au, Pt, Eu, U, and the full lanthanide chain), closing a question left open since the B²FH (1957) paper.
> **EXAM QUESTION — Q14, Q71:** *"Enrichment of ISM"* (r-process channel) / *"merger of two black holes and gravitational waves"*

**[Black Holes & GW]** Complete nucleosynthesis map by site: H/He — Big Bang (~3 min); C through Si and other light α-elements — Type II SNe; Fe-peak — ~70% Type Ia + ~30% CC SNe; s-process (Ba, La, Ce, Pb) — AGB thermal pulses; r-process (Au, Pt, Eu, U, lanthanides) — NS mergers/kilonovae plus some CC SNe.

---

## 2. Key Equations

### 2.1 Structure Equations and Foundational Physics

$$\frac{dP(r)}{dr}=-\frac{GM(r)}{r^2}\rho(r)\qquad\text{(hydrostatic equilibrium)}\qquad\qquad \frac{dM(r)}{dr}=4\pi r^2\rho(r)\quad\text{(mass continuity)}$$

$$\mu=\frac{1}{2X+\frac34Y+\frac12Z}\quad\text{(mean molecular weight, fully ionised gas)}$$
> **EXAM QUESTION — Q65:** *"How is defined the mean molecular weight?"*

$$\frac{T}{\rho^{2/3}}<10^5\ (\text{electron degeneracy onset, K, g/cm}^3)\qquad 2K+\Omega=0\ \text{(Virial theorem)}\qquad t_{KH}=\frac12\frac{GM^2}{LR}$$

$$\left.\frac{dT}{dr}\right|_\text{rad}=-\frac{3\kappa\rho}{4acT^3}\frac{L(r)}{4\pi r^2}\quad\text{(radiative temperature gradient)}$$
> **EXAM QUESTION — Q52, Q65:** *"What is the expression for the radiative gradient?"*

$$\nabla_\text{rad}>\nabla_\text{ad}=\frac{\gamma-1}{\gamma}=0.4 \implies\text{convection (Schwarzschild criterion)}$$
> **EXAM QUESTION — Q11, Q20, Q46:** *"Radiative and convective core, differences"*

$$\kappa_{BF}\propto Z(1+X)\rho/T^{3.5},\quad \kappa_{FF}\propto(X+Y)(1+X)\rho/T^{3.5},\quad \kappa_E\propto0.2(1+X)\quad\text{(Kramers opacity laws)}$$

$$\epsilon_\text{pp}\propto\rho X^2T_6^{3.5-6},\qquad \epsilon_\text{CNO}\propto\rho XX_\text{CNO}T_6^{13-20},\qquad \epsilon_{3\alpha}\propto\rho^2Y^3T^{20-30}$$
> **EXAM QUESTION — Q65:** *"expressions for the energy efficiency of PP-chain and CNO cycle"*

$$^{12}\text{C}+{}^4\text{He}\to{}^{16}\text{O}+\gamma\ (7.6\text{ MeV}) \to \cdots \to {}^{52}\text{Cr}+{}^4\text{He}\to{}^{56}\text{Ni}+\gamma\xrightarrow{\beta}{}^{56}\text{Fe}\quad\text{(alpha-capture chain)}$$
> **EXAM QUESTION — Q15:** *"Alpha capture chain"*

$$L=4\pi R^2\sigma T_e^4\qquad T^4=\frac34T_e^4(\tau_v+\tfrac23)\quad\text{(effective temperature at }\tau_v=2/3\text{)}$$

$$\left[\frac{El}{H}\right]=\log\left(\frac{El}{H}\right)_*-\log\left(\frac{El}{H}\right)_\odot\quad\text{(square-bracket abundance notation)}$$
> **EXAM QUESTION — Q31:** *"alpha/Fe - Fe/H diagram"* (axis definition)

### 2.2 Pre-MS, ZAMS, and Main-Sequence Equations

$$M_J\geq10^{23}T^{3/2}\rho^{-1/2}\text{ g}\quad\text{(Jeans mass)}\qquad\qquad L_\text{Ed}=\frac{4\pi GMc}{\kappa}\approx3.8\times10^4\left(\frac{M}{M_\odot}\right)L_\odot\quad\text{(Eddington luminosity)}$$
> **EXAM QUESTION — Q41, Q57:** *"why stars with M>90-100 solar masses are unstable"*

$$q_0=0.37\left(\frac{\mu_e}{\mu_{ic}}\right)^2\approx0.08\quad\text{(Schönberg–Chandrasekhar mass-fraction limit)}$$

$$t_\text{MS}\approx10^{10}M^{-3}\text{ yr }(M\text{ in }M_\odot);\qquad L\propto M^{3.6}\ (M>1.2M_\odot),\ M^{4-4.5}\ (0.3<M/M_\odot<1.2),\ M^{2.6}\ (\text{lowest mass})$$
> **EXAM QUESTION — Q65:** *"age-mass relation for stars along the ZAMS"*

### 2.3 RGB / He-Flash / HB / AGB Equations

$$\frac{\rho_i}{\rho_e}=\frac{\mu_i}{\mu_e}\approx2.11\qquad L_H\propto\mu^7\ \text{(H-shell luminosity)}\qquad\log T=\tfrac23\log\rho+5\ \text{(degeneracy boundary)}$$

$$M_c^{He}\approx0.5\,M_\odot\ \text{(universal He-flash ignition mass)}\qquad \frac{T}{\rho^{2/3}}>10^5\ \text{(degeneracy-lifting condition)}$$
> **EXAM QUESTION — Q21, Q52, Q58, Q64:** *"He-flash: what mechanism removes the degeneration [convection]"*

$$\log(L/L_\odot)\approx3.45,\ M_I\approx-4.0\quad\text{(TRGB standard candle)};\qquad q=\frac{M_c}{M_E}\quad\text{(ZAHB q-parameter)}$$
> **EXAM QUESTION — Q36, Q52, Q65, Q69:** *"Standard candles"* / *"the q parameter"*

$$\dot M=-4\times10^{-13}\eta\frac{L}{gR}\ M_\odot\text{yr}^{-1}\quad\text{(Reimers mass-loss law, RGB/AGB)}$$

### 2.4 Pulsating Stars Equations

$$M_V=-2.8\log P_\text{days}-1.43\quad\text{(Period–Luminosity relation, Leavitt)}$$
> **EXAM QUESTION — Q1, Q27, Q54, Q66:** *"P-L relation, how it's used, distance from light curve"*

Distance procedure: (1) $P$, $\langle V\rangle$ from light curve; (2) $M_V=-2.8\log P-1.43$; (3) $(m-M)_V=\langle V\rangle-M_V$; (4) $(m-M)_0=5\log d-5$. **Worked example:** $P=4.5$d, $\langle V\rangle=13.80\Rightarrow\log P=0.65,\ M_V=-3.26,\ (m-M)=17.06,\ d\approx25$ kpc.
> **EXAM QUESTION — Q1, Q27, Q54, Q66:** *"how to derive the distance from the light curve"*

$$\Pi=2\int_0^R\frac{dr}{v_s},\ v_s=\sqrt{\gamma P/\rho}\ \Rightarrow\ \Pi\approx\sqrt{3\pi/(2\gamma G\rho)}\propto\rho^{-1/2}\quad\text{(Period–Density relation)}$$

$$\ddot{(\delta R)}=-(3\gamma-4)\frac{GM}{R_0^3}\delta R\quad\text{(one-zone SHM; oscillation requires }\gamma>4/3\text{)}$$

$$M_V=-3.53\log P_\text{days}-2.13+2.13(B-V)\quad\text{(full Period-Luminosity-Colour relation)}$$

### 2.5 White Dwarf Equations

$$P\propto\rho^{5/3}\ \text{(non-rel.)}\ \Rightarrow\ M^{1/3}R\approx\text{const}\ (R\propto M^{-1/3});\qquad P\propto\rho^{4/3}\ \text{(ultra-rel.)}$$
> **EXAM QUESTION — Q12, Q39, Q49, Q63:** *"Mass-radius relation"*

$$\rho\propto M^2\quad\text{(consequence of }M^{1/3}R\approx\text{const — small accreted mass, large density increase)}$$

$$M_\text{Ch}=\frac{3\sqrt{2\pi}}{8}\left(\frac{\hbar c}{G}\right)^{3/2}\left[\left(\frac ZA\right)\frac1{m_H}\right]^2\approx1.44(1+X)^2\,M_\odot\quad\text{(Chandrasekhar mass)}$$
> **EXAM QUESTION — Q16:** *"Chandrasekhar-mass limit definition"*

$$L=cT_c^{7/2}\quad\text{(luminosity–central-temperature relation, matches degenerate core to non-degenerate envelope)}$$

$$L_\text{WD}(t)=L_0\left[1+\frac52\frac t{\tau_0}\right]^{-7/5}\quad\text{(Mestel cooling law)};\qquad t_\text{cool}\approx8.8\times10^6\left(\frac{M}{M_\odot}\right)^{5/7}\left(\frac{L}{L_\odot}\right)^{-5/7}\text{yr}$$
> **EXAM QUESTION — Q39, Q49:** *"WDs cooling tracks"*

### 2.6 Type II SN, URCA, Neutron Star Equations

$$^{56}\text{Fe}+e^-\to{}^{56}\text{Mn}+\nu_e\ \text{(electron capture)};\quad ^{56}\text{Fe}+\gamma\to13\,^4\text{He}+4n\ \text{(photodisintegration, }-124\text{ MeV)};\quad p^++e^-\to n+\nu_e\ \text{(URCA)}$$
> **EXAM QUESTION — Q3–Q10, Q13, Q18, Q30, Q48, Q56, Q60, Q69, Q70:** reaction set requested verbatim across many sittings.

$$\rho_\text{nuc}\approx2.4\times10^{14}\text{g/cm}^3\ \text{(nuclear density, core bounce)};\qquad \nu_e+n\leftrightarrow e^-+p^+,\ \bar\nu_e+p^+\leftrightarrow n+e^+\ \text{(gain-region heating)}$$

$$^{56}\text{Ni}\xrightarrow{t_{1/2}=6.1\text{d}}{}^{56}\text{Co}\xrightarrow{t_{1/2}=77.1\text{d}}{}^{56}\text{Fe}\quad\text{(radioactive light-curve tail)}$$

$$MR_\text{NS}^3\approx\text{const}\quad\text{(NS mass-radius relation, }m_e\to m_n\text{ analogue of WD)}$$
> **EXAM QUESTION — Q63, Q69:** *"density, temperature and radius of a neutron star"*

$$\frac{R_\text{pre-col}}{R_\text{post-col}}\approx500;\qquad P_\text{NS}=P_i(R_f/R_i)^2\approx4\times10^{-6}P_\text{pre-collapse};\qquad B_\text{NS}=B_\text{WD}(R_\text{WD}/R_\text{NS})^2$$
> **EXAM QUESTION — Q3–Q10, Q63, Q71:** radius-shrinkage/spin-up/field-amplification triad.

$$B^2=\frac{3Ic^3}{8\pi^2R^6}P\dot P\ \Rightarrow\ B\propto\sqrt{P\dot P};\qquad \tau=\frac{P}{\dot P};\qquad P_\text{death}\approx2.42\times10^{-6}\sqrt B\text{ s}$$
> **EXAM QUESTION — Q51, Q65, Q71:** *"Draw the P-Pdot diagram"*

$$K=\frac{2\pi^2I}{P^2},\ I=\frac25MR^2\sim10^{45}\text{g cm}^2;\qquad \frac{dK}{dt}=-\frac{4\pi^2I\dot P}{P^3}\ (\text{Crab}\approx5\times10^{38}\text{erg/s})$$
> **EXAM QUESTION — Q51:** *"Crab... spindown power matches synchrotron luminosity"*

$$\xi_{2.5}=\frac{M/M_\odot}{R(M)/1000\text{km}},\quad \xi_{2.5}\gtrless0.2\Leftrightarrow\text{SN(NS) vs. failed SN(BH)}\qquad \dot M\propto Z^{0.5-0.9}\ \text{(wind mass loss)}$$
> **EXAM QUESTION — Q71:** *"fallback of SN ejecta, mass accretion, mass loss"*

### 2.7 Binary Systems Equations

$$l_1=a(0.5-0.227\log(M_2/M_1)),\quad l_2=a(0.5+0.227\log(M_2/M_1)),\quad l_1+l_2=a\quad\text{(Roche lobe radii)}$$
> **EXAM QUESTION — Q32:** *"Binary Systems"* (Roche geometry)

$$\frac1a\frac{da}{dt}=\frac{2\dot M_1(M_1-M_2)}{M_1M_2}\quad\text{(conservative mass-transfer orbital evolution)}$$
> **EXAM QUESTION — Q32, Q38:** *"Binary Systems"* / *"Mass accretion on a WD"*

$$K=\frac{GMm}{R}\quad\text{(accretion energy per unit mass: WD}\sim10^{17}\text{erg/g, NS}\sim10^{20}\text{erg/g)}$$
> **EXAM QUESTION — Q32:** *"Binary Systems"* (accretion energetics)

$$\delta m<\frac{M_1+M_2}2\quad\text{(binary survival criterion after instantaneous SN mass ejection)}$$
> **EXAM QUESTION — Q71:** *"mass loss"* (survival-criterion component)

### 2.8 Black Holes and Gravitational Wave Equations

$$R_s=\frac{2GM}{c^2}=3\left(\frac{M}{M_\odot}\right)\text{km}\quad\text{(Schwarzschild radius)}$$

$$(ds)^2=c^2dt^2\left(1-\frac{R_s}{r}\right)-\frac{dr^2}{1-R_s/r}-r^2d\Omega^2\quad\text{(Schwarzschild metric)}$$

$$dL=\frac{dr}{\sqrt{1-R_s/r}}>dr;\qquad d\tau=dt\sqrt{1-\frac{R_s}{r}}<dt;\qquad \frac{dr}{dt}=c\left(1-\frac{R_s}{r}\right)\to0\text{ at }r=R_s$$
> **EXAM QUESTION** (event-horizon reasoning, general): proper radial-distance dilation, gravitational time dilation, and the frozen coordinate light speed at $r\to R_s$.

$$\xi_{2.5}=\frac{M/M_\odot}{R(M)/1000\text{km}}\quad\text{(compactness parameter, repeated from §2.6 — used for SN vs. failed-SN outcome)}$$

$$\dot M\propto Z^{0.5-0.9}\quad\text{(metallicity-dependent wind mass loss — metal-poor stars retain more mass, build larger remnants)}$$

$$r_\text{BH}=\frac{GM_\text{BH}}{\sigma^2}=4.32\times10^{-3}\frac{M_\text{BH}/M_\odot}{(\sigma/\text{km s}^{-1})^2}\text{pc}\quad\text{(IMBH sphere of influence)};\qquad M_\text{BH}\approx10^{-3}M_\text{gal}\quad\text{(Magorrian relation)}$$

$$L_\text{GW}=\frac{32}{5}\frac{G}{c^5}(\mu R^2\omega_s^3)^2\quad\text{(quadrupole GW luminosity, }\propto R^{-5}\text{ as orbit shrinks)}$$

$$\mathcal{M}_\text{chirp}=\frac{(m_1m_2)^{3/5}}{(m_1+m_2)^{1/5}}=\frac{c^3}G\left[\frac5{96}\pi^{-8/3}\nu_\text{gw}^{-11/3}\dot\nu_\text{gw}\right]^{3/5}$$
> **EXAM QUESTION — Q71:** *"chirp mass"* formula and GW150914 application.

$$M_\text{tot}\geq2.3\,\mathcal{M}_\text{chirp}\ (\text{equal-mass lower bound});\qquad M_\text{tot}=\frac1{\pi\sqrt8}\frac{c^3}{G\nu_\text{gw}^\text{max}}\ (\text{from merger frequency})$$
> **EXAM QUESTION — Q71:** *"total mass ~70 Msun"*

$$r=\frac{16}{\sqrt5}\frac{G}{c^4}\frac{\mu R^2\omega_s^2}{h_0}\quad\text{(GW distance estimate, from }F=L/4\pi r^2\text{)}$$

$$\nu_\text{gw}^\text{det}=\frac{\nu_\text{gw}^s}{1+z},\quad \dot\nu_\text{gw}^\text{det}=\frac{\dot\nu_\text{gw}^s}{(1+z)^2},\quad \mathcal{M}_\text{chirp}^\text{det}=(1+z)\,\mathcal{M}_\text{chirp}^s\quad\text{(GW redshift corrections)}$$

---

## 3. Key Algorithms / Procedures

1. **Building a stellar model / evolutionary track**: fix $[M,X,Y,Z]$ → solve the coupled structure equations (hydrostatic equilibrium, mass continuity, EoS, energy generation, radiative/convective transport with Schwarzschild test, opacity) → read off $(L,T_e)$ → advance time, update composition via burning → repeat. The sequence of points is the evolutionary track; one snapshot across all masses is the ZAMS or an isochrone.

2. **Schwarzschild convection test**: compute $\nabla_\text{rad}$ from local $\kappa,\rho,T,L(r)$; compare to $\nabla_\text{ad}=0.4$ (ideal monatomic gas, lower with partial ionisation); if $\nabla_\text{rad}>\nabla_\text{ad}$, layer is convective (mixes composition); else radiative (composition gradients accumulate).
> **EXAM QUESTION — Q11, Q20, Q46:** *"Radiative and convective core, differences"*

3. **Deriving the Schönberg–Chandrasekhar limit**: (i) integrate hydrostatic equilibrium over the isothermal core to get $P_{ic}^\text{max}\propto T_{ic}^4/(G^3M_{ic}^2\mu_{ic}^4)$; (ii) integrate over the envelope for $P_\text{env}$; (iii) equate and solve for $M_{ic}/M\propto(\mu_\text{env}/\mu_{ic})^2$.

4. **Determining post-MS core fate**: track the core's $(\log\rho_c,\log T_c)$ trajectory during isothermal growth; check whether it crosses the degeneracy line before reaching the SC limit — degeneracy first (low mass) → long RGB + He flash; SC limit first (intermediate mass) → small hook + quiet ignition; neither (very high mass) → direct quiet ignition.
> **EXAM QUESTION — Q2, Q25, Q47, Q59:** *"Evolutionary tracks for 1 and 5 solar masses"*

5. **Deriving why the RGB envelope must expand**: (i) chemical dichotomy sets $\rho_i/\rho_e=\mu_i/\mu_e$; (ii) differentiate the EoS + hydrostatic equilibrium + radiative transport to get the density-gradient ratio; (iii) evaluate using shell-luminosity fraction $u$; (iv) once $\gamma>1$ ($u>0.3$), ratio drops below $\sim0.22$, forcing $R$ to grow $\ge4\times$ — this *is* the giant branch.

6. **Helium-flash sequence**: degenerate core reaches $T\sim10^8$K at $M_c\approx0.5M_\odot$ → neutrino cooling creates off-centre temperature maximum → 3α ignites there (main flash) → convective expansion lifts degeneracy in that shell → next-innermost still-degenerate shell ignites (secondary flash) → cascade repeats inward over $\sim10^6$yr → entire core reaches $T/\rho^{2/3}>10^5$ → stable ZAHB burning begins.
> **EXAM QUESTION — Q6, Q21, Q52, Q58, Q64, Q65, Q69:** *"Helium flash"*, *"mechanism that removes degeneracy"*

7. **TP-AGB thermal-pulse cycle**: H-shell deposits He into intershell → critical mass reached → He-shell ignites (runaway pulse) → convection mixes/expands intershell, switches off H-shell → He-shell fades → H-shell reignites → repeat.

8. **Third dredge-up (two-step)**: (1) intershell convection during the He-shell pulse enriches intershell with C, O; (2) *later*, separately, envelope convection deepens as the star returns toward the Hayashi track and penetrates into the enriched intershell, carrying C/O to the surface.
> **EXAM QUESTION — Q33:** *"Dredge-up, in particular the third one"*

9. **TRGB distance measurement**: identify the sharp drop in the I-band RGB luminosity function of a resolved population → apparent tip magnitude $m_I$ → apply $M_I\approx-4.0$ (correct for metallicity/extinction) → $(m-M)_0=m_I+4.0=5\log d-5$ → solve for $d$.

10. **Cepheid distance procedure** (the single most-repeated procedural question in the bank): (1) measure period $P$ and mean apparent magnitude $\langle V\rangle$ from the light curve; (2) insert $P$ into $M_V=-2.8\log P-1.43$; (3) compute distance modulus $(m-M)_V=\langle V\rangle-M_V$ (correct for reddening); (4) solve $(m-M)_0=5\log d-5$ for $d$.
> **EXAM QUESTION — Q1, Q27, Q54, Q66:** *"how to derive the distance from the light curve"*

11. **Deriving the WD (non-relativistic) mass–radius relation**: (a) degenerate pressure $P\propto\rho^{5/3}$ from Heisenberg/Pauli; (b) impose hydrostatic balance against gravity; (c) substitute $\rho=M/(\frac43\pi R^3)$; (d) collect powers of $R$ → $M^{1/3}R\approx$const. **Chandrasekhar mass**: repeat with relativistic $P\propto\rho^{4/3}$ — both sides scale identically with $R$, so $R$ cancels, leaving one fixed mass.
> **EXAM QUESTION — Q12, Q16, Q39, Q49:** *"Mass-radius relation"* / *"Chandrasekhar-mass limit definition"*

12. **Deriving $L=cT_c^{7/2}$ and the Mestel cooling law**: combine hydrostatic equilibrium with the radiative gradient (Kramers opacity) in the non-degenerate envelope, integrate inward from the surface, match to the isothermal degenerate core at the boundary where $T=D\rho^{2/3}$ → get $L(T_c)$; equate to the thermal-reservoir depletion rate $L=-B\,dT_c/dt$ and integrate → $T_c(t)$, hence $L(t)$.

13. **Core-collapse → Type II SN, full sequence** (the single most-tested mechanism in the course): (1) Si-burning completes, forms inert Fe core (1.3–2.0$M_\odot$); (2) core contracts, electron captures on Fe-group nuclei strip electron pressure; (3) photodisintegration of Fe (~124 MeV/nucleus) removes thermal support; (4) URCA process on liberated protons strips remaining pressure; (5) $\Gamma$ drops below 4/3 → free-fall collapse ($\tau_d\sim10$ms); (6) core bounce at $\rho_\text{nuc}\approx2.4\times10^{14}$g/cm³ (strong force turns repulsive); (7) shock launches, stalls (photodisintegration + neutrino cooling losses); (8) delayed neutrino-heating mechanism deposits ~$10^{51}$erg in the gain region, revives shock 100–500ms post-bounce; (9) shock ejects envelope (KE ~$10^{51}$erg), leaving NS (or BH via fallback).
> **EXAM QUESTION — Q3–Q10, Q13, Q18, Q29, Q30, Q37, Q42, Q45, Q48, Q53, Q56, Q60, Q64, Q65, Q68, Q69, Q70, Q71** — the highest-priority procedure in the entire course.

14. **MSP recycling sequence**: (1) NS forms in a CC-SN within a surviving binary, born fast; (2) spins down via magnetic braking over $10^7$–$10^9$yr, approaches the graveyard; (3) companion evolves, fills Roche lobe, transfers mass+angular momentum via a disk; (4) NS spun up to millisecond periods (observed as X-ray binary during this phase); (5) mass transfer ends, leaving MSP + He-WD (or, via Black-Widow ablation, an isolated MSP).
> **EXAM QUESTION — Q4, Q10, Q51, Q65:** *"millisecond pulsars"*

15. **GW150914-style chirp analysis**: (i) read $\nu_\text{gw}$ and $\dot\nu_\text{gw}$ from the time–frequency spectrogram; (ii) compute $\mathcal{M}_\text{chirp}$ (constant across inspiral — built-in consistency check); (iii) get minimum $M_\text{tot}$ from the equal-mass bound; (iv) independently get $M_\text{tot}$ from the maximum GW frequency at coalescence; (v) cross-check; (vi) combine to solve for mass ratio and hence $m_1,m_2$; (vii) get distance from the flux–luminosity relation; (viii) if an EM counterpart gives $z$, correct all detector-frame masses.
> **EXAM QUESTION — Q71:** *"gravitational waves... individual masses ~36 and 29 Msun, distance ~400 Mpc"*

16. **Mass-transfer feedback sign analysis** (binary systems): identify current donor and mass ratio → if donor is more massive and losing mass, orbit shrinks (runaway) until mass ratio inverts; if accretor already more massive than donor, orbit widens (self-regulating, classical CV); if accretor less massive than donor, orbit shrinks (runaway → nova or sustained Type Ia trigger).
> **EXAM QUESTION — Q38:** *"Mass accretion on a WD in a binary system"*

---

## 4. Watch Out For

**General / foundational:**
- H-R diagram x-axis increases to the **left** — the single most-emphasized "gotcha"; examiners are "extremely persistent" both axes are logarithmic (Q41).
- Degeneracy is electron-only in practice — protons are never degenerate under any stellar condition reached in this course.
- CNO does not create C/N/O, only catalyzes; the *slow* $^{14}\text{N}(p,\gamma)$ step (not the fast branch) is rate-limiting.
- Thermoregulation failure is the single most-tested consequence of degeneracy — every major runaway (He flash, nova, Type Ia) traces back to $P$ being $T$-independent when degenerate.
- $\nabla_\text{ad}=0.4$ only for a monatomic ideal gas — partial-ionisation zones suppress it toward ~0.1.

**ZAMS / Main Sequence:**
- Don't confuse an evolutionary track (one star, all time) with an isochrone (one time, all masses).
- Kelvin–Helmholtz timescale is the pre-MS contraction time, NOT the MS lifetime — don't conflate $\tau_{KH}$ with $\tau_\text{nuc}$.
- The "hook" is a hallmark of a **convective core** (high mass) — never seen in radiative-core (low-mass) stars.
- SC limit (ideal-gas mechanism, 0.37 factor) is completely different from the electron-degeneracy boundary (quantum/Pauli effect) — low-mass stars hit degeneracy *before* SC; intermediate mass hits SC first.
- Central density *decreases* with ZAMS mass (CNO limits $T_c$ growth) — why massive-star cores avoid degeneracy.

**RGB / He-flash / HB / AGB:**
- Chemical dichotomy alone (Point 2) does **not** cause envelope expansion — the H-shell must also be active (Point 3); between them the star barely moves.
- The He-flash energy release ($\sim10^{11}L_\odot$ peak) is entirely internal — never brightens the surface; ignites **off-centre**, not at $r=0$.
- Two distinct mass thresholds are easy to confuse: $M=2.2M_\odot$ (He-core degeneracy/flash boundary) vs. $M^\text{up}=8M_\odot$ (CO-core degeneracy/SN-vs-WD boundary).
- TRGB only works for populations **older than ~1–2 Gyr** (must contain $M<2.2M_\odot$ stars).
- Convective cores **grow** during He-burning (opposite sense from MS H-burning convective cores, which shrink).
- HBB explains why the *most* massive AGB stars are *not* carbon stars, despite the most vigorous 3rd dredge-up.
- The "second parameter problem" (HB morphology) is explicitly **unsolved** — don't claim age+metallicity fully determine it.

**Pulsating stars:**
- Maximum luminosity does **not** exactly coincide with minimum radius — the phase lag is caused specifically by the H-ionisation zone, not the He II piston.
- Cepheids and W Virginis stars can occupy overlapping luminosities but are physically distinct (Pop I vs II) — a common trap (Q54).
- The P-L relation is technically a Period-Luminosity-**Colour** relation.
- RR Lyrae presence depends on HB morphology (metallicity + He abundance + mass loss) — not metallicity alone.

**White dwarfs:**
- Chandrasekhar mass is NOT WD-specific — it's the limit of any electron-degenerate substructure, including a pre-collapse iron core.
- Mass–radius relation is inverted vs. ordinary stars: higher WD mass → smaller radius.
- **At fixed age** (not fixed $T_\text{eff}$), more massive WDs are *more* luminous — isochrones have opposite slope sense to cooling tracks.
- ONe-WDs cool faster than same-mass CO-WDs (larger $A$ → smaller heat reservoir) — counterintuitive.
- He-WDs are never observed in isolation — every known one is binary-stripped.
- WD cooling is not a universal clock — slow-cooling WDs can delay cooling by up to ~1 Gyr.
- $\rho\propto M^2$ means tiny accreted mass causes large density increases; explosion requires actual **ignition** of a degenerate fuel, not merely reaching $M_\text{Ch}$.

**Supernovae / neutron stars:**
- Iron made by pre-collapse fusion stays **locked in the remnant** — ejected Fe comes from explosive Si-burning ($^{56}$Ni→Fe decay), a distinct source.
- Silicon burning is NOT direct Si+Si fusion — it's photodisintegration + alpha-capture rebuilding (NSE); silicon-burning endpoint is $^{56}$**Ni**, not Fe directly.
- Spectroscopic SN type ≠ explosion mechanism: Type I includes both thermonuclear (Ia) and core-collapse (Ib/Ic) — a very common trap.
- Chandrasekhar mass (precisely derived) vs. Oppenheimer–Volkoff limit (poorly constrained, unknown super-nuclear EoS) — not equally well-founded.
- The prompt shock **always fails** on its own — successful explosions require the delayed neutrino-heating revival.
- Only ~1% of a Type II SN's energy emerges as kinetic/optical; ~99% escapes as neutrinos.
- EC-SNe (7–11$M_\odot$) are a distinct third mechanism (electron capture on Ne/Mg) — not a smaller Fe-core CC-SN.
- MSPs combine signatures of both extreme youth (short $P$) and extreme age (very low $\dot P$) — naive $\tau=P/\dot P$ badly overestimates true MSP age.
- $\xi_{2.5}$ vs. $M_\text{ZAMS}$ is non-monotonic — a genuine mixed regime (18–26$M_\odot$) exists; don't treat the NS/BH boundary as a sharp cutoff.
- At solar metallicity, single-star evolution cannot produce a remnant above ~25$M_\odot$ — LIGO's massive BHs must be metal-poor or from binary/dynamical channels.

**Binary systems:**
- $L_1,L_2,L_3$ are all unstable saddle points — only $L_4,L_5$ are stable.
- A nova is a surface event the WD **survives** — do not confuse with a Type Ia SN (complete disruption).
- Simply reaching $M_\text{Ch}$ is not itself sufficient for a thermonuclear explosion — needs actual degenerate-fuel ignition (Q62).
- Binary survival factor is 1/2 of **total** mass, not of the ejected star's own mass.

**Black holes / GW:**
- The event horizon is not a physical local surface — infalling observers notice nothing crossing it.
- Chirp mass alone never gives individual masses — needs either the equal-mass assumption or an independent total-mass measurement.
- Detector-frame GW masses are systematically higher than source-frame by $(1+z)$ — redshift correction needs external (EM) information, since GWs carry no spectral lines.
- r-process is from mergers/kilonovae (+ some CC SNe), not from Type Ia SNe — don't conflate with the Fe-production channel.
- Cosmic Censorship (no "naked" singularities) is an unproven conjecture, not a theorem — don't overstate its certainty.
- GW luminosity $\propto R^{-5}$: negligible for ordinary wide binaries, but diverges only in the final inspiral — don't assume steady GW power throughout a binary's life.
- The Newtonian "escape velocity = c" argument gives the correct $R_s$ numerically but for the wrong physical reason — it is not evidence that GR reduces to Newtonian gravity here.
- Metallicity, not initial mass alone, caps remnant mass: at solar $Z$ no single star produces a remnant above ~25$M_\odot$, regardless of how large $M_\text{ZAMS}$ is.
- An IMBH's sphere of influence is sub-arcsecond even for a favourable globular cluster — imaging alone (density cusp) is not sufficient; kinematics (velocity-dispersion cusp) from AO-assisted spectroscopy is also required.

---

## 5. Exam Coverage Map

| Q# | Question (abbreviated) | Covered in summary |
|----|------------------------|---------------------|
| Q1 | Pulsating stars, why important, P-L relation | §1.14 Pulsating Stars; §2.4 Equations; §3.10 Algorithm |
| Q2 | Evolutionary tracks 1 vs 5 M☉, differences | §1.4 Tracks 1 vs 5 M☉; §3.4 Algorithm |
| Q3 | Neutron stars — what/properties/why exist | §1.12 Neutron Stars; §2.6 Equations; §3.13 Algorithm |
| Q4 | Neutron stars (+ MSP follow-up) | §1.12 Neutron Stars; §1.12 MSP recycling |
| Q5 | Neutron stars (+ ZAMS follow-up) | §1.12 Neutron Stars; §1.3 ZAMS |
| Q6 | Neutron stars (+ He-flash follow-up) | §1.12 Neutron Stars; §1.6 Helium Flash |
| Q7 | Neutron stars (+ RGB 1 vs 5 M☉ follow-up) | §1.12 Neutron Stars; §1.4/§1.5 RGB differences |
| Q8 | Neutron stars — what/properties/why exist | §1.12 Neutron Stars |
| Q9 | Neutron stars (+ SNe I/II follow-up) | §1.12 Neutron Stars; §1.11 SNe Classification |
| Q10 | Neutron stars (+ how to observe He-WDs) | §1.12 Neutron Stars; §1.13 WD (He-WD observability) |
| Q11 | Radiative and convective core, differences | §1.1/§1.3 Main Sequence; §2.1/§3.2 Algorithm |
| Q12 | WDs main characteristics, CO/Ne/He, mass-radius | §1.13 White Dwarfs; §2.5 Equations |
| Q13 | Photodisintegration and URCA in SNe II | §1.10 Type II SN Mechanism; §2.6 Equations |
| Q14 | Enrichment of ISM | §1.9 Advanced Burning/Nucleosynthesis |
| Q15 | Alpha capture chain | §1.9 Advanced Burning; §2.1 Equations |
| Q16 | Chandrasekhar-mass limit definition | §1.13 White Dwarfs; §2.5 Equations; §3.11 Algorithm |
| Q17 | ZAMS | §1.2 Pre-MS; §1.3 ZAMS/Main Sequence |
| Q18 | SN CC (core collapse) | §1.10 Type II SN Mechanism; §3.13 Algorithm |
| Q19 | Properties of ZAMS (M-L relation, mass range) | §1.3 ZAMS/Main Sequence |
| Q20 | Structural differences during MS by mass | §1.3 Main Sequence |
| Q21 | Helium flash | §1.6 Helium Flash; §3.6 Algorithm |
| Q22 | Final fate of stars by mass | §1.7 Final Fate Table |
| Q23 | ZAMS properties, Hayashi track role | §1.2 Pre-MS Hayashi Track; §1.3 ZAMS |
| Q24 | Evolution of 1 M☉ on the RGB | §1.5 RGB; §1.5 First Dredge-Up/RGB Bump |
| Q25 | Difference evolution 1 vs 5 M☉ (draw tracks, H-profile) | §1.4 Tracks 1 vs 5 M☉ |
| Q26 | Evolution track 5 M☉, energy source per point | §1.4 Point-by-point energy tracing |
| Q27 | Pulsating stars (origin, importance, P-L, distance) | §1.14 Pulsating Stars |
| Q28 | Final stages of evolution by mass | §1.7 Final Fate Table |
| Q29 | Mechanism of explosion of Type II SN | §1.10 Type II SN Mechanism; §3.13 Algorithm |
| Q30 | URCA process, steps from iron core to collapse | §1.10 Type II SN Mechanism; §3.13 Algorithm |
| Q31 | [α/Fe]-[Fe/H] diagram | §1.9 Advanced Burning (α/Fe diagram) |
| Q32 | Binary Systems | §1.15 Binary Systems; §2.7 Equations |
| Q33 | Dredge-up, especially the third | §1.7 Dredge-Up; §3.8 Algorithm |
| Q34 | Final stages composite (mass, SN, NS, WD) | §1.7 Final Fate; §1.10 SN Mechanism; §1.12 NS; §1.13 WD |
| Q35 | Evolution of 1 M☉ to WD phase | §1.7 Full Sequence; §1.5 Dredge-up/Bump |
| Q36 | Standard candles | §1.8 Standard Candles |
| Q37 | Type 2 SNe collapse mechanism | §1.10 Type II SN Mechanism |
| Q38 | Mass accretion on a WD in a binary | §1.13 WD Accretion; §1.15 Binary Systems; §3.16 Algorithm |
| Q39 | WD cooling tracks | §1.13 White Dwarfs (cooling); §2.5 Equations |
| Q40 | Slow cooling WDs | §1.13 White Dwarfs (slow cooling) |
| Q41 | ZAMS characteristics, Eddington instability, fully convective | §1.3 ZAMS/Main Sequence |
| Q42 | SNe types | §1.11 SNe Classification |
| Q43 | Final stages, exact mass values | §1.7 Final Fate Table |
| Q44 | General properties of a WD | §1.13 White Dwarfs |
| Q45 | SNE types | §1.11 SNe Classification |
| Q46 | ZAMS cutoffs, CNO convective cores | §1.3 Main Sequence |
| Q47 | Evolutionary tracks 1&5 M☉, point 1-2 shape | §1.4 Tracks 1 vs 5 M☉ |
| Q48 | Final stages high mass, URCA reactions | §1.10 Type II SN Mechanism |
| Q49 | Final stages low mass, WD cooling & mass-radius | §1.13 White Dwarfs |
| Q50 | Temperature profile inside the WD | §1.13 White Dwarfs (isothermal core) |
| Q51 | Neutron stars (P-Pdot, evolution in time) | §1.12 Neutron Stars (pulsars, P-Pdot) |
| Q52 | He burning (HB Teff, He flash, formulas) | §1.6 Helium Flash; §1.7 ZAHB/q-parameter |
| Q53 | Supernovae (classification, mechanism, URCA) | §1.10/§1.11 SN Mechanism & Classification |
| Q54 | Pulsating stars (positions in HR diagram) | §1.14 Pulsating Stars |
| Q55 | General properties of a WD (isothermal core) | §1.13 White Dwarfs |
| Q56 | SNe types (deflagration+detonation) | §1.11 SNe Classification (Type Ia mechanism) |
| Q57 | ZAMS cutoffs and structure | §1.3 ZAMS/Main Sequence |
| Q58 | He flash — general description | §1.6 Helium Flash |
| Q59 | Evolutionary tracks 1&5 M☉ (RGB focus) | §1.4/§1.5 Tracks & RGB differences |
| Q60 | SNII: rebound/bounce focus | §1.10 Type II SN Mechanism (core bounce) |
| Q61 | WD general properties (compositions) | §1.13 White Dwarfs |
| Q62 | SNIa: double-degenerate scenario | §1.11 SNe Classification (Type Ia) |
| Q63 | Differences between WD and NS | §1.12/§1.13 NS vs WD comparison |
| Q64 | Composite: ZAMS, He-flash, RGB, ccSN, NS | §1.3, §1.6, §1.8, §1.10, §1.12 (all cross-referenced) |
| Q65 | Mega-composite (Cristina Pallanca full exam) | Spans §1.2–§1.14 (all major sections) |
| Q66 | Pulsating stars | §1.14 Pulsating Stars |
| Q67 | White dwarfs | §1.13 White Dwarfs |
| Q68 | Type II SN | §1.10 Type II SN Mechanism |
| Q69 | Composite (Cristina Pallanca: ZAMS→NS) | §1.3, §1.5, §1.7, §1.8, §1.10, §1.12, §1.13 |
| Q70 | 50 M☉ evolution, SN II, NS common mass | §1.4 (very massive stars); §1.10; §1.12 |
| Q71 | 25 M☉, NS vs BH fate, pulsars, BH merger/GW, α/Fe | §1.9 (α/Fe); §1.10; §1.12 (NS/BH fate, pulsars); §1.16 (BH/GW) |

**All 71 questions are accounted for — no gaps.**

