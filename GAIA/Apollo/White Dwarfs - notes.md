# White Dwarfs — Study Notes
**Source:** `25.WhiteDwarfs.pdf` | **Course:** Stellar Evolution (Evoluzione Stellare — parte V)

---

## 1. Final Stages of Low-Mass Star Evolution ($M < M_\mathrm{up}$)

### 1.1 Overview and Context

Stars with initial mass below the upper mass limit $M_\mathrm{up} \approx 8\,M_\odot$ develop a degenerate carbon-oxygen (CO) core during their Asymptotic Giant Branch (AGB) evolution. This degenerate CO core represents the definitive endpoint of the thermonuclear evolution of the core: once formed, no further central nuclear burning can occur. Consequently, the last thermonuclear activity in these stars takes place during the AGB evolutionary phase, and everything that follows is dictated by the removal of the envelope and the cooling of the remnant.

Stars slightly above $M_\mathrm{up}$ develop only a mildly degenerate CO core (shaded transition region around $8\,M_\odot$), while stars well above $M_\mathrm{up}$ develop non-degenerate cores and proceed to carbon ignition and beyond, eventually forming neutron stars or black holes. The physics of the boundary at $M_\mathrm{up}$ is therefore pivotal: below it, electron degeneracy halts the core contraction and the star ends as a white dwarf; above it, the core continues burning.

For low-mass stars the final stage of this evolution is characterised by an intense and dramatic event of **mass loss**, which strips away the hydrogen-rich envelope and exposes the hot CO core. Understanding mass loss is therefore the key to understanding how white dwarfs are born.

---

## 2. Mass Loss

### 2.1 Physical Basis and the Reimers Law

Mass loss in stellar evolution is poorly understood from first principles. In stellar models it is parametrised with a dimensionless free parameter $\eta$ whose value must be calibrated against observations. All stellar models are therefore sensitive to the assumed value of $\eta$.

Stars continuously emit particles from their surface through the **stellar wind**. In most evolutionary stages this emission is very small. For the present-day Sun the mass loss rate is:

$$\dot{M}_\odot = 4 \times 10^{-14}\,M_\odot\,\mathrm{yr}^{-1}$$

This is negligible over a stellar lifetime. However, mass loss becomes critically important in very luminous stars with luminosities approaching the Eddington luminosity (very massive blue main-sequence stars), and in evolved giant stars where the radius has increased greatly.

The most relevant events of mass loss during stellar evolution occur in stages where the **surface gravity** decreases because of the large expansion of the stellar radius. Recall that surface gravity is:

$$g = \frac{GM}{R^2}$$

where $G$ is Newton's gravitational constant, $M$ is the stellar mass, and $R$ is the stellar radius. For a solar-like star:
- On the main sequence: $\log g = 4.4$ (in cgs units, cm s$^{-2}$)
- As a red giant (RGB): $\log g = -0.5$

This is a decrease by nearly five orders of magnitude, meaning surface material is held roughly $10^5$ times less tightly on the RGB than on the MS. The causal chain is: radius increases $\rightarrow$ surface gravity decreases $\rightarrow$ outer layers less bound $\rightarrow$ mass loss rate increases.

Since the mass loss rate is expected to scale with large luminosity, large radius, and small mass (small gravity), a general scaling relation is:

$$\dot{M} \propto \frac{LR}{M}$$

This immediately explains why the RGB and AGB are the dominant phases of mass loss: both have high $L$ and large $R$, and the AGB in particular extends to enormous radii.

The most widely used empirical prescription is the **Reimers (1975) law**:

$$\dot{M} = -4 \times 10^{-13}\,\eta\,\frac{L}{gR}\quad [M_\odot\,\mathrm{yr}^{-1}]$$

where:
- $\eta$ is the dimensionless free parameter (calibrated empirically, typically $\eta \approx 0.2$–$0.5$)
- $L$ is the stellar luminosity
- $g = GM/R^2$ is the surface gravity
- $R$ is the stellar radius
- The mass loss rate is expressed in solar masses per year

Because $g = GM/R^2$, the formula can be rewritten as $\dot{M} \propto LR/M$, consistent with the general scaling. The negative sign indicates mass is being lost. Reimers' law is empirical and was calibrated against observations of red giants; it should be regarded as an order-of-magnitude guide rather than a precise physical law.

### 2.2 Physical Mechanisms of Stellar Winds

Several physical mechanisms cooperate to drive mass loss from evolved stars:

**Radiation-driven winds:** As the stellar radius increases during RGB and AGB evolution, the surface temperature decreases. At sufficiently low surface temperatures, molecules and **dust grains** can form in the outer atmosphere. Dust grains have a very large geometric cross-section and high extinction efficiency (orders of magnitude greater than gas atoms), so they trap the outgoing radiation flux very efficiently. The radiation pressure on these grains (photon momentum transfer to the atmospheric material) then drives a **radiation-driven wind** that ejects material from the surface. This mechanism is especially important during the cooler AGB phase.

**Convection support:** Deep convective motions in the envelope (which become more vigorous on the AGB) may also support the release of surface material by carrying momentum upward toward the surface layers.

### 2.3 The Superwind and the End of the AGB

The most dramatic manifestation of mass loss occurs at the **very end of the AGB phase**: the so-called **superwind** phenomenon. This is characterised by an extraordinary mass loss rate:

$$\dot{M}_\mathrm{superwind} \sim 10^{-4}\,M_\odot\,\mathrm{yr}^{-1}$$

At this rate, a star can lose $1\,M_\odot$ in only $10{,}000$ years. The superwind is physically connected to the large-amplitude pulsations that AGB stars undergo — known as **MIRA variables**. During the pulsation cycles, gas compression increases the atmospheric density, further promoting molecule and dust grain formation. These dust grains trap the outgoing radiation flux and drive a strong **dust-driven wind** through both their large geometrical cross-section and their high extinction efficiency.

The AGB phase terminates when the hydrogen-rich envelope is reduced to a **minimum mass of $10^{-3}\,M_\odot$**. Below this limit, the H-burning shell cannot activate the burning process — the envelope is too thin to sustain nuclear reactions. This is the termination condition: the star leaves the AGB when the envelope mass drops below $\sim 10^{-3}\,M_\odot$.

---

## 3. Planetary Nebula Formation

### 3.1 From Superwind Ejecta to Planetary Nebula

The material ejected during the superwind phase forms a cool, molecular, and dusty expanding envelope around the stellar remnant. This ejected envelope has the chemical composition of the stellar envelope at the end of the Thermally Pulsing AGB (TPAGB) phase — it therefore carries the chemical fingerprints of all the nuclear processing and dredge-up events that occurred during the AGB. Initially, this dusty envelope **completely veils the remnant star** from optical observations, making the central star invisible.

The transition to a planetary nebula (PN) proceeds as follows: once the thermonuclear activity has concluded, the remaining stellar remnant (the proto-white-dwarf) contracts and heats up at **nearly constant luminosity**. By the Stefan-Boltzmann law:

$$L = 4\pi\sigma R^2 T^4$$

if $L$ is constant while $R$ decreases, then $T$ must increase accordingly (the contraction is entirely compensated by the increase of temperature). When the effective temperature of the central remnant reaches approximately **30,000 K**, it begins to emit copious UV photons capable of ionising the surrounding expanding gas-dust envelope. This ionisation creates the glowing shell known as the **planetary nebula**.

The diagram on page 12 (HR diagram for a 1.25 $M_\odot$, $Z=0.02$ model) illustrates this evolution:
- Axes: $\log T_e$ (horizontal, decreasing rightward from ~5 to ~3.5) vs. $\log(L/L_\odot)$ (vertical, from $-2$ to $+4$)
- The AGB lifetime is approximately 0.9 Myr
- Once the envelope is released, the star evolves leftward along the PN phase (dashed red line) at nearly constant luminosity $\log(L/L_\odot) \approx 3.3$
- The transition takes ~42,000 years from the end of the AGB to $\log T_e \approx 5$
- Post-AGB stars occupy an oval region at $\log T_e \approx 4.2$–$4.7$, $\log L \approx 2.5$–$3.5$
- Central stars of PNe occupy a narrower region at $\log T_e \approx 4.5$–$5$, $\log L \approx 2$–$3.3$
- White dwarfs occupy the lower-left diagonal band ($\log T_e \approx 4$–$5$, $\log L \approx -2.5$ to $+0.5$)
- Transition times are very rapid (~100 years) for the most massive objects, meaning they cross from the AGB tip to high $T_e$ so fast that the ejected nebula has already dispersed before it can be ionised — **no PN is formed** for these massive WDs
- Transition times are ~$10^4$ years for low-mass objects, allowing PN formation
- The final WD mass in this example is $0.57\,M_\odot$
- Mass loss rates during the post-AGB evolution are low ($\sim 10^{-8}\,M_\odot\,\mathrm{yr}^{-1}$)

### 3.2 Chemical Enrichment of the ISM via Planetary Nebulae

The ejected material that forms the planetary nebula represents the **contribution of low-mass stars to the chemical enrichment of the interstellar medium (ISM)**. The PN material contains:

1. **CNO-processed materials** — products of the CNO cycle that operated in the H-burning shell
2. **He-burning products (C, O)** — carbon and oxygen synthesised during core and shell He burning (the triple-alpha process and $^{12}$C $+$ $^4$He $\rightarrow$ $^{16}$O $+$ $\gamma$)
3. **s-process elements** — slow neutron capture products synthesised in the He-burning shell during thermal pulses on the AGB
4. **Lithium** — produced via the Cameron-Fowler mechanism in massive AGB stars

These are the channels by which low-mass and intermediate-mass stars return chemically enriched material to the galactic ISM, playing an essential role in galactic chemical evolution.

### 3.3 The Stellar Remnant

After the envelope has been ejected, the residual He and H shells are **no longer massive enough** to sustain any thermonuclear activity. Nuclear burning definitively dies out. The remnant — the CO core — is left to cool down as a **CO white dwarf**. This is the defining moment: the birth of the white dwarf.

---

## 4. White Dwarf Properties — Overview

### 4.1 HR Diagram Evolution and Cooling Tracks

Stars with different initial masses produce WDs with different final masses. The full HR diagram (page 13) shows evolutionary tracks for $1\,M_\odot$ and $5\,M_\odot$ stars:
- The $1\,M_\odot$ track evolves through the RGB (He flash at the tip), horizontal branch, AGB (thermal pulses), post-AGB, and finally down to the WD cooling track
- The $5\,M_\odot$ track avoids the He flash (quiet He ignition), undergoes a second dredge-up, reaches the AGB with thermal pulses, then similarly terminates as a WD
- The WD cooling tracks are parallel diagonal dashed lines on the lower-left part of the HR diagram, labelled as "C-O White Dwarf (0.65 $M_\odot$)" and "WD(1.0 $M_\odot$)"
- The cooling sequences proceed at **constant radius** — as the WD cools, $L \propto T^4$ so the track is a straight line of slope 4 in the $\log L$ vs $\log T_e$ plane

The concept is aptly described as a **"train station"**: proto-WDs with different masses arrive at the top of the WD cooling region and are directed onto different cooling tracks according to their mass. Each mass has a fixed radius (from the mass-radius relation), and hence a specific cooling track. The question then becomes: what determines the mass of the CO core?

### 4.2 Sirius B as a Prototype White Dwarf

Sirius B, the companion to Sirius A in a binary system, is the prototype white dwarf because its mass was empirically measured via orbital mechanics:

- Mass: $M \approx 1.05\,M_\odot$
- Effective temperature: $T \approx 27{,}000\,\mathrm{K}$
- Radius: $R = 5.5 \times 10^8\,\mathrm{cm}$

The radius is of order the Earth's radius ($6 \times 10^8$ cm). Thus a white dwarf concentrates the mass of the Sun into a sphere the size of the Earth. The average density can be calculated:

$$\rho_\mathrm{Sirius\,B} = \frac{2 \times 10^{33}}{(4/3)\pi (5.5 \times 10^8)^3} = \frac{2 \times 10^{33}}{4 \cdot 30 \cdot 5.5 \times 10^{24}} = \frac{2 \times 10^9}{600} \approx 3 \times 10^6\,\mathrm{g\,cm^{-3}}$$

For comparison, the average solar density is $\sim 1.4\,\mathrm{g\,cm^{-3}}$. Thus white dwarf material is about $2 \times 10^6$ times denser than the Sun on average. A teaspoon of this material would weigh approximately **16 tons** on Earth.

### 4.3 Luminosity and Observability

White dwarfs are extremely faint. The expected luminosity of a typical WD is:

$$L_\mathrm{WD} \approx 0.003\,L_\odot = 10^{-3}\,L_\odot$$

Converting to absolute magnitude in the V-band, with the Sun's absolute V-band magnitude $M_\odot^V = 4.8$:

$$M_\mathrm{WD}^V - M_\odot^V = -2.5\,\log\left(\frac{L_\mathrm{WD}^V}{L_\odot^V}\right)$$

$$M_\mathrm{WD}^V - 4.8 = -2.5\,\log(0.003) \implies M_\mathrm{WD}^V = 11.2\,\mathrm{mag}$$

This is **6 magnitudes fainter** than the Sun. WDs are currently observable only within our own Galaxy. The maximum observable distance is determined by the distance modulus, assuming a limiting apparent magnitude of $V = 27$ (e.g. with HST):

$$V - M_V = 5\log d - 5$$
$$27 - 11.2 = 5\log d - 5 \implies \log d = 4.16 \implies d = 14\,\mathrm{kpc}$$

WDs can only be observed to $\sim 14\,\mathrm{kpc}$, i.e. within the Milky Way. Despite about **95% of all stars ending their lives as white dwarfs**, they are individually very faint and difficult to detect beyond our galaxy.

---

## 5. White Dwarf Internal Structure

### 5.1 Layer Composition

White dwarfs are the end products of the thermonuclear evolution of intermediate- and low-mass stars ($M < 8\,M_\odot$). Their internal structure, from centre outward, is:

**CO Core (dominant component):** The electron-degenerate C/O core is the direct product of the previous thermonuclear evolution via the reactions:

$$3\,^4\mathrm{He} \rightarrow {}^{12}\mathrm{C} + \gamma \quad \text{(triple-alpha)}$$
$${}^{12}\mathrm{C} + {}^4\mathrm{He} \rightarrow {}^{16}\mathrm{O} + \gamma$$

The relative C/O ratio in the core depends on the competition between these two reactions and is not perfectly constrained observationally.

**He layer:** The CO core is surrounded by a thin, **non-degenerate** layer of helium with mass $M_\mathrm{He} \sim 10^{-2}\,M_\mathrm{WD}$. This is the remnant of the He-rich zone that surrounded the CO core during the AGB phase.

**H layer:** The He layer is surrounded by an even thinner, **non-degenerate** layer of hydrogen with mass $M_\mathrm{H} \sim 10^{-4}\,M_\mathrm{WD}$. This is what remains of the original H envelope after mass loss.

The diagram (pages 18–20) shows this structure as a wedge/pie-slice diagram:
- The innermost large black region is the C/O core
- A red intermediate zone is the He layer ($\sim 0.01\,M_\mathrm{WD}$)
- The outermost white zone is the H layer ($\sim 0.0001\,M_\mathrm{WD}$)
- **Important caveat:** The diagram is NOT to scale. The H and He layers are extremely thin in mass fraction — essentially negligible shells surrounding the dominant CO core. Their geometric thickness in the diagram is grossly exaggerated for illustration purposes.

### 5.2 Energy Source and Cooling

The currently accepted model of white dwarfs predicts:
- **No thermonuclear processes** are active (the residual He and H shells are too thin to sustain burning)
- **No contraction** is possible (electron degeneracy prevents the star from shrinking — the degenerate pressure supports the structure independently of temperature)
- Therefore the luminosity **cannot be supported** by either thermonuclear energy or gravitational contraction

The luminosity of a white dwarf is **essentially supported by the progressive decrease of the internal (thermal) energy of the ions** in the CO lattice. The ions (C and O nuclei) are warm and carry thermal energy; as this thermal energy is radiated away, the WD slowly cools. This leads to the fundamental characterisation:

> **WD evolution is a pure cooling process at constant radius**, in which the core temperature, surface temperature, and luminosity all progressively decrease with time.

This is the classical picture. A notable exception mentioned in the slides is the recent discovery of "**slow cooling WDs**" by the authors' group, which has possibly modified this scenario (see later sections).

---

## 6. CO-WD Spectral Classification

### 6.1 Spectral Types

WDs are classified spectroscopically based on the absorption lines present in their spectra. The pressure broadening (FWHM of absorption lines proportional to the number density of atoms in the stellar atmosphere — see Carroll-Ostlie Section 9.4) is extreme due to the very high surface gravity, resulting in characteristically **broad** absorption lines:

| Type | Fraction | Spectral feature |
|------|----------|-----------------|
| **DA-WD** | ~80% | Broad H absorption lines |
| **DB-WD** | ~8% | Broad He spectral lines |
| **DC-WD** | ~14% | No spectral lines (featureless continuum) |

The dominance of DA (hydrogen atmosphere) WDs results from the gravitational settling of heavy elements: in WD atmospheres, the extremely high surface gravity causes heavier elements to sink rapidly, leaving a pure hydrogen atmosphere on the surface for most WDs. The remaining ~20% of DB and DC types reflect either different initial envelope compositions or different evolutionary pathways (e.g. some DB WDs may have lost their thin H layer entirely through various mechanisms).

### 6.2 Surface Gravity and Gravitational Settling

WDs are the highest surface gravity objects among ordinary stars. Numerically, for a solar-mass WD with radius $R \approx 6 \times 10^8$ cm:

$$g = \frac{GM}{R^2} = \frac{6.7 \times 10^{-8} \times 2 \times 10^{33}}{(6 \times 10^8)^2} = \frac{6.7 \times 2 \times 10^{25}}{36 \times 10^{16}} = \frac{20 \times 10^{24}}{6 \times 10^{16}} \approx 3 \times 10^8\,\mathrm{cm\,s^{-2}}$$

This is **10,000 times the solar surface gravity** ($g_\odot = 2.7 \times 10^4\,\mathrm{cm\,s^{-2}}$). The evolution of surface gravity through the life of a solar-mass star:
- Main sequence: $\log g = 4.4$
- Red giant branch: $\log g = -0.5$
- White dwarf: $\log g = 8.4$

This enormous surface gravity causes all elements heavier than hydrogen (or helium) to **sink into the WD interior** on very short timescales (days to thousands of years, depending on $T_e$), leaving only the lightest element in the photosphere. This gravitational settling is the reason why ~80% of WDs show pure H atmospheres.

---

## 7. Electron Degeneracy in WDs

### 7.1 Verifying the Degeneracy Condition

Most white dwarf properties are characterised by the conditions of **electron degeneracy** in the dominant CO core. The degeneracy condition requires:

$$\frac{T}{\rho^{2/3}} < D = 1.3 \times 10^5 \quad \text{(with } T \text{ in K, } \rho \text{ in g cm}^{-3}\text{)}$$

For a typical WD CO core: $T \sim 10^7\,\mathrm{K}$ and $\rho \sim 10^6\,\mathrm{g\,cm^{-3}}$:

$$\frac{T}{\rho^{2/3}} = \frac{10^7}{(10^6)^{2/3}} = \frac{10^7}{10^4} = 10^3 \ll 1.3 \times 10^5$$

The CO core of a WD is therefore **firmly in the electron-degenerate regime**. On the $\log T_c$ vs. $\log \rho_c$ diagram (page 24), the WD position (red dot at $\log \rho_c \approx 6$, $\log T_c \approx 7$) lies well within the degenerate region, to the right of the diagonal red line that separates degenerate from non-degenerate regimes. The present-day Sun lies comfortably in the non-degenerate region.

### 7.2 Derivation of the Degenerate Electron Pressure

The pressure of a degenerate electron gas can be derived from the general kinetic expression for gas pressure:

$$P = \frac{1}{3}m \int_0^\infty N(v)\,v^2\,dv$$

where $N(v)$ is the velocity distribution function. This can be approximated as:

$$P \sim \frac{1}{3}\,n_e\,p\,v$$

where $n_e$ is the electron number density, $p$ is the typical electron momentum, and $v$ is the typical electron velocity.

**Electron number density:** The number of electrons per unit volume is:

$$n_e = \left(\frac{Z}{A}\right)\frac{\rho}{m_H}$$

where $Z$ is the number of protons (atomic number), $A$ is the number of nucleons (mass number), $m_H$ is the hydrogen atom mass, and $\rho$ is the mass density. For a CO mixture, $Z/A \approx 1/2$ (both C and O have equal protons and nucleons, approximately).

**Momentum from the Heisenberg principle:** In complete degeneracy, electrons are fully packed in phase space but must remain distinguishable (Pauli exclusion principle). Therefore the uncertainty in electron position equals approximately their average separation:

$$\Delta x \sim x \sim n_e^{-1/3}$$

By Heisenberg's uncertainty principle $\Delta x \cdot \Delta p \sim \hbar$:

$$p \sim \Delta p \sim \frac{\hbar}{\Delta x} \sim \hbar\,n_e^{1/3} \sim \hbar\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3}$$

**Velocity in the non-relativistic regime:** $v = p/m_e$, so:

$$v \sim \frac{\hbar}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3}$$

**Non-relativistic degenerate pressure:** Substituting all three factors into $P \sim \frac{1}{3}n_e\,p\,v$:

$$P \sim \frac{1}{3}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right] \cdot \hbar\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3} \cdot \frac{\hbar}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3}$$

$$\boxed{P \sim \frac{1}{3}\frac{\hbar^2}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{5/3}}$$

This approximate expression is a very good approximation of the exact quantum-mechanical result:

$$P = \frac{(3\pi^2)^{2/3}}{5}\frac{\hbar^2}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{5/3}$$

Key properties of this pressure:
- It scales as $P \propto \rho^{5/3}$ — this is the **non-relativistic polytropic index** $\gamma = 5/3$
- It is **temperature-independent** — once degenerate, the pressure does not depend on $T$. This is the fundamental reason why WD cooling occurs at constant radius: reducing $T$ does not reduce $P$, so there is no adjustment of the structure.
- It depends on the composition through $Z/A$: for a pure H plasma $Z/A = 1$, for He or CO $Z/A = 1/2$

---

## 8. WD Fundamental Relations — Mass-Radius Relation

### 8.1 Derivation of the Non-Relativistic Mass-Radius Relation

The mass-radius relation for white dwarfs is a direct consequence of the **balance between the degenerate electron pressure and gravity**. The virial condition (hydrostatic equilibrium in energy form) gives approximately:

$$\frac{2}{3}\pi G\rho^2 R^2 = \frac{(3\pi^2)^{2/3}}{5}\frac{\hbar^2}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{5/3}$$

Substituting the uniform-density approximation $\rho = M_\mathrm{WD}\,/\,\left(\frac{4}{3}\pi R^3\right)$ and simplifying, after careful algebra all factors of $R$ cancel except for a $R^{-1}$ on the left (from $\rho^2 R^2 \propto M^2 R^{-6} \cdot R^2 = M^2 R^{-4}$) and $R^{-5/3}$ appears on the right. The result is:

$$R \sim \frac{(18\pi)^{2/3}}{10}\frac{\hbar^2}{Gm_e}\left[\left(\frac{Z}{A}\right)\frac{1}{m_H}\right]^{5/3}\frac{1}{M^{1/3}}$$

or equivalently:

$$M^{1/3} R \sim 3 \times 10^{19}\,\mathrm{[cgs]}$$

This is the **non-relativistic WD mass-radius relation**. Its profound implications:

1. **Massive WDs are smaller.** The product $M^{1/3}R = \mathrm{const}$, so $R \propto M^{-1/3}$. If the mass doubles, the radius decreases by a factor of $2^{1/3} \approx 1.26$.

2. **This is the opposite of normal stars**, where more massive stars are larger. The inverse mass-radius relation is a unique quantum mechanical effect: higher mass means higher density, which means more tightly packed electrons, which means higher degeneracy pressure per particle, which means a smaller (more compact) equilibrium structure is needed.

3. Equivalently: $MV \sim (3\times10^{19})^3$ where $V$ is the volume. More massive WDs reach equilibrium in **more compact structures**.

The numerical constant $\sim 3 \times 10^{19}$ in cgs is evaluated as:
$$\frac{(18\pi)^{2/3}}{10}\frac{\hbar^2}{Gm_e}\left[\frac{Z/A}{m_H}\right]^{5/3} \approx 1.5\frac{(10^{-27})^2}{6.7\times10^{-8}\times10^{-27}}\left[\frac{1/2}{1.7\times10^{-24}}\right]^{5/3} \approx 3\times10^{19}\,\mathrm{cm\,g^{1/3}}$$

### 8.2 Breakdown of the Non-Relativistic Approximation

The non-relativistic mass-radius relation cannot be extrapolated to arbitrarily high masses because at the densities of WDs, electrons move at relativistic speeds. This can be verified by computing the electron velocity at WD densities:

$$v \sim \frac{\hbar}{m_e}\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{1/3} = 0.7 \times 10^8\,\rho^{1/3}\,\mathrm{cm\,s^{-1}}$$

At $\rho = 10^6\,\mathrm{g\,cm^{-3}}$:

$$v = 0.7 \times 10^8 \times (10^6)^{1/3} = 0.7 \times 10^8 \times 10^2 = 0.7 \times 10^{10}\,\mathrm{cm\,s^{-1}} \approx \frac{c}{3}$$

The electrons are moving at **$\sim 1/3$ of the speed of light** — relativistic corrections are therefore mandatory, and the non-relativistic treatment breaks down.

---

## 9. The Chandrasekhar Mass Limit

### 9.1 Relativistic Degenerate Pressure

In the **relativistic regime**, the velocity of the electron is $v \approx c$ (constant) rather than $v = p/m_e$ (which grows with density). This changes the pressure-density relation fundamentally:

Non-relativistic: $P \propto \rho^{5/3}$ (from $P \sim n_e p v$ with $v = p/m_e \propto \rho^{1/3}$)

Relativistic: $P \propto \rho^{4/3}$ (from $P \sim n_e p c$ with $v = c$, and $p \propto \rho^{1/3}$)

The exact relativistic expression for the degenerate electron pressure is:

$$P = \frac{(3\pi^2)^{1/3}}{4}\hbar c\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{4/3}$$

Note: (i) $\hbar c$ replaces $\hbar^2/m_e$ (the mass drops out in the ultra-relativistic limit), (ii) the exponent changes from $5/3$ to $4/3$.

### 9.2 Derivation of the Chandrasekhar Mass

Imposing the hydrostatic equilibrium balance with the relativistic pressure:

$$\frac{2}{3}\pi G\rho^2 R^2 = \frac{(3\pi^2)^{1/3}}{4}\hbar c\left[\left(\frac{Z}{A}\right)\frac{\rho}{m_H}\right]^{4/3}$$

Substituting $\rho = M/(4\pi R^3/3)$:

$$\frac{2}{3}\pi G\frac{M^2 R^2}{\left(\frac{4}{3}\pi\right)^2 R^6} = \frac{(3\pi^2)^{1/3}}{4}\hbar c\left[\left(\frac{Z}{A}\right)\frac{1}{m_H}\right]^{4/3}\frac{M^{4/3}}{\left(\frac{4}{3}\pi\right)^{4/3}R^4}$$

In the relativistic case, the $R$-dependence on both sides cancels completely — both sides scale as $R^{-4}$:

$$G\frac{M^2}{R^4} \propto \hbar c\,\left[\left(\frac{Z}{A}\right)\frac{1}{m_H}\right]^{4/3}\frac{M^{4/3}}{R^4}$$

$$\Rightarrow M^{2/3} = \mathrm{const} \times \frac{\hbar c}{G}\left[\left(\frac{Z}{A}\right)\frac{1}{m_H}\right]^{4/3}$$

This gives a **fixed mass**, independent of $R$. There is no free radius to adjust — only one specific mass satisfies the balance equation. This is the Chandrasekhar mass:

$$\boxed{M_\mathrm{Ch} = \frac{3\sqrt{2\pi}}{8}\left(\frac{\hbar c}{G}\right)^{3/2}\left[\left(\frac{Z}{A}\right)\frac{1}{m_H}\right]^2}$$

### 9.3 Physical Significance and Value

The Chandrasekhar mass is one of the most profound results in astrophysics. Its "heart" is the combination of three fundamental constants:
- $\hbar$ — representing **quantum physics** (Pauli exclusion principle, degeneracy)
- $c$ — representing **special relativity** (electrons approaching light speed)
- $G$ — representing **gravity** (the force that electron degeneracy must overcome)

Together $\hbar c/G$ sets a mass scale where quantum mechanics, relativity, and gravity meet. Numerically:

$$M_\mathrm{Ch} = 1.44\,M_\odot$$

No white dwarf more massive than $1.44\,M_\odot$ has ever been observed, confirming this theoretical limit. The exact expression accounting for the hydrogen abundance $X$ in the envelope is:

$$M_\mathrm{Ch} = 1.44\,(1+X)^2\,M_\odot$$

For a pure CO core ($X = 0$): $M_\mathrm{Ch} = 1.44\,M_\odot$. For a He WD ($X = 0$): same. For an H-rich composition the limit is higher. In practice, the relevant composition for the CO core has $Z/A = 1/2$, giving $M_\mathrm{Ch} = 1.44\,M_\odot$.

The physical meaning is as follows: in the relativistic limit, the electron pressure scales as $\rho^{4/3}$ and gravity also scales as $\rho^{4/3}$ (for a fixed mass within a given radius). There is therefore only one mass where these two forces are in balance — for any higher mass, gravity wins over the pressure at all densities and radii, and there is no equilibrium. The star collapses. This is why the Chandrasekhar mass is a **maximum mass limit** rather than a mass-radius relation.

---

## 10. The Chandrasekhar Mass — Scope and Critical Warnings

### 10.1 General Applicability

The Chandrasekhar mass limit is **not** exclusively a white dwarf concept. It is a general result applying to **any stellar structure or sub-structure maintained in hydrostatic equilibrium by electron degeneracy pressure**. This is a critical distinction:

- It applies to CO white dwarfs
- It applies to He white dwarfs
- It applies to **degenerate iron cores inside evolved massive stars** (just before core collapse)
- In all cases it is the mass of the electron-degenerate sub-structure, not the initial mass of the star

**Critical warning:** The Chandrasekhar mass $M_\mathrm{Ch} = 1.44\,M_\odot$ must never be confused with the **initial mass of the progenitor star**. An initial $8\,M_\odot$ star can develop a degenerate CO core and leave a WD of $\sim 1\,M_\odot$ well below $M_\mathrm{Ch}$. What matters is the mass of the electron-degenerate structure, not the original stellar mass.

### 10.2 Mass-Density and Mass-Radius Diagrams

The Chandrasekhar mass limit is graphically illustrated in two complementary diagrams (page 42):

**Plot (a) — Mass vs. central density ($M/M_\odot$ vs. $\log \rho_c$):**
- Axes: horizontal = $\log \rho_c$ from 6 to 10; vertical = $M/M_\odot$ from 0 to above 1.0
- The curve rises steeply from low density, reaches a maximum at $M = M_\mathrm{Ch}$ (red horizontal line), and then turns over and would decrease
- The red horizontal line marks the Chandrasekhar limit — the curve never exceeds this maximum
- Physical interpretation: as mass increases, the central density must increase to maintain equilibrium; but as electrons become relativistic, the pressure-density index changes from $5/3$ to $4/3$ and the maximum supportable mass saturates at $M_\mathrm{Ch}$

**Plot (b) — Mass vs. radius ($M/M_\odot$ vs. $\log R/R_\odot$):**
- Axes: horizontal = $\log R/R_\odot$ from $-3$ to $-2$; vertical = $M/M_\odot$ from 0 to above 1.0
- The curve rises from small radii (very massive, very compact objects), reaches a maximum, then falls
- The red horizontal line again marks the Chandrasekhar limit
- Physical interpretation: this is the famous inverse mass-radius relation — more massive WDs have smaller radii; as $M \rightarrow M_\mathrm{Ch}$, the radius $R \rightarrow 0$. At the Chandrasekhar limit the radius shrinks to zero in the idealised treatment.
- Real physics prevents this: inverse beta decay and neutronisation set in before collapse, halting the purely electronic degeneracy support and leading either to a neutron star or a complete disruption (Type Ia supernova if accretion is the mechanism).

---

## 11. WD Cooling Sequence — HR Diagram Properties

### 11.1 Cooling at Constant Radius in the HR Diagram

Since the WD structure is supported by electron degeneracy, **no contraction is possible** — the radius is fixed by the mass-radius relation. Consequently, WD evolution in the HR diagram proceeds at a **constant radius**. From the Stefan-Boltzmann law $L = 4\pi\sigma R^2 T_e^4$, if $R = \mathrm{const}$, then:

$$\log\frac{L}{L_\odot} \propto 4\,\log\frac{T_e}{T_\odot} + 2\,\log\frac{R}{R_\odot} + c$$

For fixed $R$, this is a straight line in the $\log L$ vs. $\log T_e$ plane with slope 4. Each WD mass traces a distinct parallel straight-line cooling track, because the mass-radius relation assigns a unique $R$ to each $M$. The mass-radius relation $M \sim R^{-3}$ (i.e. $R \propto M^{-1/3}$) substituted into the luminosity equation gives:

$$\log\frac{L}{L_\odot} \propto 4\,\log\frac{T_e}{T_\odot} - \frac{2}{3}\,\log\frac{M}{M_\odot} + c$$

**Key consequence at fixed temperature:** More massive WDs are **less luminous** than less-massive WDs. This is because more massive WDs have smaller radii (from the inverse mass-radius relation), hence smaller radiating surface area, hence lower luminosity at the same $T_e$.

### 11.2 HR Diagram of WD Cooling Sequences (Figure 26.1)

The theoretical HR diagram for WDs (pages 45–46) shows:
- Axes: $\log T_e$ from 4.4 to 3.6 (horizontal, decreasing rightward); $\log L/L_\odot$ from 0 to $-4$ (vertical)
- The main sequence runs diagonally from upper-left to lower-right as a reference
- Four WD cooling sequences are shown as parallel diagonal lines labelled by mass: $0.25\,M_\odot$, $0.50\,M_\odot$, $0.80\,M_\odot$, $1.00\,M_\odot$
- The tracks are **parallel** — WDs cool along lines of equal slope 4 in log-log space
- The $0.25\,M_\odot$ track lies **above** the $1.00\,M_\odot$ track at any given temperature, confirming: less massive WDs are more luminous at fixed $T_e$
- A blue arrow on the $0.5\,M_\odot$ track shows the direction of evolution: toward lower $T_e$ and lower $L$ as time progresses

On a second version of the same diagram (page 46), a **vertical blue line** at $\log T_e = 4.2$ and a **horizontal red line** at $\log L/L_\odot = -2.7$ are added to illustrate isochrones — all WDs of a given age cluster along lines in the HR diagram.

The train-station analogy (page 47–48): proto-WDs arrive at the top-left region of the WD sequence (green oval at $\log T_e \approx 4.6$–$5$, $\log L \approx 2$–$3$) after the PN phase. They are then dispatched onto different cooling tracks depending on their mass. The mass sets the radius, and the radius sets the cooling track. All subsequent evolution is a slow drift downward and to the right along that track.

---

## 12. WD Internal Structure — Isothermal Core and Degenerate/Non-Degenerate Boundary

### 12.1 Isothermal Core from Electron Conduction

An important consequence of electron degeneracy is that it promotes extremely efficient **thermal conduction**. In a degenerate gas, all low-energy electron states are occupied (Fermi sea is full). When an electron tries to scatter off an ion nucleus, it cannot do so unless it finds an empty quantum state to scatter into. This means that low-energy scatterings are Pauli-blocked — only electrons near the Fermi surface can scatter. The net result is that electron **mean free paths** are very large in a degenerate gas (compared to a non-degenerate plasma). Since thermal conduction scales with the mean free path, electron conduction in the WD core is extremely efficient.

This leads to the key structural result: **the innermost region of the WD is essentially isothermal**. Temperature gradients are flattened out by conduction on short timescales. The whole degenerate core — which constitutes the vast majority of the WD mass — sits at a uniform temperature $T_c$ (the central temperature).

### 12.2 Temperature Profile from the Internal Structure Diagram (Figure 15.8)

The temperature profile inside a WD model is shown in a detailed figure (pages 49–52):
- Horizontal axis: $r/R_\mathrm{WD}$ from 0 (centre) to 1 (surface)
- Vertical axis: $\log_{10} T$ (K) from $-3$ to $+7$, and also the degeneracy parameter $\log_{10}(T\rho^{-2/3} D^{-1})$ from $-3$ to $+7$

The upper flat curve labelled $\log_{10} T$(K) is approximately constant at $\log T \approx 7$ (i.e. $T \approx 10^7$ K) from $r/R_\mathrm{WD} = 0$ to $\approx 0.95$ — this is the isothermal core (highlighted by the blue oval in the slides). The curve then **drops steeply** at $r/R_\mathrm{WD} \approx 0.95$–$1.0$ to the surface temperature, which is much lower.

The lower slowly rising curve labelled $\log_{10}(T\rho^{-2/3}D^{-1})$ measures the degree of degeneracy. This quantity is below zero (i.e. $T/\rho^{2/3} < D$) throughout the interior — the material is degenerate everywhere the curve is below the dashed red line at $y = 0$. Only in the extreme outer layers ($r/R_\mathrm{WD} > 0.97$–$1.0$) does this quantity cross zero — indicating the **thin non-degenerate surface layer** (highlighted by the blue oval in the version on page 50).

The structural picture (page 51):
- The large hatched interior region is **completely degenerate**
- The thin yellow outer ring is the **non-degenerate layer**
- The degenerate portion is conductive and isothermal
- The non-degenerate layer is where the temperature drops from $T_c$ to $T_\mathrm{surface}$ — this is where the luminosity is set by radiative transport

The degenerate/non-degenerate **border** (green line in the figure on page 52 and page 57) sits at $r/R_\mathrm{WD} \approx 0.97$. At this border, the condition $T/\rho^{2/3} = D$ is exactly satisfied. Since the core is isothermal, the temperature at this border equals $T_c$ everywhere along it.

---

## 13. WD Cooling Sequence Properties — Luminosity-Temperature Relation

### 13.1 Derivation via the Non-Degenerate Envelope

The peculiar two-layer structure (isothermal degenerate core + thin non-degenerate outer envelope) allows a precise relationship between the **observed luminosity** and the **central temperature** to be derived analytically. The derivation proceeds through the non-degenerate layer using standard stellar physics.

**Step 1 — Combine hydrostatic equilibrium and radiative gradient:**

In the non-degenerate outer layer, two equations hold:

$$\frac{dP}{dr} = -\frac{GM\rho}{r^2} \quad \text{(hydrostatic equilibrium)}$$

$$\frac{dT}{dr} = -\frac{3\kappa\rho}{4ac}\frac{1}{T^3}\frac{L_r}{4\pi r^2} \quad \text{(radiative temperature gradient)}$$

Dividing one by the other to eliminate $r$:

$$\frac{dP}{dT} = \frac{GM}{L_r}\frac{16\pi ac}{3}\frac{T^3}{\kappa}$$

**Step 2 — Apply Kramers bound-free opacity:**

The opacity of the non-degenerate layer is dominated by the **bound-free (Kramers) opacity**:

$$\kappa = \kappa_0\,\rho\,T^{-3.5}$$

where $\kappa_0 = 4.34 \times 10^{25}\,Z(1+X)\,\mathrm{cm^2\,g^{-1}}$, $Z$ is the heavy-element abundance, and $X$ is the hydrogen abundance. Substituting this opacity and the ideal gas equation of state $\rho = P\mu H/(kT)$ (where $\mu$ is the mean molecular weight, $H$ is the hydrogen mass, and $k$ is Boltzmann's constant), after several algebraic steps:

$$P\,dP = \frac{16\pi ac}{3}\frac{GM}{L}\frac{k}{\kappa_0\mu H}\,T^{7.5}\,dT$$

**Step 3 — Integrate from the surface to the degenerate border:**

Integrating (with boundary condition $P \approx 0$ at the surface):

$$P^2 = \frac{2}{17}\left(\frac{16\pi ac\,GM}{3\,L}\frac{k}{\kappa_0\mu H}\right) T^{17/2}$$

$$P = \left(\frac{4\cdot16\pi ac\,GM}{17\cdot3\cdot L}\frac{k}{\kappa_0\mu H}\right)^{1/2} T^{17/4}$$

From the ideal gas law, the density is then:
$$\rho = \left(\frac{4\cdot16\pi ac\,GM}{17\cdot3\cdot L\,\kappa_0}\right)^{1/2}\left(\frac{\mu H}{k}\right)^{1/2} T^{13/4}$$

This is a relation connecting density, luminosity, and temperature valid in the non-degenerate layers. It connects the observable luminosity to the local conditions.

### 13.2 Matching Condition at the Degenerate Border

The key step is to **evaluate these expressions at the degenerate/non-degenerate border** (the green line in the figure), where:
1. The degeneracy condition is exactly satisfied: $T/\rho^{2/3} = D$, i.e. $T = D\rho^{2/3}$
2. The temperature at this border equals the core temperature $T_c$ (since the core is isothermal)

Substituting $T^3 D^{-3} = \rho^2$ into the density equation evaluated at $T = T_c$:

$$T_c^3\,D^{-3} = \left(\frac{4\cdot16\pi ac\,GM}{17\cdot3\cdot L}\frac{\mu H}{k\kappa_0}\right) T_c^{13/2}$$

Solving for $L$:

$$\boxed{L = c\,T_c^{7/2}}$$

where the constant is:

$$c \equiv \frac{4D^3\,16\pi ac\,GH}{17\cdot3\cdot\kappa_0 k}\,\mu\,M_\mathrm{WD} = 7.3 \times 10^5\,\left(\frac{M_\mathrm{WD}}{M_\odot}\right)\frac{\mu}{Z(1+X)}$$

This is the fundamental result: **the luminosity of a WD is proportional to $T_c^{7/2}$**, where $T_c$ is the central (core) temperature. The surface temperature is different and much lower; the observable $T_\mathrm{eff}$ is linked to $T_c$ only through the non-degenerate envelope, but the luminosity is directly set by $T_c^{7/2}$. This relation is what makes the Mestel cooling theory tractable.

---

## 14. Energy Source of WD Luminosity and the Mestel Cooling Law

### 14.1 Thermal Energy of the Ions as the Energy Reservoir

Since no thermonuclear processes are active and no contraction is possible, the luminosity must be drawn from the **internal (thermal) energy of the CO ions** in the degenerate core. The number of ions in a WD of mass $M_\mathrm{WD}$ made of carbon ($A = 12$) is:

$$N_\mathrm{ions} = \frac{M_\mathrm{WD}}{A\,m_H}$$

Each ion has thermal energy:

$$E_c \sim \frac{3}{2}kT_c$$

Therefore the total internal thermal energy (the energy reservoir):

$$U = \frac{M_\mathrm{WD}}{A\,m_H}\frac{3}{2}kT_c$$

**Numerical estimate for a $1\,M_\odot$ CO-WD at $T_c = 10^7$ K:**

$$U = \frac{2\times10^{33}}{12 \times 1.7\times10^{-24}}\frac{3}{2}(1.4\times10^{-16})(10^7) = \frac{1}{4}\times10^{48}\,\mathrm{erg} \approx 2.5\times10^{47}\,\mathrm{erg}$$

This enormous energy reservoir ($2.5 \times 10^{47}$ erg) is the only energy source of the WD. The WD luminosity is the rate at which this reservoir is depleted:

$$L_\mathrm{WD} = -\frac{dU}{dt} = -\frac{d}{dt}\left(\frac{M_\mathrm{WD}}{Am_H}\frac{3}{2}kT_c\right) = -B\frac{dT_c}{dt}$$

where:
$$B \equiv \frac{M_\mathrm{WD}}{Am_H}\frac{3}{2}k$$

### 14.2 Derivation of the Mestel Cooling Law

Equating the two expressions for the luminosity ($L = cT_c^{7/2}$ from the envelope analysis, and $L = -B\,dT_c/dt$ from the thermal reservoir):

$$-B\frac{dT_c}{dt} = cT_c^{7/2}$$

This ODE connects the **cooling time** to the **central temperature**. Separating variables:

$$T_c^{-7/2}\,dT_c = -\frac{c}{B}\,dt$$

Integrating with initial condition $T_c = T_0$ at $t = 0$:

$$\left[-\frac{2}{5}T_c^{-5/2}\right]_{T_0}^{T(t)} = -\frac{c}{B}\,t$$

$$T_c^{-5/2} - T_0^{-5/2} = \frac{5}{2}\frac{c}{B}\,t$$

$$T_c(t) = T_0\left[1 + \frac{5}{2}\frac{t}{\tau_0}\right]^{-2/5}$$

where $\tau_0 = B/(cT_0^{5/2})$ is the **cooling timescale at the initial temperature $T_0$**.

Since $L_0 = cT_0^{7/2}$ and $L_\mathrm{WD} = cT_c^{7/2}$:

$$\boxed{L_\mathrm{WD}(t) = L_0\left[1 + \frac{5}{2}\frac{t}{\tau_0}\right]^{-7/5}}$$

This is the **Mestel Cooling Law** (Mestel 1952). Its physical content:

1. At early times ($t \ll \tau_0$): $L \approx L_0(1 - \frac{7}{2}\frac{t}{\tau_0})$ — nearly linear decline
2. At late times ($t \gg \tau_0$): $L \propto t^{-7/5}$ — the luminosity decreases as a **power law** $t^{-7/5}$
3. The luminosity declines rapidly at first (very hot WDs cool quickly) and then more slowly as the WD dims (cooler WDs take longer to cool further)
4. **Important note:** $T_c$ is the **central** temperature, not the surface temperature. The connection to the observable effective temperature is through $L = 4\pi\sigma R^2 T_e^4$, which gives a different time dependence for $T_e$.

### 14.3 The Cooling Time Formula

From the Mestel law, the **cooling time** to reach a given luminosity $L$ can be extracted:

$$\boxed{t_\mathrm{cool} = 8.8\times10^6\left(\frac{A}{12}\right)^{-1}\left(\frac{M}{M_\odot}\right)^{5/7}\left(\frac{\mu}{2}\right)^{-2/7}\left(\frac{L}{L_\odot}\right)^{-5/7}\,\mathrm{yr}}$$

For canonical CO chemistry ($A = 12$, $\mu = 2$):

$$\boxed{t_\mathrm{cool} = 8.8\times10^6\left(\frac{M}{M_\odot}\right)^{5/7}\left(\frac{L}{L_\odot}\right)^{-5/7}\,\mathrm{yr}}$$

This formula expresses the time it takes a WD of mass $M$ to cool to luminosity $L$. Key deductions:

- At fixed luminosity, $t_\mathrm{cool} \propto M^{5/7}$: **more massive WDs take longer to cool** to the same $L$ (because they have a larger thermal reservoir $U \propto M/A$)
- At fixed mass, $t_\mathrm{cool} \propto L^{-5/7}$: reaching a lower luminosity takes longer
- Therefore **low-mass WDs cool more rapidly** at fixed luminosity — they have a smaller thermal reservoir

**Numerical comparison at fixed luminosity:**

| $L/L_\odot$ | $t_\mathrm{cool}$ ($1\,M_\odot$) | $t_\mathrm{cool}$ ($0.5\,M_\odot$) |
|------------|----------------------------------|--------------------------------------|
| $10^{-1}$ | $4.4\times10^7$ yr | $2.7\times10^7$ yr |
| $10^{-2}$ | $2.2\times10^8$ yr | $1.4\times10^8$ yr |
| $10^{-3}$ | $1.1\times10^9$ yr | $6.8\times10^8$ yr |
| $10^{-4}$ | $5.6\times10^9$ yr | $3.4\times10^9$ yr |
| $10^{-4.5}$ | $12\times10^9$ yr (circled) | $7.6\times10^9$ yr |
| $10^{-4.8}$ | $20\times10^9$ yr | $12\times10^9$ yr (circled) |

After 12 Gyr, the massive $1\,M_\odot$ WD is at $\log(L/L_\odot) \approx -4.5$ (more luminous), while the $0.5\,M_\odot$ WD has already cooled to $\log(L/L_\odot) \approx -4.8$ (less luminous). At a fixed age of 12 Gyr, **more massive WDs appear more luminous** — the opposite of what one might naively expect. This remarkable reversal occurs because massive WDs cool more slowly due to their larger reservoir.

---

## 15. Cooling Curves and the Theoretical HR Diagram

### 15.1 Mestel Law vs. Full Numerical Models

The cooling curves for $0.6\,M_\odot$ WD models (page 67–69, Figure 15.9) show:
- Horizontal axis: time in $10^9$ yr from 0 to 15
- Vertical axis: $\log_{10}(L/L_\odot)$ from $-1$ to $-5$
- The solid line labelled "Eq. (15.21)" is the Mestel law prediction
- The dashed line labelled "Winget et al. (1987)" is a full numerical model

The two curves are **very close** for $\log(L/L_\odot) > -4$, confirming that the Mestel law is an excellent approximation of real cooling. Both show the characteristic rapid early decline followed by slower cooling.

At $\log(L/L_\odot) \approx -4$ (around 5–8 Gyr), the numerical model shows a pronounced **plateau** — the cooling rate temporarily slows down dramatically. This is the signature of **crystallisation**.

### 15.2 Crystallisation

As the WD cools, the CO ions eventually become cold enough to form an ordered **crystal lattice**. The physical process:
- As $T_c$ decreases, the thermal kinetic energy of the ions $\sim kT$ drops
- At the crystallisation temperature, the ions can no longer maintain a random liquid-like arrangement; they settle into a minimum-energy crystal structure
- Forming the crystal structure **reduces the degrees of freedom** of the ions (from 3 translational + 3 rotational for free particles to collective phonon modes in a crystal)
- This reduction in degrees of freedom **releases energy** (of order $\sim kT$ per ion — the latent heat of crystallisation)
- This energy release temporarily slows the cooling process, creating the luminosity plateau at $\log(L/L_\odot) \approx -4$

After crystallisation is complete, no further energy can be extracted from the structural transformation. The cooling resumes and accelerates toward the final fate of all CO WDs:

> **CO white dwarfs are destined to become Crystals of Carbon — a sort of Cosmic Diamond**

### 15.3 WD Cooling Isochrones in the Theoretical HR Diagram

The isochrone interpretation of the WD HR diagram (page 71):
- At fixed mass, luminosity and temperature both decrease as a function of time
- A "snapshot" at a fixed age (an isochrone) connects points of equal age on different cooling tracks
- From the diagram: at 1 Gyr, WDs all cluster along a specific diagonal segment; at 2 Gyr and 3 Gyr they cluster progressively further down-right
- This suggests the WD cooling sequence can be used as a cosmic chronometer

The counterintuitive result (pages 73–74): at fixed time, the **massive WDs appear more luminous** than less-massive ones. On the HR diagram at 12 Gyr, three blue dots are shown at the bottom of three different cooling tracks, with the most massive WD ($1\,M_\odot$, $\log T_e \approx 3.8$, $\log L \approx -4.5$) lying **higher** (more luminous) than the $0.5\,M_\odot$ WD ($\log T_e \approx 3.6$, $\log L \approx -4.8$). The isochrone therefore has a **negative slope** in the $\log L$ vs. $\log T_e$ plane — it points toward more massive (hotter and more luminous) objects, not toward less massive ones.

The cooling sequence in an observed CMD of NGC 6397 (Anderson et al. 2008b, page 75):
- Horizontal axis: colour $(m_{F606W} - m_{F814W})$; vertical axis: magnitude $m_{F606W}$
- The WD cooling sequence appears as a narrow diagonal band (red oval) bending to the right (redder colours) at the faint end
- The bend at the bottom of the sequence is the observable signature of the age of the cluster
- The same structure is seen in M4 (left panel) and NGC 6397 (middle and right panels) with progressively deeper HST exposures, clearly identifying the faint end of the cooling sequence

---

## 16. WD as a Cosmic Chronometer

### 16.1 The WD Luminosity Function as an Age Indicator

The precise monotonic relationship between WD luminosity and cooling time makes the WD cooling sequence a potential **cosmic chronometer**. The method:

1. Observe the WD population in a cluster or the solar neighbourhood
2. Construct the **WD luminosity function** (WDLF): the number of WDs per unit luminosity interval as a function of luminosity
3. As one goes to fainter luminosities, more WDs have accumulated (they spend longer at low $L$ because cooling slows down)
4. The WDLF rises toward faint magnitudes, but abruptly **drops off** at the faintest end
5. This abrupt drop is the signature of the **oldest WDs** — stars that have been cooling since the cluster formed have not yet had time to cool past a certain luminosity, so there are no WDs fainter than this cutoff
6. The luminosity of this cutoff directly gives the age of the stellar population via the Mestel cooling formula

**The observable used for solar-neighbourhood WDs:** The drastic drop in the WDLF at $\log(L/L_\odot) \approx -4.5$, observed in the classic Winget et al. (1987, Ap. J. Lett., 315, L77) figure (pages 76, 100):
- Horizontal axis: $\log(L/L_\odot)$ from 0 to $-5$; vertical axis: $\log N$ (number density in $\mathrm{pc^{-3}\,M_{\mathrm{bol}}^{-1}}$) from $-2$ to $-6$
- The data (filled circles) rise from $\log(L/L_\odot) = 0$ toward $\log(L/L_\odot) = -3$ following the theoretical curve, then peak and fall sharply around $\log(L/L_\odot) = -4$ to $-4.5$
- The sharp cutoff (blue arrow) indicates the faint end of the cooling sequence
- The theoretical curve matches well, confirming the Mestel framework and enabling an age estimate of the galactic disk

Previously this method could only be applied in the solar neighbourhood (where WDs as faint as $\log L/L_\odot \sim -5$ to $-6$ are detectable). HST observations have extended this to globular clusters (M4, NGC 6397), where the entire cooling sequence — down to its faint endpoint — can be resolved for the first time.

**Caveat:** Despite being a beautiful method, WD chronometry does not surpass the accuracy of the **main-sequence turnoff (MS-TO)** as an age indicator. The faintness of the relevant WDs introduces large photometric uncertainties, making it very unlikely to achieve age precision better than the MS-TO method. The MS-TO remains the gold standard for stellar population ages.

### 16.2 WD Cooling in the Observational CMD (Colour-Magnitude Diagram)

In the theoretical HR diagram, the cooling sequence is a perfect straight line (because $R$ is constant and $L \propto T_e^4$). However, in the **observational CMD** (magnitude vs. colour), the sequence is not a straight line. This is because:
- Photometric magnitudes in a given band depend not only on $L$ and $T_e$ but also on the **spectral energy distribution**
- As the WD surface temperature changes, the opacity of the outer H layer changes
- At $T_e \approx 10{,}000$ K, hydrogen in the outer layers transitions from **fully ionised** to **neutral**
- This transition dramatically changes the opacity of the H layer
- As a consequence, there is a **detectable "kink" or "deformation"** in the cooling sequence at $\sim 1$ Gyr for a $0.5\,M_\odot$ WD (page 103, 105)

The observational CMD (page 103) in the $M_U$ vs. $(U-V)_0$ plane for a $0.5\,M_\odot$ WD:
- Horizontal axis: colour $(U-V)_0$; vertical axis: absolute magnitude $M_U$
- Open squares trace the theoretical cooling sequence; filled squares mark specific ages (1, 2, 3 Gyr)
- The sequence starts at the upper left (blue, hot) and proceeds toward the lower right (red, cool), but there is a visible **change in slope** around $(U-V)_0 \approx -0.3$ to $0$ (corresponding to $T_e \approx 10{,}000$ K)
- The dashed line shows the hydrogen-atmosphere blackbody locus
- The kink arises because neutral hydrogen dramatically increases the opacity in the UV band, redistributing the flux toward longer wavelengths and making the WD appear **redder** than a blackbody at the same temperature

---

## 17. Post-AGB HR Diagram — Detailed Evolutionary Tracks

### 17.1 Figure 13.13 — Post-AGB Evolution of a 0.6 $M_\odot$ Star

An important reference figure (page 104, from Iben 1982) shows the post-AGB and PN-phase evolution of a $0.6\,M_\odot$ star in detail:

- Axes: $\log L$ from 1.5 to 4 (vertical), $\log T_e$ from 3.5 to 5.0 (horizontal)
- The curve starts at the upper right (AGB tip, cool and luminous) and evolves leftward (hotter) at nearly constant luminosity
- Numbered points (1–11) mark stages; the time elapsed (in years) and envelope mass (in $M_\odot$, in parentheses) are annotated:
  - $t = 0$: start of post-AGB evolution (AGB tip); envelope mass $\approx 0.00113\,M_\odot$
  - $t = 5{,}000$ yr (0.00080 $M_\odot$): still on the high-luminosity plateau, evolving left
  - $t = 10{,}000$ yr (0.00049 $M_\odot$): continue toward hotter $T_e$
  - $t = 15{,}000$ yr (0.00027 $M_\odot$): approaching the hot side
  - The track crosses the **Main Sequence Band** and the **Core Helium Burning Band** (hatched/shaded regions)
  - Labels identify the "Zero Age Horizontal Branch," "E-AGB," and "Fundamental Blue Edge"
  - A label "Last Thermal Pulse Begins" at point 11 ($t = 18{,}600$ yr, $\log L \approx 2.0$, $\log T_e \approx 5.0$)
  - The label "$R = 0.0285$" (solar radii) is attached to the final WD position at $\log T_e \approx 5$, $\log L \approx 2.8$
- The numbers $-5{,}000$, $-10{,}000$, $-20{,}000$, $-30{,}000$ along the top (at high $T_e$) indicate negative times, i.e. the star reaching very high temperatures; the corresponding envelope masses are given in parentheses (0.00147, 0.00184, 0.00253, 0.000315 $M_\odot$)

This figure illustrates that the post-AGB evolution at constant luminosity lasts thousands of years, and the final WD has $R \approx 0.03\,R_\odot$.

---

## 18. Slowly Cooling White Dwarfs — A New Discovery

### 18.1 The Standard Picture Revisited

The classical (canonical) picture of WD cooling assumes that **all WDs with the same mass cool at essentially the same rate**, following the Mestel law. This means:
- The relation between WD age and luminosity/temperature is universal for a given mass
- The WD luminosity is a reliable clock

The foundation of this universality is the assumption that **no thermonuclear activity is present** in the WD. This is guaranteed if the residual H-layer mass is below the threshold for H-burning:

$$M_\mathrm{H} < 10^{-4}\,M_\mathrm{WD}$$

If the H layer is above this threshold, the conditions at the base of the H envelope — where the temperature is highest — could be sufficient to sustain stable hydrogen burning. This would provide an **extra energy source** beyond the thermal reservoir, slowing the cooling. This is the mechanism behind slowly cooling WDs.

### 18.2 Publication: Chen et al. (2021), Nature Astronomy

**Reference:** Chen et al. (2021), *Nature Astronomy*, **5**, 1170 — "Slowly cooling white dwarfs in M13 from stable hydrogen burning"

**Authors:** Jianxing Chen, Francesco R. Ferraro, Mario Cadelano, Maurizio Salaris, Barbara Lanzoni, Cristina Pallanca, Leandro G. Althaus, Emanuele Dalessandro

This paper reported the **first empirical detection** of slowly cooling WDs. The discovery was made by comparing the WD populations of two globular clusters that are considered "twin" clusters — M3 and M13.

### 18.3 The M3–M13 Twin Cluster Comparison

**Why M3 and M13 are twins:** Both clusters have:
- The same age ($\sim 12$ Gyr)
- The same metallicity ($[Fe/H] \approx -1.5$)
- Almost the same total mass

Their CMDs are virtually identical when one cluster is shifted to the distance of the other (page 85 overlaid CMD): the main sequence, RGB, and upper AGB all overlap perfectly. The combined CMD (blue = M13, red = M3 shifted) shows a single tight sequence for the main evolutionary sequences.

**The crucial difference — Horizontal Branch morphology (pages 82–84):**
- M3 has a **red HB** (HB stars concentrated at cool temperatures, $T_e \sim 6{,}000$–$7{,}000$ K)
- M13 has a **blue HB** with an extended blue tail (E-HB): a large fraction of HB stars with $T_e > 10{,}000$ K, many at very high temperatures (20,000–30,000 K)

The HR diagram comparison in U–V colour (page 83, right panels):
- M3 (top): HB predominantly red (rightward cluster)
- M13 (bottom): HB predominantly blue (leftward band extending to extreme blue), with blue horizontal branch stars and some red clump

This difference in HB morphology has a profound downstream consequence for the WD population.

### 18.4 WD Population Excess in M13

When the WD cooling sequences of the two clusters are compared (page 86):
- Both CMDs show WDs as a diagonal sequence to the left of the main sequence
- In M13 (left panel): WDs are labelled at cooling times of 10 Myr, 30 Myr, 80 Myr from top to bottom
- In M3 (right panel): same labels
- After normalisation to the RGB population (which should be identical for the two clusters since they are twins), **M13 harbours 1.5 times more WDs than M3** (pages 86–87)

The comparison of WD luminosity functions (page 87):
- Horizontal axis: magnitude $m_{F275W}$; vertical axis: $N_\mathrm{WD}/N_\mathrm{RGB}$
- The blue points (M13) and red points (M3) agree at faint magnitudes but diverge strongly at bright magnitudes ($m_{F275W} \lesssim 22$)
- The solid line shows the prediction of canonical models — these canonical models **fail to reproduce** the M13 excess
- The comparison unambiguously shows a WD excess in M13, not a deficit in M3

**Total WD counts (page 87):**
- M13: 467 WDs, $N_\mathrm{RGB} = 1176$
- M3: 326 WDs, $N_\mathrm{RGB} = 1235$

The excess in M13 is $\sim 50\%$ after normalisation.

### 18.5 The Physical Explanation — HB Morphology and Residual H-Layer

The causal chain connecting HB morphology to slowly cooling WDs (pages 88–89 and 90):

**Step 1 — Blue HB stars skip the AGB phase:**
Stars with small envelopes on the HB (particularly the most extreme blue HB stars — E-HB stars) lose so much mass before and during the HB that their residual H envelope is too small to sustain an AGB phase. They **skip the AGB** (and therefore also skip the Third Dredge-Up).

**Step 2 — The Third Dredge-Up burns hydrogen:**
For stars that do experience the AGB and the Third Dredge-Up:
- During the Third Dredge-Up (the deepest mixing event in a star's lifetime), a convective zone penetrates inward into the He-burning shell
- Carbon produced in the He shell is carried outward into the envelope (C dredge-up)
- Simultaneously, a significant amount of hydrogen from the base of the envelope is mixed inward and burned
- This reduces the residual H-layer mass below $10^{-4}\,M_\mathrm{WD}$

**Step 3 — AGB-skipping stars retain more H:**
Stars that skip the AGB and Third Dredge-Up never undergo this H-consuming mixing event. Their residual H layer remains at $M_H > 10^{-4}\,M_\mathrm{WD}$. When these stars become WDs, the base of the thick H envelope is hot enough to sustain **stable H-burning** (pp-chain and CNO cycle).

**Step 4 — Extra energy slows cooling:**
The stable H-burning provides an additional luminosity contribution $L_\mathrm{CNO} + L_\mathrm{pp}$ on top of the ionic thermal energy. This extra energy source slows the cooling process, keeping the WD more luminous for longer. The WD appears to spend more time at high luminosity — hence there are more bright WDs than expected — creating the observed excess at $m_{F275W} \lesssim 22$.

**The summary diagram (page 90):**

| HB colour | AGB evolution | H layer | H-burning | WD type |
|-----------|--------------|---------|-----------|---------|
| Red HB | AGB + III Dredge-Up | $M_H < 10^{-4}\,M_\mathrm{WD}$ | No H-burning | **Canonical WD** |
| Blue HB (E-HB) | No-AGB, No III Dredge-Up | $M_H > 10^{-4}\,M_\mathrm{WD}$ | H-burning active | **Slow-cooling WD** |

The diagram on page 89 (HR/CMD) shows:
- M13 (left panel): blue oval marks E-HB stars at $m_{F275W} \approx 15.8$, $(m_{F275W}-m_{F336W}) \approx -0.5$; these bypass the AGB entirely (dashed blue arc); green oval marks the sparse AGB population; blue rectangle labelled "Slow WDs" at $m_{F275W} \approx 19$
- M3 (right panel): red oval marks the red HB; red arrow shows normal AGB evolution; green oval marks the well-populated AGB; red rectangle labelled "Standard WDs"

### 18.6 Quantitative Verification: AGB/HB Ratio

If the blue HB stars in M13 are indeed AGB-skippers, there should be significantly fewer AGB stars relative to the number of HB stars in M13 compared to M3 (page 94):

- In M13: $N_\mathrm{AGB}/N_\mathrm{HB} = 30/368 = 0.08 \pm 0.01$
- In M3: $N_\mathrm{AGB}/N_\mathrm{HB} = 45/344 = 0.13 \pm 0.02$

This confirms that M13 has significantly fewer AGB stars per HB star than M3. The difference is statistically significant and consistent with a large fraction of E-HB stars in M13 skipping the AGB phase.

### 18.7 Theoretical Models of H-Burning WDs

Theoretical cooling models including stable H-burning were computed (page 95):

**Left panel (two sub-panels):**
- Upper: $(L_\mathrm{CNO} + L_\mathrm{pp})/L_\mathrm{tot}$ vs. $\log T_e$ for a $0.54\,M_\odot$ WD with H-burning. The H-burning luminosity contributes 40–60% of the total at $\log T_e \approx 4$–$4.5$, with oscillations.
- Lower: Time delay [Myr] vs. $\log(L/L_\odot)$ for the same model — the time delay grows from 0 at high $L$ to $\sim 800$ Myr at $\log(L/L_\odot) \approx -4$

**Right panel:**
- Time delay [Myr] vs. $\log(L/L_\odot)$, comparing:
  - Solid blue: $0.54\,M_\odot$ WD with H-burning
  - Dashed black: $0.54\,M_\odot$ WD without H-burning
- At $\log(L/L_\odot) \approx -1$ to $-2$ (bright WDs), the time delay increases rapidly; at $\log L \approx -1.7$, the delay is $\Delta t \approx 60$ Myr (75% of the total delay)
- The global cumulative effect is **of order 1 Gyr** — the slow-cooling WDs are delayed by $\sim 1$ Gyr compared to canonical WDs at any given luminosity
- The H-burning process predominantly affects the **bright portion** of the WD cooling sequence ($\log L/L_\odot \gtrsim -2$)

### 18.8 Reproducing the M13 WD Luminosity Function

With the slow-cooling WD models (page 96), the observed M13 WD luminosity function is reproduced:

The plot shows $(\Sigma N_\mathrm{WD})/N_\mathrm{RGB}$ vs. $m_{F275W}$ for M13:
- Horizontal axis: $m_{F275W}$ from 19 to 23+
- Vertical axis: cumulative ratio from 0 to 0.4
- **Dashed black line:** 100% standard (canonical) WDs — significantly underpredicts the observed M13 counts at bright magnitudes
- **Solid black line:** 70% slow-cooling + 30% standard WDs — excellent match to the observed blue data points

The best-fit mixture is **70% slowly cooling WDs + 30% standard WDs** in M13. This fraction is consistent with the fraction of E-HB stars in M13 that are expected to skip the AGB.

### 18.9 Independent Confirmation in Additional Clusters

The discovery was further confirmed using two additional clusters (pages 91, 97):

**M5 (blue HB morphology):** Shows a WD excess compared to M3, consistent with a significant fraction of slow-cooling WDs. The luminosity function of M5 WDs lies above the 100%-standard model at bright magnitudes.

**NGC 6752 (blue HB morphology):** Also shows a WD excess. Comparison with theoretical models including 70% slow + 30% standard gives a better fit than 100% standard models.

In all cases the pattern is consistent: clusters with blue HB morphology (which produces AGB-skipping stars and hence thick H-layer WDs) show WD excesses that can only be explained by slow-cooling WDs.

### 18.10 Implications for WD Chronometry

The discovery of slowly cooling WDs has a direct and important implication for the use of WDs as cosmic chronometers:

> **Some caution should be used in adopting WDs as cosmic chronometers.**

The standard Mestel cooling theory assumes a universal, composition-independent cooling rate for all WDs of the same mass. The existence of slowly cooling WDs (with residual H-layers above the canonical threshold, driven by the HB morphology of the progenitor cluster) breaks this universality. For stellar populations with a significant fraction of blue HB stars:
- The WD cooling is systematically slower than the canonical prediction
- The luminosity cutoff of the WDLF would suggest a younger age than the true age
- Age estimates based on the WD technique need to be corrected for the fraction of slow-cooling WDs

The correction can be of order 1 Gyr — comparable to the uncertainties in MS-TO age determinations. This means WD chronometry must account for the HB morphology of the parent population.

---

## 19. Additional Consequences of the Mass-Radius Relation

### 19.1 Density Scales as $M^2$

From the mass-radius relation $M^{1/3}R = \mathrm{const}$, or equivalently $MR^3 = \mathrm{const}$ (i.e. $R \propto M^{-1/3}$), and since $\rho \propto M/R^3$:

$$\rho \propto \frac{M}{R^3} \propto \frac{M}{M^{-1}} = M^2$$

$$\boxed{\rho \propto M^2}$$

This is a remarkable result: **the density of a WD increases as the square of its mass**. A small increase in mass causes a large increase in density. Equivalently, $M^2/\rho = \mathrm{const}$ (since $M^{1/3}R \sim \mathrm{const}$ implies $MR^3 \sim \mathrm{const}$, and $\rho \sim M/R^3$, so $M/\rho \sim R^3 \sim M^{-1}$, giving $M^2/\rho \sim \mathrm{const}$).

**Practical implication (p. 101):** Adding even a small amount of mass onto a WD (e.g. by accretion from a companion in a binary system) causes a very large increase in the central density. This is physically crucial for understanding **Type Ia supernovae**: as a WD in a binary accretes mass toward the Chandrasekhar limit, the central density soars, eventually triggering thermonuclear carbon ignition.

In Italian (page 101): "Aggiungere piccole quantità di massa su una WD fa aumentare molto la densità" — Adding small amounts of mass to a WD increases the density greatly.


