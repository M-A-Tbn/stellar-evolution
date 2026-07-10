# Supernovae & Neutron Stars — Study Notes (Part 2)
**Source:** `28.SNe+NS_hifi.md` | **Session:** Supernovae & Neutron Stars | **Date:** 2026-05-23

---

## 11. Pulsars: The Observational Manifestation of Neutron Stars

### 11.1 Discovery and Initial Properties

Pulsars (Pulsating Sources of Radio) were discovered in 1967 by Jocelyn Bell as a persistent, extremely regular radio signal that initially appeared to be an instrumental artifact. The signal was so precise that it was briefly catalogued as LGM ("Little Green Men") — a tentative signal from an extraterrestrial civilization — before the astrophysical interpretation was established.

The main observed characteristics of pulsars:

1. **Very short periods**: Most pulsars have periods between $0.2$ and $2$ seconds. The longest known period is $4.3$ s; the shortest is $0.0016$ s ($1.6$ ms). The extreme regularity and short period immediately pointed to a compact, massive object — no star of normal dimensions could rotate at millisecond periods without being torn apart by centrifugal forces.

2. **Extremely regular period**: Pulsar periods are stable to $\sim 10^{-17}$ s — among the most precise natural clocks known. This ruled out binary orbital motion (which would introduce Doppler shifts) and confirmed the rotation interpretation.

3. **Gradual period increase**: All pulsars slow down over time. The rate of period increase is the **period derivative**:

$$\dot{P} = \frac{dP}{dt} \quad \text{(dimensionless, typically } \dot{P} \sim 10^{-15}\text{)}$$

This secular slowdown reflects the loss of rotational kinetic energy to electromagnetic radiation. A **characteristic age** (spindown age) can be defined:

$$\tau = \frac{P}{\dot{P}} \sim 10^7\ \text{yr}$$

This is an order-of-magnitude estimate of the pulsar's age. Note that this estimate assumes the initial period was much shorter than the current one, which is generally true for young pulsars. For recycled pulsars (see Section 13), this assumption breaks down.

### 11.2 The Connection to Supernova Remnants: The Crab Pulsar

The interpretation of pulsars as rapidly rotating neutron stars, and their connection to supernovae, was established through studies of the **Crab Nebula** — the remnant of a supernova observed in AD 1054. The Crab Pulsar has:

$$P_\text{crab} = 0.0333\ \text{s} \quad (\dot{P} = 4 \times 10^{-13})$$

The very short period of the Crab Pulsar (33 milliseconds) requires an object far denser than a white dwarf to avoid rotational disruption, strongly supporting the neutron star hypothesis.

The Crab Nebula emits **synchrotron radiation** — radiation produced by relativistic electrons spiraling along magnetic field lines. As electrons follow helical paths around field lines, they emit a cone of radiation in the forward direction (the relativistic headlight effect; see Section 11.5). The synchrotron radiation from the Crab Nebula requires a continuous injection of highly relativistic electrons. The energy source for this injection is the **rotational kinetic energy** of the Crab Pulsar.

The rotational kinetic energy is:

$$K = \frac{1}{2}I\omega^2 = \frac{2\pi^2 I}{P^2}$$

For a NS with $M = 1.4\,M_\odot$ and $R = 10^6$ cm:

$$I = \frac{2}{5}MR^2 = \frac{2}{5} \times 1.4 \times 2 \times 10^{33} \times 10^{12} = 10^{45}\ \text{g\,cm}^2$$

The rate of energy loss from spindown:

$$\frac{dK}{dt} = -\frac{4\pi^2 I \dot{P}}{P^3}$$

Substituting the Crab values ($P = 0.033$ s, $\dot{P} = 4 \times 10^{-13}$):

$$\frac{dK}{dt} = 5 \times 10^{38}\ \text{erg\,s}^{-1}$$

This is **exactly the luminosity required to power the Crab Nebula's synchrotron emission**. This quantitative agreement constitutes the definitive proof that the Crab Nebula is powered by the rotational energy of its central pulsar (rotating neutron star). No other energy source can explain the nebular luminosity at this level.

The total rotational energy reservoir:

$$K = \frac{2\pi^2 I}{P^2} = \frac{20 \times 1.1 \times 10^{45}}{(0.033)^2} = 1.2 \times 10^{48}\ \text{erg}$$

At the observed energy-loss rate ($5 \times 10^{38}$ erg s$^{-1}$), the Crab Pulsar can power the nebula for approximately:

$$t \approx \frac{1.2 \times 10^{48}}{5 \times 10^{38}} \approx 2.4 \times 10^9\ \text{s} \approx 75\ \text{yr}$$

This timescale is consistent with the nebula's current observed age of approximately $\sim 1000$ years (the SN was observed in 1054 AD), given that the energy loss rate was higher in the past when the pulsar was spinning faster.

### 11.3 The Pulsar Emission Mechanism

The emission of radiation from pulsars is the least well-understood aspect of pulsar physics, but the broad outlines are established.

The rapidly rotating, strongly magnetized neutron star induces a **huge electric field** at its surface through the changing magnetic flux. The induced surface electric field ($\sim 10^8$ statvolts cm$^{-1}$) exceeds the gravitational force at the NS surface by many orders of magnitude. As a result, charged particles (electrons and ions) are **ripped from the surface** of the NS.

These particles are immediately accelerated to relativistic speeds by the induced electric field. As relativistic electrons follow curved magnetic field lines, they emit **curvature radiation** in the form of **gamma-ray photons**. Each gamma-ray photon carries sufficient energy to spontaneously convert into an electron-positron pair:

$$\gamma \rightarrow e^+ + e^-$$

The newly produced electrons are themselves accelerated, produce more gamma rays, which produce more pairs, and so on. This **cascade of pair production** generates a coherent beam of relativistic particles and radiation that constitutes the observed radio pulse emission.

### 11.4 The Magnetosphere and the Light Cylinder

All charged particles torn from the NS surface form a co-rotating halo called the **magnetosphere**. The magnetosphere is locked to the NS rotation — the particles are forced to rotate with the pulsar. However, the co-rotation velocity of a particle at radius $r$ is $v = \omega r$. At some radius, this velocity equals $c$ — the speed of light. No physical particle can exceed $c$, so the magnetosphere cannot extend beyond this critical radius.

The **Light Cylinder** is defined as the surface at which co-rotation would require $v = c$:

$$R_\text{lc} = \frac{c}{\omega} = \frac{cP}{2\pi}$$

where $P$ is the pulsar period and $c$ is the speed of light. For the Crab Pulsar ($P = 0.033$ s): $R_\text{lc} = c \times 0.033 / (2\pi) \approx 1.6 \times 10^8$ cm $= 1{,}600$ km.

Magnetic field lines that close within the light cylinder trap particles in closed loops. Field lines that cross the light cylinder boundary **become open** — they extend to infinity, and particles flowing along them escape the system entirely. These open field lines originate from the magnetic poles. The particles accelerated along open field lines are lost from the NS, carrying away both energy and angular momentum. This is the primary braking mechanism (see Section 12.1).

Emission occurs at two locations: (1) from the light cylinder boundary where the magnetic field configuration changes, and (2) from the **magnetic poles**, where open field lines originate and where the pair-cascade emission is most intense.

### 11.5 The Headlight Effect and Lighthouse Emission

The pulsar emission is concentrated into a **narrow beam** due to two physical effects.

First, the **relativistic headlight effect**: in special relativity, when a source moves relativistically relative to an observer, radiation that is emitted isotropically in the source rest frame is seen to be beamed forward in the observer's frame. The velocity transformation relations are:

$$v_x = \frac{v'_x + u}{1 + \frac{u v'_x}{c^2}}, \quad v_y = \frac{v'_y \sqrt{1 - u^2/c^2}}{1 + \frac{u v'_x}{c^2}}$$

Consider radiation emitted perpendicular to the direction of motion in the moving frame ($v'_x = 0, v'_y = c$). In the rest frame, the transformed components are $v_x = u$ and $v_y = c\sqrt{1-u^2/c^2}$, so the angle of emission relative to the motion axis satisfies:

$$\sin\theta = \frac{v_y}{v} = \frac{c\sqrt{1-u^2/c^2}}{c} = \sqrt{1-\frac{u^2}{c^2}}$$

For relativistic velocities ($u \sim c$), $\sin\theta \ll 1$ — the angle $\theta$ is very small. All light emitted into the forward hemisphere in the moving frame is squeezed into a **narrow forward cone** in the rest frame. The half-opening angle of this cone is $\theta \approx 1/\gamma$ where $\gamma = (1-u^2/c^2)^{-1/2}$ is the Lorentz factor. For $\gamma \sim 10^3$–$10^6$ (typical for pulsar electrons), this is an extremely narrow beam.

Second, the **lighthouse effect**: the pulsar's magnetic axis is not aligned with its rotation axis. The narrow emission beam therefore sweeps through space like the beam of a lighthouse as the NS rotates. An Earth-based observer detects a pulse each time the beam sweeps past the line of sight.

The three ingredients that produce the observed radio pulses are thus: (1) a narrow coherent beam from the magnetic poles (relativistic headlight effect), (2) misalignment of the magnetic and rotation axes, and (3) fast rotation of the NS.

### 11.6 Dispersion and Distance Measurement

Pulsar pulses observed at different radio frequencies arrive at slightly different times — a phenomenon called **dispersion**. As the radio wave travels through the ionized interstellar medium (ISM), the oscillating electric field of the wave causes free electrons to vibrate, which slows the propagation speed of the wave below $c$. The slowdown is frequency-dependent: lower frequencies are slowed more than higher frequencies.

A sharp pulse emitted simultaneously at all frequencies at the NS is gradually **dispersed** as it travels: higher-frequency components arrive first, lower-frequency components arrive later. The time delay $\Delta t$ between frequencies $\nu_1$ and $\nu_2$ is:

$$\Delta t \propto \text{DM} \times \left(\frac{1}{\nu_2^2} - \frac{1}{\nu_1^2}\right)$$

where DM is the **dispersion measure** — the column density of free electrons along the line of sight, $\text{DM} = \int n_e\,dl$. By measuring the frequency-dependent arrival time delays of pulses from a pulsar of known period, and using a model for the Galactic electron distribution, one can estimate the **distance to the pulsar**. Dispersion measurement is therefore a primary distance estimator for pulsars.

---

## 12. Pulsar Evolution: The P–$\dot{P}$ Diagram

### 12.1 Energy Loss and Spindown

As a pulsar ages, it loses rotational energy through magnetic dipole radiation and particle emission. This energy loss drives a gradual increase in the period $P$ and a gradual decrease in $\dot{P}$ (the spindown rate). The **magnetic dipole radiation formula** provides a direct link between $P$, $\dot{P}$, and the surface magnetic field strength $B$:

$$B^2 = \frac{3Ic^3}{8\pi^2 R^6} P\frac{dP}{dt}$$

Rearranging: $B \propto \sqrt{P\dot{P}}$. Lines of constant $B$ are therefore diagonal lines in the $\log P$–$\log\dot{P}$ diagram.

Young pulsars are born with:
- Short periods: $\log P \approx -3$ (i.e., $P \sim 0.001$ s)
- High spindown rates: $\log\dot{P} \approx -13$

As they age, pulsars spin down: $P$ increases (moves right in the diagram) and $\dot{P}$ decreases (moves down). The evolutionary track in the $P$–$\dot{P}$ diagram sweeps from upper left (young, fast, high $\dot{P}$) toward lower right (old, slow, low $\dot{P}$).

Old pulsars have:
- Long periods: $\log P \approx 0$ (i.e., $P \sim 1$ s)
- Low spindown rates: $\log\dot{P} \approx -19$

### 12.2 The Pulsar Graveyard and the Death Line

The electromagnetic emission mechanism requires sufficient charged particles to be extracted from the NS surface and accelerated to produce the pair cascade. This mechanism breaks down when the pulsar has slowed to the point where the electric field at the surface can no longer extract and accelerate enough particles. Below a critical combination of $P$ and $\dot{P}$, the pulsar becomes effectively invisible — this boundary is the **death line**.

The death line corresponds approximately to:

$$P \approx 2.42 \times 10^{-6}\,B^{1/2}\ \text{s}$$

This equation sets the minimum magnetic field intensity needed to sustain sufficient pair production. Pulsars whose evolution tracks cross the death line fall into the **graveyard** — a region in the lower-right of the $P$–$\dot{P}$ diagram where pulsars are extinct (no longer detectable).

The $P$–$\dot{P}$ diagram also marks the positions of several notable classes:
- **The Crab and Vela pulsars**: upper left (young, energetic)
- **Normal pulsars**: scattered across the central-right region, with characteristic ages $10^4$–$10^8$ yr
- **Binary pulsars**: circled separately (their evolution is modified by mass transfer)
- **Magnetars (SGR/AXP)**: upper right of the diagram ($B \sim 10^{14}$–$10^{15}$ G), with very high $\dot{P}$
- **Millisecond pulsars**: lower left (short $P$, very low $\dot{P}$) — the "recycled" pulsars

### 12.3 The $P$–$B$ Perspective

An equivalent way to visualize the pulsar evolution is the spin-period vs. magnetic-field-strength diagram. Young pulsars spin rapidly and have strong magnetic fields. As they age, they slow and their effective magnetic field decreases. The evolutionary path runs from the upper-left (young, fast, strong field) toward the lower-right ("death line" boundary where emission quenches). Below the death line lies the "Graveyard" of extinct pulsars. Characteristic ages can also be read off contours in this diagram.

---

## 13. Millisecond Pulsars and the Recycling Scenario

### 13.1 The Paradox of Millisecond Pulsars

In the $P$–$\dot{P}$ diagram, there exists a separate cluster of pulsars in the extreme lower-left: the **millisecond pulsars (MSPs)**. Their paradoxical properties are:

- **Very short period** ($P \sim 10^{-3}$ s): typical of a very young pulsar, because angular momentum conservation at birth demands fast rotation.
- **Very low period derivative** ($\dot{P} \sim 10^{-19}$–$10^{-20}$): typical of a very old pulsar, because only after a long time does the spindown rate become this small.

The characteristic age of the first known MSP, PSR 1937+214 ($P = 1.5 \times 10^{-3}$ s, $\dot{P} = 10^{-19}$):

$$\tau = \frac{P}{\dot{P}} = \frac{1.5 \times 10^{-3}}{10^{-19}} = 1.5 \times 10^{16}\ \text{s} \approx 5 \times 10^8\ \text{yr}$$

This characteristic age is one order of magnitude larger than normal pulsars. PSR 1937+214 rotates 600 times per second — the oldest observable pulsar is also one of the fastest rotators. This is the core paradox that the recycling scenario resolves.

### 13.2 The Recycling Scenario

The recycling scenario (Bhattacharya et al. 1991) proposes that MSPs are **old pulsars that have been spun up by accretion of mass (and angular momentum) from a binary companion**. The scenario proceeds in stages:

**Stage 1 — Formation**: The NS is formed in a SN explosion from a massive star in a binary system. The SN explosion does not necessarily disrupt the binary (if the kick velocity is not too large). The NS appears as a normal, young pulsar with fast rotation.

**Stage 2 — Spindown**: The NS (now an old pulsar) gradually slows down through magnetic dipole radiation. Its period increases and $\dot{P}$ decreases. Eventually it approaches or enters the pulsar graveyard — becoming too faint to detect.

**Stage 3 — Mass accretion (spin-up phase)**: The companion star evolves off the main sequence, expands as a red giant, fills its Roche lobe, and begins transferring mass onto the NS through an **accretion disk**. Accreted matter carries **angular momentum** that is transferred to the NS, spinning it up. X-ray emission is produced as the accreted material falls onto the NS surface. This phase is observed as an **X-ray binary**.

The mass transfer process is complicated by the NS's strong magnetic field and magnetosphere. The accretion disk is disrupted at the **Alfvén radius** $r_A$ (also called the magnetospheric radius), where the magnetic energy density equals the kinetic energy density of the infalling gas:

$$\frac{B^2}{8\pi} = \frac{1}{2}\rho v^2$$

Using $B(r) = B_s (R/r)^3$ (dipole field), $v = \sqrt{2GM/r}$ (free-fall velocity), and $\dot{M} = 4\pi r^2 \rho v$ (mass continuity), one derives:

$$r_A = \left(\frac{B_s^4 R^{12}}{2GM\dot{M}^2}\right)^{1/7}$$

where $B_s$ is the surface magnetic field, $R$ is the NS radius, $G$ is the gravitational constant, $M$ is the NS mass, and $\dot{M}$ is the mass accretion rate. The gas is channeled from $r_A$ inward along the magnetic field lines to the magnetic poles.

The effective disruption radius is somewhat smaller:

$$r_d \approx 0.5\,r_A$$

The angular momentum transferred to the NS per unit time equals the specific angular momentum of the accreted matter at $r_d$:

$$\frac{dL}{dt} = \dot{M} v r_d \quad (v = \sqrt{GM/r_d})$$

Setting this equal to the NS angular momentum change rate:

$$-2\pi I\frac{\dot{P}}{P^2} = \dot{M}\sqrt{GM\,r_d}$$

This gives the **spin-up rate**:

$$\frac{\dot{P}}{P} = -\frac{P}{2\pi I}\sqrt{\alpha} \cdot \left(\frac{B_s^2 R^6 G^3 M^3 \dot{M}^6}{2}\right)^{1/7}$$

where $\alpha \approx 0.5$ is the ratio $r_d/r_A$. The key features of this equation: spin-up is faster (more negative $\dot{P}/P$) for higher accretion rates, stronger magnetic fields, and larger NS masses. The minimum achievable period (the "spin-up line") is set when the NS rotation rate equals the Keplerian orbital rate at $r_d$.

**Stage 4 — Result of recycling**: After mass transfer ceases, the NS has been spun up to millisecond periods. The companion has been stripped of most of its envelope; what remains is typically the core of a red giant — a **helium white dwarf**. The system appears as a binary consisting of an MSP + He-WD.

**Stage 5 — In the $P$–$\dot{P}$ diagram**: The recycled pulsar appears in the lower-left corner (short $P$, low $\dot{P}$). The evolutionary track is shown as a large horizontal arrow pointing from the graveyard region (right) back to the millisecond period region (left) — opposite to the normal spindown evolution.

### 13.3 Observational Confirmation

The first MSP, PSR 1937+214, was discovered and immediately interpreted within this scenario. Subsequent observations confirmed many of its predictions:

- MSPs are preferentially found in **binary systems** with WD companions (as predicted by the recycling scenario). The companion is typically a low-mass He-WD — the stripped core of the donor star.
- MSPs are overabundant in **globular clusters**, where stellar encounters are frequent and can create new binary systems via **tidal capture**. However, tidal capture is rare even in dense cluster cores (only $\sim 10$ events per $10^{10}$ years per cluster).
- A "newborn MSP" system was directly observed in the globular cluster NGC 6397 (Ferraro et al. 2001, ApJ 561, L93), showing an accreting NS in the process of being spun up — caught in the act of recycling.

### 13.4 Black Widow Pulsars

Some MSPs are found as **isolated objects** — they have no binary companion. How does an MSP that requires a binary partner for its recycling end up isolated?

The **Black Widow** scenario explains this:

1. The NS is recycled via mass accretion from its companion, as in the standard scenario.
2. After most of the envelope is transferred, the companion is a low-mass remnant — typically a very small He-WD (a few $0.01\,M_\odot$).
3. The NS is now an active MSP, emitting intense radiation and a wind of relativistic particles.
4. This intense radiation and particle wind **irradiates and ablates** the small companion. If the companion is too low-mass to survive, it is gradually **vaporized** by the MSP emission.
5. Over a few million years, the swarm of particles from the MSP evaporates the remnant companion entirely, leaving the MSP as an **isolated star**.

The name "Black Widow" refers to the spider species in which the female (the MSP) destroys her mate (the companion) after mating (mass transfer). The process has been directly observed: the Fermi Space Telescope detected a Black Widow pulsar actively ablating its companion, and NASA produced a visualization of this process. The companion star in an active Black Widow system shows evidence of intense irradiation on its inner (pulsar-facing) hemisphere.

---

## 14. The Galactic Bulge, Chemical Evolution, and Bulge Fossil Fragments

### 14.1 Chemical Evolution of Different Environments

The [$\alpha$/Fe]–[Fe/H] diagram (discussed in Section 5) can be used to infer the star formation history of any environment from the observed stellar abundance patterns. Three contrasting environments in the Local Group illustrate the range of behaviors:

**Local Group Dwarf Galaxies**: Low SFR. The knee occurs at very low metallicity ($[\text{Fe/H}] \approx -1.5$). By the time the first Type Ia SNe exploded, few SN II had enriched the ISM, so the knee is at low [Fe/H]. Stars formed after the knee descend steeply toward low [$\alpha$/Fe].

**Galactic Halo**: Intermediate SFR. The knee falls around $[\text{Fe/H}] \approx -1.0$. Halo stars formed early and rapidly, but not as rapidly as bulge stars.

**Galactic Bulge**: High SFR. The bulge formed stars so rapidly that SN II enriched the ISM to near-solar metallicity before the first SN Ia exploded. The knee occurs at $[\text{Fe/H}] \approx -0.3$ to $0.0$. Bulge stars at all but the highest metallicities show elevated [$\alpha$/Fe] ratios — the hallmark of a rapid, intense early burst of star formation.

This pattern — the position of the knee as a function of environment — is the **chemical DNA** of the formation history. By measuring stellar abundances in any environment (from dwarf galaxies to massive cluster systems), one can infer the SFR and the epoch of first Type Ia SN enrichment with high precision.

### 14.2 The Lambda-CDM Framework and Bulge Formation

The prevailing $\Lambda$-cold dark matter ($\Lambda$CDM) cosmological model predicts that cosmic structures form **hierarchically**: large structures are assembled from the merging of smaller ones. This model successfully explains the observed properties of galaxies and galaxy clusters. N-body simulations show that dark matter forms an increasingly complex web at successively lower redshifts ($z = 4.2 \rightarrow 2.1 \rightarrow 0$), with massive nodes representing galaxies.

Observations with the Gaia satellite have confirmed that a relevant fraction of the Galactic halo was assembled via repeated mergers. Several kinematically distinct stellar streams (Gaia-Enceladus, Helmi streams, Sequoia, etc.) have been identified and attributed to past accretion events. The most significant confirmed event is the merger of the Milky Way with the Gaia-Enceladus dwarf galaxy ($\sim 10^9\,M_\odot$) approximately 10 Gyr ago, which deposited a large fraction of the inner halo stars.

However, until recently, **no direct evidence existed for the hierarchical assembly of the Galactic Bulge**. The bulge is the most inaccessible region of the Milky Way due to extreme and differential dust extinction. One proposed mechanism for bulge formation involves massive clumps of gas and stars ($10^8$–$10^9\,M_\odot$) observed in "clumpy galaxies" at high redshift ($z \sim 1$–$2$, corresponding to $\sim 8$–$10$ Gyr ago). These clumps are thought to migrate toward the galactic center through dynamical friction, dissipatively coalesce, and build the bulge. The vast majority of such clumps would be destroyed in the coalescence process, but a few might survive as distinct stellar systems.

### 14.3 Bulge Fossil Fragments: Terzan 5 and Liller 1

The **Bulge Fossil Fragments** (BFF) are massive stellar systems in the Galactic bulge that superficially resemble globular clusters but possess properties fundamentally inconsistent with the standard globular cluster picture. They are proposed to be the surviving remnants of primordial massive clumps that contributed to building the Galactic bulge.

All Galactic globular clusters contain only old, coeval stellar populations (near-uniform age of $\sim 12$–$13$ Gyr). Bulge Fossil Fragments, by contrast, contain **multiple stellar populations with significantly different ages and metallicities**:

**Terzan 5** (Ferraro et al. 2009, Nature, 462, 483):
- Located in the Galactic bulge, observable in near-infrared with HST
- Color-Magnitude Diagram (CMD) shows an extremely complex morphology with multiple intertwined sequences
- The zoomed region around the subgiant branch reveals **two distinct subgiant branches** (visible in HST $m_{F115W}$ vs $m_{F115W}-m_{F200W}$ filters), proving two stellar populations with different ages and/or metallicities
- Sub-populations have ages of $\sim 12$ Gyr (old) and $\sim 4$–$5$ Gyr (young)
- Multiple iron sub-populations: one at $[\text{Fe/H}] \approx -0.3$ and one at $[\text{Fe/H}] \approx +0.3$
- The $[\alpha/\text{Fe}]$–$[\text{Fe/H}]$ pattern of Terzan 5's sub-populations matches the Galactic Bulge field stars perfectly
- The orbit of Terzan 5 is highly confined to the bulge region ($Z \lesssim 1$ kpc, $R < 2$ kpc), confirming its association

**Liller 1** (Ferraro et al. 2021, Nature Astronomy, 5, 311):
- CMD (K vs I-K, corrected for differential reddening and proper motions) reveals **two widely separated main sequence turnoffs**: one old ($\sim 12$ Gyr, redder/fainter) and one young ($\sim 1$–$2$ Gyr, bluer/brighter)
- The chemical abundance pattern ($[\text{<Mg,Si,Ca>/Fe}]$ vs $[\text{Fe/H}]$) of Liller 1 stars (orange squares) tracks the Galactic Bulge field running median across a wide metallicity range — confirming a bulge origin
- Liller 1's orbit is extremely flattened and disk-confined ($Z \approx 0$), extending to $R \lesssim 0.8$ kpc
- Ages: old population $\sim 12$ Gyr, young population $\sim 1$–$2$ Gyr

The presence of two sub-populations with vastly different ages implies that these systems experienced at least two major episodes of star formation separated by several Gyr. This is inconsistent with the single-burst picture of globular clusters but consistent with a massive primordial structure that retained enough gas to form new stars long after its initial burst.

### 14.4 The New BFF Research Program

The discovery of Terzan 5 and Liller 1 as BFFs opened a systematic search program. An international team led by Francesco R. Ferraro (University of Bologna) has been awarded **255 hours of Very Large Telescope (VLT) observing time** (PI: Ferraro) to survey **17 stellar systems** in the Galactic Bulge, measuring their chemical abundances (chemical DNA). The goal is to identify additional BFFs and reconstruct the hierarchical assembly history of the Galactic Bulge — searching for accreted sub-structures as has been done for the halo (Gaia-Enceladus, etc.).

The 17 target systems span galactic coordinates within $|l| \lesssim 20°$, $|b| \lesssim 10°$ and include systems such as NGC 6380, NGC 6441, NGC 6388, Terzan 5, Terzan 6, Terzan 2, Terzan 1, Palomar 6, NGC 6304, NGC 6316, UKS 1, Djorgovski 2, Terzan 10, NGC 6528, NGC 6553, NGC 6656, and Liller 1. The chemical abundance pattern of each system is compared to the theoretical BFF template (the Galactic Bulge $[\alpha/\text{Fe}]$–$[\text{Fe/H}]$ sequence) and to each other to identify systems that share a common chemical origin.

The observational evidence for BFFs is supported by: (a) the observed "clumpy galaxy" morphology at high redshift ($z \sim 0.24$–$1.2$, from GOODS HST observations by Elmegreen et al. 2009), (b) N-body simulations of bulge formation via clump coalescence that reproduce the migration and merger sequence, and (c) the BFF systems' orbital confinement to the bulge region. The analogy is explicitly archaeological: the team is "digging into the bulge" to find the fossil remnants of ancient cosmic structures, as archaeologists seek the vestiges of ancient civilizations.

---

## 15. Accretion Onto Neutron Stars and Spin-Up Physics

### 15.1 The Alfvén Radius: Where the Magnetosphere Disrupts the Disk

When matter accretes onto a magnetized neutron star, the infalling gas cannot form a standard disk all the way to the NS surface. At some radius, the magnetic pressure of the NS's dipole field dominates over the ram pressure (kinetic energy density) of the infalling gas. Beyond this point, the gas is channeled along magnetic field lines to the magnetic poles.

The **Alfvén radius** $r_A$ (also called the magnetospheric radius) is defined by the balance:

$$\frac{B^2(r_A)}{8\pi} = \frac{1}{2}\rho(r_A)\,v^2(r_A)$$

The dipole magnetic field at radius $r$ is $B(r) = B_s (R/r)^3$. The free-fall velocity at $r$ is $v = \sqrt{2GM/r}$. The mass conservation relation gives $\dot{M} = 4\pi r^2 \rho v$, so $\rho = \dot{M}/(4\pi r^2 v)$.

Substituting into the balance condition:

$$\frac{B_s^2}{8\pi}\left(\frac{R}{r}\right)^6 = \frac{1}{2} \cdot \frac{\dot{M}}{4\pi r^2} \cdot \sqrt{\frac{2GM}{r}}$$

After algebraic manipulation:

$$B_s^2\frac{R^6}{r^4} = \frac{\dot{M}}{r^2}\sqrt{\frac{2GM}{r}} \implies B_s^4\frac{R^{12}}{\dot{M}^2} = r^7 \cdot 2GM$$

$$r_A = \left(\frac{B_s^4 R^{12}}{2GM\dot{M}^2}\right)^{1/7}$$

The **destruction radius** (the actual inner edge of the disk) is:

$$r_d \approx 0.5\,r_A$$

### 15.2 Angular Momentum Transfer and Spin Evolution

The angular momentum of the NS is $L = I\omega = 2\pi I/P$. The rate of change due to the NS spin evolution:

$$\frac{dL}{dt} = I\frac{d\omega}{dt} = -\frac{2\pi I \dot{P}}{P^2}$$

The angular momentum carried per unit time by the accreted gas at the destruction radius:

$$\frac{dL}{dt} = \dot{M}\,v\,r_d \quad \text{where } v = \sqrt{GM/r_d}$$

Equating and substituting $r_d = \alpha r_A$ (with $\alpha = 0.5$):

$$-\frac{2\pi I \dot{P}}{P^2} = \dot{M}\sqrt{GM\,r_d}$$

$$\frac{\dot{P}}{P} = -\frac{P}{2\pi I}\sqrt{\alpha} \cdot \left(\frac{B_s^2 R^6 G^3 M^3 \dot{M}^6}{2}\right)^{1/7}$$

This is the **spin-up rate equation** for mass-accreting NSs. Key physical implications:

- The NS spins up (negative $\dot{P}$) when mass is transferred at the destruction radius with the Keplerian velocity.
- The spin-up is more efficient for higher $\dot{M}$, stronger $B$, and more massive NS.
- As the NS spins faster, the equilibrium (spin-up) period decreases until it equals the Keplerian period at $r_d$ — this sets the **minimum achievable spin period** (the spin-up line in the $P$–$\dot{P}$ diagram).
- As the NS spins down after accretion ceases, the period increases and $\dot{P}$ decreases — the MSP moves slowly through the lower-left portion of the $P$–$\dot{P}$ diagram.
- Some models predict a **significant decay of the magnetic field** over time (not just the spin-down), which would further reduce $\dot{P}$ and allow the pulsar to persist in the millisecond regime.

### 15.3 High-Mass Binary Stars in the Intermediate Mass Range

Stars with $7 < M/M_\odot < 9$–$11$ occupy a special evolutionary niche. Carbon ignites in a **weakly degenerate core** at $T \sim 5$–$6 \times 10^8$ K, proceeding through the reactions listed in Section 4.1. Critically, from the onset of carbon burning onward, **enormous amounts of energy are lost as neutrinos**. This neutrino energy loss exceeds the nuclear energy production rate, meaning nuclear burning alone cannot supply the luminosity demanded by the stellar structure. To compensate, the star **rapidly contracts**, releasing gravitational potential energy (as demanded by the virial theorem). This contraction dramatically accelerates the pace of subsequent nuclear burning stages.

At the end of central C burning, the core — composed mainly of oxygen (from prior He burning) and neon (from C burning) — becomes **electron-degenerate**. If this core grows through shell burning to exceed $M_{Ch}$, electron captures on $^{20}$Ne and $^{24}$Mg trigger a collapse to a neutron star (the **electron-capture supernova** channel). If the core remains below $M_{Ch}$, the star sheds its envelope on the AGB and leaves an **ONe white dwarf**.

---

## 16. Summary: Stellar Endpoints and Supernova Types

### 16.1 Complete Endpoint Table

| Initial mass ($M_\odot$) | Final core state | Endpoint | SN type |
|---|---|---|---|
| $< 0.08$ | Never ignites H | Brown Dwarf | — |
| $0.08$–$0.5$ | Permanent degenerate He core | He-WD | — |
| $0.5$–$7$ | Degenerate CO core | CO-WD | — |
| $7$–$11$ | Mildly degenerate CO/ONe core | ONe-WD or EC-SN | EC-SN (rare) |
| $11$–$25$ | Non-degenerate Fe core | Neutron Star | Type II (CC) |
| $> 25$ | Non-degenerate Fe core (very massive) | Black Hole | Type II (CC) or direct collapse |

Type Ia SNe arise from any CO-WD in a binary, regardless of the WD progenitor's initial mass, provided it reaches $M_{Ch}$ through accretion or merging.

### 16.2 Energy Budget Comparison

| Event | Total energy | Neutrino energy | Kinetic energy | Optical energy |
|---|---|---|---|---|
| Type Ia SN | $\sim 10^{51}$ erg (nuclear) | None | $\sim 10^{51}$ erg | $\sim 10^{49}$ erg |
| Type II SN | $\sim 3 \times 10^{53}$ erg (gravitational) | $\sim 3 \times 10^{53}$ erg | $\sim 10^{51}$ erg | $\sim 10^{49}$ erg |

The Type II SN releases $\sim 300$ times more total energy than a Type Ia, but almost all of it ($\sim 99\%$) escapes as neutrinos. The optical display of a Type II SN is comparable to (or even less than) that of a Type Ia despite its vastly larger total energy output. This reinforces why detecting the neutrino burst from a nearby SN (as was done for SN1987A) is essential for testing core-collapse models.

### 16.3 Nucleosynthetic Contributions

The origin of the elements in the periodic table, summarized by contribution source:

- **Big Bang** ($A \sim 1$–$4$): H, He, trace Li
- **$\alpha$-elements** (O, Mg, Ca, Si, Ti; $A \sim 10$–$50$): Core-collapse SNe (SN II, Ib, Ic). These elements are produced in the $\alpha$-capture chain during He, C, Ne, and O burning in massive stars.
- **Iron-peak elements** ($A \sim 50$–$60$): Primarily Type Ia SNe (which produce about 2/3 of all Galactic Fe), with a minor contribution from SN II (which eject $\sim 0.1\,M_\odot$ Fe per event vs. $\sim 0.6\,M_\odot$ per Type Ia).
- **s-process elements** ($A > 90$): Low-mass AGB stars (main component, $A > 90$) and massive stars (weak component, $70 < A < 90$).
- **r-process elements** ($A > 56$, neutron-rich isotopes, U, Th): Core-collapse SNe and kilonovae (neutron star mergers). The kilonova route was confirmed observationally in 2017 (GW170817).

The [$\alpha$/Fe]–[Fe/H] diagram probes the interplay between SN II ($\alpha$ contributors) and SN Ia (Fe contributors) in any stellar population, making it the most powerful single diagnostic of chemical enrichment history.
