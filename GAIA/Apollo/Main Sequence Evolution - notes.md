# Main Sequence Evolution — Study Notes
**Source:** `21.MS_evolution_hifi.md` | **Session:** Main Sequence Evolution | **Date:** 2026-05-20

---

## 1. The Zero Age Main Sequence (ZAMS)

### 1.1 Definition and Physical Meaning

The Zero Age Main Sequence (ZAMS) is a reference locus in the Hertzsprung-Russell (HR) diagram that connects stars of different masses at the very moment they ignite hydrogen burning in their cores. The word "zero age" refers literally to time zero of a star's nuclear-burning life: a star is placed on the ZAMS at the instant its core reaches the temperature required to sustain the hydrogen-to-helium fusion reaction.

It is crucial to understand what the ZAMS is **not**: it is not an evolutionary track. An evolutionary track shows how a single star of fixed mass moves through the HR diagram over time. The ZAMS, by contrast, is a snapshot locus that simultaneously shows stars of wildly different masses, all at time zero of their nuclear lives. Once evolution begins, each star departs from its ZAMS position and moves along its individual track.

The ZAMS is the **only** location in the HR diagram where a firm, straightforward connection between stellar mass and luminosity can be established. Because all ZAMS stars are freshly ignited and have not yet evolved, the mass-luminosity relation applies cleanly without the complications introduced by chemical evolution or structural changes.

A key physical property of all ZAMS stars is chemical homogeneity. Every ZAMS star has a uniform chemical composition throughout its entire volume. This homogeneity arises because during the pre-main-sequence (pre-MS) phase, deep convection mixed the stellar material completely. When the star arrives on the ZAMS, there is no abundance gradient from centre to surface — the composition is the same everywhere.

Pre-MS evolutionary tracks on the HR diagram show a set of curved paths (one per stellar mass) converging from high luminosity down toward the ZAMS. The ZAMS itself appears as a thick diagonal band or line stretching from the lower right (cool, faint, low-mass stars) to the upper left (hot, luminous, high-mass stars). Red arrows in the theoretical HR diagrams indicate that, as soon as evolution commences, every star moves away from this starting line.

### 1.2 Extent of the ZAMS: Mass Range

The ZAMS does not extend infinitely in either direction. It is bounded at both ends by physically determined mass limits. The range across the ZAMS spans effective temperatures from approximately $T_{eff} \approx 2700\ \text{K}$ (at the low-mass end) to $T_{eff} \approx 53000\ \text{K}$ (at the high-mass end) — a factor of about 20 in temperature. Over the same range, the mass varies from $0.08\, M_\odot$ to $90\, M_\odot$ — a factor of over 1000. This enormous range in mass produces only a factor of 20 in surface temperature, illustrating how stellar structure moderates the response to mass.

---

## 2. Mass Cut-Off Limits

### 2.1 The Lower Cut-Off: $M_{low} \approx 0.08\, M_\odot$

There is a minimum mass below which a forming stellar object cannot sustain hydrogen burning. This lower critical mass is:

$$M_{crit} = 0.08\, M_\odot \approx 0.1\, M_\odot$$

Objects with $M < M_{crit}$ never reach the central temperature required to ignite the full pp chain. They are not stars in the astrophysical sense — they are **brown dwarfs**, sometimes called "failed stars." Their cores are not hot enough to sustain a self-regulating thermonuclear furnace, and they simply radiate away their gravitational potential energy and cool down over time.

This lower bound appears as the red-dashed extension of the ZAMS below $0.08\, M_\odot$ in the HR diagram, indicating that objects in this regime lie along the Hayashi track (the pre-MS track) but never converge onto the true ZAMS.

### 2.2 The Upper Cut-Off: $M_{up} \approx 90\, M_\odot$

At the other extreme, very massive stars become structurally unstable. The upper mass limit is approximately:

$$M_{up} \sim 90\, M_\odot$$

This is not an absolute, rigorous cut-off — it depends on metallicity — but it captures the physical message that forming a stable star with $M \gtrsim 100\, M_\odot$ is extremely difficult. The reason is the Eddington luminosity, discussed in detail in Section 3. The key point is that at such masses, the radiation pressure becomes comparable to gravity, threatening hydrostatic equilibrium in the outer layers.

---

## 3. The Eddington Luminosity

### 3.1 Derivation from First Principles

In the outer envelopes of very hot, luminous (high-mass) stars, the radiation pressure can dominate over gas pressure. In this regime the pressure gradient is driven by the radiative flux $F_{rad}$:

$$\frac{dP}{dr} = -\frac{\kappa \rho}{c} F_{rad}, \quad\quad F_{rad} = \frac{L}{4\pi r^2}$$

Here $\kappa$ is the opacity (cm$^2$ g$^{-1}$), $\rho$ is the local density (g cm$^{-3}$), $c$ is the speed of light (cm s$^{-1}$), and $F_{rad}$ is the radiative flux (erg s$^{-1}$ cm$^{-2}$) at radius $r$, where $L$ is the total luminosity passing through that shell.

On the other hand, hydrostatic equilibrium requires the pressure gradient to balance gravity:

$$\frac{dP}{dr} = -\frac{GM\rho}{r^2}$$

where $G$ is the gravitational constant and $M$ is the mass interior to radius $r$. Setting these two expressions equal (i.e., at the point where radiation force exactly counterbalances gravity):

$$\frac{GM\rho}{r^2} = \frac{\kappa\rho}{c} \frac{L}{4\pi r^2}$$

Both $\rho$ and $r^2$ cancel from both sides, giving the **Eddington luminosity**:

$$\boxed{L_{ed} = \frac{4\pi G M c}{\kappa}}$$

This is the **maximum luminosity** that a star of mass $M$ can radiate while maintaining hydrostatic equilibrium, for a given opacity $\kappa$. If $L > L_{ed}$, radiation pressure exceeds gravity in the outer regions, disrupting hydrostatic equilibrium and potentially driving mass loss.

### 3.2 Numerical Evaluation and Connection to the Upper Mass Limit

To evaluate $L_{ed}$ numerically, express $M$ in solar masses and use CGS values. In hot, massive stars the dominant opacity source is electron scattering (Thomson scattering), for which:

$$\kappa = 0.2(1+X)$$

where $X$ is the hydrogen mass fraction. Adopting a typical value $X = 0.7$:

$$\kappa = 0.2(1+0.7) = 0.34\ \text{cm}^2\ \text{g}^{-1}$$

Substituting the constants $G = 6.7\times10^{-8}$ dyn cm$^2$ g$^{-2}$, $c = 3\times10^{10}$ cm s$^{-1}$, $M_\odot = 2\times10^{33}$ g:

$$L_{ed} \sim 1.5\times10^{38}\ \frac{M}{M_\odot}\ \text{erg s}^{-1}$$

Converting to solar luminosities ($L_\odot = 4\times10^{33}$ erg s$^{-1}$):

$$\frac{L_{ed}}{L_\odot} \approx 3.8\times10^4 \frac{M}{M_\odot}$$

For a $90\, M_\odot$ star this gives $L_{ed} \approx 3.5\times10^6\, L_\odot$. Crucially, the observed and theoretical luminosity of a $90\, M_\odot$ ZAMS star is only about 3 times smaller than $L_{ed}$. This near-coincidence explains why stars more massive than $\sim 90\, M_\odot$ are extremely difficult to form stably at solar metallicity: their own luminosity is close enough to the Eddington limit that radiative forces make the structure unstable.

---

## 4. Hydrogen Burning Modes on the ZAMS

### 4.1 Two Chains and Their Temperature Thresholds

Every star on the ZAMS is a core hydrogen-burning star. The conversion of hydrogen into helium proceeds by one of two thermonuclear chains, which have different activation temperatures:

- **pp chain** (proton-proton chain): ignites at $T_c \approx 1.4\times10^7$ K. This is the dominant process in low-mass stars including the Sun.
- **CNO cycle** (carbon-nitrogen-oxygen cycle): ignites at $T_c \approx 1.8\times10^7$ K. This requires slightly higher temperatures but becomes overwhelmingly dominant at higher masses.

Because the core temperature $T_c$ increases with stellar mass, there is a transition mass above which the CNO cycle takes over. This transition occurs at a surprisingly low mass:

$$M_{transition} \approx 1.2\, M_\odot$$

At $1\, M_\odot$, $T_c = 1.4\times10^7$ K and the pp chain dominates. At $15\, M_\odot$, $T_c = 3.4\times10^7$ K and the CNO cycle dominates entirely. In the Sun, the ratio $\epsilon_{pp}/\epsilon_{CNO} \sim 100$, confirming that the pp chain contributes about 99% of the solar luminosity.

### 4.2 The Dramatic Temperature Dependence of the CNO Cycle

The energy generation rates for the two processes depend on temperature very differently:

$$\epsilon_{pp} \propto \rho X^2 T_6^5 \qquad \epsilon_{CNO} \propto \rho X Z_{CNO} T_6^{15}$$

where $T_6$ is the temperature in units of $10^6$ K, $X$ is the hydrogen mass fraction, and $Z_{CNO}$ is the mass fraction of CNO catalyst elements. The exponent $n \sim 15$ for the CNO cycle versus $n \sim 5$ for the pp chain is the central fact driving all subsequent differences in stellar structure and evolution.

Although the core temperatures differ only modestly between low-mass and high-mass ZAMS stars (both are in the range of a few times $10^7$ K), the CNO cycle's extreme temperature sensitivity ($T_6^{15}$) makes $\epsilon_{CNO}$ tremendously larger than $\epsilon_{pp}$ even for modest temperature increases. This has the consequence that in $M > 1.2\, M_\odot$ stars, essentially 90% of the luminosity is generated within the innermost 10% of the stellar mass — a much more centrally concentrated energy production than in the Sun, where 70% of the luminosity comes from the innermost 20%.

### 4.3 CNO Burning Sets the Stellar Structure: Why High-Mass Stars Have Convective Cores

The concentrated energy production of the CNO cycle directly causes the central convection in massive stars. The relevant condition for convection is:

$$\nabla_{rad} > \nabla_{ad}$$

The radiative temperature gradient is:

$$\left.\frac{dT}{dr}\right|_{rad} = -\frac{3\kappa\rho}{4acT^3} \frac{L_r}{4\pi r^2}$$

When $\epsilon_{CNO}$ is large (due to its steep temperature dependence), $L_r$ rises very steeply near the centre. Combined with the concentrated nature of the energy production (large $L_r/r^2$ term), $\nabla_{rad}$ exceeds $\nabla_{ad}$ in the core, triggering convection. Thus:

$$\text{H-burning via CNO cycle} \implies \text{convective core}$$

In contrast, the pp chain distributes energy production over a larger volume, so $L_r$ rises more gradually and the core remains radiative. The conclusion is that the type of hydrogen burning, determined entirely by stellar mass, determines whether the core is convective or radiative.

---

## 5. Stellar Structure Along the ZAMS: Three Regimes

### 5.1 Overview of the Three Mass Regimes

The internal structure of a ZAMS star — specifically, where convection occurs — depends on its mass. Two transition masses define three structural regimes:

1. $M > 1.2\, M_\odot$: convective core, radiative envelope
2. $0.3\, M_\odot < M < 1.2\, M_\odot$: radiative core, convective envelope
3. $M < 0.3\, M_\odot$: fully convective

These are not arbitrary divisions but arise from two distinct physical mechanisms, each explained below.

### 5.2 Stars with $M > 1.2\, M_\odot$: Convective Core, Radiative Envelope

As discussed in Section 4.3, CNO burning produces an intense, concentrated flux in the core, causing $\nabla_{rad} > \nabla_{ad}$ and therefore convection. For a $5\, M_\odot$ star, the structure is approximately:

- Innermost ~10% by radius: the H-burning region where nuclear reactions occur
- 10–30% of the radius: the convective zone (driven by the high flux from the burning region)
- Outer 70% of the radius: radiative envelope

This convective core has profound implications for subsequent evolution because it homogenizes the composition within the core. Any hydrogen anywhere inside the convective zone is mixed throughout, enlarging the effective fuel reservoir and creating the flat-topped H-abundance profiles discussed in Section 9.

### 5.3 Stars with $0.3\, M_\odot < M < 1.2\, M_\odot$: Radiative Core, Convective Envelope

In this intermediate regime, the core burns hydrogen via the pp chain, which is less concentrated and does not drive core convection. The core is therefore radiative. For a $1\, M_\odot$ star the structure is approximately:

- Innermost ~20% by radius: H-burning, radiative
- 20–70% by radius: radiative envelope
- Outer 30% by radius: convective zone

The convective envelope arises from two separate physical effects acting together:

1. Low surface temperatures cause high opacity via the Kramers law: $\kappa \propto T^{-3.5}$. Higher opacity increases $\nabla_{rad}$, pushing it above $\nabla_{ad}$ in the outer layers.
2. Partially ionized zones in the outer stellar layers reduce the adiabatic gradient from its standard value of 0.4 down toward 0.1. Recall that $\nabla_{ad} = 1 - 1/\gamma$ where $\gamma = c_P/c_V$. In partial ionization zones, both $c_P$ and $c_V$ increase strongly (energy goes into ionization rather than heating), so $\gamma \to 1$ and $\nabla_{ad} \to 0$. When $\nabla_{ad}$ drops, the condition $\nabla_{rad} > \nabla_{ad}$ is satisfied even with modest radiative flux.

Both effects together — elevated $\nabla_{rad}$ and depressed $\nabla_{ad}$ — cooperate to make the outer stellar layers convective. This is why the Sun, and all stars in this mass range, have convective envelopes above their radiative interiors. The transition of the adiabatic gradient is visible in plots of $\nabla$ vs $\log P$: $\nabla_{ad}$ stays near 0.4 in the fully ionized interior, dips sharply toward 0.1 in the partial ionization zones near the surface, and the shaded region where $\nabla_{rad} > \nabla_{ad}$ marks the convective region.

### 5.4 Very Low-Mass Stars with $M < 0.3\, M_\odot$: Fully Convective

The lowest-mass main-sequence stars are fully convective from centre to surface. The physics is essentially an extreme version of the convective envelope mechanism: with very low temperatures throughout, the opacity is very high everywhere, and the adiabatic gradient is suppressed in large portions of the star by partial ionization. The convective instability condition is satisfied throughout the entire stellar volume. The Hayashi track for these stars is very nearly coincident with the ZAMS — their pre-MS track merges into the ZAMS because the convective structure changes very little upon H-ignition.

---

## 6. Effect of Burning Mode on Core Temperature and the Mass-Luminosity Relation

### 6.1 The CNO Cycle Limits Core Temperature Growth

If all stars burned hydrogen via the pp chain, the core temperature would need to increase steeply with mass to sustain higher luminosities. The CNO cycle, with its enormously stronger temperature dependence, allows the same (or larger) luminosity to be produced at much lower core temperatures. A plot of $T_c$ vs $M/M_\odot$ shows two curves:

- If only pp burning operated: core temperature would rise steeply (dashed red curve)
- With CNO burning dominant above $\sim 1.2\, M_\odot$: core temperature increase is dramatically flattened (solid black curve)

In numerical terms from the ZAMS data table (solar metallicity $Z=0.02$, $Y=0.27$): a $1.5\, M_\odot$ star has $T_c \approx 1.81\times10^7$ K, while a $7\, M_\odot$ star has $T_c \approx 2.91\times10^7$ K. A factor-of-~5 increase in mass corresponds to only a factor of about 1.6 in central temperature — because the CNO cycle does not need extreme temperatures to generate the required luminosity.

This has a crucial secondary consequence: at increasing mass, the central density $\rho_c$ also **decreases**. From the ZAMS data table:
- $0.1\, M_\odot$: $\rho_c \approx 402.5$ g cm$^{-3}$
- $7.0\, M_\odot$: $\rho_c \approx 13.5$ g cm$^{-3}$

High-mass stars have significantly less dense cores than low-mass stars. This matters enormously for later evolution: low density makes electron degeneracy far less likely in high-mass cores, as the degeneracy condition $T/\rho^{2/3} < D \approx 10^5$ is much harder to satisfy at low $\rho$.

### 6.2 The Mass-Luminosity Relation and Its Change Across the ZAMS

The different burning processes also modify the mass-luminosity relation, producing a broken power law:

- **Upper main sequence** ($M \gtrsim 1.2\, M_\odot$, CNO burning): $L \approx M^{3.6}$ (shallower slope)
- **Lower main sequence** ($M \lesssim 1.2\, M_\odot$, pp burning): $L \approx M^{4}$ to $M^{4.5}$ (steeper slope)
- **Very low mass** ($M \ll 1\, M_\odot$): $L \approx M^{2.6}$ (shallowest slope)

The shallower slope in the upper main sequence occurs because the CNO cycle limits the temperature increase, meaning that each added unit of mass contributes a smaller fractional gain in luminosity than it would if the pp chain were operating. The broken power law is directly measurable in log-log plots of $L$ vs $M$ for main-sequence stars.

### 6.3 Summary of the Four Effects of CNO Burning

The CNO burning process, which dominates in stars above $\sim 1.2\, M_\odot$, has four distinct effects:

1. **Stellar structure**: CNO burning sets convective cores in stars above $1.2\, M_\odot$
2. **Core temperature**: CNO burning limits the otherwise steep increase of $T_c$ with mass
3. **Mass-luminosity relation**: CNO burning reduces the power-law exponent (shallower $L$ vs $M$ dependence)
4. **Post-MS evolutionary tracks**: CNO burning shapes the hydrogen-abundance profile inside the star, producing a clear signature (the "hook") in the evolutionary tracks immediately after hydrogen exhaustion — discussed in detail in Section 9

---

## 7. Metallicity and Helium Abundance Effects on the ZAMS

### 7.1 Metallicity Effects ($Z \nearrow$, $Y$ fixed)

Metallicity $Z$ affects stellar structure primarily through its influence on opacity. An increase in metallicity raises opacity (more metal atoms and ions contribute to bound-free and bound-bound absorption). Higher opacity means a steeper radiative temperature gradient, so the star must be less luminous (fainter) and cooler (redder) to maintain hydrostatic equilibrium. Consequences:

- **Higher $Z$**: stars are fainter and cooler at given mass — the ZAMS shifts down and to the right in the HR diagram. Fainter, cooler stars radiate more slowly, so they have **longer MS lifetimes**.
- **Lower $Z$**: stars are brighter and hotter — the ZAMS shifts up and to the left. Additionally, at low metallicity ($Z = 0.0001$), CNO elements are scarce, so CNO burning is suppressed. The pp chain dominates longer and at higher masses, requiring higher core temperatures to generate the same luminosity. This is why low-metallicity stars have systematically **hotter cores**: the $T_c$ vs $M/M_\odot$ curve lies well above the solar-metallicity curve.

For stellar populations, these effects translate into changes in the turnoff mass at fixed age. Because higher-$Z$ stars are fainter and live longer, at any given age a metal-rich population has a **larger turnoff mass** than a metal-poor one. Specifically, at 13 Gyr: the $Z=0.0001$ isochrone has a turnoff mass of $0.77\, M_\odot$ while the $Z=0.02$ isochrone has a turnoff mass of $0.85\, M_\odot$.

### 7.2 Helium Abundance Effects ($Y \nearrow$, $Z$ fixed)

Helium content $Y$ affects stellar structure through two channels:

1. **Opacity**: increasing $Y$ (at fixed $Z$) decreases the hydrogen fraction $X = 1 - Y - Z$, reducing radiative opacity (since hydrogen contributes substantially to electron scattering opacity).
2. **Mean molecular weight**: increasing $Y$ increases $\mu$, since helium nuclei are heavier per electron than hydrogen. This makes the gas more compact and hotter at fixed mass, driving a more luminous structure.

The combined effect of increased $Y$ is a **brighter and hotter** star. The luminosity scales approximately as $L \approx \mu^7$, so even modest helium enhancements produce large luminosity increases. For a $5\, M_\odot$ star at fixed $Z=0.02$:
- $Y = 0.20$: baseline track
- $Y = 0.30$: noticeably brighter and hotter
- $Y = 0.40$: significantly brighter and hotter, strongly shifted to the upper left of the HR diagram

Since He-enhanced stars are brighter, they burn through fuel faster and have shorter lifetimes. At fixed age a He-rich population therefore has a **smaller turnoff mass**. At 13 Gyr with $Z=0.002$: $Y=0.24$ gives $M_{TO} = 0.79\, M_\odot$, while $Y=0.40$ gives only $M_{TO} = 0.59\, M_\odot$.

---

## 8. The Main Sequence as an Evolutionary Phase

### 8.1 Definition of the Main Sequence: Points 1 and 2

The main sequence (MS) as an **evolutionary phase** is the period of core hydrogen burning, spanning from the moment of H-ignition (**Point 1** on an evolutionary track) to the moment of H-exhaustion in the core (**Point 2**, defined as $X_c < 0.05$). In the HR diagram, the set of all Point 2 positions across different mass tracks form a "terminal age main sequence" (TAMS) locus that runs roughly parallel to the ZAMS. Every star between Point 1 and Point 2 is on the main sequence. The segment between Point 2 and Point 3 (H-ignition in the shell) is discussed in Section 10.

### 8.2 Timescale: Why the MS is the Longest Phase

The core H-burning phase is by far the longest evolutionary stage in a star's life. This is because the H-burning process (in either chain) is the most energetically efficient thermonuclear reaction per unit of fuel, and it operates on a very large fuel reservoir (essentially the entire stellar core).

The MS lifetimes from theory (solar metallicity):

| $M/M_\odot$ | 15.0 | 9.0 | 5.0 | 3.0 | 2.25 | 1.5 | 1.0 |
|---|---|---|---|---|---|---|---|
| $t_{MS}$ (yr) | $10^7$ | $2.2\times10^7$ | $7\times10^7$ | $2\times10^8$ | $5\times10^8$ | $1.7\times10^9$ | $9\times10^9$ |

A simple approximate scaling law encapsulates this strong dependence:

$$t_{MS} \cong 10^{10}\, M^{-3}\ \text{yr}$$

where $M$ is in solar masses. This relation arises from the mass-luminosity law ($L \propto M^4$ roughly) combined with the fact that the total fuel is proportional to $M$: $t_{MS} \propto M/L \propto M^{-3}$.

The MS lifetime decreases very steeply with mass. For $10\, M_\odot$: $t_{MS} \sim 10^7$ yr. For $1\, M_\odot$: $t_{MS} \sim 10^{10}$ yr. An intriguing cosmological corollary: the MS lifetime of a $\sim 0.8\, M_\odot$ star is comparable to the Hubble time ($\sim 13.8\times10^9$ yr). Therefore, **all stars with $M \lesssim 0.8\, M_\odot$ that formed at the epoch of the Big Bang are still on the main sequence today**, still burning hydrogen in their cores. The MS for low-mass stars effectively stretches across cosmic time.

### 8.3 Solar Evolution During the Main Sequence

Although the MS is the most quiescent evolutionary phase, stellar properties do change slowly. In the Sun over its $\sim 4.6$ Gyr lifetime:

- Luminosity has increased from $\sim 0.7\, L_\odot$ to the current $1.0\, L_\odot$ — an increase of about 30%
- Radius has increased modestly
- Effective temperature $T_{eff}$ has increased from $\sim 5650$ K to $\sim 5780$ K

These macroscopic changes are slow (driven by the thermonuclear timescale) but cumulatively significant. The key driver is the rising mean molecular weight as H converts to He in the core (see Section 9.1). The density profile drops steeply from $\sim 160$ g cm$^{-3}$ at the centre to near zero at $r/R_\odot \sim 0.5$. The luminosity profile, plotted vs radius, rises steeply from the core and reaches a flat plateau ($L_r = L_\odot = $ constant) by $r/R_\odot \approx 0.25$. This means **no energy is produced in the outer 75–80% of the Sun by radius** — the outer solar volume is purely a radiative transport layer.

The current solar core abundances ($X=0.35$, $Y=0.63$, $Z=0.02$) represent roughly halfway through hydrogen burning relative to the initial values ($X=0.71$, $Y=0.27$, $Z=0.02$) and the future exhausted state ($X=0.00$, $Y=0.98$, $Z=0.02$).

A notable feature is the $^3$He abundance peak: the pp chain produces $^3$He as an intermediate via $H^2 + H^1 \to {^3\text{He}} + \gamma$, but in regions of moderate temperature the subsequent reaction $^3\text{He} + {^3\text{He}} \to {^4\text{He}} + H^1 + H^1$ is slow. This leads to a buildup of $^3$He (visible as a small peak in the abundance profile at intermediate radii), a direct observational signature of the incomplete pp chain at those temperatures.

Near the solar surface, diffusive settling slowly depletes heavier elements downward, slightly lowering the surface helium abundance over billions of years. The standard solar model must account for this effect.

---

## 9. MS Evolution: The Segment 1–2 and the Role of Mean Molecular Weight

### 9.1 Physics of the Evolving Core: $\mu$ Increases as H Converts to He

As hydrogen is consumed in the core, four hydrogen nuclei combine into one helium nucleus. This reduces the total number of free particles in the gas. In a fully ionised plasma the mean molecular weight is:

$$\mu = \frac{1}{2X + \frac{3}{4}Y + \frac{1}{2}Z}$$

As $X$ decreases and $Y$ increases (with $Z$ fixed), the denominator decreases and $\mu$ increases. Concrete values for the solar core:

| Epoch | $X$ | $Y$ | $Z$ | $\mu$ |
|---|---|---|---|---|
| Initial | 0.71 | 0.27 | 0.02 | 0.62 |
| Current | 0.35 | 0.63 | 0.02 | 0.85 |
| Future (exhausted) | 0.00 | 0.98 | 0.02 | 1.35 |

Since the gas pressure is $P = k\rho T/\mu H$ (where $H$ is the atomic mass unit), an increase in $\mu$ at fixed temperature reduces the pressure. The chain of consequences:

$$\mu \nearrow \implies P \searrow \implies \text{core contracts} \implies \rho \nearrow,\ T \nearrow$$

The star is a virialized structure, so core contraction converts gravitational potential energy into thermal energy, raising $T_c$. Higher temperature increases the burning efficiency: $\epsilon \nearrow$ and $L \nearrow$. The process operates on the thermonuclear timescale — extremely slow, but inexorable throughout the MS phase.

### 9.2 Segment 1–2 for Low-Mass Stars ($M < 1.2\, M_\odot$)

In low-mass stars burning via the pp chain ($\epsilon_{pp} \propto \rho X^2 T_6^5$, $n \sim 5$), two competing effects operate simultaneously:

1. The rising core temperature tends to **increase** $\epsilon_{pp}$ (temperature dominates with $T^5$)
2. The decreasing hydrogen abundance $X$ tends to **decrease** $\epsilon_{pp}$ (fuel depletion)

The temperature effect dominates, so $\epsilon \nearrow$ and $L \nearrow$. The increased luminosity drives an expansion of the stellar structure.

In low-mass stars, the pp chain burns hydrogen over a relatively large volume (approximately 20–30% by radius). This means the $\mu$-driven core contraction affects a significant fraction of the stellar mass. Two competing global effects result:

- Core contraction (due to $\mu \nearrow$) partially counteracts the expansion
- Expansion of the outer structure (due to $L \nearrow$) drives the radius outward

These effects partially cancel. The net result is that $R$ increases, but not enough to compensate the growth of $L$ fully. Since $L = 4\pi R^2 \sigma T_{eff}^4$, if $L$ grows faster than $R^2$, then $T_{eff}$ increases. The low-mass MS track therefore moves **slightly upward and to the left** (slightly higher luminosity, slightly hotter) during segment 1–2. The increase in $T_{eff}$ is small because the competing effects nearly cancel, but it is in the correct direction.

A key reminder: an increase in $R$ at fixed $L$ would cool the surface ($T_{eff} \searrow$); here the luminosity increases fast enough that $T_{eff}$ still rises slightly despite $R$ also increasing.

### 9.3 Segment 1–2 for High-Mass Stars ($M > 1.2\, M_\odot$)

In high-mass stars burning via the CNO cycle ($\epsilon_{CNO} \propto \rho X Z_{CNO} T_6^{15}$, $n \sim 15$), the temperature sensitivity is so extreme that the hydrogen depletion ($X \searrow$) has only a modest impact on $\epsilon$; the rising $T$ dominates. Again $L \nearrow$.

The crucial geometric difference: the CNO cycle operates in a very compact region (inner ~10% by radius, contributing ~90% of the luminosity). Therefore, the $\mu$-driven contraction is localised in a small core volume and does **not** significantly counteract the overall expansion of the stellar envelope driven by increased luminosity. The expansion of the outer layers is essentially unopposed.

The result is a **substantial increase in the stellar radius** $R$, which — since $L = 4\pi R^2 \sigma T_{eff}^4$ and $R^2$ grows fast — drives $T_{eff}$ downward. The high-mass MS track therefore moves **upward and to the right** during segment 1–2: the star becomes more luminous but also significantly cooler (more extended). This is clearly visible in HR diagrams as the rightward slope of the upper-MS tracks.

**The fundamental explanation for the different MS track morphology** is the **different spatial extent of the nuclear burning region**, set by the different H-burning process. The pp chain involves ~20–30% of the stellar radius; the CNO cycle involves only ~10%. This geometric difference, not any difference in total luminosity or temperature, is what distinguishes the two regimes.

---

## 10. Post-MS Evolution: The Segment 2–3

### 10.1 Overview: Point 2 Marks H-Core Exhaustion

Point 2 marks hydrogen exhaustion in the core ($X_c < 0.05$). What happens next depends critically on the hydrogen-abundance profile left inside the star by the preceding core-burning phase. This H-profile shape is entirely determined by whether the core was convective (high-mass, CNO burning) or radiative (low-mass, pp burning). The segment 2–3 is where the most notable structural difference between the two mass regimes manifests.

### 10.2 H-Profile Shape: Radiative vs Convective Core

**Low-mass stars ($M < 1.2\, M_\odot$), radiative cores:** The pp chain burns hydrogen in a smooth, diffuse region without any sharp mixing boundaries. Hydrogen is consumed progressively from the centre outward, creating a smooth gradient H-abundance profile. At any time, $X$ decreases monotonically from the surface value to some minimum at the centre. The burning history is visible as a nested set of increasingly depleted curves over time (0, 1.4, 4.2, 6.6, 8.6 Gyr snapshots show the centre continuously depleting). The boundary between the H-exhausted zone and the H-rich envelope is gradual — there is no sharp edge.

**High-mass stars ($M > 1.2\, M_\odot$), convective cores:** Convection continuously mixes the entire core, maintaining a **flat, uniform hydrogen abundance** within the convective zone at all times. The H-profile therefore has a characteristic step shape: $X \approx \text{const}$ (the current average core value) for all mass coordinates inside the convective boundary, then a sharp step up to the initial abundance at the convective boundary, then the undepleted envelope. Over time (time snapshots labeled 1–7):

- $X_{core}$: 0.71 → 0.62 → 0.40 → 0.21 → 0.10 → 0.01 → 0.00
- The convective core boundary **retreats inward** over time (shrinks), because as H is converted to He, the opacity decreases: $\kappa_{FF} \propto 10^{22}(X+Y)(1+X)\rho/T^{3.5}$. A He-rich mixture has lower opacity, so $\nabla_{rad}$ decreases, and the convective zone shrinks. This leaves behind a composition gradient in the intermediate zone between the former convective core and the outer unprocessed envelope.
- At point 2, the **entire convective core reaches $X = 0$ simultaneously** — all the hydrogen within the zone is exhausted at the same moment.

### 10.3 Transition at Point 2 for Low-Mass Stars: Smooth to Shell Burning

For low-mass stars, the smooth, gradient H-profile ensures a seamless transition. When the centre first reaches $X \approx 0$, the adjacent shell immediately has hydrogen available and is already at nearly the right temperature (since the temperature profile is continuous). H-shell burning ignites without a pause, and points 2 and 3 effectively coincide. There is no interruption of thermonuclear activity.

The evolutionary track during segment 2–3 shows a **smooth, continuous upward curvature** — the star gently moves off the main sequence and up the subgiant branch without any discontinuity or hook. Low-mass stars do not have hooks because their H-profile never creates a scenario where no thermonuclear burning is available.

### 10.4 Transition at Point 2 for High-Mass Stars: Gravitational Contraction Phase and the Hook

For high-mass stars, the step-function H-profile creates a structural crisis at point 2. When the convective core reaches $X = 0$ simultaneously everywhere, the star faces a situation where:

- The core is entirely exhausted of hydrogen and **too cool to ignite helium** (He burning via the triple-alpha reaction requires $T \sim 10^8$ K, far above the current $T_c \sim$ a few $\times 10^7$ K)
- The hydrogen shell just above the former convective core boundary is **too cool to immediately ignite H-burning** (it has been far from the burning region and is at a lower temperature)

There is therefore a brief phase of **no thermonuclear energy production** anywhere in the star. With no nuclear energy source, the entire stellar structure contracts under gravity. This contraction proceeds on the **Kelvin-Helmholtz (thermodynamic) timescale** — much shorter than the nuclear timescale but still slow compared to dynamical timescales. The energy radiated during this phase comes entirely from **gravitational contraction** (labeled "G" on the evolutionary tracks). The contraction raises the temperature of the shell, and eventually (at point 3), the shell becomes hot enough to ignite H-burning.

In the HR diagram, this gravitational contraction phase produces the characteristic **hook**: the star's track swings back rapidly (during the contraction phase, the structure contracts and becomes slightly hotter and smaller, causing $T_{eff}$ to rise temporarily), forming a hook-like feature at the turnoff before settling back to lower $T_{eff}$ as the shell ignites and drives envelope expansion. The hook is a direct observational signature of a convective core during the MS.

**Observational confirmation:** The Color-Magnitude Diagram of the globular cluster NGC 1978 (observed with HST/ACS, age $\sim 2$ Gyr, $M_{TO} \approx 1.5\, M_\odot$) shows a prominent hook feature at the main-sequence turnoff. The arrows point directly to this morphological feature, confirming the theoretical prediction. This is one of the clearest observational validations of the convective core scenario in intermediate-mass stars.

### 10.5 Summary of Points 1, 2, 3 for Both Mass Regimes

| Point | Physical event | Low mass ($M < 1.2\, M_\odot$) | High mass ($M > 1.2\, M_\odot$) |
|---|---|---|---|
| **1** | H-ignition in the core (ZAMS) | Chemically homogeneous | Same |
| **2** | H-exhaustion in the core | Smooth gradient reaches 0 at centre | Entire convective core reaches $X=0$ simultaneously |
| **3** | H-ignition in shell | Simultaneous with Point 2 (no gap) | After gravitational contraction phase (hook between 2 and 3) |

---

## 11. The Growing Isothermal Helium Core

### 11.1 Formation and Nature of the Isothermal Core

From Point 3 onward, all stars have a helium core that is thermonuclearly inactive: $\epsilon = 0$ and $L(r) = 0$ for mass coordinates within the core. The energy is produced entirely in the thick H-burning shell above the core.

Because there is no energy source in the core ($L_r = 0$), the radiative temperature gradient is:

$$\left.\frac{dT}{dr}\right|_{rad} = -\frac{3\kappa\rho}{4acT^3}\frac{L(r)}{4\pi r^2} = 0$$

A zero temperature gradient means the core is **isothermal** — it has the same temperature throughout its volume. This isothermal He core is a physically distinct substructure: a uniformly-temperature helium sphere with no internal energy production, surrounded by the actively burning thick H-shell.

The mass of this isothermal core grows continuously as the H-shell converts hydrogen to helium and deposits freshly synthesized He onto the core surface. The thick shell is essentially a one-way conveyor belt, feeding mass into the growing core.

The burning rate in the shell is quantified by $\epsilon = dL/dm$, proportional to the slope of the luminosity profile just outside the core. In the $1\, M_\odot$ interior structure plot at this stage (labeled "Figure 9.3"), the luminosity rises from zero in the core to $L_\odot$ very steeply just outside the He core, confirming a very high energy generation rate in the thin shell. A dashed red line drawn tangent to this steep rise visually illustrates the large value of $dL/dm$.

The stellar interior at Point 3 (for $1\, M_\odot$) shows: the temperature profile is completely flat in the isothermal core (horizontal curve in the $T$ vs $m(r)/M$ plot), rising steeply in and above the shell; the luminosity is zero for all $r$ inside the core and rises sharply at the shell. The profile for the star "between points 2 and 3" (Figure 9.2 reference) shows the same isothermal characteristic.

### 11.2 Hydrostatic Balance in the Isothermal Core

Even without nuclear burning, the isothermal core must maintain hydrostatic equilibrium. With $dT/dr = 0$, pressure support against gravity comes from the density gradient:

$$-\frac{GM\rho}{r^2} = \frac{dP}{dr} = \frac{kT}{\mu H}\frac{d\rho}{dr}$$

A density gradient from centre outward (density higher in the centre) provides the necessary outward pressure gradient. This works because $P = k\rho T/\mu H$, and even at fixed $T$, a density gradient creates a pressure gradient. However, this hydrostatic balance has a physical maximum — the Schönberg-Chandrasekhar mass limit — as derived in Section 12.

### 11.3 Key Parameter: The Core Mass Fraction $q$

The parameter $q$ is defined as the fraction of the total stellar mass contained in the He core:

$$q = \frac{M_c}{M_{tot}}$$

This parameter grows continuously as the thick shell deposits He onto the core. It is a key diagnostic: as $q$ increases, the core must offer more pressure to support the overlying envelope. The SC limit specifies the maximum $q$ the isothermal core in perfect gas conditions can sustain.

---

## 12. The Schönberg-Chandrasekhar Mass Limit

### 12.1 Physical Concept

The **Schönberg-Chandrasekhar (SC) limit** is the maximum mass that an isothermal core in perfect gas (ideal gas) conditions can support against the weight of the overlying envelope while maintaining hydrostatic equilibrium. It was derived analytically by Schönberg and Chandrasekhar in 1942.

The physical competition is between:
- **Thermal pressure**: the kinetic energy of gas particles tends to increase the core pressure, supporting it against gravity
- **Self-gravity of the core**: the gravitational self-energy of the core tends to reduce the effective pressure available to support the envelope

As the core mass grows, its self-gravity increases, and the maximum pressure it can supply decreases. When the core becomes too massive, it can no longer support itself against the envelope pressure, and it begins to contract.

### 12.2 Two Equivalent Formulations

**Formulation 1 (mass fraction):**

$$q \leq q_0 = 0.37\left(\frac{\mu_e}{\mu_{ic}}\right)^2$$

where $\mu_e$ is the mean molecular weight of the envelope (H-rich, $\mu_e \approx 0.62$) and $\mu_{ic}$ is the mean molecular weight of the isothermal inner core (He-rich, $\mu_{ic} \approx 1.33$). The ratio $(\mu_e/\mu_{ic})^2 \approx (0.62/1.33)^2 \approx 0.22$, giving $q_0 \approx 0.37 \times 0.22 \approx 0.08$. When $q > q_0$, the core begins to contract.

**Formulation 2 (absolute mass):**

$$M_c \leq M_{sc} = 0.10\, M_{tot}$$

When the core mass exceeds approximately 10% of the total stellar mass, the SC limit is exceeded. The two formulations are equivalent for typical compositions; both capture the same physical threshold.

### 12.3 Derivation of the SC Limit

**Step 1 — Maximum pressure the isothermal core can supply.**

Starting from hydrostatic equilibrium in mass coordinates:

$$\frac{dP}{dM_r} = -\frac{GM_r}{4\pi r^4}$$

Multiply both sides by $4\pi r^3$ and manipulate using the product rule for $d(4\pi r^3 P)/dM_r$:

$$\frac{d(4\pi r^3 P)}{dM_r} - 3\frac{P}{\rho} = -\frac{GM_r}{r}$$

Integrate over the isothermal core mass ($0$ to $M_{ic}$):

$$4\pi R_{ic}^3 P_{ic} - 2K_{ic} = U_{ic}$$

where:
- Term (1): $\int_0^{M_{ic}} d(4\pi r^3 P)/dM_r\, dM_r = 4\pi R_{ic}^3 P_{ic}$ (boundary term; inner boundary is zero by symmetry)
- Term (2): $\int_0^{M_{ic}} 3P/\rho\, dM_r = 3kT_{ic}/(\mu_{ic}H) \cdot M_{ic} = 2K_{ic}$ where $K_{ic} = \frac{3}{2}N_{ic}kT_{ic}$ is the total thermal kinetic energy ($N_{ic} = M_{ic}/\mu_{ic}H$ is the total number of particles)
- Term (3): $\int_0^{M_{ic}} GM_r/r\, dM_r = -U_{ic}$ where $U_{ic} = -\frac{3}{5}GM_{ic}^2/R_{ic}$ is the gravitational self-energy (for a uniform-density sphere, derived as $U = -3GM^2/5R$)

This is a generalized virial theorem for the core subregion. The full stellar virial theorem ($2K + U = 0$) emerges when this is integrated to the stellar surface (where $P = 0$).

Rearranging to express the core pressure:

$$P_{ic} = \frac{3}{4\pi R_{ic}^3}\left(\frac{M_{ic}kT_{ic}}{\mu_{ic}H} - \frac{1}{5}\frac{GM_{ic}^2}{R_{ic}}\right)$$

This is the difference between thermal energy (first term, supports the core) and gravitational energy (second term, works against the pressure). To find the radius $R_{ic}$ that maximises $P_{ic}$, set $dP_{ic}/dR_{ic} = 0$:

$$\frac{dP_{ic}}{dR_{ic}} = 0 \implies R_{ic}^{max} = \frac{4}{15}\frac{GM_{ic}\mu_{ic}H}{kT_{ic}}$$

This is the core radius at which it offers maximum pressure. Substituting back gives the maximum pressure available:

$$P_{ic}^{max} = \frac{3\cdot 15^3}{4^5\pi}\left(\frac{kT_{ic}}{\mu_{ic}H}\right)^4 \frac{1}{G^3 M_{ic}^2}$$

The critical property: $P_{ic}^{max}$ **decreases** as $M_{ic}^2$ in the denominator increases. A more massive core is inherently less able to support itself.

**Step 2 — Pressure exerted by the envelope on the core.**

Integrating hydrostatic equilibrium over the envelope mass (with approximations: $M_{ic}^2 \ll M^2$, $\langle r^4\rangle \approx R^4/2$):

$$P_{env} \approx \frac{GM^2}{4\pi R^4}$$

Using the envelope gas pressure to estimate the stellar radius $R$:

$$R \sim \frac{1}{3}\frac{GM\mu_{env}H}{kT_{ic}}$$

Substituting this $R$ into $P_{env}$:

$$P_{env} \sim \frac{81}{4\pi}\frac{1}{G^3 M^2}\left(\frac{kT_{ic}}{\mu_{env}H}\right)^4$$

Note that $P_{env}$ scales as $1/M^2$: a more massive star exerts more pressure on its core.

**Step 3 — Equating $P_{ic}^{max} = P_{env}$ to find the SC limit.**

$$\frac{3\cdot15^3}{4^5\pi}\frac{1}{\mu_{ic}^4 M_{ic}^2} = \frac{81}{4\pi}\frac{1}{M^2\mu_{env}^4}$$

Solving for $M_{ic}/M$:

$$\left(\frac{M_{ic}}{M}\right)^2 = \frac{3\cdot15^3}{4^4\cdot81}\left(\frac{\mu_{env}}{\mu_{ic}}\right)^4$$

$$\frac{M_{ic}}{M} \approx 0.7\left(\frac{\mu_{env}}{\mu_{ic}}\right)^2$$

The course estimate gives 0.7; the exact Schönberg-Chandrasekhar result is **0.37**. The discrepancy reflects the approximations in estimating $P_{env}$ and $R$. The structural form of the result — proportional to $(\mu_{env}/\mu_{ic})^2$ — is exact.

**Physical interpretation of the formula:** The SC limit scales as $(\mu_{env}/\mu_{ic})^2$. Since the core (He-rich) has higher $\mu_{ic}$ than the envelope (H-rich), the ratio is less than 1, giving $q_0 < 0.37$. If the core and envelope had the same composition, $\mu_{ic} = \mu_{env}$ and the limit would be $q_0 \approx 0.37$ — but in that case, the "core" would not be a chemically distinct substructure. The SC limit is fundamentally a consequence of the **chemical contrast** between the He-rich core (product of nuclear burning) and the H-rich envelope.

### 12.4 Consequences of Exceeding the SC Limit

When the core mass exceeds the SC limit, the core begins to contract on the Kelvin-Helmholtz timescale. Contraction raises the core temperature and establishes a temperature gradient ($dT/dr \neq 0$), ending the strictly isothermal phase. Whether this contraction heats the core enough to ignite He burning depends critically on whether the core is in perfect gas or degenerate conditions — as determined by stellar mass.

---

## 13. Mass-Dependence of Core Conditions After the MS

### 13.1 Three Mass Regimes for Post-MS Core Behavior

The condition of the growing He core — whether it remains ideal gas or enters electron degeneracy — is the pivotal question determining the entire subsequent evolutionary path (RGB, helium flash, or direct He ignition). Three distinct regimes exist:

**Regime 1 — $M > 6\, M_\odot$ (no isothermal core):**
The convective core mass at the ZAMS already represents a large enough fraction of the total mass that, upon H-exhaustion, contraction begins immediately. There is no stable isothermal phase. The core remains in ideal gas conditions throughout its evolution — the core's trajectory in the $(\log\rho_c, \log T_c)$ plane moves up and to the right, remaining entirely within the non-degenerate region. These stars evolve directly from H-exhaustion to He ignition without ascending a developed Red Giant Branch.

**Regime 2 — $2.2\, M_\odot < M < 6\, M_\odot$ (temporary isothermal core):**
The He core initially sits well within ideal gas territory. As the shell deposits He and the core mass grows, the SC limit is eventually reached (at $M_c \approx 0.10 M$). At that point, contraction begins on the Kelvin-Helmholtz timescale, the core heats up, and He ignition eventually follows. The isothermal phase is temporary; these stars show a small hook in their evolutionary tracks.

**Regime 3 — $M < 2.2\, M_\odot$ (long-lasting isothermal/degenerate core):**
As the He core grows in density, it crosses the electron degeneracy boundary before reaching the SC limit. Once degenerate, the core is supported by **electron degeneracy pressure** ($P \propto \rho^{5/3}$, independent of temperature). This pressure is insensitive to temperature, so the core can grow far beyond the SC limit **without contracting or heating significantly**. He ignition is therefore severely delayed. These stars develop a well-developed Red Giant Branch (ascending to high luminosity) before He eventually ignites (in a degenerate environment, leading to the helium flash for low-mass stars).

### 13.2 The Electron Degeneracy Condition

Electron degeneracy occurs when all energy states below the Fermi energy are filled. The Fermi energy is:

$$\epsilon_F = \frac{\hbar^2}{2m_e}(3\pi^2 n_e)^{2/3}$$

where the electron number density is:

$$n_e = \frac{Z}{A}\frac{\rho}{m_H}$$

with $Z/A \approx 1/2$ for typical stellar material. For full degeneracy, the thermal energy must be less than the Fermi energy:

$$\frac{3}{2}kT < \epsilon_F = \frac{\hbar^2}{2m_e}\left[3\pi^2\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{2/3}$$

Rearranging:

$$\frac{T}{\rho^{2/3}} < D \approx 10^5\ ^\circ\text{K cm}^2\text{ g}^{-2/3}$$

The constant $D$ is computed from fundamental constants:
- $\hbar = 10^{-27}$ erg s
- $m_e = 10^{-27}$ g
- $k = 1.4\times10^{-16}$ erg K$^{-1}$
- $m_H = 1.7\times10^{-24}$ g
- $Z/A \approx 1/2$

The numerical calculation gives $D \approx 10^5$, making the degeneracy condition simple to evaluate.

In the $\log\rho$-$\log T$ diagram, the degeneracy boundary is the line:

$$\log T = \frac{2}{3}\log\rho + 5 \quad (\text{or more precisely, }\ \log T = \frac{2}{3}\log\rho + 5.11)$$

Regions below and to the right of this line are degenerate.

### 13.3 The $\log\rho$-$\log T$ Phase Diagram and Stellar Locations

The $\log\rho$-$\log T$ diagram divides into several regions according to the dominant equation of state:

- **Upper left**: radiation pressure dominated ($P \propto T^4$); applies to outer layers of very luminous massive stars where radiation dominates
- **Central region**: ideal (perfect) gas ($P \propto \rho T$); applies to most stellar interiors during the MS and early post-MS
- **Lower right**: non-relativistic degenerate electron gas ($P \propto \rho^{5/3}$); applies to He cores of low-mass post-MS stars, white dwarfs
- **Far lower right**: relativistic degenerate electron gas ($P \propto \rho^{4/3}$); applies to very dense white dwarfs near the Chandrasekhar limit

The locations of key stellar phases in this diagram:
- **MS stars**: ideal gas region at moderate $\rho$ and $T$
- **Red Giants**: ideal gas region but at higher $\rho$ and $T$ than the MS; the He core of low-mass red giants is in the degenerate region
- **White Dwarfs**: deep in the degenerate electron gas region

**Core evolutionary trajectories:**
- For high-mass stars ($15\, M_\odot$, $25\, M_\odot$, $35\, M_\odot$): cores evolve diagonally up and to the right in the ($\log\rho_c$, $\log T_c$) plane, remaining safely within the ideal gas region. They represent the "ideal gas passageway" — they never cross into the degenerate region.
- For solar-mass stars: the core trajectory moves to the right (increasing density), eventually crossing the degeneracy boundary and entering the degenerate zone deep in the He-core phase before any He ignition.

The fundamental difference in core trajectories between high-mass and low-mass stars traces back to the very different central densities at the ZAMS ($\rho_c \sim 13$ g cm$^{-3}$ for $7\, M_\odot$ vs $\rho_c \sim 400$ g cm$^{-3}$ for $0.1\, M_\odot$). Low-mass stars have inherently denser cores, placing them much closer to the degeneracy boundary from the beginning.

---

## 14. Key Evolutionary Reference Points and Connections

### 14.1 Complete Summary of Evolutionary Points

| Point | Physical Event | Notes |
|---|---|---|
| **Point 1** | H-ignition in the core — ZAMS | Star is chemically homogeneous; onset of core H-burning |
| **Point 2** | H-exhaustion in the core | End of the MS phase ($X_c < 0.05$); all of the main sequence burning has occurred |
| **Point 3** | H-ignition in the thick shell | For low mass: coincides with Point 2. For high mass: after gravitational contraction (hook). |
| **Point 6** | He-ignition in the core | End of the Red Giant Branch (RGB) ascent; onset of horizontal branch / He clump |

### 14.2 Central Organizing Principle

Every aspect of main-sequence and immediate post-MS evolution follows from a single physical chain: **mass determines the burning mechanism; the burning mechanism determines everything else.**

- Mass above $1.2\, M_\odot$ → CNO cycle dominates
- CNO cycle → concentrated energy production → convective core
- Convective core → flat H-profile → hook at point 2–3 in the HR diagram
- Convective core → lower central density (CNO limits $T_c$ growth, so $\rho_c$ is lower) → avoids degeneracy
- Low central density + higher $T_c$ → core remains in ideal gas as it contracts → direct He ignition without a helium flash

Conversely:
- Mass below $1.2\, M_\odot$ → pp chain dominates
- pp chain → diffuse energy production → radiative core
- Radiative core → smooth H-profile → no hook; seamless transition to shell burning
- Higher central density → core crosses degeneracy boundary → SC limit exceeded without contraction → degenerate He core → long RGB ascent → helium flash

The four effects of CNO burning (structure, core temperature, mass-luminosity, post-MS morphology) are not independent: they all arise from the same root cause — the extreme temperature sensitivity ($T^{15}$) of the CNO cycle. Understanding this single physical fact provides the key to understanding all of main-sequence stellar evolution.
