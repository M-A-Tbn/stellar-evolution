# Introduction — Study Notes

**Source:** `10.introduction_hifi.md` | **Session:** Introduction | **Date:** 2026-05-20

---

## 1. Course Overview and Goals

### 1.1 The Aim of Stellar Evolution

The central goal of this course is to **identify the physical processes that produce the major changes in the structure of stars of different masses and chemical composition as a function of time**. This is not merely descriptive — the course demands a mechanistic understanding of why stars evolve the way they do.

Stellar evolution matters beyond individual stars because all large-scale cosmic structures — globular clusters, spiral galaxies like Andromeda, and interacting galaxy groups like Stephan's Quintet — are built from stars and gas. The **photometric properties** (how bright objects are, in which colors) and the **chemical evolution** of every cosmic structure depend directly on what the stars inside them are doing. To understand galaxy evolution, galaxy colors, or interstellar chemical enrichment, one must first understand how a single star evolves.

### 1.2 Course Syllabus

The course is organized into the following lecture blocks:

- **10. Intro:** Basic background on stellar structure (this set of notes)
- **20. Pre-Main Sequence evolution**
- **21. Main Sequence evolution**
- **22. Post-Main Sequence evolution**
- **23. The HB and AGB evolutionary sequences**
- **24. Pulsating Stars**
- **25. White Dwarfs**
- **26. Final Stages of High-mass Stars**
- **27. Binary Systems**
- **28. Supernovae and Neutron Stars**
- **29. Black Holes and Gravitational Waves**

### 1.3 Recommended Textbooks

Four key references are recommended:

1. Schwarzschild, *Structure and Evolution of the Stars*, Dover Publication — one of the classic foundational texts.
2. Carroll & Ostlie, *An Introduction to Modern Astrophysics*, Addison-Wesley — the primary course textbook; specific chapters are referenced throughout.
3. Bowers & Deeming, *Astrophysics I: Stars*.
4. Salaris & Cassisi, *Evolution of Stars and Stellar Populations*, Wiley — a more specialized modern treatment.

### 1.4 Exam Expectations

The oral exam is described as a "relaxed chat" about course topics but demands genuine conceptual clarity. Five specific competencies are expected:

1. **Astrophysical language precision:** Use "contraction" only when the collapse occurs over a thermal (Kelvin–Helmholtz) timescale; use "collapse" only when the contraction occurs over a dynamical timescale. The timescale context is part of the meaning.
2. **Comprehensive nuclear reaction knowledge:** Know all thermonuclear reactions and their respective ignition temperatures.
3. **Final stages by mass:** Know the endpoint of stars with different initial masses.
4. **Degeneracy's role:** Understand how electron degeneracy alters stellar behavior at each stage of evolution.
5. **Transition masses:** Know the critical masses that separate qualitatively different evolutionary paths, and the physical mechanism that sets each one.

Additionally, the student must be able to:
- Draw and discuss evolutionary tracks for stars of different masses in the H-R diagram, highlighting the differences and explaining why they differ.
- Read internal structure diagrams (Kippenhahn diagrams) of stars.
- Identify and describe each physical mechanism driving major stellar evolutionary events and its impact on stellar populations.

---

## 2. The Hertzsprung-Russell Diagram

### 2.1 Definition and Orientation

The **Hertzsprung-Russell (H-R) Diagram** is the fundamental tool of stellar evolution. It is a two-dimensional plot that relates a star's **luminosity** (on the vertical axis) to its **surface (effective) temperature** (on the horizontal axis).

Key axis conventions:

- The vertical axis is $\log(L/L_\odot)$, where $L_\odot$ is the solar luminosity.
- The horizontal axis is $\log T_e$ (the effective temperature). Crucially, **the temperature axis increases toward the left** — so hot stars are on the left side of the diagram and cool stars are on the right. This is the opposite of most graphs and must be memorized.

High surface temperatures (hot, blue stars) are on the left; low surface temperatures (cool, red stars) are on the right. Lines of constant radius run diagonally across the diagram (from upper left to lower right).

### 2.2 Why the H-R Diagram Is the Ideal Tool

A stellar model — given the inputs of mass $M$ and chemical composition $(X, Y, Z)$ — produces the outputs of luminosity $L$ and surface temperature $T_e$. These two numbers define **exactly one point** on the H-R diagram. A single stellar model is thus one point.

When time is introduced, the chemical composition of a star changes (as nuclear reactions convert hydrogen into helium, for example). At each time step $t \to t + \Delta t$, the stellar model equations are solved again with the new composition, yielding a new $(L, T_e)$ pair and a new point on the H-R diagram. The sequence of points traced out over time is called an **evolutionary track**. The H-R diagram therefore translates the abstract equations of stellar structure into a visually readable history of the star.

The variety of evolutionary tracks for stars of different masses — simple main-sequence lines for low-mass stars versus complex loops and zig-zags for high-mass stars — is one of the central mysteries the course explains.

---

## 3. Inputs to a Stellar Model

### 3.1 The Two Required Inputs

A stellar model requires only two inputs:

1. **Total mass** $M$
2. **Chemical composition** $(X, Y, Z)$

### 3.2 Chemical Composition Variables

The chemical composition is specified by three mass fractions that must satisfy $X + Y + Z = 1$:

- **$X$**: mass fraction of **hydrogen**
- **$Y$**: mass fraction of **helium**
- **$Z$**: mass fraction of **metals** — all elements heavier than helium (carbon, nitrogen, oxygen, iron, etc.)

For the **Sun**, the present-day values are approximately:
- $X = 0.70$ (70% hydrogen)
- $Y = 0.28$ (28% helium)
- $Z = 0.02$ (2% metals)

These values are not universal; stars of different ages or formed from chemically enriched gas have different compositions, and evolution itself changes $X$ and $Y$ inside the star (as hydrogen is converted to helium in the core).

---

## 4. The Seven Equations of Stellar Structure

### 4.1 Overview

A stellar model is built from a **system of seven coupled differential equations** (plus one algebraic equation of state) that together describe the physical conditions at every radius inside the star. The independent variable is the radial distance from the center, $r$. The solution of this system yields the luminosity $L$ and surface temperature $T_e$ — placing the star on the H-R diagram.

The seven equations are:
1. Hydrostatic equilibrium
2. Mass continuity
3. Equation of state (gas + radiation pressure)
4. Energy source (luminosity gradient)
5. Radiative temperature gradient and Schwarzschild criterion
6. Opacity
7. Energy production by thermonuclear reactions

Each is derived and discussed in detail below.

---

## 5. Equation 1 — Hydrostatic Equilibrium

### 5.1 Physical Picture

A star is a **sphere of gas in hydrostatic equilibrium**: the inward pull of gravity is exactly balanced at every layer by the outward push of gas pressure. This balance is what makes a star a stable, long-lived structure rather than either collapsing or exploding.

The internal structure of a star consists of a series of concentric spherical shells. As one moves outward from the center, both the **density** $\rho$ and the **temperature** $T$ decrease. For the Sun, the central temperature is $\sim 15{,}000{,}000$ K and the surface temperature is $\sim 6{,}000$ K; the central density is $\sim 1.5 \times 10^2$ g/cm$^3$ and decreases to $\sim 2 \times 10^{-7}$ g/cm$^3$ in the outer layers.

### 5.2 Derivation

Consider a small volume element (a thin shell of cross-sectional area $dS$ and radial thickness $dr$) at distance $r$ from the center. Two forces act on it:

**Pressure force:** The net pressure force on the element is the difference between the pressure pushing inward from above and the pressure pushing outward from below:

$$F_\text{pres} = P(r+dr)\,dS - P(r)\,dS$$

Expanding $P(r+dr)$ in a Taylor series:

$$P(r+dr) = P(r) + \frac{dP(r)}{dr}\,dr$$

Substituting:

$$F_\text{pres} = \frac{dP(r)}{dr}\,dr\,dS$$

Note that $dP/dr$ is negative (pressure decreases outward), so this force acts inward when $P$ is larger at smaller $r$ — but in the equilibrium equation it is the net pressure gradient force.

**Gravitational force:** The gravitational acceleration at radius $r$ depends on the mass $M(r)$ enclosed within radius $r$ (by the shell theorem). The force on the mass element $dm = \rho(r)\,dr\,dS$ is:

$$F_\text{grav} = \frac{GM(r)}{r^2}\,\rho(r)\,dr\,dS \quad \text{(directed inward, toward the center)}$$

**Equilibrium condition:** For the element to be in static equilibrium, the net force is zero:

$$F_\text{pres} + F_\text{grav} = 0$$

$$\frac{dP(r)}{dr}\,dr\,dS - \frac{GM(r)}{r^2}\,\rho(r)\,dr\,dS = 0$$

Dividing through by $dr\,dS$:

$$\boxed{\frac{dP(r)}{dr} = -\frac{GM(r)}{r^2}\,\rho(r)}$$

The negative sign is essential: pressure must **decrease outward** (i.e., $dP/dr < 0$) to balance the inward gravitational force.

### 5.3 Physical Meaning

This equation states that at every depth $r$ inside the star, the local pressure gradient exactly supports the weight of all the material above. The deeper one goes (larger $\rho$, larger $M(r)$), the steeper the pressure gradient must be. This equation connects the pressure profile to the density profile and the enclosed mass profile — it constrains how all three must be mutually consistent.

---

## 6. Equation 2 — Mass Continuity

### 6.1 Derivation

The mass contained in a thin spherical shell of radius $r$ and thickness $dr$ is:

$$dM(r) = 4\pi r^2\,\rho(r)\,dr$$

(This is simply the volume of the shell, $4\pi r^2\,dr$, multiplied by its density $\rho(r)$.)

Dividing both sides by $dr$:

$$\boxed{\frac{dM(r)}{dr} = 4\pi r^2\,\rho(r)}$$

This is the **mass continuity equation** (also called the equation of conservation of mass).

### 6.2 Physical Meaning

This equation connects the mass distribution $M(r)$ to the density profile $\rho(r)$. It says that the rate at which the enclosed mass increases with radius equals the density at that radius multiplied by the surface area of the sphere. Together with the hydrostatic equilibrium equation, it forms the backbone of the stellar structure problem: given $\rho(r)$, one can compute both $P(r)$ and $M(r)$.

As a consistency check: if the density were uniform ($\rho = \bar{\rho}$), integrating from $0$ to $r$ gives $M(r) = \frac{4}{3}\pi r^3 \bar{\rho}$, the familiar formula for the mass of a uniform sphere.

---

## 7. Equation 3 — Equation of State

### 7.1 Overview

The equation of state connects pressure $P$ to the local thermodynamic conditions (temperature $T$, density $\rho$, and chemical composition). The total pressure inside a star has two components:

$$P = P_\text{rad} + P_\text{gas}$$

### 7.2 Radiation Pressure

$$P_\text{rad} = \frac{a\,T^4}{3}$$

where $a = 7.6 \times 10^{-15}$ erg cm$^{-3}$ K$^{-4}$ is the radiation constant, related to the Stefan–Boltzmann constant $\sigma = 5.6 \times 10^{-5}$ erg s$^{-1}$ cm$^{-2}$ K$^{-4}$ by $a = 4\sigma/c$.

In the **stellar interior**, radiation pressure is negligible compared to gas pressure for most stars and most evolutionary stages. However, it becomes important in the most massive stars, which can approach the Eddington limit.

### 7.3 Perfect Gas Pressure

For a perfect (ideal) gas:

$$P_\text{gas} = \frac{k\,\rho\,T}{\mu\,H}$$

where:
- $k = 1.4 \times 10^{-16}$ erg K$^{-1}$ is the Boltzmann constant,
- $\rho$ is the mass density (g cm$^{-3}$),
- $T$ is the temperature (K),
- $H$ is the mass of a proton ($\approx 1.67 \times 10^{-24}$ g),
- $\mu$ is the **mean molecular weight** — the average mass of a gas particle in units of the proton mass.

The product $\mu H$ is therefore the average mass of a particle in the gas.

### 7.4 Mean Molecular Weight

The mean molecular weight $\mu$ depends on the chemical composition because fully ionized gases contribute many more particles per unit mass than un-ionized ones. For a fully ionized gas composed of hydrogen (mass fraction $X$), helium (mass fraction $Y$), and metals (mass fraction $Z$):

$$\boxed{\mu = \frac{1}{2X + \frac{3}{4}Y + \frac{1}{2}Z}}$$

**Derivation of the formula:** Fully ionized hydrogen contributes 2 particles per proton mass (1 proton + 1 electron); fully ionized helium contributes 3 particles per 4 proton masses (1 alpha particle + 2 electrons), i.e., 3/4 particles per proton mass; metals are approximated as contributing roughly 1/2 particle per proton mass. The reciprocal of the total particle number density per unit mass gives $\mu$.

For the Sun ($X=0.70$, $Y=0.28$, $Z=0.02$), this yields $\mu \approx 0.617$.

### 7.5 The Thermoregulation Property of a Perfect Gas

The perfect gas equation has a crucial physical property: it is **self-regulating (thermoregulated)**. The feedback loop works as follows:

> Temperature increases → pressure increases → gas expands → temperature decreases

This negative feedback loop is what makes a normal star stable. Any perturbation that heats the gas triggers an expansion that cools it back down. This is the "breathing action" of normal gas.

This property is essential for stable thermonuclear burning: it ensures that reactions cannot run away. However, as discussed below, degenerate gas breaks this feedback, with drastic consequences.

### 7.6 Electron Degeneracy — When Gas Deviates from Perfect Behavior

Electrons deviate from the perfect gas behavior when **all the low-energy quantum states (below the Fermi level $\epsilon_F$) are completely occupied**. This occurs when the Pauli exclusion principle prevents electrons from occupying lower energy states — they are said to be **degenerate**.

At absolute zero (T = 0), the Fermi-Dirac distribution is a perfect step function: all states below $\epsilon_F$ are fully occupied and all states above are empty. At finite temperature $T > 0$, the distribution softens near $\epsilon_F$, but if $kT \ll \epsilon_F$, the gas is still effectively degenerate.

**Condition for electron degeneracy:**

$$\frac{T}{\rho^{2/3}} < 10^5 \quad \text{(electron degeneracy)}$$

A useful mnemonic: the solar core (definitely a perfect gas) has $T = 10^7$ K and $\rho = 10^2$ g/cm$^3$, giving:

$$\frac{T}{\rho^{2/3}} = \frac{10^7}{(10^2)^{2/3}} = \frac{10^7}{10^{4/3}} = 10^{7-4/3} = 10^{17/3} \approx 10^{5.67} \gg 10^5$$

So the solar core is a perfect gas, and the inequality sign must go the other way for degeneracy.

The general form of the condition, valid for any particle species, is:

$$\frac{T}{\rho^{2/3}} < \frac{2.4 \times 10^{-22}}{m}$$

where $m$ is the particle mass. This immediately shows that **lighter particles degenerate more easily**:
- Electrons ($m_e \sim 10^{-27}$ g): degenerate when $T/\rho^{2/3} < 2.4 \times 10^5$.
- Protons ($m_p \sim 10^{-24}$ g): degenerate when $T/\rho^{2/3} < 240$.

At any stellar interior condition where electrons are degenerate, protons are still a perfect gas because the proton degeneracy boundary ($\log T = \frac{2}{3}\log\rho + 2.38$) lies far into the relativistic electron degeneracy region. Therefore, **in this course "degenerate gas" always means electron-degenerate gas**.

### 7.7 The Log T – Log ρ Phase Diagram

The $\log T$–$\log\rho$ diagram partitions stellar interior conditions into regimes with different dominant pressure contributions. The temperature axis ranges from $\log T = 6$ to $9$ and the density axis from $\log\rho = 0$ to $8$ — these are the conditions found in stellar cores.

| Region | Condition | Pressure law |
|--------|-----------|-------------|
| Top-left (high $T$, low $\rho$) | radiation-dominated | $P \propto T^4$ |
| Central white region | perfect gas | $P \propto \rho T$ |
| Right (high $\rho$, moderate $T$) | non-relativistic electron degeneracy | $P \propto \rho^{5/3}$ |
| Far right (very high $\rho$) | relativistic electron degeneracy | $P \propto \rho^{4/3}$ |

The boundary between perfect gas and non-relativistic electron degeneracy is the diagonal line $\log T = \frac{2}{3}\log\rho + 5$ (equivalently, $T/\rho^{2/3} = 10^5$). The electron degeneracy boundary for electrons is a red line on this diagram; the corresponding proton degeneracy boundary ($\log T = \frac{2}{3}\log\rho + 2.38$) falls inside the relativistic electron degenerate region, confirming that proton degeneracy is never reached in practice.

### 7.8 Consequences of Electron Degeneracy

When electrons are degenerate, the pressure formula for the electron component changes from perfect gas to:

| Gas type | Pressure formula | Depends on |
|----------|-----------------|------------|
| Perfect gas (electrons) | $P = \frac{k\rho T}{\mu_e H}$ | $\rho$ and $T$ |
| Degenerate non-relativistic | $P = k_1\,\rho^{5/3}$ | $\rho$ only |
| Degenerate relativistic | $P = k_2\,\rho^{4/3}$ | $\rho$ only |

Two critical consequences follow:

**Consequence 1 — Loss of thermoregulation:**

The degenerate electron pressure is **independent of temperature**. This destroys the negative feedback loop:

> Normal gas: $T\nearrow \Rightarrow P\nearrow \Rightarrow$ expansion $\Rightarrow T\searrow$ (stable)
>
> Degenerate gas: $T\nearrow \Rightarrow$ no change in $P \Rightarrow$ no expansion $\Rightarrow T\nearrow$ (unstable)

This is catastrophic when a thermonuclear reaction ignites in a degenerate environment: the reaction releases heat, the temperature rises, the reaction rate increases (since $\epsilon \propto T^\nu$ with large $\nu$), but no expansion occurs to cool the gas. The result is a **thermonuclear runaway** — an explosive, uncontrolled ignition. The most important example in stellar evolution is the **helium flash** at the tip of the red giant branch.

**Consequence 2 — Incompressibility:**

A degenerate gas is much less compressible than a perfect gas at the same density. The pressure depends only on density (not temperature), so once the gas is compressed to a given density, it resists further compression very strongly. This is the physical basis for **white dwarf stability**.

### 7.9 Full Equation of State

The complete equation of state, valid in all regimes, is:

$$P = \underbrace{\frac{aT^4}{3}}_{\text{radiation}} + \underbrace{\frac{k\rho T}{\mu_i H}}_{\text{ions (always perfect gas)}} + \underbrace{\begin{cases} \frac{k\rho T}{\mu_e H} & \text{perfect gas electrons} \\ k_1\rho^{5/3} & \text{degenerate non-relativistic} \\ k_2\rho^{4/3} & \text{degenerate relativistic} \end{cases}}_{\text{electrons}}$$

Note that the **ionic** component (protons and alpha particles) always behaves as a perfect gas under stellar conditions; it is only the **electron** component that can degenerate. In the degenerate regime, the electron pressure term dominates over the ionic term. The selection of which electron pressure formula applies is governed by $T/\rho^{2/3}$ relative to $10^5$.

---

## 8. Equation 4 — Energy Source

### 8.1 Luminosity Gradient

Consider a thin spherical shell at radius $r$ with thickness $dr$. Define $L(r)$ as the luminosity (energy per unit time) flowing outward through the sphere of radius $r$. The additional luminosity added by the shell is:

$$dL(r) = L(r+dr) - L(r) = \underbrace{4\pi r^2\,\rho(r)\,dr}_{\text{mass of shell}} \times \underbrace{\epsilon}_{\text{energy per unit mass per unit time}}$$

where $\epsilon$ (erg g$^{-1}$ s$^{-1}$) is the energy generation rate per unit mass.

In differential form:

$$\boxed{\frac{dL(r)}{dr} = 4\pi r^2\,\rho(r)\,\epsilon}$$

This is the **energy conservation equation**: the increase in luminosity per unit radius equals the energy generated per unit time in that shell.

### 8.2 Sources of Energy: Thermonuclear Reactions and Gravitational Contraction

The primary energy source $\epsilon$ comes from thermonuclear reactions. However, gravitational contraction also contributes energy, as explained via the Virial Theorem. This distinction is important: different energy sources are relevant on different timescales and at different evolutionary stages.

### 8.3 The Virial Theorem and Gravitational Energy

A star in hydrostatic equilibrium satisfies the **Virial Theorem**:

$$2K + \Omega = 0$$

where $K$ is the total kinetic (thermal) energy and $\Omega$ is the gravitational potential energy (which is negative, $\Omega < 0$). Therefore:

$$K = -\frac{\Omega}{2} > 0$$

The total internal energy is:

$$U = K + \Omega = -\frac{\Omega}{2} + \Omega = \frac{\Omega}{2} < 0$$

Since $\Omega < 0$, $U < 0$ as well.

**Key insight:** When a star contracts ($d\Omega < 0$, meaning $\Omega$ becomes more negative):
- Half the released gravitational energy goes into heating the gas: $K$ increases, so temperature rises.
- The other half is radiated away: $U$ becomes more negative, supporting the observed luminosity.

This can be summarized as: **any loss of total energy (emission of radiation) causes the star to contract, which simultaneously heats up the interior**. Stars become hotter as they lose energy — the opposite of everyday experience with cooling objects. This is known as the **negative heat capacity** of gravitational systems.

### 8.4 The Kelvin–Helmholtz Timescale

Gravitational contraction can support the stellar luminosity for a finite time. The luminosity supplied by contraction is:

$$L = \frac{dU}{dt} = \frac{1}{2}\left|\frac{d\Omega}{dt}\right|$$

The total gravitational energy of a star of mass $M$ and radius $R$ is $|\Omega| \approx \frac{GM^2}{R}$. The timescale over which gravitational contraction can power the star is:

$$\boxed{t_{KH} = \frac{1}{2}\frac{GM^2}{LR}}$$

This is the **Kelvin–Helmholtz timescale** (also called the thermodynamic contraction time).

For the Sun:
$$t_{KH} = \frac{1}{2}\frac{6.6\times10^{-8} \times (2\times10^{33})^2}{4\times10^{33} \times 7\times10^{10}} = \frac{1.4 \times 10^{52}}{2.8 \times 10^{44}} \approx 5 \times 10^{14} \text{ s} \approx 1.5 \times 10^7 \text{ yr}$$

Gravitational energy can power the Sun for only **15 million years**. Since the Sun is known to be 4.5 billion years old, gravity alone cannot be the primary energy source on the main sequence. This was a major unresolved problem before nuclear physics was understood. The resolution is thermonuclear fusion, which powers the Sun for billions of years.

The Kelvin–Helmholtz timescale is, however, the relevant timescale for pre-main-sequence contraction and for phases when nuclear burning is not available (e.g., between shell flashes or during gravitational contraction toward a new burning stage).

---

## 9. Equation 5 — Radiative Temperature Gradient and Convection

### 9.1 Radiative Temperature Gradient

Energy can be transported outward by radiation. In the radiative regime, the temperature gradient required to carry the luminosity $L(r)$ outward by photon diffusion is derived from two relations.

The gradient of radiation pressure with radius is:

$$\frac{dP_\text{rad}}{dr} = \frac{4}{3}aT^3\frac{dT}{dr}$$

At the same time, the radiation pressure gradient is driven by the opacity and the radiation flux:

$$\frac{dP_\text{rad}}{dr} = -\frac{\kappa\rho}{c}\,F_\text{rad}$$

where $\kappa$ is the opacity (cm$^2$ g$^{-1}$) and $F_\text{rad} = L(r)/(4\pi r^2)$ is the radiation flux.

Combining these two expressions:

$$\frac{4}{3}aT^3\frac{dT}{dr} = -\frac{\kappa\rho}{c}\frac{L(r)}{4\pi r^2}$$

Solving for $dT/dr$:

$$\boxed{\left.\frac{dT}{dr}\right|_\text{rad} = -\frac{3\kappa\rho}{4ac}\frac{L(r)}{4\pi r^2 T^3}}$$

This is the **radiative temperature gradient** (Equation 5). The negative sign indicates that temperature decreases outward. Note the dependence on opacity $\kappa$ and flux $L(r)/(4\pi r^2)$: if opacity is high or the energy flux is large, a steep temperature gradient is needed to push radiation through.

### 9.2 Three Mechanisms of Energy Transport

There are three mechanisms by which energy is transported inside a star:

1. **Radiation (radiative transport):** Energy carried by photons diffusing outward. Always operating; the dominant mechanism in radiative zones.
2. **Convection (convective transport):** Energy carried by bulk motions of gas cells ("bubbles") that rise when hot and sink when cool. This is a **mixing process**: convection homogenizes the chemical composition of any zone it reaches. It is analogous to boiling water in a pot.
3. **Conduction (thermal conduction):** Energy carried by electrons. This mechanism is **efficient only when the gas is degenerate**, because in degenerate gas electrons have very long mean free paths (they cannot be scattered into already-occupied quantum states). In non-degenerate stellar interiors, thermal conduction is negligible.

Understanding when convection operates is crucial because it directly affects the structure and chemical mixing of the star.

### 9.3 Physical Picture of Convection — The Schwarzschild Criterion

Convection operates like boiling water: it starts when the temperature gradient inside the medium exceeds a threshold value. The criterion that determines whether a given region is convective is the **Schwarzschild criterion**.

**Physical argument:** Consider a small parcel of gas at position $r$ with properties ($\rho_1^*$, $P_1^*$, $T_1^*$). This parcel is displaced **adiabatically** (no heat exchange with surroundings) outward to position $r + dr$, where its properties become ($\rho_2^*$, $P_2^*$, $T_2^*$). The surrounding environment at $r + dr$ has properties ($\rho_2$, $P_2$, $T_2$).

The parcel immediately adjusts its pressure to match the surroundings (pressure equilibration is fast). Now compare its temperature to the environment:

- **If the parcel is hotter than its surroundings** (at fixed pressure, using $P = k\rho T/(\mu H)$): it has lower density than the surroundings. Being buoyant, it **continues to rise** → **CONVECTION is active**.
- **If the parcel is cooler than its surroundings**: it has higher density, is heavier, and **sinks back** → **NO CONVECTION**.

Since the parcel moves adiabatically, whether it is hotter or cooler than the environment at $r + dr$ depends on which temperature gradient is steeper:
- If the actual (radiative) gradient is steeper than the adiabatic gradient, the parcel displaced adiabatically arrives hotter than its surroundings → convection.
- If the actual (radiative) gradient is shallower than the adiabatic gradient, the parcel arrives cooler → no convection.

This gives the Schwarzschild criterion:

$$\left|\frac{dT}{dr}\right|_\text{rad} > \left|\frac{dT}{dr}\right|_\text{ad} \implies \text{CONVECTION}$$

$$\left|\frac{dT}{dr}\right|_\text{rad} < \left|\frac{dT}{dr}\right|_\text{ad} \implies \text{NO CONVECTION}$$

### 9.4 The Nabla Formalism

In practice, the Schwarzschild criterion is expressed in terms of the logarithmic temperature gradient with respect to pressure (rather than with respect to radius), because temperature and pressure are deeply connected inside a star:

$$\nabla \equiv \frac{d\log T}{d\log P} = \frac{P}{T}\frac{dT}{dP}$$

The quantity $\nabla$ is called "**nabla**" (or the temperature gradient in the logarithmic pressure scale). The two descriptions are equivalent but related by:

$$\nabla = \frac{P}{T}\frac{dr}{dP}\frac{dT}{dr} \qquad \Longleftrightarrow \qquad \frac{dT}{dr} = \nabla\frac{T}{P}\frac{dP}{dr}$$

The advantage of using $\nabla$ is that the adiabatic gradient takes an extremely simple form. Starting from the adiabatic condition:

$$\left.\frac{dT}{dr}\right|_\text{ad} = \left(1 - \frac{1}{\gamma}\right)\frac{T}{P}\frac{dP}{dr}$$

and multiplying both sides by $P/(T\,dP/dr)$:

$$\nabla_\text{ad} = 1 - \frac{1}{\gamma} = \frac{\gamma - 1}{\gamma}$$

For a monatomic ideal gas, $\gamma = c_P/c_V$. The specific heats are:
- At constant volume: $c_V = \frac{3}{2}RN_m$
- At constant pressure: $c_P = \frac{5}{2}RN_m$

Their ratio: $\gamma = c_P/c_V = 5/3$. Therefore:

$$\boxed{\nabla_\text{ad} = \frac{\gamma - 1}{\gamma} = \frac{2}{5} = 0.4}$$

This is a constant for a simple ideal gas. The Schwarzschild criterion in nabla form becomes:

$$\nabla_\text{rad} > \nabla_\text{ad} = 0.4 \implies \text{CONVECTION}$$
$$\nabla_\text{rad} < \nabla_\text{ad} = 0.4 \implies \text{NO CONVECTION}$$

On a graph of $\nabla$ versus $\log P$ (where $\log P$ increases inward), the adiabatic gradient appears as a horizontal line at $\nabla = 0.4$. The radiative gradient curve starts high at low $\log P$ (outer layers), crosses down, and dips below $\nabla_\text{ad}$ in the deeper interior. Regions where the radiative gradient curve lies above the horizontal $\nabla_\text{ad} = 0.4$ line are convective; regions below are radiative.

### 9.5 Physical Triggers of Convection

During stellar evolution, the radiative gradient $\nabla_\text{rad} \propto \kappa\,L_r/(4\pi r^2)$ must be constantly monitored because two parameters can push it above the threshold:

1. **High opacity $\kappa$:** High opacity makes it harder for radiation to pass through, requiring a steeper temperature gradient to carry the same flux. This is why the helium second-ionization opacity hump (at $T \sim 40{,}000$ K) triggers the **outer convection zone** in solar-type stars.
2. **High energy flux** $L(r)/(4\pi r^2)$: If the energy flux is very high (e.g., in massive stars with intense CNO-cycle burning concentrated in a very small core, or in any star where a large luminosity must pass through a small cross-section), convection can be triggered in the **core**.

Convection is a key phenomenon because it **mixes the gas**, homogenizing chemical composition over the convective zone. This directly affects the fuel available for nuclear reactions and the evolution of the stellar structure.

---

## 10. Equation 6 — Opacity

### 10.1 Definition and Units

**Opacity** $\kappa(\rho, T)$ measures the resistance of stellar material to the passage of radiation. It is a cross-section per unit mass, with units of **cm$^2$ g$^{-1}$**. High opacity means photons are frequently absorbed or scattered and energy flows slowly; low opacity means photons travel more freely.

Physically, opacity is driven by the interaction of **electrons** with photons. Four types of electron-photon interactions are relevant.

### 10.2 Four Types of Opacity Processes

**Bound-Bound (BB) absorption:**
An electron bound to an atom absorbs a photon and transitions to a higher energy level but remains bound. This is the process responsible for **spectral absorption lines**. Inside the stellar interior, where essentially all atoms are fully ionized, BB absorption is negligible. It is, however, crucial in the **stellar atmosphere**, where it produces the observable absorption spectrum.

**Bound-Free (BF) absorption (photoionization):**
A bound electron absorbs a photon energetic enough to free it entirely from the atom, producing an ion and a free electron. This is the photoionization process. It is the dominant opacity source at intermediate stellar temperatures ($\sim 10{,}000$ to $\sim 10^6$ K).

**Free-Free (FF) absorption (inverse bremsstrahlung):**
A free electron (not bound to any nucleus) absorbs a photon and increases its kinetic energy. This is dominant in the hot stellar interior where all atoms are fully ionized and the gas is a plasma of free electrons and bare nuclei.

**Electron Scattering (Thomson/Compton scattering):**
A free electron scatters (deflects) a photon without absorbing it. This is not a true absorption but effectively impedes the outward flow of radiation. It becomes the dominant opacity source at very high temperatures where the other processes weaken.

### 10.3 Ionization Structure of the Star and Dominant Opacity by Region

The dominant opacity process at each depth depends on the ionization state, which is controlled by temperature. Reading the stellar cross-section from outside to inside:

- **Outer layer** ($T \sim 6{,}000$–$10{,}000$ K): hydrogen is mostly neutral → **BB absorption** dominates.
- **Intermediate layer** ($T \sim 10{,}000$–$10^6$ K): hydrogen is ionized, helium is partially ionized → **BF absorption** dominates.
- **Deep interior** ($T > 10^6$ K): all elements are completely ionized, no bound electrons available → **FF absorption** and then **electron scattering** dominate.

As one moves inward, both the number of completely ionized atoms and the number of free electrons increase monotonically. At $T \sim 10{,}000$ K, H fully ionizes; at $T \sim 15{,}000$–$40{,}000$ K, He progressively ionizes (partial then complete).

### 10.4 Kramers' Laws

The opacity of each process can be approximated by analytical expressions called **Kramers' laws**:

$$\kappa_{BF} \propto 10^{25}\,Z\,(1+X)\,\frac{\rho}{T^{3.5}}$$

$$\kappa_{FF} \propto 10^{22}\,(X+Y)\,(1+X)\,\frac{\rho}{T^{3.5}}$$

$$\kappa_E \propto 0.2\,(1+X)$$

**Explanation of dependences:**

- $\kappa_{BF}$ depends on **$Z$** (the metal mass fraction) because at the temperatures where BF dominates, hydrogen and helium are already fully ionized and have no bound electrons. Only the heavy elements (metals) still have a few bound electrons that can absorb photons. Therefore, bound-free opacity increases with metallicity.
- $\kappa_{FF}$ depends on **$(X+Y)(1+X)$**: ionized hydrogen and helium (which dominate in $X+Y$) produce the free electrons needed for FF absorption; $(1+X)$ reflects the electron density which also includes the electrons from hydrogen.
- Both $\kappa_{BF}$ and $\kappa_{FF}$ scale as $\rho/T^{3.5}$: they increase with density (more absorbers) and **decrease strongly with temperature** (hotter photons are more penetrating; the Kramers $T^{-3.5}$ dependence is a fundamental result from quantum mechanical cross-section calculations).
- $\kappa_E$ (electron scattering) has **no dependence on density or temperature** — it depends only on the number density of free electrons, which scales with $(1+X)$ at fixed $\rho$. This makes it the "floor" opacity at very high temperatures.

### 10.5 Opacity as a Function of Temperature

The opacity $\log\kappa$ plotted versus $\log T$ (for various fixed densities $\log\rho$) shows several characteristic features:

1. **Sharp rise near $T \approx 10{,}000$ K:** Associated with the ionization of hydrogen. As hydrogen ionizes, the number of free electrons surges, dramatically increasing BB and BF opacity. The opacity increases steeply (marked by a red line in the diagram) at this ionization temperature.

2. **Declining region ($T \sim 10{,}000$ to $\sim 10^6$ K):** After the ionization peak, opacity decreases with temperature as $\kappa \propto \rho T^{-3.5}$ (the Kramers law slope of $-3.5$ on the log–log plot, shown as red lines along the curves).

3. **He-ionization hump near $T \approx 40{,}000$ K:** A notable deviation from the Kramers $T^{-3.5}$ decrease — the opacity "bulges" upward near $T \sim 40{,}000$ K (the "hump" highlighted by a blue arrow). This is caused by the **second ionization of helium** (He$^+$ → He$^{2+}$), which provides an additional burst of free electrons and bound-free opacity. This hump is significant because it can trigger convection in the envelopes of stars near this temperature range.

4. **Flat plateau at very high $T$:** The opacity levels off to the constant electron scattering opacity $\kappa_E = 0.2(1+X)$ (horizontal blue line on the diagram).

5. **Density dependence:** At any given temperature, higher density shifts the opacity curves upward (more absorbing matter per unit volume), consistent with the $\rho$ factor in $\kappa_{BF}$ and $\kappa_{FF}$.

---

## 11. Equation 7 — Thermonuclear Energy Production

### 11.1 Why Thermonuclear Fusion?

Thermonuclear fusion reactions are the **primary energy source** of stars. The fusion of light atomic nuclei produces:
- **Energy** (from the mass deficit $\delta m$, via $E = \delta m\,c^2$)
- **New, heavier chemical elements** (nucleosynthesis)

The process is extremely efficient because $c^2 \approx 10^{21}$ cm$^2$ s$^{-2}$ is an enormous factor — even a very small mass deficit yields huge amounts of energy.

Fusion reactions are organized into **chains**, each with a characteristic "ignition" temperature, fuel species, and product. Three key parameters: **fuel**, **chain type**, and **ignition temperature**.

### 11.2 The Coulomb Barrier Problem

All atomic nuclei carry **positive electric charge**. Two approaching nuclei repel each other via the **Coulomb (electrostatic) force**. As $r \to 0$, the Coulomb potential $V \propto 1/r$ rises steeply — creating a **Coulomb barrier** that must be overcome for the nuclei to come close enough for the **strong nuclear force** to take over.

The strong force is attractive but has an extremely short range ($r_0 < 10^{-13}$ cm); beyond this range, only the repulsive Coulomb force acts. Classically overcoming the barrier would require temperatures $\sim 10^{10}$ K. Quantum mechanical **tunneling** allows nuclei to tunnel through the barrier at stellar core temperatures ($T \sim 10^7$–$10^9$ K).

The required conditions — **high density** (to maximize the collision rate) and **high temperature** (to give nuclei enough thermal kinetic energy to approach close enough for tunneling) — are found uniquely in the **stellar core**. The relevant kinetic energy relation is $\frac{1}{2}mv^2 \approx kT$.

### 11.3 Nuclear Binding Energy

The stability of a nucleus is measured by its **binding energy**:

$$E_B(Z, A) = \{Z\,m_p + (A-Z)\,m_n - m_\text{nucl}\}\,c^2$$

where:
- $Z$ = number of protons, $A$ = total number of nucleons
- $m_p = 1.672 \times 10^{-24}$ g (proton mass)
- $m_n = 1.675 \times 10^{-24}$ g (neutron mass)
- $m_\text{nucl}$ = actual mass of the nucleus

The binding energy measures how much energy would be required to disassemble the nucleus into its individual free nucleons. It is always positive because the bound nucleus is always less massive than the sum of its free constituents — the **mass deficit** $\delta m = Z\,m_p + (A-Z)\,m_n - m_\text{nucl}$ is converted to binding energy.

The **binding energy per nucleon** $E_B/A$ is the key quantity for understanding nuclear stability. A graph of $E_B/A$ (in MeV) versus mass number $A$:
- Rises steeply from hydrogen (A=1) through the light elements.
- Reaches a broad maximum at $A \approx 56$ — the **iron group** (Fe, Co, Ni). Iron is the most tightly bound nucleus.
- Declines slowly for $A > 56$.

**Critical consequence:** Fusion reactions release energy only when combining lighter nuclei into heavier ones **up to iron**. Fusion beyond iron would require energy input rather than producing it. This is why:

$$\text{THERMONUCLEAR FUSION REACTIONS STOP AT IRON}$$

Iron represents the final stage of the chemical evolution of a stellar core. Once the core is composed of iron, no additional fusion can generate energy, and the core must collapse.

### 11.4 Basic Nuclear Nomenclature

A nucleus is specified by its **atomic number $Z$** (number of protons, which uniquely determines the chemical element) and its **mass number $A$** (total number of nucleons = protons + neutrons). Neutron number $N = A - Z$.

**Isotopes** are nuclei of the same element ($Z$) but different $A$ — e.g., He$^3$ and He$^4$ are both helium isotopes.

Key particles:
- Proton: $Z=1, A=1$ (positive charge)
- Neutron: $Z=0, A=1$ (neutral)
- Alpha particle: He$^4$ nucleus (2 protons + 2 neutrons)

Examples:
- $Z=1, A=1$: H$^1$ (proton)
- $Z=2, A=4$: He$^4$ (alpha particle)
- $Z=2, A=3$: He$^3$ (helium-3 isotope)
- $Z=3, A=7$: Li$^7$
- $Z=4, A=9$: Be$^9$

---

## 12. The Main Thermonuclear Fusion Chains

### 12.1 Summary of Chains and Ignition Temperatures

| Chain | Type | Fuel | Ignition Temperature |
|-------|------|------|---------------------|
| Proton-Proton (PP) | H-burning | H | $T \approx 1.4 \times 10^7$ K |
| CNO cycle | H-burning | H (C, N, O as catalysts) | $T \approx 1.8 \times 10^7$ K |
| Triple-alpha ($3\alpha$) | He-burning | He | $T \approx 1.5 \times 10^8$ K |
| Alpha-capture | He/C/O burning | He + heavier nuclei | $T > 5 \times 10^8$ K |
| Carbon burning | C-burning | C | $T \approx 5$–$6 \times 10^8$ K |
| Neon burning | Ne-burning | Ne | $T \approx 1.2$–$1.9 \times 10^9$ K |
| Oxygen burning | O-burning | O | $T \approx 1.5$–$2.6 \times 10^9$ K |
| Silicon burning | Si-burning (photo-disintegration) | Si | $T \approx 2.3 \times 10^9$ K |

At all these temperatures, all atoms are **completely ionized** — the gas is a plasma of bare nuclei and free electrons. The reactions involve only nuclei.

### 12.2 The Proton-Proton (PP) Chains — Hydrogen Burning

The PP chains convert 4 hydrogen nuclei into 1 helium-4 nucleus:

$$4\,\text{H}^1 \to \text{He}^4 + 2e^+ + 2\nu_e + \text{energy}$$

There are three branches, sharing a common first two steps.

**Common first steps:**
$$\text{H}^1 + \text{H}^1 \to \text{H}^2 + e^+ + \nu \qquad (+1.44 \text{ MeV} - 0.26 \text{ MeV (neutrino)},\quad t_{1/2} \sim 1.4\times10^9 \text{ yr})$$
$$\text{H}^2 + \text{H}^1 \to \text{He}^3 + \gamma \qquad (+5.49 \text{ MeV},\quad t \sim 6 \text{ sec})$$

The first reaction is the **rate-limiting step** of the entire PP chain system — by far the most unlikely reaction because it requires a proton to transform into a neutron via $\beta^+$ decay:

$$p^+ \to n + e^+ + \nu \qquad (\beta^+ \text{ decay})$$

For free protons, $\beta^+$ decay is essentially impossible because the proton mass is smaller than the neutron mass (the process would require energy input rather than releasing it). However, inside a two-proton collision, the weak interaction allows this with a very small probability, giving the enormous timescale of $\sim 1.4 \times 10^9$ yr. This long timescale is what makes the Sun long-lived — it effectively throttles the fusion rate.

**Sign convention:** Negative energy values in the reaction tables indicate energy **lost to neutrinos**, which escape the star without depositing their energy. Total neutrino loss in PPI is about 0.5 MeV ($\sim 2\%$).

**The $\beta^-$ decay note:** In contrast to the nearly impossible $\beta^+$ decay of protons, the $\beta^-$ decay of free neutrons is **spontaneous and rapid**:

$$n \to p^+ + e^- + \bar{\nu} \qquad (t_{1/2} \approx 800 \text{ sec} \approx 13 \text{ min})$$

Free neutrons are therefore systematically destroyed within minutes. This is why free neutrons essentially do not exist in nature unless just freshly produced. This has major implications for nucleosynthesis.

**PP-I Branch (69% branching in the Sun):**
$$\text{He}^3 + \text{He}^3 \to \text{He}^4 + 2\,\text{H}^1 \qquad (+12.85 \text{ MeV},\quad t \sim 10^6 \text{ yr})$$

Net reaction: $4\text{H}^1 \to \text{He}^4$. Total energy:
$$2(1.44 - 0.26 + 5.49) + 12.85 = 26.2 \text{ MeV} = 4.2 \times 10^{-5} \text{ erg}$$

**PP-II Branch (from the remaining 31%; 99.7% of this branch):**
$$\text{He}^3 + \text{He}^4 \to \text{Be}^7 + \gamma$$
$$\text{Be}^7 + e^- \to \text{Li}^7 + \nu \qquad (p + e^- \to n + \nu \text{ inside Be}^7)$$
$$\text{Li}^7 + \text{H}^1 \to \text{Be}^8 \to 2\,\text{He}^4 + \gamma$$

The Be$^7$ captures an electron, converting one of its protons to a neutron via inverse $\beta$ decay, producing Li$^7$, which then captures a proton to form unstable Be$^8$, which immediately splits into two alpha particles.

**PP-III Branch (0.3% of the 31% branch = ~0.1% total):**
$$\text{He}^3 + \text{He}^4 \to \text{Be}^7 + \gamma$$
$$\text{Be}^7 + \text{H}^1 \to \text{B}^8 + \gamma$$
$$\text{B}^8 \to \text{Be}^8 + e^+ + \nu \qquad (p \to n + e^+ + \nu)$$
$$\text{Be}^8 \to 2\,\text{He}^4 + \gamma$$

PPIII is rare but important in neutrino physics: B$^8$ decay produces high-energy neutrinos detectable on Earth (the solar neutrino problem historically concerned these).

The three PP branches share the same initial two reactions; the branching between PP-I and PP-II/III occurs at the He$^3$ junction. The branching ratios depend on temperature.

### 12.3 The CNO Cycle — Hydrogen Burning via Catalysts

The CNO cycle is an alternative hydrogen-burning mechanism that **requires pre-existing carbon, nitrogen, and oxygen** as catalysts. It does not produce these elements — they are used and regenerated in each cycle.

**Important:** This process does NOT produce C, N, and O — it requires them to already be present and uses them as catalysts.

**The main CN cycle (a closed loop):**

$$\text{C}^{12} + \text{H}^1 \to \text{N}^{13} + \gamma$$
$$\text{N}^{13} \to \text{C}^{13} + e^+ + \nu \qquad (p \to n + e^+ + \nu, \text{ beta decay})$$
$$\text{C}^{13} + \text{H}^1 \to \text{N}^{14} + \gamma$$
$$\text{N}^{14} + \text{H}^1 \to \text{O}^{15} + \gamma$$
$$\text{O}^{15} \to \text{N}^{15} + e^+ + \nu \qquad (p \to n + e^+ + \nu, \text{ beta decay})$$
$$\text{N}^{15} + \text{H}^1 \to \text{C}^{12} + \text{He}^4$$

The cycle closes: C$^{12}$ is regenerated. The net result is $4\text{H}^1 \to \text{He}^4$.

The cycle has a **rapid branch** (C$^{12}$ → N$^{13}$ → C$^{13}$ → N$^{14}$, on the right side of the cycle) and a **slow branch** (N$^{14}$ → O$^{15}$ → N$^{15}$ → C$^{12}$, on the left side). The slow branch is rate-limited by the $\text{N}^{14}+\text{H}^1$ reaction, which has the lowest cross-section in the cycle. As a result, during CNO burning, **nitrogen-14 accumulates** at the expense of carbon and oxygen — this is an observationally important prediction.

**Ignition temperature:** $T \approx 1.8 \times 10^7$ K, slightly higher than PP chains. However, the energy generation rate of the CNO cycle is **extremely sensitive to temperature** ($\epsilon_{CN} \propto T_6^{13-20}$), compared to PP chains ($\epsilon_{pp} \propto T_6^{3.5-6}$). This steep temperature dependence means:
- In lower-temperature cores ($T \lesssim 2 \times 10^7$ K), PP chains dominate.
- In higher-temperature cores ($T \gtrsim 2 \times 10^7$ K), the CNO cycle rapidly overtakes.
- In more massive stars (which have hotter cores), the CNO cycle dominates and the energy production is highly concentrated in the center, tending to drive core convection.

### 12.4 The Triple-Alpha Process ($3\alpha$) — Helium Burning

After hydrogen is exhausted in the core, the star contracts and heats until helium burning ignites at $T \approx 1.5 \times 10^8$ K. The process converts three helium nuclei (alpha particles) into one carbon-12 nucleus.

The **alpha particle** is the alternative name for the helium nucleus (He$^4$). Helium burning is thus "alpha burning."

The reaction cannot proceed as a single triple collision — that is too improbable. It proceeds in two steps:

**Step 1 (quasi-equilibrium):**
$$\text{He}^4 + \text{He}^4 \leftrightarrow \text{Be}^8 \qquad (-0.1 \text{ MeV})$$

Be$^8$ is **unstable** and decays back into two alpha particles with a lifetime of only $\sim 10^{-17}$ s. A tiny equilibrium population of Be$^8$ exists at any moment, but it is extremely small. The $-0.1$ MeV indicates this step is very slightly endothermic — the double-headed arrow shows it is an equilibrium.

**Step 2:**
$$\text{Be}^8 + \text{He}^4 \to \text{C}^{12} + \gamma \qquad (+7.4 \text{ MeV})$$

Before the Be$^8$ decays, if it is struck by another alpha particle, it can fuse to form C$^{12}$. This step requires a **resonance in C$^{12}$** at the appropriate energy level (the famous **Hoyle state**, predicted by Fred Hoyle before its experimental discovery in 1957). Without this coincidental nuclear resonance, carbon would not form in significant quantities in stars — a remarkable fine-tuning.

Net energy of $3\alpha$: $-0.1 + 7.4 = +7.3$ MeV $\approx 1.2 \times 10^{-5}$ erg.

The energy generation rate is $\epsilon_{3\alpha} \propto \rho^2 Y^3 T_8^{20-30}$ — extremely sensitive to temperature, and also depends on $\rho^2$ because it is effectively a three-body process.

### 12.5 Advanced Burning Stages — Carbon, Neon, Oxygen, Silicon

After helium burning produces C$^{12}$ and O$^{16}$, more massive stars (with non-degenerate cores) can reach even higher temperatures and ignite further burning stages:

**Carbon burning** (at $T \approx 5$–$6 \times 10^8$ K, non-degenerate core):
$$\text{C}^{12} + \text{C}^{12} \to \begin{cases} \text{O}^{16} + 2\text{He}^4 \\ \text{Ne}^{20} + \text{He}^4 \end{cases}$$

**Neon burning** (at $T \approx 1.2$–$1.9 \times 10^9$ K, non-degenerate core):
$$\text{Ne}^{20} + \gamma \to \text{O}^{16} + \text{He}^4$$
$$\text{Ne}^{20} + \text{He}^4 \to \text{Mg}^{24} + \gamma$$

**Oxygen burning** (at $T \approx 1.5$–$2.6 \times 10^9$ K, non-degenerate core):
$$\text{O}^{16} + \text{O}^{16} \to \text{S}^{32} \to \text{Si}^{28} + \text{He}^4$$
(and other channels producing P$^{28}+p$, S$^{31}+n$, P$^{30}+$H$^2$)

**Silicon burning** (at $T \approx 2.3 \times 10^9$ K, non-degenerate core):

Silicon burning is dominated by **photo-disintegration** — gamma-ray photons at this extreme temperature are energetic enough to break nuclei apart. The cascade runs backwards through the alpha-capture chain:
$$\text{Si}^{28} + \gamma \to \text{Mg}^{24} + \text{He}^4$$
$$\text{Mg}^{24} + \gamma \to \text{Ne}^{20} + \text{He}^4$$
$$\text{Ne}^{20} + \gamma \to \text{O}^{16} + \text{He}^4$$
$$\text{O}^{16} + \gamma \to \text{C}^{12} + \text{He}^4$$
$$\text{C}^{12} + \gamma \to 3\text{He}^4$$

The liberated alpha particles are then captured by existing heavy nuclei via alpha-capture reactions, gradually increasing the mean atomic weight of the core until it is dominated by iron-group nuclei ($A \approx 56$). Silicon burning is essentially a **photo-disintegration equilibrium** that produces alpha particles, which are then captured to build heavier elements all the way to the iron group.

### 12.6 Alpha-Capture Processes and Alpha Elements

At $T > 6 \times 10^8$ K, existing nuclei can capture alpha particles in a chain building progressively heavier nuclei:

$$\text{C}^{12} + \text{He}^4 \to \text{O}^{16} + \gamma \quad (7.6 \text{ MeV})$$
$$\text{O}^{16} + \text{He}^4 \to \text{Ne}^{20} + \gamma \quad (4.7 \text{ MeV})$$
$$\text{Ne}^{20} + \text{He}^4 \to \text{Mg}^{24} + \gamma \quad (9.3 \text{ MeV})$$
$$\text{Mg}^{24} + \text{He}^4 \to \text{Si}^{28} + \gamma \quad (9.9 \text{ MeV})$$
$$\text{Si}^{28} + \text{He}^4 \to \text{S}^{32} + \gamma \quad (6.9 \text{ MeV})$$
$$\text{S}^{32} + \text{He}^4 \to \text{Ar}^{36} + \gamma \quad (6.6 \text{ MeV})$$
$$\vdots$$
$$\text{Cr}^{52} + \text{He}^4 \to \text{Ni}^{56} + \gamma$$

Ni$^{56}$ then undergoes beta decay to Fe$^{56}$ with a half-life of 6 days.

The products of alpha-capture — O, Ne, Mg, Si, S, Ar, Ca — are called **alpha elements** because they are built by successive addition of alpha particles. They are among the **most abundant elements in the Universe** after hydrogen and helium. The observed ratio of alpha elements to iron ([α/Fe]) in stellar atmospheres is a key diagnostic of nucleosynthesis history: stars enriched primarily by core-collapse supernovae (from rapidly evolving massive stars) have high [α/Fe], while stars enriched mainly by Type Ia supernovae have lower [α/Fe].

### 12.7 Neutron-Capture Processes

Elements heavier than iron cannot be built by thermonuclear fusion (which would require energy input beyond iron). Instead, they are built by **neutron capture**:

A nucleus $(Z, A)$ captures a neutron:
$$(Z, A) + n \to (Z, A+1)$$

This creates an isotope of the same element (same $Z$) but with one more neutron. Many of these new isotopes are unstable and undergo $\beta^-$ decay:

$$(Z, A+1) \to (Z+1, A+1) + e^- + \bar{\nu}$$

converting a neutron into a proton and thus creating a new element with $Z+1$.

The problem with neutron capture is the scarcity of free neutrons — they decay ($n \to p^+ + e^- + \bar{\nu}$) with a half-life of $\sim 800$ s. Key reactions that produce neutrons in stars:

$$\text{Fe}^{56} + \gamma \to 13\,\text{He}^4 + 4n$$
$$\text{C}^{13} + \alpha \to \text{O}^{16} + n$$

**Two types of neutron capture:**

- **s-process (slow):** The neutron capture rate is slower than the $\beta^-$ decay rate of the produced unstable isotope. Only one neutron is captured before the nucleus decays. The s-process therefore walks along the valley of stability on the nuclide chart, stepping diagonally by neutron capture (increases $N$) followed by beta decay (converts $N$ to $Z$).
- **r-process (rapid):** The neutron capture rate is faster than beta decay. Multiple neutrons are captured before any decay occurs, creating very neutron-rich, highly unstable isotopes far from the valley of stability. After the neutron flux ceases (e.g., after a supernova), these decay back toward stability, producing elements that cannot be reached by the s-process (trans-iron elements, heavy isotopes). The r-process likely occurs in neutron star mergers and/or core-collapse supernovae.

The cosmic abundance distribution of elements heavier than iron is the combined product of BB nucleosynthesis (H and He), thermonuclear fusion in stars (C through Fe group), and neutron-capture processes (s and r processes beyond Fe).

### 12.8 Energy Generation Rate Formula

The energy generation rate $\epsilon$ (erg g$^{-1}$ s$^{-1}$) quantifies the energy produced per second per gram of material. More precisely:

$$\epsilon = \sum \frac{\text{energy per reaction}}{\text{time}} \times \frac{\text{reactions per cm}^3}{\text{second}} \times \frac{\text{cm}^3}{\text{gram}} \quad [\text{erg g}^{-1} \text{s}^{-1}]$$

This depends on the available **fuel**, **temperature**, and **density**. Approximate formulae:

$$\epsilon_{pp} = \epsilon_1\,\rho\,X^2\,T_6^{\nu_{pp}}, \quad \nu_{pp} \in [3.5, 6]$$
$$\epsilon_{CN} = \epsilon_2\,\rho\,X\,X_{CN}\,T_6^{\nu_{CN}}, \quad \nu_{CN} \in [13, 20]$$
$$\epsilon_{3\alpha} = \epsilon_3\,\rho^2\,Y^3\,T_8^{\nu_{3\alpha}}, \quad \nu_{3\alpha} \in [20, 30]$$

where $T_6 = T/(10^6 \text{ K})$, $T_8 = T/(10^8 \text{ K})$, and $X_{CN}$ is the mass fraction of CNO elements.

**Key observations:**

- The dependence on $X^2$ in PP chains reflects that two protons must collide; $X\,X_{CN}$ in CNO reflects one proton colliding with a CNO nucleus.
- The $3\alpha$ rate depends on $\rho^2$ (three-body process: two sequential He-He encounters) and $Y^3$.
- The **temperature exponents $\nu$ are large** — especially for CNO ($\nu \sim 13$–20) and $3\alpha$ ($\nu \sim 20$–30). This extreme temperature sensitivity means that thermonuclear reactions effectively act as thermostats only when the environment is thermoregulated (perfect gas). In a **degenerate** gas, the absence of thermoregulation leads to thermonuclear runaway.

On a $\log\epsilon$ vs $\log T$ plot, the CNO curve has a much steeper slope than the PP curve. The two curves intersect at a crossover temperature. Above this temperature, CNO dominates. The dramatic sensitivity of CNO to temperature has a direct structural consequence: stars that burn H primarily via CNO have much more concentrated energy production in the core, driving core convection.

### 12.9 Photo-disintegration and Neutrino Emission

At extreme temperatures (several $10^8$–$10^9$ K), two additional phenomena become important even in non-degenerate conditions:

**Photo-disintegration:** Gamma-ray photons are energetic enough to break up heavy nuclei. The most important examples are Si-burning (see Section 12.5) and the iron photo-disintegration that triggers core collapse in massive stars:
$$\text{Fe}^{56} + \gamma \to 13\,\text{He}^4 + 4n$$

This reaction is strongly endothermic — it consumes enormous energy — and when it occurs in a massive star's iron core, it removes the thermal pressure support and triggers gravitational collapse.

**Neutrino emission:** At high temperatures and densities, various processes produce neutrinos that carry energy directly out of the star at essentially the speed of light, bypassing the normal slow radiative diffusion. The relevant processes include:
- **Plasma process** (dominant at high density, lower temperature)
- **Photoneutrino process** (lower density, moderate temperature)
- **Pair-annihilation process** (dominant at high temperature)

Neutrino energy losses are negligible in the Sun but become increasingly important in later burning stages (carbon, oxygen, silicon burning), dramatically accelerating the pace of those advanced evolutionary phases. A star that burns hydrogen for billions of years may complete silicon burning in days once neutrino losses dominate.

---

## 13. The Stellar Atmosphere and Effective Temperature

### 13.1 Role of the Atmosphere

The seven structural equations determine the **luminosity** of the star. To complete the model and obtain the second H-R diagram parameter (the surface temperature), one must model the **stellar atmosphere** — the thin outer layer from which light escapes to the observer.

### 13.2 Optical Depth

In the atmosphere, the relevant independent variable is no longer the distance from the center $r$, but the **optical depth** $\tau_\lambda$:

$$\tau_{\lambda}(z) = \int_0^z \kappa_\lambda\,\rho\,dz$$

where $z$ is the geometric depth into the atmosphere and $\lambda$ indicates the wavelength. Optical depth is a dimensionless measure of how optically thick the atmosphere is. The atmosphere is modeled as concentric shells at increasing temperature as optical depth increases (moving inward). At $\tau = 0$, the atmosphere is fully transparent; larger $\tau$ means deeper, denser, hotter layers.

A photon at a given wavelength is last scattered or absorbed at approximately the layer where $\tau_\lambda \approx 1$ — this is the layer from which the observed radiation at that wavelength appears to emerge. The optical depth formulation allows one to naturally identify the depth of formation of the continuum and spectral lines.

### 13.3 The Temperature Profile and Effective Temperature

The key equation relating temperature to the vertical optical depth $\tau_v$ in the stellar atmosphere is:

$$\boxed{T^4 = \frac{3}{4}\,T_e^4\left(\tau_v + \frac{2}{3}\right)}$$

This equation defines the **effective (surface) temperature** $T_e$: it is the temperature of the layer at optical depth $\tau_v = 2/3$.

**Why $\tau_v = 2/3$?** At this depth, the photon mean free path equals the remaining path to the surface — roughly speaking, this is the deepest layer from which photons can escape directly. The radiation observed from outside corresponds to this layer. Under the assumption of blackbody radiation, the observed flux is $F = \sigma T_e^4$, so $T_e$ is the effective temperature inferred from the stellar luminosity and radius: $L = 4\pi R^2 \sigma T_e^4$.

**This is the temperature inserted into the H-R diagram.** For the Sun, $T_e = 5770$ K.

### 13.4 The Photosphere

The **photosphere** is the thin layer around $\tau \approx 2/3$ to $\tau = 0$. It is where:
- The **continuum spectrum** forms (at $\tau \approx 2/3$, the radiation field is approximately blackbody at $T_e$).
- The **absorption spectral lines** form: cooler gas in the outer photosphere ($\tau \approx 0$) absorbs specific wavelengths from the brighter continuum radiation emerging from below.

Spectral lines contain crucial observational information: the **chemical abundances** and the **radial velocities** of stars.

---

## 14. The Stellar Atmosphere — Spectral Lines and Chemical Abundances

### 14.1 Why Temperature Controls the Spectrum

In the stellar atmosphere, density is very low compared to the interior. The key physical parameter is **temperature**, which determines:
1. The **ionization state** of each chemical species (via the Saha equation): how many electrons are stripped from each atom.
2. The **excitation level** of each atomic species (via the Boltzmann equation): which energy levels are populated.

Together, these determine which spectral lines appear, at what strength, and thus the observable **spectral type** of the star.

### 14.2 The Saha Equation — Ionization Equilibrium

The Saha equation governs the ionization equilibrium between successive ionization states of an element:

$$\log\frac{N_{j+1}}{N_j} = -0.176 - \log P_e + \log\frac{U_{j+1}(T)}{U_j(T)} + 2.5\log T - \frac{5040}{T}\chi_i$$

where:
- $N_j$ and $N_{j+1}$ are the number densities of atoms in ionization states $j$ and $j+1$,
- $P_e$ is the electron pressure,
- $U_j(T)$ and $U_{j+1}(T)$ are the partition functions of the respective ionization states,
- $\chi_i$ is the ionization energy (in eV) of the $j$-th ionization state.

The Saha equation answers: **at a given temperature $T$, what fraction of atoms of this element have lost $j$ electrons?** Higher temperature → higher ionization state.

### 14.3 The Boltzmann Equation — Excitation

The Boltzmann equation gives the fraction of atoms in ionization state $j$ that are in a specific excited level $i$:

$$\frac{N_{ji}}{N_j} = \frac{g_i}{U_j(T)}\,10^{-\chi_i(5040/T)}$$

where $g_i$ is the statistical weight (degeneracy) of the excited level and $\chi_i$ is its excitation energy (eV).

The Boltzmann equation answers: **at temperature $T$, what fraction of atoms in ionization state $j$ is in the specific energy level that produces the observed spectral line?**

### 14.4 Spectral Classification

The ionization and excitation levels vary with temperature in characteristic ways, producing the **spectral classification** (O, B, A, F, G, K, M from hottest to coolest):

- **O stars** ($T > 30{,}000$ K): He II lines; highly ionized species.
- **B stars** ($T \sim 10{,}000$–$30{,}000$ K): He I lines; H lines appearing.
- **A stars** ($T \sim 7{,}500$–$10{,}000$ K): Hydrogen Balmer lines at maximum strength.
- **F and G stars** ($T \sim 5{,}000$–$7{,}500$ K): Ionized metal lines (Ca II, Fe II) strongest; solar-type spectra.
- **K and M stars** ($T < 5{,}000$ K): Neutral metal lines (Ca I) and molecular bands (TiO) appear; H lines weaken.

The observed line strength at a given $T$ reflects both the abundance of the element and the fraction of atoms in the correct ionization and excitation state.

### 14.5 Spectral Lines — Radial Velocity Measurement

Spectral lines carry kinematic information. A spectral line is expected at its laboratory ("rest") wavelength $\lambda_0$ but is observed at $\lambda_1$. The shift is due to the **Doppler effect**:

$$\frac{\lambda_1 - \lambda_0}{\lambda_0} = \frac{\Delta\lambda}{\lambda_0} = \frac{v_r}{c}$$

where $v_r$ is the radial velocity of the star along the line of sight. A positive shift ($\lambda_1 > \lambda_0$) means the star is receding (redshift); a negative shift means it is approaching (blueshift).

### 14.6 Equivalent Width — Measuring Line Intensity

The **equivalent width** $W$ measures the intensity (strength) of a spectral absorption line:

$$W = \int \frac{F_c - F_\lambda}{F_c}\,d\lambda$$

where $F_c$ is the continuum flux and $F_\lambda$ is the flux at wavelength $\lambda$ within the line.

Geometrically, $W$ is the width (in Angstroms) of a rectangle of height equal to the continuum level ($F_c$) and of area equal to the total area removed from the continuum by the absorption line. Equivalently, it is the width of a completely black (zero-flux) rectangle that absorbs the same total flux as the actual line.

**Physical meaning:** $W$ correlates with the **number of absorbing atoms** $N_a$ — those atoms currently in exactly the right ionization state and excitation level to absorb photons at this wavelength.

**Key note:** $N_a$ is the number of **active** atoms (those generating the observed line), not the total number of atoms of that element in the atmosphere. These can differ enormously depending on temperature.

### 14.7 The Curve of Growth

The relationship between $W$ and the column density of absorbing atoms $N_a$ is called the **curve of growth** ($\log W$ vs $\log N_a$). It has three regimes:

1. **Linear regime** ($W \propto N_a$): At low $N_a$, the line is optically thin and $W$ grows linearly with $N_a$.
2. **Flat (saturation) regime** ($W \propto (\ln N_a)^{1/2}$): At moderate $N_a$, the line core saturates — the central wavelengths are fully absorbed, and additional atoms only very slightly broaden the line.
3. **Square-root (damping) regime** ($W \propto N_a^{1/2}$): At very high $N_a$, the Lorentzian wings of the absorption line (from natural and pressure broadening) grow, and $W$ rises again.

**Practical use:** Measure $\log W$ from the spectrum, enter the curve of growth at the $y$-axis, and read off $\log N_a$ from the $x$-axis. For the Sun, a measured $\log(W/\lambda) = -3.90$ corresponds to reading $\log Nf\lambda \approx 14.85$ from the solar curve of growth.

### 14.8 From $N_a$ to $N_\text{TOT}$ — Ionization and Excitation Corrections

$N_a$ is only the number of atoms in the active configuration. The total number of atoms of that element in the atmosphere ($N_\text{TOT}$) requires two corrections, visualized as nested sets:

$$N_\text{TOT} \supset \underbrace{N_j}_{\text{Saha}} \supset \underbrace{N_{ji}}_{\text{Boltzmann}} = N_a$$

- **Ionization correction (Saha equation):** At photosphere temperature $T_e$, the Saha equation gives the fraction of atoms of this element in ionization state $j$ (the state producing the observed line). The remaining atoms are in other ionization states and do not contribute to this line. Correcting for all ionization states gives $N_\text{TOT from this ionization state}$, and summing over all ionization states gives $N_\text{TOT}$.
- **Excitation correction (Boltzmann equation):** The Boltzmann equation gives the fraction of atoms in ionization state $j$ that are in the correct excited level $i$. Dividing $N_a$ by this fraction gives $N_j$.

Both corrections depend strongly on temperature, which is why an accurate knowledge of $T_e$ is essential before measuring chemical abundances.

### 14.9 Deriving Chemical Abundances — The Square Bracket Notation

Once $N_\text{TOT}$ is known (atoms per cm$^2$ of atmosphere), the mass of the element per unit area is:

$$El_\text{mass} = N_\text{TOT} \times m_\text{atom} \quad [\text{g cm}^{-2}]$$

Chemical abundances are expressed as double-normalized logarithmic ratios — normalized first to hydrogen and then to the solar ratio — using the **square bracket notation**:

$$\left[\frac{El}{\text{H}}\right] = \log\left(\frac{El}{\text{H}}\right)_* - \log\left(\frac{El}{\text{H}}\right)_\odot$$

**Interpretation:**
- $[El/H] = 0$: same abundance ratio as the Sun.
- $[El/H] = +1$: 10 times more of that element (relative to hydrogen) than in the Sun.
- $[El/H] = -1$: 10 times less.

The ratio most commonly quoted in stellar evolution is **[Fe/H]** (iron-to-hydrogen ratio), which serves as a proxy for overall metallicity $Z$.

**Worked example from the lecture:**
- In a star: $El_\text{mass} = 9.3 \times 10^{-5}$ g cm$^{-2}$, H mass $\sim 1.1$ g cm$^{-2}$, so $\log(El/H)_* = \log(9.3 \times 10^{-5}/1.1) \approx -4$.
- In the Sun: $\log(El/H)_\odot = 6.33 - 12 = -5.67$.
- Result: $[El/H] = -4 - (-5.67) = +1.67$, meaning the element is $10^{1.67} \approx 47$ times more abundant in this star than in the Sun.

---

## 15. The Helium Problem and Primordial Nucleosynthesis

### 15.1 The Helium Problem

PP and CNO chains both produce helium during stellar hydrogen burning. However, if one integrates the total helium production from all stars over the entire age of the universe (the Hubble time, $\sim 13.8$ Gyr), the global helium mass fraction produced by stellar burning is only a few percent.

Yet observations show that even the **oldest stars in the Galaxy** — the most metal-poor, least-processed stars — have a helium mass fraction of about **24%** ($Y \approx 0.24$). This is far more than stellar nucleosynthesis can account for.

This discrepancy is called the "Helium Problem." Its resolution is **Big Bang nucleosynthesis (BBN)**: a large fraction of the observed helium was produced in the first few minutes after the Big Bang.

### 15.2 Big Bang Nucleosynthesis

The key to BBN is the availability of free neutrons in the first $\sim 15$ minutes after the Big Bang. In stars, free neutrons are nearly impossible to produce because the $\beta^+$ decay of protons inside proton-proton pairs is governed by the weak interaction and has an effective timescale of $\sim 1.4 \times 10^9$ yr. In the very early universe, however, neutrons were thermally produced in abundance.

The BBN helium-production chain:
$$n + p \to \text{H}^2 + \gamma$$
$$\text{H}^2 + \text{H}^2 \to \text{He}^3 + n$$
$$\text{He}^3 + n \to \text{H}^3 + p$$
$$\text{H}^2 + \text{H}^3 \to \text{He}^4 + n$$

The **primordial helium abundance** produced by BBN is $Y_p = 0.24$ — precisely what is observed in the oldest, least-processed stars. This is a major confirmation of the Big Bang model.

### 15.3 The A=5 and A=8 Bottleneck

Primordial nucleosynthesis effectively stopped at helium (with only trace amounts of Li$^7$ and Be$^9$) because **there are no stable nuclei with $A = 5$ or $A = 8$** in nature:

- He$^4$ + H$^1$ would produce a nucleus with $A = 5$ — but no such stable nucleus exists.
- He$^4$ + He$^4$ produces Be$^8$, which is unstable with a lifetime of only $10^{-17}$ s.

Without a stable "bridge" at mass 5 or 8, the nucleosynthesis chain could not proceed to carbon and beyond during the Big Bang (where the temperature and density rapidly fell below what was needed). The BBN thus produced essentially only H, He, and traces of Li and Be.

In stars, the triple-alpha process bridges the A=8 gap using the tiny equilibrium population of Be$^8$ that exists at the much higher temperatures and densities of helium-burning cores ($T \sim 10^8$ K, $\rho \sim 10^4$ g/cm$^3$). This is only possible because of the Hoyle resonance in C$^{12}$.

The cosmic abundance distribution therefore naturally divides into three contributions:
1. **H and He** (the dominant peak): from the Big Bang.
2. **C through Fe** (peaks of the alpha elements and iron group): from thermonuclear fusion in stars.
3. **Elements beyond Fe**: from neutron-capture processes (s-process in AGB stars, r-process in neutron star mergers/supernovae).

---

## 16. The Sun as the Reference Star

### 16.1 Solar Parameters

The Sun is the fundamental unit of measurement in stellar astrophysics. All stellar masses, luminosities, radii, and ages are typically expressed in solar units.

| Parameter | Value |
|-----------|-------|
| Distance from Earth | $1.5 \times 10^{13}$ cm ($= 1$ AU) |
| Radius $R_\odot$ | $7 \times 10^{10}$ cm ($\approx 100 \times R_\oplus$) |
| Mass $M_\odot$ | $2 \times 10^{33}$ g ($\approx 10^6 \times M_\oplus$) |
| Luminosity $L_\odot$ | $4 \times 10^{33}$ erg s$^{-1}$ |
| Average density | $1.4$ g cm$^{-3}$ |
| Central density | $\sim 1.5 \times 10^2$ g cm$^{-3}$ ($= 160$ g cm$^{-3}$) |
| Chemical composition | $X = 0.70$, $Y = 0.28$, $Z = 0.02$ |
| Surface temperature $T_e$ | $5770$ K |
| Central temperature $T_c$ | $\approx 1.6 \times 10^7$ K |
| Age | $4.5$ Gyr |

### 16.2 The Sun as a Calibration Object

The Sun serves as the calibration anchor for stellar astrophysics in multiple ways:

- The solar central temperature ($1.6 \times 10^7$ K) and central density ($\sim 160$ g cm$^{-3}$) confirm the solar core is a perfect gas: $T/\rho^{2/3} = 10^7/160^{2/3} \approx 10^7/29 \approx 3.4 \times 10^5 \gg 10^5$.
- The Kelvin–Helmholtz timescale for the Sun ($\sim 1.5 \times 10^7$ yr) is far shorter than the solar age ($4.5$ Gyr), proving that thermonuclear fusion — not gravity — powers the main sequence.
- The solar abundance ($X=0.70, Y=0.28, Z=0.02$) is the reference for the "[El/H]" abundance notation.
- The solar position on the H-R diagram (spectral type G2V, near the middle of the main sequence) anchors our understanding of the main sequence.
- The cutaway diagram of the solar interior (core, radiative zone, convective zone, photosphere, chromosphere, corona) provides the template for understanding stellar internal structure.

---

## 17. Textbook References

### 17.1 Carroll and Ostlie Chapter Guide

For Carroll & Ostlie, *An Introduction to Modern Astrophysics*:

| Topic | Chapter and Pages |
|-------|-----------------|
| Hydrostatic equilibrium | Chapter 10.1, pp. 315–320 |
| Gas pressure and equation of state | Chapter 10.2, pp. 320–328 |
| Physics of degenerate matter | p. 583 |
| Stellar energy sources | Chapter 10.3, pp. 329–350 |
| Energy transport and thermodynamics | Chapter 10.4, pp. 350–365 |
| Stellar opacity (interior and atmosphere) | Chapter 9.2, pp. 261–276 |
| Radiative transfer | Chapter 9.3, pp. 276–293 |
| Structure of spectral lines | Chapter 9.4, pp. 293–306 |
