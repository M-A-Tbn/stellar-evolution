# Black Holes & Gravitational Waves — Study Notes
**Source:** `29.BH_GW_hifi.md` | **Session:** Black Holes & Gravitational Waves | **Date:** 2026-05-23

---

## 1. Black Holes: Basic Concepts and Formation

### 1.1 The Oppenheimer–Volkoff Mass Limit and BH Formation

When the remnant left behind by a core-collapse supernova (CC SN) has a mass exceeding the **Oppenheimer–Volkoff (OV) limit** of approximately $2.5$–$3\,M_\odot$, no stable compact object configuration is possible. Neutron degeneracy pressure, which supports a neutron star against gravity, is insufficient once this mass threshold is crossed. The remnant therefore has no equilibrium state and undergoes total gravitational collapse to form a **black hole (BH)**. This OV mass limit corresponds to a progenitor star with an initial main-sequence mass of roughly $25\,M_\odot$; stars more massive than this are the primary factories of stellar-mass BHs through the core-collapse channel.

It is instructive to note that even within purely classical (Newtonian) mechanics, a configuration resembling a BH can be predicted. A sufficiently massive and compact object can possess an escape velocity exceeding the speed of light:

$$v^2 = \frac{2GM}{R} > c^2$$

This classical argument was first articulated by **George Michell in 1784**, who called such objects **"black stars."** His remarkable insight — that such objects would be invisible to direct light but could potentially be inferred from the orbital motion of luminous companions — anticipates the modern observational strategy for detecting BHs. However, the Newtonian picture is only a suggestive analogy; the proper treatment requires general relativity, which profoundly changes the physical interpretation. The classical formula nevertheless yields the correct numerical expression for the critical radius (the Schwarzschild radius), even though it does so for the wrong physical reasons.

### 1.2 The Schwarzschild Radius

Setting the Newtonian escape velocity equal to $c$ and solving for the critical radius gives the **Schwarzschild radius** $R_s$:

$$R_s = \frac{2GM}{c^2}$$

Here:
- $G = 6.67 \times 10^{-8}\ \mathrm{dyne\,cm^2\,g^{-2}}$ is Newton's gravitational constant,
- $c = 3 \times 10^{10}\ \mathrm{cm\,s^{-1}}$ is the speed of light,
- $M$ is the mass of the object.

Converting to practical solar units using $M_\odot = 2 \times 10^{33}\ \mathrm{g}$:

$$R_s = \frac{2GM}{c^2} = 3 \times \frac{M}{M_\odot}\ \mathrm{km}$$

This deceptively simple result reveals a striking fact: **the Schwarzschild radius is extremely small** even for massive stars. For a $1\,M_\odot$ object, $R_s = 3$ km; for a $50\,M_\odot$ object, $R_s = 150$ km. The entire mass of the Sun would need to be compressed into a sphere of radius 3 km to form a BH. This compactness is orders of magnitude beyond that of any ordinary star or even a white dwarf (which has $R \sim 10^4$ km). In practice, $R_s$ sets the scale below which general relativistic effects completely dominate and classical physics fails entirely.

The formula $R_s = 3(M/M_\odot)$ km is one of the most important numerical results in the subject and must be memorised. It provides an immediate physical scale: knowing the mass of a compact remnant, one immediately knows the spatial scale of the event horizon.

---

## 2. Spacetime Geometry and the Metric

### 2.1 The Flat Spacetime Metric and the Interval

To understand how a BH modifies the geometry around it, one must first understand how distance is defined in flat (Minkowski) spacetime. In special relativity, the **spacetime interval** $\Delta s$ between two events $A$ and $B$ is:

$$(\Delta s)^2 = \left[c(t_B - t_A)\right]^2 - (x_B - x_A)^2 - (y_B - y_A)^2 - (z_B - z_A)^2$$

This quantity $(\Delta s)^2$ can be positive, negative, or zero, and each case has a fundamentally different physical meaning:

- **$(\Delta s)^2 > 0$ (timelike):** The two events can be causally connected by a particle moving with velocity $v < c$. This region is the **explorable** part of spacetime — the future and past light cones accessible to a massive observer.
- **$(\Delta s)^2 = 0$ (lightlike or null):** Only light can connect the two events. This condition defines the **surface of the light cone**, the boundary between causally connected and disconnected regions.
- **$(\Delta s)^2 < 0$ (spacelike):** No causal connection can be established. Connecting these events would require a signal travelling faster than light, which is forbidden. This region is called the **elsewhere** — the unknowable region.

The partition of spacetime into these three regions is one of the foundational structures of relativity and governs what any observer can ever know about the universe.

### 2.2 The Light Cone and Causal Structure

The **light cone** is the geometric object in spacetime that organises causal relationships. Visualising time on the vertical axis and one spatial dimension on the horizontal axis: light emitted from an event at the origin travels along the lines $x = ct$, forming a V-shape. Everything within the V (upward) is the future light cone — reachable; everything within the inverted V (downward) is the past light cone — from which signals can arrive. Everything outside both cones is the elsewhere.

A key constraint of relativity is that **all particle trajectories must remain confined within their local light cone**. Moving outside the light cone is equivalent to travelling faster than light, which violates causality. This principle applies in both special and general relativity, but in the presence of gravity (general relativity), the light cones themselves are **tilted and distorted** by the curvature of spacetime. Far from a massive body, cones point symmetrically upward. Approaching a BH, cones tilt progressively toward the centre. At the event horizon, the future light cone is tilted so strongly that even the outward-directed light ray lies exactly on the horizon — nothing can escape. Inside the horizon, the entire future light cone points toward the singularity: every possible future for an infalling observer leads to the singularity.

This tipping of light cones is the geometric explanation of why nothing can escape from within a BH: it is not that things are "pulled back," but rather that the geometry of spacetime inside the horizon makes every possible future trajectory lead inward.

### 2.3 The Schwarzschild Metric: Curved Spacetime Around a Mass

In flat spacetime expressed in spherical coordinates (more natural for a spherically symmetric mass), the interval becomes:

$$(ds)^2 = \left[c\,dt\right]^2 - (dr)^2 - (r\,d\theta)^2 - (r\sin\theta\,d\phi)^2$$

When a spherical mass $M$ is present, this flat metric is modified by factors involving the Schwarzschild radius. The resulting **Schwarzschild metric** is:

$$(ds)^2 = \left[c\,dt\,\sqrt{1 - \frac{2GM}{rc^2}}\right]^2 - \left[\frac{dr}{\sqrt{1 - \frac{2GM}{rc^2}}}\right]^2 - (r\,d\theta)^2 - (r\sin\theta\,d\phi)^2$$

This can be written compactly using $R_s = 2GM/c^2$:

$$(ds)^2 = \left[c\,dt\,\sqrt{1 - \frac{R_s}{r}}\right]^2 - \left[\frac{dr}{\sqrt{1 - R_s/r}}\right]^2 - (r\,d\theta)^2 - (r\sin\theta\,d\phi)^2$$

This metric is valid outside a spherically symmetric, non-rotating, uncharged mass (the Schwarzschild solution to Einstein's field equations). It describes exact general relativistic spacetime curvature. The factor $\sqrt{1 - R_s/r}$ appears in the time component with a square root in the numerator and in the spatial radial component with a square root in the denominator. Both effects diverge as $r \to R_s$, signalling the extreme nature of the event horizon.

### 2.4 Radial Distance Dilation and Gravitational Time Dilation

The Schwarzschild metric implies two profound measurable effects on radial distance and time intervals as one approaches the horizon.

**Radial distance dilation:** Consider two points separated by a coordinate difference $dr$ along the same radial line, measured simultaneously ($dt = 0$) with $d\theta = d\phi = 0$. The proper (physical) distance $dL$ between them is:

$$dL = \frac{dr}{\sqrt{1 - R_s/r}}$$

Since $\sqrt{1 - R_s/r} < 1$ for all finite $r > R_s$, we have $dL > dr$. The actual physical distance is always **larger** than the coordinate separation $dr$. Numerically:
- At $r = 5R_s$: $\sqrt{1 - 1/5} = 0.89$, so $dL \approx 1.12\,dr$
- At $r = 4R_s$: $\sqrt{1 - 1/4} = 0.87$, so $dL \approx 1.15\,dr$
- At $r = 2R_s$: $\sqrt{1 - 1/2} = 0.7$, so $dL \approx 1.41\,dr$

This is analogous to reading distances from a topographic map: the map gives coordinate differences, but the actual surface distance always includes the additional path length due to elevation changes. Here, the "elevation" is the curvature induced by mass. As $r \to R_s$, the denominator $\to 0$ and the proper radial distance between two fixed coordinate points diverges — the interior of the BH is "infinitely far away" in proper distance measured from outside.

**Gravitational time dilation:** The proper time $d\tau$ measured by a clock at coordinate radius $r$ is related to the coordinate time $dt$ (measured by an observer at infinity) by:

$$d\tau = \frac{ds}{c} = dt\,\sqrt{1 - \frac{R_s}{r}}$$

Since $\sqrt{1 - R_s/r} < 1$, we have $d\tau < dt$: **time passes more slowly at smaller radii**. This is gravitational time dilation. As $r \to R_s$, $d\tau \to 0$ for a fixed $dt$: time slows to a **complete stop** as seen by a distant observer. From the distant observer's perspective, nothing ever actually reaches $R_s$ — infalling matter appears to freeze asymptotically at the horizon. In the infalling observer's own proper time, however, they cross the horizon in finite time.

### 2.5 The Frozen Speed of Light at the Event Horizon

For light, the spacetime interval is zero: $(ds)^2 = 0$. Considering radial light propagation ($d\theta = d\phi = 0$) in the Schwarzschild metric:

$$0 = \left[c\,dt\,\sqrt{1 - \frac{R_s}{r}}\right]^2 - \left[\frac{dr}{\sqrt{1 - R_s/r}}\right]^2$$

Solving for $dr/dt$ gives the **coordinate velocity of light** as measured by a distant observer:

$$\frac{dr}{dt} = c\left(1 - \frac{R_s}{r}\right)$$

At large distances ($r \gg R_s$): $dr/dt \approx c$ — light travels at its normal speed. But as $r \to R_s$: $dr/dt \to 0$ — **light appears frozen at the event horizon** from the viewpoint of a distant observer. No signal emitted from $r = R_s$ or smaller can ever reach the outside. This is the operational definition of the event horizon: it is the surface from which not even light can escape.

Crucially, the **event horizon is not a physical surface** — it has no material or force. An infalling observer crosses it without feeling anything locally (in a sufficiently large BH, tidal forces at the horizon can be very mild). The horizon is a global property of the spacetime, a mathematical surface defined by the causal structure of the geometry.

---

## 3. The Event Horizon, Singularity, and Cosmic Censorship

### 3.1 The Event Horizon

The **event horizon** is the spherical surface at coordinate radius $r = R_s$. It is the boundary of the region from which no signal — not even light — can escape to the outside universe. Once any material or information crosses inward through the horizon, it is forever cut off from the external universe. This is precisely why the object is called a "black hole": from outside, it is observationally dark (no light escapes), and it acts as a one-way membrane for all physical processes.

The event horizon is a consequence of the extreme tipping of light cones. Just outside $R_s$, the outward-directed edge of the future light cone is nearly vertical — light can barely escape. At $R_s$ exactly, the outward edge of the future light cone lies along the horizon surface itself — light can remain stationary in coordinate terms but cannot escape. Inside $R_s$, the entire future light cone points inward — all possible futures lead toward $r = 0$.

### 3.2 The Singularity and Cosmic Censorship

At the centre of a BH, $r = 0$, the mathematical solution predicts a **singularity**: a point of zero volume where the mass of the BH is compressed and the spacetime curvature diverges to infinity. The laws of physics as we know them break down at the singularity — general relativity itself predicts its own failure here, signalling the need for a theory of quantum gravity. The singularity is a mathematical indicator that the classical theory is being pushed beyond its domain of validity.

The observational inaccessibility of the singularity is guaranteed by the event horizon: no observer outside can receive any signal from the singularity. This principle is formalised as the **Cosmic Censorship hypothesis**: singularities in general relativity are always "clothed" by an event horizon and are therefore never "naked" (directly observable). A naked singularity would violate causality in fundamental ways. While this remains a conjecture (no general proof exists), it is supported by all known exact solutions of GR describing gravitational collapse.

---

## 4. BH Formation: Progenitors and the Compactness Parameter

### 4.1 The Mass Gap and Black Hole Progenitors

The detection of massive BHs — with masses of a few tens of solar masses — raises the central question of their stellar progenitors. BHs detected via X-ray binary studies (where a BH accretes material from a companion star, producing X-rays) typically have masses in the range $\sim 5$–$15\,M_\odot$. The LIGO/Virgo gravitational wave detections have dramatically extended this range, revealing BH masses from $\sim 10\,M_\odot$ up to over $60\,M_\odot$ in merging binary systems (events such as GW150914, LVT151012, GW151226, GW170104, GW170608, GW170814). Understanding the progenitors of these massive BHs requires understanding which stars collapse directly to BHs and which explode as supernovae.

### 4.2 The Compactness Parameter $\xi_M$ and Failed Supernovae

A key quantity governing whether a star successfully explodes as a supernova or collapses directly to a BH is the **compactness parameter** $\xi_M$:

$$\xi_M = \frac{M / M_\odot}{R(M) / 1000\ \mathrm{km}}$$

This dimensionless number is the ratio of the enclosed mass $M$ (in solar masses) to the radius $R(M)$ containing that mass (in units of 1000 km), evaluated at the moment of iron-core infall. The most commonly used value is $\xi_{2.5}$, which evaluates the compactness at the innermost $2.5\,M_\odot$ of the collapsing star.

A **higher compactness** means more mass is packed into a smaller radius: the core is denser and the gravitational binding energy is larger, making it harder for the SN shock to reverse the collapse. Empirically (and through numerical simulations), a threshold of $\xi_{2.5} \approx 0.2$ has been identified:

- **$\xi_{2.5} < 0.2$:** the model is likely to produce a successful SN explosion, leaving behind a neutron star.
- **$\xi_{2.5} > 0.2$:** the model is likely a **"failed SN"** — direct collapse to a BH without an explosion. All the mass falls into the BH; no supernova is observed.

The dependence of $\xi_{2.5}$ on initial stellar mass $M_\mathrm{ZAMS}$ is not monotonic. Based on PARSEC stellar evolution models (evolved to Fe-core infall using MESA):

- **$M_\mathrm{ZAMS} < 18\,M_\odot$:** the large majority of stars have low compactness and explode as SN, leaving a NS remnant.
- **$18 < M_\mathrm{ZAMS} < 26\,M_\odot$:** a mixed regime with some models exploding and some forming BHs directly (the non-monotonic structure of the compactness parameter means that not all stars in this range behave the same way). Models with core radius exceeding $\sim 12{,}500$ km would produce failed SN.
- **$M_\mathrm{ZAMS} > 26\,M_\odot$:** the majority of stars do not explode as SN and instead collapse directly to a BH (failed SN).

This distinction between "successful SN → NS" and "failed SN → BH" has observational consequences: failed SNe produce no optical transient (no supernova light curve), and the entire stellar mass effectively falls into the remnant BH. This is one pathway to forming the more massive stellar BHs observed by LIGO.

---

## 5. The Mass Spectrum of Compact Remnants: Metallicity Dependence

### 5.1 The Role of Stellar Winds and Metallicity

The mass of a compact remnant depends critically on two quantities: the **final mass of the star** $M_\mathrm{fin}$ at the time of collapse, and the **mass of its final CO core** $M_\mathrm{CO}$ (set at the end of helium burning, since subsequent evolution is much faster). Both depend on $M_\mathrm{ZAMS}$ and on the stellar **metallicity** $Z$.

The final mass is related to the initial mass by the accumulated mass loss through stellar winds:

$$M_\mathrm{fin} = M_\mathrm{ZAMS} - \int \frac{dM}{dt}\,dt$$

The mass-loss rate $\dot{M}$ in massive stars depends on metallicity as:

$$\dot{M} \propto Z^\alpha \quad \mathrm{with}\ \alpha \sim 0.5\text{–}0.9$$

This is physically because stellar winds in hot massive stars are driven by radiation pressure on metal ions (principally Fe). Higher metallicity means more available absorbing lines, stronger radiation-driven outflows, and therefore more mass lost. At solar metallicity ($Z = Z_\odot$), a star initially at $100\,M_\odot$ can lose more than 50% of its mass by winds alone during its lifetime. At very low metallicity ($Z \approx 0.005\,Z_\odot$), the same star loses far less mass, retaining much of its initial mass until collapse.

The key rule: **metal-poor stars lose less mass → more massive remnants, regardless of the SN model assumed.**

### 5.2 Effect on CO Core Mass

The CO core mass $M_\mathrm{CO}$ also decreases with increasing metallicity, for related physical reasons. Metal-poor stars have higher internal temperatures at a given mass (because higher opacity means stronger radiation pressure, requiring higher temperatures to maintain hydrostatic equilibrium). This accelerates thermonuclear reactions and drives larger convective cores on the main sequence. Larger convective cores lead to more efficient mixing and ultimately larger CO cores after the He-burning phase.

The trend can be summarised schematically:

$$Z \nearrow \quad \Rightarrow \quad M_\mathrm{fin} \searrow \quad M_\mathrm{core} \searrow \quad R_\mathrm{core} \searrow$$

Quantitatively, $M_\mathrm{CO}$ varies from a maximum of $\sim 20\,M_\odot$ at solar metallicity to $\sim 65\,M_\odot$ at the lowest metallicities ($Z \sim 10^{-4}$), for the same $M_\mathrm{ZAMS}$ range.

### 5.3 Remnant Mass as a Function of Metallicity and Initial Mass

Combining wind mass loss and the SN explosion model, the mass of the compact remnant $M_\mathrm{rem}$ as a function of $M_\mathrm{ZAMS}$ shows dramatically different behaviour at different metallicities:

- **Metal-poor ($Z = 2 \times 10^{-4}$) and intermediate metallicity ($Z = 2 \times 10^{-3}$):** remnant masses can exceed $25\,M_\odot$ for $M_\mathrm{ZAMS} \gtrsim 40\,M_\odot$. Massive BHs form readily.
- **Solar metallicity ($Z = 2 \times 10^{-2}$):** no remnant exceeds $25\,M_\odot$ for any initial mass up to $150\,M_\odot$, across all SN models considered. **At solar metallicity, massive BHs cannot form from single-star evolution.**

This has profound implications for the interpretation of LIGO detections: the most massive BH binaries (with individual masses $\sim 30$–$60\,M_\odot$) almost certainly formed from metal-poor progenitors, either in the early Universe, in metal-poor satellite galaxies, or in dense stellar environments.

---

## 6. Black Hole Mass Classes and Intermediate-Mass BHs

### 6.1 The Black Hole Mass Spectrum

Observationally and theoretically, BHs are classified into three mass regimes:

- **Stellar-mass BHs** ($M_\mathrm{BH} \lesssim 50$–$100\,M_\odot$): formed from the collapse of individual massive stars or binary mergers. Detected via X-ray binaries and gravitational waves.
- **Intermediate-mass BHs (IMBHs)** ($M_\mathrm{BH} \sim 10^2$–$10^5\,M_\odot$): a largely observationally unconfirmed category. Their existence is theoretically expected and they are searched for in dense stellar environments, particularly globular clusters (GCs).
- **Supermassive BHs (SMBHs)** ($10^6 < M_\mathrm{BH}/M_\odot < 10^9$): found at the centres of virtually all large galaxies, including our own Milky Way ($M \sim 4 \times 10^6\,M_\odot$). Detected via stellar and gas dynamics near galactic centres and via AGN/quasar activity.

### 6.2 Why IMBHs Are Crucial

IMBHs occupy a mass regime between stellar BHs and SMBHs and are scientifically important for three interconnected reasons:

1. **They probe an unexplored BH mass range.** The physical processes forming IMBHs (runaway stellar mergers in dense clusters? direct collapse of massive Pop III stars? repeated BH mergers?) are distinct from those forming stellar or supermassive BHs. Confirming their existence would constrain BH formation channels.

2. **They may be the seeds of SMBHs.** SMBHs are observed in quasars (QSOs) as early as $z > 6$, when the Universe was only $\sim 1$ Gyr old. Growing a SMBH of $10^9\,M_\odot$ from stellar-mass BHs ($\sim 10\,M_\odot$) by Eddington-limited accretion or mergers within $\sim 1$ Gyr is problematic: one would need to merge more than $10^5$ stellar-mass BHs, which is not possible in the available time. IMBHs ($10^2$–$10^5\,M_\odot$) as seeds dramatically relax this constraint.

3. **They are central to understanding galaxy–AGN co-evolution.** The **Magorrian relation** (also called the $M_\mathrm{BH}$–$M_\mathrm{bulge}$ or $M_\mathrm{BH}$–$\sigma$ relation) establishes that SMBHs and their host galaxy bulges grew together:

$$M_\mathrm{BH} \approx 10^{-3}\,M_\mathrm{gal}$$

Extrapolating this relation down to globular cluster masses ($M_\mathrm{GC} \sim 10^5$–$10^6\,M_\odot$) predicts IMBH masses of $\sim 10^2$–$10^3\,M_\odot$ at GC centres. If GCs harbour IMBHs, they are natural laboratories for studying the low-mass end of this relation and testing theories of galaxy formation.

### 6.3 Observational Signatures of IMBHs in Globular Clusters

An IMBH at the centre of a GC would produce two characteristic observational signatures:

**1. Shallow stellar density cusp at the centre.** The IMBH's gravity increases the density of stars in its vicinity, creating a power-law cusp in the surface brightness profile toward the centre (rather than the flat core predicted by a King model without a central mass). Detecting this requires high-resolution imaging (HST or adaptive-optics assisted), because the signal appears only within the inner arcsecond or so.

**2. Steep cusp in the velocity dispersion (VD) profile.** Stars near the IMBH orbit with Keplerian velocities: $v \propto r^{-1/2}$. This produces a **steep rise** in the central velocity dispersion within the **sphere of influence** of the IMBH, defined as:

$$r_\mathrm{BH} = \frac{GM_\mathrm{BH}}{\sigma^2}$$

where $\sigma$ is the velocity dispersion of the surrounding cluster stars. In practical units:

$$r_\mathrm{BH} = 4.32 \times 10^{-3}\,\frac{M_\mathrm{BH}}{M_\odot}\,\left(\frac{\sigma}{\mathrm{km\,s^{-1}}}\right)^{-2}\ \mathrm{pc}$$

For a typical GC with $M_\mathrm{BH} = 10^3\,M_\odot$ and $\sigma = 10\ \mathrm{km\,s^{-1}}$:

$$r_\mathrm{BH} = 4.32 \times 10^{-3} \times \frac{10^3}{10^2}\ \mathrm{pc} = 0.04\ \mathrm{pc}$$

Converting to angular size at a GC distance of $d = 10$ kpc:

$$r''_\mathrm{BH} = 0.89 \times \frac{M_\mathrm{BH}}{M_\odot}\,\left(\frac{\sigma}{\mathrm{km\,s^{-1}}}\right)^{-2}\,\frac{1}{d_\mathrm{kpc}} \approx 0.89''$$

The sphere of influence subtends **sub-arcsecond to arcsecond scales** — requiring adaptive optics (AO) assisted integral field spectroscopy on large telescopes. In the case of NGC 6388, adaptive-optics assisted integral field spectroscopy provided radial velocities for 52 individual stars within $r < 2''$ ($\sim 0.13$ pc), enabling a meaningful probe of the central velocity dispersion profile. Both imaging with HST/HRC and spectroscopy from IFS are needed: the former gives the density profile, the latter the kinematics. King models (which assume no central BH) predict a flat or slowly varying central VD. The "King + IMBH" model predicts a sharp upward cusp in the VD profile toward the centre, consistent with Keplerian enhancement.

---

*Continued in Part 2: Gravitational Waves — Theory, Detection, and GW150914 Analysis*
