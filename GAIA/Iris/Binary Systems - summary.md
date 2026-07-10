# Binary Systems — Summary

## 1. Key Concepts

- **Binary system:** two gravitationally bound stars orbiting a common barycentre; not orbiting each other directly.
- **Separation $a$:** distance between component centres of mass (semi-major axis if elliptical).
- **Primary/secondary ($M_1, M_2$):** by convention $M_1 \geq M_2$; mass ratio $q = M_2/M_1 \leq 1$.
- **Roche potential $\Phi_\text{eff}$:** effective gravitational + centrifugal potential in the co-rotating frame.
- **Equipotential surfaces:** surfaces of constant $\Phi_\text{eff}$; hydrostatic gas follows them; form a figure-eight at the critical (Roche lobe) value.
- **Lagrangian points $L_1$–$L_5$:** points where $\nabla\Phi_\text{eff}=0$. $L_1$ (between stars), $L_2$ (beyond $M_2$), $L_3$ (beyond $M_1$) are unstable saddle points; $L_1$ is the mass-transfer gateway. $L_4$, $L_5$ (triangular, $60°$ off) are stable (Coriolis-stabilized, requires $M_1/M_2 > 25$).
- **Roche lobe:** the equipotential surface through $L_1$; the largest closed surface still gravitationally bound to a star; teardrop-shaped, pointed toward $L_1$.
- **Roche lobe overflow (RLOF):** mass flow through $L_1$ once a star fills its Roche lobe.
- **Detached / semidetached / contact systems:** classification by whether 0, 1, or 2 stars fill their Roche lobes.
- **Common envelope (CE):** in contact systems, a shared gas envelope surrounding both cores; short-lived, ends in merger or envelope ejection.
- **Accretion disk:** Keplerian disk formed by infalling material that retains orbital angular momentum; rotates in the same sense as the binary orbit.
- **Blue straggler stars (BSS):** stars brighter/bluer than the cluster MS-turnoff; formed via mass-transfer rejuvenation or direct MS-MS merger; observational proof of binary interaction.
- **Reduced mass $\mu$:** effective one-body mass equivalent for the two-body orbital problem.
- **Conservative mass transfer:** idealized case with no mass or angular momentum lost from the system.
- **Cataclysmic variable (CV):** WD accreting from a low-mass donor; outbursts from disk instabilities, not nuclear burning.
- **Classical nova:** thermonuclear runaway (H-flash) of degenerate accreted hydrogen on a WD surface; recurrent, WD survives.
- **Type Ia supernova:** thermonuclear disruption of a WD approaching the Chandrasekhar mass (accretion or WD–WD merger); standardizable candle.
- **Single-degenerate / double-degenerate channels:** Type Ia progenitor scenarios — WD + non-degenerate donor, vs. two merging WDs.
- **Binary survival criterion:** condition on ejected SN mass for the binary to remain bound.
- **X-ray binary:** NS or BH accretor releasing gravitational energy as X-rays; can arise via wind accretion or RLOF.

## 2. Key Equations

- Effective (Roche) potential: $$\Phi_{\text{eff}}(\mathbf{r}) = -\frac{GM_1}{|\mathbf{r}-\mathbf{r}_1|} -\frac{GM_2}{|\mathbf{r}-\mathbf{r}_2|} -\frac{1}{2}\omega^2|\mathbf{r}-\mathbf{r}_\text{cm}|^2$$ — potential in the co-rotating frame; used to locate Lagrangian points and equipotentials.
- Roche lobe effective radii: $$l_1 = a\left(0.5-0.227\log\frac{M_2}{M_1}\right), \quad l_2 = a\left(0.5+0.227\log\frac{M_2}{M_1}\right), \quad l_1+l_2=a$$ — approximate radii of the sphere with equal volume to each Roche lobe; the more massive star always has the larger lobe.
- Reduced mass: $$\mu = \frac{M_1 M_2}{M_1+M_2}$$ — equivalent one-body mass for Keplerian orbit analysis.
- Orbital angular momentum (general): $$L = \mu\sqrt{GMa(1-e^2)}$$ — reduces to $L=\mu\sqrt{GMa}$ for circular orbits ($e=0$).
- Perihelion/aphelion velocity ratio: $$\frac{v_p}{v_a}=\frac{r_a}{r_p}=\frac{1+e}{1-e}, \qquad v_p^2=\frac{GM}{a}\frac{1+e}{1-e}$$ — from angular momentum + energy conservation at the turning points.
- **Conservative mass-transfer orbital evolution equation (central result):** $$\boxed{\frac{1}{a}\frac{da}{dt} = \frac{2\dot M_1(M_1-M_2)}{M_1 M_2}}$$ — governs whether the orbit shrinks or widens; sign set by who is losing mass and the current mass ratio.
- Kepler's third law / frequency evolution: $$\omega^2=\frac{GM}{a^3}, \qquad \frac{1}{\omega}\frac{d\omega}{dt}=-\frac{3}{2}\frac{1}{a}\frac{da}{dt}$$ — orbit shrinking ($\dot a<0$) speeds up the orbit ($\dot\omega>0$) and vice versa.
- Accretion kinetic energy release: $$K=\frac{GMm}{R}$$ — energy released per infalling mass $m$; scales inversely with accretor radius (compactness).
- Nuclear vs. accretion efficiency (fraction of $mc^2$): H-burning $\approx 0.007$; WD accretion $\approx 0.00025$; NS accretion $\approx 0.15$; non-spinning BH $\approx 0.1$; maximally spinning BH $\approx 0.42$ — sets the luminosity hierarchy of accreting systems.
- Binary survival after instantaneous SN mass ejection $\delta m$: $$\delta m < \frac{M_1+M_2}{2}$$ — the ejected mass must be less than half the pre-explosion total mass for the system to stay bound.

## 3. Key Algorithms / Procedures

1. **Deriving $L=\mu\sqrt{GMa(1-e^2)}$:** apply angular-momentum conservation at perihelion/aphelion ($L=\mu r v$, $v\perp r$) → get $v_p/v_a$ ratio → apply energy conservation to solve $v_p$ → substitute into $L=\mu r_p v_p$ → simplify to the general formula (circular case drops the $e$ term).
2. **Deriving the conservative mass-transfer orbital equation:** start from $L=\mu\sqrt{GMa}$ (circular, $M=$const) → differentiate, set $\dot L=0$ → get $\frac{1}{a}\dot a = -\frac{2}{\mu}\dot\mu$ → compute $\dot\mu$ from $\mu=M_1M_2/M$ using $\dot M_2=-\dot M_1$ → substitute to obtain $\frac{1}{a}\dot a=\frac{2\dot M_1(M_1-M_2)}{M_1M_2}$.
3. **Sign analysis of mass transfer (apply the boxed equation):**
   a. Identify which star is currently the donor (sign of $\dot M_1$).
   b. Compare current masses ($M_1-M_2$ sign).
   c. Product of signs gives $\dot a$: same-sign factors → orbit widens (self-regulating/negative feedback); opposite-sign factors → orbit shrinks (runaway/positive feedback).
   d. Track how the shrinking/growing Roche lobe ($l\propto a$) feeds back on the donor's overflow rate.
4. **Nova thermonuclear runaway sequence:** accreted H layer becomes degenerate → shell reaches critical mass ($\sim10^{-4}M_\odot$) → CNO ignition at $T\gtrsim2\times10^7$K → degenerate burning raises $T$ without raising $P$ (runaway) → degeneracy lifted → explosive expansion/ejection at $\sim10^3$ km/s → WD survives, cycle repeats every $10^4$–$10^5$ yr.
5. **Case-study evolutionary pipeline (massive binary → X-ray binary):** ZAMS binary → primary fills Roche lobe first (RLOF, positive then self-regulating feedback) → primary strips to He core, secondary gains mass and widens orbit → He core collapses (Type II SN) → check survival criterion ($\delta m$ vs. $M_\text{tot}/2$) → if bound, detached BH+MS phase with wind accretion (HMXB) → secondary evolves, fills its own Roche lobe → full accretion disk forms onto BH, luminosity rises.

## 4. Watch Out For

- $L_1$, $L_2$, $L_3$ are all unstable (local maxima/saddle points) — only $L_4$/$L_5$ are stable, and only under the mass-ratio condition $M_1/M_2>25$.
- By convention, the mass-**losing** star in a semidetached system is called "the secondary" regardless of its original identity — naming reflects current state, not birth mass.
- Roche lobe radius depends on **both** $a$ and mass ratio — as $a$ changes, $l_1, l_2$ change too, creating the feedback loop; don't treat the Roche lobe as fixed.
- Sign convention trap: in the orbital evolution equation, $\dot M_1$ is positive when $M_1$ *accretes*, negative when it *donates* — always check which star is $M_1$ in a given problem before applying signs.
- Feedback reverses mid-transfer: once the initially more massive donor becomes the less massive star, $(M_1-M_2)$ flips sign, turning runaway (shrinking) into self-regulating (widening) — the system self-corrects rather than transferring indefinitely.
- Distinguish CV dwarf-nova outbursts (disk instability, no nuclear burning) from classical novae (thermonuclear H-flash) — different physical mechanisms despite both being WD binaries.
- A classical nova does **not** destroy the WD; only a Type Ia SN (or merger reaching $M_\text{Ch}$) fully disrupts it.
- Neutron star accretion is ~30× more efficient than H-burning per unit mass, and BH accretion (spinning) can reach $0.42\,mc^2$ — far exceeding nuclear energy scales; don't assume nuclear burning dominates energetics near compact objects.
- SN survival criterion applies to **half the total pre-explosion mass**, not half the exploding star's own mass — easy factor-of-two error.
- Prior RLOF stripping the exploding star's envelope is often what allows the SN ejecta to satisfy the survival criterion; without it, ejected mass could exceed the bound-system threshold.
- Blue stragglers can form via **two distinct channels** (mass-transfer rejuvenation vs. direct MS-MS merger) — both are valid, not mutually exclusive explanations.
- Detached systems still interact gravitationally (tides, circularization) even with zero mass transfer — "detached" does not mean "non-interacting."
- In the HS 2231+2441 case, the object causing the common envelope is a **brown dwarf**, well below the H-burning mass limit ($\sim80\,M_J$) — CE physics does not require a stellar-mass companion.
