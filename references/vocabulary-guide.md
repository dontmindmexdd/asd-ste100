# ASD-STE100 Issue 9 Vocabulary & Substitution Guide

This guide provides quick-reference tables extracted directly from **Part 2 (Dictionary) of ASD-STE100 Issue 9 (2025-01-15)**. For programmatic lookup across all 2,198 dictionary entries (879 approved entries and 1,319 unapproved entries), consult [ste-issue9-dictionary.json](../resources/ste-issue9-dictionary.json) and [unapproved-words.json](../resources/unapproved-words.json).

---

## 1. Official Issue 9 "List of Recurring Errors" (Pages 2-0-17 to 2-0-18)

The ASD-STE100 Issue 9 specification highlights these **39 most frequently recurring errors** made by technical writers:

| Non-STE Word (POS) | Official STE Approved Replacement | Notes & Example |
| :--- | :--- | :--- |
| `acceptable (adj)` | **`PERMITTED (adj)`** (or `SATISFACTORY (adj)`, `SERVICEABLE (adj)`) | `A latency value of 20 ms is permitted.` |
| `alternate (adj)` | **`ALTERNATIVE (adj)`** | `Use an alternative route.` |
| `any (adj)` | **None** or a different sentence construction (or `ALL (adj)`, `A/AN`) | `Repair all damaged files.` (not `any damaged files`) |
| `avoid (v)` | **`PREVENT (v)`** (or `DO NOT`) | `To prevent data loss, make a backup file.` |
| `both (adj)` | **`THE TWO (TN)`** (or `EACH (adj)`) | `Connect the two cables.` |
| `check (v)` | **`CHECK (n)`** (or `MAKE SURE (v)`, `EXAMINE (v)`, `MEASURE (v)`) | `CHECK` is approved **only as a noun** (`Do a check of the log`). |
| `cover (v)` | **`COVER (TN)`** (`PUT A COVER ON`) | `COVER` is a Technical Noun, not an approved verb. |
| `complete (adj)` | **`COMPLETED (adj)`** (or `FULL (adj)`, `ALL (adj)`) | `COMPLETE` is an approved **verb** (`Complete the test`); use `COMPLETED`, `FULL`, or `ALL` as an adjective. |
| `damage (v)` | **`DAMAGE (n)`** (`CAUSE DAMAGE TO`, `DAMAGED (adj)`) | `DAMAGE` is an approved **noun**, and `DAMAGED` is an approved **adjective**. |
| `ensure (v)` | **`MAKE SURE (v)`** | Always follow with `that`: `Make sure that the port is open.` |
| `fit (v)` | **`INSTALL (v)`** (or `ATTACH (v)`) | `Install the adapter in slot 2.` |
| `follow (v)` | **`OBEY (v)`** (or `DO (v)`) | `Obey the safety instructions.` |
| `further (adj)` | **`MORE (adj)`** | `For more data, refer to Section 4.` |
| `further (adv)` | **`MORE (adv)`** (or `FARTHER (adv)`) | `Turn the knob 10 degrees more.` |
| `have to (v)` | **Use an action verb in the imperative form** (or `MUST (v)`) | `Restart the daemon.` (not `You have to restart the daemon.`) |
| `however (adv)` | **`BUT (conj)`** | `The connection succeeded, but the request timed out.` |
| `insert (v)` | **`PUT (v)`** (or `INSTALL (v)`) | `Put the token in the header.` |
| `main (adj)` | **`PRIMARY (adj)`** | `The primary database node processes write operations.` |
| `may (v)` | **`CAN (v)`** | `High load can cause a timeout.` |
| `need (v)` | **`NECESSARY (adj)`** (or `WANT (v)`) | `It is necessary to restart the service.` |
| `now (adv)` | **`AT THIS TIME`** | `Two workers are active at this time.` |
| `old (adj)` | **`REMAINING (adj)`**, **`USED (adj)`**, **`EXPIRED (adj)`** | `Remove the expired certificates.` |
| `over (prep)` | **`ABOVE (prep)`**, **`ON (prep)`**, **`ALONG (prep)`**, **`MORE THAN`** | `The CPU usage is more than 80%.` |
| `people (n)` | **`PERSON (n)`**, **`PERSONNEL (n)`** | `Only approved personnel can get access to the vault.` |
| `perform (v)` | **`DO (v)`** | `Do a check of the checksum.` |
| `portion (n)` | **`PART (n)`** | `Read the first part of the buffer.` |
| `press (v)` | **`PUSH (v)`** | *Exception*: `press` is permitted as a Computer Technical Verb (Rule 1.12 Cat 2a: `Press the ENTER key`). For physical switches/buttons, use `PUSH (v)`. |
| `reach (v)` | **`GET (v)`** (or `COME TO`, `TOUCH (v)`) | `When the temperature gets to 80 °C, the fan starts.` |
| `repeat (v)` | **`DO (v) ... AGAIN`** | `Do steps 1 thru 3 again.` |
| `required (v/adj)` | **`NECESSARY (adj)`** (or `SPECIFIED (adj)`, `MANDATORY (adj)`) | `Make sure that the necessary permissions are active.` |
| `rotate (v)` | **`TURN (v)`** | `Turn the shaft clockwise.` |
| `secure (v)` | **`ATTACH (v)`**, **`SAFETY (v)`** | `Attach the cable to the rack.` |
| `shall (v)` | **`MUST (v)`** (or imperative in procedures) | `The payload must contain a valid signature.` |
| `should (v)` | **`MUST (v)`** (or imperative in procedures) | Never use `should`. Use `MUST` for obligations or imperative for steps. |
| `since (conj)` | **`BECAUSE (conj)`** | `Because the key expired, the handshake failed.` |
| `test (v)` | **`TEST (n)`** (`DO A TEST OF`) | `TEST` is approved **only as a noun** (`Do a test of the endpoint`). |
| `therefore (adv)` | **`THUS (adv)`**, **`AS A RESULT`** | `The queue is full. As a result, the producer waits.` |
| `under (prep)` | **`BELOW (prep)`**, **`IN (prep)`**, **`LESS THAN`** | `Keep the latency less than 50 ms.` |
| `using (v)` | **`USE (v)`**, **`WITH (prep)`** | `Encrypt the file with the KMS key.` (never `using the KMS key`) |

---

## 2. Official Issue 9 List of Approved Verbs (208 Core Verbs)

Only the **208 verbs** below are approved in the core ASD-STE100 Issue 9 dictionary (in addition to domain-specific Technical Verbs permitted under Rule 1.12):

* **A**: `ABSORB`, `ACCEPT`, `ACTIVATE`, `ADAPT`, `ADD`, `ADJUST`, `AGREE`, `ALIGN`, `APPLY`, `ARM`, `ASSEMBLE`, `ATTACH`
* **B**: `BALANCE`, `BE` (`IS`, `ARE`, `WAS`, `WERE`), `BECOME`, `BEND`, `BLEED`, `BLOW`, `BOND`, `BREAK`, `BREATHE`, `BURN`, `BYPASS`
* **C**: `CALCULATE`, `CALIBRATE`, `CAN` (`COULD`), `CANCEL`, `CANNOT`, `CATCH`, `CAUSE`, `CHANGE`, `CHARGE`, `CLEAN`, `CLOSE`, `COLLECT`, `COME`, `COME ON`, `COMPARE`, `COMPLETE`, `COMPRESS`, `CONNECT`, `CONTACT`, `CONTAIN`, `CONTINUE`, `CONTROL`, `CORRECT`, `COUNT`, `CUT`
* **D**: `DE-ENERGIZE`, `DEACTIVATE`, `DECREASE`, `DEFLATE`, `DEFUEL`, `DEPLOY`, `DISARM`, `DISASSEMBLE`, `DISCARD`, `DISCONNECT`, `DISENGAGE`, `DIVIDE`, `DO`, `DRAIN`, `DRINK`, `DRY`
* **E**: `EAT`, `EJECT`, `ENERGIZE`, `ENGAGE`, `ERASE`, `EXAMINE`, `EXPAND`, `EXTEND`, `EXTINGUISH`
* **F**: `FALL`, `FEATHER`, `FEEL`, `FILL`, `FIND`, `FIRE`, `FLASH`, `FLOW`, `FLUSH`, `FOLD`, `FOLLOW` *(for physical tracking only; for rules/procedures use `OBEY`)*, `FREEZE`
* **G**: `GET`, `GIVE`, `GO`, `GO OFF`, `GROUND`
* **H**: `HANG`, `HAVE` (`HAS`, `HAD`), `HEAR`, `HELP`, `HIT`, `HOLD`
* **I**: `IDENTIFY`, `IGNORE`, `ILLUMINATE`, `INCLUDE`, `INCREASE`, `INFLATE`, `INSTALL`, `INTERCHANGE`, `ISOLATE`
* **K–L**: `KEEP`, `KILL`, `KNOW`, `LATCH`, `LET`, `LIFT`, `LISTEN`, `LOCK`, `LOOK`, `LOOSEN`, `LOWER`, `LUBRICATE`
* **M–O**: `MAKE`, `MAKE SURE`, `MEASURE`, `MELT`, `MIX`, `MONITOR`, `MOOR`, `MOVE`, `MULTIPLY`, `MUST`, `OBEY`, `OCCUR`, `OPEN`, `OPERATE`, `OVERRIDE`
* **P–R**: `PAINT`, `PARK`, `POINT`, `POLISH`, `PREPARE`, `PRESSURIZE`, `PREVENT`, `PROTRUDE`, `PULL`, `PUSH`, `PUT`, `PUT ON`, `READ`, `RECEIVE`, `RECOMMEND`, `RECORD`, `RECYCLE`, `REFER`, `REFUEL`, `REJECT`, `RELEASE`, `REMOVE`, `REPAIR`, `REPLACE`, `RETRACT`, `RUB`
* **S**: `SAFETY`, `SCHEDULE`, `SEAL`, `SEE`, `SELECT`, `SEND`, `SENSE`, `SET`, `SHAKE`, `SHOW`, `SIMULATE`, `SMELL`, `SMOKE`, `SOAK`, `SPEAK`, `SPILL`, `SPRAY`, `START`, `STAY`, `STOP`, `STOW`, `SUBTRACT`, `SUPPLY`, `SWALLOW`
* **T–W**: `TAG`, `TAP`, `TELL`, `THINK`, `TIGHTEN`, `TILT`, `TORQUE`, `TOUCH`, `TOW`, `TRANSMIT`, `TRY`, `TUNE`, `TURN`, `TWIST`, `UNFOLD`, `UNLOCK`, `UNWIND`, `USE`, `WAIT`, `WALK`, `WANT`, `WEAR`, `WEIGH`, `WILL`, `WIND`, `WRITE`

---

## 3. High-Risk Part-of-Speech & Meaning Traps (Rules 1.2 & 1.3)

Several everyday technical words are approved in STE **only in one specific part of speech or meaning**:

| Word | Approved POS & Meaning | Unapproved Usage | How to Write in STE |
| :--- | :--- | :--- | :--- |
| **`CHECK`** | **Noun (`CHECK (n)`)**: an examination or verification | Verb (`check (v)`) | `Do a check of the database.` / `Make sure that the database is active.` / `Examine the log.` |
| **`TEST`** | **Noun (`TEST (n)`)**: a procedure to verify operation | Verb (`test (v)`) | `Do a test of the endpoint.` |
| **`COMPLETE`** | **Verb (`COMPLETE (v)`)**: to finish (`COMPLETES, COMPLETED`) | Adjective (`complete (adj)`) | As verb: `Complete the migration.` As adjective, use `COMPLETED (adj)`, `FULL (adj)`, or `ALL (adj)`. |
| **`DAMAGE`** | **Noun (`DAMAGE (n)`)** & **Adjective (`DAMAGED (adj)`)** | Verb (`damage (v)`) | `High voltage can cause damage to the board.` / `Replace the damaged cable.` |
| **`COVER`** | **Technical Noun (`COVER (TN)`)** | Verb (`cover (v)`) | `Put a cover on the sensor.` |
| **`DISPLAY`** | **Technical Noun (`display (TN)`)**: screen/monitor | Verb (`display (v)`) | `The screen shows the error code.` (never `displays the error code`) |
| **`CONTROL`** | **Verb (`CONTROL (v)`)** & **Noun (`CONTROL (n)`)**: command/mechanism | Verb meaning "to check/verify" (False friend `GR-5`) | Use `CONTROL` only for regulating/directing (`The daemon controls the worker pool`). For checking, use `EXAMINE` or `MEASURE`. |
| **`ABOUT`** | **Preposition (`ABOUT (prep)`)**: concerned with | Adverb meaning "approximately" | Approved: `For data about the API, refer to Section 2.` Unapproved: `about 5 seconds` -> `approximately 5 seconds`. |
| **`ABOVE`** | **Preposition (`ABOVE (prep)`)**: physically higher than | Preposition meaning "more than" | Approved: `Install the fan above the heat sink.` Unapproved: `above 80%` -> `more than 80%`. |
| **`UNDER`** | **Preposition (`UNDER`)**: *Unapproved!* | All uses of `under` are unapproved! | Physical position: `BELOW (prep)`. Quantity/limit: `LESS THAN`. Context/grouping: `IN (prep)` or `WITH (prep)`. |
| **`OVER`** | **Preposition (`OVER`)**: *Unapproved!* | All uses of `over` are unapproved! | Physical position: `ABOVE (prep)` or `ON (prep)`. Quantity/limit: `MORE THAN`. Duration: `DURING (prep)`. |
| **`SEE`** | **Verb (`SEE (v)`)**: perceive with the eyes | Cross-reference in a document | Approved: `If you see smoke, stop the test.` Unapproved: `See Section 3` -> `Refer to Section 3`. |
| **`SINCE`** | **Preposition/Conjunction**: *Unapproved!* | Causal ("because") or temporal ("from the time") | Causal: `BECAUSE (conj)`. Temporal: `AFTER (prep/conj)` or `FROM (prep)`. |
| **`WHILE`** | **Conjunction (`WHILE`)**: *Unapproved!* | Temporal ("during the time that") or contrastive ("whereas") | Temporal: `WHEN (conj)` or `DURING (prep)`. Contrastive: `AND (conj)` or `BUT (conj)`. |

---

## 4. Top Unapproved-to-Approved Dictionary Substitutions (A–Z)

| Unapproved Word / Phrase | Approved Issue 9 Replacement | STE Example |
| :--- | :--- | :--- |
| `accomplish (v)` / `achieve (v)` | **`DO (v)`**, **`COMPLETE (v)`**, **`GET (v)`** | `To complete the task, run the script.` |
| `accurate (adj)` | **`CORRECT (adj)`**, **`PRECISE (adj)`** | `Make sure that the timestamp is correct.` |
| `acquire (v)` / `obtain (v)` | **`GET (v)`** | `Get an access token from the server.` |
| `activate (v)` / `deactivate (v)` | **`ACTIVATE (v)`** / **`DEACTIVATE (v)`** *(Approved in Issue 9!)* | `Activate the firewall rule.` |
| `additional (adj)` / `extra (adj)` | **`MORE (adj)`**, **`OTHER (adj)`**, **`SPARE (adj)`** | `If you need more memory, add a node.` |
| `adequate (adj)` / `enough (adj)` | **`SUFFICIENT (adj)`**, **`SATISFACTORY (adj)`** | `Make sure that there is sufficient disk space.` |
| `adjacent to (prep)` | **`NEXT TO (prep)`**, **`NEAR (prep)`** | `Install the sensor next to the port.` |
| `advise (v)` / `inform (v)` / `notify (v)` | **`TELL (v)`**, **`REPORT (v)`** | `Tell the administrator that the build failed.` |
| `affect (v)` | **`CHANGE (v)`**, **`HAVE AN EFFECT ON`** | `This flag changes the timeout behavior.` |
| `afterwards (adv)` / `subsequently (adv)` | **`THEN (adv)`**, **`LATER (adv)`** | `First stop the proxy. Then update the binary.` |
| `alert (v)` / `warn (v)` | **`TELL (v)`**, **`GIVE A WARNING`** | `The monitor gives a warning when memory is low.` |
| `alter (v)` / `modify (v)` | **`CHANGE (v)`** | `Do not change the default port.` |
| `always (adv)` | **`ALWAYS (adv)`** *(Approved!)* | `Always validate the input payload.` |
| `aid (n/v)` / `assist (v)` | **`HELP (n/v)`** | `This tool helps you find memory leaks.` |
| `annually (adv)` / `yearly (adj/adv)` | **`EVERY YEAR`**, **`12-MONTH`** | `Rotate the root key every year.` |
| `apparent (adj)` / `obvious (adj)` | **`CLEAR (adj)`** | `The cause of the error is clear.` |
| `appear (v)` | **`SHOW (v)`**, **`COME ON (v)`**, **`SEEM`** -> **`BE (v)`** | `The error message shows on the screen.` |
| `appropriate (adj)` / `proper (adj)` / `suitable (adj)` | **`APPLICABLE (adj)`**, **`CORRECT (adj)`** | `Select the applicable configuration file.` |
| `ascertain (v)` / `determine (v)` | **`FIND (v)`**, **`CALCULATE (v)`**, **`MAKE SURE (v)`** | `Find the cause of the high latency.` |
| `attempt (n/v)` / `endeavor (v)` | **`TRY (n/v)`** | `Try to connect to the primary host.` |
| `authorize (v)` | **`APPROVE (v)`**, **`ALLOW (v)`** *(or TV `authorize`)* | `Only a supervisor can approve this change.` |
| `auxiliary (adj)` | **`SECONDARY (adj)`**, **`ALTERNATIVE (adj)`**, **`STANDBY (TN)`** | `The secondary power supply starts automatically.` |
| `carry out (v)` / `conduct (v)` | **`DO (v)`** | `Do a check of the network interface.` |
| `cease (v)` / `halt (v)` / `terminate (v)` | **`STOP (v)`** | `Stop the worker process immediately.` |
| `check (v)` / `inspect (v)` | **`EXAMINE (v)`**, **`MAKE SURE (v)`**, **`DO A CHECK OF`** | `Examine the certificate for expiration.` |
| `choose (v)` / `pick (v)` | **`SELECT (v)`** | `Select the region from the list.` |
| `commence (v)` / `initiate (v)` / `launch (v)` | **`START (v)`**, **`BEGIN (v)`** | `Start the migration job.` |
| `comprise (v)` / `consist of (v)` | **`HAVE (v)`**, **`CONTAIN (v)`**, **`INCLUDE (v)`** | `The cluster contains three control nodes.` |
| `conceal (v)` / `hide (v)` | **`COVER (TN)`**, **`KEEP OUT OF SIGHT`** | `Do not show the secret key in the log.` |
| `conclude (v)` / `finish (v)` | **`COMPLETE (v)`**, **`STOP (v)`** | `Wait until the script completes the backup.` |
| `confirm (v)` / `verify (v)` | **`MAKE SURE (v)`** *(or TV `validate`)* | `Make sure that the pod is ready.` |
| `consequently (adv)` / `hence (adv)` / `therefore (adv)` | **`THUS (adv)`**, **`AS A RESULT`** | `The token is invalid. Thus, the server rejects it.` |
| `construct (v)` / `fabricate (v)` / `manufacture (v)` | **`MAKE (v)`**, **`ASSEMBLE (v)`** | `Make a temporary directory for the artifacts.` |
| `consult (v)` / `see (v)` (for docs) | **`REFER (v)`** (`REFER TO`) | `Refer to the API specification.` |
| `convert (v)` / `transform (v)` | **`CHANGE (v)`** | `The parser changes the input into JSON.` |
| `customary (adj)` / `normal (adj)` / `regular (adj)` | **`USUAL (adj)`**, **`STANDARD (adj)`**, **`NORMAL (adj)`** *(Approved!)* | `The service operates in its normal mode.` |
| `danger (n)` / `hazard (n)` | **`RISK (n)`**, **`DANGEROUS (adj)`** | `This procedure decreases the risk of data loss.` |
| `defect (n)` / `flaw (n)` | **`DEFECT (TN)`**, **`DAMAGE (n)`**, **`ERROR (TN)`** | `Examine the response for errors.` |
| `demonstrate (v)` / `exhibit (v)` / `reveal (v)` | **`SHOW (v)`** | `The graph shows the request rate.` |
| `denote (v)` / `indicate (v)` / `signify (v)` | **`SHOW (v)`**, **`MEAN`** -> **`BE (v)`** | `A green icon shows that the node is healthy.` |
| `Entire (adj)` / `whole (adj)` | **`ALL (adj)`**, **`FULL (adj)`**, **`COMPLETE` -> `FULL`** | `Copy all the contents of the folder.` |
| `equip (v)` / `furnish (v)` / `provide (v)` | **`SUPPLY (v)`**, **`GIVE (v)`**, **`HAVE (v)`** | `Supply a valid API key in the request header.` |
| `essential (adj)` / `vital (adj)` / `required (adj)` | **`NECESSARY (adj)`**, **`MANDATORY (adj)`** | `A TLS certificate is mandatory for production.` |
| `establish (v)` | **`MAKE (v)`**, **`SET (v)`**, **`START (v)`** | `Start a secure connection to the host.` |
| `estimate (v)` | **`CALCULATE (v)`**, **`APPROXIMATELY (adv)`** | `Calculate the necessary storage capacity.` |
| `evaluate (v)` / `assess (v)` | **`EXAMINE (v)`**, **`MEASURE (v)`**, **`CALCULATE (v)`** | `Measure the throughput of the pipeline.` |
| `exceed (v)` | **`BE MORE THAN`** | `The payload size must not be more than 10 MB.` |
| `excessive (adj)` | **`TOO MUCH`**, **`MORE THAN PERMITTED`** | `Too much traffic can cause a timeout.` |
| `exclusively (adv)` / `merely (adv)` / `solely (adv)` | **`ONLY (adv)`** | `Use this flag only in debug mode.` |
| `forward (v)` / `transmit (v)` | **`SEND (v)`**, **`TRANSMIT (v)`** *(Approved!)* | `The proxy sends the packet to the backend.` |
| `frequently (adv)` / `often (adv)` | **`FREQUENTLY (adv)`** *(Approved!)* | `If the error occurs frequently, examine the logs.` |
| `generate (v)` / `produce (v)` | **`MAKE (v)`**, **`CAUSE (v)`** | `The command makes a new key pair.` |
| `identical (adj)` | **`THE SAME`** | `The two replicas use the same image.` |
| `immediately (adv)` / `promptly (adv)` / `at once` | **`IMMEDIATELY (adv)`** *(Approved!)* | `If a breach occurs, revoke the token immediately.` |
| `impact (n/v)` | **`EFFECT (n)`**, **`HIT (v)`**, **`DAMAGE (n)`** | `This setting has no effect on latency.` |
| `implement (v)` | **`DO (v)`**, **`USE (v)`**, **`INSTALL (v)`** | `Use the new retry policy on all clients.` |
| `important (adj)` / `significant (adj)` | **`IMPORTANT (adj)`** *(Approved!)* | `It is important to save the recovery key.` |
| `improper (adj)` / `inaccurate (adj)` / `invalid (adj)` | **`INCORRECT (adj)`**, **`NOT VALID`** | `If the signature is not valid, reject the request.` |
| `in addition` / `moreover (adv)` / `furthermore (adv)` | **`ALSO (adv)`**, **`AND (conj)`** | `The worker validates the schema and also logs the event.` |
| `in accordance with` | **`AS SPECIFIED IN`**, **`OBEY (v)`** | `Configure the firewall as specified in Section 5.` |
| `in order to` / `so as to` | **`TO (prep)`** | `To free memory, clear the cache.` |
| `initial (adj)` | **`FIRST (adj)`** | `After the first boot, change the root password.` |
| `prior to (prep)` / `previous to` | **`BEFORE (prep/conj)`** | `Before you upgrade the database, make a backup file.` |
| `prohibit (v)` / `forbid (v)` | **`NOT ALLOW`**, **`DO NOT`**, **`NOT PERMITTED`** | `Anonymous access is not permitted.` |
| `purchase (v)` / `buy (v)` | **`GET (v)`** | `Get a license from the vendor.` |
| `rapidly (adv)` / `quickly (adv)` | **`QUICKLY (adv)`** *(Approved!)* | `The autoscaler increases capacity quickly.` |
| `reduce (v)` / `diminish (v)` / `lessen (v)` | **`DECREASE (v)`** | `Compression decreases the payload size.` |
| `regarding (prep)` / `concerning (prep)` | **`ABOUT (prep)`**, **`FOR (prep)`** | `For data about error codes, refer to Table 3.` |
| `remedy (v)` / `rectify (v)` / `resolve (v)` | **`CORRECT (v)`**, **`REPAIR (v)`** | `To correct the mismatch, synchronize the clocks.` |
| `request (v)` / `ask (v)` | **`ASK (v)`** -> **`TELL (v)`**, **`WANT (v)`**, **`GET (v)`** | `The client sends a request for a new token.` (`request (n)` is a TN). |
| `retain (v)` / `preserve (v)` / `maintain (v)` | **`KEEP (v)`** | `Keep the audit logs for 90 days.` |
| `retrieve (v)` / `fetch (v)` | **`GET (v)`** | `Get the secret from the vault.` |
| `return (v)` | **`PUT BACK`**, **`SEND BACK`**, **`GO BACK`** | `The function sends back a status code.` |
| `routine (adj)` | **`STANDARD (adj)`**, **`SCHEDULED (adj)`**, **`USUAL (adj)`** | `Do the scheduled maintenance every Sunday.` |
| `specify (v)` | **`SPECIFIED (adj)`** *(past participle only!)*, **`GIVE (v)`**, **`SHOW (v)`** | `Enter the specified port number.` (`specify` is approved only as `SPECIFIED (adj)`). |
| `state (v)` / `declare (v)` / `mention (v)` | **`SAY` -> `SHOW (v)`**, **`TELL (v)`**, **`WRITE (v)`** | `The manifest shows the memory limit.` |
| `utilize (v)` / `employ (v)` | **`USE (v)`** | `Use the CLI to deploy the service.` |
| `via (prep)` / `by means of` / `through (prep)` | **`WITH (prep)`**, **`THROUGH (prep)`** *(Approved for physical passage)*, **`BY (prep)`** | `Connect to the host with SSH.` |
| `yet (adv/conj)` | **`AT THIS TIME`**, **`BUT (conj)`** | `The volume is not mounted at this time.` |

---

## 5. Official Issue 9 Computer & Software Terms (Rules 1.5 & 1.12)

ASD-STE100 Issue 9 explicitly authorizes computer science and software vocabulary through **Rule 1.5 Category 19 (Technical Nouns)** and **Rule 1.12 Category 2 (Technical Verbs)**:

### Rule 1.5 Category 19: Computer Science, Information and Communication Technology (TNs)
`add-in`, `add-on`, `AI`, `arrow`, `artificial intelligence`, `authentication`, `backup`, `backup file`, `bookmark`, `chatbot`, `content`, `cursor`, `cybersecurity`, `database`, `deep learning`, `dialog check box`, `digitalization`, `digitization`, `e-mail`, `embedding`, `field`, `file`, `firewall`, `hallucination`, `HTML`, `icon`, `interface`, `internet`, `laptop`, `large language model`, `local operation`, `machine learning`, `memory`, `menu`, `metadata`, `mouse`, `network`, `operating system`, `phone`, `plug-in`, `pre-loaded software`, `preset value`, `prompt engineering`, `remote operation`, `screen`, `search engine`, `smartphone`, `status bar`, `store`, `tablet`, `token`, `toolbar`, `touchscreen`, `tweet`, `tuning`, `update`, `voice mail`, `XML`

### Rule 1.12 Category 2: Computer Processes and Applications (TVs)
* **2a. Input/Output Processes**: `click`, `digitize`, `enter`, `press`, `print`, `swipe`, `tap`, `type`
* **2b. User-Interface and Application Processes**: `clear`, `close`, `copy`, `cut`, `delete`, `deselect`, `disable`, `drag`, `drag and drop`, `enable`, `encrypt`, `erase`, `filter`, `highlight`, `invalidate`, `maximize`, `minimize`, `navigate`, `open`, `paste`, `save`, `scroll`, `sort`, `store`, `tweet`, `validate`, `zoom in`, `zoom out`
* **2c. System Operations**: `abort`, `boot`, `communicate`, `debug`, `download`, `format`, `install`, `load`, `manage`, `process`, `reboot`, `update`, `upgrade`, `upload`

> [!IMPORTANT]
> Even when a word is an approved Technical Noun or Technical Verb, **Rule 1.7** (never use a TN as a verb) and **Rule 1.13** (never use a TV as a noun) still apply strictly. Note that a handful of words (`store`, `tweet`, `update`) appear in **both** Rule 1.5 Category 19 and Rule 1.12 Category 2 in Issue 9, so they are valid as both a Technical Noun and a Technical Verb.
