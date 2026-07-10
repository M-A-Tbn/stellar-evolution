# Black Holes & Gravitational Waves — Summary

---

## 1. Key Concepts

- **Oppenheimer–Volkoff (OV) limit:** ~$2.5$–$3\,M_\odot$; the maximum mass a neutron star can support against gravity via degeneracy pressure. Remnants above it collapse to a BH; corresponds to a progenitor of roughly $25\,M_\odot$.
- **Black star (Michell, 1784):** Newtonian prediction that a sufficiently compact mass has escape velocity $> c$; correct numerology for $R_s$, wrong physics (needs GR).
- **Schwarzschild radius $R_s$:** the critical radius at which escape velocity equals $c$; defines the event horizon size.
- **Spacetime interval $\Delta s$:** invariant separation between two events; sign classifies causal relation (timelike/lightlike/spacelike).
- **Timelike / lightlike (null) / spacelike:** regions reachable by $v<c$ particles / by light only / causally disconnected ("elsewhere").
- **Light cone:** geometric structure bounding all causal trajectories; tilts and distorts near mass in GR.
- **Schwarzschild metric:** exact GR solution describing curved spacetime outside a static, spherical, uncharged mass.
- **Proper distance vs. coordinate distance:** physical radial distance always exceeds the coordinate difference $dr$ near a mass.
- **Gravitational time dilation:** clocks run slower at smaller $r$; freeze ($d\tau \to 0$) at the horizon as seen from infinity.
- **Event horizon:** the $r=R_s$ surface; a one-way causal boundary, not a physical/material surface — no locally detectable effect on an infalling observer.
- **Singularity:** the $r=0$ point of infinite curvature/zero volume where classical GR breaks down, requiring quantum gravity.
- **Cosmic Censorship hypothesis:** conjecture that singularities are always hidden behind horizons (never "naked").
- **Compactness parameter $\xi_M$ (esp. $\xi_{2.5}$):** measures how tightly mass is packed at core collapse; predicts successful SN (→NS) vs. failed SN (→BH) via a threshold $\approx 0.2$.
- **Failed supernova:** direct collapse to BH with no explosion or optical transient; entire mass falls in.
- **Metallicity dependence of remnant mass:** metal-poor stars lose less wind mass and form larger CO cores → more massive BHs; at solar metallicity no remnant exceeds $25\,M_\odot$.
- **BH mass classes:** stellar-mass ($\lesssim 50$–$100\,M_\odot$), intermediate-mass (IMBH, $10^2$–$10^5\,M_\odot$, unconfirmed), supermassive (SMBH, $10^6$–$10^9\,M_\odot$).
- **Magorrian ($M_\mathrm{BH}$–$M_\mathrm{bulge}$/$\sigma$) relation:** SMBH mass co-scales with host galaxy bulge mass; extrapolated to GCs predicts IMBH masses.
- **Sphere of influence:** radius within which an IMBH's gravity dominates cluster stellar kinematics, producing a Keplerian ($v\propto r^{-1/2}$) cusp in velocity dispersion and a density cusp in surface brightness.
- **Gravitational waves (GWs):** spacetime ripples from accelerating mass/energy; transverse, quadrupolar (spin-2), unlike EM dipole radiation; absent in Newtonian gravity.
- **Strain $h(t)$:** fractional distortion of proper length caused by a passing GW.
- **Chirp:** simultaneous rise in GW amplitude and frequency during inspiral, giving the signature time–frequency sweep.
- **Chirp mass $M_\mathrm{chirp}$:** the unique mass combination directly measurable from $\nu_\mathrm{gw}(t)$ alone, independent of distance or individual masses.
- **Mass-ratio degeneracy:** chirp mass alone cannot separate $m_1,m_2$; equal masses give the minimum possible total mass.
- **Coalescence/merger condition:** onset when binary separation equals the sum of the two Schwarzschild radii.
- **Michelson interferometer (LIGO):** detector design measuring differential arm-length change from a passing GW via interference.
- **Multi-messenger astronomy:** simultaneous detection of GW + EM (GRB, kilonova) signals from the same event (established by GW170817).
- **Kilonova:** optical/near-IR transient powered by radioactive decay of freshly synthesised r-process nuclei in merger ejecta.
- **r-process (rapid neutron capture):** nucleosynthesis path building neutron-rich heavy nuclei (up to/beyond U) faster than beta decay; occurs in NS mergers (and some CC SNe).
- **s-process (slow neutron capture):** nucleosynthesis in AGB stars producing Ba/La/Ce/Pb peaks.
- **Cosmological redshift of GW observables:** detector-frame frequency/derivative and masses are shifted relative to source-frame values.

## 2. Key Equations

- Escape velocity criterion: $v^2 = \dfrac{2GM}{R} > c^2$ — Newtonian analogy motivating $R_s$.
- Schwarzschild radius: $$R_s = \frac{2GM}{c^2} = 3\left(\frac{M}{M_\odot}\right)\,\mathrm{km}$$ — event horizon size; must be memorised.
- Flat-spacetime interval: $(\Delta s)^2 = [c\Delta t]^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ — defines causal structure in SR.
- Schwarzschild metric: $$(ds)^2 = c^2dt^2\left(1-\frac{R_s}{r}\right) - \frac{dr^2}{1-R_s/r} - r^2 d\Omega^2$$ — exact curved geometry outside a static spherical mass.
- Proper radial distance: $dL = \dfrac{dr}{\sqrt{1-R_s/r}} > dr$ — physical distance exceeds coordinate separation; diverges as $r\to R_s$.
- Gravitational time dilation: $d\tau = dt\sqrt{1-R_s/r} < dt$ — clocks near a mass run slow relative to a distant observer; $\to 0$ at horizon.
- Coordinate speed of light: $\dfrac{dr}{dt} = c\left(1-\dfrac{R_s}{r}\right) \to 0$ as $r\to R_s$ — light appears frozen at the horizon to a distant observer.
- Compactness parameter: $$\xi_{2.5} = \frac{M_{2.5}/M_\odot}{R(M_{2.5})/1000\,\mathrm{km}}, \quad \xi_{2.5}\gtrless 0.2 \Leftrightarrow \text{SN vs. failed SN}$$
- Wind mass-loss metallicity scaling: $\dot M \propto Z^\alpha,\ \alpha\approx 0.5$–$0.9$ — higher $Z$ → more mass lost → smaller remnants.
- Magorrian relation: $M_\mathrm{BH} \approx 10^{-3} M_\mathrm{gal}$ — links SMBH/IMBH mass to host system mass.
- Sphere of influence: $$r_\mathrm{BH} = \frac{GM_\mathrm{BH}}{\sigma^2} = 4.32\times10^{-3}\frac{M_\mathrm{BH}/M_\odot}{(\sigma/\mathrm{km\,s^{-1}})^2}\,\mathrm{pc}$$ — angular size $\approx 0.89\frac{M_\mathrm{BH}/M_\odot}{(\sigma/\mathrm{km\,s^{-1}})^2\,d_\mathrm{kpc}}''$; sets AO/IFS requirement.
- Kepler's third law (binary orbit): $\omega_s^2 = \dfrac{GM}{R^3}$ — links separation to orbital (and GW) frequency.
- Strain definition and signal: $\dfrac{\Delta L}{L}=h_0$, $\ h(t)=h_0\cos(\omega_\mathrm{gw}t)$, with $\omega_\mathrm{gw}=2\omega_s$ (factor 2 from quadrupole symmetry).
- Strain amplitude: $$h_0 = 2\frac{R_{S1}}{r}\frac{R_{S2}}{R} = 2\left(\frac{2GM}{c^2r}\right)\left(\frac{2G\mu}{c^2R}\right)$$ — product of compactness ratios over distance; grows as orbit shrinks, falls as $1/r$.
- Total orbital energy: $E_\mathrm{tot} = -\dfrac{GM\mu}{2R} = -\dfrac{Gm_1m_2}{2R}$ — becomes more negative (system loses energy) as $R$ shrinks.
- GW luminosity: $$L = \frac{32}{5}\frac{G}{c^5}(\mu R^2\omega_s^3)^2 \propto R^{-5}$$ — negligible for ordinary binaries; diverges near merger.
- GW energy flux: $F = \dfrac{1}{32\pi}\dfrac{c^3}{G}h_0^2\omega_\mathrm{gw}^2$ — connects observables to radiated power; used for distance estimate.
- Inspiral (frequency evolution) equation: $\dot\omega_s = \dfrac{96G}{5c^5}\dfrac{\mu}{M}R^5\omega_s^7$ — derived from energy balance $L=-dE_\mathrm{tot}/dt$; mass dependence enters as $\mu^3M^2$.
- Chirp mass definition and observable form: $$M_\mathrm{chirp}=(\mu^3M^2)^{1/5}=\frac{(m_1m_2)^{3/5}}{(m_1+m_2)^{1/5}} = \frac{c^3}{G}\left[\frac{5}{96}\pi^{-8/3}\nu_\mathrm{gw}^{-11/3}\dot\nu_\mathrm{gw}\right]^{3/5}$$ — the primary, distance/mass-independent observable; $[\nu_\mathrm{gw}^{-11}\dot\nu_\mathrm{gw}^3]$ is constant through the inspiral.
- Total mass vs. mass ratio: $$M_\mathrm{tot} = \frac{M_\mathrm{chirp}}{[\alpha(1-\alpha)]^{3/5}} \geq 2.3\,M_\mathrm{chirp}$$ — minimum at equal masses ($\alpha=1/2$).
- Total mass from max GW frequency: $$M_\mathrm{tot} = \frac{1}{\pi\sqrt8}\frac{c^3}{G\nu_\mathrm{gw}^\mathrm{max}}$$ — from the coalescence condition $R_S = 2GM/c^2$; higher merger frequency → lighter system.
- Distance estimate: $$r = \frac{16}{\sqrt5}\frac{G}{c^4}\frac{\mu R^2\omega_s^2}{h_0}$$ — from setting $L=4\pi r^2F$.
- Redshift transformations: $$\nu_\mathrm{gw}^\mathrm{det}=\frac{\nu_\mathrm{gw}^s}{1+z},\quad \dot\nu_\mathrm{gw}^\mathrm{det}=\frac{\dot\nu_\mathrm{gw}^s}{(1+z)^2},\quad M_\mathrm{chirp}^\mathrm{det}=(1+z)M_\mathrm{chirp}^s$$ — detector-frame chirp/individual masses are over-estimated by $(1+z)$.

## 3. Key Algorithms / Procedures

**Determining BH binary parameters from a GW signal (e.g. GW150914):**
1. From the time–frequency spectrogram, read successive time intervals $\Delta t$ between wave minima at different inspiral stages → gives $\nu_\mathrm{gw}$ and $\dot\nu_\mathrm{gw}$ at each stage.
2. Compute the chirp mass from $\nu_\mathrm{gw}, \dot\nu_\mathrm{gw}$ (constant across stages — internal consistency check); GW150914 → $M_\mathrm{chirp}\approx 30\,M_\odot$.
3. Get a **minimum total mass**: $M_\mathrm{tot}^\mathrm{min}=2.3\,M_\mathrm{chirp}$ (equal-mass assumption) → $\approx 69\,M_\odot$.
4. Read the **maximum observed GW frequency** ($\nu_\mathrm{gw}^\mathrm{max}\approx 330$ Hz for GW150914) and compute $M_\mathrm{tot}$ independently from the coalescence-frequency formula → $70\,M_\odot$ (cross-check against step 3; also gives merger $R_S$ as a consistency check with the minimum orbital separation from the data).
5. Solve $[\alpha(1-\alpha)]^{3/5}=M_\mathrm{chirp}/M_\mathrm{tot}$ for the mass ratio $\alpha$ → individual masses $m_1=\alpha M_\mathrm{tot}$, $m_2=(1-\alpha)M_\mathrm{tot}$.
6. Estimate the source distance $r$ from the flux–luminosity relation using measured $h_0$, $\nu_\mathrm{gw}$ (hence $\omega_s$, $R$) and $\mu$.
7. If an EM counterpart or host-galaxy redshift is available (or via luminosity-distance–redshift cosmology), correct detector-frame masses to source-frame masses using the $(1+z)$ relations.

**Assessing SN vs. failed SN (BH) outcome for a massive star:**
1. Evolve the star to the point of Fe-core infall (e.g. via PARSEC/MESA models).
2. Compute the compactness $\xi_{2.5}$ from the enclosed mass/radius at $2.5\,M_\odot$.
3. Compare to threshold $\approx0.2$: below → successful SN, NS remnant; above → failed SN, direct BH collapse (no optical transient, full mass retained in remnant).

**Detecting an IMBH candidate in a globular cluster:**
1. Obtain a high-resolution surface-brightness profile (HST/AO imaging) — look for a power-law density cusp vs. flat King-model core.
2. Obtain resolved stellar radial velocities near the centre (AO-assisted IFS) to build a velocity-dispersion profile.
3. Compare the observed VD profile to a King-only model vs. a "King + IMBH" model; a Keplerian ($v\propto r^{-1/2}$) upward cusp within the sphere of influence supports an IMBH.

## 4. Watch Out For

- The Newtonian "escape velocity = $c$" derivation gives the numerically correct $R_s$ but for the wrong physical reason — don't confuse this heuristic with an actual GR derivation.
- The event horizon is **not** a physical surface; nothing special happens locally to an infalling observer crossing it (exam trap: "you'd feel a wall" is wrong).
- Distant observers never see anything actually cross the horizon (infinite coordinate time / frozen image); the infalling observer's own proper time to cross is finite. Don't mix these two frames.
- Compactness threshold $\xi_{2.5}\approx0.2$ is **not monotonic** in $M_\mathrm{ZAMS}$ — the $18$–$26\,M_\odot$ range is mixed (both outcomes possible), not a clean cutoff.
- Metallicity effect is twofold and same-signed: lower $Z$ → less wind mass loss **and** larger CO core → both push toward more massive remnants. At solar $Z$, no single star can produce a remnant $>25\,M_\odot$ — this rules out single-star channels for LIGO's most massive BH-BH events at solar metallicity.
- GW frequency is **twice** the orbital frequency ($\omega_\mathrm{gw}=2\omega_s$) — a common factor-of-2 slip when converting between them.
- Chirp mass alone cannot give individual masses (mass-ratio degeneracy); the "equal mass" total-mass estimate is a strict **lower bound**, not the true value, unless independently confirmed (as it was for GW150914 via the max-frequency method).
- GW strain is dimensionless and minuscule ($h_0\sim10^{-22}$) — remember the "one-atom-diameter change over the Earth–Sun distance" scale to sanity-check any strain calculation.
- Newtonian orbital mechanics has **no GW emission**; the quadrupole (not dipole or monopole) is the lowest radiating multipole for gravity — a purely spherical or axisymmetric collapse emits no GWs.
- Detector-frame (observed) masses/chirp mass are systematically **larger** than source-frame values by $(1+z)$; always ask whether a quoted LIGO mass has been redshift-corrected. Redshift cannot be read from the GW signal alone — needs an EM counterpart or cosmological distance–redshift relation.
- Two widely separated detectors (Hanford–Livingston, light-travel time ~10 ms) are required to reject local noise and confirm a real signal — a single-detector "detection" is not credible evidence.
- Final BH mass after a merger is always **less** than $m_1+m_2$; the mass deficit is radiated as GWs (e.g. ~$3\,M_\odot$ for GW150914) — don't assume mass is conserved in the merger remnant.
- Distinguish the two independent NS-merger EM signatures and their physical origins: short GRB (relativistic jet, arrives within ~seconds) vs. kilonova (radioactive r-process decay, evolves over days, reddens as ejecta becomes lanthanide-rich/high-opacity).
- r-process happens in NS mergers (and some CC SNe); s-process happens in AGB stars — do not conflate the two neutron-capture channels or their products (r: Au/Pt/Eu/Ir/U; s: Ba/La/Ce/Pb).
- IMBH existence remains **observationally unconfirmed** — sphere-of-influence signals are subtle (sub-arcsecond) and require both imaging (density cusp) and spectroscopy (velocity-dispersion cusp) together; either alone is not sufficient evidence.
- Cosmic Censorship is a **conjecture**, not a proven theorem — do not state it as an established law of GR.
