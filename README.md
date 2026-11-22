# ASD-STE100 Agent Skill

[![Agent Skills Standard](https://img.shields.io/badge/Agent%20Skills-agentskills.io-blue)](https://agentskills.io/)
[![Standard](https://img.shields.io/badge/ASD--STE100-Issue%209%20(2025--01--15)-brightgreen)](https://www.asd-ste100.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B%20(stdlib%20only)-yellow)](#validator-cli-reference-scriptscheck_stepy)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](./LICENSE)

A portable [Agent Skills](https://agentskills.io/) package for authoring, rewriting, reviewing, and auditing technical and software documentation in compliance with **ASD-STE100 Simplified Technical English (Issue 9, 2025-01-15)**.

Includes modular Issue 9 rule guides, bundled Issue 9 dictionary JSON resources (2,198 entries), software/Markdown adaptation guidelines, before-and-after examples, and a zero-dependency Python 3 compliance checker (`scripts/check_ste.py`).

**Works with:** Claude Code, OpenAI Codex CLI, Cursor, GitHub Copilot, Gemini CLI, Antigravity, Windsurf, OpenCode, Cline, Roo Code, and any other agent supporting the [Agent Skills open standard](https://agentskills.io/).

---

## Quick Install

### Universal Installer (Recommended)

Use the [Skills CLI](https://github.com/vercel-labs/skills) to install into all detected coding agents automatically:

```bash
# Install into the current project
npx skills add dontmindmexdd/asd-ste100

# Install globally for all projects
npx skills add dontmindmexdd/asd-ste100 -g
```

### Gemini CLI

```bash
gemini skills install https://github.com/dontmindmexdd/asd-ste100
```

---

## For Coding Agents

### Ask Your Agent to Install It

Paste this prompt directly into Claude Code, Codex, Cursor, Copilot, Gemini CLI, Antigravity, Windsurf, OpenCode, Cline, or Roo Code:

> Install the `asd-ste100` skill from `https://github.com/dontmindmexdd/asd-ste100` into my global skills directory for your environment, then verify that `scripts/check_ste.py` runs cleanly on a sample sentence.

### Agent Integration Notes

If you are a coding agent installing or executing this skill:

1. **Skill Entrypoint:** `SKILL.md` at the repository root defines the skill (`name: asd-ste100`) and follows progressive disclosure. Read `references/` and `examples/` on demand as linked from `SKILL.md`.
2. **Install Location:** Clone or copy this repository into a directory named `asd-ste100` inside your agent's skills folder (see [Manual / Per-Agent Install](#manual--per-agent-install)). Keep the folder name `asd-ste100` so it matches `name: asd-ste100` in `SKILL.md`.
3. **Running the Validator:** Invoke `scripts/check_ste.py` relative to the installed skill root directory (`python3 scripts/check_ste.py ...`). The script resolves `../resources/*.json` relative to `__file__`, so it works from any current working directory without extra configuration.
4. **Verification Command:** Run the following from the installed skill directory (or with the path to `scripts/check_ste.py`) and confirm exit code `0`:
   ```bash
   python3 scripts/check_ste.py --mode procedural - <<'EOF'
   1. Start the service and examine the log file.
   EOF
   ```

---

## Manual / Per-Agent Install

Clone the repository directly into your agent's project or global skills directory:

```bash
git clone https://github.com/dontmindmexdd/asd-ste100 <TARGET_SKILLS_DIR>/asd-ste100
```

Replace `<TARGET_SKILLS_DIR>` using the table below:

| Agent | Project Scope | Global Scope |
| :--- | :--- | :--- |
| **Universal (Cross-Agent)** | `.agents/skills/asd-ste100` | `~/.agents/skills/asd-ste100` |
| **Claude Code** | `.claude/skills/asd-ste100` | `~/.claude/skills/asd-ste100` |
| **OpenAI Codex CLI** | `.agents/skills/asd-ste100` or `.codex/skills/asd-ste100` | `~/.agents/skills/asd-ste100` or `~/.codex/skills/asd-ste100` |
| **Cursor** | `.cursor/skills/asd-ste100` or `.agents/skills/asd-ste100` | `~/.cursor/skills/asd-ste100` or `~/.agents/skills/asd-ste100` |
| **GitHub Copilot** | `.github/skills/asd-ste100` or `.agents/skills/asd-ste100` | `~/.copilot/skills/asd-ste100` or `~/.agents/skills/asd-ste100` |
| **Gemini CLI** | `.gemini/skills/asd-ste100` or `.agents/skills/asd-ste100` | `~/.gemini/skills/asd-ste100` or `~/.agents/skills/asd-ste100` |
| **Antigravity** | `.agents/skills/asd-ste100` | `~/.gemini/config/skills/asd-ste100` |
| **Windsurf** | `.windsurf/skills/asd-ste100` | `~/.agents/skills/asd-ste100` |
| **OpenCode** | `.opencode/skills/asd-ste100` or `.agents/skills/asd-ste100` | `~/.config/opencode/skills/asd-ste100` or `~/.agents/skills/asd-ste100` |
| **Cline** | `.cline/skills/asd-ste100` | `~/.cline/skills/asd-ste100` |
| **Roo Code** | `.roo/skills/asd-ste100` or `.agents/skills/asd-ste100` | `~/.roo/skills/asd-ste100` or `~/.agents/skills/asd-ste100` |

> **Tip:** To share one copy across multiple agents that do not read `~/.agents/skills/`, clone once into `~/.agents/skills/asd-ste100` and symlink it (for example, `ln -s ~/.agents/skills/asd-ste100 ~/.claude/skills/asd-ste100`).

---

## Usage & Example Prompts

Once installed, compatible agents automatically activate the skill when you ask for ASD-STE100 / Simplified Technical English work. In agents that support slash commands (such as Claude Code or Cursor), you can also invoke it directly with `/asd-ste100`.

**Example prompts:**

- **Author new docs:** *"Write a production database failover runbook following ASD-STE100 Issue 9 guidelines and verify it with `check_ste.py`."*
- **Rewrite existing docs:** *"Rewrite `docs/getting-started.md` in Simplified Technical English (STE) and fix all errors reported by the validator."*
- **Audit documentation:** *"Audit `docs/api-reference.md` for ASD-STE100 compliance. Summarize violations by rule number and provide compliant rewrites."*
- **Safety notices & notes:** *"Review all `WARNING`, `CAUTION`, and `NOTE` blocks in `docs/deployment.md` against ASD-STE100 Sections 5 and 7."*

---

## Validator CLI Reference (`scripts/check_ste.py`)

`scripts/check_ste.py` is a standalone, **zero-dependency Python 3.8+ (standard library only)** compliance checker. You can run it directly from the terminal, inside CI pipelines, or via a coding agent.

### Usage

```bash
python3 scripts/check_ste.py [OPTIONS] <PATH...>
```

Pass one or more Markdown/text file paths, or `-` to read from `stdin`.

### Options

| Flag | Values / Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `paths` | `PATH [...]` or `-` | *(required)* | One or more files to check, or `-` for `stdin`. |
| `--mode` | `auto`, `procedural`, `descriptive` | `auto` | Enforcement mode. `auto` infers procedural (20-word limit) vs. descriptive (25-word limit) from headings and numbered lists. |
| `--glossary` | `PATH` (repeatable) | none | Additional project-specific glossary (`.json` or `.csv`) for domain Technical Nouns/Verbs. |
| `--dictionary` | `PATH` (repeatable) | none | Additional custom dictionary override (`.json` or `.csv`). |
| `--no-default-glossary` | flag | off | Disable bundled `resources/default-software-glossary.json` (keeps only official Issue 9 Rule 1.5 Cat 19 and Rule 1.12 Cat 2 terms). |
| `--format` | `text`, `json` | `text` | Output format (`text` for human-readable reports, `json` for CI/tooling). |
| `--strict` | flag | off | Exit with status `1` on warnings (`[WARN]`) as well as errors (`[ERROR]`). |

### Exit Codes

- `0` — Pass (0 errors; and 0 warnings when `--strict` is set).
- `1` — Fail (one or more errors, or one or more warnings with `--strict`).

### Examples

```bash
# Check a Markdown file in auto mode
python3 scripts/check_ste.py docs/runbook.md

# Check piped procedural text
python3 scripts/check_ste.py --mode procedural - <<'EOF'
1. Start the container and examine the log file.
EOF

# Check with a project glossary and JSON output for CI
python3 scripts/check_ste.py --glossary project-glossary.json --format json --strict docs/*.md
```

### Sample Output

```text
=== ASD-STE100 Issue 9 Check: <stdin> [FAIL] (Sentences: 1, Errors: 2, Warnings: 0) ===
  [ERROR] Line 1 (STE-1.1): Unapproved word 'Ensure' (dictionary entry: 'ensure (v)').
    Sentence  : Ensure that you are using the latest configuration.
    Suggestion: Use: MAKE SURE (v). (STE example: 'MAKE SURE THAT THE CORRECT SEALS ARE INSTALLED.')
  [ERROR] Line 1 (STE-3.5): Unapproved '-ing' form 'using' (Rule 3.5 permits '-ing' words only in the 9 approved dictionary entries or as part of a Technical Noun).
    Sentence  : Ensure that you are using the latest configuration.
    Suggestion: Rewrite with a simple verb tense (Infinitive, Imperative, Simple Present, Simple Past, or Simple Future) or an explicit clause ('Before you start...', 'When the service runs...').
```

---

## Repository Structure

```text
asd-ste100/
├── SKILL.md                                # Skill manifest (YAML frontmatter + core workflow)
├── README.md                               # Human & agent documentation
├── LICENSE                                 # MIT License + ASD-STE100 trademark/attribution notice
├── .gitignore                              # Python/OS/editor ignore rules
├── scripts/
│   └── check_ste.py                        # Zero-dependency Python 3.8+ STE Issue 9 validator
├── resources/
│   ├── ste-issue9-dictionary.json          # Extracted Issue 9 Part 2 dictionary (2,198 entries)
│   ├── unapproved-words.json               # Fast-lookup unapproved words, POS traps, phrases
│   └── default-software-glossary.json      # Rule 1.5 Cat 19 ICT TNs & Rule 1.12 Cat 2 TVs + software terms
├── references/
│   ├── writing-rules.md                    # Complete Issue 9 rules (Sections 1–9 & GR-1..GR-8)
│   ├── vocabulary-guide.md                 # 39 recurring errors, 208 approved verbs, POS traps
│   └── markdown-software-adaptation.md     # Applying STE to Markdown, APIs, CLI docs & alerts
└── examples/
    └── before-after-software.md            # Four paired software documentation transformations
```

---

## License & Attribution

- **Skill Instructions, Scripts & Software Documentation:** Licensed under the [MIT License](./LICENSE).
- **ASD-STE100 Attribution & Disclaimer:** ASD-STE100™ (Simplified Technical English) is a trademark and copyrighted specification of the **AeroSpace and Defence Industries Association of Europe (ASD)**. The official specification (Issue 9, 2025-01-15) is maintained and distributed by ASD at [https://www.asd-ste100.org/](https://www.asd-ste100.org/). This repository is an independent, community-maintained tooling package and is not affiliated with, endorsed by, or sponsored by ASD.
