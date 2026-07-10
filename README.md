# Detection Engineering

This repository documents my Detection Engineering learning path and hands-on SOC-focused labs.

The main goal of this project is to understand how detections are created, tested, tuned, documented, and improved inside a Security Operations Center environment.

The project covers detection engineering fundamentals, tactical detection, threat intelligence usage, Sigma rule development, IOC-based hunting, endpoint detection with Aurora EDR, and SOAR automation workflows.

---

## Project Overview

Detection engineering is not only about writing alert rules. A useful detection should have clear logic, relevant telemetry, proper context, false positive awareness, and investigation guidance.

Across these rooms and labs, I focused on:

- Understanding different detection types
- Mapping attacker behaviour to detection logic
- Using threat intelligence in SOC workflows
- Writing and reviewing Sigma rules
- Creating detections from IOCs
- Testing detections against malicious activity
- Understanding endpoint detection and response concepts
- Learning how SOAR playbooks support SOC automation and response

---

## Repository Contents

| # | Room / Lab | Main Focus |
|---|---|---|
| 01 | [Detection Engineering Fundamentals](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/01%20-%20Detection%20Engineering%20Fundamentals.md) | Detection types, Detection as Code, detection workflow, frameworks, ADS Framework, and detection maturity |
| 02 | [Tactical Detection](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/02.%20Tactical%20Detection.md) | IOC-based detections, Sigma conversion, public Sigma rules, tripwires, honeypots, and Sigma rule testing |
| 03 | [Threat Intelligence for SOC](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/03.%20Threat%20Intelligence%20for%20SOC.md) | Threat intelligence types, IOC handling, Uncoder, Kibana hunting, firewall blocking, DNS sinkhole, and ElastAlert |
| 04 | [Sigma](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/04.%20Sigma.md) | Sigma syntax, rule fields, logsource, detection logic, modifiers, false positive filtering, and practical Sigma labs |
| 05 | [Sigma Hunt Lab: Creating Detection Rules from IOCs](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/05%20-%20Sigma%20Hunt%20Lab%3A%20Creating%20Detection%20Rules%20from%20IOCs.md) | Creating Sigma rules from incident response IOCs across a ransomware attack chain |
| 06 | [Aurora EDR: Endpoint Detection and Response Lab](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/06%20-%20Aurora%20EDR%3A%20Endpoint%20Detection%20and%20Response%20Lab.md) | Endpoint telemetry, Windows Event Logs, ETW, Aurora EDR, Sigma-based detections, and response actions |
| 07 | [Introduction to SOAR: SOC Automation and Response Workflows](https://github.com/BatuhanTekin95/Detection-Engineering/blob/main/doc/07%20-%20Introduction%20to%20SOAR%3A%20SOC%20Automation%20and%20Response%20Workflows.md) | SOC challenges, SOAR concepts, orchestration, automation, response, and playbook workflows |

---

## Sections

### 01 - Detection Engineering Fundamentals

This section covers the foundation of detection engineering and explains how different detection approaches can be used inside a SOC environment.

Topics covered include:

- Configuration detection
- Modelling
- Indicator detection
- Threat behaviour detection
- Detection as Code
- Detection gap analysis
- Data source identification
- Baseline creation
- Rule writing, testing, deployment, and tuning
- MITRE ATT&CK, CAR, Pyramid of Pain, Cyber Kill Chain, and Unified Kill Chain
- Alerting and Detection Strategy Framework
- Detection Maturity Level Model

The main takeaway from this section is that effective detections should be clear, testable, documented, and adaptable over time.

---

### 02 - Tactical Detection

This section focuses on creating practical detections from known threats, previous incident findings, threat intelligence, and Indicators of Compromise.

Topics covered include:

- IOC-based detection logic
- Sigma rule development
- Public Sigma rule review
- Rule conversion with Uncoder
- Follina-MSDT detection example
- Log4j suspicious shell detection example
- Tripwire detection
- Honeypots and hidden files
- Object access auditing
- Sigma rule testing and tuning

The main point of this section is that tactical detections should be relevant, actionable, and useful for investigation.

---

### 03 - Threat Intelligence for SOC

This section focuses on how threat intelligence can support SOC monitoring, detection, investigation, prevention, and response.

Topics covered include:

- Threat intelligence types
- Threat intelligence producers and consumers
- IOC handling
- Defanged indicator conversion
- IOC query generation with Uncoder
- IOC hunting in Kibana
- Destination IP and port analysis
- Firewall blocking
- Domain blocking
- DNS sinkhole concepts
- ElastAlert alerting workflow

This section shows how threat intelligence becomes more useful when it is connected to real SOC workflows.

---

### 04 - Sigma

This section focuses on Sigma, a vendor-agnostic rule format used to write log-based detection rules.

Topics covered include:

- Sigma rule structure
- YAML syntax
- Common Sigma fields
- Logsource configuration
- Detection blocks
- Search identifiers
- Conditions
- Value modifiers
- False positive filtering
- Rule metadata
- MITRE ATT&CK tagging

The practical part includes examples such as suspicious AnyDesk installation detection, scheduled task activity, ransomware-related behaviour, and Sigma rule validation.

---

### 05 - Sigma Hunt Lab

This lab focuses on creating Sigma rules from IOCs provided after a ransomware incident.

The attack chain included:

- Malicious `mshta.exe` execution
- `certutil.exe` payload download
- Netcat reverse shell activity
- PowerUp privilege escalation enumeration
- Service binary modification
- RunOnce persistence
- Data collection
- Exfiltration activity
- Ransomware file encryption

The purpose of this lab was to practise turning incident response findings into reusable detection rules.

---

### 06 - Aurora EDR

This section focuses on endpoint detection and response concepts using Aurora EDR.

Topics covered include:

- Endpoint telemetry
- Windows Event Logs
- Windows Event Viewer
- Event Tracing for Windows
- Aurora EDR overview
- Aurora and Sysmon comparison
- Aurora presets
- Aurora output options
- Aurora response actions
- Aurora Event IDs
- Sigma-based endpoint detections

This lab connects endpoint visibility, Sigma-based detection logic, and response actions inside an EDR workflow.

---

### 07 - Introduction to SOAR

This section focuses on how SOAR can help SOC teams reduce repetitive manual work and improve response workflows.

Topics covered include:

- Traditional SOC challenges
- Alert fatigue
- Disconnected tools
- Manual processes
- SOAR concepts
- Orchestration
- Automation
- Response
- SOC analyst decision points
- Phishing playbook
- CVE patching playbook

The main point of this section is that SOAR does not replace SOC analysts. It helps analysts work more efficiently by automating repetitive steps and standardising response workflows.

---

## Tools and Platforms Mentioned

- SIEM
- EDR
- Sigma
- Uncoder.io
- Kibana
- Elastic Stack
- Windows Event Logs
- Windows Event Viewer
- Event Tracing for Windows
- Aurora EDR
- Sysmon
- Firewall rules
- DNS sinkhole
- ElastAlert
- SOAR playbooks
- MITRE ATT&CK
- Cyber Kill Chain
- Pyramid of Pain

---

## Key Skills Practised

Through this project, I practised:

- Analysing detection logic
- Understanding attacker behaviour
- Mapping detections to security frameworks
- Reviewing required log sources
- Using IOCs in investigations
- Creating Sigma rules
- Testing detection rules
- Considering false positives
- Understanding detection maturity
- Reviewing endpoint detection alerts
- Connecting SOC workflows with automation and response

---

## Key Takeaways

Detection engineering is an ongoing process. A detection should not be treated as a one-time rule.

A useful detection should be:

- Clear
- Testable
- Documented
- Tuned
- Supported by reliable telemetry
- Mapped to relevant attacker behaviour
- Useful for SOC investigation

This project also showed that detection engineering connects many SOC areas together, including threat intelligence, SIEM monitoring, endpoint detection, incident response, and SOAR automation.

---

## Disclaimer

This repository was created for learning and portfolio purposes.

The content is based on practical training rooms, lab scenarios, and detection engineering notes. The examples are intended to show my understanding of SOC workflows, detection logic, Sigma rules, endpoint visibility, and response automation.
