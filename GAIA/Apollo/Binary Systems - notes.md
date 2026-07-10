# Binary Systems: Interactions, Mass Transfer, and Exotic Outcomes

**Sources:** High-fidelity transcription of lecture notes on binary stellar systems, covering the physics of gravitational potentials, Roche lobe geometry, conservative and non-conservative mass transfer, orbital evolution, accretion energetics, novae, Type Ia supernovae, binary survival after explosions, and detailed evolutionary case studies.
**Session:** Binary Systems

---

## 1. Motivation — Why Binary Systems Matter

### 1.1 Limitations of Single-Star Evolution

Standard stellar evolution theory deals with the **passive, isolated evolution of a single star**. Given a star's initial mass and chemical composition, single-star theory predicts a unique evolutionary track in the Hertzsprung–Russell (HR) diagram: the star progresses from the main sequence (MS) through subgiant and red giant branches, ultimately ending as a white dwarf, neutron star, or black hole depending on mass. This framework is internally consistent and describes the vast majority of stars well.

However, a large variety of cosmic objects cannot be interpreted within this single-star picture. They require the existence of **interacting stars in binary (or higher-order multiple) systems**. The observational evidence is compelling: HR diagrams of old globular clusters — which should be among the cleanest laboratories for single-star evolution — reveal populations of stars that violate the expectations of passive evolution.

A key example is provided by the globular clusters **NGC 288** and **NGC 362**. Their colour–magnitude diagrams (CMDs) show stars that appear **brighter than the main-sequence turn-off (MS-TO)**. This is a forbidden position for single stars: at the age of a globular cluster (many Gyr), every star that could have evolved off the MS and become luminous should have already done so and departed the MS. Stars brighter than the MS-TO, still on or near the MS, cannot exist in a pure single-star population. Their presence demands an additional physical process — specifically, interactions between stars in binary systems — to explain their anomalous youth.

This observational anomaly is one of the primary drivers for studying binary systems in detail. The binary channel does not merely produce exotic endpoints; it fundamentally alters the evolutionary trajectories of both components, generating a rich phenomenology that single-star theory cannot reproduce.

### 1.2 The Zoo of Binary-Interaction Products

When compact objects — white dwarfs (WDs), neutron stars (NSs), or black holes (BHs) — are members of a binary system, the combination of the compact object's extreme properties (small size, large mass, or both) with the gravitational interaction of the companion star can produce a remarkable range of high-energy and transient phenomena:

- **Cataclysmic variables (CVs):** Systems with a WD accreting from a low-mass companion. They exhibit quasi-periodic outbursts driven by instabilities in the accretion disk.
- **Novae:** Thermonuclear explosions on the surface of a WD caused by the runaway burning of accreted hydrogen. They recur on timescales of $10^4$–$10^5$ years.
- **Type Ia supernovae:** The complete thermonuclear disruption of a WD when its mass approaches the Chandrasekhar limit, either through accretion from a companion or through the merger of two WDs.
- **X-ray binaries:** Systems where a NS or BH accretes from a companion, releasing gravitational potential energy in the form of X-rays. They are among the most luminous objects in the X-ray sky.
- **Millisecond pulsars:** NSs that have been spun up to rotation periods of milliseconds by sustained accretion from a companion over millions of years (the "recycling" scenario).

Each of these outcomes is produced by a specific combination of mass ratio, orbital separation, and evolutionary state. Understanding the physics of binary interaction is therefore central to understanding a wide swath of astrophysical phenomena.

---

## 2. Fundamental Physics of Binary Systems

### 2.1 Definition and Key Parameters

A **binary system** is defined as a gravitationally bound pair of two astronomical bodies (here, stars) whose mutual gravitational attraction causes them to orbit a common **centre of mass** (barycentre). The two stars do not orbit each other directly; each orbits the barycentre at a distance inversely proportional to its mass.

The two most fundamental parameters characterising a binary system are:

1. **Separation $a$:** The distance between the centres of mass of the two components. For a circular orbit, this is constant; for an elliptical orbit, it is the semi-major axis. The separation determines the strength of the gravitational interaction and the size of the region of gravitational influence of each star.

2. **Component masses $M_1$ and $M_2$:** By convention, $M_1 \geq M_2$, so $M_1$ is called the **primary** (more massive) and $M_2$ the **secondary** (less massive). The mass ratio $q = M_2/M_1 \leq 1$ appears throughout the theory. The total mass $M = M_1 + M_2$ governs the orbital period via Kepler's third law.

These two parameters, together with the orbital eccentricity $e$, completely specify the orbital geometry. Much of binary-star physics amounts to understanding how $a$, $M_1$, and $M_2$ evolve over time as the stars interact.

### 2.2 Equipotential Surfaces and the Roche Potential

To understand mass transfer, one must think about the **gravitational potential** experienced by material in the binary system. In the co-rotating reference frame (rotating with the binary's orbital angular velocity $\omega$), the effective potential includes contributions from the gravitational attraction of both stars **and** from the centrifugal force due to the rotation:

$$\Phi_{\text{eff}}(\mathbf{r}) = -\frac{GM_1}{|\mathbf{r} - \mathbf{r}_1|} - \frac{GM_2}{|\mathbf{r} - \mathbf{r}_2|} - \frac{1}{2}\omega^2 |\mathbf{r} - \mathbf{r}_\text{cm}|^2$$

where $\mathbf{r}_1$ and $\mathbf{r}_2$ are the positions of the two stars, $\mathbf{r}_\text{cm}$ is the centre of mass, and $\omega$ is the orbital angular frequency. This is the **Roche potential**.

**Equipotential surfaces** are surfaces of constant $\Phi_{\text{eff}}$. In the orbital plane, these contours look like nested closed loops surrounding each star at low potential values (deep inside each star's gravitational well) that progressively deform and merge as the potential value increases (i.e., as one moves outward). The contour map forms a characteristic **figure-eight** shape at one specific critical potential value — this is the boundary that defines the Roche lobes.

The physical significance of equipotential surfaces is profound: **gas in hydrostatic equilibrium tends to follow equipotential surfaces**. If a star's surface happens to coincide with one of these equipotential surfaces, its shape is determined by the equipotential. If the star expands to fill successively larger equipotentials, it eventually reaches the critical surface — the Roche lobe.

### 2.3 The Lagrangian Points

Points in space where the gradient of the effective potential vanishes — where the net force (gravitational + centrifugal) is zero — are the **Lagrangian points** $L_1$ through $L_5$. These are points of **gravitational equilibrium** in the co-rotating frame.

There are five such points. Three are **collinear** (lying along the axis connecting the two masses) and two are **triangular** (forming equilateral triangles with the two masses):

- **$L_1$ (inner Lagrangian point):** Located **between** the two stars on the line connecting them. It is the point at which the gravitational pulls of $M_1$ and $M_2$, combined with the centrifugal force, exactly cancel. The potential $\Phi_{\text{eff}}$ has a **local maximum** (saddle point in 3D) at $L_1$, meaning it is a point of **unstable equilibrium**. The slightest perturbation causes material to fall toward one star or the other. This instability is precisely what makes $L_1$ the gateway for mass transfer.

- **$L_2$:** Located on the far side of the less massive star $M_2$ along the line connecting the two masses. It is also a local maximum (saddle point) — material at $L_2$ can escape the system entirely.

- **$L_3$:** Located on the far side of the more massive star $M_1$. Also unstable.

- **$L_4$ and $L_5$:** The triangular points, located $60°$ ahead of and behind the secondary in its orbit. These are points of **stable equilibrium** (local potential maxima only in a restricted sense; stability is maintained by Coriolis forces when $M_1/M_2 > 25$). They are less relevant to mass transfer.

In a plot of $\Phi_{\text{eff}}$ versus distance $x/a$ along the axis connecting the two stars, the points $L_1$, $L_2$, and $L_3$ appear as **local maxima** in the potential curve — peaks sitting between the two deep potential wells centred on each star. The potential well of $M_1$ is deeper (because $M_1$ is more massive), and the $L_1$ saddle point is located closer to $M_2$ than to $M_1$ for unequal mass ratios.

---

## 3. The Roche Lobe

### 3.1 Definition and Physical Meaning

The **Roche lobe** of a star is defined as the equipotential surface that passes through the inner Lagrangian point $L_1$. It is the **largest closed equipotential surface** around a given star that is still bound to that star in the gravitational sense.

More physically: the Roche lobe delimits the **region of gravitational dominance** of each star. Within its Roche lobe, a star's own gravity dominates over the companion's gravity (corrected for the co-rotating frame). Material inside the Roche lobe is gravitationally bound to its star. Material that crosses through $L_1$ passes into the Roche lobe of the companion and becomes gravitationally bound to it.

Together, the two Roche lobes share the point $L_1$ as a **common contact point**. In three dimensions, each lobe resembles a teardrop (axially symmetric around the axis between the stars), with its pointed end directed toward $L_1$.

The Roche lobe concept is central to binary stellar evolution because it defines the **maximum size** a star can attain before it begins to transfer mass to its companion. As long as both stars remain entirely within their respective Roche lobes, they evolve independently, as if isolated. Once a star expands to fill its Roche lobe — for instance, as it ascends the giant branch — material at its surface reaches $L_1$ and begins to flow toward the companion. This is **Roche lobe overflow (RLOF)**, the primary mass-transfer mechanism.

### 3.2 Geometry: Approximate Roche Lobe Radii

Because the Roche lobe is a three-dimensional, non-spherical surface, it is characterised by its **effective radius** — the radius of a sphere with the same volume. Two widely used approximate formulae for the effective Roche lobe radii $l_1$ (around the primary $M_1$) and $l_2$ (around the secondary $M_2$) are:

$$l_1 = a \left( 0.5 - 0.227 \log \frac{M_2}{M_1} \right)$$

$$l_2 = a \left( 0.5 + 0.227 \log \frac{M_2}{M_1} \right)$$

with the constraint:

$$l_1 + l_2 = a$$

**Understanding these formulae:**
- When $M_1 = M_2$ (equal masses, mass ratio $M_2/M_1 = 1$): $\log(1) = 0$, so both $l_1 = l_2 = 0.5\,a$. By symmetry, each star's Roche lobe extends exactly halfway to the other star. This is the symmetric case.
- When $M_2 < M_1$ (the usual convention): $\log(M_2/M_1) < 0$, so $l_1 > 0.5\,a$ and $l_2 < 0.5\,a$. The more massive primary has a **larger** Roche lobe; the less massive secondary has a **smaller** Roche lobe. This is intuitive — a more massive star has a stronger gravitational grip on surrounding material.
- The Roche lobe radius depends on **both** $a$ (the orbital separation) and the mass ratio. If $a$ changes (as it does during mass transfer), the Roche lobe radii change correspondingly. This feedback — between orbital evolution and Roche lobe size — is what drives the runaway or self-regulating nature of mass transfer.

The shapes are not spherical. The lobes are deformed into a **drop shape** (teardrop or pear shape) in the direction of $L_1$, elongated toward the partner star. The degree of deformation increases as the mass ratio departs from unity. For very extreme mass ratios, one Roche lobe can be much smaller and more elongated than the other.

---

## 4. Classification of Binary Systems

### 4.1 The Three Morphological Classes

Binary systems are classified based on whether the component stars fill their respective Roche lobes. There are three fundamental classes:

**1. Detached systems:** The radii of **both** components are smaller than their respective Roche lobe radii ($R_1 < l_1$ and $R_2 < l_2$). Neither star fills its Roche lobe. There is no mass transfer through $L_1$. The stars interact gravitationally (causing tidal distortions and orbital circularisation) but evolve essentially **independently**, as single stars. The vast majority of wide binary systems are detached. This phase persists as long as neither star has expanded enough to reach $L_1$.

**2. Semidetached systems:** One component — typically the more evolved (and hence larger) star — has **expanded to fill its Roche lobe** while the other still fits within its own. Mass is actively being transferred through $L_1$ from the lobe-filling star to the companion. By convention, the star that is **losing mass is called the secondary** (even if it was originally the more massive star; the naming reflects current state, not initial conditions). The companion accretes this material. The accreting star may accumulate an **accretion disk** around it if it is compact (see Section 4.2).

**3. Contact systems:** Both components have **expanded to fill, or overflow, their respective Roche lobes**. They share a **common envelope** — a single extended envelope of gas surrounds both stellar cores. The surface of the common envelope follows the outer critical equipotential that passes through $L_2$ and $L_3$. Energy and angular momentum are exchanged through the common envelope. Contact systems are unstable: the common envelope phase is short-lived (on dynamical or thermal timescales, far shorter than nuclear timescales), ending either in the merger of the two cores or in the ejection of the envelope and the emergence of a close compact binary.

### 4.2 Accretion Disks

When material flows through $L_1$ in a semidetached system, it does **not** fall directly onto the accreting star. Instead, it arrives with a specific angular momentum — inherited from the orbital motion of the binary — and forms a **Keplerian accretion disk** around the compact or main-sequence companion. The material in the disk slowly loses angular momentum through viscosity (or magnetic turbulence) and spirals inward, eventually impacting the stellar surface (or the innermost stable orbit in the case of a black hole). Crucially, the **sense of rotation of the accretion disk is the same as the sense of the binary orbit**, since the angular momentum of the infalling stream derives from the orbital angular momentum. Energy is released viscously throughout the disk, making the disk a source of radiation that can span from infrared to X-rays depending on the compactness of the accreting star.

---

## 5. The Role of Stellar Expansion in Mass Transfer

### 5.1 Evolutionary Stages and Binary Interaction

The key physical condition for Roche lobe overflow is that a star must **expand** sufficiently to fill its Roche lobe. Not all evolutionary phases lead to significant expansion; the ones that do are:

- **Subgiant Branch (SGB) / Red Giant Branch (RGB):** After core hydrogen exhaustion, the star develops an inert helium core and a hydrogen-burning shell. The envelope expands dramatically as the star ascends the RGB, increasing its radius by factors of tens to hundreds compared to its main-sequence radius. A star on the RGB can easily overfill its Roche lobe in a binary system with moderate separation.

- **Asymptotic Giant Branch (AGB):** After core helium exhaustion, a star with $M \lesssim 8\,M_\odot$ develops a degenerate carbon-oxygen core and ascends the AGB, expanding to even larger radii than on the RGB. AGB stars are among the largest stars known, making AGB-phase RLOF common in wide binaries.

- **Post-MS expansion in massive stars:** Massive stars ($M \gtrsim 10\,M_\odot$) evolve rapidly off the MS and can expand to supergiant radii on nuclear or thermal timescales.

The **size** of the star at each evolutionary stage is therefore the key parameter controlling when and whether mass transfer occurs. Stars on the MS are compact and typically remain within their Roche lobes. Stars on the giant branches are extended and susceptible to RLOF. This is why binary interactions tend to be concentrated at specific, well-defined evolutionary phases.

### 5.2 Blue Straggler Stars — Rejuvenation Through Mass Transfer

**Blue Straggler Stars (BSS)** are stars observed in old stellar populations (globular clusters, open clusters, the Galactic halo) that appear **brighter and bluer than the main-sequence turn-off point** of the host population. In a purely single-star population of age $t$, the MS-TO defines the most luminous, hottest stars still on the MS — any star brighter than the TO must have already evolved off. Blue stragglers violate this rule: they appear to be younger, more massive MS stars in a population where no such stars should exist.

The binary explanation for blue stragglers is **mass transfer rejuvenation:** a star in a binary receives mass from its companion (the primary star, ascending the RGB or AGB). The accreted mass adds fresh hydrogen to the envelope and, if the mass transfer is sufficiently large, can reignite or prolong MS hydrogen burning. The star's position in the CMD shifts upward and to the left (bluer and more luminous), mimicking a younger, more massive single star. The "old" star has been **rejuvenated** by binary interaction.

Alternatively, BSS can form through the **direct merger** of two MS stars in a contact binary: the combined star is more massive than either component and settles onto the MS at a position appropriate for its new, higher mass. In both channels (mass transfer and merger), the binary interaction is the essential ingredient. The existence of blue stragglers in clusters is therefore direct, observational proof that binary interactions occur and have significant demographic consequences.

---

## 6. Angular Momentum and Orbital Dynamics

### 6.1 The Reduced Mass Formalism

To analyse how the orbit evolves during mass transfer, one employs the **reduced mass** formalism. For two bodies with masses $M_1$ and $M_2$, the **reduced mass** is:

$$\mu = \frac{M_1 M_2}{M_1 + M_2}$$

The reduced mass has units of mass ($M_\odot$ in stellar applications). It represents the effective single-body mass in the equivalent one-body problem: the two-body orbital problem is mathematically equivalent to a single particle of mass $\mu$ orbiting in the combined gravitational field of the total mass $M = M_1 + M_2$ concentrated at the origin. This simplification is extremely useful because all the standard results of Keplerian mechanics — energy, angular momentum, orbital period — can be expressed in terms of $\mu$, $M$, and the orbital parameters $a$ and $e$.

The total orbital **angular momentum** of the system is:

$$L = \mu \sqrt{GM\,a(1 - e^2)}$$

where $G$ is Newton's gravitational constant, $a$ is the semi-major axis, and $e$ is the orbital eccentricity. This is the fundamental quantity that must be tracked when mass transfer or mass loss occurs.

### 6.2 Derivation of the Angular Momentum Formula

The formula $L = \mu \sqrt{GMa(1-e^2)}$ is derived from the geometry of Keplerian orbits using conservation of energy and angular momentum at the two turning points of the orbit — **perihelion** (closest approach) and **aphelion** (farthest point):

- Perihelion distance: $r_p = a(1-e)$
- Aphelion distance: $r_a = a(1+e)$

At both turning points, the velocity is perpendicular to the radius vector, so angular momentum is purely $L = \mu\,r\,v$. Conservation of angular momentum gives:

$$\frac{v_p}{v_a} = \frac{r_a}{r_p} = \frac{1+e}{1-e}$$

The faster the star moves at perihelion compared to aphelion, the more eccentric the orbit. Using energy conservation between perihelion and aphelion (total energy is conserved = kinetic + potential), one can solve for $v_p$:

$$v_p^2 = \frac{GM}{a} \frac{1+e}{1-e}$$

Substituting into $L = \mu\,r_p\,v_p = \mu\,a(1-e)\,v_p$ yields the standard result. For a **circular orbit** ($e = 0$), this reduces to $L = \mu\sqrt{GMa}$, and $v_p = v_a = \sqrt{GM/a}$ is the constant circular orbital speed.

### 6.3 Conservative Mass Transfer: Orbital Evolution

The most important idealized case is **conservative mass transfer**, meaning:

1. **No mass is lost from the system:** $dM/dt = 0$, i.e., $\dot{M}_1 + \dot{M}_2 = 0$, which implies $\dot{M}_1 = -\dot{M}_2$.
2. **No angular momentum is lost from the system:** $dL/dt = 0$.

In reality, some mass and angular momentum escape (through stellar winds, jets, or radiation-driven outflows), but the conservative case is the essential baseline that reveals the fundamental direction of orbital evolution.

For a circular orbit ($e = 0$), the angular momentum is:

$$L = \mu \sqrt{GMa}$$

Differentiating with respect to time and setting $dL/dt = 0$:

$$0 = \sqrt{GM} \left( \frac{d\mu}{dt}\sqrt{a} + \frac{\mu}{2\sqrt{a}}\frac{da}{dt} \right)$$

Dividing through by $\mu\sqrt{GMa}$:

$$0 = \frac{1}{\mu}\frac{d\mu}{dt} + \frac{1}{2a}\frac{da}{dt}$$

Rearranging:

$$\frac{1}{a}\frac{da}{dt} = -\frac{2}{\mu}\frac{d\mu}{dt}$$

This equation tells us that the **fractional rate of change of the orbital separation is determined by the fractional rate of change of the reduced mass**. To use this, we need to compute $d\mu/dt$ explicitly.

### 6.4 Computing the Time Derivative of the Reduced Mass

Starting from $\mu = M_1 M_2 / M$ with $M = M_1 + M_2 = \text{const}$ (conservative assumption):

$$\frac{d\mu}{dt} = \frac{1}{M}\frac{d(M_1 M_2)}{dt} = \frac{1}{M}\left(\dot{M}_1 M_2 + M_1 \dot{M}_2\right)$$

Applying the conservative condition $\dot{M}_2 = -\dot{M}_1$:

$$\frac{d\mu}{dt} = \frac{1}{M}\left(\dot{M}_1 M_2 - M_1 \dot{M}_1\right) = \frac{\dot{M}_1(M_2 - M_1)}{M}$$

Substituting into the orbital separation equation:

$$\frac{1}{a}\frac{da}{dt} = -\frac{2}{\mu}\cdot\frac{\dot{M}_1(M_2 - M_1)}{M} = \frac{2\dot{M}_1(M_1 - M_2)}{M_1 M_2}$$

(using $\mu = M_1 M_2/M$ in the denominator). This is the **key orbital evolution equation for conservative mass transfer**:

$$\boxed{\frac{1}{a}\frac{da}{dt} = \frac{2\dot{M}_1(M_1 - M_2)}{M_1 M_2}}$$

The sign and magnitude of $da/dt$ — whether the orbit shrinks or expands — depends entirely on the **sign of $\dot{M}_1$ and the sign of $(M_1 - M_2)$**, i.e., on who is transferring mass and whether the mass-losing star is currently more or less massive than the companion.

### 6.5 Orbital Frequency Evolution

The **orbital angular frequency** $\omega$ is related to $a$ and $M$ via **Kepler's third law**:

$$\omega^2 = \frac{G(M_1 + M_2)}{a^3} = \frac{GM}{a^3}$$

Taking the logarithmic time derivative (and noting that $M$ is constant in the conservative case):

$$\frac{2\dot{\omega}}{\omega} = -\frac{3\dot{a}}{a}$$

$$\frac{1}{\omega}\frac{d\omega}{dt} = -\frac{3}{2}\frac{1}{a}\frac{da}{dt}$$

If $a$ decreases ($\dot{a} < 0$), then $\omega$ increases — the stars orbit each other **faster**. If $a$ increases, $\omega$ decreases — the orbit slows. This is the direct link between orbital separation and period: shrinking orbits have shorter periods, and expanding orbits have longer periods.

---

## 7. Feedback Mechanisms in Mass Transfer

### 7.1 The Two Cases and Their Sign Analysis

The orbital evolution equation $\frac{1}{a}\frac{da}{dt} = \frac{2\dot{M}_1(M_1 - M_2)}{M_1 M_2}$ yields **qualitatively different outcomes** depending on the masses and the direction of transfer. There are two instructive cases to analyse.

**Recall the sign convention:** $M_1$ is the star currently losing mass (in RLOF, $\dot{M}_1 < 0$ if $M_1$ donates and $\dot{M}_1 > 0$ if $M_1$ accretes). The factor $(M_1 - M_2)$ simply compares the current masses of the two components.

### 7.2 Example 1 — Primary Fills Roche Lobe First ($M_1 > M_2$)

In the most natural scenario, the **more massive primary** $M_1$ evolves faster (more massive stars have shorter nuclear timescales) and expands to fill its Roche lobe first. It therefore begins transferring mass to the less massive secondary $M_2$.

Applying the formula:
- $\dot{M}_1 < 0$ (primary is losing mass)
- $(M_1 - M_2) > 0$ (primary is still more massive at the start of transfer)
- Therefore $\frac{da}{dt} \propto \dot{M}_1 \cdot (M_1 - M_2) < 0$ — the separation **decreases**

The physical interpretation: as mass flows from the more massive to the less massive star, the orbit **shrinks**. The two stars move closer together. As $a$ decreases, the Roche lobe radius $l_1 \propto a$ also decreases. The donor star was already filling its Roche lobe; now the Roche lobe has become even smaller. The star still needs to fit inside a shrinking Roche lobe, which forces **more** mass to overflow — the transfer accelerates. This is a **positive feedback** (runaway) mechanism.

The runaway proceeds until the mass ratio inverts ($M_1 = M_2$, then $M_1 < M_2$). Once the originally more massive star has transferred enough mass to become the **less massive** of the two, the factor $(M_1 - M_2)$ changes sign, and the orbital evolution reverses — $a$ begins to increase and the feedback becomes negative (self-regulating). The system finds a stable mass-transfer regime. The outcome of this process is a transformed system: one star has lost most of its envelope (leaving, for instance, a helium core), and the other has gained mass, potentially appearing as a **blue straggler** if it has been pushed up the MS.

### 7.3 Example 2 — Accretion onto a White Dwarf ($M_1$ is a WD)

Consider a system where the originally more massive primary has already completed its evolution and become a **white dwarf** $M_1$ (WD). The secondary $M_2$ is now the evolving star. As $M_2$ ascends the RGB or AGB, it expands and eventually fills its own Roche lobe, initiating mass transfer **to** the WD. In this notation, $\dot{M}_1 > 0$ (the WD is gaining mass from the secondary).

**Sub-case A: $M_1 > M_2$ (WD is more massive than the donor)**
- $\dot{M}_1 > 0$ (WD accreting)
- $(M_1 - M_2) > 0$
- $\frac{da}{dt} \propto (+)(+) > 0$ — separation **increases** (**negative feedback / self-regulating**)

As the orbit expands, the Roche lobe radius of $M_2$ grows. The donor star does not need to fill as large a volume — the overflow rate decreases. The system naturally **self-regulates**. This leads to stable, sustained accretion at moderate rates, the hallmark of cataclysmic variables with stable disks.

**Sub-case B: $M_1 < M_2$ (WD is less massive than the donor)**
- $\dot{M}_1 > 0$ (WD accreting)
- $(M_1 - M_2) < 0$
- $\frac{da}{dt} \propto (+)(-) < 0$ — separation **decreases** (**positive feedback / runaway**)

The orbit shrinks, the donor's Roche lobe shrinks, the overflow rate increases in a runaway. This leads to rapidly increasing mass-transfer rates onto the WD. The high accretion rate may drive a **nova eruption** (if the rate is in the right range) or, ultimately, push the WD toward the Chandrasekhar mass and trigger a **Type Ia supernova**.

The sign of the feedback is therefore a critical predictor of the long-term fate of the system and the type of transient phenomenon it produces.

---

## 8. Accretion Energetics

### 8.1 Energy Released by Accretion

When material falls from large distances (effectively from infinity, or from the Roche lobe overflow region) onto a compact star, it releases **gravitational potential energy** as kinetic energy upon impact. For a mass element $m$ falling onto a star of mass $M$ and radius $R$, the kinetic energy at the stellar surface is:

$$K = \frac{GMm}{R}$$

This is the energy per unit mass $m$ (here, $K$ scales linearly with $m$). The amount of energy released depends critically on the **compactness** of the accreting object (how small $R$ is for a given $M$). More compact objects release vastly more energy per unit accreted mass.

**Numerical estimates for $m = 1$ g:**

- **White dwarf** ($M \approx 0.85\,M_\odot$, $R \sim 0.01\,R_\odot$): $K \approx 10^{17}$ erg per gram
- **Neutron star** ($M \approx 1.4\,M_\odot$, $R \sim 10$ km): $K \approx 10^{20}$ erg per gram — approximately **30 times larger** than the energy released by hydrogen burning ($\sim 6 \times 10^{18}$ erg/g)

The neutron star figure is remarkable: **gravitational accretion onto a neutron star is 30 times more efficient than hydrogen nuclear burning**. This explains why X-ray binaries with neutron stars are among the most luminous steady-state sources in the galaxy.

### 8.2 Accretion Efficiency Compared to Nuclear Burning

Accretion efficiency is often expressed as a fraction of $mc^2$, the maximum possible energy release (rest mass energy). Nuclear burning of hydrogen to helium releases approximately $0.7\%$ of the rest mass energy:

$$\epsilon_\text{nuc} \approx 0.007\,mc^2$$

In contrast, the efficiencies for accretion onto compact objects are:

| Accretor | Efficiency |
|---|---|
| Black hole (non-spinning) | $\sim 0.1\,mc^2$ |
| Black hole (maximally spinning) | $\sim 0.42\,mc^2$ |
| Neutron star | $\sim 0.15\,mc^2$ |
| White dwarf | $\sim 0.00025\,mc^2$ |
| H nuclear burning | $0.007\,mc^2$ |

These comparisons make clear the energy hierarchy: accreting onto a neutron star or black hole releases far more energy per unit mass than nuclear burning. White dwarf accretion, while less efficient, still plays a crucial role because the accreted hydrogen can trigger surface thermonuclear reactions (novae) that produce brief but extremely luminous outbursts.

---

## 9. Novae and Cataclysmic Variables

### 9.1 Cataclysmic Variables

**Cataclysmic variables (CVs)** are a class of close binary systems consisting of a **white dwarf** accreting from a low-mass donor (typically a late K or M dwarf filling its Roche lobe). The accretion rate for classical CVs is very low:

$$\dot{M} \sim 10^{-11}\,M_\odot\,\text{yr}^{-1}$$

At these rates, the accreted material settles onto the WD surface and accumulates in a thin shell. The slowly growing envelope is not hot or dense enough to ignite; instead, the system shows quasi-periodic brightening events (dwarf novae) driven by thermal instabilities in the accretion disk. These disk instabilities — not nuclear reactions — cause the optical outbursts. The underlying WD and the quiescent disk are visible in the inter-outburst phases.

### 9.2 Classical Novae

**Classical novae** occur at higher accretion rates:

$$\dot{M} \sim 10^{-8}$$ to $$10^{-9}\,M_\odot\,\text{yr}^{-1}$$

At these rates, hydrogen accumulates on the WD surface more rapidly. The key physical process is that the accreted layer becomes **electron-degenerate** before it can ignite. Because degenerate material has a pressure that is independent of temperature, raising the temperature does not cause expansion and cooling; instead, energy is deposited at constant density. The temperature rises without bound until the hydrogen shell becomes hot enough to ignite via the **CNO cycle** (a temperature-sensitive nuclear burning pathway that dominates over the proton-proton chain at $T \gtrsim 2 \times 10^7$ K).

The ignition of degenerate hydrogen leads to a **thermonuclear runaway (H-flash)**:
1. The accreted shell accumulates to a critical mass of approximately $\sim 10^{-4}\,M_\odot$ before conditions for ignition are met.
2. Ignition of the CNO cycle releases energy rapidly, raising the temperature.
3. Because the layer is degenerate, rising temperature does not increase pressure and expand the layer — the burning proceeds at nearly constant density, causing the temperature to skyrocket (a runaway).
4. When the temperature becomes high enough, the degeneracy is lifted (matter becomes non-degenerate again), and the sudden pressure increase causes the outer layers to expand explosively.
5. The expanding layers are ejected at speeds of $\sim 10^3$ km/s, producing the characteristic nova shell observable in the sky as a rapidly brightening optical source.

After the eruption, the WD retains its mass (minus the ejected shell), and accretion from the companion resumes. The cycle **repeats** on a timescale of $10^4$–$10^5$ years, making novae **recurrent transients**. It is important to note that a classical nova is not the destruction of the WD — it is a surface explosion that the WD survives.

---

## 10. Type Ia Supernovae

### 10.1 The Chandrasekhar Limit and WD Ignition

**Type Ia supernovae** represent the most energetic endpoint of WD accretion. The underlying physics involves the **Chandrasekhar mass** $M_\text{Ch} \approx 1.4\,M_\odot$ — the maximum mass a cold, non-rotating white dwarf can have before electron degeneracy pressure can no longer support it against gravitational collapse.

When accretion on a WD (or the merger of two WDs) drives its total mass toward $M_\text{Ch}$, the central density increases to the point where **carbon ignition** occurs in the degenerate core. Carbon burning in a degenerate environment, just like hydrogen burning in the nova scenario, proceeds as a thermonuclear runaway: the energy released raises the temperature without lifting the degeneracy (initially), driving the burning rate higher and higher. Within a fraction of a second, the entire WD is consumed in a **thermonuclear explosion** — a Type Ia supernova.

The explosion releases $\sim 10^{51}$ erg of energy (the canonical "foe"), synthesising roughly $0.5\,M_\odot$ of radioactive ${}^{56}$Ni, whose decay powers the light curve. Because the explosion always involves a WD near the Chandrasekhar mass, Type Ia supernovae are thought to be standardisable candles — their intrinsic luminosities (corrected via the Phillips relation for light-curve width) are nearly uniform, making them crucial tools for measuring cosmological distances.

### 10.2 The Binary Connection and Post-Explosion Fate

The Type Ia progenitor system is binary: either a WD accreting from a non-degenerate companion (**single-degenerate channel**) or two WDs merging (**double-degenerate channel**). In the single-degenerate channel, sustained accretion at rates of $10^{-7}$–$10^{-6}\,M_\odot\,\text{yr}^{-1}$ allows the WD to grow toward $M_\text{Ch}$ without ejecting too much mass via novae.

A critical and non-obvious point: **SN explosions do not necessarily destroy the binary system**. If the companion star survives the explosion — possible if it is a main-sequence or subgiant star that is not engulfed by the ejecta — the binary system may continue to exist post-explosion, albeit in a very different configuration. This is relevant not just for Type Ia SNe but for any SN in a binary (see Section 11). The criteria for system survival after a sudden mass-loss event are examined next.

---

## 11. Survival of Binaries After Supernova Explosions

### 11.1 The Binding Energy Criterion

When one component of a binary explodes as a supernova, it **instantaneously ejects mass** $\delta m$. This sudden mass loss changes the total mass of the system, altering the gravitational potential and the energy budget of the orbit. If too much mass is ejected too quickly, the two components no longer have enough binding energy to remain gravitationally bound — the system is disrupted and the two objects fly apart as runaway stars.

The condition for the system to remain bound can be derived from the orbital energy. Before the explosion, with masses $M_1$ and $M_2$ and separation $a$, the total orbital energy is negative (bound). After instantaneous ejection of $\delta m$ from one component, the masses are $M_1' = M_1 - \delta m$ and $M_2$. The orbital velocity at the moment of explosion is assumed unchanged (instantaneous explosion approximation). The system remains bound if the total post-explosion energy $E' < 0$.

The resulting **binding condition** is:

$$\delta m < \frac{M_1 + M_2}{2}$$

**Physical interpretation:** The ejected mass must be **less than half the total pre-explosion system mass**. If more than half the total mass is ejected, the remnant system is unbound. The factor of one-half comes directly from comparing the kinetic energy of the orbital motion (which was appropriate for the pre-explosion masses) with the gravitational binding energy of the post-explosion system.

This criterion has profound implications: massive stars with initial masses $M_1 \gg M_2$ that eject large amounts of mass in a Type II SN may disrupt the binary. Conversely, if the exploding star has already lost most of its envelope through RLOF (leaving only a helium core), the ejected mass in the SN may be small enough to satisfy the criterion — the binary survives. This is one reason why Case A and Case B mass transfer (which strip the envelope before the SN) are so important for producing bound NS or BH + companion systems.

---

## 12. Detailed Evolutionary Case Study — Blue Supergiant + Black Hole Binary

### 12.1 Initial Configuration and Step-by-Step Evolution

The following case study illustrates the full evolutionary pathway from a ZAMS binary to an X-ray binary system, demonstrating how each physical process described above operates in sequence. The example uses a representative pair:

- **Initial state:** $M_1 = 20\,M_\odot$ (primary), $M_2 = 6\,M_\odot$ (secondary). Orbital period $P = 4.4$ days. Both stars begin on the zero-age main sequence. The separation is small enough that the primary will fill its Roche lobe during its post-MS expansion.

**Step 1 — Post-MS evolution of $M_1$ and onset of RLOF:**
The primary ($M_1 = 20\,M_\odot$) exhausts its core hydrogen first (massive stars evolve faster). It expands as a subgiant/supergiant, and its radius eventually fills the Roche lobe. Conservative mass transfer begins: $M_1$ donates mass to $M_2$ through $L_1$.

**Step 2 — Outcome of mass transfer phase:**
The mass transfer is rapid (positive feedback initially, since $M_1 > M_2$), then self-regulating. The primary loses most of its hydrogen envelope, leaving behind its helium core. The secondary gains the transferred mass. Final masses: $M_1 \rightarrow 5.4\,M_\odot$ (He core), $M_2 \rightarrow 20.6\,M_\odot$ (now the more massive star). The orbital period has changed to $P = 5.2$ days (the orbit widened when $M_1 < M_2$ at late stages of transfer).

**Step 3 — Core collapse of $M_1$ and formation of a black hole:**
The $5.4\,M_\odot$ helium core of $M_1$ completes nuclear burning and collapses in a **Type II supernova**. The SN ejects $3.4\,M_\odot$, leaving a **$2\,M_\odot$ black hole** remnant. At this point, the binary satisfies the survival criterion: the ejected mass ($3.4\,M_\odot$) must be compared to half the total pre-SN mass ($\sim 0.5 \times (5.4 + 20.6) = 13\,M_\odot$). Since $3.4 < 13$, the system remains bound (with a changed orbital period). New period: $P = 5.9$ days.

**Step 4 — Detached phase: BH + MS star, wind accretion:**
The system is now a black hole ($2\,M_\odot$) + main-sequence/subgiant star ($M_2 = 20.6\,M_\odot$). The MS star has not yet filled its Roche lobe — the system is detached. However, the massive star $M_2$ drives a powerful stellar wind. The BH captures a fraction of this wind and **accretes it**, releasing gravitational energy. Because the BH is extremely compact, this accretion releases copious X-rays: the system becomes an **X-ray binary** (specifically a high-mass X-ray binary, HMXB, given the mass of $M_2$). The stellar wind material falls into the BH potential well, forming a partial accretion disk or direct accretion flow, and the system is observable in X-rays.

**Step 5 — Roche lobe overflow of $M_2$:**
Eventually $M_2$ leaves the MS and expands to giant/supergiant dimensions, filling its own Roche lobe. Now RLOF begins from $M_2$ to the BH: mass flows through $L_1$ and forms a full **accretion disk** around the BH. The increased accretion rate produces even more luminous emission. The disk can emit across a wide spectrum — UV, optical, and X-rays — depending on the local temperature profile (inner regions near the BH are hottest, emitting X-rays; outer disk regions are cooler, emitting optical and UV light).

### 12.2 Key Lessons from the Case Study

This step-by-step scenario illustrates several important principles simultaneously:

1. **Sequential evolution:** In a binary, the more massive star always evolves first. Its evolution directly affects the companion — first through mass transfer (changing $M_2$'s position on the CMD) and later through the SN (producing the compact object that will accrete from $M_2$).

2. **Role of mass transfer in shaping the SN progenitor:** Without RLOF stripping $M_1$'s envelope, $M_1$ would have exploded with a much larger mass, potentially ejecting enough mass to disrupt the system. The prior RLOF phase ensures that only the helium core ($5.4\,M_\odot$) explodes, making the ejected mass small enough for the system to survive.

3. **Multiple accretion phases:** The system goes through two distinct X-ray emission phases — first wind accretion (quiescent, moderate luminosity) and then RLOF accretion (brighter, with a full disk). Real HMXBs often show both phases depending on the evolutionary state of the companion.

---

## 13. Extreme Case — Common Envelope from Brown Dwarf Companion (HS 2231+2441)

### 13.1 The System and Its History

The system **HS 2231+2441** is a striking example of binary interaction taken to an extreme, often described as "the brown dwarf that killed its brother." It consists of a **brown dwarf** (BD) with mass $\sim 40\,M_J$ ($M_J$ = Jupiter mass) and a **$\sim 1\,M_\odot$ star** that has been reduced to a low-mass helium white dwarf. The system is extremely compact:

- Orbital period: $P = 0.1$ days ($\sim 2.4$ hours)
- Orbital separation: $a \approx 0.6\,R_\odot$

This period is far shorter than any main-sequence binary and implies that the two objects are separated by less than the radius of the Sun.

### 13.2 The Common Envelope Phase and Its Outcome

The extreme compactness of the current orbit cannot be a primordial configuration — it is a product of dramatic orbital shrinkage during a **common envelope (CE) phase**. The evolutionary history was:

1. **Initial system:** A $\sim 1\,M_\odot$ star orbited by a much less massive brown dwarf at a much wider separation. The brown dwarf's mass ($\sim 40\,M_J$) is far below the hydrogen-burning minimum mass ($\sim 80\,M_J$), so it cannot be a star in any conventional sense.

2. **RGB expansion of the $1\,M_\odot$ star:** As the star ascended the red giant branch, its radius expanded dramatically — reaching tens to hundreds of solar radii. At some point, the expanding giant **engulfed** the brown dwarf entirely. The brown dwarf was now orbiting inside the extended envelope of the giant: a common envelope configuration.

3. **Orbital energy dissipation:** Inside the envelope, the brown dwarf experienced **drag** from the surrounding gas. This drag extracted orbital energy from the BD's orbit and deposited it into the giant's envelope. The BD spiralled inward as it lost orbital energy, converting gravitational potential energy into thermal energy of the envelope.

4. **Envelope ejection:** If enough orbital energy was deposited into the envelope, the envelope could become gravitationally unbound and be ejected. The BD's inward spiral continued until either the BD merged with the core, or enough energy was released to eject the envelope before the merger. In this case, the envelope was ejected, and the BD **survived** — barely. What remained was the **naked helium core** of the giant (now a low-mass He WD) and the BD in a very tight orbit at $\sim 0.6\,R_\odot$.

5. **The naming:** The BD "killed its brother" in the sense that, by spiralling through the envelope and ejecting it, it stripped the companion of its outer layers, preventing it from ever completing RGB or AGB evolution to become a normal carbon-oxygen WD. The remnant is a low-mass He WD — an object that would not normally form from a $1\,M_\odot$ single star (which would produce a C-O WD), but which forms when the RGB evolution is cut short by envelope stripping.

### 13.3 Physical Significance

The HS 2231+2441 system illustrates the **common envelope mechanism** in a particularly dramatic way. It demonstrates that:

- Even objects well below the stellar mass limit (brown dwarfs, possibly planets) can dramatically alter stellar evolution if they are sufficiently close.
- Common envelope phases are extremely effective at shrinking orbits — from wide initial separations to $\sim 0.6\,R_\odot$ in a single interaction.
- The common envelope interaction can produce compact binary remnants (close WD + companion systems) that are the progenitors of cataclysmic variables and, in more massive versions, of neutron star or black hole binaries.
- The outcome depends sensitively on the energy budget: whether the orbital energy released is sufficient to unbind the envelope determines whether the BD merges or survives.

---

## 14. Summary of Key Concepts and Connections

### 14.1 The Central Thread

The physics of binary systems revolves around one core concept: **stars in binaries do not evolve in isolation**. The evolutionary clock of each component triggers interactions — through RLOF, common envelopes, SN explosions, and accretion — that feed back onto both partners and the orbit.

The central quantitative tool is the **orbital evolution equation** under conservative mass transfer:

$$\frac{1}{a}\frac{da}{dt} = \frac{2\dot{M}_1(M_1 - M_2)}{M_1 M_2}$$

The sign of this equation determines whether each mass-transfer episode drives the stars together (positive feedback, potentially runaway) or apart (negative feedback, self-regulating). The direction depends entirely on the mass ratio and which star is currently the donor.

### 14.2 Connections Between Topics

- The **Roche lobe radius** ($l \propto a$) links orbital evolution directly to mass transfer: if $a$ shrinks, the Roche lobe shrinks, forcing more mass through $L_1$.
- The **accretion energetics** determine what type of observable is produced: low accretion rates → CVs, moderate rates → novae, high rates (sustained, on WD near $M_\text{Ch}$) → Type Ia SN, accretion onto NS/BH → X-ray binaries.
- The **SN survival criterion** ($\delta m < M_\text{tot}/2$) connects the prior mass-transfer history (which determines how much mass the exploding star has left) to whether the post-SN binary remains bound and can produce an X-ray binary or recycled pulsar.
- **Blue stragglers** are the optical-wavelength observational signature of mass transfer in old populations — direct proof that binary interactions occur on observable timescales.
- The **common envelope phase** is the mechanism that converts wide binaries into the very tight configurations needed to produce cataclysmic variables, Type Ia SN progenitors, and compact NS/BH binaries. Without the CE, there would be no pathway from the wide initial orbits (needed to let both stars evolve) to the tight current orbits of interacting systems.
