# ASD-STE100 Issue 9 (2025-01-15) Writing Rules Reference

This document provides the complete, authoritative reference for all **53 writing rules** across Sections 1 through 9 and the **8 General Recommendations (`GR-1` through `GR-8`)** of **ASD-STE100 Issue 9 (released 2025-01-15)**.

---

## Section 1: Words (Rules 1.1–1.14)

| Rule | Official Issue 9 Summary | Practical Guidance & Examples |
| :--- | :--- | :--- |
| **Rule 1.1** | Use words that are: **Approved in the dictionary**, **Technical nouns (TNs)**, or **Technical verbs (TVs)**. | In the official dictionary ([ste-issue9-dictionary.json](../resources/ste-issue9-dictionary.json)), approved words appear in `UPPERCASE` (`879` entries) and unapproved words appear in `lowercase` (`1,319` entries). |
| **Rule 1.2** | Use approved words from the dictionary only as the specified part of speech. | `CHECK (n)` and `TEST (n)` are approved **nouns**, never verbs. Write `Do a check of the log` or `Examine the log` (never `Check the log`). `COMPLETE (v)` and `COMPLETED (adj)` are approved, whereas `complete (adj)` is unapproved (use `COMPLETED`, `FULL`, or `ALL`). |
| **Rule 1.3** | Use approved words only with their approved meanings. | `ABOUT (prep)` is approved only for *"concerned with"* (`data about the server`); for approximate quantities, use `APPROXIMATELY (adv)`. `SEE (v)` is approved only for physical sight with the eyes; for cross-references, use `REFER (v)` (`Refer to Table 1`). `SINCE` is unapproved as a causal conjunction; use `BECAUSE (conj)`. |
| **Rule 1.4** | Use only the approved forms of verbs and adjectives. | The dictionary lists every permitted inflected form (e.g., `ABSORB (v), ABSORBS, ABSORBED, ABSORBED` and `LARGE (adj), LARGER, LARGEST`). Adjectives such as `LESS (adj)` and `TACKY (adj)` have no other forms. Color technical nouns (Category 17) have no comparative or superlative forms. |
| **Rule 1.5** | You can use words that you can include in a **technical noun category** (22 categories). | See Section 1.5 below for all 22 official categories, including **Category 19: Computer science, information and communication technology**. |
| **Rule 1.6** | Use a word that is not approved in the dictionary, only when it is a technical noun or part of a technical noun. | For example, `base` is unapproved as a standalone noun (use `BOTTOM` or `FOUNDATION`), but it is permitted inside the multi-word Technical Noun `base plate` or `database`. |
| **Rule 1.7** | Do not use words that are technical nouns as verbs. | Never verbify a Technical Noun. Write `Apply grease to the fitting` (not `Grease the fitting`), `Make a backup file` (not `Backup the file`), and `Send an e-mail` (not `E-mail the user`). |
| **Rule 1.8** | Use technical nouns that are approved in your company, industry, or subject field. | Use official names from standards, API schemas, UI labels, and system manifests (`ReplicaSet`, `OAuth token`, `webhook`). |
| **Rule 1.9** | When you must select a technical noun, use one which is short and easy to understand. | Prefer concise, self-explanatory domain terms over ornate synonyms. |
| **Rule 1.10** | Do not use regional, slang, or jargon words as technical nouns. | Do not write colloquial expressions such as `brick the router`, `nuke the cache`, or `spin up a box`. |
| **Rule 1.11** | Do not use different technical nouns for the same item. | Maintain 1:1 terminology consistency. Do not alternate between `configuration file`, `config file`, and `settings manifest` for the same artifact. |
| **Rule 1.12** | You can use verbs that you can include in a **technical verb category** (4 categories). | See Section 1.12 below for all 4 official categories, including **Category 2: Computer processes and applications** (`click`, `delete`, `disable`, `enable`, `encrypt`, `install`, `reboot`, `update`, `validate`, etc.). |
| **Rule 1.13** | Do not use technical verbs as nouns. | Note: The past participle form of a technical verb can be used as an adjective (`an encrypted file`, `the installed package`). Do not use a TV as a noun (`the install failed` -> `the installation failed` or `the installer failed`). |
| **Rule 1.14** | Use **American English** spelling unless other official directives tell you differently. | Write `color`, `center`, `aluminum`, `liter`, `meter`, `program`, `initialize`, `analyze`. Exception (Rule 8.6): keep original British spelling inside unchanged quoted text or proper nouns (`"Ministry of Defence"`). |

### Official Rule 1.5 Technical Noun Categories (22 Categories)
1. **Parts, components, equipment, and systems** (`actuator`, `adapter`, `antenna`, `axle`, `bearing`, `bracket`, `cable`, `circuit breaker`, `connector`, `display`, `diode`, `filter`, `fuse`, `gasket`, `gear`, `generator`, `harness`, `hose`, `housing`, `manifold`, `motor`, `nozzle`, `panel`, `pipe`, `piston`, `plug`, `pump`, `relay`, `resistor`, `rotor`, `screen`, `seal`, `sensor`, `shaft`, `Simulate`, `spring`, `switch`, `terminal`, `transformer`, `transistor`, `tube`, `valve`, `wire`)
2. **Tools and support equipment** (`adapter`, `allen key`, `bar`, `brush`, `caliper`, `clamp`, `container`, `crane`, `cutter`, `drill`, `extinguisher`, `gauge`, `goggles`, `grinder`, `hammer`, `hoist`, `jack`, `ladder`, `lathe`, `mask`, `micrometer`, `multimeter`, `oscilloscope`, `pliers`, `press`, `puller`, `punch`, `rack`, `saw`, `scale`, `scissors`, `screwdriver`, `sling`, `spanner`, `stand`, `syringe`, `tape`, `tester`, `thermometer`, `torch`, `trolley`, `vise`, `voltmeter`, `wrench`)
3. **Materials, consumables, and substances** (`acetylene`, `acid`, `adhesive`, `alcohol`, `alloy`, `aluminum`, `ammonia`, `argon`, `asbestos`, `carbon`, `Cardboard`, `cement`, `ceramic`, `chlorine`, `chromium`, `cloth`, `coating`, `compound`, `concrete`, `copper`, `cotton`, `detergent`, `diesel`, `electrolyte`, `enamel`, `epoxy`, `ether`, `fabric`, `felt`, `fiberglass`, `film`, `foam`, `foil`, `freon`, `fuel`, `gas`, `gasoline`, `glass`, `glue`, `gold`, `graphite`, `grease`, `helium`, `hydraulic fluid`, `hydrogen`, `ink`, `insulation`, `iron`, `isopropyl alcohol`, `kerosene`, `lacquer`, `lead`, `leather`, `lubricant`, `magnesium`, `mercury`, `metal`, `methanol`, `mica`, `molybdenum`, `nickel`, `nitrogen`, `nylon`, `oil`, `oxygen`, `paint`, `paper`, `paraffin`, `paste`, `petroleum`, `plastic`, `platinum`, `plywood`, `polyester`, `polyethylene`, `polyurethane`, `porcelain`, `powder`, `primer`, `propane`, `putty`, `quartz`, `resin`, `rubber`, `rust`, `sand`, `sealant`, `silicon`, `silicone`, `silver`, `soap`, `solder`, `solvent`, `steel`, `stone`, `sulfur`, `synthetic rubber`, `tape`, `tar`, `teflon`, `thinner`, `tin`, `titanium`, `toluene`, `tungsten`, `uranium`, `varnish`, `vinyl`, `primer`, `water`, `wax`, `wood`, `wool`, `zinc`)
4. **Facilities, infrastructure, and locations** (`airport`, `aisle`, `apron`, `bay`, `bridge`, `building`, `bunker`, `cabin`, `canal`, `cockpit`, `compartment`, `corridor`, `craneway`, `customs`, `dam`, `deck`, `depot`, `dock`, `doorway`, `elevator`, `entrance`, `exit`, `factory`, `fence`, `floor`, `foundry`, `garage`, `gate`, `hangar`, `harbor`, `headquarters`, `helipad`, `highway`, `hospital`, `hotel`, `jetty`, `laboratory`, `landing`, `library`, `lighthouse`, `lobby`, `lock`, `lounge`, `mine`, `office`, `parking`, `passage`, `pier`, `pipeline`, `plant`, `platform`, `plaza`, `port`, `power plant`, `quarry`, `quay`, `railroad`, `railway`, `ramp`, `refinery`, `reservoir`, `restaurant`, `road`, `roof`, `room`, `runway`, `school`, `shipyard`, `shop`, `sidewalk`, `silo`, `staircase`, `stairs`, `station`, `storage`, `store`, `Warehouse`, `street`, `substation`, `subway`, `taxiway`, `terminal`, `theater`, `tower`, `track`, `tunnel`, `university`, `vault`, `viaduct`, `wall`, `warehouse`, `wharf`, `window`, `workshop`, `yard`)
5. **Vehicles, machines, and transport** (`aircraft`, `airplane`, `ambulance`, `automobile`, `barge`, `bicycle`, `boat`, `bus`, `car`, `cargo aircraft`, `carriage`, `cart`, `catamaran`, `chopper`, `coach`, `combine`, `convertiplane`, `conveyor`, `craft`, `crane`, `cruiser`, `destroyer`, `dirigible`, `dredger`, `drone`, `dump truck`, `earthmover`, `excavator`, `ferry`, `fighter`, `Fire truck`, `forklift`, `freighter`, `frigate`, `glider`, `gondola`, `helicopter`, `hovercraft`, `icebreaker`, `jet`, `launch`, `lifeboat`, `lighter`, `limousine`, `liner`, `locomotive`, `lorry`, `minibus`, `monorail`, `moped`, `motorbike`, `motorcycle`, `motorhome`, `oil tanker`, `omnibus`, `parachute`, `patrol boat`, `pickup`, `plane`, `pontoon`, `pram`, `raft`, `railcar`, `rocket`, `sailboat`, `satellite`, `scooter`, `seaplane`, `sedan`, `semi-trailer`, `ship`, `shuttle`, `sidecar`, `skiff`, `sled`, `sledge`, `sleigh`, `snowmobile`, `spacecraft`, `spaceship`, `speedboat`, `station wagon`, `steamboat`, `steamship`, `streetcar`, `submarine`, `submersible`, `subway train`, `supertanker`, `tank`, `tanker`, `taxi`, `taxicab`, `tender`, `tractor`, `trailer`, `train`, `tram`, `tramcar`, `transport`, `trawler`, `tricycle`, `trolley`, `trolleybus`, `truck`, `tug`, `tugboat`, `van`, `vessel`, `wagon`, `warship`, `watercraft`, `wheelbarrow`, `wheelchair`, `yacht`, `zeppelin`)
6. **Named parts of items, shapes, and geometric terms** (`angle`, `arc`, `axis`, `bevel`, `bore`, `centerline`, `chamfer`, `chord`, `circle`, `circumference`, `cone`, `contour`, `corner`, `cross-section`, `cube`, `curve`, `cylinder`, `diagonal`, `diameter`, `dome`, `ellipse`, `face`, `fillet`, `flange`, `grid`, `groove`, `helix`, `hemisphere`, `hexagon`, `hole`, `hypotenuse`, `intersection`, `lobe`, `loop`, `margin`, `mesh`, `notch`, `octagon`, `oval`, `parabola`, `parallelogram`, `perimeter`, `perpendicular`, `plane`, `polygon`, `prism`, `profile`, `pyramid`, `quadrant`, `radius`, `rectangle`, `rib`, `ridge`, `rim`, `ring`, `sector`, `segment`, `semicircle`, `slot`, `sphere`, `spiral`, `spline`, `square`, `strip`, `surface`, `symmetry`, `tangent`, `taper`, `thread`, `triangle`, `vertex`, `void`, `wedge`, `zig-zag`)
7. **Units of measurement and time** (`ampere`, `angstrom`, `atmosphere`, `bar`, `becquerel`, `bit`, `byte`, `calorie`, `candela`, `carat`, `centimeter`, `century`, `coulomb`, `cubic centimeter`, `cubic foot`, `cubic inch`, `cubic meter`, `cubic yard`, `curie`, `day`, `decibel`, `decade`, `degree`, `degree Celsius`, `degree Fahrenheit`, `degree Kelvin`, `dyne`, `electronvolt`, `erg`, `farad`, `fathom`, `fluid ounce`, `foot`, `foot-pound`, `furlong`, `gallon`, `gauss`, `gigabyte`, `gigahertz`, `gilbert`, `grain`, `gram`, `gray`, `hectare`, `hectopascal`, `henry`, `hertz`, `horsepower`, `hour`, `hundredweight`, `inch`, `joule`, `karat`, `kelvin`, `kilobit`, `kilobyte`, `kilocalorie`, `kilogram`, `kilohertz`, `kilometer`, `kilopascal`, `kilovolt`, `kilowatt`, `kilowatt-hour`, `knot`, `league`, `light-year`, `liter`, `lumen`, `lux`, `maxwell`, `megabit`, `megabyte`, `megahertz`, `megawatt`, `meter`, `microampere`, `microfarad`, `microgram`, `microhenry`, `micrometer`, `micron`, `microsecond`, `microvolt`, `microwatt`, `mil`, `mile`, `milliampere`, `millibar`, `milligram`, `millihenry`, `milliliter`, `millimeter`, `millisecond`, `millivolt`, `milliwatt`, `minute`, `mole`, `month`, `nanometer`, `nanosecond`, `nautical mile`, `newton`, `newton-meter`, `oersted`, `ohm`, `ounce`, `parsec`, `pascal`, `peck`, `pennyweight`, `picofarad`, `picosecond`, `pint`, `poise`, `pound`, `pound-foot`, `pound-inch`, `quart`, `rad`, `radian`, `rem`, `revolution`, `roentgen`, `second`, `siemens`, `sievert`, `slug`, `square centimeter`, `square foot`, `square inch`, `square kilometer`, `square meter`, `square mile`, `square millimeter`, `square yard`, `steradian`, `stokes`, `stone`, `tablespoon`, `teaspoon`, `terabyte`, `tesla`, `therm`, `ton`, `tonne`, `torr`, `volt`, `volt-ampere`, `watt`, `watt-hour`, `weber`, `week`, `yard`, `year`)
8. **Numbers and mathematical, scientific, and engineering terms** (`acceleration`, `addition`, `algebra`, `algorithm`, `amplitude`, `average`, `azimuth`, `binary`, `calculus`, `capacitance`, `centroid`, `coefficient`, `compliance`, `compression`, `concentration`, `conductance`, `conductivity`, `constant`, `coordinate`, `correlation`, `cosine`, `current`, `cycle`, `damping`, `data`, `decimal`, `declination`, `decrement`, `deflection`, `density`, `derivative`, `deviation`, `differential`, `diffusion`, `dimension`, `dipole`, `direct current`, `displacement`, `distribution`, `dividend`, `division`, `divisor`, `drag`, `ductility`, `duration`, `dynamics`, `eccentricity`, `efficiency`, `elasticity`, `electricity`, `electromagnetism`, `electron`, `element`, `elevation`, `elongation`, `emission`, `emissivity`, `energy`, `enthalpy`, `entropy`, `equation`, `equilibrium`, `erosion`, `error`, `evaporation`, `exponent`, `factor`, `fatigue`, `fission`, `flammability`, `flexibility`, `flow`, `flux`, `force`, `formula`, `fraction`, `frequency`, `friction`, `fusion`, `gain`, `gradient`, `gravity`, `hardness`, `harmonics`, `heat`, `humidity`, `hydraulics`, `hydrodynamics`, `hydrostatics`, `hysteresis`, `impedance`, `impulse`, `inclination`, `increment`, `inductance`, `induction`, `inertia`, `infinity`, `insolation`, `integer`, `integral`, `intensity`, `interference`, `interpolation`, `ion`, `ionization`, `isotope`, `kinematics`, `kinetics`, `kurtosis`, `latitude`, `lift`, `limit`, `linearity`, `logarithm`, `logic`, `longitude`, `luminance`, `luminescence`, `mach`, `magnetism`, `magnitude`, `mass`, `matrix`, `maximum`, `mean`, `mechanics`, `median`, `minimum`, `mode`, `modulation`, `modulus`, `moment`, `momentum`, `multiplication`, `multiplier`, `neutron`, `noise`, `norm`, `nucleus`, `number`, `numerator`, `nutrition`, `octave`, `offset`, `opacity`, `optics`, `orbit`, `ordinate`, `oscillation`, `osmosis`, `output`, `oxidation`, `parameter`, `parity`, `particle`, `pendulum`, `percentage`, `period`, `permeability`, `permittivity`, `phase`, `phenomenon`, `photon`, `physics`, `pitch`, `pixel`, `plasma`, `plasticity`, `polarity`, `polarization`, `polynomial`, `porosity`, `potential`, `power`, `precession`, `precision`, `pressure`, `probability`, `product`, `progression`, `projection`, `proportion`, `proton`, `pulse`, `quantity`, `quantum`, `quotient`, `radiation`, `radioactivity`, `range`, `rate`, `ratio`, `reactance`, `reaction`, `refraction`, `relativity`, `reluctance`, `remainder`, `resistance`, `resistivity`, `resolution`, `resonance`, `resultant`, `reverberation`, `rigidity`, `rms`, `roll`, `root`, `rotation`, `salinity`, `saturation`, `scalar`, `scale`, `scattering`, `sequence`, `series`, `shear`, `shock`, `signal`, `sine`, `skewness`, `slope`, `solubility`, `solution`, `sonics`, `sound`, `specific gravity`, `specific heat`, `spectrum`, `speed`, `spin`, `stability`, `standard deviation`, `statics`, `statistics`, `stiffness`, `stoichiometry`, `strain`, `stress`, `sublimation`, `subtraction`, `sum`, `superconductivity`, `susceptance`, `susceptibility`, `symmetry`, `synchronization`, `tangent`, `temperature`, `tension`, `tensor`, `theorem`, `thermodynamics`, `thrust`, `time`, `tolerance`, `torque`, `torsion`, `trajectory`, `transconductance`, `transfer`, `transformation`, `transient`, `transmission`, `transmittance`, `trigonometry`, `turbulence`, ` ultrasonic`, `vacuum`, `valence`, `value`, `vapor`, `vaporization`, `variable`, `variance`, `variation`, `vector`, `velocity`, `vibration`, `viscosity`, `volatility`, `voltage`, `volume`, `vortex`, `wake`, `wave`, `waveform`, `wavelength`, `weight`, `work`, `yaw`, `yield`, `zero`)
9. **Medical, anatomical, and physiological terms**
10. **Geographical, meteorological, and environmental terms**
11. **Official documents, publications, and regulations** (`manual`, `specification`, `logbook`, `checklist`, `bulletin`, `directive`, `certificate`, `license`)
12. **Processes, states, and conditions** (`corrosion`, `contamination`, `decompression`, `delamination`, `distortion`, `erosion`, `evaporation`, `ignition`, `installation`, `lubrication`, `maintenance`, `operation`, `oxidation`, `polarization`, `pressurization`, `rotation`, `turbulence`, `vibration`)
13. **People, roles, and organizations** (`administrator`, `analyst`, `architect`, `auditor`, `author`, `captain`, `client`, `commander`, `committee`, `company`, `contractor`, `controller`, `crew`, `customer`, `department`, `developer`, `director`, `diver`, `doctor`, `driver`, `electrician`, `engineer`, `firefighter`, `inspector`, `instructor`, `manager`, `manufacturer`, `mechanic`, `nurse`, `officer`, `operator`, `organization`, `owner`, `passenger`, `personnel`, `pilot`, `plumber`, `police`, `programmer`, `public`, `rescue team`, `scientist`, `security`, `specialist`, `staff`, `student`, `supervisor`, `supplier`, `surgeon`, `surveyor`, `team`, `technician`, `user`, `vendor`, `visitor`, `welder`, `worker`)
14. **Indicators, placards, and UI/panel inscriptions**
15. **Abbreviations, acronyms, and alphanumeric identifiers**
16. **Directional and positional terms** (`clockwise`, `counterclockwise`, `inboard`, `outboard`, `midship`, `starboard`, `port`, `upwind`, `downwind`)
17. **Colors** (`amber`, `beige`, `black`, `blue`, `bronze`, `brown`, `chrome`, `copper`, `crimson`, `cyan`, `gold`, `gray`, `green`, `indigo`, `ivory`, `khaki`, `lavender`, `magenta`, `maroon`, `navy`, `ochre`, `olive`, `orange`, `pink`, `purple`, `red`, `scarlet`, `silver`, `tan`, `teal`, `turquoise`, `violet`, `white`, `yellow` — *Note: Colors are Technical Nouns in Issue 9 and do not have comparative or superlative forms like `redder` or `reddest`.*)
18. **Packaging, logistics, and transport containers**
19. **Computer science, information and communication technology (ICT)** — *Official Issue 9 list*:
    `add-in`, `add-on`, `AI`, `arrow`, `artificial intelligence`, `authentication`, `backup`, `backup file`, `bookmark`, `chatbot`, `content`, `cursor`, `cybersecurity`, `database`, `deep learning`, `dialog check box`, `digitalization`, `digitization`, `e-mail`, `embedding`, `field`, `file`, `firewall`, `hallucination`, `HTML`, `icon`, `interface`, `internet`, `laptop`, `large language model`, `local operation`, `machine learning`, `memory`, `menu`, `metadata`, `mouse`, `network`, `operating system`, `phone`, `plug-in`, `pre-loaded software`, `preset value`, `prompt engineering`, `remote operation`, `screen`, `search engine`, `smartphone`, `status bar`, `store`, `tablet`, `token`, `toolbar`, `touchscreen`, `tweet`, `tuning`, `update`, `voice mail`, `XML`
20. **Audio, video, photography, and media**
21. **Law and regulations**
22. **Animals, plants, and other life forms**

### Official Rule 1.12 Technical Verb Categories (4 Categories)
1. **Manufacturing processes** (`1a` Machining/cutting: `bore, chamfer, countersink, drill, grind, hone, lathe, mill, polish, ream, rout, saw, shear, tap, thread, trim, turn`; `1b` Joining/fastening: `bond, braze,bolt, cement, clamp, crimp, glue, lockwire, nail, pin, rivet, screw, seal, solder, Splice, staple, stitch, tack, tape, torque, weld`; `1c` Forming/shaping: `bend, cast, coin, extrude, forge, form, mold, press, roll, stamp, swage`; `1d` Surface/heat treatment: `anneal, anodize, buff, cadmium-plate, case-harden, chrome-plate, coat, electroplate, etch, galvanize, harden, heat-treat, normalize, oxidize, passivate, pickle, plate, prime, quench, sandblast, shot-peen, temper, varnish`; `1e` Chemical/cleaning: `degrease, demineralize, distill, filter, flush, neutralize, purge, rinse, sanitize, scrub, sterilize, wash`; `1f` Inspection/testing: `calibrate, Eddy-current test, magnaflux, radiographically inspect, ultrasonic-test, X-ray`)
2. **Computer processes and applications** — *Official Issue 9 list*:
   * **2a. Input/output processes**: `click`, `digitize`, `enter`, `press`, `print`, `swipe`, `tap`, `type`
   * **2b. User-interface and application processes**: `clear`, `close`, `copy`, `cut`, `delete`, `deselect`, `disable`, `drag`, `drag and drop`, `enable`, `encrypt`, `erase`, `filter`, `highlight`, `invalidate`, `maximize`, `minimize`, `navigate`, `open`, `paste`, `save`, `scroll`, `sort`, `store`, `tweet`, `validate`, `zoom in`, `zoom out`
   * **2c. System operations**: `abort`, `boot`, `communicate`, `debug`, `download`, `format`, `install`, `load`, `manage`, `process`, `reboot`, `update`, `upgrade`, `upload`
3. **Subject fields** (`3a` Electricity & electronics; `3b` Aviation, marine & automotive; `3c` Hydraulics & pneumatics; `3d` Optics & photography; `3e` Medicine & first aid; `3f` Logistics & packaging)
4. **Law and regulations** (`certify`, `comply`, `copyright`, `enforce`, `infringe`, `legislate`, `license`, `patent`, `prohibit`, `ratify`, `regulate`, `revoke`, `sanction`, `subpoena`)

---

## Section 2: Multi-Word Nouns (Rules 2.1–2.2)

* **Rule 2.1**: **Write multi-word nouns of no more than three words.**
  * *Non-STE (4 words)*: `runway light circuit calibration`
  * *STE*: `the calibration of the runway light circuit`
  * *Non-STE (5 words)*: `database connection pool timeout value`
  * *STE*: `the timeout value for the database connection pool`
* **Rule 2.2**: **When a technical noun has more than three words, write it in full, then either give a shorter form or use hyphens (`-`) between words that are used as one unit.**
  * Do not connect groups of more than three words with hyphens.
  * *Shortened form pattern*: `The Content Delivery Network Edge Cache (referred to as the Edge Cache) stores static assets.`
  * *Hyphenated unit pattern*: `the forward-passenger-door lock` (the 3-word hyphenated modifier counts as 1 word under Rule 8.7).

---

## Section 3: Verbs (Rules 3.1–3.7)

* **Rule 3.1**: **Use only the verb forms given in the dictionary.**
* **Rule 3.2**: **Use only these 6 verb forms/tenses**:
  1. **Infinitive**: `to start`, `to connect`
  2. **Imperative**: `Start the service.`, `Do not delete the key.`
  3. **Simple present**: `The service starts.`, `The worker processes the queue.`
  4. **Simple past**: `The service started.`, `The request failed.`
  5. **Simple future**: `The service will start.`
  6. **Past participle (strictly as an adjective)**: `the connected client`, `the encrypted token`
* **Rule 3.3**: **Use the past participle form only as an adjective.**
  * You can place the past participle before a noun (`the damaged cable`, `the installed certificate`) or after the verbs `to be`, `to become`, or `to stay` to describe a state or condition (`The cable is damaged`, `The port stays closed`).
* **Rule 3.4**: **Do not use auxiliary verbs to make complex verb constructions.**
  * Forbidden: progressive/continuous (`is running`, `was starting`), present/past perfect (`has completed`, `had failed`), passive modal chains (`should have been restarted`, `could be configured`).
* **Rule 3.5**: **Use the `-ing` form of a verb only as a technical noun or as a modifier in a technical noun.**
  * Never use an `-ing` form as a progressive verb (`The pod is restarting`), a participial clause (`Using the CLI, deploy the app`), or a gerund phrase (`Before starting the server...` -> `Before you start the server...`).
  * Only **9 `-ing` words** are approved in the core Issue 9 dictionary:
    * **Nouns (4)**: `LIGHTING`, `OPENING`, `ROUTING`, `SERVICING`
    * **Adjectives (3)**: `MATING`, `MISSING`, `REMAINING`
    * **Pronoun (1)**: `SOMETHING`
    * **Preposition (1)**: `DURING`
  * Other `-ing` words are valid **only** when part of an approved Technical Noun (`cooling fan`, `operating system`, `machine learning`, `prompt engineering`, `landing gear`).
* **Rule 3.6**: **Use the active voice.**
  * In procedural writing, always use active voice (imperative commands or active conditions: `If you find an error, stop the job`).
  * In descriptive writing, always use active voice (`The load balancer routes the traffic`). You can use passive voice in descriptive writing **only** when the agent is genuinely unknown (or use `something` as the active subject: `If something damages the seal...`).
* **Rule 3.7**: **Use an approved verb to describe an action, not a noun or other parts of speech.**
  * Avoid nominalizations (`smell of fuel` / `make an adjustment to` / `do a comparison of`).
  * *Non-STE*: `Prior to installation of the package, perform a validation of the checksum.`
  * *STE*: `Before you install the package, validate the checksum.` (Note: when the noun itself is the only approved STE form, such as `DO A TEST OF` or `DO A CHECK OF`, that construction is required by Rule 1.2).

---

## Section 4: Sentences (Rules 4.1–4.5)

* **Rule 4.1**: **Write short and clear sentences.**
* **Rule 4.2**: **Do not omit words or use contractions to make your sentences shorter.**
  * Never omit nouns, verbs, subjects, or articles (`Check log` -> `Examine the log file`; `If corrupt, delete` -> `If the file is damaged, delete it`).
  * Never use contractions (`don't` -> `do not`, `isn't` -> `is not`, `aren't` -> `are not`, `can't` -> `cannot`, `won't` -> `will not`, `it's` -> `it is`).
* **Rule 4.3**: **Use a vertical list for complex texts.**
  * End the introductory lead-in clause with a colon (`:`).
  * Start each list item with an uppercase letter.
  * If list items are complete sentences, end each item with a period (`.`).
  * If list items are sentence fragments (not complete sentences), put **no punctuation** (no comma, no semicolon, no period, no `and`/`or`) at the end of items before the last item, and put a **period (`.`) at the end of the last item**.
  * In a vertical list of negative commands or safety prohibitions, repeat `Do not` or `DO NOT` at the start of every single list item.
* **Rule 4.4**: **Use connecting words and connecting phrases to connect sentences with related topics.**
  * Approved connecting words: `AND`, `BUT`, `THEN`, `THUS`.
  * Approved connecting phrases: `AS A RESULT`, `AT THE SAME TIME`.
* **Rule 4.5**: **When applicable, use an article (`the`, `a`, `an`) or a demonstrative adjective (`this`, `these`) before a noun or multi-word noun.**
  * **Exception**: Do **not** use `the` before a noun that is followed by an alphanumeric identifier:
    * *STE*: `Open circuit breaker 36L7.` / `Refer to Figure 2.` / `Connect pin A1 to terminal B4.`
    * *Non-STE*: `Open the circuit breaker 36L7.`

---

## Section 5: Procedural Writing (Rules 5.1–5.5)

* **Rule 5.1**: **Write short sentences. Give a maximum of 20 words in each sentence.**
  * Applies to all procedural instructions, steps, and safety instructions (`WARNING` and `CAUTION`).
* **Rule 5.2**: **Write only one instruction in each sentence unless two or more actions occur at the same time.**
  * *Sequential actions (split into two sentences or steps)*:
    * *Non-STE*: `Stop the worker process and delete the temporary directory.`
    * *STE*: `1. Stop the worker process.` / `2. Delete the temporary directory.`
  * *Simultaneous actions (connect with `and` or `at the same time`)*:
    * *STE*: `Hold the reset button and connect the power cable.`
* **Rule 5.3**: **Write instructions in the imperative (command) form.**
  * Never put `must` or `you must` before an imperative instruction (`You must restart the daemon` -> `Restart the daemon`).
  * Never use passive instructions (`The token is entered in the prompt` -> `Enter the token in the prompt`).
* **Rule 5.4**: **If an instruction has a descriptive condition, start the instruction with the condition.**
  * Always place a **comma (`,`)** between the condition and the imperative command:
    * *STE*: `If the health check fails, restart the container.`
    * *STE*: `When the status bar shows 100%, close the window.`
* **Rule 5.5**: **Write notes only to give information, not instructions.**
  * A `NOTE` must **never** contain imperative verbs, safety hazards, or work-step tolerances/limits.
  * Notes follow descriptive writing rules (maximum **25 words** per sentence).
  * *Non-STE*: `NOTE: Make sure that you save the key before you close the dialog.`
  * *STE (as a procedural step)*: `Save the key before you close the dialog.`
  * *STE (as an informational note)*: `NOTE: The system encrypts the key automatically with AES-256.`

---

## Section 6: Descriptive Writing (Rules 6.1–6.6)

* **Rule 6.1**: **Give information gradually.**
  * Do not use imperative verbs in descriptive text. Present one idea per sentence, progressing from general context to specific details.
* **Rule 6.2**: **Use key words and key phrases to give your text a logical structure.**
  * Repeat key terms across adjacent sentences to link cause, effect, and component relationships clearly.
* **Rule 6.3**: **Write short sentences. Give a maximum of 25 words in each sentence.**
* **Rule 6.4**: **Use paragraphs to show related information.**
  * Start each paragraph with a clear **topic sentence** that states what the paragraph is about.
* **Rule 6.5**: **Make sure that each paragraph has only one topic.**
* **Rule 6.6**: **Make sure that no paragraph has more than six sentences.**

---

## Section 7: Safety Instructions (Rules 7.1–7.3)

* **Rule 7.1**: **Use an applicable word (`WARNING` or `CAUTION`) to identify the level of risk.**
  * **`WARNING`**: Related to materials, processes, or procedures that can cause **injury or death** to persons.
  * **`CAUTION`**: Related to materials, processes, or procedures that can cause **damage to objects, equipment, systems, or data**.
  * Place the safety instruction immediately **before** the step or procedure to which it applies.
  * All sentences in a `WARNING` or `CAUTION` must obey the **20-word procedural sentence limit** (Rule 5.1).
* **Rule 7.2**: **Start a safety instruction with a clear and accurate command or condition.**
  * Do not use vague commands such as `Be careful` or `Take care`. Give the exact action to do or not to do.
* **Rule 7.3**: **Give an explanation to show the risk or possible result.**
  * *STE Warning*: `WARNING: DO NOT TOUCH THE POWER TERMINALS WHEN THE UNIT IS ENERGIZED. HIGH VOLTAGE CAN CAUSE INJURY OR DEATH.`
  * *STE Caution*: `CAUTION: DO NOT DELETE THE STATE FILE WHILE THE CLUSTER IS ACTIVE. THIS CAN CAUSE DATA CORRUPTION.`

---

## Section 8: Punctuation and Word Count (Rules 8.1–8.7)

* **Rule 8.1**: **You can use all standard English punctuation marks except the semicolon (`;`).**
  * Never use a semicolon (`;`) in prose. Replace it with a period (`.`) or a conjunction (`and`, `but`).
* **Rule 8.2**: **Use hyphens (`-`) to connect words that are directly related.**
  * Use hyphens for prefixes (`de-energize`, `anti-icing`, `non-metallic`, `pre-loaded`, `re-install`, `self-locking`), fractions (`two-thirds`), compound modifiers before a noun (`high-pressure valve`, `read-only volume`), and multi-word modifiers up to three words (`soap-and-water solution`).
* **Rule 8.3**: **There are seven permitted uses of parentheses `()`**:
  1. To identify an abbreviation or shortened name after the full term (`Content Delivery Network (CDN)`).
  2. To give a reference (`(Refer to Figure 3.)`).
  3. To show an alternative unit of measurement (`20 kg (44 lb)`).
  4. To identify tool or part numbers (`disconnect the connector (P104)`).
  5. To give a callout or item identifier from an illustration (`remove the bolt (3)`).
  6. To clarify plural option in a heading or table (`Defect(s)`).
  7. To give a short supplementary explanation (`The valve closes automatically (by spring force).`).
  * Never nest parentheses `((...))`.
* **Rule 8.4**: **In a vertical list, a colon (`:`) has the same effect on word count as a period.**
  * The lead-in clause ending with `:` is counted as one independent sentence (max 20 words in procedures, max 25 words in descriptions). Each vertical list item is counted as its own separate sentence.
* **Rule 8.5**: **Count text in parentheses as one word.**
  * Everything inside `(...)` counts as **1 word** in the enclosing sentence.
  * **Crucial**: The text inside the parentheses is **also evaluated as a separate sentence** for STE word-count limits (max 20 words in procedures, max 25 words in descriptions)!
* **Rule 8.6**: **Count each of these 7 elements as one word**:
  1. **Numbers**: `25`, `1,500`, `3.14159`, `3/4`.
  2. **Numbers together with units of measurement**: Both abbreviated and spelled-out units count with their number as **1 word** (`10 °C`, `10 degrees Celsius`, `20 kg`, `20 kilograms`, `500 ms`, `10 a.m.`).
  3. **Abbreviations**: `NASA`, `VPN`, `REST`, `JSON`, `e.g.` (though `e.g.` is forbidden by `GR-6`).
  4. **Alphanumeric identifiers**: `36L7`, `No. 1`, `Fig. 2`, `v2.4.1`, `eth0`.
  5. **Quoted text**: Any unchanged string enclosed in quotation marks (`"Service Overview"`), or a mathematical/chemical formula (`A = B + C`).
  6. **Titles, headings, and text on placards and labels**: Not subject to the 20/25-word sentence limit, and when referenced inline (`the START switch`, `the " Retry " button`), the label counts as **1 word**.
  7. **Proper nouns**: Names of individuals, groups, organizations, and geopolitical entities count as **1 word** (`United States of America`, `George Washington`, `European Union`, `Linux Foundation`).
* **Rule 8.7**: **Count hyphenated words as one word.**
  * Examples: `high-pressure` = 1 word; `soap-and-water` = 1 word; `6-mm` = 1 word.

---

## Section 9: Writing Practices (Rules 9.1–9.4) & General Recommendations (GR-1–GR-8)

### Rules 9.1–9.4
* **Rule 9.1**: **Use a different sentence construction when a word-for-word replacement is not sufficient.**
  * Do not mechanically substitute words into a long, passive sentence. Rebuild the sentence around the actor and action.
* **Rule 9.2**: **Use each approved word correctly.**
  * Verify grammar, part of speech, and word order against the STE dictionary examples.
* **Rule 9.3**: **When you use two words together, do not make phrasal verbs.**
  * Do not combine an approved verb with a preposition/adverb to create an idiomatic phrasal verb (`look for` -> `try to find`; `carry out` -> `do`; `set up` -> `install` / `prepare`; `find out` -> `get data`).
  * Only **3 phrasal verbs** are approved in the Issue 9 dictionary:
    1. **`COME ON (v)`**: For lights or indicators illuminating (`The warning light comes on`).
    2. **`GO OFF (v)`**: For lights or indicators extinguishing (`The warning light goes off`).
    3. **`PUT ON (v)`**: For donning protective clothing or equipment (`Put on the safety goggles`).
* **Rule 9.4**: **Always use a consistent style and wording.**
  * Use identical phrasing for recurring operations across a document or manual.

### General Recommendations (`GR-1` through `GR-8`)
* **`GR-1` (The conjunction `that`)**: Do not omit the conjunction `that` after verbs such as `make sure`, `show`, `recommend`, `indicate` (`Make sure that the port is open`, not `Make sure the port is open`).
* **`GR-2` (Ambiguity with `with`)**: Make sure that prepositional phrases with `with` are unambiguous (`Examine the cracks with a magnifying glass` vs. `Examine the pipes that have cracks`).
* **`GR-3` (Pronouns)**: Only the pronouns `IT`, `ITS`, `THEY`, `THEIR`, `THEM`, `YOU`, `YOUR`, `THIS`, `THESE`, `SOMETHING`, `ONE`, `ALL`, `NONE`, `OTHER`, `WHICH`, `WHO`, `THAT` are approved. Never use `I`, `we`, `our`, `us`, `he`, `him`, `his`, `she`, `her`, `hers`, `myself`, `itself`, `themselves`. Replace `it` or `they` with the explicit noun whenever more than one antecedent is possible.
* **`GR-4` (The pronoun `this`)**: Avoid standalone `this` when it refers vaguely to an entire preceding clause unless the meaning is unmistakable (`This can cause damage`). Prefer `this <noun>` (`this condition`, `this procedure`, `this value`).
* **`GR-5` (False friends)**: Guard against words that have different meanings in other languages (e.g., `disposition`, `control`, `eventual`, `actual`).
* **`GR-6` (Latin abbreviations)**: **Never** use Latin abbreviations (`e.g.`, `i.e.`, `etc.`, `viz.`, `cf.`, `et al.`). Use `FOR EXAMPLE`, `THAT IS`, or list the exact items.
* **`GR-7` (Inclusive language)**: Always use gender-neutral, inclusive language. Words such as `he`, `she`, `man`, `men`, `woman`, `women`, `workman`, `manpower`, `man-hour` are not permitted in STE (use `PERSON`, `PERSONNEL`, `OPERATOR`, `TECHNICIAN`, `USER`, `WORK HOUR`).
* **`GR-8` (Possessive form `'s`)**: Avoid the `'s` Saxon genitive on inanimate objects (`the server's configuration` -> `the configuration of the server` or `the server configuration`).
