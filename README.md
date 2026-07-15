# Detection Engineering

This repository documents my detection engineering learning path through SOC-focused notes, practical labs, and reusable Sigma rules.

The goal is to understand how detections are designed, tested, tuned, documented, and connected to investigation workflows. The project covers detection fundamentals, threat intelligence, Sigma, IOC-based hunting, endpoint visibility with Aurora EDR, and SOAR concepts.

## What This Repository Demonstrates

- Translating attacker behaviour and incident findings into detection logic
- Selecting useful telemetry and Sigma log sources
- Writing behaviour-focused Windows process creation rules
- Mapping detections to MITRE ATT&CK
- Considering false positives, limitations, and tuning
- Reviewing detections in Kibana, Windows Event Viewer, and lab environments
- Connecting detection, investigation, response, and automation

## Repository Structure

```text
.
├── doc/                              # Learning notes and hands-on labs
├── rules/
│   └── windows_process_creation/     # Reusable Sigma rules
├── scripts/                          # Local validation utilities
└── .github/workflows/                # Automated rule validation
```

## Labs and Documentation

| # | Lab | Main Focus |
|---|---|---|
| 01 | [Detection Engineering Fundamentals](doc/01%20-%20Detection%20Engineering%20Fundamentals.md) | Detection types, Detection as Code, workflow, frameworks, and maturity |
| 02 | [Tactical Detection](doc/02%20-%20Tactical%20Detection.md) | IOC detections, Sigma conversion, tripwires, auditing, and validation |
| 03 | [Threat Intelligence for SOC](doc/03%20-%20Threat%20Intelligence%20for%20SOC.md) | IOC handling, Kibana hunting, DNS sinkholes, prevention, and ElastAlert |
| 04 | [Sigma](doc/04%20-%20Sigma.md) | Sigma syntax, log sources, conditions, modifiers, filtering, and practical labs |
| 05 | [Sigma Hunt Lab](doc/05%20-%20Sigma%20Hunt%20Lab%20-%20Creating%20Detection%20Rules%20from%20IOCs.md) | Building detections from a ransomware incident attack chain |
| 06 | [Aurora EDR Lab](doc/06%20-%20Aurora%20EDR%20-%20Endpoint%20Detection%20and%20Response%20Lab.md) | ETW telemetry, Sigma matches, endpoint investigation, and response actions |
| 07 | [Introduction to SOAR](doc/07%20-%20Introduction%20to%20SOAR%20-%20SOC%20Automation%20and%20Response%20Workflows.md) | Orchestration, automation, response, and playbook design |

## Practical Sigma Rules

| Rule | Detection Focus | MITRE ATT&CK | Status |
|---|---|---|---|
| [MSHTA launched by a browser](rules/windows_process_creation/mshta_from_browser.yml) | Browser process spawning `mshta.exe` | T1218.005 | Experimental |
| [Suspicious Certutil download](rules/windows_process_creation/certutil_suspicious_download.yml) | `certutil.exe` with common download flags | T1105 | Experimental |
| [Netcat reverse shell](rules/windows_process_creation/netcat_reverse_shell.yml) | Netcat-compatible executable launching a command shell with `-e` | T1059.003 | Experimental |

The Sigma Hunt lab contains nine completed challenges. Three have currently been converted into standalone, reusable rule files. The remaining six are planned additions:

- PowerUp enumeration
- Service binary modification
- RunOnce persistence
- Password-protected 7-Zip collection
- cURL data exfiltration
- Ransomware file creation

## Rule Scope and Tuning

The rules are intentionally focused on the behaviour observed in the lab rather than claiming to detect every variation.

- The MSHTA rule focuses on common browser parent processes.
- The Certutil rule requires the `-urlcache`, `-split`, and `-f` options.
- The Netcat rule focuses on the `-e` option launching a Windows command shell.
- Legitimate administration, deployment, and authorised testing activity may require filtering.
- Field mappings and case sensitivity can vary between Sigma backends and SIEM platforms.

Before production use, each rule should be converted for the target backend, tested against representative logs, and tuned for the environment.

## Validation

Sigma files are automatically checked for:

- Valid YAML
- Required top-level fields
- A detection condition
- Unique rule IDs
- Expected file extensions

Automated checks improve consistency, but they do not replace testing against real telemetry.

## Tools and Platforms

- Sigma
- MITRE ATT&CK
- Kibana and Elastic Stack
- Windows Event Logs and Event Viewer
- Aurora EDR
- Sysmon concepts
- Uncoder.io
- ElastAlert
- SIEM, EDR, and SOAR workflows
- Firewall and DNS sinkhole concepts

## Key Takeaway

Detection engineering is an ongoing process. A useful detection needs clear logic, reliable telemetry, documentation, validation, false-positive awareness, and investigation value. It should be reviewed and improved as attacker behaviour and the monitored environment change.

## Training Context

This repository was created for learning and portfolio purposes. The notes and screenshots are based on guided training rooms and lab scenarios, while the summaries, analyst observations, repository structure, and standalone rule files document my own learning and implementation.

The rules are educational examples and should be reviewed and tested before being used in a production environment.
