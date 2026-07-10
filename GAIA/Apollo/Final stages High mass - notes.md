# Final Stages of High-Mass Stars: Advanced Burning, Core Collapse, Supernovae, and Nucleosynthesis

**Sources:** Lecture slides covering the complete evolutionary sequence of intermediate-to-high-mass stars, from carbon ignition through to the final supernova explosion, remnant formation, and chemical enrichment of the galaxy. Includes discussion of nuclear burning stages, electron-capture supernovae, the iron core collapse mechanism, the neutrino-driven delayed explosion, explosive nucleosynthesis (including the r-process and $^{56}$Ni decay chain), Type II supernova light curves, and observational SN classification.
**Session:** 26.finalstages_highmass

---

## 1. Evolution of Intermediate-Mass Stars ($7 < M/M_\odot < 9$–$11$)

### 1.1 Overview and Evolutionary Outcomes by Mass

The stellar mass at the end of core He-burning is the single most important parameter determining a star's ultimate fate. The evolutionary outcomes can be read off a mass-versus-fate diagram, with key transition masses acting as boundaries:

- Stars below $\sim 0.5\,M_\odot$ develop a degenerate helium core and leave behind a **He white dwarf (He-WD)**.
- Stars up to $\sim 7\,M_\odot$ develop a degenerate carbon-oxygen core and end as **CO white dwarfs**.
- Stars in the range **$7$–$11\,M_\odot$** ("mildly degenerate CO core" regime) ignite carbon burning under conditions of moderate electron degeneracy; depending on the competition between mass loss and core growth, they leave either an **O-Ne white dwarf** or undergo an **electron-capture supernova (EC-SN)**.
- Stars above $\sim 11\,M_\odot$ ("no degenerate CO core" regime) undergo the full sequence of advanced nuclear burning and explode as **Type II core-collapse supernovae**.

The transition mass $M_\mathrm{up}$ (roughly $8\,M_\odot$) marks the boundary between stars that end as white dwarfs and those that can produce neutron stars. The exact value of $M_\mathrm{up}$ depends on details of convection, mass loss, and nuclear reaction rates. Understanding this range is critical because it determines which channel of chemical enrichment — WD cooling, EC-SN, or classical core-collapse SN — contributes to the interstellar medium.

### 1.2 Chemical Composition of the CO Core After He Burning

After helium core burning completes, the interior is composed primarily of carbon and oxygen. The relative proportions are determined by the competition between the triple-alpha process (which builds $^{12}$C) and the subsequent alpha-capture reaction:

$$^{12}\mathrm{C} + ^4\mathrm{He} \rightarrow ^{16}\mathrm{O} + \gamma$$

Because this reaction efficiently converts carbon into oxygen at the temperatures and densities characteristic of helium burning, the post-He-burning core is **oxygen-rich**. The oxygen fraction depends on stellar mass: more massive cores run at higher temperatures, which favour oxygen production, so the oxygen mass fraction is systematically higher in more massive cores. White dwarf interior structure models confirm this: a $1.0\,M_\odot$ WD shows a much higher and flatter oxygen profile than a $0.6\,M_\odot$ WD. This oxygen fraction matters because it determines the amount of fuel available for carbon ignition and subsequent burning stages.

### 1.3 Carbon Ignition in the Mildly Degenerate Core

Stars in the $7$–$11\,M_\odot$ range ignite carbon fusion when the core temperature reaches $T \sim 5$–$6 \times 10^8\,\mathrm{K}$, but crucially they do so in a **weakly degenerate** core — unlike higher-mass stars where carbon ignites in a fully non-degenerate environment, and unlike lower-mass stars where the CO core would never reach ignition. The partial electron degeneracy plays a decisive role in shaping how the burning proceeds.

The primary carbon fusion reactions are:

$$^{12}\mathrm{C} + ^{12}\mathrm{C} \rightarrow ^{20}\mathrm{Ne} + ^4\mathrm{He}$$

and possibly the follow-on reaction:

$$^{20}\mathrm{Ne} + ^4\mathrm{He} \rightarrow ^{24}\mathrm{Mg} + \gamma$$

At the end of carbon burning the core is therefore composed principally of **oxygen** (the dominant pre-existing species from He burning), **neon** (the main product of $^{12}$C$+^{12}$C), and possibly **magnesium**. The precise mixture and the mass of this O-Ne-Mg core then determine the star's final fate.

### 1.4 The Role of Neutrino Energy Losses in Advanced Burning

From carbon burning onward, **thermal neutrino losses** dominate the energy budget and fundamentally alter the star's internal evolution. Three key neutrino-production processes operate in the relevant temperature-density regime:

1. **Photo-neutrino process:** $e^- + \gamma \rightarrow e^- + \nu + \bar{\nu}$. An electron scatters off a photon and the energy is carried away as a neutrino pair.
2. **Plasma process (plasmon decay):** $\gamma_\mathrm{pl} \rightarrow e^- + e^+ \rightarrow \nu + \bar{\nu}$. A plasmon (collective quantum of the electron plasma) decays into a neutrino-antineutrino pair.
3. **Pair-annihilation process:** Electron-positron pairs produced at high temperature annihilate into neutrino pairs.

Each of these processes drains energy from the stellar interior at a rate that increases steeply with temperature and density. The critical consequence is that from carbon burning onward, **nuclear burning in the core cannot supply all the energy the star requires**. The star must also draw on gravitational potential energy: the core contracts on the Kelvin-Helmholtz timescale of that burning stage, providing the extra luminosity via the virial theorem. This is why the timescales for advanced burning stages become drastically shorter — the core contracts rapidly between stages, accelerating toward collapse.

This feedback between neutrino losses and core contraction is the engine that drives the "staircase" structure of the $T$–time diagram (see Section 2.1): during each burning stage the temperature is roughly constant (the burning thermostat), but the drop between stages as the core contracts raises the temperature rapidly to the threshold for the next fuel.

### 1.5 The Carbon Flash: Off-Centre Ignition and Convective Flame

The carbon burning process in a weakly degenerate core is directly analogous to the **helium flash** in low-mass stars. Partial electron degeneracy decouples the pressure from the temperature, so when carbon ignites, the energy release does not immediately expand and cool the gas — instead the temperature rises, the burning accelerates, and a **flash** develops. Additionally, neutrino cooling preferentially removes energy from the centre, making the temperature (and hence the carbon-burning rate) peak slightly off-centre rather than at the geometric centre.

Carbon burning therefore always proceeds in three distinct steps:

1. **Off-centre convective flash:** Carbon ignites at a shell off the centre where the temperature is highest (the net effect of modest degeneracy and neutrino cooling from the centre). The flash is analogous to the He-flash: runaway burning before pressure can respond.
2. **Convective flame propagation inward:** The burning region generates a convective zone whose inner boundary ("convective flame front") propagates toward the centre, progressively dredging in unburned carbon and erasing the electron degeneracy.
3. **Stable central C-burning:** Once the flame reaches the centre and degeneracy is lifted, quiescent, stable carbon burning proceeds in the fully convective core.

The mass-dependence of this process is dramatic: at lower stellar mass, the core degeneracy is stronger, so the C flash occurs **progressively further off-centre**. The $M_r$-vs-time Kippenhahn diagrams (for masses $9.0$, $9.5$, $10.0$, $10.5$, $10.8$, $11.3\,M_\odot$) illustrate this clearly — as mass decreases within this range, the arrow marking the flash origin moves to larger $M_r$ (i.e., further from the centre). For the $11.3\,M_\odot$ star, the flash is almost at the centre; for the $9.0\,M_\odot$ star, it occurs far off-centre and the convective flame must travel a significant fraction of the core radius.

### 1.6 The Super-AGB Phase

After the carbon flash, the subsequent evolution of stars in the $7$–$11\,M_\odot$ range closely mirrors that of low-mass stars on the AGB. The post-carbon-burning O-Ne core is surrounded by He- and H-burning shells, and the following events occur in sequence:

- **Second Dredge-Up (II DREDGE-UP):** Convection from the envelope penetrates into the He-exhausted core region, mixing He-burning products toward the surface.
- **He-shell thermal pulses:** The He-burning shell becomes thermally unstable, generating periodic flashes (thermal pulses) whose luminosity oscillations are visible in the $\log(L/L_\odot)$ vs time plot — intense oscillations in both $L_\mathrm{tot}$ and $L_\mathrm{He}$.
- **Third Dredge-Up (III DREDGE-UP):** Convection driven by each He-shell flash extends into the He-burning region and may carry He-burning products (mainly $^{12}$C) up to the surface.
- **Dredge-out:** In some mass ranges, convection that develops above the He-burning shell merges with the surface convection zone, bringing He-burning products (mainly carbon) to the surface in a single large mixing event. This is effectively the super-AGB analog of the third dredge-up: **dredge-out + dredge-up = III DREDGE-UP** in this context.

This phase is called the **Super-AGB phase** because the star behaves like an AGB star but with a more massive, more compact O-Ne-Mg core (rather than the CO core of classical AGB). The stellar structure at this stage consists of a **Red Supergiant envelope** surrounding the **inert O-Ne-Mg core**, with a hydrogen-burning shell, a helium-burning shell, and a carbon-burning shell progressively depositing mass onto the growing O-Ne core.

### 1.7 The Critical Competition: O-Ne WD vs Electron-Capture SN

The fate of the Super-AGB star is determined by whether the O-Ne-Mg core grows to approximately the Chandrasekhar mass ($M_\mathrm{Ch} \approx 1.4\,M_\odot$) before the envelope is lost to stellar winds. Two outcomes are possible:

- **High mass-loss rate:** The carbon-burning shell adds mass to the O-Ne core, but the wind strips the envelope faster than the core can grow. When the envelope is exhausted, the core mass is still well below $M_\mathrm{Ch}$. The result is an **O-Ne white dwarf** with a mass typically in the range $\sim 1.0$–$1.2\,M_\odot$.
- **Low mass-loss rate:** The envelope persists long enough for the carbon-burning shell to push the core mass up to $\sim M_\mathrm{Ch}$. At that point, a qualitatively different physical process takes over — electron capture — and the star explodes as an **electron-capture supernova (EC-SN)**, leaving a **neutron star** remnant.

The sensitivity to mass loss rate means that the boundary between these two outcomes is not a sharp mass threshold but a transition zone whose location depends on the uncertain stellar wind prescriptions. This is one of the key uncertainties in stellar evolution theory for intermediate-mass stars.

### 1.8 Electron-Capture Supernovae (EC-SN)

When the degenerate O-Ne-Mg core approaches $M_\mathrm{Ch}$, a distinct collapse mechanism operates that is different from the classical iron core collapse of more massive stars:

1. **Electron capture on Mg and Ne:** The protons locked inside $^{24}$Mg and $^{20}$Ne nuclei begin to capture the free electrons that provide pressure support. This transforms protons into neutrons: $^{24}$Mg $+ e^- \rightarrow ^{24}$Na $+ \nu_e$, and similarly for $^{20}$Ne. The physical reason this initiates at $M_\mathrm{Ch}$ is that at very high density, the electron Fermi energy becomes high enough to make electron capture energetically favorable.

2. **Runaway collapse via positive feedback:** Electron capture reduces the electron pressure $\rightarrow$ the core contracts $\rightarrow$ density increases $\rightarrow$ the electron Fermi energy increases further $\rightarrow$ electron capture is even more favoured. This is a runaway process with no stabilizing mechanism.

3. **Oxygen ignition in a semi-degenerate environment:** When the central density reaches $\sim 2.5 \times 10^{10}\,\mathrm{g\,cm^{-3}}$, the temperature has risen sufficiently for **oxygen burning to ignite**. This happens in a semi-degenerate environment, so the burning proceeds as a deflagration (a subsonic burning front) that propagates outward through the contracting core, converting O-Ne-Mg material into iron-peak elements.

4. **Neutron star formation:** The collapse of the core produces a **neutron star**. The EC-SN mechanism is thought to produce relatively weak explosions with small amounts of $^{56}$Ni, and the neutron stars formed may have lower kicks than those from classical core collapse.

EC-SNe occupy an interesting theoretical niche: they are the lowest-energy core-collapse supernovae, and observationally they may correspond to some fraction of Type IIP supernovae with low nickel masses.

### 1.9 O-Ne White Dwarfs

If the Super-AGB star loses its envelope before the core reaches $M_\mathrm{Ch}$, the remnant is an **O-Ne white dwarf**. These objects have distinctive properties compared to the more common CO white dwarfs:

- **Mass range:** $\sim 1.0$–$1.2\,M_\odot$ — substantially higher than the typical $0.6\,M_\odot$ CO WD, reflecting the fact that only the most massive WD progenitors develop O-Ne cores.
- **Chemical composition (typical mass fractions):**
  - $^{16}$O: $0.50$–$0.70$
  - $^{20}$Ne: $0.15$–$0.35$
  - $^{23}$Na: $0.05$ (roughly constant across the mass range)
  - $^{22}$Ne: $0.001$–$0.01$
- **Cooling:** The cooling mechanism is the same as for CO WDs (energy loss via photon emission from the surface, with the interior heat stored in ionic lattice vibrations). However, O-Ne WDs cool **faster** than CO WDs of similar mass because the mean atomic mass $A$ is larger (O: $A=16$, Ne: $A=20$, vs C: $A=12$, O: $A=16$ for CO). For the same total mass, a larger $A$ means fewer ions, hence a smaller thermal heat capacity $C \propto N_\mathrm{ions} k_B$, so less thermal energy is stored and it is radiated away more quickly.

---

## 2. Final Stages of Truly Massive Stars ($M > 11\,M_\odot$)

### 2.1 The Staircase: Advanced Burning Stages Overview

For stars above $\sim 11\,M_\odot$, the CO core at the end of He burning is non-degenerate (the $\log\rho$–$\log T$ track stays safely in the non-degenerate regime, well away from the electron-degeneracy boundary). This is a qualitative difference from the $7$–$11\,M_\odot$ range: carbon ignites gently and stably, not as a flash, and subsequent burning stages follow in rapid succession.

The overall evolution can be visualised as a **staircase in $T$–time space**:
- The **horizontal steps** represent stable thermonuclear burning phases, during which nuclear energy keeps the core temperature roughly constant.
- The **rising slopes** between steps represent rapid gravitational contractions (powered by the virial theorem), during which the core heats up without burning to prepare conditions for the next fuel.

The burning stages in sequence are: H $\rightarrow$ He $\rightarrow$ C $\rightarrow$ Ne $\rightarrow$ O $\rightarrow$ Si $\rightarrow$ Fe (inert).

Each successive stage operates at higher temperature and density, and — critically — for a dramatically shorter duration, primarily because neutrino losses escalate steeply with temperature and drain the nuclear energy away before the star can maintain equilibrium for long. This is documented quantitatively in Section 2.7.

### 2.2 Carbon Burning in a Non-Degenerate Core ($T \sim 8 \times 10^8\,\mathrm{K}$)

In massive stars ($M > 11\,M_\odot$), carbon burning ignites at $T \sim 8 \times 10^8\,\mathrm{K}$ in a non-degenerate core, without the flash mechanism. The dominant reactions are:

$$^{12}\mathrm{C} + ^{12}\mathrm{C} \rightarrow ^{16}\mathrm{O} + 2\,^4\mathrm{He}$$

$$^{12}\mathrm{C} + ^{12}\mathrm{C} \rightarrow ^{20}\mathrm{Ne} + ^4\mathrm{He}$$

The first reaction breaks the $^{12}$C nucleus and releases two alpha particles along with $^{16}$O. The second is the direct production of $^{20}$Ne with one alpha particle. Both reactions release alpha particles (helium-4 nuclei) that can then drive further reactions, particularly the production of $^{24}$Mg via $^{20}$Ne$\,+\,^4$He.

At $T \sim 8 \times 10^8\,\mathrm{K}$ and $\rho \sim 8 \times 10^5\,\mathrm{g\,cm^{-3}}$, the carbon burning timescale is $\sim 10^3\,\mathrm{yr}$ for a $20\,M_\odot$ star — already three to four orders of magnitude shorter than helium burning.

### 2.3 Neon Burning ($T \sim 1.6 \times 10^9\,\mathrm{K}$)

Neon burning does not proceed via direct $^{20}$Ne$+^{20}$Ne fusion. Instead, it is driven by **photo-disintegration**: at $T \sim 1.6 \times 10^9\,\mathrm{K}$, the thermal photon bath is energetic enough to break apart $^{20}$Ne nuclei:

$$^{20}\mathrm{Ne} + \gamma \rightarrow ^{16}\mathrm{O} + ^4\mathrm{He}$$

The liberated alpha particles are immediately captured by other $^{20}$Ne nuclei:

$$^{20}\mathrm{Ne} + ^4\mathrm{He} \rightarrow ^{24}\mathrm{Mg} + \gamma$$

The net effect is that neon burning produces oxygen and magnesium. The reaction is not a fusion of two heavy nuclei but rather a photo-disintegration coupled to alpha-capture. This is why neon burning occurs at a lower temperature than oxygen burning: it is energetically easier to photo-disintegrate Ne than to fuse two oxygen nuclei. The condition for photo-disintegration to be significant is that the photon energy exceeds the nuclear binding energy difference, which for $^{20}$Ne occurs at $T \sim 1.5$–$1.6 \times 10^9\,\mathrm{K}$. At the characteristic density $\rho \sim 5 \times 10^6\,\mathrm{g\,cm^{-3}}$, the timescale is only $\sim 3\,\mathrm{yr}$.

### 2.4 Oxygen Burning ($T \sim 2 \times 10^9\,\mathrm{K}$)

Oxygen burning ignites at $T \sim 2 \times 10^9\,\mathrm{K}$ and $\rho \sim 7 \times 10^6\,\mathrm{g\,cm^{-3}}$, with a timescale of only $\sim 200\,\mathrm{days}$ ($\approx 0.8\,\mathrm{yr}$). The oxygen-oxygen fusion reactions are:

$$^{16}\mathrm{O} + ^{16}\mathrm{O} \rightarrow ^{32}\mathrm{S}^* \rightarrow ^{28}\mathrm{Si} + ^4\mathrm{He}$$

$$^{16}\mathrm{O} + ^{16}\mathrm{O} \rightarrow ^{31}\mathrm{P} + p$$

$$^{16}\mathrm{O} + ^{16}\mathrm{O} \rightarrow ^{31}\mathrm{S} + n$$

The compound nucleus $^{32}$S is formed in an excited state and then decays by alpha emission (main channel), proton emission, or neutron emission. The primary products are therefore **silicon, sulfur, phosphorus**, plus free protons and neutrons that drive a network of secondary reactions producing calcium, argon, and other intermediate-mass elements. At the characteristic density and temperature, oxygen burning generates the bulk of the Si, S, Cl, Ar, K, and Ca that we observe in the universe.

### 2.5 Silicon Burning ($T \sim 3$–$4 \times 10^9\,\mathrm{K}$)

Silicon burning is fundamentally different from all previous stages. At $T \sim 3$–$4 \times 10^9\,\mathrm{K}$ and $\rho \sim 5 \times 10^7\,\mathrm{g\,cm^{-3}}$, the photon bath is energetic enough to photo-disintegrate even silicon:

$$^{28}\mathrm{Si} + \gamma \rightarrow ^{24}\mathrm{Mg} + ^4\mathrm{He}$$

$$\dots$$

$$^{12}\mathrm{C} + \gamma \rightarrow 3\,^4\mathrm{He}$$

Silicon burning is therefore not a direct fusion of two $^{28}$Si nuclei but rather a **photo-disintegration cascade** that strips nuclei down to alpha particles. These liberated alpha particles are then the **main fuel** for a chain of **alpha-capture reactions** that build up progressively heavier nuclei:

$$^{12}\mathrm{C} + ^4\mathrm{He} \rightarrow ^{16}\mathrm{O} + \gamma \quad (7.6\,\mathrm{MeV})$$
$$^{16}\mathrm{O} + ^4\mathrm{He} \rightarrow ^{20}\mathrm{Ne} + \gamma \quad (4.7\,\mathrm{MeV})$$
$$\dots$$
$$^{52}\mathrm{Cr} + ^4\mathrm{He} \rightarrow ^{56}\mathrm{Ni} + \gamma$$

Each step adds one alpha particle and increases the atomic mass by 4. The chain continues until it reaches the iron group, where the binding energy per nucleon peaks and no further energy can be extracted from fusion. The material is said to be in **nuclear statistical equilibrium (NSE)** — a statistical distribution favouring iron-peak nuclei. The timescale for silicon burning is only $\sim 1\,\mathrm{week}$.

### 2.6 The $^{56}$Ni Endpoint and Its Radioactive Decay Chain

Silicon burning does not produce $^{56}$Fe directly. Instead, the endpoint is **$^{56}$Ni** (28 protons, 28 neutrons). This is because during silicon burning the core is hot and the timescale is too short for **weak interactions** (beta decays, electron captures) to equilibrate the neutron-to-proton ratio. The material therefore stays at equal numbers of neutrons and protons, which for 56 nucleons gives $^{56}$Ni rather than $^{56}$Fe ($Z=26$, $N=30$).

$^{56}$Ni is radioactive and decays via:

$$^{56}\mathrm{Ni} \rightarrow ^{56}\mathrm{Co} + e^+ + \nu_e \quad (\tau_{1/2} = 6.1\,\mathrm{days})$$

$$^{56}\mathrm{Co} \rightarrow ^{56}\mathrm{Fe} + e^+ + \nu_e \quad (\tau_{1/2} = 77.1\,\mathrm{days})$$

Both decays produce positrons and neutrinos, releasing energy that, when the ejecta are optically thin, thermalizes and powers the supernova light curve at late times (the "radioactive tail"). The abundance pattern of the cosmic alpha-elements (those with $A = 4n$: O, Ne, Mg, Si, S, Ar, Ca, Ti) is a direct consequence of the alpha-capture chain, and the peaks in the cosmic abundance distribution correspond to these nuclei.

### 2.7 Timescales of Advanced Burning: The Catastrophic Acceleration

One of the most striking features of massive star evolution is the dramatic shortening of successive burning timescales. For a representative $20\,M_\odot$ star:

| Fuel | Main Product | $T_9$ ($10^9\,\mathrm{K}$) | Duration |
|------|-------------|--------------------------|----------|
| H | He | $0.02$ | $10^7\,\mathrm{yr}$ |
| He | C, O | $0.2$ | $10^6\,\mathrm{yr}$ |
| C | Ne, Mg | $0.8$ | $10^3\,\mathrm{yr}$ |
| Ne | O, Mg | $1.5$ | $3\,\mathrm{yr}$ |
| O | Si, S | $2.0$ | $\sim 200\,\mathrm{days}$ |
| Si | Fe | $3.5$ | $\sim 1\,\mathrm{week}$ |

The acceleration from $10^7$ years (hydrogen burning) to 1 week (silicon burning) is a factor of $\sim 10^9$. The dominant cause is not that nuclear reactions run faster at higher $T$ (though they do), but that **neutrino losses scale roughly as $T^9$**, so at the temperatures of silicon burning the neutrinos are draining the nuclear energy reservoir almost as fast as it is produced. The star barely has time to adjust before the core runs out of fuel.

From a practical standpoint, this means that a massive star spends 99.99% of its life on or near the main sequence, and the last stages — from carbon ignition to iron core collapse — span less than a few thousand years. A star observed as a red supergiant is almost certainly still in hydrogen- or helium-shell burning; the advanced stages are essentially invisible because they proceed too fast and emit predominantly in neutrinos, not photons.

### 2.8 The Onion-Shell Structure

At the end of silicon burning, the interior of a massive star has developed a classic **onion-shell structure**, with layers ordered by nuclear weight from outside in:

- H-burning shell (outermost active shell)
- He-burning shell
- C-burning shell
- O-burning shell
- Ne layer (vestigial)
- Si-burning shell
- **Inert Fe core** (innermost, $\sim 1.3$–$2.0\,M_\odot$ depending on stellar mass)

Each shell boundary marks a sharp composition gradient. In the Kippenhahn diagram (Interior Mass $M_r$ vs $\log(t_\mathrm{collapse} - t)$, showing how the structure evolves as the moment of collapse approaches), the chemical zones are visible as distinct regions: the Si zone, O zone, C zone, He zone, and H envelope shrink in characteristic patterns as each shell consumes its fuel. The diagram for a $25\,M_\odot$ star shows this structure with great clarity and is the canonical example used in stellar astrophysics.

---

## 3. Toward the Iron Core Collapse

### 3.1 Why the Iron Core Collapses: The Exhaustion of Nuclear Energy

Once silicon burning has produced an iron core of $\sim 1.3$–$2.0\,M_\odot$, the stellar interior faces an absolute energy crisis. Iron-group nuclei sit at the **peak of the nuclear binding energy curve**: fusion of iron nuclei into anything heavier requires energy (endothermic) rather than releasing it. There is no nuclear energy source that can be tapped.

Without a nuclear energy source to provide pressure support, the iron core must contract. As it contracts, it gets hotter and denser. Under these extreme conditions, two processes initiate and accelerate the collapse:

**1. Electron captures on iron-group nuclei:**

$$^{56}\mathrm{Fe} + e^- \rightarrow ^{56}\mathrm{Mn} + \nu_e$$
$$^{56}\mathrm{Mn} + e^- \rightarrow ^{56}\mathrm{Cr} + \nu_e$$

These reactions occur on many iron-group nuclei (not just Fe) and convert protons (inside nuclei) into neutrons. This process **reduces the number of free electrons**, directly reducing the electron degeneracy pressure that was providing part of the support. Each captured electron produces a neutrino that immediately leaves the star, carrying away energy.

**2. Photo-disintegration of iron nuclei ($T \sim 5$–$10 \times 10^9\,\mathrm{K}$):**

$$^{56}\mathrm{Fe} + \gamma \rightarrow 13\,^4\mathrm{He} + 4n$$
$$^4\mathrm{He} + \gamma \rightarrow 2p^+ + 2n$$

At temperatures of $\sim 5$–$10 \times 10^9\,\mathrm{K}$, the thermal photon field is energetic enough to reverse all of the nuclear burning that the star spent millions of years performing. Each $^{56}$Fe nucleus is ripped apart into 13 helium-4 nuclei and 4 free neutrons, absorbing $\sim 124\,\mathrm{MeV}$ per reaction. This is the nuclear equivalent of the gravitational energy the star invested in building up heavy elements being suddenly reclaimed by photons. The process is **endothermic** — it removes thermal energy from the gas, further reducing the pressure and accelerating the collapse.

**3. The URCA process:**

$$p^+ + e^- \rightarrow n + \nu_e$$

Free protons (liberated by photo-disintegration of alpha particles) capture electrons. This is the URCA process, named for a Rio de Janeiro casino (because it takes energy away and gives nothing back). It operates on free protons rather than nuclei, converting them directly to neutrons and neutrinos. It efficiently removes both electrons (reducing pressure) and energy (neutrino emission).

### 3.2 Quantitative Energy Loss Rates

For a $20\,M_\odot$ star undergoing core collapse, the neutrino luminosity reaches approximately:

$$E_\nu \sim 3 \times 10^{45}\,\mathrm{erg\,s^{-1}}$$

This is an enormous luminosity — comparable to the entire optical luminosity of the observable universe — and it is sustained for seconds. The consequences are:

(a) **Reduction in electron number:** Free electrons are systematically removed by capture, reducing the electron pressure support. The effective adiabatic index $\Gamma$ drops below $4/3$, the critical value for stability, at which point pressure can no longer balance gravity — the Jeans criterion is violated and collapse is unavoidable.

(b) **Increase in neutrino energy losses:** The neutrino emission itself carries away thermal energy, further reducing the temperature and pressure. The combination of both effects produces a **rapid, runaway contraction** of the iron core.

### 3.3 Free-Fall Collapse

Once the adiabatic index drops below $4/3$, the iron core enters near-**free-fall collapse**. The free-fall timescale is:

$$\tau_\mathrm{FF} \propto \frac{1}{\sqrt{\rho_0}}$$

where $\rho_0$ is the initial density before collapse. At $\rho \sim 10^{10}\,\mathrm{g\,cm^{-3}}$ (the density at which the collapse accelerates dramatically), the dynamical timescale is:

$$\tau_d \approx 10^{-2}\,\mathrm{s} = 10\,\mathrm{ms}$$

The core collapses from a radius of $\sim 1000\,\mathrm{km}$ to nuclear density in a time of order tens of milliseconds. This is the fastest known stellar evolutionary transition — a star's entire core structure changes irreversibly in less time than it takes to blink.

---

## 4. The Explosion Mechanism

### 4.1 The Core Bounce and Shock Wave Formation

As the inner core ($\sim 0.7\,M_\odot$) reaches nuclear density $\rho_\mathrm{nuc} \approx 2.4 \times 10^{14}\,\mathrm{g\,cm^{-3}}$, the **strong nuclear force** transitions from attractive to repulsive (nuclear matter is nearly incompressible). The collapse of the inner core abruptly halts, and because infall had been supersonic, the core **overshoots** nuclear density, then rebounds elastically.

This rebound — the **core bounce** — launches an outward-propagating pressure wave into the still-infalling outer core. The outer core is collapsing at supersonic speed, so the outgoing wave steepens into a **strong shock wave** at the sonic surface. The shock carries the kinetic energy of the rebounding inner core.

**Energy balance (prompt explosion estimate):**

The total gravitational energy released during collapse is:

$$\Delta E_g \approx \frac{GM^2}{R_f} \approx 10^{53}\,\mathrm{erg}$$

where $R_f \sim 10\,\mathrm{km}$ is the radius of the proto-neutron star. Of this, only $\sim 10^{51}\,\mathrm{erg}$ is needed to unbind the stellar envelope (the kinetic energy of the eventual SN ejecta). On paper, there is $\sim 100 \times$ more energy available than needed. However, $\approx 10^{53}\,\mathrm{erg}$ is rapidly carried away by neutrinos, and only a small fraction of this can be deposited back into the envelope. The challenge is the **coupling efficiency** between neutrino energy and the shock.

### 4.2 Why the Prompt Shock Fails

The shock does not simply propagate outward and blow the star apart — it stalls. The reason is two-fold:

1. **Energy loss by photo-disintegration:** As the shock passes through the infalling iron layers, it heats the material to temperatures at which photo-disintegration of iron nuclei occurs. Each $^{56}$Fe nucleus that is photo-disintegrated absorbs $\sim 124\,\mathrm{MeV}$. The shock **loses approximately $10^{51}\,\mathrm{erg}$ per $0.1\,M_\odot$** of iron traversed. Since the iron core itself is $\sim 1.3$–$2.0\,M_\odot$, the shock can be depleted of $\sim 10^{52}$–$10^{53}\,\mathrm{erg}$ — more than the energy it started with.

2. **Neutrino cooling from behind the shock:** Neutrinos produced by electron captures in the compressed layer immediately behind the shock stream outward, cooling the post-shock region and further sapping the shock energy.

The combined effect is that the **shock stalls within a few milliseconds**, typically at a radius of $\sim 100$–$200\,\mathrm{km}$ from the centre. Without additional energy input, the stalled shock would collapse back and the core would become a black hole without an explosion.

### 4.3 The Delayed Neutrino-Driven Explosion Mechanism

The currently favoured mechanism for reviving the stalled shock is the **delayed neutrino heating mechanism** (Wilson 1985):

**The key physical insight:** At the densities of the newly formed proto-neutron star, neutrinos are **trapped**. The density is so high that even neutrinos — which interact only via the weak force — cannot escape freely. They diffuse outward slowly, like photons in the solar interior. The surface from which neutrinos can finally escape freely is called the **neutrino-sphere**.

**How it works:**
- Below the neutrino-sphere: neutrinos are trapped and carry enormous energy ($\sim 3 \times 10^{53}\,\mathrm{erg}$).
- Just above the neutrino-sphere: the material is dense enough to absorb a small fraction of the outflowing neutrinos via:

$$\bar{\nu}_e + p^+ \leftrightarrow n + e^+$$
$$\nu_e + n \leftrightarrow e^- + p^+$$

- The energy deposited by neutrino absorption in the **gain region** (the shell between the neutrinosphere and the stalled shock) heats the material, increases its pressure, and can re-energise the stalled shock from behind.
- If enough energy is deposited ($\sim 10^{51}\,\mathrm{erg}$), the shock is revived and begins to propagate outward again — the **delayed explosion**, typically occurring $\sim 100$–$500\,\mathrm{ms}$ after core bounce.

This is an elegant mechanism because it uses the enormous neutrino energy reservoir (which cannot drive the prompt explosion because neutrinos escape too freely at that stage) to deliver energy to the shock after the shock has stalled and the density at the shock radius has dropped enough for absorption to be efficient.

### 4.4 The Four Stages of Collapse Visualised

The physics can be followed through four characteristic epochs:

1. **Initial collapse:** Core density $\rho \sim 3 \times 10^{11}\,\mathrm{g\,cm^{-3}}$. Neutrinos ($\nu$) are escaping freely — the core is transparent. This is the stage of rapid electron capture and energy loss.

2. **Neutrino trapping:** Core density $\rho \sim 3 \times 10^{12}\,\mathrm{g\,cm^{-3}}$. The neutrino mean free path drops below the core radius; a neutrino-sphere forms and neutrinos are trapped inside. The core now collapses nearly adiabatically.

3. **Core bounce:** Core density $\rho \sim 10^{14}\,\mathrm{g\,cm^{-3}}$ (nuclear density). The core rebounds, the shock wave forms.

4. **Stalled shock and neutrino revival:** The prompt shock loses energy to photo-disintegration and stalls. Neutrinos from the neutrino-sphere diffuse into the gain region, deposit energy, and (in successful explosions) revive the shock. In unsuccessful cases, the shock recollapse produces a black hole directly.

### 4.5 The Successful Explosion and Its Energy Budget

When neutrino heating revives the shock, it provides the shock with the $\sim 10^{51}\,\mathrm{erg}$ needed to overcome the remaining mass above it and produce the observable supernova explosion. The **delayed explosion mechanism** thus works as follows: the explosion energy does not come directly from the nuclear binding energy of the iron core, but from the gravitational energy of the proto-neutron star transported by neutrinos.

The final kinetic energy of the ejected material is $\sim 10^{51}\,\mathrm{erg}$ (sometimes written as $1\,\mathrm{Bethe} \equiv 10^{51}\,\mathrm{erg}$). This is what is measured observationally from the expansion velocities of supernova ejecta.

---

## 5. Explosive Nucleosynthesis

### 5.1 What the Shock Wave Produces

As the revived shock propagates outward through the onion layers, it heats each shell to extreme temperatures. The shock does not just passively carry previously synthesised nuclei out of the star — it **triggers new nuclear reactions** (explosive nucleosynthesis) in the shells it traverses. Different shells are heated to different peak temperatures, and the duration of the heating is short ($\sim 0.1$–$1\,\mathrm{s}$), so the network of reactions is not in equilibrium and the products reflect the instantaneous reaction rates:

- **Innermost ejecta** ($T > 10^{10}\,\mathrm{K}$, time $\sim 1\,\mathrm{s}$): Site of the **r-process** (rapid neutron capture). The extreme neutron flux from the URCA process and photo-disintegration drives rapid neutron capture, producing heavy neutron-rich nuclei (see Section 5.3). These are the heaviest elements — platinum, gold, uranium, etc.

- **Si/O shell** ($T > 4 \times 10^9\,\mathrm{K}$, time $\sim 0.1\,\mathrm{s}$): Material heated to this temperature undergoes explosive silicon burning and is fully converted to **$^{56}$Ni** and other iron-group elements. This is where essentially all of the supernova's $^{56}$Ni is produced — and since $^{56}$Ni later decays to $^{56}$Fe, this is the source of the iron ejected by core-collapse supernovae.

- **O shell** ($T \sim 3$–$4 \times 10^9\,\mathrm{K}$, time $\sim 1\,\mathrm{s}$): Explosive oxygen burning produces Si, S, Cl, Ar, K, and Ca — the intermediate-mass elements.

A notable benchmark: a single $25\,M_\odot$ supernova ejects approximately **3 solar masses of oxygen** — one of the most important contributions of massive stars to the chemical enrichment of galaxies.

### 5.2 The Fate of Iron From Pre-Explosion Burning

An important point about chemical evolution: the large amount of iron that was produced by silicon burning in the pre-collapse core does **not** contribute to the chemical enrichment of the galaxy via this supernova. It remains **trapped inside the collapsed core** (the proto-neutron star or eventual black hole). The iron observed in Type II SN ejecta and in the ISM is produced by **explosive nucleosynthesis** — the $^{56}$Ni synthesis in the shock — not by the pre-collapse silicon burning. Type II SNe are estimated to produce about **one-third of the iron in the Milky Way** (the other two-thirds coming from Type Ia SNe), as well as essentially all of the oxygen and alpha-elements in the universe.

### 5.3 The r-Process: Rapid Neutron Capture

The **r-process (rapid neutron capture process)** produces approximately half of all elements heavier than iron. It operates when:

1. **Free neutrons are available in large numbers.** The URCA process ($p^+ + e^- \rightarrow n + \nu_e$) and the photo-disintegration of iron nuclei ($^{56}$Fe $+ \gamma \rightarrow 13\,^4$He $+ 4n$) produce a large flux of free neutrons in the innermost ejecta.

2. **Neutron capture is faster than beta decay.** In the r-process, a nucleus captures neutrons so rapidly that it becomes neutron-rich far beyond the valley of nuclear stability, building up isotopes that would ordinarily beta-decay before capturing another neutron. Contrast with the **s-process (slow neutron capture)** that occurs in AGB stars, where captures are slow enough that the nucleus beta-decays before each successive capture — the s-process follows the valley of stability.

The r-process reaction chain:

$${}^A_Z X + n \rightarrow {}^{A+1}_Z X\,(\text{unstable}) \rightarrow {}^{A+1}_{Z+1} X + e^- + \bar{\nu}_e$$

The nucleus captures many neutrons before it beta-decays, producing a series of neutron-rich isotopes at fixed $Z$ until the nucleus becomes so neutron-rich it is beyond the drip line. Then it beta-decays ($Z+1$), and the process continues on the new element. This path runs parallel to but well to the neutron-rich side of the valley of stability on the chart of nuclides, only rejoining the stable isotopes when the neutron flux drops and the nuclei cascade down via beta decays.

An extended chain example:
$${}^{56}\mathrm{Fe} + n \rightarrow {}^{57}\mathrm{Fe} + n \rightarrow {}^{58}\mathrm{Fe} + n \rightarrow {}^{59}\mathrm{Fe} \rightarrow {}^{59}\mathrm{Co}\,(\text{stable})$$

In the r-process, capture continues well past $^{59}$Fe: $^{59}$Fe $+ n \rightarrow {}^{60}$Fe $+ n \rightarrow {}^{61}$Fe $+ \dots$, building deeply neutron-rich species.

The **r-process abundance peaks** (at $A \approx 80$, $130$, $195$) arise from the neutron magic numbers ($N = 50$, $82$, $126$) where neutron capture cross-sections are small and nuclei pile up momentarily before continuing the chain. The presence of r-process elements (Eu, Ba, Pt, Au, U) in the ISM and in metal-poor halo stars is the **chemical signature of core-collapse supernovae** (and, more recently confirmed by gravitational wave observations, neutron star mergers).

Note: the $^{22}$Ne present in the WD and SN ejecta is produced by the combustion of nitrogen during He-burning:
$$^{14}\mathrm{N} + ^4\mathrm{He} \rightarrow ^{18}\mathrm{O} + e^+ + \nu_e$$
$$^{18}\mathrm{O} + ^4\mathrm{He} \rightarrow ^{22}\mathrm{Ne} + \gamma$$

This $^{14}$N was itself the product of the CNO cycle during H-burning, so $^{22}$Ne traces the original metallicity of the progenitor star.

---

## 6. The Onion Structure and Shock Propagation

### 6.1 Propagation Through the Layers

Once the shock is revived, it propagates outward through the onion-shell structure. At each layer boundary, the shock transitions from one composition to another:

- **Fe core boundary:** The shock originates here (from the core rebound). The proto-neutron star (inner $\sim 0.7\,M_\odot$) stays behind. Everything outside this is ejected.
- **Si shell:** Explosive silicon burning converts Si to $^{56}$Ni and iron-group elements.
- **O shell:** Explosive oxygen burning produces intermediate-mass elements.
- **C shell:** Explosive carbon burning may produce some neon and magnesium.
- **He layer:** Little explosive processing — the He is ejected largely unprocessed.
- **H/He envelope:** The outer envelope is pushed off by the shock, with no significant nuclear processing.

**Key point:** Everything external to the proto-neutron star (roughly everything outside $\sim 0.7$–$1.5\,M_\odot$ depending on fallback) is **ejected**. The shock sweeps the matter off the star. For large stars ($M > 30\,M_\odot$), some material — potentially several solar masses — may fall back onto the proto-neutron star after the explosion, potentially converting it into a black hole (fallback black hole). The explosion energy determines whether fallback is significant.

### 6.2 The Ejected Composition

The supernova ejecta contains:
- All pre-explosion nucleosynthesis products from the He layer outward.
- Explosive nucleosynthesis products from the innermost ejecta.
- $^{56}$Ni (which decays to $^{56}$Co then $^{56}$Fe).

Type II SNe eject mainly **H, He, C, O, Si, Ne, Mg, Ca** and only **small quantities of Fe** (the pre-collapse iron stays locked in the neutron star). This is the opposite of Type Ia SNe, which eject predominantly iron-peak elements.

---

## 7. Supernova Light Curves

### 7.1 Shock Breakout and Initial Brightening

The shock, launched at the core, takes hours to days to traverse the stellar envelope, depending on the stellar radius. When it **breaks out** of the stellar surface, there is a brief flash of ultraviolet and X-ray radiation. The surface subsequently **expands and cools rapidly**, with the photospheric temperature dropping from $\sim 200,000\,\mathrm{K}$ at breakout to $\sim 5,000\,\mathrm{K}$ within days to weeks.

During this cooling phase, the hydrogen envelope is ionized by the shock heating, producing a **high electron opacity**. Photons generated by the shock cannot escape — they are trapped in the optically thick ionized envelope. The radiation energy is stored in the expanding ejecta as the envelope recombines.

### 7.2 The Optical Peak: Recombination and Opacity Drop

As the envelope expands and cools, hydrogen recombines from H$^+$ + $e^-$ (high opacity) back to **neutral HI** (nearly zero electron opacity). This recombination begins at the surface and progresses inward as a **recombination front**. When the opacity drops, the trapped radiation stored behind the recombination front is suddenly free to escape — this produces the **optical peak** of the light curve. The peak magnitude of a Type II SN is typically $\sim 300$ million $L_\odot$ (compared to $\sim 6$ billion $L_\odot$ for Type Ia, which lack the hydrogen layer and show a different mechanism).

### 7.3 The Plateau Phase: Constant Recombination Temperature

After the peak, the light curve enters a **plateau** that can last for months. The physical origin of the plateau is the following:

- The recombination front moves inward through the hydrogen envelope (in mass coordinate, it recedes; in radius coordinate, it may expand with the ejecta but always at a rate slower than the outer photosphere).
- Hydrogen recombines at a nearly constant temperature of $\sim 5,000\,\mathrm{K}$ regardless of other conditions (this is set by the ionization energy of hydrogen and the local conditions when the recombination front passes).
- As long as the recombination front is still within the H envelope, the photospheric temperature (and hence luminosity at constant photospheric area) remains roughly constant.
- The result is a **constant luminosity** (the plateau) that persists until the recombination front has passed through the entire H envelope.

**SNII-P (Plateau) vs SNII-L (Linear):** Type IIP supernovae have the classic plateau; Type IIL have a linear (exponential) decline with no plateau. The physical difference is the **size of the hydrogen envelope**: IIL progenitors have lost most of their H envelope to stellar winds or binary mass transfer before explosion, so there is not enough H to sustain a recombination plateau. This connects the SN type to the pre-explosion mass-loss history of the progenitor.

### 7.4 The Radioactive Tail: $^{56}$Co Powered Decay

After the recombination front has passed through the entire hydrogen envelope, the plateau ends and the light curve drops onto a **radioactive tail**. At this point, the dominant energy source is the decay:

$$^{56}\mathrm{Co} \rightarrow ^{56}\mathrm{Fe} + e^+ + \nu_e \quad (\tau_{1/2} = 77.1\,\mathrm{days})$$

The gamma rays and positrons from this decay thermalise in the ejecta and power the optical luminosity. The number of $^{56}$Co nuclei decays as:

$$N(t) = N_0 \, e^{-0.693\, t / \tau_{1/2}}$$

so the luminosity follows:

$$L \propto N(t) = N_0 \, e^{-0.693\, t / \tau_{1/2}}$$

Taking the logarithmic derivative:

$$\frac{d\ln L}{dt} = -\frac{0.693}{\tau_{1/2}}$$

Converting to bolometric magnitudes ($M_\mathrm{bol} = -2.5\log L + \mathrm{const}$):

$$\frac{dM_\mathrm{bol}}{dt} \propto \frac{0.74}{\tau_{1/2}}$$

**The slope of the radioactive tail encodes the half-life of the powering isotope.** This is a powerful diagnostic: by measuring the rate of decline of the light curve, one can directly identify which radioactive species is responsible. The $^{56}$Co tail has a slope corresponding to $\tau_{1/2} = 77.1\,\mathrm{days}$. If other isotopes (e.g. $^{57}$Co, $\tau_{1/2} = 271\,\mathrm{days}$) become dominant at later times, the slope changes, allowing them to be identified.

The **tail is universal** across all core-collapse supernovae because the half-life is a nuclear constant, not dependent on the progenitor's mass or structure. The amplitude (vertical offset) of the tail depends on how much $^{56}$Ni was synthesised in the explosion.

---

## 8. Supernova Classification

### 8.1 The Spectroscopic Classification System

Supernovae are classified **empirically** from their observed spectra at maximum light. The classification tree is:

**Top-level split — hydrogen:**
- **Type II:** H lines present in spectrum (Balmer series in absorption/emission).
- **Type I:** No H lines present.

**Within Type I — silicon:**
- **Type Ia:** Silicon lines present ($\lambda 6355$ Si II absorption feature is the key identifier).
- **No Si:** Silicon absent.

**Within "No Si" — helium:**
- **Type Ib:** Helium lines present (He I absorption features).
- **Type Ic:** No helium lines and no silicon lines — "bare core" supernovae.

This classification is purely observational — it says nothing directly about the explosion mechanism.

### 8.2 Physical Mechanisms Underlying the Classes

Behind the observational classification lie two distinct physical explosion mechanisms:

**Thermonuclear Supernovae (Type Ia):**
- Explosive ignition of a degenerate C-O core, typically in a white dwarf that has accreted matter to near $M_\mathrm{Ch}$ (or via double WD merger).
- No iron core collapse. No neutron star remnant.
- Ejects predominantly iron-peak elements (primarily $^{56}$Ni).
- No hydrogen lines because WD has no hydrogen envelope; silicon lines because of incomplete burning.

**Core-Collapse Supernovae (Type II, Ib, Ic):**
- Fe core collapse in a massive star ($M > 8\,M_\odot$).
- All involve the neutrino-driven delayed explosion mechanism.
- Leave a neutron star or black hole remnant.
- Observational differences among subtypes reflect the **pre-explosion mass-loss history**:
  - **Type II:** Progenitor retains its hydrogen envelope → H lines present.
  - **Type Ib:** Progenitor has lost the H envelope (stripped by wind or binary interaction) but retains the He layer → He lines but no H.
  - **Type Ic:** Progenitor has lost both the H envelope and the He layer → no H or He in the spectrum, just a bare C-O core exploding.

This connection between stripping and spectral type is supported by the fact that Ib/Ic SNe are found preferentially in regions of recent star formation with strong winds, and some Ib/Ic progenitors have been identified as Wolf-Rayet stars (which have lost their envelopes).

### 8.3 Summary of Type II Supernovae

A Type II SN has the following observed and inferred properties:

- **Spectral signature:** Hydrogen Balmer lines (the defining feature).
- **Progenitor:** Massive star, $M > 8\,M_\odot$, most likely a red supergiant.
- **Kinetic energy of ejecta:** $\sim 10^{51}\,\mathrm{erg}$ (the canonical "one Bethe").
- **Neutrino burst energy:** $\sim 3 \times 10^{53}\,\mathrm{erg}$ — 99% of the total energy released goes into neutrinos.
- **Peak optical luminosity:** $\sim 3 \times 10^8\,L_\odot$ (much less than Type Ia at $\sim 6 \times 10^9\,L_\odot$).
- **Chemical yield:** Produces approximately one-third of the iron in the Galaxy, plus essentially **all of the oxygen** and other alpha-elements (Ne, Mg, Si, S, Ca, Ti) in the universe.
- **Remnant:** Neutron star (if $M < 25\,M_\odot$) or black hole (if $M > 25\,M_\odot$, or by fallback).

---

## 9. Remnant: Neutron Star or Black Hole?

### 9.1 The Mass Threshold for Remnant Type

The nature of the compact remnant left by a core-collapse supernova depends primarily on the **initial stellar mass**:

- $M < 25\,M_\odot$: Explosion is successful, leaves a **neutron star (NS)**.
- $M > 25\,M_\odot$: The explosion may fail or the ejecta may fall back, leaving a **black hole (BH)**.

However, these thresholds are approximate and depend strongly on the **density gradient around the iron core**. A shallow density gradient at the boundary between the iron core and the silicon/oxygen shells means that the shock must sweep through more slowly decreasing density — which is harder to explode. Steep density gradients allow the shock to accelerate once it crosses the boundary and are more conducive to successful explosions.

### 9.2 Prompt vs Fallback Black Holes

Black holes can form in two qualitatively different ways:

1. **Prompt formation:** The explosion fails entirely. The proto-neutron star accretes the infalling material without a successful shock revival and collapses directly to a BH. No observable supernova — the star "disappears" (possible examples have been observed as stars that simply vanish).

2. **Fallback formation:** The explosion initially succeeds and ejects material, but some of the ejecta lacks sufficient velocity to escape and falls back onto the proto-neutron star. If enough fallback occurs ($\gtrsim 1\,M_\odot$ typically), the NS exceeds the maximum NS mass ($\sim 2$–$3\,M_\odot$) and collapses to a BH. In large stars ($M > 30\,M_\odot$), fallback of several solar masses is possible.

The distinction matters observationally: a prompt BH produces no supernova (no optical transient from the shock breakout or radioactive tail), while a fallback BH does produce a supernova — but one that may be dim (little $^{56}$Ni) or that shows an unusual light curve as the fallback affects the late-time emission.

### 9.3 Observational Properties of Supernovae: A Summary

- **Type II SN peak luminosity:** $\sim 3 \times 10^8\,L_\odot$ — transient lasts weeks to months.
- **Type Ia SN peak luminosity:** $\sim 6 \times 10^9\,L_\odot$ — significantly brighter, which is why they are used as standard candles (after calibration) for cosmological distance measurements.
- **Exponential radioactive tail:** Governed by the $^{56}$Co half-life of $77.1\,\mathrm{days}$, universal across all core-collapse events.
- **No repetition:** An explosive stellar death is by definition a singular event.
- **After the display ends:** The star leaves behind only a NS or BH, stable essentially forever (on astrophysical timescales).

---
