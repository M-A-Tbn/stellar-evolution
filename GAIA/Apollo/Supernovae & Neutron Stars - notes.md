# Supernovae & Neutron Stars — Study Notes
**Source:** `28.SNe+NS_hifi.md` | **Session:** Supernovae & Neutron Stars | **Date:** 2026-05-23

---

## 1. Supernova Classification

### 1.1 Overview of the Classification Scheme

Supernovae are classified along two independent axes: spectroscopic appearance and physical explosion mechanism. Understanding both axes is essential, because the spectroscopic class tells you what the progenitor's envelope looked like at the time of explosion, while the explosion-mechanism class tells you the underlying physics that powered the event.

The primary spectroscopic split is simple: does the spectrum show hydrogen features? If yes, the event is **Type II**. If no hydrogen is present, the event is **Type I**, which is then further subdivided by the presence or absence of silicon and helium.

The classification tree proceeds as follows:

- **Type II** — hydrogen present in spectrum.
- **Type Ia** — no hydrogen, but silicon (Si) features present. These are thermonuclear explosions of white dwarfs.
- **Type Ib** — no hydrogen, no silicon, but helium (He) features present. Core collapse of a stripped massive star that has lost its H envelope.
- **Type Ic** — no hydrogen, no silicon, no helium. Core collapse of a massive star that has lost both its H-rich and He-rich envelopes.

The explosion-mechanism classification groups these differently. **Type Ia** supernovae are thermonuclear (driven by runaway nuclear burning in a white dwarf). **Types Ib, Ic, and II** are all **core-collapse supernovae (CC SNe)**, driven by the gravitational collapse of a massive star's iron core.

### 1.2 Type I Supernovae: The Hydrogen-Free Events

A Type I supernova is defined purely by what is absent — no hydrogen feature appears in the spectrum at any phase. This absence reveals that the progenitor had already shed its hydrogen-rich outer layers before the explosion, either through binary mass transfer, stellar winds, or common-envelope evolution.

**Type Ib and Type Ic** share the same physical engine (core collapse of a massive star), but differ in how much of the envelope was stripped. Type Ib progenitors retained their helium layer while losing all hydrogen; Type Ic progenitors went further, losing both hydrogen and helium envelopes. The stripping mechanism is typically strong stellar winds (as in Wolf-Rayet stars) or Roche-lobe overflow onto a binary companion. The key implication is that the spectroscopic Type I designation does not mean the explosion physics is the same — Type Ia is fundamentally different from Ib/Ic.

---

## 2. Type Ia Supernovae: Thermonuclear Explosions

### 2.1 The Fundamental Mechanism

Type Ia supernovae arise from the thermonuclear explosion of a carbon-oxygen white dwarf (CO-WD) whose mass exceeds or reaches the Chandrasekhar limit. The Chandrasekhar mass ($M_{Ch} \approx 1.4\,M_\odot$) is the maximum mass supportable by electron degeneracy pressure. When this limit is exceeded, the white dwarf can no longer maintain hydrostatic equilibrium and begins to collapse. However, the increasing density and temperature ignite explosive carbon burning before the structure fully collapses, releasing sufficient nuclear energy to completely disrupt the star. No compact remnant is left — the entire WD is incinerated.

Two distinct progenitor scenarios are proposed for how a CO-WD can reach or exceed the Chandrasekhar mass: the **double-degenerate scenario** (merging of two white dwarfs) and the **single-degenerate scenario** (accretion from a non-degenerate companion). Both lead to the same explosion physics once the critical density is reached.

### 2.2 The Double-Degenerate Scenario

The double-degenerate scenario begins with a primordial binary system consisting of two intermediate-mass stars, each with initial masses roughly $5$–$9\,M_\odot$. Both stars evolve and undergo **common envelope episodes** — phases during which both stellar envelopes are physically in contact, leading to significant orbital shrinkage and mass ejection from the system. After these episodes, the system consists of two CO white dwarfs in a very close orbit, with a combined mass exceeding the Chandrasekhar limit.

For the merger to occur within a Hubble time, the orbital separation must be small enough that energy loss via **gravitational wave emission** gradually shrinks the orbit until the two WDs come into contact. The gravitational wave timescale depends sensitively on orbital separation, so only close-enough systems merge in time. Wider binaries produce WDs that never merge before the Universe is too old.

The merger sequence, as illustrated in numerical simulations, proceeds through three stages: (1) a spiral-in phase where the two WDs orbit each other with trailing tidal arms of ejected material forming a disk; (2) an extreme close-approach phase where matter flows actively between and around the two objects; (3) an explosive detonation as the merged object exceeds $M_{Ch}$.

Once the merged product surpasses the Chandrasekhar mass, electron degeneracy can no longer provide the required pressure. The structure collapses, and the rising density triggers **carbon ignition at $\rho \approx 10^9$ g cm$^{-3}$** in a degenerate environment. Because the gas is degenerate, temperature increases without corresponding pressure increases (no thermostatic regulation), so the burning immediately becomes a runaway — a **thermonuclear explosion**. The evolutionary sequence for two $5$–$9\,M_\odot$ primordial stars (from Iben & Tutukov 1984) involves: primordial system $\rightarrow$ first common envelope ($\dot{M} \sim 10^{-3}\,M_\odot\,\text{yr}^{-1}$, lasting $\sim 10^3$ yr) $\rightarrow$ intermediate system (WD + giant, orbital period $\sim 2$–$30$ days) $\rightarrow$ second common envelope $\rightarrow$ two WDs with orbital period of minutes to hours $\rightarrow$ gravitational wave inspiral $\rightarrow$ disk formation (period $\sim 15$–$30$ s) $\rightarrow$ SN Ia.

### 2.3 The Single-Degenerate Scenario

An alternative route involves a CO-WD in a binary system with a normal (non-degenerate) companion star. The WD accretes hydrogen-rich material from the companion as it evolves and overflows its Roche lobe. Two requirements must be satisfied: (1) the WD must grow to $M_{Ch}$ through accretion, and (2) no hydrogen should remain in the ejecta at the time of explosion (since Type Ia spectra show no H).

The single-degenerate evolutionary sequence from Chandrasekhar-mass thermonuclear supernova: (a) two main sequence stars ($1\,M_\odot$ + $2\,M_\odot$) in orbit; (b) the more massive star evolves off the MS and fills its Roche lobe as a red giant, transferring mass to the companion; (c) the $2\,M_\odot$ star sheds its envelope, leaving a $0.8\,M_\odot$ RGB/HB core; the companion gains mass becoming $2.2\,M_\odot$; (d) the core becomes a $0.6\,M_\odot$ WD; (e) the $2.4\,M_\odot$ companion evolves, fills its Roche lobe, and transfers mass onto the WD; (f) the WD reaches $1.4\,M_\odot$ and explodes, while the companion is stripped to $0.9\,M_\odot$.

### 2.4 The Nova Problem: Accretion Rate Constraints

The single-degenerate scenario faces a crucial constraint: the accretion rate onto the WD must fall within a narrow acceptable window. This is illustrated on a plot of $\log(\dot{M}_H)$ vs. $M_{WD}/M_\odot$, which identifies four distinct regimes:

**Low accretion rate** ($\dot{M} \sim 10^{-9}\,M_\odot\,\text{yr}^{-1}$): The WD experiences strong H-burning pulses — the **nova phenomenon**. About $10^{-4}\,M_\odot$ of H accumulates and then ignites explosively through the CNO cycle in a degenerate environment. The temperature reaches $10^8$ K, some He is converted to C, and eventually radiation pressure expels essentially all the accreted material (and sometimes some of the pre-existing WD layers) into space. The cycle repeats as long as accretion continues. Because most of the accreted mass is lost in each nova eruption, the WD takes longer than the Hubble time to reach $M_{Ch}$ — this path cannot produce a Type Ia SN.

**High accretion rate** ($\dot{M} \sim 10^{-7}\,M_\odot\,\text{yr}^{-1}$): Accretion is so rapid that the WD acquires a thick hydrogen envelope and swells to red-giant dimensions. The system then evolves toward a common-envelope phase — also not a viable path to SN Ia.

**Intermediate accretion rate** (the viable window): The H flashes are mild. H-burning ashes build up a helium layer. This He layer can itself experience a flash, which may trigger the next stage of burning. This intermediate regime is the only one in which the WD can grow steadily toward $M_{Ch}$.

### 2.5 Sub-Chandrasekhar-Mass Progenitors

A separate class of models considers CO white dwarfs that never reach $M_{Ch}$. In principle, a sub-$M_{Ch}$ WD cannot reach the critical density and temperature for explosive carbon burning by simple accretion. However, a sub-set of models shows an important alternative trigger: **detonations in the accumulated helium layer**.

If a $\sim 0.2\,M_\odot$ helium shell is built up on a WD in the mass range $0.6$–$0.8\,M_\odot$ (a region highlighted in the accretion-rate diagram), this He shell can detonate. The He-detonation ignites at the top of the CO core and drives a strong inward-propagating shock wave into the CO core, which triggers a secondary **carbon detonation** at the center. This double-detonation mechanism can thus destroy the entire WD even below the Chandrasekhar mass, though it is not the standard or most accepted model.

---

## 3. SN Ia Explosion Mechanics

### 3.1 Deflagration vs. Detonation

The thermonuclear runaway in a Type Ia SN is ignited in the central regions of the WD, where $\rho \approx 10^9$ g cm$^{-3}$. The burning front then propagates outward, but the speed at which it propagates fundamentally determines the nucleosynthetic output.

The key parameter is whether the burning front travels at subsonic or supersonic velocity relative to the unburned material.

A **deflagration wave** travels subsonically. Because it is slower than sound, the outer WD layers have time to receive the pressure perturbation and expand. As the WD expands, its density decreases. This density decrease means the burning front encounters successively less dense material as it propagates outward, reducing the maximum temperature reached in the burning and allowing the production of a range of elements — not just iron-peak elements.

A **detonation wave** travels supersonically. The unburned layers have no time to respond before the shock arrives and incinerates them at their original high density. A full detonation of a CO-WD at $\rho \sim 10^9$ g cm$^{-3}$ would produce essentially only nickel (Fe-peak elements) — there would be no intermediate-mass elements in the ejecta. This pure detonation model is ruled out observationally because Type Ia SN spectra show silicon, sulfur, calcium, and other intermediate-mass elements.

### 3.2 The W7 Deflagration Model

The W7 model (Nomoto et al. 1984) is the canonical deflagration model and the benchmark for SN Ia nucleosynthesis. In this model, a C deflagration wave (carrying a convective front) propagates outward through the WD over approximately $3.22$ seconds. The evolution of temperature and density within the WD during the deflagration proceeds through 8 discrete time steps (labeled 1 through 8).

The burning is divided into two compositional zones, demarcated at approximately $0.85\,M_\odot$:

- **Inner region** ($0$ to $\sim 0.85\,M_\odot$): The high density means high temperature at the burning front, producing Fe-peak elements: $^{56}$Ni ($0.613\,M_\odot$), $^{56}$Fe ($0.145\,M_\odot$), $^{54}$Fe, $^{58}$Ni.
- **Outer region** ($\sim 0.85$ to $1.4\,M_\odot$): Lower density at the time of burning (because the WD has expanded) produces intermediate-mass elements: $^{28}$Si ($0.155\,M_\odot$), $^{32}$S, $^{40}$Ca, $^{24}$Mg, $^{16}$O ($0.140\,M_\odot$), $^{12}$C.

The total nickel yield of $\sim 0.61\,M_\odot$ is the primary determinant of the peak luminosity (see Section 3.4). The density of the layer that the burning front crosses directly controls the temperature reached and hence the nucleosynthetic outcome, because the nuclear reaction rates are extremely temperature-sensitive.

### 3.3 The Delayed Detonation Model

The pure deflagration (W7) and the pure detonation are both unsatisfactory in different ways. The best match to observations is achieved by the **delayed detonation model**: the explosion begins as a subsonic deflagration (allowing the WD to expand and intermediate-mass elements to form), and at a later stage undergoes a transition to a supersonic detonation. This transition is thought to be triggered when the compression shock from the deflagration wave crosses the now low-density outer layers, causing a runaway detonation.

The delayed detonation model naturally reproduces the observed mixed nucleosynthesis (iron-peak elements in the inner ejecta, intermediate-mass elements in the outer ejecta) and the overall observed light curve and spectral evolution. The density at which the deflagration-to-detonation transition occurs determines the relative fractions of Ni and intermediate-mass elements — and thus the peak luminosity of the event. This sensitivity to the transition density is one of the physical bases for the observed scatter in SN Ia peak brightness.

### 3.4 The Light Curve and Standard Candle Utility

The SN Ia light curve is powered entirely by **radioactive decay**: no hydrogen envelope, no shock-heated gas dominates the optical emission. The chain is:

$$^{56}\text{Ni} \xrightarrow{\text{EC},\ t_{1/2} = 6.1\ \text{days}} {^{56}\text{Co}} \xrightarrow{80\%\ \text{EC},\ 20\%\ \beta^+,\ t_{1/2} = 77\ \text{days}} {^{56}\text{Fe}}$$

$^{56}$Ni is synthesized in the explosive Si-burning region of the detonation/deflagration. It decays rapidly via electron capture to $^{56}$Co, which then decays more slowly to stable $^{56}$Fe. The early light curve (first weeks) is dominated by the $^{56}$Ni decay (half-life 6.1 days), driving a sharp rise and peak. The later light curve (months) follows the $^{56}$Co half-life of 77 days, producing the characteristic long radioactive tail.

The shape of the late-time light curve also depends on (1) the fraction of gamma-rays from radioactive decays that escape the ejecta (which increases over time as the ejecta expand and become optically thin), and (2) the fraction of positrons (from the minority $\beta^+$ channel of $^{56}$Co decay) that are annihilated within the ejecta rather than escaping.

**Standard candle properties**: The ejected material is mainly Fe (from $^{56}$Ni decay) since the burning front transforms most material into Ni as it propagates. No compact remnant is left. The characteristic observables are:
- Kinetic energy: $\sim 10^{51}$ erg
- Ejecta velocity: $v \sim 5{,}000$–$30{,}000$ km s$^{-1}$
- No neutrino burst (purely thermonuclear, no core collapse)
- Optical energy released: $E_\text{optical} \sim 10^{49}$ erg
- Peak luminosity: $L_\text{peak} \sim 10^{43}$ erg s$^{-1}$ sustained for $\sim 2$ weeks
- Absolute magnitude at peak: $M_B \approx -19.6$
- Galactic rate: $\sim 1$ per 200 years

The **stretch-factor correction** (also called the Phillips relation or width-luminosity relation) is critical: the raw SN Ia light curves observed from the Calán/Tololo survey show a range of peak brightnesses and temporal widths, but once the time axis is stretched to normalize light curve width, all Type Ia light curves collapse onto a single master template. This makes Type Ia SNe **secondary standard candles** (they require calibration via this empirical correction) but extraordinarily powerful ones. They are responsible for the discovery of the accelerating expansion of the Universe.

---

## 4. Type II and Core-Collapse Supernovae

### 4.1 Overview of Core-Collapse SNe

Type II, Ib, and Ic supernovae share the same fundamental physical engine: the gravitational collapse of the iron core of a massive star. Stars with $M > 8$–$11\,M_\odot$ (with the exact threshold depending on the treatment of convection and mass loss) develop iron cores through successive stages of nuclear burning (H → He → C → Ne → O → Si → Fe). Iron cannot release energy through fusion — the iron nucleus is at the minimum of the binding energy per nucleon — so once an iron core forms, there is no energy source to halt collapse.

For stars with $M > 11\,M_\odot$: the iron core exceeds $M_{Ch}$, electron degeneracy can no longer support it, and the core collapses. If the initial mass is $11\,M_\odot < M < 25\,M_\odot$, the collapse produces a neutron star. For $M > 25\,M_\odot$, the remnant exceeds the maximum neutron star mass and becomes a black hole.

For stars with $7\,M_\odot < M < 11\,M_\odot$: carbon ignites in a mildly degenerate core at $T \sim 5$–$6 \times 10^8$ K. The main C-burning reactions are:

$$^{12}\text{C} + ^{12}\text{C} \rightarrow ^{24}\text{Mg} \rightarrow ^{20}\text{Ne} + ^4\text{He}$$
$$\rightarrow ^{23}\text{Na} + p$$
$$\rightarrow ^{23}\text{Mg} + n$$

After central C burning, the core is composed mainly of oxygen (from prior He burning) and neon (from C burning), and becomes electron degenerate, producing an ONe WD — or in some conditions an electron-capture supernova.

### 4.2 Observational Properties: Type II vs. Type Ia

The full contrast between the two main classes is tabulated below.

| Property | Type Ia | Type II |
|---|---|---|
| Spectral signature | No H | H present |
| Progenitor mass | Any (WD in binary) | $M > 8\,M_\odot$ |
| Remnant | None | Neutron star or black hole |
| Kinetic energy | $\sim 10^{51}$ erg | $\sim 10^{51}$ erg |
| Ejecta velocity | $5{,}000$–$30{,}000$ km s$^{-1}$ | $2{,}000$–$30{,}000$ km s$^{-1}$ |
| Neutrino burst | None | $\sim 3 \times 10^{53}$ erg |
| Optical energy | $\sim 10^{49}$ erg | $\sim 10^{49}$ erg |
| Peak luminosity | $\sim 10^{43}$ erg s$^{-1}$ for $\sim 2$ weeks | $\sim 3 \times 10^{42}$ erg s$^{-1}$ for $\sim 3$ months |
| Light curve tail | $^{56}$Ni + $^{56}$Co decay | $^{56}$Co decay only |
| Galactic rate | 1 per 200 yr | 2 per 100 yr |

Two key physical differences stand out. First, Type II SNe generate an enormous **neutrino burst** ($\sim 3 \times 10^{53}$ erg), which is the dominant energy release channel — far exceeding the kinetic energy of the ejecta and the optical luminosity. The optical energy represents only $\sim 10^{-4}$ of the total energy budget. Second, the Type II light curve peak is lower and more extended because it is powered partly by the shock-heated hydrogen envelope (which gradually recombines, powering the plateau in Type II-P subclass) and only later by the $^{56}$Co decay tail.

### 4.3 Chemical Enrichment Contributions

**Type II SNe** eject large amounts of material processed through H, He, and C burning: primarily **$\alpha$-elements** (O, Mg, Ca, Si, Ti) and a moderate amount of Fe ($\sim 0.1\,M_\odot$ per event — most iron stays in the remnant). They produce virtually all the oxygen in the Universe and all the $\alpha$-elements, plus the r-process elements (heavy elements built by rapid neutron capture).

**Type Ia SNe** eject predominantly **iron-peak elements**: typically $\sim 0.6\,M_\odot$ of Fe per event (originally synthesized as $^{56}$Ni). They produce about two-thirds of all the iron in the Galaxy. They also eject He-burning products ($^{12}$C, $^{16}$O) and Si-burning products (mainly Fe-group nuclei), but virtually no $\alpha$-elements in proportion to iron.

**Novae** contribute small amounts ($\sim 10^{-5}\,M_\odot$ per ejection) of rare CNO-processed nuclei ($^{13}$C, $^{15}$N, $^{17}$O, $^{22}$Na), with $\sim 35$ events per year in the Galaxy but minimal total mass contribution.

**Stellar winds and planetary nebulae** (from AGB and massive Wolf-Rayet stars) contribute CNO-processed material, He, $^{12}$C, and s-process heavy elements.

---

## 5. Chemical Enrichment and the [$\alpha$/Fe]–[Fe/H] Diagram

### 5.1 The Logarithmic Abundance Scale

Chemical abundances of stars are measured in a logarithmic differential scale normalized to the Sun. For any element "el":

$$\left[\frac{\text{el}}{\text{H}}\right] = \log\left(\frac{\text{el}}{\text{H}}\right)_* - \log\left(\frac{\text{el}}{\text{H}}\right)_\odot$$

By definition, $[\text{el}/\text{H}] = 0$ for the Sun. This scale is linear in the logarithm of abundance ratios. In practice:
- $[\text{Fe/H}] = 0$: solar iron abundance
- $[\text{Fe/H}] = -0.5$: one-third of solar iron
- $[\text{Fe/H}] = -2$: one-hundredth of solar iron (the star formed from a very metal-poor gas)

The $[\text{Fe/H}]$ value serves as a **proxy for the iron abundance of the interstellar medium (ISM) at the time the star formed**. Because the stellar atmosphere preserves a record of the ISM composition at birth, the observed surface abundances of old stars encode the chemical enrichment history of their birth environment.

### 5.2 Physical Basis of the [$\alpha$/Fe]–[Fe/H] Diagram

The [$\alpha$/Fe]–[Fe/H] diagram is the most powerful observational diagnostic of the chemical evolution history of a stellar population. It combines two quantities that respond to different supernova types on different timescales:

- **$\alpha$-elements** (O, Mg, Ca, Si, Ti): produced almost exclusively in massive stars and ejected by Type II SNe on very short timescales ($< 30$ Myr, the lifetime of $M > 8$–$10\,M_\odot$ stars).
- **Iron (and iron-peak elements)**: produced predominantly by Type Ia SNe, which operate on a **delayed timescale** — the minimum delay from star formation to first Type Ia SN is $\sim 30$–$35$ Myr in the single-degenerate model, but the timescale distribution extends from several $10^7$ yr to $10^{10}$ yr.

Because of this time-lag, there is a window early in the history of any stellar system when only Type II SNe are enriching the ISM. During this phase, the ISM is enriched with $\alpha$-elements and modest amounts of Fe in a fixed ratio — the [$\alpha$/Fe] ratio is elevated above solar and remains roughly constant, forming a **plateau**.

### 5.3 Interpretation of the Diagram Features

The theoretical [$\alpha$/Fe]–[Fe/H] diagram has three characteristic regions:

**The Plateau**: At low metallicities ($[\text{Fe/H}] \lesssim -1$ for the Milky Way halo), [$\alpha$/Fe] is approximately constant at $\sim +0.35$ (super-solar). This plateau exists because only Type II SNe have had time to enrich the ISM. Both $\alpha$-elements and Fe are produced by SN II, but in a ratio that is $\alpha$-enhanced relative to solar. The **height of the plateau** is determined by the IMF: a top-heavy IMF produces more massive stars, more SN II per unit stellar mass, and a higher [$\alpha$/Fe] plateau.

**The Knee**: At a critical metallicity, the first Type Ia SNe begin exploding and injecting large amounts of iron without proportionally increasing the $\alpha$ abundances. The [$\alpha$/Fe] ratio drops steeply — this is the "knee" in the diagram. The **position of the knee** (the metallicity at which the downturn begins) is determined by the Star Formation Rate (SFR). A higher SFR means SN II events occur more rapidly and inject more Fe before the first SN Ia explode, so the knee shifts to higher [Fe/H]. A lower SFR leaves the ISM at lower metallicity when the first SN Ia appear, so the knee occurs at lower [Fe/H].

**The Descending Slope**: After the knee, Type Ia SNe dominate the iron enrichment. [$\alpha$/Fe] decreases toward solar while [Fe/H] increases. The efficiency and slope of this descent depend on the SFR and the specific delay-time distribution of SN Ia.

Importantly, stars in the Milky Way halo and disk do exhibit this pattern in observations: a plateau at low metallicity, a knee near $[\text{Fe/H}] \approx -1$, and a descending slope.

### 5.4 Comparisons Across Different Environments

The [$\alpha$/Fe]–[Fe/H] pattern is environment-specific and can serve as a **chemical DNA signature** of the population's birth environment, because different environments have different SFRs:

**Local Group Dwarf Galaxies**: Low SFR. The knee occurs at very low metallicity ($[\text{Fe/H}] \approx -1.5$). The ISM was relatively metal-poor when the first SN Ia exploded because few SN II had enriched it. The descending slope covers low metallicities.

**Galactic Halo**: Intermediate SFR. The knee occurs around $[\text{Fe/H}] \approx -1.0$.

**Galactic Bulge**: High SFR. Stars formed rapidly, SN II enriched the ISM to high metallicity before the first SN Ia exploded. The knee occurs at high metallicity ($[\text{Fe/H}] \approx -0.3$ or even approaching solar). The plateau extends to much higher [Fe/H].

This chemical signature is a direct observational tool to reconstruct the star formation history of any environment where stellar spectroscopy is feasible.

### 5.5 Heavy Elements from Neutron Capture

Elements with $A > 56$ are built primarily by neutron capture reactions, not by charged-particle fusion:

- **s-process** in AGB stars (low-mass stars, "main component"): produces elements along the valley of beta-stability with $A > 90$, including Pb ($\sim 90\%$ of all Pb in the Galaxy).
- **s-process in massive stars** ("weak component"): produces elements in the range $70 < A < 90$.
- **r-process**: produces the most neutron-rich isotopes and the heaviest elements (U, Th), as well as about half of all elements above iron. The r-process sites include **core-collapse SNe** and, crucially, **kilonova events** (mergers of two neutron stars — gravitational wave events like GW170817).

The r-process elements produced in SN II and kilonovae (neutron star mergers) have become a key frontier. The kilonova contribution was confirmed observationally in 2017.

---

## 6. Stellar Endpoints: The Full Mass-Remnant Map

### 6.1 Overview

The final fate of a star is determined almost entirely by its initial mass on the Zero-Age Main Sequence (ZAMS). The full taxonomy of stellar endpoints, from lowest to highest mass:

**$M < 0.08\,M_\odot$** — Never ignite hydrogen burning. Final stage: **Brown Dwarfs**.

**$0.08\,M_\odot < M < 0.5\,M_\odot$** — Ignite H but never ignite He burning. Final stage: **He white dwarfs** (He-WDs). These stars have a permanently degenerate helium core from the moment He could ignite; the star leaves the main sequence but the He core never reaches the required temperature.

**$0.5\,M_\odot < M < 7\,M_\odot$** — Ignite He burning (through the helium flash in lower-mass stars, non-degenerately in higher-mass stars), but never ignite C burning. The degenerate CO core left after He exhaustion cannot contract further at WD masses. Final stage: **CO white dwarfs** (CO-WDs).

**$7\,M_\odot < M < 11\,M_\odot$** — Ignite C burning in a mildly degenerate environment ($T \sim 5$–$6 \times 10^8$ K), but never ignite oxygen burning. The resulting degenerate ONeMg core can either cool to an **O-Ne WD** or, if the core grows large enough through shell burning, undergo **electron-capture supernova (EC SN)** when the ONeMg core exceeds the Chandrasekhar mass and electron captures on $^{20}$Ne and $^{24}$Mg trigger collapse.

**$M > 11\,M_\odot$** — Burn through all nuclear fuels (H → He → C → Ne → O → Si → Fe) in a non-degenerate core. The iron core collapses to produce a **Type II (CC) SN**:
- $11\,M_\odot < M < 25\,M_\odot$: remnant is a **Neutron Star**
- $M > 25\,M_\odot$: remnant is a **Black Hole**

The transition between NS and BH formation is not sharp and depends on the detailed explosion dynamics, the equation of state of dense matter, and rotation. Some models produce BHs by direct collapse (no visible SN) for the most massive stars.

### 6.2 The Mass-Remnant Diagram

The full mass-to-remnant diagram maps the internal core structure (which sets the outcome) as a function of initial mass. The key interior structure types are: permanently degenerate He core (below $0.5\,M_\odot$), transient degenerate He core then degenerate CO core (0.5–$2.2\,M_\odot$), non-degenerate He core then degenerate CO core ($2.2$–$7\,M_\odot$), mildly degenerate CO core ($7$–$11\,M_\odot$), and non-degenerate CO core leading to Type II SN (above $11\,M_\odot$). The structural convection zones also shift: stars below $0.3\,M_\odot$ are fully convective; those from $0.3$–$1.2\,M_\odot$ have a radiative core and convective envelope; those above $1.2\,M_\odot$ have a convective core.

---

## 7. Neutron Stars: Structure and Properties

### 7.1 Basic Physical Parameters

Neutron stars (NSs) are the remnants of core-collapse SNe produced by stars with $11\,M_\odot < M < 25\,M_\odot$. They are among the most extreme physical objects in the Universe. Their key parameters are:

- **Mass**: $1.2$–$2.5\,M_\odot$
- **Radius**: $R = 10$–$15$ km
- **Central density**: $\rho_c = 10^{14}$–$10^{15}$ g cm$^{-3}$

The structure consists of a very thin atmosphere and non-degenerate envelope approximately **one meter** thick, within which the temperature increases by a factor of $\sim 100$ and the density reaches values comparable to a white dwarf with relativistic degenerate electrons. Just **one kilometer below the surface** the density reaches $\sim 10^{11}$ g cm$^{-3}$ and increases toward $10^{15}$ g cm$^{-3}$ at the center.

### 7.2 Why NS Masses Cluster Near the Chandrasekhar Mass

The measured masses of neutron stars in binary systems are remarkably concentrated near $1.4\,M_\odot$ — the Chandrasekhar mass. This is not coincidental but physically expected: essentially all NSs form from the collapse of iron cores that were supported by **degenerate electron pressure** and therefore had masses close to $M_{Ch}$. The Chandrasekhar mass sets the mass of the collapsing core, and since most of the iron core mass becomes the NS (with only a fraction carried away by neutrinos), the resulting NS mass is inevitably close to $M_{Ch}$.

### 7.3 Neutron Number and Density

The number of nucleons in a typical NS of $M = 1.4\,M_\odot$:

$$n_\text{neutr} = \frac{1.4\,M_\odot}{m_n} = \frac{1.4 \times 2 \times 10^{33}\,\text{g}}{1.7 \times 10^{-24}\,\text{g}} = 10^{57}$$

The estimated nucleon ratio is $n:p:e = 8:1:1$ (8 neutrons for every proton and electron). The density:

$$\rho = \frac{1.4 \times 2 \times 10^{33}}{\frac{4}{3}\pi (10^6)^3} \approx 7 \times 10^{14}\ \text{g cm}^{-3}$$

This density is **a few times larger than that of atomic nuclei** ($\rho_\text{nucl} \approx 2 \times 10^{14}$ g cm$^{-3}$). To put it in perspective: one teaspoon of NS material would weigh approximately as much as all of Earth's 8 billion inhabitants combined.

### 7.4 The Mass-Radius Relation and the Oppenheimer-Volkov Limit

As in white dwarfs, neutron stars are supported by degenerate particle pressure — but this time by **degenerate neutrons** rather than electrons. The derivation of the mass-radius relation parallels the WD case, with the crucial substitution $m_e \rightarrow m_n$:

Starting from the virial balance between gravitational pressure ($\sim \frac{2}{3}\pi G\rho^2 R^2$) and degenerate neutron pressure ($\sim \frac{1}{3}\frac{\hbar^2}{m_H}(\rho/m_H)^{5/3}$), substituting $\rho = M/(\frac{4}{3}\pi R^3)$, one derives:

$$M^{1/3} R_{NS} = \frac{\hbar^2}{m_H^{8/3}} \frac{(\frac{4}{3}\pi)^{1/3}}{2\pi G} = \text{const}$$

which gives $M R_{NS}^3 = \text{const}$. The more accurate result is:

$$M = \left(\frac{15.2\ \text{km}}{R}\right)^3 M_\odot$$

This implies — as for WDs — that more massive NSs are **smaller** and **denser**. Two reference equations linking central density, radius, and mass:

$$R = 14.6 \times \left(\frac{10^{15}\ \text{g\,cm}^{-3}}{\rho_c}\right)^{1/6}\ \text{km}$$

$$M = \left(\frac{15.2\ \text{km}}{R}\right)^3 M_\odot$$

Numerical examples:
- $\rho_c = 10^{15}$ g cm$^{-3}$ → $R = 14.6$ km, $M = 1.1\,M_\odot$
- $\rho_c = 1.5 \times 10^{15}$ g cm$^{-3}$ → $R = 13.6$ km, $M = 1.4\,M_\odot$

Analogously to the Chandrasekhar mass for WDs, there exists a **maximum mass for neutron stars** beyond which no known pressure can halt collapse: the **Oppenheimer-Volkov mass limit**:

$$M_{NS}^\text{limit} \sim 2.5\text{–}3\,M_\odot$$

Exceeding this limit leads to collapse to a black hole. Unlike the Chandrasekhar mass (which is precisely derived from well-understood electron degeneracy), the Oppenheimer-Volkov limit is **poorly constrained** because it depends on the equation of state (EoS) of matter at densities exceeding nuclear saturation density — a regime where the relevant physics (quark condensates, pion condensates, hyperon formation) is not yet theoretically resolved. Different proposed super-nuclear EoS give maximum NS masses ranging from $\sim 2.0$ to $2.7\,M_\odot$, as shown in Mass-Radius diagrams using EoS labels such as ALF1, AP3, BSK20, MS1, SLY, etc.

---

## 8. Neutron Star Internal Structure

### 8.1 Overview of Layers

The interior of a neutron star is organized into distinct layers, each characterized by a different density regime, composition, and dominant physics. Progressing from the surface inward:

**Outer Crust** ($\rho \sim 10^6$–$10^{11}$ g cm$^{-3}$): The most external region has densities comparable to those in white dwarfs. Electrons are relativistic and degenerate. At $\rho \sim 10^6$ g cm$^{-3}$, iron nuclei coexist with non-relativistic free electrons (crystallized ion lattice). At $\rho \sim 10^9$ g cm$^{-3}$, electrons become relativistic. Their high Fermi energy enables **electron capture** by heavy nuclei, including iron:

$$e^- + p \rightarrow n + \nu_e$$

producing increasingly neutron-rich isotopes such as $^{62}$Ni, $^{64}$Ni, $^{66}$Ni. Under normal conditions these isotopes would be unstable and undergo $\beta^-$ decay:

$$n \rightarrow p + e^- + \nu$$

However, in a **completely degenerate electron gas**, all low-energy electron states below the Fermi level are occupied. The emitted electron from $\beta^-$ decay has no available state to occupy, so the decay is **forbidden**. This phenomenon is called **neutronization** — neutrons are thermodynamically stabilized by the degenerate electron sea.

**Inner Crust** ($\rho \sim 10^{11}$–$10^{12}$ g cm$^{-3}$): At $\rho \approx 4 \times 10^{11}$ g cm$^{-3}$, the density is high enough that neutrons begin to appear outside nuclear structures — the **neutron drip point**. The reaction:

$$p^+ + e^- \rightarrow n + \nu_e$$

proceeds because the electron kinetic energy is large enough to supply the energy corresponding to the neutron-proton mass difference:

$$m_n c^2 = m_p c^2 + m_e c^2 + 0.78\ \text{MeV}$$

The plasma now consists of neutron-rich nuclei, non-relativistic degenerate free neutrons, and relativistic degenerate electrons. At $\rho \sim 10^{12}$ g cm$^{-3}$, the number of free neutrons increases until **neutron degeneracy pressure begins to dominate** over electron degeneracy pressure.

**Interior** ($\rho \sim 10^{14}$ g cm$^{-3}$): At this density, the inter-neutron spacing inside nuclei becomes comparable to that outside, so nuclear structures effectively **dissolve**. The plasma is a mixture of free neutrons, protons, and electrons in the ratio $n:p:e^- \approx 8:1:1$.

**Core** (above $\rho \approx 4 \times 10^{14}$ g cm$^{-3}$): Superfluid free neutrons and superconducting free protons coexist with relativistic electrons. At even higher densities, pion or kaon condensation may occur, and at the highest densities ($\rho > 5 \times 10^{14}$ g cm$^{-3}$), other elementary particles (hyperons, pions, kaons) or even deconfined quarks may appear. The physics here is genuinely unknown — this is the **super-nuclear equation of state problem**.

The internal structure at the neutron drip boundary between inner crust and interior is marked by $\rho \sim \rho_\text{nucl} \approx 2 \times 10^{14}$ g cm$^{-3}$.

### 8.2 Comparison with White Dwarfs

| Property | Neutron Star | White Dwarf |
|---|---|---|
| Mass | $1$–$3\,M_\odot$ | $< 1.4\,M_\odot$ |
| Radius | $\sim 10$ km | $\sim 5{,}000$ km |
| Density | $\sim 10^{14}$ g cm$^{-3}$ | $\sim 10^7$ g cm$^{-3}$ |
| Supporting pressure | Neutron degeneracy | Electron degeneracy |
| Inner structure | Outer crust + inner crust + interior + core | Thin envelope + CO lattice + degenerate core |

The Sun for reference: $R = 7 \times 10^5$ km, $\rho \sim 1$ g cm$^{-3}$.

---

## 9. The Core Collapse: Radius Shrinkage, Angular Momentum, and Magnetic Fields

### 9.1 The Factor-500 Radius Collapse

The ratio of pre-collapse to post-collapse core radius can be estimated by comparing the WD and NS mass-radius relations. The WD radius scales as:

$$R_{WD} \propto \frac{\hbar^2}{G m_e M^{1/3}} \left(\frac{Z}{A}\frac{1}{m_H}\right)^{5/3}$$

The NS radius scales as:

$$R_{NS} \propto \frac{\hbar^2}{G M^{1/3}} \left(\frac{1}{m_H}\right)^{8/3}$$

Taking the ratio for an iron core ($Z/A = 26/56 \approx 0.5$):

$$\frac{R_\text{core}^\text{pre-col}}{R_\text{core}^\text{post-col}} = \frac{m_n}{m_e}\left(\frac{Z}{A}\right)^{5/3} = \frac{1.7 \times 10^{-24}}{9.1 \times 10^{-28}} \times 0.3 \approx 500$$

The collapse reduces the core radius by **a factor of 500**. An iron core of WD dimensions ($R \sim 5{,}000$ km) is compressed to a neutron star of $\sim 10$ km radius.

### 9.2 Spin-Up by Angular Momentum Conservation

Conservation of angular momentum during the collapse naturally produces a rapidly rotating neutron star. Assuming no mass loss during collapse ($M_{WD} = M_{NS}$) and treating the core as a uniform sphere with moment of inertia $I = \frac{2}{5}MR^2$:

$$I_i \omega_i = I_f \omega_f \implies \frac{2}{5}M R_i^2 \omega_i = \frac{2}{5}M R_f^2 \omega_f$$

$$\omega_f = \omega_i \left(\frac{R_i}{R_f}\right)^2 \implies P_{NS} = P_i \left(\frac{R_f}{R_i}\right)^2$$

$$P_{NS} = 4 \times 10^{-6}\,P_\text{pre-collapse}$$

For a pre-collapse core rotation period comparable to observed WD periods ($P_{WD} \sim 1{,}000$ s):

$$P_{NS} \approx 4 \times 10^{-6} \times 10^3\ \text{s} = 4 \times 10^{-3}\ \text{s}$$

This is a period of a few milliseconds. Even the slowest pre-collapse cores are spun up to millisecond or near-millisecond periods at birth. **Neutron stars are born as fast rotators.**

### 9.3 Magnetic Field Amplification

The magnetic flux through the stellar surface is conserved during the collapse. The magnetic flux through a sphere is:

$$\Phi = B \cdot 4\pi R^2 = \text{const}$$

Therefore:

$$B_i \cdot 4\pi R_i^2 = B_f \cdot 4\pi R_f^2 \implies B_{NS} = B_{WD} \left(\frac{R_{WD}}{R_{NS}}\right)^2$$

With $R_i/R_f \approx 500$ and assuming a modest pre-collapse field $B_{WD} \sim 10^8$ G:

$$B_{NS} \sim 10^8 \times (500)^2 = 10^8 \times 2.5 \times 10^5 = 2.5 \times 10^{13}\ \text{G}$$

Typical NS magnetic fields are in the range $B \sim 10^{13}$–$10^{14}$ G. Even a modest pre-collapse field is amplified to enormous values. Combined with the factor-500 radius compression, the collapse naturally produces:

- **A fast-rotating compact object** (period of milliseconds at birth)
- **A compact object with an enormously strong magnetic field** ($10^{13}$–$10^{14}$ G)

These are exactly the defining properties of a neutron star / pulsar.

---

## 10. Neutron Star Cooling

### 10.1 Thermal Evolution

Neutron stars are born at temperatures of $T \sim 10^{11}$ K (immediately post-collapse). Cooling is initially extremely rapid because of the intense emission of neutrinos. The thermal evolution proceeds as:

| Time after formation | Temperature |
|---|---|
| Formation | $\sim 10^{11}$ K |
| Minutes | $\sim 10^{10}$ K |
| $\sim 100$ years | $\sim 10^8$ K |
| $\sim 10^5$ yr | $\sim 10^6$ K |

After $\sim 10^5$–$10^6$ years, neutrino luminosity $L_\nu$ becomes negligible, and the cooling energy budget is:

$$L_\gamma + L_\nu = -\frac{dE}{dt}$$

where $E$ is the thermal energy of the degenerate neutrons and relativistic electrons. The residual thermal energy exists because neutrons and electrons at finite temperature have some available states below the Fermi energy; without a contribution from fully non-degenerate ions, this is the primary energy reservoir for the cooling phase.

### 10.2 Observational Consequences

At $T \sim 10^6$ K (late cooling), a neutron star radiates predominantly as a blackbody in the **X-ray** domain. The Wien displacement law gives:

$$\lambda T = 0.29\ \text{cm\,K} \implies \lambda = \frac{0.29}{10^6}\ \text{cm} = 29\ \text{Å} \quad (\text{X-ray})$$

The luminosity:

$$L = 4\pi R^2 \sigma T^4 = 4\pi (10^6\ \text{cm})^2 \times 5.6 \times 10^{-5} \times (10^6)^4 \approx 7 \times 10^{32}\ \text{erg s}^{-1}$$

This is actually **lower than the Sun's luminosity** ($L_\odot \approx 3.8 \times 10^{33}$ erg s$^{-1}$). Direct observation of the thermal X-ray emission from old NSs is thus extremely difficult. In practice, isolated neutron stars are observed primarily as **pulsars**, whose radio emission is powered not by thermal energy but by the rotational kinetic energy of the NS.

---

*End of Part 1. Continued in: `Supernovae & Neutron Stars - notes 2.md`*
