# Pre-Main Sequence Evolution — Study Notes
**Source:** `20.PreMS_evolution_hifi.md` | **Session:** Pre-Main Sequence Evolution | **Date:** 2026-05-20

---

## 1. Stellar Evolution: Framework and Tools

### 1.1 What Stellar Evolution Studies

Stellar evolution is defined as the analysis of the **macroscopic variation of the characteristics of stars as a function of time**. The word "macroscopic" is important: we are not tracking microscopic nuclear reactions in isolation, but the global, observable properties — luminosity, temperature, radius — as they change over the lifetime of a star. The ideal tool for displaying and interpreting this evolution is the **Hertzsprung-Russell (H-R) Diagram**, a plot of luminosity versus effective temperature. A crucial orientation convention: **the x-axis ($\log T_e$) increases to the left**, so hot stars sit on the left and cool stars on the right. This is the opposite of the natural reading direction and must be kept in mind when interpreting every evolutionary track.

The H-R diagram acts as a phase space for stellar structure: any set of stellar equations, solved for a given mass and composition, maps to a unique point $(L, T_e)$. The diagram therefore encodes the full structural state of a star at any instant.

### 1.2 The Stellar Model Flow Chart

A stellar model takes as input the four fundamental parameters:

$$\text{INPUT: } [M,\, X,\, Y,\, Z]$$

where $M$ is the total stellar mass, $X$ is the hydrogen mass fraction, $Y$ is the helium mass fraction, and $Z$ is the metal (heavy element) mass fraction, with $X + Y + Z = 1$. These are fed into the stellar structure equations, and the output is exactly one point in the H-R diagram:

$$\text{OUTPUT: } [L,\, T_e]$$

This means: **a single stellar model gives a single point in the H-R diagram**. The structure equations (hydrostatic equilibrium, mass continuity, energy generation, radiative/convective transport) form a closed system whose solution uniquely determines the luminosity and effective temperature once mass and composition are fixed.

At each time step, when time is introduced, the code must also check two additional physical questions that are highlighted explicitly in the flow chart:

- **Degeneracy?** — Has the central density and temperature combination entered the regime of electron degeneracy? If so, the equation of state changes qualitatively.
- **Convection?** — Is any region of the star convectively unstable by the Schwarzschild criterion? If so, the energy transport equation must switch from the radiative to the convective form.

### 1.3 Introducing Time: Evolutionary Tracks

When time is introduced, the composition $X, Y, Z$ changes as nuclear reactions burn hydrogen into helium (and later helium into carbon, etc.). The flow chart gains a feedback loop:

$$[M, X, Y, Z] \rightarrow [t = t + \Delta t] \rightarrow [\text{Stellar model equations}] \rightarrow [L, T_e] \rightarrow \text{(feedback)} \rightarrow [t = t + \Delta t]$$

At each time step $\Delta t$, the composition is updated, new structure equations are solved, and a new point $(L, T_e)$ is placed in the H-R diagram. The sequence of all such points, each labelled with a time tag, forms an **evolutionary track**. An evolutionary track therefore represents the complete life history of a star of fixed initial mass $M$ in the H-R diagram — from its formation to the endpoint of its evolution.

Lines of **constant radius** appear as diagonal lines in the H-R diagram (from the Stefan-Boltzmann law $L = 4\pi R^2 \sigma T_e^4$). Along an evolutionary track, moving upper-right implies increasing radius; moving lower-left implies decreasing radius. These constant-$R$ lines are a useful reference for interpreting whether the star is expanding or contracting at any given evolutionary stage.

### 1.4 Evolutionary Tracks vs. Isochrones

Evolutionary tracks for stars of different masses form a family of curves in the H-R diagram. It is critical to distinguish two conceptually different curves:

- **Evolutionary track**: the path of a **single star** (fixed mass) through the H-R diagram over time. Every point on the track corresponds to a different age of that one star.
- **Isochrone**: a curve connecting points of **equal age** across stars of **different masses**. If a stellar population forms at $t=0$, then at time $t = t_0$, each star of a different mass is at a different point on its own evolutionary track. Connecting those points gives the isochrone for age $t_0$.

A concrete example: the isochrone for $t = 700\,\text{Myr} = 0.7\,\text{Gyr}$ is constructed by taking evolutionary tracks for masses from $0.8\,M_\odot$ up to $3.0\,M_\odot$ (and beyond), finding the point on each track with a time tag of 700 Myr, and drawing a smooth curve through all those points. The result is what an observer sees when they plot a star cluster of that age in a colour-magnitude diagram. This is why **isochrones and evolutionary tracks look so different** from each other when both are plotted on the same H-R diagram — one is a time snapshot of many different masses, the other is the complete time history of one mass. In a cluster H-R diagram, the observer always sees an isochrone, not evolutionary tracks.

---

## 2. Timescales of Stellar Evolution

### 2.1 The Three Regimes

The evolution of a star is fundamentally driven by its **core**, which continuously tends toward gravitational contraction. As the core contracts, its density and temperature increase. This process operates on three distinct timescales, which characterise three successive regimes:

1. **Dynamical (free-fall) timescale** $\tau_d$ — set by gravity alone, when gas pressure cannot balance gravity. The cloud collapses freely. This is the fastest timescale.
2. **Thermodynamic (Kelvin-Helmholtz) timescale** $\tau_{KH}$ — set by how long gravitational energy can power the observed luminosity. The structure is virialized; pressure balances gravity but the star slowly contracts and radiates.
3. **Thermonuclear timescale** $\tau_\text{nuc}$ — set by how long the available nuclear fuel lasts at the observed luminosity. This is the longest timescale and defines the main sequence lifetime.

For a $1\,M_\odot$ star these timescales are approximately:

| Timescale | Duration |
|-----------|----------|
| Dynamical | minutes to $10^2$ yr |
| Thermodynamic | $10^7$ yr |
| Thermonuclear | $10^{10}$ yr |

The transitions between regimes are triggered by physical thresholds: **gas pressure balancing gravity** ends the dynamical phase; **fusion reactions balancing gravity** ends the thermodynamic phase. The path of increasing timescale as the star forms can be summarised as:

$$\text{Gas cloud} \rightarrow \text{Proto-star} \rightarrow \text{Star}$$

### 2.2 Dynamical Timescale and Free-Fall

When a gas cloud exceeds the Jeans mass and gravity is unresisted by pressure, the cloud equation of hydrostatic equilibrium includes a radial acceleration term:

$$\frac{\partial P}{\partial r} + \frac{Gm\rho}{r^2} = \rho\,\alpha$$

where $\alpha$ is the radial acceleration. During free fall, the pressure gradient $\partial P/\partial r$ is negligible compared to the gravitational term, so the cloud falls as a set of mass shells accelerated by gravity. From the kinematics of gravitational acceleration $r = \frac{1}{2}g t^2$ with $g = GM/r^2$, one derives the dynamical (free-fall) timescale:

$$T_d = \sqrt{\frac{2r^3}{GM}}$$

Here $r$ is the radius of the structure (cm), $M$ is the enclosed mass (g), and $G = 6.67\times10^{-8}\,\text{dyne\,cm}^2\,\text{g}^{-2}$. The surface gravity $g = GM/R^2$ (often quoted logarithmically as $\log g$) is a **highly sensitive diagnostic** of structural changes during stellar evolution: it varies dramatically between a puffed-up giant and a compact main-sequence star of the same mass.

For gas clouds, where we know the density better than we know $r$ and $M$ separately, the dynamical timescale expressed in terms of mean density $\bar{\rho} = 3M/(4\pi r^3)$ is more useful:

$$T_d = \sqrt{\frac{2}{\,G\,}\cdot\frac{3}{4\pi\bar{\rho}}} = \frac{2600}{\sqrt{\bar{\rho}}}\,\text{s}$$

where $\bar{\rho}$ must be in $\text{g\,cm}^{-3}$. This shows immediately that denser structures collapse faster.

**Numerical examples:**

*The Sun* (a fully formed, dense object):
$$T_d = \sqrt{\frac{2\,(7\times10^{10})^3}{6.7\times10^{-8}\cdot 2\times10^{33}}} \approx 2.3\times10^3\,\text{s} \approx 38\,\text{min}$$
If pressure support were instantaneously removed, the Sun would collapse in ~38 minutes.

*A typical interstellar gas cloud* with $\bar{\rho} = 10^{-23}\,\text{g\,cm}^{-3}$:
$$T_d = \frac{2600}{\sqrt{10^{-23}}}\,\text{s} = 2.6\times10^3 \times 3.3\times10^{11}\,\text{s} \approx 10^{15}\,\text{s} \approx 10^7\,\text{yr}$$
Even the "fast" dynamical timescale is $10^7$ years for a diffuse ISM cloud, because the density is so low.

### 2.3 Transition from Dynamical to Thermodynamic

During free-fall collapse, three simultaneous effects convert kinetic energy into heat: (1) density increases through compression, (2) temperature rises adiabatically, and (3) the gas ionises, dramatically raising the opacity. The combined effect is a **substantial increase in gas pressure**. In the denser central regions, this pressure increase becomes sufficient to decelerate and halt the collapse. When gravity is balanced by pressure, the structure enters the virialized regime:

$$\text{Collapse} \rightarrow \text{Temperature increase} \rightarrow \text{Pressure increase} \rightarrow \text{Gravity balanced}$$

From this point, contraction slows from the dynamical to the thermodynamic timescale.

### 2.4 Thermodynamic Timescale and the Virial Theorem

In the virialized (quasi-static) regime, the **Virial Theorem** holds:

$$2K + \Omega = 0$$

where $K > 0$ is the total thermal kinetic energy of the gas and $\Omega < 0$ is the gravitational potential energy. This deceptively simple relation has a profound consequence: when the structure contracts slightly ($\Omega$ becomes more negative, $d\Omega < 0$), the kinetic energy must increase:

$$dK = -\frac{d\Omega}{2} > 0$$

The total energy of the system is:

$$U = K + \Omega$$

Substituting $K = -\Omega/2$ from the Virial Theorem:

$$U = -\frac{\Omega}{2} + \Omega = \frac{\Omega}{2} < 0$$

When the structure contracts ($d\Omega < 0$):
$$dK = +\frac{|d\Omega|}{2} \quad\text{(internal temperature increases)}$$
$$dU = +\frac{d\Omega}{2} < 0 \quad\text{(total energy decreases = energy is radiated away)}$$

**In plain language**: of the gravitational energy released by contraction, exactly **half heats the gas** and **half is radiated as luminosity**. The gas simultaneously emits energy and heats up. This is the **negative heat capacity** of a self-gravitating system — losing energy makes it hotter. This appears counterintuitive but is a rigorous consequence of the Virial Theorem and governs pre-MS evolution, the post-MS giant phase, and all other phases where gravity controls the contraction.

### 2.5 Kelvin-Helmholtz Timescale

The luminosity of a virialized contracting proto-star is powered by gravitational potential energy release:

$$L = \left|\frac{dU}{dt}\right| = \frac{1}{2}\left|\frac{d\Omega}{dt}\right|$$

Integrating over the contraction lifetime $t$:

$$L \cdot t = \frac{1}{2}|\Omega| \approx \frac{1}{2}\frac{GM^2}{R}$$

Solving for $t$:

$$t_{KH} = \frac{1}{2}\frac{GM^2}{LR}$$

This is the **Kelvin-Helmholtz timescale**: the time a star of mass $M$, luminosity $L$, and radius $R$ can shine by gravitational contraction alone. Physical constants: $G = 6.67\times10^{-8}\,\text{dyne\,cm}^2\,\text{g}^{-2}$; $M$ in grams; $L$ in erg/s; $R$ in cm.

**For the Sun:**
$$t_{KH,\odot} = \frac{1}{2}\frac{6.6\times10^{-8}\cdot4\times10^{66}}{4\times10^{33}\cdot7\times10^{10}} = \frac{10^{15}}{2} \approx 5\times10^{14}\,\text{s} \approx 1.5\times10^7\,\text{yr}$$

**Crucial historical implication:** Gravitational energy can power the Sun's present luminosity for only ~15 million years. Since geological and fossil evidence shows the Earth is ~4.5 billion years old, the Sun's energy source **cannot** be gravitational contraction alone. This contradiction — identified by Kelvin and Helmholtz in the 19th century — was only resolved with the discovery of nuclear fusion as the actual energy source. The Kelvin-Helmholtz timescale is therefore the time an unborn star spends descending to the main sequence, not the main-sequence lifetime itself.

### 2.6 Thermonuclear Timescale

As the core temperature rises during Kelvin-Helmholtz contraction, it eventually reaches the threshold for **thermonuclear fusion**. For hydrogen burning, this is $T_c \sim 10^7\,\text{K}$. Once fusion ignites, the energy it supplies balances the radiative losses, halting further contraction. The structure enters the **thermonuclear timescale** regime — for a $1\,M_\odot$ star, $\sim10^{10}$ yr.

Physically, thermonuclear reactions reduce the number of particles in the core: four protons fuse into one helium-4 nucleus plus two positrons and two neutrinos — a net reduction in particle count by a factor of roughly 4. Fewer particles at the same temperature means lower pressure ($P = n k T$, fewer $n$), which slightly favours contraction. But this process is extremely slow — the particle number decreases on the thermonuclear timescale, so the star adjusts quasi-statically and appears stable. The thermonuclear regime is therefore a **long break in the core's tendency to contract**.

### 2.7 The Staircase of Core Evolution and Electron Degeneracy

After each fuel reservoir is exhausted, the core contracts again on the Kelvin-Helmholtz timescale, heating until the next fuel ignites. The **core temperature as a function of time** forms a characteristic staircase pattern:

- **Slanted segments** (labelled $\tau_G$): gravitational Kelvin-Helmholtz contraction phases, during which $T_c$ rises steeply.
- **Flat plateaus**: stable nuclear burning phases, during which $T_c$ stays roughly constant.

The successive burning phases in order of increasing temperature are: $H\rightarrow He$, $He\rightarrow C,O$, $C\rightarrow Mg$, $O\rightarrow S$, and ultimately the $Fe$ core (for massive stars only).

This staircase describes cores that remain **perfect gases** throughout. However, after helium burning, the core conditions may drive the electrons into **degeneracy**. The $\log T$ vs $\log\rho$ diagnostic diagram shows the key boundary:

- **Perfect gas** regime ($P \propto \rho T$): holds when thermal pressure dominates.
- **Degenerate gas** regime: non-relativistic degeneracy gives $P\propto\rho^{5/3}$; relativistic gives $P\propto\rho^{4/3}$. Degenerate pressure is much stronger than thermal pressure at the same density, and is nearly independent of temperature.

After helium burning, each subsequent gravitational contraction phase must be evaluated: does the trajectory in $(\log\rho_c, \log T_c)$ space cross into the degenerate regime? For stars with $M < 8\,M_\odot$: yes — the CO core becomes degenerate. The staircase is permanently cut off after the $He\rightarrow C,O$ plateau. No further carbon ignition occurs. These stars end as **white dwarfs** (degenerate CO structures). For $M > 8\,M_\odot$: the core is hot and massive enough to avoid degeneracy and proceeds through all subsequent burnings to an iron core.

The onset of electron degeneracy is thus the most important **branching point** in stellar evolution, separating stars that become white dwarfs from those that explode as core-collapse supernovae.

---

## 3. Cloud Contraction and the Jeans Criterion

### 3.1 Stars from Gas Clouds — Physical Setup

Stars form from the gravitational collapse of interstellar gas clouds (Jeans 1902). For a cloud to collapse, gravity must overcome thermal pressure. Consider a particle of mass $H$ (the mass of an atomic or molecular hydrogen particle; for $H_2$: $H_2 = 2\times1.6\times10^{-24}\,\text{g}$) at the periphery of a cloud of mass $M$ and radius $R$. Its gravitational binding energy is $GMH/R$ and its thermal kinetic energy is $kT$ (from the equipartition theorem; the numerical factor $3/2$ is absorbed into the inequality). The **collapse condition** is:

$$\frac{GMH}{R} \geq kT$$

Gravity wins when the gravitational binding energy per particle exceeds the thermal energy per particle. If thermal energy dominates, the cloud disperses. The cloud is depicted physically as a region with inward gravitational forces (black arrows toward the centre) and outward gas pressure forces (blue arrows outward), with the collapse condition specifying when the inward forces win.

### 3.2 Derivation of the Jeans Mass

To express the collapse condition in terms of the cloud's **density** $\rho$ and **temperature** $T$ — the two observable macroscopic parameters of an ISM environment — we eliminate $R$ using:

$$M = \frac{4}{3}\pi R^3\rho \quad\Longrightarrow\quad R = \left(\frac{3}{4\pi}\right)^{1/3}\frac{M^{1/3}}{\rho^{1/3}}$$

Substituting into the collapse condition:

$$\frac{GH \cdot M \cdot \rho^{1/3}}{\left(\frac{4\pi}{3}\right)^{1/3}M^{1/3}} \geq kT$$

$$M^{2/3} \geq \underbrace{\frac{k}{\left(\frac{4\pi}{3}\right)^{1/3}GH}}_{\equiv\,a}\cdot\frac{T}{\rho^{1/3}}$$

The constant $a$ involves only fundamental physical constants and the hydrogen mass. Numerically:
- $H_2 = 2\times1.6\times10^{-24}\,\text{g}$
- $G = 6.67\times10^{-8}\,\text{dyne\,cm}^2\,\text{g}^{-2}$
- $k = 1.4\times10^{-16}\,\text{erg/K}$

gives $a \approx 10^{15}\,\text{g\,K}^{-1}\,\text{cm}^{-1}$. Raising both sides to the $3/2$ power:

$$M \geq a^{3/2}\cdot\frac{T^{3/2}}{\rho^{1/2}}$$

$$\boxed{M_J \geq 10^{23}\cdot T^{3/2}\cdot\rho^{-1/2}\,\text{g}}$$

with $T$ in Kelvin and $\rho$ in g/cm$^3$. This is the **Jeans mass criterion**: clouds with mass exceeding $M_J$ at their $(T,\rho)$ will collapse; those below $M_J$ will not. The derivation is elegant because it directly produces the condition in terms of the two most accessible observational parameters of an ISM region.

### 3.3 Physical Meaning and the ISM Phase Diagram

The scaling $M_J \propto T^{3/2}\rho^{-1/2}$ encodes the key physics:

- **Higher temperature** $T$: larger $M_J$ required. Hotter gas has more thermal energy per particle, so a more massive cloud is needed to overcome thermal pressure with gravity.
- **Higher density** $\rho$: smaller $M_J$ required. Denser gas brings more mass within a smaller radius, strengthening the gravitational binding energy relative to thermal energy.

In a $\log n$ vs $\log T$ phase diagram (where $n$ is particle number density, related to $\rho$ by the mean particle mass), lines of constant $M_J$ are diagonal boundaries sloping upward to the right. The **contraction region** lies above and to the left of each $M_J$ line. Different ISM phases populate different regions:

- **Dense molecular clouds**: cold ($T\sim 10$–$50$ K) and dense ($n\sim 10^3$–$10^6\,\text{cm}^{-3}$) — fall in the upper-left, requiring small $M_J \sim 1$–$10\,M_\odot$. **These are the ideal star-forming environments.**
- **Diffuse clouds**: somewhat warmer and less dense — require $M_J\sim 10$–$100\,M_\odot$.
- **HII regions**: hot and ionized — require very large $M_J$.
- **Hot intercloud medium and supernova remnants**: extremely hot and tenuous — $M_J$ is enormous, no collapse occurs.

The figure makes immediately clear why star formation is concentrated in dense, cold molecular clouds: only there is $M_J$ small enough to be consistent with forming individual stars rather than requiring enormous cluster-scale masses to collapse.

### 3.4 Numerical Example: Typical Cold ISM

With $\bar{\rho} = 1\times10^{-23}\,\text{g/cm}^3$ and $T \approx 10\,\text{K}$:

$$M_J \geq 10^{23}\times(10)^{3/2}\times(10^{-23})^{-1/2} = 10^{23}\times31.6\times3.16\times10^{11} \approx 10^{35}\,\text{g} \approx 100\,M_\odot$$

This result is key: the Jeans mass for typical cold ISM conditions is $\sim 100\,M_\odot$. Individual solar-mass stars ($M_\odot = 2\times10^{33}\,\text{g}$) are 50 times less massive than this. This means:

1. A single Jeans-mass clump collapses as a whole and must **fragment** during the collapse to form smaller objects. The fragmentation process during collapse is what determines the IMF.
2. The natural product of star formation is not a single star but a **stellar aggregate** — a cluster or OB association. Isolated field stars are, in this picture, escapees from such groups.

### 3.5 Collapse Triggers

The Jeans criterion identifies **which** clouds can collapse, but not **what triggers** the collapse. The ISM can sit in a marginally stable state for a long time. Identified physical triggers include:

- **Shock fronts** from supernova explosions: the expanding blast wave compresses surrounding ISM gas, locally raising the density above the Jeans threshold. This explains the spatial correlation of young star clusters with supernova remnants and the triggering of star formation in sequential waves.
- **Cloud-cloud collisions**: two gas clouds moving through the ISM at random velocities can collide and locally compress the gas to above the Jeans threshold.
- **Gas compression in spiral arms**: a spiral arm is a gravitational potential well in the galaxy's disk. As gas orbits the galaxy and passes through a spiral arm, it is compressed. This concentrates star formation along spiral arm patterns, explaining the visual appearance of star-forming regions in spiral galaxies.
- **Galaxy interactions**: tidal forces during galaxy mergers or close encounters drive massive gas inflows and compressions, triggering enormous bursts of star formation (starbursts).

### 3.6 The Initial Mass Function

The fragmentation of a collapsing cloud determines the **mass spectrum** of the resulting stars — the **Initial Mass Function (IMF)**, $\Psi(M)$. The IMF describes the number of stars formed per unit mass interval (per unit volume). Observationally, for $M\gtrsim 1\,M_\odot$ it follows a power law (**Salpeter 1955**):

$$\Psi(M) = k\,M^{-s}, \quad s_\text{Salpeter} = 2.35$$

In a $\log\Psi$ vs $\log(M/M_\odot)$ plot, this is a straight line with slope $-2.35$. A shallower slope ($s=1.5$) would mean more high-mass stars; a steeper slope ($s=3.5$) would mean even more low-mass stars. The Salpeter value $s=2.35$ is a well-measured observational result for the solar neighbourhood and is often assumed to be universal (though this universality is still debated).

The IMF is of central importance in astrophysics for three reasons:
1. **Final fate**: a star's endpoint (white dwarf, neutron star, black hole) is determined entirely by its initial mass. The IMF therefore sets the ratio of compact object types in any population.
2. **Chemical enrichment**: the rate and timescale of metal enrichment of the ISM depend on mass — more massive stars evolve faster and return processed material sooner. The IMF weights these contributions.
3. **Core-collapse supernovae**: stars with $M\gtrsim 10\,M_\odot$ end as core-collapse supernovae (CC-SNe). Their rate per stellar population is set directly by the IMF above $\log(M/M_\odot)\sim1$. Key open questions: Is the IMF universal across cosmic time? Does it depend on cloud metallicity or physical conditions?

---

## 4. The Three Stages of Stellar Evolution

### 4.1 Overview

The entire life history of a star is divided into three broad stages, each defined by the state of nuclear burning in the core:

1. **Pre-Main Sequence (pre-MS) evolution**: from gas cloud to the Zero Age Main Sequence (ZAMS). The proto-star contracts gravitationally, heating its core until hydrogen fusion ignites. Ends when hydrogen burning in the core begins.
2. **Main Sequence (MS) evolution**: the star burns hydrogen in its core. This is the longest stage — for the Sun, $\sim10^{10}$ yr. Ends when hydrogen in the core is exhausted.
3. **Post-Main Sequence (post-MS) evolution**: from hydrogen exhaustion onward. The core contracts, shell burning begins, and the star expands into a giant. Ends at the stellar graveyard (white dwarf, neutron star, or black hole).

The focus of these notes is entirely on **pre-MS evolution**.

---

## 5. Pre-Main Sequence Evolution: From Cloud to ZAMS

### 5.1 Starting Conditions — Point A

The proto-star at the start of its evolution is labelled **point A** in the H-R diagram. It is essentially a large, cool, diffuse gas cloud characterised by three properties:

- **Large radius** $R$: the cloud has not yet substantially contracted. For a $1\,M_\odot$ cloud, $R\sim10^4\,R_\odot = 7\times10^{14}\,\text{cm}$.
- **Low luminosity**: despite its large size, the cloud is not very luminous because $T_e$ is very low and the surface is optically thick in ways that suppress radiation.
- **Low effective temperature** $T_e$: at this stage, $T_e$ is only a few thousand K.

In the H-R diagram, point A is located in the upper-right region — high luminosity (because radius is huge, even though surface temperature is low), very cool. The exact position depends on the mass.

### 5.2 Segment A–B: Initial Free-Fall Collapse

Segment A–B represents the **initial gravitational collapse**. At the start, the cloud is not in hydrostatic equilibrium: gravity dominates over pressure and the cloud falls essentially freely, obeying:

$$\frac{\partial P}{\partial r} + \frac{GM_r\rho}{r^2} = -\rho\frac{\partial^2 r}{\partial t^2}$$

where $-\rho\partial^2 r/\partial t^2$ is the radial acceleration term. The collapse proceeds on the **free-fall timescale**:

$$\tau_{FF} \sim 2\sqrt{\frac{R^3}{GM}} \sim \frac{4\times10^3}{\sqrt{\rho}}\,\text{s}$$

A critical detail: the **central regions are denser** and therefore collapse more rapidly than the outer envelope. The core reaches hydrostatic equilibrium first, while the outer layers continue to fall freely. This differential collapse is key — the inner core becomes a stable nucleus while the envelope is still in free fall.

**Free-fall calculation for a $1\,M_\odot$ solar-like cloud:**

The cloud has $R\approx10^4\,R_\odot = 7\times10^{14}\,\text{cm}$ and $M = 2\times10^{33}\,\text{g}$. The mean density:

$$\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{2\times10^{33}}{4\,(7\times10^{14})^3} = \frac{10^{33}}{6\times10^{44}} \approx 10^{-12}\,\text{g/cm}^3$$

$$\tau_{FF} \approx \frac{4\times10^3}{\sqrt{10^{-12}}}\,\text{s} = \frac{4\times10^3}{10^{-6}}\,\text{s} = 4\times10^9\,\text{s} \approx 10^2\,\text{yr}$$

For $1\,M_\odot$, segment A–B takes **~100 years** — an extremely short time astronomically. In the H-R diagram, this appears as a nearly **vertical drop** at roughly constant (low) effective temperature, falling steeply in luminosity.

### 5.3 Segment B–C: Shock Wave and Luminosity Spike

With the inner core in hydrostatic equilibrium and the outer envelope still in free fall, the in-falling outer material eventually **collides with the core**. This collision generates an **outward-propagating shock wave** that sweeps through the surrounding gas. Two important effects follow:

1. The shock wave **disperses gas** around the forming stellar structure, removing material from the immediate vicinity.
2. The shock dramatically **reduces the opacity** $\kappa$ of the gas surrounding the core.

The luminosity escaping a stellar interior is governed by:

$$\left.\frac{dT}{dr}\right|_\text{rad} = -\frac{3\kappa\rho}{4\pi r^2}\frac{L(r)}{4acT^3}$$

When $\kappa$ drops sharply, radiation can escape much more freely. The result is a **sudden, large increase in luminosity** — segment B–C is a rapid spike upward in the H-R diagram to a local maximum at point C. The proto-star's effective temperature remains low (it is still a large, cool object), so the luminosity spike is nearly vertical in the H-R diagram.

For a $1\,M_\odot$ star, the B–C transition is extremely rapid: $\sim\mathbf{10}$ **days**. This is so brief that it would be essentially invisible observationally.

### 5.4 Segment C–E: Progressive Hydrostatic Equilibrium Throughout

After the luminosity peak at C, the shock wave has passed and the proto-star must establish **hydrostatic equilibrium progressively outward** through all envelope layers. The outermost layers, still moving after the shock, decelerate and achieve equilibrium one by one, from the inside out. At **point E**, the **entire proto-star** — from centre to surface — is in hydrostatic equilibrium.

During C–E, the luminosity decreases from its peak (as the opacity increases back toward equilibrium values) and the proto-star settles onto a more stable thermal structure. The C–E segment takes $\sim10^5$ yr for $1\,M_\odot$.

**At point E, the proto-star has:**
- $L \sim 10^3\,L_\odot$ (very luminous)
- $R \sim 10^2\,R_\odot$ (very large)
- $T_e \sim 2500\,\text{K}$ (very cool)

The star is a large, puffed-up, very cool but luminous object. Its position at $T_e \sim 2500\,\text{K}$ places it at the extreme right of the H-R diagram.

### 5.5 Point E and the Hayashi Track

**Point E has special significance**: it is the first moment in the proto-star's history when the structure is **entirely in hydrostatic equilibrium**. This makes it the entry point onto the Hayashi Track — a physically fundamental locus in the H-R diagram described in the next section.

---

## 6. The Hayashi Track

### 6.1 Definition

**Hayashi tracks** are defined as follows: for a fixed chemical composition, the Hayashi tracks form a family of nearly-vertical lines in the H-R diagram — one line per mass — representing stellar models that are simultaneously (a) in **hydrostatic equilibrium** and (b) **completely convective** throughout. In other words, the Hayashi track for a given mass is the locus of all fully convective, hydrostatically equilibrated models of that mass as the luminosity (and hence radius) decreases during Kelvin-Helmholtz contraction.

In the H-R diagram, Hayashi tracks appear as nearly vertical lines on the cool (right) side of the diagram. Different masses have slightly different positions (higher-mass tracks are slightly hotter, i.e., slightly to the left), but all are nearly vertical.

### 6.2 Physical Origin: Kramers Opacity and the Schwarzschild Criterion

The reason Hayashi tracks exist in the low-temperature regime is tied to the **Kramers opacity law**:

$$\kappa = \kappa(\rho,T) \propto \frac{\rho}{T^{3.5}}$$

At low temperatures (the right side of the H-R diagram), $\kappa$ is very large — the gas is highly opaque. High opacity drives a steep radiative temperature gradient:

$$\left.\frac{dT}{dr}\right|_\text{rad} = -\frac{3\kappa\rho}{4\pi r^2}\frac{L(r)}{4acT^3}$$

A large $\kappa$ makes $|dT/dr|_\text{rad}$ very steep. Convective instability is triggered when the **Schwarzschild criterion** is satisfied:

$$\nabla_\text{rad} > \nabla_\text{ad} \quad\text{where}\quad \nabla = \frac{d\log T}{d\log P}$$

When $\nabla_\text{rad}$ (the actual radiative gradient) exceeds $\nabla_\text{ad}$ (the adiabatic gradient, which depends only on the equation of state), the layer is convectively unstable. At the low temperatures of the Hayashi regime, high Kramers opacity forces $\nabla_\text{rad}\gg\nabla_\text{ad}$ throughout the entire star, making the **entire structure convective**. This is the defining characteristic of a Hayashi-track model.

As the star contracts and heats (moving down the Hayashi track), the opacity at fixed density scales as $\kappa\propto T^{-3.5}$, so higher temperature means lower opacity. Eventually, in the central regions, $\nabla_\text{rad}$ drops below $\nabla_\text{ad}$ and the core becomes radiative. At that point, the model leaves the Hayashi track and moves leftward.

### 6.3 The Hayashi Theorem: Forbidden Region

The **Hayashi Theorem** states: at fixed chemical composition and mass, there is a **forbidden region** in the H-R diagram to the **right** of the Hayashi track. No stable stellar model in hydrostatic equilibrium can exist there.

The physical reason: temperatures to the right of the Hayashi track would be even lower, driving $\kappa$ even higher, which would drive $\nabla_\text{rad}$ to even larger values. But a fully convective structure in hydrostatic equilibrium cannot be shifted arbitrarily to cooler temperatures while maintaining physical self-consistency — there is a minimum temperature for a given luminosity and mass. Below that temperature, no stable configuration exists. The Hayashi track is the **cool temperature boundary** of the allowed region for hydrostatic stellar models.

The allowed region of the H-R diagram (for a given mass, fixed composition):
- **Forbidden (right of Hayashi track)**: no stable models exist.
- **On the Hayashi track**: stable, fully convective models.
- **Left of the Hayashi track** ("OK region"): stable, partially convective (partly radiative core) models.

**Critical note**: The Hayashi Theorem is **universal** — it applies at all stages of stellar evolution, not just pre-MS. In post-MS evolution, when a star cools into the red giant branch, it is again constrained by its Hayashi track. The forbidden zone always lies to its right. The concept defined in the pre-MS context applies without modification to giants, supergiants, and any other hydrostatically balanced structure.

### 6.4 The Three Possible States for a Given Mass

Consider three models at the same luminosity but different temperatures for a $2\,M_\odot$ star (or any given mass):

- **Model A** (to the **left** of the Hayashi track): **stable and partially convective**. The inner core has sufficiently high temperature that $\kappa$ is lower, $\nabla_\text{rad}<\nabla_\text{ad}$ in the core, so the core is radiative. Only the outer envelope is convective. Physically consistent.
- **Model B** (exactly **on** the Hayashi track): **stable and fully convective**. $\nabla_\text{rad}>\nabla_\text{ad}$ everywhere. The boundary case.
- **Model C** (to the **right** of the Hayashi track): **unstable**. No stable hydrostatic equilibrium is possible. A star in this position cannot exist in a steady state.

### 6.5 Composition Dependence of Hayashi Tracks

The exact shape and position of a Hayashi track depend on both mass and chemical composition. Computed tracks for different metallicities ($Z = 10^{-4}$, $0.004$, $0.02$) and helium fractions ($Y = 0.245$, $0.345$, $0.425$) show small but systematic horizontal offsets. Higher metallicity shifts the track slightly to lower temperatures (slightly further right) because metal-rich gas has higher opacity, sustaining convection at slightly higher temperatures. These shifts are calculated from the full stellar structure equations in the adiabatic approximation (Salaris & Cassisi, pp. 110–114).

Along the Hayashi track, the proto-star is a convective structure with a **progressively decreasing radius** — it is contracting. From $L = 4\pi R^2\sigma T_e^4$, a decreasing $R$ at nearly constant $T_e$ means decreasing $L$, which is why the Hayashi track runs nearly vertically downward (decreasing luminosity) at nearly constant effective temperature.

---

## 7. Evolution Along the Hayashi Track

### 7.1 Energy Source Along the Hayashi Track

Once the proto-star is at point E (fully convective, hydrostatic equilibrium, on the Hayashi track), it evolves **downward along its Hayashi track** — luminosity decreasing, effective temperature roughly constant. The energy source at this stage is **gravitational contraction** on the Kelvin-Helmholtz timescale — not nuclear burning, since the core is not yet hot enough. For $1\,M_\odot$, descent along the Hayashi track from point E takes from $\sim10^5$ yr to $\sim10^6$ yr.

The Virial Theorem operates continuously: half of the released gravitational energy heats the interior (raising $T_c$ and $\rho_c$) and half is radiated as luminosity $L$. The decreasing luminosity along the track reflects the fact that as the radius decreases, the total gravitational energy per unit time being released also decreases (the star is more tightly bound but contracting more slowly).

### 7.2 Internal Energy Processes: Molecular Dissociation

As the core heats, a significant fraction of the released gravitational energy is consumed by **dissociation of molecular hydrogen** ($H_2 \rightarrow 2H$) and subsequently by **ionisation of atomic hydrogen** ($H \rightarrow H^+ + e^-$) and helium ($He \rightarrow He^+ + e^-$, $He^+ \rightarrow He^{2+} + e^-$). These are endothermic processes — they absorb energy. They therefore temporarily reduce the rate at which the gas temperature rises (the effective adiabatic index $\gamma$ drops below $5/3$ during these transitions), which allows contraction to proceed without a corresponding rapid temperature increase. This is an important energy sink during the early Hayashi-track descent.

### 7.3 Development of a Radiative Core — Departure from the Hayashi Track

As the proto-star contracts along the Hayashi track, the central temperature rises continuously. From the Kramers law, $\kappa\propto T^{-3.5}$: higher temperature means **lower opacity in the core**. Lower $\kappa$ directly reduces the radiative gradient:

$$\nabla_\text{rad} \propto \frac{3\kappa\rho L_r}{4\pi r^2 T^3\cdot4ac}$$

When $T$ rises enough in the core that $\kappa$ decreases sufficiently to make $\nabla_\text{rad}<\nabla_\text{ad}$ in the central region, the Schwarzschild criterion is no longer satisfied there and the **core becomes radiative**. The star is no longer completely convective — it has left the Hayashi track and entered the "OK" region.

In the H-R diagram, the **evolutionary track bends sharply to the left** (toward higher $T_e$) at this point. The convective envelope progressively retreats outward as the radiative core grows. The internal structure diagram — showing mass fraction $M_r/M$ on the y-axis versus $\log t$ — reveals this clearly: a wedge of radiative material (blank space) grows from the centre outward, while the convective region (cloud pattern) shrinks to an ever-thinner outer shell, until only the outer envelope remains convective.

### 7.4 The Internal Structure Timeline

The complete internal structure evolution from cloud to ZAMS:
- **A through E** (free-fall through shock, entering Hayashi track): the **entire star is fully convective** from centre to surface throughout.
- **On the Hayashi track** (descent from E): still **fully convective** throughout. This is confirmed by the complete filling of the mass fraction diagram with convective pattern at these times.
- **Departing the Hayashi track**: a **radiative core** begins at the centre and grows progressively outward. The convective zone retreats.
- **Approaching the ZAMS**: the radiative zone occupies most of the stellar interior. Only the outermost envelope remains convective (for a $1\,M_\odot$ star, this becomes the solar convective envelope, constituting the outer $\sim28\%$ by radius of the Sun).
- **At the ZAMS**: structure stabilised. For $M\lesssim0.3\,M_\odot$, the entire star remains convective; for $M\gtrsim1.5\,M_\odot$, a convective core (driven by the steep temperature dependence of CNO burning) develops at the centre, while the envelope is radiative.

---

## 8. Pre-MS Tracks for Different Masses

### 8.1 The Departure Point and Its Mass Dependence

The point at which a pre-MS evolutionary track bends leftward away from the Hayashi track — the **moment of first radiative core development** — depends critically on stellar mass. Three characteristic departure points are defined from computed pre-MS tracks:

- **Point 1** (for $M > 5\,M_\odot$): departure occurs **early and high** on the Hayashi track. Massive proto-stars have much higher Kelvin-Helmholtz luminosities ($L_{KH}\propto M^2/R$), so they radiate gravitational energy away rapidly and contract fast. Their cores heat quickly, developing radiative cores at high luminosity. These stars barely touch the Hayashi track before heading leftward.
- **Point 2** (for $1.25 < M < 3\,M_\odot$): departure at intermediate luminosities. The proto-star descends partway down the Hayashi track before the core heats enough for $\nabla_\text{rad}<\nabla_\text{ad}$.
- **Point 3** (for $\sim1\,M_\odot$): departure at **low luminosities**, deep in the descent along the Hayashi track. Low-mass proto-stars have lower luminosities and heat their cores more slowly, so they descend much further along the Hayashi track before developing a radiative core.

The physical driver is the **"heating velocity" of the core** — the speed at which contraction raises $T_c$. More massive stars contract faster (shorter $\tau_{KH}$), raise $T_c$ more rapidly, and depart the Hayashi track sooner and higher up.

### 8.2 Point 2 in Detail: First Partial Nuclear Ignition

**Point 2** (relevant for $1.25 < M < 3\,M_\odot$) marks both the departure from the Hayashi track (last moment of complete convection) and, simultaneously, the onset of a few thermonuclear reactions in the core. The core temperature is now high enough to activate **partial sequences** of the pp chain and CNO cycle — but not the complete chains.

The activated reactions are:

From the pp chain (second step):
$$^2\text{H} + ^1\text{H} \rightarrow ^3\text{He} + \gamma$$

From the CNO cycle (first three steps):
$$^{12}\text{C} + ^1\text{H} \rightarrow ^{13}\text{N} + \gamma$$
$$^{13}\text{N} \rightarrow ^{13}\text{C} + e^+ + \nu$$
$$^{13}\text{C} + ^1\text{H} \rightarrow ^{14}\text{N} + \gamma$$

These reactions are not yet self-sustaining as a complete cycle — the final reclosure steps have not been activated because the required temperatures are not yet reached. Nevertheless, they **contribute additional energy** ($\varepsilon\nearrow$, $L_\varepsilon\nearrow$), supplementing the gravitational luminosity. The proto-star's energy output now comes from both gravitational contraction and partial nuclear burning.

The physical reason for the coincidence of radiative core development and partial nuclear ignition is that both are driven by rising $T_c$: higher $T_c$ reduces $\kappa$ (triggering the radiative core) and simultaneously activates thermonuclear reactions (as the Coulomb barrier becomes easier to penetrate). They are concurrent effects of the same underlying contraction-driven heating.

### 8.3 Point 5: Nuclear Energy Dominates

**Point 5** is defined as the moment when thermonuclear energy production has increased to the point where it begins to **dominate over gravitational contraction** as the primary energy source. This represents the proto-star's transition from a gravitationally powered to a nuclearly powered object.

The increased nuclear energy injection causes the **core to slightly expand** — a perfect gas thermostat response (Section 9.3 discusses this in detail). This expansion reduces both $\rho_c$ and $T_c$ slightly:

$$L\searrow,\quad T_C\searrow\text{ (temporarily)}$$

The contribution of gravitational energy to total luminosity, $L_g/L$, begins its dramatic fall toward zero. In the $\log\rho_c$ vs $\log t$ and $\log T_c$ vs $\log t$ diagrams, the previously steeply rising curves of $\rho_c$ and $T_c$ flatten and stabilise as the nuclear energy takes over from gravitational contraction.

---

## 9. Approach to the Zero-Age Main Sequence

### 9.1 Progressive Rise of $\rho_c$ and $T_c$

The entire pre-MS evolutionary path (from point A onward) is characterised by a **continuous increase** of the central density $\rho_c$ and central temperature $T_c$. This monotonic rise is the direct consequence of the Virial Theorem: half of every joule of gravitational energy released by contraction goes into heating the interior. Plots of $\log\rho_c$ and $\log T_c$ versus $\log t$ show steeply rising curves throughout the pre-MS phase, from the initial cloud conditions to conditions approaching hydrogen ignition.

As partial nuclear reactions activate (around point 2 and beyond), these curves begin to flatten — the gravitational luminosity fraction $L_g/L$ drops steeply from $\approx1$ toward 0. The energy balance is progressively taken over by nuclear reactions.

### 9.2 Final Activation of $^3\text{He}+^3\text{He}$

The last critical reaction that must activate to complete the pp chain and establish self-sustaining hydrogen burning is:

$$^3\text{He} + ^3\text{He} \rightarrow ^4\text{He} + 2p$$

This reaction requires a higher core temperature than the preceding pp chain steps because it involves two $Z=2$ nuclei and therefore faces a larger Coulomb barrier ($V_C \propto Z_1Z_2/r$, with $Z=2$ for $^3\text{He}$). The $^3\text{He}$ abundance builds up in the core until this temperature is finally reached.

The **ZAMS is reached exactly when the $^3\text{He}+^3\text{He}$ reaction is fully activated.** Before this, the pp chain is not closed and hydrogen is not being stably burned into helium-4 in a self-sustaining way. After this reaction ignites, the complete pp chain operates: $4p \rightarrow ^4\text{He} + 2e^+ + 2\nu + \text{energy}$, providing the sustained energy output needed to power the stellar luminosity indefinitely on the thermonuclear timescale.

### 9.3 The Perfect-Gas Thermostat: Core Expansion at the ZAMS

When the $^3\text{He}+^3\text{He}$ reaction turns on, it provides an additional energy source on top of the existing partial reactions. The **core responds as a perfect gas thermostat**: the extra energy input causes a **slight core expansion**. This expansion:
- Decreases $\rho_c$ (the density drops as the core expands into a larger volume)
- Decreases $T_c$ (the temperature drops as the gas expands and does work against gravity)

In the $\log\rho_c$ vs $\log t$ diagram, this manifests as a small but identifiable **dip** in $\rho_c$ just at the transition to the ZAMS. Similarly, $T_c$ shows a small dip. The gravitational luminosity fraction $L_g/L$ even goes **briefly negative** during this episode — the core is absorbing energy (expanding) rather than releasing it. After this transient, the star stabilises at the ZAMS with $L_g/L = 0$.

This thermostat effect is the same mechanism that makes main-sequence stars stable: if nuclear energy generation increases (e.g., due to a small perturbation), the core expands and cools, reducing the reaction rate and restoring equilibrium. If it decreases, the core contracts and heats, increasing the rate. This negative feedback loop is the physical basis of stellar stability on the main sequence.

### 9.4 Summary of the Gravitational Luminosity Fraction

The ratio $L_g/L$ evolves as follows through the pre-MS:
- **A through E and along the Hayashi track**: $L_g/L \approx 1$ — almost entirely gravitationally powered.
- **Points 2 through 5**: $L_g/L$ falls from $\approx1$ as partial nuclear reactions contribute increasingly.
- **Just before ZAMS**: $L_g/L$ dips briefly below zero (core expansion absorbs energy).
- **At the ZAMS**: $L_g/L = 0$ — entirely nuclear-powered. Contraction has ceased.

---

## 10. Pre-MS Timescales

### 10.1 Overall Duration and Mass Dependence

The pre-MS phase lasts $10^4$ to $10^7$ yr — a small fraction of any star's total main-sequence lifetime. There is a strong inverse correlation with mass: more massive stars complete pre-MS evolution faster. Computed values (from standard pre-MS tables, e.g., Carroll & Ostlie Table 12.3):

| Mass ($M_\odot$) | Pre-MS duration |
|---------|---------|
| 0.5 | $\sim10^8$ yr |
| 1.0 | $\sim10^7$ yr |
| 5.0 | $\sim10^5$ yr |
| 15.0 | $\sim10^4$ yr |

This inverse mass–timescale trend for pre-MS evolution mirrors the main-sequence trend (more massive stars burn hydrogen faster) and arises from the same physics: more massive stars are far more luminous, so they radiate energy away (gravitational or nuclear) much faster.

### 10.2 Approximate Scaling Formula

An approximate relation for the pre-MS timescale as a function of mass, luminosity, and radius:

$$t_\text{PMS} \sim 4\times10^7\left(\frac{M}{M_\odot}\right)^2\frac{R_\odot}{R}\frac{L_\odot}{L}\,\text{yr}$$

Breaking down the dependencies: the $M^2$ factor alone would suggest longer pre-MS for massive stars (they have more gravitational energy to radiate). But this is **counteracted** by the $L^{-1}$ and $R^{-1}$ factors: more massive proto-stars are both **much more luminous** and **larger**, which drastically shortens the time needed to radiate the gravitational energy.

**Verification for the Sun** ($M=M_\odot$, $R=R_\odot$, $L=L_\odot$):
$$t_\text{PMS,\odot} = 4\times10^7\,\text{yr} \approx 10^7\,\text{yr}$$
Consistent with the Kelvin-Helmholtz time computed directly.

**For a $10\,M_\odot$ proto-star** (where from the HR diagram: $L\sim10^4\,L_\odot$ and $R\sim10\,R_\odot$):
$$t_\text{PMS} = 4\times10^7\times(10)^2\times\frac{1}{10}\times\frac{1}{10^4}\,\text{yr} = 4\times10^7\times100\times0.1\times10^{-4}\,\text{yr} = 4\times10^4\,\text{yr}$$

This is 1000 times shorter than the solar pre-MS timescale, primarily because $L\sim10^4\,L_\odot$ — the $10\,M_\odot$ proto-star radiates gravitational energy away at an enormous rate.

**Important implication**: In a young star-forming region, massive stars ($M\gtrsim10\,M_\odot$) have already reached the main sequence and are burning hydrogen by the time solar-mass stars are still on the Hayashi track. This differential evolution has observational consequences: young clusters show a mix of main-sequence massive stars and pre-MS low-mass stars simultaneously.

---

## 11. The Zero-Age Main Sequence (ZAMS)

### 11.1 Definition and Physical Meaning

The **Zero Age Main Sequence (ZAMS)** is defined as the locus in the H-R diagram connecting the positions of stars of different masses at the precise moment they first achieve **self-sustaining hydrogen burning** in their cores ($^3\text{He}+^3\text{He}$ fully activated, $L_g/L = 0$). At the ZAMS:

- The star is in **thermal equilibrium**: $L_\text{nuc} = L_\text{surface}$.
- The star is in **hydrostatic equilibrium** at every point.
- **No net contraction** occurs: the gravitational energy contribution is zero.
- The star is in the **thermonuclear timescale** regime for the first time.

In the H-R diagram, the ZAMS appears as a well-defined diagonal band: lower-left (low-mass stars: cool, faint) to upper-right (high-mass stars: hot, luminous). Each point on the ZAMS is the terminus of one pre-MS evolutionary track. A diagram showing all the pre-MS tracks ends on a collective line — the ZAMS — connecting these endpoints for all masses.

### 11.2 The ZAMS as a Uniqueness Theorem

For a fixed chemical composition ($X, Y, Z$), each mass $M$ maps to a unique point $(L, T_e)$ on the ZAMS. This is a consequence of the uniqueness of stellar structure models: given $M$, $X$, $Y$, $Z$, and the constraint that the model is in full nuclear-thermal equilibrium (ZAMS conditions), the structure equations have exactly one solution. The ZAMS is therefore a **one-parameter family of models** parameterised by mass alone (at fixed composition). This is why the ZAMS is such a clean, tight sequence.

The slope of the ZAMS reflects the mass-luminosity and mass-temperature relations for hydrogen-burning stars. Moving along the ZAMS to higher masses, $L$ increases very steeply ($L\propto M^{3-4}$ approximately), while $T_e$ increases more moderately. This steep $L$-$M$ relation directly determines the main-sequence lifetime ($\tau_\text{MS}\propto M/L\propto M^{-2}$ to $M^{-3}$) — the most massive stars burn out fastest.

### 11.3 The ZAMS as the Starting Point for All Main-Sequence Evolution

The ZAMS is simultaneously the **end of pre-MS evolution** and the **beginning of main-sequence evolution**. For a stellar population that forms at $t=0$ with the same initial composition, all stars start from the ZAMS at $t=0$. The most massive stars evolve away from the ZAMS first (shortest $\tau_\text{MS}$). As time passes, the **main-sequence turnoff point** — the luminosity at which stars are just leaving the main sequence — moves progressively downward along the ZAMS to lower and lower masses. The turnoff luminosity is a direct clock for the age of the population, and this is the primary method of dating star clusters.

---

## 12. Summary: The Complete Pre-MS Evolutionary Path

### 12.1 Sequence of Events

The full pre-MS journey of a $1\,M_\odot$ star, from gas cloud to ZAMS, can be summarised in a single coherent narrative:

| Segment | Physical Process | Timescale | H-R Motion |
|---------|-----------------|-----------|------------|
| A | Initial state: large, cool, low-$L$ cloud | — | Upper right |
| A–B | Free-fall collapse; central core reaches hydrostatic equilibrium first | $\sim10^2$ yr | Steep vertical drop |
| B–C | Shock wave disperses envelope, opacity drops, luminosity spikes | $\sim10$ days | Nearly vertical rise to peak |
| C–E | Progressive hydrostatic equilibrium established throughout envelope | $\sim10^5$ yr | Drop to Hayashi track |
| E | Entire proto-star in HE; fully convective; on Hayashi track | — | Right side of HR |
| E $\to$ departure | Descent along Hayashi track; KH contraction; gravitationally powered | $\sim10^5$–$10^6$ yr | Downward along Hayashi track |
| Departure | Radiative core forms; track bends leftward | — | Leftward hook |
| Partial ignition | Partial pp and CNO reactions ignite; $L_g/L$ falls | — | Leftward toward ZAMS |
| ZAMS | $^3\text{He}+^3\text{He}$ fully active; $L_g/L=0$ | — | Main sequence |

### 12.2 Three Governing Physical Principles

Three overarching physical principles govern every stage of the pre-MS:

1. **The Virial Theorem and negative heat capacity**: every phase of gravitational contraction in a self-gravitating gas heats the interior while radiating half the released energy. This drives the inexorable core temperature rise that eventually ignites hydrogen fusion.

2. **The Hayashi constraint**: the forbidden region to the right of the Hayashi track is physically inaccessible to any hydrostatically equilibrated stellar model. The pre-MS proto-star must therefore first descend vertically along the Hayashi track (while fully convective) and only then move leftward (as the radiative core grows). This constraint applies at all evolutionary stages, not just pre-MS.

3. **The perfect-gas thermostat**: a perfect-gas core responds to increased energy generation by expanding and cooling, and to decreased energy generation by contracting and heating. This negative feedback loop stabilises nuclear burning once the ZAMS is reached and maintains stellar stability throughout the main sequence.

### 12.3 Mass Dependence Summary

The mass of a proto-star determines virtually every aspect of its pre-MS evolution:

- **Departure from the Hayashi track**: earlier (higher luminosity, shorter time) for higher mass (points 1, 2, 3 for high, intermediate, low masses respectively).
- **Pre-MS duration**: shorter for higher mass, because $t_\text{PMS}\propto M^2 L^{-1} R^{-1}$ and both $L$ and $R$ increase steeply with mass.
- **ZAMS position**: hotter and more luminous for higher mass.
- **Internal structure at ZAMS**: fully convective for $M\lesssim0.3\,M_\odot$; convective envelope + radiative interior for $\sim0.3$–$1.5\,M_\odot$; convective core + radiative envelope for $M\gtrsim1.5\,M_\odot$ (driven by the steep temperature dependence $\varepsilon_{CNO}\propto T^{15}$ of CNO burning concentrating energy production at the centre).
- **Post-pre-MS fate**: ultimately determined by mass — stars with $M<8\,M_\odot$ end as white dwarfs; stars with $M>8\,M_\odot$ end as core-collapse supernovae.
