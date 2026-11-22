# ASD-STE100 Issue 9 Before & After Software Documentation Examples

This reference contains four paired transformations showing how to convert typical engineering prose into **ASD-STE100 Issue 9 (2025-01-15)** compliant documentation.

---

## Example 1: Production Database Failover Runbook (Procedural Writing)

### Before (Non-Compliant)
> **NOTE:** Make sure you don't execute this failover script prior to verifying that the replica lag is under 100 ms; otherwise, data loss may occur.
>
> 1. Utilize the CLI tool in order to check the current replication status of the standby node, and if it's healthy, proceed with stopping the primary service.
> 2. Using the `pg_ctl promote` command, promote the standby database and test the connection via port 5432.

**Key Issue 9 Violations in "Before":**
* **Rule 5.5 & Rule 7.1**: Places a data-loss hazard inside a `NOTE` with an imperative verb (`Make sure`) instead of a `CAUTION` block.
* **Rule 4.2**: Uses contractions (`don't`, `it's`).
* **Rule 8.1**: Uses a semicolon (`;`).
* **Rule 5.1 & Rule 5.2**: Step 1 has 27 words (exceeds 20-word procedural limit) and combines multiple instructions in one sentence.
* **Rule 1.1 & Rule 1.2**: Uses unapproved words and recurring errors (`execute`, `prior to`, `verifying`, `under`, `otherwise`, `may`, `utilize`, `in order to`, `check (v)`, `proceed`, `using`, `test (v)`, `via`).
* **Rule 3.5**: Uses unapproved `-ing` forms (`verifying`, `stopping`, `Using`).
* **General Recommendation `GR-1`**: Omits `that` after `Make sure`.

### After (ASD-STE100 Issue 9 Compliant)

```markdown
## Database Failover Procedure

> [!CAUTION]
> Do not start the failover script if the replica lag is more than 100 ms. High replica lag can cause data loss.

1. Enter this command to measure the replication lag on standby node A1:
   ```bash
   dbctl status --node A1
   ```
2. Make sure that the replication lag is less than 100 ms.
3. If the standby node is serviceable, stop the primary database service.
4. Enter the `pg_ctl promote` command on standby node A1.
5. Do a test of the database connection on port 5432.
```

---

## Example 2: REST API Endpoint Specification (Descriptive + Procedural Reference)

### Before (Non-Compliant)
> ### Token Rotation Endpoint
> An authentication token rotation is performed by the `/v1/tokens/rotate` endpoint whenever a client needs to obtain a fresh access token. It's required that the caller provides a valid refresh token (e.g., a signed JWT) in the request payload; otherwise, the request will be rejected by the API gateway. See the security manual for further details.

**Key Issue 9 Violations in "Before":**
* **Rule 3.6 & Rule 3.7**: Uses passive voice and nominalization (`An authentication token rotation is performed by...`, `will be rejected by...`).
* **Rule 1.1 & Rule 1.3**: Uses unapproved words (`whenever`, `needs`, `obtain`, `fresh`, `required`, `provides`, `valid`, `otherwise`, `further`), and misuses `See` for a document reference (use `Refer to`).
* **`GR-6`**: Uses the Latin abbreviation `e.g.` (use `for example`).
* **Rule 4.2 & Rule 8.1**: Uses a contraction (`It's`) and a semicolon (`;`).

### After (ASD-STE100 Issue 9 Compliant)

```markdown
## Token Refresh Endpoint Overview

The `/v1/tokens/rotate` endpoint gives a new access token to an authenticated client. The client must send a correct refresh token in the JSON payload. For example, the client can send a signed JWT string. If the refresh token is expired, the API gateway rejects the request with status code 401.

For more data about token signatures, refer to the Authentication Manual.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `refresh_token` | `String` | Mandatory. The active refresh token that the authentication server gave to the client. |
| `scope` | `String` | Optional. The permission scope for the new access token. |
```

---

## Example 3: System Architecture Overview (Descriptive Writing)

### Before (Non-Compliant)
> ### Telemetry Ingestion Architecture
> Our telemetry pipeline is responsible for collecting metrics from edge nodes and forwarding them to the central storage cluster. While the collector daemon is running on each host, it buffers incoming events in memory so that network spikes don't impact application performance. Approximately 10,000 events per second can be processed by each collector instance. Furthermore, if the network connection is lost, the buffer is automatically flushed to a local disk file by the daemon. Once connectivity has been restored, the daemon reads the local file and transmits the old data to the server.

**Key Issue 9 Violations in "Before":**
* **`GR-3`**: Uses the first-person plural pronoun `Our`.
* **Rule 3.5 & Rule 3.4**: Uses progressive tenses and gerunds (`collecting`, `forwarding`, `While ... is running`, `incoming`, `has been restored`).
* **Rule 3.6**: Uses passive voice (`can be processed by`, `is automatically flushed ... by`, `has been restored`).
* **Rule 1.1**: Uses unapproved words (`responsible`, `while`, `so that`, `impact`, `furthermore`, `connectivity`, `old`).
* **Rule 4.2**: Uses a contraction (`don't`).

### After (ASD-STE100 Issue 9 Compliant)

```markdown
## Telemetry Pipeline Architecture

The telemetry pipeline collects metrics from edge nodes and sends them to the primary storage cluster. One collector daemon operates on each host. The daemon stores new events in a memory buffer. This buffer prevents high network latency during traffic peaks. Each collector instance processes a maximum of 10,000 events each second.

If the network connection stops, the daemon writes the buffered events to a local file. When the network connection operates again, the daemon reads the local file. Then the daemon transmits the remaining events to the primary storage cluster.

> [!NOTE]
> The collector daemon encrypts all local buffer files with AES-256.
```

---

## Example 4: CLI Installation & Configuration Guide (Mixed Procedural + Descriptive)

### Before (Non-Compliant)
> ### Installing and Setting Up the Agent
> Prior to installing the agent, ensure your operating system has enough free disk space (about 500 MB is needed).
> 1. Download the archive and extract it into `/opt/agent`; then check the binary checksum.
> 2. Modify `/etc/agent/config.yaml` using your preferred text editor and insert your API key.

**Key Issue 9 Violations in "Before":**
* **Rule 3.5 & Rule 9.3**: Heading uses unapproved `-ing` forms and phrasal verb `Setting Up`.
* **Rule 1.1, Rule 1.2 & Rule 1.3**: Uses `Prior to` (`Before`), `installing` (gerund), `ensure` (`make sure that`), `enough` (`sufficient`), `about 500 MB` (`approximately 500 MB`), `needed` (`necessary`), `extract` (`decompress` / `remove`), `check (v)` (`do a check of` / `validate`), `Modify` (`Change` / `Edit`), `using` (`with`), `preferred` (unapproved), `insert` (`put` / `enter`).
* **Rule 8.1 & Rule 5.2**: Step 1 uses a semicolon (`;`) and packs three sequential instructions into one sentence.

### After (ASD-STE100 Issue 9 Compliant)

```markdown
## Agent Installation Procedure

Before you install the agent, make sure that the host has a minimum of 500 MB of free disk space.

1. Download the agent package to the `/tmp` directory.
2. Decompress the agent package into the `/opt/agent` directory.
3. Validate the binary checksum with this command:
   ```bash
   sha256sum -c /opt/agent/agent.sha256
   ```
4. Open the `/etc/agent/config.yaml` file in a text editor.
5. Enter your API key in the `api_key` field.
6. Save the `/etc/agent/config.yaml` file and start the agent service.
```
