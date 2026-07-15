# Detection Engineering

[![Validate Sigma rules](https://github.com/BatuhanTekin95/Detection-Engineering/actions/workflows/validate-sigma.yml/badge.svg)](https://github.com/BatuhanTekin95/Detection-Engineering/actions/workflows/validate-sigma.yml)

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
├── tests/                            # Positive and negative event examples
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
| [PowerUp enumeration](rules/windows_process_creation/powerup_invoke_allchecks.yml) | PowerUp `Invoke-AllChecks` execution | PowerSploit S0194 | Experimental |
| [Service binary modification](rules/windows_process_creation/service_binpath_modification.yml) | `sc.exe config` changing a service `binPath` | T1543.003 | Experimental |
| [RunOnce persistence](rules/windows_process_creation/runonce_registry_persistence.yml) | `reg.exe` adding a RunOnce value | T1547.001 | Experimental |
| [Password-protected 7-Zip archive](rules/windows_process_creation/password_protected_7zip_archive.yml) | 7-Zip archive creation with password protection | T1560.001 | Experimental |
| [Suspicious cURL data transfer](rules/windows_process_creation/curl_data_exfiltration.yml) | `curl.exe` submitting data to a remote URL | T1041 | Experimental |
| [Ransomware Huntme file creation](rules/windows_file_event/ransomware_huntme_file_creation.yml) | File creation using the lab-specific `.huntme` extension | T1486 | Experimental |

All nine Sigma Hunt challenges have been converted into standalone rule files.

## MITRE ATT&CK Coverage

| Detection | Tactic | ATT&CK Mapping | Log Source |
|---|---|---|---|
| Browser-launched MSHTA | Defense Evasion | T1218.005 | Windows process creation |
| Certutil download | Command and Control | T1105 | Windows process creation |
| Netcat reverse shell | Execution | T1059.003 | Windows process creation |
| PowerUp enumeration | Discovery / Privilege Escalation | PowerSploit S0194 | Windows process creation |
| Service binary modification | Persistence / Privilege Escalation | T1543.003 | Windows process creation |
| RunOnce registry persistence | Persistence | T1547.001 | Windows process creation |
| Password-protected archive | Collection | T1560.001 | Windows process creation |
| cURL data transfer | Exfiltration | T1041 | Windows process creation |
| Huntme file creation | Impact | T1486 | Windows file event |

## Rule Scope and Tuning

The rules are intentionally focused on the behaviour observed in the lab rather than claiming to detect every variation.

- The MSHTA rule focuses on common browser parent processes.
- The Certutil rule requires the `-urlcache`, `-split`, and `-f` options.
- The Netcat rule focuses on the `-e` option launching a Windows command shell.
- The PowerUp rule focuses on the `PowerUp` and `Invoke-AllChecks` strings appearing together.
- The service and RunOnce rules focus on command-line changes made with native Windows utilities.
- The archive and cURL rules are medium severity because both tools have common legitimate uses.
- The ransomware rule is specific to the `.huntme` extension used in the lab scenario.
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
- Positive and negative example coverage
- Conformance with the official Sigma JSON schema

Automated checks improve consistency, but they do not replace testing against real telemetry.

## Test Examples

[`tests/rule_examples.yml`](tests/rule_examples.yml) contains at least one expected match and one expected non-match for every standalone rule. These examples document the intended behaviour and provide a starting point for backend-specific testing.

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
