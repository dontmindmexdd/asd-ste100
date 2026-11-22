---
name: asd-ste100
description: >-
  Author, rewrite, review, and audit technical and software documentation in
  compliance with ASD-STE100 Simplified Technical English (Issue 9, 2025-01-15).
  Use this skill whenever the user asks to write or edit documentation,
  runbooks, API references, architecture specifications, procedures, safety
  notices, or text following ASD-STE100, STE, or Simplified Technical English
  guidelines.
license: MIT
compatibility: Requires Python 3.8+ (standard library only) for scripts/check_ste.py
metadata:
  author: Denis Lupu
  version: "1.0.0"
  standard: "ASD-STE100 Issue 9 (2025-01-15)"
---

# ASD-STE100 Simplified Technical English (Issue 9)

This skill enforces **ASD-STE100 Issue 9 (2025-01-15)** writing rules (53 rules across Sections 1–9 plus General Recommendations `GR-1` through `GR-8`) and the official Issue 9 dictionary across technical and software documentation, backed by modular reference guides, bundled official JSON dictionaries, and an automated compliance checker.

---

## 1. Non-Negotiable Core Constraints (Quick Reference)

| Category | ASD-STE100 Issue 9 Constraint | Rule Ref |
| :--- | :--- | :--- |
| **Vocabulary** | Use only words that are: (1) **Approved in the STE dictionary** (`UPPERCASE` entries), (2) **Technical Nouns (TNs)** (22 categories, including Category 19 Computer Science & ICT), or (3) **Technical Verbs (TVs)** (4 categories, including Category 2 Computer Processes & Applications). | Rules 1.1, 1.5, 1.12 |
| **One Meaning / One POS** | Use each approved word strictly in its specified part of speech and approved meaning. Never use a Technical Noun as a verb or a Technical Verb as a noun. | Rules 1.2, 1.3, 1.7, 1.13 |
| **Spelling** | Use standard **American English** spelling (`color`, `center`, `liter`) unless inside unchanged quoted text. | Rules 1.14, 8.6 |
| **Multi-Word Nouns** | Write multi-word nouns of **no more than 3 words**. For longer technical nouns, write in full first and define a shorter form, or connect related words as one unit with hyphens (`-`) (maximum 3 hyphenated words). | Rules 2.1, 2.2, 8.2 |
| **Allowed Verb Forms** | Use **only 6 forms** from the dictionary: (1) Infinitive (`to start`), (2) Imperative (`Start`), (3) Simple Present (`starts`), (4) Simple Past (`started`), (5) Simple Future (`will start`), and (6) Past Participle **strictly as an adjective** (before a noun, or after `to be`, `to become`, or `to stay`). | Rules 3.1–3.3 |
| **Forbidden Verb Forms** | Do not use auxiliary verbs to make complex verb constructions (no progressive/continuous `is running`, no perfect `has completed`). Do not use unapproved modals (`should`, `shall`, `may`, `might`, `would`). | Rules 3.2, 3.4 |
| **`-ing` Form Restriction** | Use an `-ing` form only as a Technical Noun, as a modifier in a Technical Noun (`cooling fan`), or if it is one of the **9 approved `-ing` dictionary words** (`lighting, opening, routing, servicing, mating, missing, remaining, something, during`). Never use `using` (`USE (v)` or `WITH (prep)`). | Rule 3.5 |
| **Active Voice** | Use the **active voice** (`The gateway rejects the request`). In descriptive writing, passive voice is permitted only when the agent is unknown (or use `something` as the active subject). Use an approved verb to describe an action, not a noun (`DO A TEST OF` or specific TV, not nominalizations). | Rules 3.6, 3.7 |
| **Sentences & Lists** | Write short, clear sentences. Never omit words (nouns, verbs, subjects, articles `the/a/an`) or use contractions (`don't`, `isn't`). Omit `the` before a noun followed by an alphanumeric identifier (`Tag circuit breaker 36L7`). Use vertical lists introduced by a colon (`:`) for complex texts. | Rules 4.1–4.5 |
| **Procedural Writing** | Maximum **20 words** per sentence. Write **one instruction per sentence** unless two actions occur at the same time. Use the **imperative (command) form** (never put `must` before an imperative). Start conditional instructions with the descriptive condition followed by a comma (`If the build fails, examine the log file.`). | Rules 5.1–5.4 |
| **Notes** | Write `NOTE` blocks only to give information, **never** instructions, safety warnings, or step tolerances. Notes obey descriptive rules (maximum **25 words** per sentence, no imperatives). | Rule 5.5 |
| **Descriptive Writing** | Maximum **25 words** per sentence. Give information gradually (no imperatives). Start each paragraph with a topic sentence, keep **one topic per paragraph**, and never exceed **6 sentences per paragraph**. | Rules 6.1–6.6 |
| **Safety Instructions** | Place **before** the hazardous step. Identify risk level with `WARNING` (injury or death) or `CAUTION` (damage to objects, equipment, or systems). Start with a clear command or condition and give an explanation of the risk. Obey the **20-word** procedural sentence limit. | Rules 5.1, 7.1–7.3 |
| **Punctuation & Counting** | **No semicolons (`;`)**. A vertical-list colon (`:`) ends the lead-in sentence. Text in parentheses `(...)` counts as **1 word** in the outer sentence and is also checked as a separate sentence. Hyphenated words count as **1 word**. Numbers, number + unit (`10 °C`, `20 kg`), abbreviations, alphanumeric IDs, quoted text, headings/labels, and proper nouns each count as **1 word**. | Rules 8.1–8.7 |
| **General Practices** | Restructure sentences when word-for-word replacement is insufficient. Do not make phrasal verbs (only `COME ON`, `GO OFF`, `PUT ON` are approved). Include conjunction `that` after verbs (`make sure that`, `shows that`). Never use Latin abbreviations (`e.g.`, `i.e.`, `etc.`). Use gender-neutral inclusive language (`he`, `she`, `man`, `woman` are unapproved). | Rules 9.1–9.4, GR-1–GR-8 |

---

## 2. Progressive-Disclosure Reference Map

Read the relevant reference file below when you need detailed guidance on a specific aspect of ASD-STE100 Issue 9:

* **[Writing Rules Reference (Sections 1–9 & GR-1..GR-8)](./references/writing-rules.md)**: Complete summary of all 53 rules across Sections 1–9 and General Recommendations `GR-1` through `GR-8` from the official Issue 9 (2025-01-15) specification, including all 22 Technical Noun categories (Rule 1.5), 4 Technical Verb categories (Rule 1.12), and Section 8 word-counting rules.
* **[Vocabulary & Substitution Guide](./references/vocabulary-guide.md)**: Official Issue 9 "List of recurring errors" (39 high-frequency traps), the complete Issue 9 "List of approved verbs" (208 verbs), top unapproved-to-approved replacements, part-of-speech traps (`CHECK (n)` vs. `check (v)`, `TEST (n)` vs. `test (v)`, `COMPLETE (v)` vs. `complete (adj)`), and computer TNs/TVs.
* **[Markdown & Software Documentation Adaptation](./references/markdown-software-adaptation.md)**: How to apply STE Issue 9 rules to Markdown code blocks, inline identifiers, CLI commands, REST API specifications, tables, and GitHub-flavored alerts (`> [!WARNING]`, `> [!CAUTION]`, `> [!NOTE]`).
* **[Before & After Software Examples](./examples/before-after-software.md)**: Four complete paired transformations (Production Runbook, REST API Endpoint Reference, System Architecture Overview, and CLI User Guide).
* **Bundled Official Issue 9 JSON Resources**:
  * [ste-issue9-dictionary.json](./resources/ste-issue9-dictionary.json) — Complete extracted ASD-STE100 Issue 9 Part 2 Dictionary (2,198 entries: 879 approved entries with POS/forms/meanings/examples, 1,319 unapproved entries with approved alternatives/examples, 39 recurring errors, 208 approved verbs, Rule 1.5 Cat 19 ICT nouns, and Rule 1.12 Cat 2 computer verbs).
  * [unapproved-words.json](./resources/unapproved-words.json) — Fast-lookup database of 1,179 strictly unapproved words, 107 POS/meaning-restricted words, 39 recurring errors, and forbidden phrases/Latin abbreviations.
  * [default-software-glossary.json](./resources/default-software-glossary.json) — Official Rule 1.5 Category 19 ICT Technical Nouns and Rule 1.12 Category 2 Computer Technical Verbs, extended with standard software engineering terms.

---

## 3. Mandatory Workflow for Authoring, Rewriting, or Auditing

Follow these four steps every time this skill is activated:

### Step 1: Classify Content & Identify Domain Terms
1. Determine whether each section is **Procedural** (step-by-step tasks, runbooks, installation guides -> max 20 words, imperative mood), **Descriptive** (architecture, concepts, API behavior -> max 25 words, max 6 sentences/paragraph, declarative mood), a **Note** (Rule 5.5 -> max 25 words, strictly informational, no imperatives), or a **Safety Instruction** (`WARNING` / `CAUTION` -> max 20 words).
2. Identify domain-specific terms that qualify as **Technical Nouns (TNs)** under Rule 1.5 Category 19 (`authentication`, `backup file`, `database`, `firewall`, `interface`, `network`, `operating system`, `token`, or project-specific nouns) or **Technical Verbs (TVs)** under Rule 1.12 Category 2 (`click`, `enter`, `type`, `clear`, `close`, `copy`, `delete`, `disable`, `enable`, `encrypt`, `erase`, `filter`, `navigate`, `open`, `paste`, `save`, `store`, `validate`, `abort`, `boot`, `communicate`, `debug`, `download`, `format`, `install`, `load`, `manage`, `process`, `reboot`, `update`, `upgrade`, `upload`).
3. Keep usage strict under Rules 1.7 and 1.13: never use a Technical Noun as a verb (e.g., write `Make a backup file`, not `Backup the file`), and never use a Technical Verb as a noun (e.g., write `Install the package` or `Installation (TN)`, not `the install`).

### Step 2: Draft or Rewrite Using STE Structure
1. **Restructure before replacing words** (Rule 9.1): Do not do naive word-for-word substitution on convoluted prose. Split long or multi-clause sentences into single-topic sentences or vertical lists introduced by a colon (`:`).
2. **Convert passive voice and nominalizations to active verbs** (Rules 3.6, 3.7):
   * *Non-STE*: `An authentication check is performed by the gateway prior to request forwarding.`
   * *STE*: `The gateway authenticates each request before it sends the request to the service.`
3. **Eliminate recurring errors and unapproved vocabulary** (consult [vocabulary-guide.md](./references/vocabulary-guide.md) or search [ste-issue9-dictionary.json](./resources/ste-issue9-dictionary.json)):
   * `ensure` -> `MAKE SURE (v)` (always include `that`: `Make sure that...` per `GR-1`)
   * `need (v)` / `require (v)` / `required` -> `NECESSARY (adj)` (`It is necessary to...` or `The necessary permission`)
   * `perform` / `carry out` -> `DO (v)`
   * `check (v)` -> `CHECK (n)` (`Do a check of...`), `MAKE SURE (v)`, `EXAMINE (v)`, or `MEASURE (v)`
   * `test (v)` -> `TEST (n)` (`Do a test of...`)
   * `finish (v)` -> `COMPLETE (v)` (`When you complete the test...`)
   * `complete (adj)` -> `COMPLETED (adj)`, `FULL (adj)`, or `ALL (adj)`
   * `enough` -> `SUFFICIENT (adj)` / `SUFFICIENTLY (adv)`
   * `now` -> `AT THIS TIME`
   * `about` (for quantities) -> `APPROXIMATELY (adv)`
   * `see` / `consult` (for document cross-references) -> `REFER (v)` (`Refer to Section 2.`)
   * `using` -> `USE (v)` or `WITH (prep)`
   * `avoid` -> `PREVENT (v)`
   * `should` / `shall` -> `MUST (v)` (in descriptive text) or imperative verb (in procedures)
   * `may` -> `CAN (v)`
   * `however` -> `BUT (conj)`
   * `therefore` -> `THUS (adv)` or `AS A RESULT`
   * `since` (causal) -> `BECAUSE (conj)`

### Step 3: Validate Deterministically with `check_ste.py`
Always run the bundled compliance checker script [check_ste.py](./scripts/check_ste.py) (invoked relative to the skill root directory) on any file or draft you produce or audit. The script automatically loads the full Issue 9 dictionary ([ste-issue9-dictionary.json](./resources/ste-issue9-dictionary.json)), [unapproved-words.json](./resources/unapproved-words.json), and [default-software-glossary.json](./resources/default-software-glossary.json):

```bash
# Run from (or resolve paths relative to) the skill root directory:

# Validate a Markdown or text file (auto-detects procedural vs. descriptive sections)
python3 scripts/check_ste.py path/to/doc.md

# Validate piped text in procedural or descriptive mode
python3 scripts/check_ste.py --mode procedural - <<'EOF'
1. Start the container and monitor the log file.
EOF

# Include an additional project-specific glossary (JSON or CSV)
python3 scripts/check_ste.py \
  --glossary path/to/project-glossary.json \
  path/to/doc.md
```

### Step 4: Resolve Violations & Deliver
1. Fix all **`[ERROR]`** diagnostics reported by `check_ste.py` (sentence word-count breaches, paragraph sentence-count breaches, semicolons, contractions, slashes, unapproved words/phrases, forbidden `-ing` forms, complex tenses, imperatives in notes).
2. Inspect every **`[WARN]`** diagnostic:
   * For `STE-1.2` (POS/meaning-restricted words like `check`, `test`, `complete`, `cover`, `damage`, `about`, `see`): Confirm that the word is used only in its approved part of speech and approved meaning.
   * For `STE-3.6` (passive voice vs. Rule 3.3 adjectival past participle): Rewrite if it describes an action in passive voice (`The file is erased by the job` -> `The job erases the file`); keep only if the past participle describes a state after `to be`, `to become`, or `to stay` (`The file is damaged`).
   * For `STE-2.1` (multi-word noun clusters > 3 words): Hyphenate related modifiers (up to 3 words), insert prepositions (`of`, `for`, `in`, `on`, `to`, `with`), or define a shorter Technical Noun.
3. Re-run `check_ste.py` to confirm **0 errors** before presenting the final text to the user.
4. When auditing existing documentation for a user, summarize findings by Issue 9 rule number, quote the offending sentence with its STE word count, explain the violation, and provide a verified STE-compliant rewrite.
