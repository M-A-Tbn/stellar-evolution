# Pulsating Stars — Exhaustive Study Notes

**Source:** `24.pulsating_stars.pdf` | **Session:** Pulsating Stars | **Date:** 2026-05-20

---

## 1. Introduction to Pulsating Stars

### 1.1 Definition and Physical Mechanism

Pulsating stars are a class of variable stars whose luminosity varies periodically because their radius (and surface temperature) oscillates periodically. The luminosity variation is not due to an external cause (eclipsing binary) but is intrinsic: the star itself is physically pulsating — its layers expand and contract in a regular, repeating cycle. This makes pulsating stars fundamentally different from other types of variable stars.

The luminosity of a star depends on both radius and temperature via the Stefan-Boltzmann relation:

$$L = 4\pi R^2 \sigma T_e^4$$

where $L$ is luminosity (W), $R$ is stellar radius (m), $\sigma$ is the Stefan-Boltzmann constant ($5.67 \times 10^{-8}$ W m$^{-2}$ K$^{-4}$), and $T_e$ is the effective surface temperature (K). Since both $R$ and $T_e$ vary periodically during a pulsation cycle, the luminosity varies accordingly.

Pulsating stars have been classified into several distinct classes depending on their light curve morphology, metallicity, evolutionary stage, and pulsation mode. They occupy a well-defined near-vertical band in the Hertzsprung-Russell Diagram (HRD) called the **Instability Strip**. This strip runs roughly parallel to the luminosity axis, spanning an effective temperature range of approximately $\delta T \approx 600$–$1000$ K, between 6000 and 7100 K. The existence of such a well-defined strip in temperature immediately tells us that pulsation is a phenomenon tied to specific conditions that can only be maintained in a narrow thermal window.

### 1.2 The Prototypical Case: Cepheids and Historical Background

The most famous and extensively studied class of pulsating stars are the **Cepheids**, named after the prototype $\delta$ Cephei, discovered by John Goodricke in the 18th century. The period of $\delta$ Cephei is 5 days 8 hours 48 minutes — a precision that can be measured by the naked eye from the brightness variation of this relatively bright star.

The key observable in all pulsating stars is the **periodic variation of the apparent magnitude** (the light curve). A typical light curve for a classical Cepheid shows a characteristic asymmetric shape: a relatively rapid rise to maximum brightness followed by a slower decline to minimum. The period is measured as the time between successive maxima (or minima).

The turning point in the systematic study of pulsating variable stars came at the beginning of the 20th century with the work of **Henrietta Leavitt** at the Harvard College Observatory. Working with photographic plates of the **Small Magellanic Cloud (SMC)** — an irregular dwarf galaxy satellite of the Milky Way at approximately 60 kpc from the Sun — Leavitt identified and measured the variability periods of more than 2000 Cepheid variables.

The critical advantage of the SMC sample was geometric: all SMC stars are at essentially the same distance from us. This means that observed differences in apparent magnitude directly reflect real differences in absolute magnitude (and hence intrinsic luminosity). With this sample, Leavitt was the first to notice a tight correlation between the luminosity of a Cepheid and its variability period:

> **More luminous Cepheids have longer pulsation periods.**

This fundamental relationship became, once the distance to the SMC was calibrated, the famous **Period-Luminosity (P-L) relation**.

---

## 2. The Period-Luminosity Relation

### 2.1 The P-L Relation and Its Form

The P-L relation, as calibrated from galactic and extragalactic Cepheids, takes the empirical form:

$$M_V = -2.8 \log P_{\rm days} - 1.43$$

where $M_V$ is the absolute visual magnitude (dimensionless, in the magnitude system) and $P_{\rm days}$ is the pulsation period in days. The negative slope means that stars with longer periods ($\log P$ larger) have more negative $M_V$, i.e., they are intrinsically more luminous. This is exactly what Leavitt found: luminous stars have long periods.

The figure showing the P-L relation (Sandage & Tammann 1968) displays absolute magnitude $M_V$ on the y-axis (ranging from about $-2$ to $-7$, brighter at the top) versus $\log P$ on the x-axis (ranging from 0.4 to 2.0). Data points from Galactic cluster Cepheids, the Perseus association, the LMC (distance modulus $(m-M)^0 = 18.45$), the SMC ($(m-M)^0 = 18.85$), M31 ($(m-M)^0 = 24.20$), and NGC 6822 ($(m-M)^0 = 23.75$) all fall on the same tight linear sequence. The tight scatter around a single line from objects at vastly different distances confirms the universality of the P-L relation across different stellar populations and environments.

### 2.2 The P-L Relation as the First Step of the Cosmic Distance Ladder

The P-L relation is of extraordinary practical importance: it represents the **first step of the Cosmic Distance Ladder**. The key insight is that measuring the pulsation period of a Cepheid — which requires only time-series photometry — immediately gives its absolute magnitude via the P-L relation. Comparing this to the observed mean apparent magnitude yields the distance modulus, and hence the distance to the host galaxy. All cosmological distances currently in use are ultimately anchored to the Cepheid P-L relation.

### 2.3 How to Use the P-L Relation: Step-by-Step Procedure

The procedure for distance determination using a Cepheid is as follows:

**Step 1:** From the observed light curve (apparent magnitude $m$ vs. time in days), measure:
- The pulsation period $P$ (time between successive light maxima)
- The time-averaged mean apparent magnitude $\langle V \rangle$ (the intensity-weighted mean over the full cycle)

**Step 2:** Insert the measured period into the P-L relation to obtain the absolute magnitude:
$$M_V = -2.8 \log P_{\rm days} - 1.43$$

**Step 3:** Compute the distance modulus:
$$(m-M)_V = \langle V \rangle - M_V$$

If no interstellar reddening is present, $(m-M)_V = (m-M)_0$, and the distance in parsecs follows from:
$$(m-M)_0 = 5 \log d - 5$$

**Worked example:** For a Cepheid with $P = 4.5$ d and $\langle V \rangle = 13.80$:
- $\log P = 0.65$
- $M_V = -2.8 \times 0.65 - 1.43 = -1.82 - 1.43 = -3.26$
- $(m-M)_V = 13.80 - (-3.26) = 17.06$
- Assuming no reddening: $(m-M)_0 = 17.06$
- $5 \log d = 22.06 \Rightarrow \log d = 4.41 \Rightarrow D \approx 25$ kpc

This elegant three-step procedure transforms a simple brightness measurement into a distance, illustrating why Cepheids are so powerful as standard candles.

---

## 3. The Physical Nature of Pulsations

### 3.1 Radial Pulsations: The Shapley–Eddington Picture

In 1914, Shapley first suggested that the luminosity variability of Cepheids is due to **radial pulsations** of the stellar structure — the star periodically expanding and contracting as a whole. Four years later, Eddington proposed a possible physical mechanism to drive such pulsations. Zhevakin later identified the specific stellar regions responsible. The modern picture is as follows.

**Radial pulsations** involve a periodic variation of both the stellar radius $R$ and the surface temperature $T_e$. These two quantities vary in **anti-phase**: when the radius increases (expansion), the surface temperature decreases; when the radius decreases (compression), the surface temperature increases. This anticorrelation arises from the adiabatic compression and expansion: compression heats the gas, expansion cools it.

Since $L = 4\pi R^2 \sigma T_e^4$, the luminosity depends on both $R^2$ and $T_e^4$. The $T_e^4$ dependence is much stronger than the $R^2$ dependence, so it is primarily the temperature variation that drives the luminosity variation. This is confirmed quantitatively for classical Cepheids: the radius variation is of order 10% ($\Delta R / R \sim 0.1$), while the temperature varies by 1000–1500 K (from spectral type F5 to G2). Since a 1000 K change on a $\sim$6500 K star represents $\Delta T/T \sim 15\%$, and this enters as $T^4$, the luminosity change due to temperature far outweighs the radius contribution.

The logical consequence is:

> **Maximum luminosity occurs when temperature is maximum, which coincides with minimum radius.**

### 3.2 Observed Pulsation Properties of $\delta$ Cephei and the Phase Lag

The observed pulsation properties of $\delta$ Cephei (Figure 14.5 from the textbook) show four panels plotted versus time (0–8 days):

1. **V-band apparent magnitude** (top panel): ranges from $V \approx 3.5$ (maximum, bright) to $V \approx 4.5$ (minimum, faint). The light curve shows a rapid rise and slower decline.
2. **Surface temperature** $T$ (K) (second panel): varies from $\approx$ 5800 K to $\approx$ 6700 K, in phase with the light curve.
3. **Relative radius** $R/R_{\rm min}$ (third panel): varies from 1.0 (minimum radius) to $\approx$ 1.12 (maximum radius), anti-phase with temperature.
4. **Radial velocity** $v_r$ (km s$^{-1}$) (bottom panel): varies from $\approx 0$ to $\approx -25$ km/s (negative = approaching = expanding surface).

The data confirm that:
- Maximum luminosity (minimum $V$) corresponds to maximum temperature.
- However, **maximum luminosity does NOT coincide exactly with minimum radius**. The luminosity maximum occurs slightly after the minimum radius is reached — the star is already beginning to expand when it reaches peak brightness.

This time offset between the minimum-radius phase and the maximum-luminosity phase is called the **Phase Lag**. It is a real, observable effect that requires a physical explanation from the mechanism driving the oscillations. Understanding the phase lag is one of the key diagnostics of stellar pulsation theory.

---

## 4. The Instability Strip and the Transient Nature of Pulsation

### 4.1 The Instability Strip in the HRD

Pulsating stars do not occupy random locations in the HRD. They are confined to a near-vertical band — the **Instability Strip** — bounded in temperature between approximately 6300 and 7100 K (i.e., $\log T_e \approx 3.80$–$3.85$). This strip runs parallel to the luminosity axis across a wide range of luminosities, from $\log(L/L_\odot) \approx 0.5$ ($\delta$ Scuti) up to $\log(L/L_\odot) \approx 5$ (bright Classical Cepheids) and even higher for some variables.

The HRD figure shows evolutionary tracks for stars of different masses (from $0.25 M_\odot$ to $15 M_\odot$) overlaid with the instability strip (shaded red region). Different classes of pulsating variables occupy different luminosity segments of the strip:
- **$\delta$ Scuti stars** ($\log L/L_\odot \sim 0.5$–$1.5$): Low-luminosity, main-sequence or near-main-sequence pulsators.
- **RR Lyrae stars** ($\log L/L_\odot \sim 1.5$–$2.0$): Horizontal Branch pulsators.
- **W Virginis stars** ($\log L/L_\odot \sim 3.0$–$4.0$): Population II analogs of Classical Cepheids.
- **Classical Cepheids** ($\log L/L_\odot \sim 3.5$–$4.5$): Population I, intermediate-mass He-burning supergiants.

The strip has a finite width in temperature ($\delta T \sim 600$–$1000$ K). Stars within this temperature range pulsate; stars outside it do not. The temperature range $6300$–$7100$ K corresponds approximately to spectral types F5–G2 at the luminosities of classical Cepheids.

Since our Galaxy hosts several million pulsating stars but the total stellar population is a few hundred billion, pulsation affects only a tiny fraction of stars. This immediately implies that pulsation is a **transient phenomenon** — stars are pulsating only during the brief evolutionary phase when their track passes through the Instability Strip.

### 4.2 Classification of Pulsating Variable Stars

Pulsating stars have been classified by light curve shape, metallicity, and other properties. The main classes and their properties (Table 14.1) are:

| Type | Period Range | Population | Mode |
|---|---|---|---|
| Long-Period Variables (LPVs) | 100–700 days | I, II | Radial |
| Classical Cepheids | 1–50 days | I | Radial |
| W Virginis stars | 2–45 days | II | Radial |
| RR Lyrae stars | a few hours to 1 day | II | Radial |
| $\delta$ Scuti stars | 1–3 hours | I | R, NR |
| $\beta$ Cephei stars | 3–7 hours | I | R, NR |
| ZZ Ceti stars | 100–1000 seconds | I | Non-Radial |

Key distinctions:
- **Classical Cepheids** are Population I (metal-rich, young, disk stars), periods 1–50 days.
- **W Virginis stars** are Cepheid-like but Population II (metal-poor).
- **RR Lyrae stars** are Population II, with periods of a few hours to about one day.
- **$\delta$ Scuti stars** are Main Sequence pulsators.
- **ZZ Ceti stars** are White Dwarf pulsators with non-radial pulsations.
- **LPVs** (Mira variables and related) are AGB stars and red supergiants outside the main Instability Strip.
- **$\beta$ Cephei stars** are blue supergiants near the end of the MS phase; their pulsation mechanism is more complex.

---

## 5. The Evolutionary Stage of Pulsating Stars

### 5.1 Which Stars Pulsate and When

Since pulsation occurs only when a star crosses the Instability Strip, we need to identify which evolutionary phases correspond to the strip crossing. Stellar evolutionary tracks for stars of different masses can cross the Instability Strip multiple times:

**First crossing:** This occurs soon after hydrogen exhaustion in the core, during the rapid first expansion of the envelope from the ZAMS toward the red giant branch. This crossing is very fast (evolutionary timescale is short), so comparatively few stars are observed during this phase.

**Second crossing (He-burning, slow):** As the star ignites core He-burning and settles onto the horizontal branch (or He-clump for intermediate-mass stars), it crosses the Instability Strip from the red side toward the blue side. This is a significantly **slower** crossing because the star spends a substantial fraction of its He-burning lifetime within the strip. This is the evolutionary phase where the majority of Cepheids and RR Lyrae are found.

**Third crossing:** After the ZAHB (Zero-Age Horizontal Branch) phase, stars evolve toward the AGB. This crossing is rapid again and contributes fewer pulsators.

The key conclusion is that **the He-burning phase (horizontal branch / He-clump phase) is the dominant evolutionary stage during which we observe stellar pulsations.** The amount of time a star spends inside the Instability Strip during its He-burning phase determines the likelihood of observing it as a variable. Stars whose He-burning track lies entirely inside the strip, or whose track crosses the strip slowly, produce the bulk of the observed pulsating star population.

The figure showing this (figure with "striscia d'instabilità") displays multiple evolutionary loop tracks in the region $3.6 < \log T_e < 4.0$ at several luminosity levels. The vertical instability strip lines are shown. Tracks at different luminosities show different amounts of time spent within the strip — this directly maps to different pulsation period ranges because $\Pi \propto \rho^{-1/2}$ (see Section 7).

### 5.2 RR Lyrae Stars: Population II Horizontal Branch Pulsators

RR Lyrae stars are the Population II analog of classical Cepheids. They are **Horizontal Branch (HB) stars** undergoing core helium burning. The Zero-Age Horizontal Branch (ZAHB) is crossed by the Instability Strip, and all HB stars with surface temperatures between approximately 6000 and 8000 K are variable.

Because all RR Lyrae stars are at the same evolutionary phase (core He-burning), they have approximately the same luminosity ($M_V \approx +0.5$, $\log L/L_\odot \approx 1.5$–$1.7$). This nearly constant luminosity makes them **standard candles** for measuring distances to star clusters and the halo. The distance to a cluster hosting RR Lyrae can be determined simply by comparing their known absolute magnitude to the observed apparent magnitude.

**Observational evidence:** The color-magnitude diagram of the old globular cluster M3 (containing 8161 stars) shows a clear gap in the distribution of stars along the Horizontal Branch. This gap corresponds to the Instability Strip: the RR Lyrae variables, being pulsating, are not plotted in this static CMD, leaving a visible "void" in the HB at $V \approx 15.5$, $(B-V) \approx 0.2$–$0.5$.

### 5.3 Dependence of RR Lyrae on HB Morphology and Metallicity

Whether a globular cluster harbors RR Lyrae depends on the **HB morphology** — the distribution of HB stars in temperature. This in turn depends on multiple parameters:

**Metallicity effect:** Metal-rich HB stars have larger masses (since high-metallicity stars on the ZAMS are more massive for a given age), so they reach the HB with larger total masses and populate the **red side** of the instability strip (or even redder). High-metallicity clusters may therefore have no HB stars inside the strip and no RR Lyrae.

**Helium abundance effect:** He-rich stars reach the HB with smaller masses (because higher He content means smaller ZAMS mass at the same age) and populate the **blue side** of the instability strip or bluer. Very He-rich clusters may have all their HB stars blueward of the strip and again no RR Lyrae.

**Intermediate metallicity:** Clusters with intermediate metallicity have HB stars distributed across the instability strip and therefore host RR Lyrae populations.

The schematic diagrams showing HB morphology under three metallicity conditions illustrate this clearly:
- High metallicity: HB is entirely red of the strip — no RR Lyrae.
- Intermediate metallicity: HB crosses the strip — RR Lyrae present.
- Low metallicity: HB is entirely blue of the strip — no RR Lyrae.

The population of RR Lyrae in a cluster is thus controlled by all parameters that affect HB morphology: metallicity, helium content, age, mass loss history on the RGB, and possibly others (the "second parameter" problem). For a 0.8 $M_\odot$ star at 13 Gyr (shown in the HRD figure), the track intersects the ZAHB at $\log L/L_\odot \approx 1.5$–$1.7$ and crosses the instability strip region near $\log T_{\rm eff} \approx 3.8$.

The left-panel figure showing the ZAHB shows how the position along the ZAHB depends on star mass, with points from 0.5 $M_\odot$ (blue/hot side) to 0.65 $M_\odot$ (red/cool side). The right-panel CMDs compare different metallicities (Z = 0.0001 and Z = 0.02) and helium abundances (Y = 0.24 and Y = 0.40) at 13 Gyr. In the high-metallicity case ($Z = 0.02$, $M = 0.85 M_\odot$ from ZAMS), stars arrive on the HB with more mass and sit on the red side. In the high-He case ($Y = 0.40$, $M = 0.69 M_\odot$), smaller HB masses push stars to the blue.

---

## 6. Pulsation Modes: Analogy with Standing Sound Waves

### 6.1 The Standing Wave Model

The propagation of pulsations within a star is treated mathematically as the propagation of **standing sound (acoustic) waves** — analogous to standing waves in a closed organ pipe. The key physics is that:
- The stellar center acts like the closed end of the pipe (a displacement node — zero displacement of gas).
- The stellar surface acts like the open end (an antinode where gas motion is maximum).

Figure 14.7 shows three cases:

**(a) Fundamental Mode:** No nodes between center and surface. The gas moves uniformly in the same direction at every point of the star at any given instant. In the pipe analogy, the wavelength is $2L$ (pipe of length $L$), and in the star the nodal line is the center with motion extending to the surface at $R$.

**(b) First Overtone:** One node lies between center and surface (at $\approx 0.6 R$ from center, i.e., $0.4 R$ from surface). Gas on either side of the node moves in opposite directions simultaneously. In the pipe, the node is at $0.67 L$.

**(c) Second Overtone:** Two nodes between center and surface (at $\approx 0.5 R$ and $\approx 0.8 R$). In the pipe, nodes are at $0.4 L$ and $0.8 L$.

Higher overtones have shorter wavelengths and therefore shorter periods for the same physical size, just as higher harmonics in a pipe have shorter wavelengths.

**Observationally:**
- The vast majority of **Classical Cepheids and W Virginis stars** pulsate in the **fundamental mode**.
- **RR Lyrae stars** pulsate in either the **fundamental mode** or the **first overtone** (and sometimes both simultaneously, the so-called "beat" or "double-mode" pulsators).

---

## 7. Derivation of the Period-Density Relation

### 7.1 Acoustic Wave Crossing Time

Since pulsations propagate as acoustic (sound) waves, the pulsation period can be estimated as the time needed for an acoustic wave to cross the diameter of the star:

$$\Pi = 2\int_0^R \frac{dr}{v_s}$$

where $v_s$ is the local sound speed and the factor of 2 accounts for the round trip (center to surface and back). This integral over the stellar radius correctly captures how the varying density profile affects the wave propagation time.

### 7.2 The Sound Speed in an Ideal Gas

The sound speed in a compressible medium depends on the medium's **resistance to compression** (bulk modulus $B$) and its **density** $\rho$:

$$v_s = \sqrt{\frac{B}{\rho}}$$

where the bulk modulus is defined as $B = -V(\partial P/\partial V)_{ad}$, which describes how pressure changes with volume under adiabatic conditions. Substituting:

$$v_s = \sqrt{-\frac{V}{\rho}\left(\frac{\partial P}{\partial V}\right)_{ad}}$$

### 7.3 Derivation of $-V dP/dV = \gamma P$ for an Adiabatic Process

For an adiabatic process, the first law of thermodynamics gives $dU + P\,dV = 0$ (since $dQ = 0$). For a monatomic ideal gas with $N$ particles, $U = \frac{3}{2}NRT_m$ (where $R$ is the gas constant and $T_m$ the temperature). Differentiating:

$$\frac{3}{2}RN\,dT + P\,dV = 0 \implies P\,\frac{dV}{dT} = -\frac{3}{2}RN$$

From the ideal gas law $PV = NRT_m$, differentiating at constant $V$ and constant $P$ respectively and combining:

$$\frac{5}{2}RN - V\frac{dP}{dT} = 0 \implies dT = \frac{V\,dP}{c_P}$$

Working through the algebra, one obtains for the adiabatic case:

$$\gamma P = -V\frac{dP}{dV}$$

where $\gamma = c_P/c_V$ is the ratio of specific heats ($\gamma = 5/3$ for a monatomic ideal gas). Therefore:

$$v_s = \sqrt{\frac{\gamma P}{\rho}}$$

This is the standard adiabatic sound speed formula: it depends on pressure and density. Higher pressure increases the sound speed (stiffer medium); higher density decreases it (more inertia).

### 7.4 Pressure Profile from Hydrostatic Equilibrium

To evaluate the sound speed at each layer inside the star, we need the pressure profile $P(r)$. From the hydrostatic equilibrium equation:

$$\frac{dP}{dr} = -\frac{GM_r \rho(r)}{r^2}$$

Assuming a uniform average density $\rho$ and using $M_r = \frac{4}{3}\pi \rho r^3$:

$$\frac{dP}{dr} = -\frac{4}{3}\pi G \rho^2 r$$

Integrating from radius $r$ to the surface $R$ (where $P(R) = 0$):

$$P(R) - P(r) = -\frac{4}{3}\pi G\rho^2 \frac{R^2 - r^2}{2}$$

$$P(r) = \frac{2}{3}\pi G\rho^2 (R^2 - r^2)$$

This is the pressure at radius $r$ for a uniform-density star. At the centre ($r=0$): $P(0) = \frac{2}{3}\pi G\rho^2 R^2$, decreasing parabolically to zero at the surface.

### 7.5 Evaluating the Period Integral

Substituting the sound speed $v_s = \sqrt{\frac{2}{3}\gamma\pi G\rho(R^2 - r^2)}$ into the period integral:

$$\Pi \approx 2\int_0^R \frac{dr}{\sqrt{\frac{2}{3}\pi\gamma G\rho(R^2 - r^2)}}$$

$$= 2\sqrt{\frac{3}{2\pi\gamma G\rho}} \int_0^R \frac{dr}{\sqrt{R^2 - r^2}}$$

Substituting $x = r/R$, the integral $\int_0^1 dx/\sqrt{1-x^2} = [\arcsin x]_0^1 = \pi/2$. The factors of $R$ cancel. Therefore:

$$\boxed{\Pi \approx \sqrt{\frac{3\pi}{2\gamma G\rho}}}$$

### 7.6 Physical Meaning: The Period-Density Relation

This central result states that the pulsation period is **inversely proportional to the square root of the mean stellar density**:

$$\Pi \propto \rho^{-1/2}$$

Physical interpretation: A denser star has a higher sound speed (pressure increases with density), so acoustic waves cross the star faster, giving a shorter period. A low-density (giant/supergiant) star has a much lower sound speed, requiring longer for the wave to propagate, giving a longer period. This naturally explains why luminous, extended (low-density) stars have longer pulsation periods — they are giants or supergiants — and why the P-L relation exists: **the Period-Luminosity relation observed by Leavitt is fundamentally a manifestation of a Period-Density relation.** In the HRD, luminosity and mean density are strongly correlated because the most luminous stars are giants with very low average density.

For a monoatomic ideal gas ($\gamma = 5/3$), the period formula gives:

$$P = \frac{2\pi}{\omega}, \quad \omega^2 = (3\gamma - 4)\frac{GM}{R_0^3}$$

which is consistent with the one-zone model result derived in Section 10.

---

## 8. The Mechanism Driving Pulsations: The Eddington Valve and the $\kappa$-Mechanism

### 8.1 The Thermodynamic Engine Analogy

For pulsations to be sustained over many cycles rather than dying away (damping), there must be a physical mechanism that continuously replenishes the kinetic energy of oscillation. Eddington proposed that this mechanism operates like a **thermodynamic (Carnot) engine**: a layer inside the star converts **thermal energy (heat) into mechanical energy (work)** by absorbing heat at high temperature and releasing it at low temperature. This is precisely the Carnot driving cycle.

The Carnot cycle in a P-V diagram is a reversible closed loop. If the path is followed **clockwise** in a P-V diagram (pressure on y-axis, volume on x-axis), the cycle does net positive work on the surrounding layers (driving cycle). If it is followed **counterclockwise**, the work is negative (damping cycle). The area enclosed by the loop equals the net work done per cycle.

The majority of gas layers inside a star are **dissipative (damping)**. This is why we need a special layer — a **thermal valve** — to overcome the dissipation and maintain the oscillation.

### 8.2 Formal Derivation of the Driving Condition

Consider a gas layer A inside the star. Over one complete oscillation cycle, the internal energy $U$ and entropy $S$ must return to their initial values (reversible cycle):

$$\oint dU = 0, \quad \oint dS = 0$$

From the first law: $dU = dQ - dW$. Since $\oint dU = 0$:

$$\bar{W} \equiv \oint \frac{dQ}{dt}\,dt$$

The work performed by layer A on surrounding layers over one cycle equals the net heat absorbed. For the entropy condition, using $dQ = T\,dS$:

$$\oint \frac{1}{T}\frac{dQ}{dt}\,dt = 0$$

Writing $T(t) = T_0 + \delta T(t)$ where $T_0$ is the equilibrium temperature and $\delta T \ll T_0$, the linearized condition gives:

$$\bar{W} = \frac{1}{T_0}\oint \frac{dQ}{dt}\,\delta T\,dt$$

This is the key result: the work performed by the layer on its surroundings depends on the **correlation between the heat injection rate** $dQ/dt$ and the **temperature perturbation** $\delta T$. The driving condition $\bar{W} > 0$ requires:

- Either $dQ/dt > 0$ (heat injection) **when** $\delta T > 0$ (layer hotter than equilibrium, i.e., during compression), **or**
- $dQ/dt < 0$ (heat release) **when** $\delta T < 0$ (layer cooler than equilibrium, i.e., during expansion).

Stated in physical terms:

> **A gas layer acts as a driving (active) layer ONLY IF it absorbs heat when hot (during compression) and releases heat when cold (during expansion).**

This is the opposite of what normally happens: ordinary gas layers, when compressed, heat up and lose energy by radiation (damping behavior). We need a special "valve" mechanism.

### 8.3 The Role of Opacity: Normally Damping Behavior

Eddington realized that the thermal valve must operate through the **opacity** $\kappa$. Under normal fully-ionized stellar interior conditions, opacity follows **Kramers' law**:

$$\kappa \propto \frac{\rho}{T^{3.5}}$$

When a layer is compressed (temperature increases), the opacity **decreases** (because $T$ increases in the denominator). Lower opacity means the layer is more transparent to radiation — it lets photons escape more easily. So during compression (when hot), energy leaks out rather than being trapped. This is the **opposite** of what is needed for driving. Normal stellar layers are therefore dissipative: they absorb heat during expansion (when they cool down and opacity increases) and release heat during compression (when they are hot and transparent). This damps the oscillations.

### 8.4 The $\kappa$-Mechanism in Partially Ionized Layers (Zhevakin's Discovery)

Zhevakin (confirmed by Kippenhahn, Baker, and Cox) identified the special conditions under which the thermal valve actually works: **partially ionized regions**. In such regions, the opacity behaves in the opposite sense from Kramers' law, enabling the driving cycle. This is the **$\kappa$-mechanism** (kappa-mechanism):

**During compression (hot phase):** The increased temperature favors the **ionization process** rather than raising the kinetic temperature. The energy absorbed by ionization is temporarily "locked" in the ionization energy — the layer acts as a heat reservoir. The opacity $\delta\kappa > 0$ because the increased ionization fraction raises the opacity (partially ionized: more electrons available for bound-free transitions). The layer is **opaque when compressed** — it traps energy.

**During expansion (cool phase):** As the layer expands and cools, the ions and electrons **recombine**, releasing the stored ionization energy. The opacity decreases. The layer is **transparent when expanded** — it releases energy.

This is exactly the behavior of a thermal valve: absorb heat when hot (compression → ionization), release heat when cold (expansion → recombination). The layer behaves as a "piston" that periodically stores and releases energy in phase with the oscillation.

There is also a secondary reinforcing effect called the **$\gamma$-mechanism**: in partially ionized regions, the absorbed heat goes partly into ionization rather than temperature increase, so $\delta T$ is suppressed below what it would be in a fully ionized layer. This suppressed temperature rise means that photons from deeper layers tend to flow into the cooler-than-expected partially ionized zone, providing additional heat injection. This enhances the driving beyond what the opacity effect alone would provide.

### 8.5 The Two Ionization Zones

There are **two major partially ionized regions** inside a star, each driving pulsations:

**H ionization zone** (temperature $\approx 1.5 \times 10^4$ K):
- $\rm H\,I \rightarrow H\,II$ (hydrogen ionization)
- $\rm He\,I \rightarrow He\,II$ (first helium ionization — occurs at nearly the same temperature)
- These two processes overlap in the same zone.

**He ionization zone** (temperature $\approx 4 \times 10^4$ K):
- $\rm He\,II \rightarrow He\,III$ (second helium ionization)
- This zone is significantly deeper inside the star.

**Observational confirmation (Figure 14.11):** A plot of $\delta\kappa$ (cm$^2$ g$^{-1}$) and $\delta T$ ($10^3$ K) versus temperature ($10^4$ K) throughout an RR Lyrae model at maximum compression shows:
- At the He II partial ionization zone ($T \approx 40{,}000$ K): $\delta\kappa > 0$ (opacity increases during compression) and $\delta T$ is reduced (temperature rise suppressed). These are exactly the $\kappa$- and $\gamma$-mechanisms.
- At the H ionization zone ($T \approx 15{,}000$ K): $\delta T$ is large (the temperature perturbation propagates freely) but $\delta\kappa$ changes sign.

**Figure 11.2 (work per zone):** A histogram showing the ratio of mechanical work done per cycle to kinetic energy of pulsations for each zone in an RR Lyrae model clearly shows:
- Zones 1–25 (deep dissipation zone): large negative values — these layers strongly damp the oscillation.
- He II zone (around zone 27): large positive values — strong driving.
- Hydrogen zone (around zone 31–35): moderate positive values — additional driving.
- Atmospheric layers: small negative values — weak atmospheric dissipation.

The net result is that the He II ionization zone provides the dominant driving, overcoming the dissipation from the deep interior and other layers, allowing sustained pulsation.

### 8.6 The Real Piston: He Ionization, the Phase Lag: H Ionization

From the theoretical models and from experiments in which layers are artificially removed:

**The He-ionization region is the real piston of stellar pulsation.** If the He II ionization zone is removed from the numerical model, no pulsation is observed. The $\kappa$-mechanism in this zone provides the driving work.

**The H-ionization region introduces the Phase Lag.** The maximum in luminosity (Lr) reaching the base of the H-ionization region is perfectly synchronized with the minimum radius. However, the radiation must penetrate through the H-ionization zone, where part of the energy is used in H-ionization. This energy is released only when the layer expands, cools, and the electrons recombine. This delay propagates outward to the surface, arriving when the star is already expanding — producing the observed time offset between minimum radius and maximum surface luminosity. Without the H-ionization layer, the maximum in luminosity and the minimum radius would be exactly in phase, as the simulation confirms.

---

## 9. Why the Instability Strip Has Boundaries

### 9.1 The Blue Edge

For stars that are **too hot** (left of the blue edge of the instability strip), the partial ionization zones (H and He II) are located very close to the stellar surface. When the ionization zones are too shallow (too little mass above them), there is insufficient overlying envelope mass to produce an appreciable pulsation amplitude. The oscillation driven by these thin ionization layers is insufficient to overcome the damping from the rest of the star. This naturally explains the **blue edge** of the Instability Strip.

The HRD figure confirms this: the blue edge corresponds to $\log T_{\rm eff} \approx 3.85$ ($T_{\rm eff} \approx 7100$ K). Stars blueward of this line cannot pulsate.

### 9.2 The Red Edge

For stars that are **too cool** (right of the red edge), the ionization zones are well positioned inside the star (sufficient overlying mass), but the cooler surface temperature triggers the onset of **convection** in the outer envelope. Surface convection becomes efficient and damps the pulsations: the turbulent convective motions destroy the coherent acoustic wave patterns needed for resonant oscillations. The convective energy transport "short-circuits" the thermal valve mechanism, preventing the Carnot-like driving cycle from operating effectively.

The two boundaries of the Instability Strip are therefore set by physically distinct mechanisms:
- **Blue edge**: ionization zones too close to surface — insufficient driving mass.
- **Red edge**: convection in the envelope damps the pulsation.

---

## 10. The One-Zone Model: Formal Derivation of Period-Density

### 10.1 Model Setup

To understand the period-density relation at a more rigorous level, a simplified **one-zone model** is introduced. In this toy model:
- All the mass $M$ of the star is concentrated at the center.
- The interior is filled with a massless gas exerting pressure $P$.
- We describe the motion of a thin shell of mass $m$ at radius $R$ from the center.

The setup (Figure 14.13) shows the central mass $M$, the shell of mass $m$ at the surface, the interior pressure $P$, and vacuum outside.

### 10.2 Equation of Motion

The equation of motion for the shell is:

$$m\frac{d^2R}{dt^2} = -G\frac{Mm}{R^2} + 4\pi R^2 P$$

The two forces are gravity (inward) and pressure (outward through the spherical surface area $4\pi R^2$). At equilibrium radius $R_0$:

$$G\frac{Mm}{R_0^2} = 4\pi R_0^2 P_0$$

### 10.3 Linearization around Equilibrium

Writing $R = R_0 + \delta R$ and $P = P_0 + \delta P$ with $|\delta R| \ll R_0$ and $|\delta P| \ll P_0$, and expanding to first order in small quantities:

$$\frac{1}{(R_0 + \delta R)^2} \approx \frac{1}{R_0^2}\left(1 - \frac{2\delta R}{R_0}\right)$$

After expanding, using the equilibrium condition $G\frac{Mm}{R_0^2} = 4\pi R_0^2 P_0$, and canceling all zeroth-order terms, the linearized equation of motion becomes:

$$m\frac{d^2}{dt^2}(\delta R) = 2G\frac{Mm}{R_0^3}\delta R + 8\pi R_0 P_0 \delta R + 4\pi R_0^2 \delta P \quad \text{(A)}$$

### 10.4 Adiabatic Pressure-Radius Relation

For adiabatic pulsations, $PV^\gamma = \text{const}$ with $V = \frac{4}{3}\pi R^3$, so $PR^{3\gamma} = \text{const}$. Differentiating logarithmically:

$$\frac{\delta P}{P_0} = -3\gamma \frac{\delta R}{R_0} \implies \delta P = -3\gamma \frac{P_0}{R_0}\delta R$$

### 10.5 Substitution and Final Result

Substituting $\delta P$ into equation (A) and using $G\frac{Mm}{R_0^3} = 4\pi R_0 P_0$:

$$m\frac{d^2}{dt^2}(\delta R) = 4\frac{GMm}{R_0^3}\delta R - 3\gamma\frac{GMm}{R_0^3}\delta R = -(3\gamma - 4)\frac{GMm}{R_0^3}\delta R$$

Dividing by $m$:

$$\boxed{\frac{d^2}{dt^2}(\delta R) = -(3\gamma - 4)\frac{GM}{R_0^3}\,\delta R}$$

### 10.6 Physical Interpretation of the One-Zone Result

This is the equation of **simple harmonic motion**: $\ddot{x} = -\omega^2 x$, with:

$$\omega^2 = (3\gamma - 4)\frac{GM}{R_0^3}$$

The solution is $\delta R = A\sin(\omega t)$ (oscillation) **only if $\omega^2 > 0$**, which requires:

$$\gamma > \frac{4}{3}$$

This is the condition for **dynamical stability** of the star: if $\gamma < 4/3$ (e.g., if radiation pressure dominates, pushing $\gamma$ toward $4/3$, or if partial ionization reduces the effective adiabatic index below $4/3$), the star is dynamically unstable and would collapse or explode rather than oscillate.

For a monatomic ideal gas ($\gamma = 5/3$), $3\gamma - 4 = 1$, giving real oscillations. The angular frequency is:

$$\omega = \sqrt{(3\gamma-4)\frac{GM}{R_0^3}}$$

and the pulsation period is:

$$P = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{\frac{4}{3}\pi G\rho_0 (3\gamma-4)}}$$

Since $M = \frac{4}{3}\pi R_0^3 \rho_0$, we have $\frac{GM}{R_0^3} = \frac{4}{3}\pi G\rho_0$:

$$\boxed{P = \frac{2\pi}{\sqrt{\frac{4\pi}{3}G\rho_0}}}$$

This confirms the Period-Density relation: **period depends only on the mean stellar density**, not on the mass or radius independently. This is the one-zone model analog of $\Pi \propto (G\rho)^{-1/2}$ derived from the acoustic wave argument.

---

## 11. From Period-Density to Period-Luminosity: The Full Derivation

### 11.1 Connecting Period to Observable Quantities

Starting from the period-density relation:

$$\log P = -\frac{1}{2}\log\rho + \text{const}$$

Since $\rho \propto M/R^3$:

$$\log P = -\frac{1}{2}\log M - \frac{1}{2}\log R^{-3} + c = -\frac{1}{2}\log M + \frac{3}{2}\log R + c$$

Using the Stefan-Boltzmann law $L = 4\pi\sigma R^2 T^4$, solving for $R$:

$$R = \left(\frac{L}{4\pi\sigma T^4}\right)^{1/2}$$

Substituting into the period expression:

$$\log P = -\frac{1}{2}\log M + \frac{3}{2}\log\left(\frac{L}{4\pi\sigma T^4}\right)^{1/2} + c$$

$$= -\frac{1}{2}\log M + \frac{3}{4}\log L - 3\log T_{\rm eff} + c$$

In boxed form:

$$\boxed{\log P = -\frac{1}{2}\log M + \frac{3}{4}\log L - 3\log T_{\rm eff} + c}$$

In solar units:

$$\log P = -\frac{1}{2}\log\!\left(\frac{M}{M_\odot}\right) - 3\log\!\left(\frac{T}{T_\odot}\right) - 0.3(M_{\rm bol} - M_{\rm bol}^\odot) - 1.294$$

### 11.2 Eliminating Mass Using the Mass-Luminosity Relation

To make this an observable relationship, we eliminate mass using the known mass-luminosity relation along the ZAMS:

$$M_{\rm bol}^{\rm MS} = 3.96 - 8.22\log\!\left(\frac{M}{M_\odot}\right) \quad \text{for } -8 < M_{\rm bol} < 1$$

For a star crossing the instability strip during the He-burning phase, it is approximately 1 magnitude brighter than its ZAMS luminosity. Hence:

$$M_{\rm bol}^{\rm He-C} \approx 2.96 - 8.22\log\!\left(\frac{M}{M_\odot}\right) \approx 3 - 8.22\log\!\left(\frac{M}{M_\odot}\right)$$

Solving for $-\frac{1}{2}\log(M/M_\odot)$:

$$-\frac{1}{2}\log\!\left(\frac{M}{M_\odot}\right) = 0.06(M_{\rm bol} - 3)$$

Substituting back:

$$\log P = 0.06(M_{\rm bol} - 3) - 3\log\!\left(\frac{T}{T_\odot}\right) - 0.3(M_{\rm bol} - M_{\rm bol}^\odot) - 1.294$$

Collecting terms (using $M_{\rm bol}^\odot = 4.75$):

$$\log P = -3\log\!\left(\frac{T}{T_\odot}\right) - 0.24 M_{\rm bol} - 0.049$$

### 11.3 Transforming to Observational Quantities (Colors)

Bolometric magnitudes are not directly observable; broadband photometry (V, B filters) is. Transformations are needed:
- $M_{\rm bol} - M_V = BC_V$ (bolometric correction in V band)
- $M_{\rm bol} - M_B = BC_B$ (bolometric correction in B band)
- Both $BC_\lambda$ depend on color index $(B-V)$: $BC_\lambda = f(B-V)$

For the range $0.4 < (B-V) < 1$, an approximate bolometric correction is:
$$M_{\rm bol} = M_V + 0.145 - 0.322(B-V)$$

There is also a standard calibration relating effective temperature to color:
$$\log T_e = 3.886 - 0.175(B-V)$$

Substituting these transformations into the period-color-magnitude relation yields:

$$\boxed{\log P = -0.239 M_V + 0.602(B-V) - 0.456}$$

This clearly shows that the pulsation period depends on **both** the stellar magnitude $M_V$ **and** the color $(B-V)$. The period is not a function of luminosity alone — the Period-Luminosity relation is more precisely a **Period-Luminosity-Color (PLC) relation**.

Inverting to express $M_V$ in terms of observables:

$$\boxed{M_V = -3.53\log P_{\rm days} - 2.13 + 2.13(B-V)}$$

The simple PL relation ($M_V = -2.8\log P - 1.43$) is the PLC relation evaluated at the mean color of classical Cepheids. This explains why the scatter in the PL diagram increases when stars of different colors (metallicities) are mixed: the intrinsic scatter in the pure PL relation is largely color scatter.

---

## 12. Answers to the Four Key Questions

### 12.1 Question 1: What is the Origin of the Pulsation?

The origin of stellar pulsation is the **$\kappa$-mechanism** (also strengthened by the $\gamma$-mechanism): a thermodynamic valve supported by the opacity behavior in partially ionized regions. Specifically, the **He II partial ionization zone** at $T \approx 40{,}000$ K is the primary **piston** driving the pulsation. In this zone, compression causes increased ionization (absorbing energy in the ionization process and raising opacity), while expansion causes recombination (releasing stored energy). This cyclical energy storage and release drives work into the oscillation, overcoming the damping from the rest of the star.

### 12.2 Question 2: Why Do Pulsations Occur Only in the Instability Strip?

The instability strip is bounded by two physically distinct effects:
- **Blue edge** ($T_{\rm eff} \approx 7100$ K): For hotter stars, the He II ionization zone is too close to the surface. There is insufficient envelope mass above it to produce an appreciable pulsation. The "engine" has no "load."
- **Red edge** ($T_{\rm eff} \approx 6300$ K): For cooler stars, the ionization zones are appropriately positioned deeper inside the star, but the onset of convection in the outer envelope dissipates the pulsation energy. Turbulent convection damps the coherent wave pattern.

Only within the narrow temperature window between these two limits does the $\kappa$-mechanism successfully drive sustained oscillations.

### 12.3 Question 3: Why Does the Period Change with Luminosity?

The period-luminosity relation is a direct consequence of the **period-density relation** $\Pi \propto \rho^{-1/2}$. In the HRD, there is a strong correlation between luminosity and average stellar density: the most luminous stars are giant/supergiant stars with very low average density. Low density implies long acoustic crossing time, hence longer pulsation periods. Transforming the period-density relation into observable quantities (luminosity and color) naturally produces the PLC relation and, by fixing color, the PL relation. The slope and zero-point of the PL relation thus have a purely physical basis.

### 12.4 Question 4: Why Does Maximum Luminosity Not Correspond to Minimum Radius?

This phase lag arises from the action of the **H ionization layer**. The internal luminosity maximum occurs perfectly in phase with minimum radius at the base of the H-ionization zone. However, as this luminosity wave propagates through the H-ionization zone, part of the energy is used for hydrogen ionization. This energy is only returned (as radiation) when the zone cools and electrons recombine — during the expansion phase. The resulting delay in the emerging luminosity means that when the wave finally reaches the surface, the star is already expanding. Maximum observed surface luminosity thus occurs when the star is expanding, shortly after minimum radius — this is the observed phase lag.

---

## 13. Summary: The Big Picture of Pulsating Stars

### 13.1 Overview and Key Connections

Pulsating stars form a coherent physical system understood at every level: observation, mechanism, and theory.

**Observationally:** Light curves provide period and mean magnitude. The P-L relation (or more precisely PLC relation) immediately gives luminosity and hence distance. Radial velocity curves from spectroscopy confirm the radial motions, verify the oscillation amplitude, and show the phase lag between radius minimum and luminosity maximum.

**Mechanistically:** Pulsations are driven by the $\kappa$-mechanism in the He II partial ionization zone. The piston (He zone) and the phase-lag producer (H zone) are distinct regions. The instability strip boundaries arise from the interplay of ionization zone depth (blue edge) and convective damping (red edge).

**Theoretically:** The Period-Density relation ($\Pi \propto \rho^{-1/2}$) follows from acoustic wave propagation, confirmed by both the standing wave calculation and the one-zone model. The dynamical stability condition ($\gamma > 4/3$) connects pulsation theory to stellar structure theory. The PLC relation connects density to observable luminosity and color.

**Evolutionarily:** Pulsation is a transient phase corresponding to the He-burning evolutionary stage. Stars cross the Instability Strip once or a few times during their lifetime, pulsating only while within the strip. The fraction of time spent inside sets the statistics of observed pulsators.

**Cosmological application:** The PL relation is the cornerstone of the extragalactic distance scale — the first rung of the Cosmic Distance Ladder — enabling distance measurements to galaxies up to tens of Mpc, calibrating Type Ia supernova distances, and ultimately the measurement of the Hubble constant.
