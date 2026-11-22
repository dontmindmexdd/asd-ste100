# Markdown & Software Documentation Adaptation Guide

When applying **ASD-STE100 Issue 9 (2025-01-15)** to software and engineering documentation written in Markdown (`.md`), reStructuredText, or AsciiDoc, follow these adaptation rules so that technical precision and STE readability reinforce each other.

---

## 1. Fenced Code Blocks & Configuration Snippets

* **Rule:** Code inside fenced code blocks (```` ```bash ... ``` ````) is **executable source code**, not prose. It is exempt from STE sentence and vocabulary limits.
* **Comments inside code blocks:** Keep code comments concise and written in active, simple STE (`# Start the worker service` rather than `# Here we are going to initialize the worker daemon`).
* **Introduce every code block with a complete STE sentence or lead-in ending in a colon (`:`) (Rule 8.4):**
  * *Procedural lead-in (≤20 words):*
    `Run this command to start the API server:`
  * *Descriptive lead-in (≤25 words):*
    `This configuration file sets the maximum number of database connections:`

---

## 2. Inline Code, CLI Flags, File Paths, and Endpoints

Under **Rules 1.5 and 8.6**, exact software identifiers wrapped in backticks count as **1 word** (a Technical Noun, alphanumeric identifier, or quoted/literal label):

| Markdown Construct | STE Treatment | Word Count (Rule 8.6) |
| :--- | :--- | :--- |
| `` `--max-connections=100` `` | Technical Noun / Alphanumeric Identifier | **1 word** |
| `` `/etc/nginx/nginx.conf` `` | Technical Noun (File Path) | **1 word** |
| `` `POST /v1/users/{id}/tokens` `` | Technical Noun (API Endpoint) | **1 word** |
| `` `ERR_TLS_HANDSHAKE_TIMEOUT` `` | Technical Noun (Error Code) | **1 word** |
| `"Save and Restart"` | Quoted UI Label | **1 word** |

* **Always anchor inline code with a descriptive category noun (Rule 1.8 / Rule 4.5):**
  * *Ambiguous:* `Set max_connections to 50 in config.yaml.`
  * *STE Compliant:* ``Set the `max_connections` parameter to 50 in the `config.yaml` file.``
  * *Exception (Rule 4.5):* Do not use `the` before a category noun followed by an alphanumeric identifier (`Examine node A1`, `Restart pod 3`).
* **Never use CLI command names or Technical Nouns as prose verbs (Rule 1.7):**
  * *Non-STE:* `Grep the log file and curl the health endpoint.`
  * *STE Compliant:* ``Enter the `grep` command for the log file. Then send a request to the `/healthz` endpoint with the `curl` tool.``

---

## 3. GitHub-Flavored Markdown Callouts (`WARNING`, `CAUTION`, `NOTE`)

Map ASD-STE100 **Section 5 (Rules 5.1, 5.5)** and **Section 7 (Rules 7.1–7.3)** directly to standard Markdown alert blocks:

### 3.1 `CAUTION` (System Damage, Service Outage, or Data Loss — Rules 7.1–7.3)
Place **before** the step. Start with an imperative command or condition, then state the exact damage or data loss risk. Every sentence must be **≤20 words** (Rule 5.1):

```markdown
> [!CAUTION]
> Do not run the `db:drop` command in the production environment. This command deletes all customer records permanently.
```

### 3.2 `WARNING` (Physical Injury or Death — Hardware / Electrical / Robotics — Rules 7.1–7.3)
Use only when physical injury or death is possible. Every sentence must be **≤20 words** (Rule 5.1):

```markdown
> [!WARNING]
> Disconnect the primary power cable before you open the server chassis. High voltage inside the chassis can cause injury or death.
```

### 3.3 `NOTE` (Strictly Informational — No Imperatives! — Rule 5.5)
Under **Rule 5.5**, a `NOTE` must **never** contain an imperative command, safety hazard, or work-step tolerance. Notes follow descriptive writing rules (**≤25 words** per sentence):

* *Non-STE:*
  ```markdown
  > [!NOTE]
  > Make sure that you make a backup file of `.env` before you upgrade.
  ```
* *STE Compliant (informational note):*
  ```markdown
  > [!NOTE]
  > The upgrade script keeps the existing `.env` file unchanged.
  ```
  *(If the reader must make a backup file, write it as a numbered procedural step instead of a note!)*

---

## 4. Vertical Lists and Tables in Markdown

### 4.1 Vertical Lists (Rules 4.3 & 8.4)
* Introduce every bulleted or numbered list with a lead-in clause ending in a colon (`:`). The colon acts as the end of the lead-in sentence for word counting.
* In **Procedural Writing**, use numbered lists (`1.`, `2.`, `3.`) for sequential steps. Each step sentence must be **≤20 words** and start with an imperative verb (or a condition `If ...,` followed by an imperative verb).
* In **Descriptive Writing**, use bulleted lists (`*` or `-`) to present complex items clearly. Each full-sentence bullet counts as an independent sentence (**≤25 words**) and ends with a period (`.`).
* Under **Rule 4.3**, if vertical list items are non-sentence fragments, do not put punctuation at the end of items before the last item, and put a period (`.`) at the end of the last item. In safety or prohibition lists, repeat `Do not` or `DO NOT` at the start of each item.

### 4.2 Markdown Tables
* Cell text inside tables must use consistent STE terminology and approved words.
* When a table column contains full sentences (such as a `Description` column for API parameters), keep every sentence within the **25-word descriptive limit** (or **20-word limit** if the cell gives a procedural instruction) and use active voice.
* Short noun-phrase cells (`String`, `Mandatory`, `Default: 30 s`) are evaluated as labels (Rule 8.6) rather than prose sentences.

---

## 5. Headings and Hyperlinks

* **Headings (Rule 8.6):** Titles and headings are not subject to the 20/25-word sentence limit and do not require a trailing period, but they must use approved STE vocabulary, Technical Nouns, and Technical Verbs (`## Install the CLI Agent` or `## CLI Agent Installation`). Never use unapproved words (`## Utilizing the CLI`) in headings.
* **Markdown Links (`[link text](https://...)`):**
  * The target URL inside `(...)` is markup and does not count toward the sentence word count.
  * The visible `[link text]` counts as part of the enclosing sentence (or as 1 word if it is a quoted/proper document title under Rule 8.6).
  * Use `Refer to` (never `See` or `Click here`) for cross-references:
    * *Non-STE:* `Click [here](https://example.com/docs) or see the docs for details.`
    * *STE Compliant:* `For token configuration data, refer to the [Authentication Guide](https://example.com/docs).`
