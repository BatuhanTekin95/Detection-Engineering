# Detection Engineering

## Introduction

This repository contains my notes and lab write-ups from the Detection Engineering section.

Before starting this repository, I worked on several SOC-related projects, including phishing analysis, SIEM investigations, threat hunting, and firewall fundamentals. Those projects helped me understand how attacks appear in logs, how analysts investigate suspicious activity, and how network or endpoint events can be used during an investigation.

In my phishing project, I focused on email-based threats, header analysis, suspicious domains, attachments, and indicators of compromise. That project helped me understand how attackers use social engineering and how analysts can identify suspicious email activity.

In my SIEM investigation project, I worked with Splunk and Elastic to investigate multi-stage attacks, Active Directory lateral movement, PowerShell activity, credential access, persistence, and ransomware impact. That project gave me a stronger understanding of how different log sources can be correlated to reconstruct an attack timeline.

In my firewall project, I focused on firewall concepts, rule direction, traffic filtering, Windows Defender Firewall, and how network controls can reduce attack surface.

After completing those projects, I wanted to move one step further and focus on how detections are created, tested, tuned, and improved. This repository is focused on that part of SOC work.

The main goal of this repository is to understand how suspicious behaviour can be converted into useful detection logic.

## Repository Focus

This repository focuses on:

* Detection engineering fundamentals
* Detection types
* Detection as Code
* Tactical detection development
* Threat intelligence for SOC
* Sigma rule writing
* Detection validation
* Endpoint detection with EDR telemetry
* SOAR concepts and response automation

The purpose is not only to collect notes, but also to understand how detections are built from real attacker behaviour and how they can support SOC analysts during alert triage and investigations.

## Why I Created This Repository

During my previous SIEM and threat hunting investigations, I mostly focused on answering questions such as:

* What happened?
* Which host was affected?
* Which user account was involved?
* What command was executed?
* Which technique did the attacker use?
* What was the impact?

Detection engineering adds another important question:

* How can this activity be detected earlier next time?

That is why I created this repository.

I wanted to understand how detection rules are planned, written, tested, tuned, and maintained. A detection should not only generate an alert. It should provide useful context, reduce unnecessary noise, and help analysts focus on real threats.

## Repository Structure

### 01 - Detection Engineering Fundamentals

This section introduces the main concepts of detection engineering, including detection types, environment-based detection, threat-based detection, and Detection as Code.

### 02 - Tactical Detection

This section focuses on converting attacker behaviour into detection logic. The main focus is understanding how analysts can detect suspicious activity based on techniques, tools, and behaviours instead of relying only on static indicators.

### 03 - Threat Intelligence for SOC

This section covers how threat intelligence can support SOC operations and detection development. It focuses on IOCs, TTPs, threat actor behaviour, and intelligence-driven detection.

### 04 - Sigma

This section focuses on Sigma rule writing and vendor-neutral detection logic. The goal is to understand how Sigma rules are structured and how they can be used across different SIEM platforms.

### 05 - SigHunt

This section focuses on using Sigma rules and detection logic for hunting activity. It connects detection engineering with threat hunting.

### 06 - Aurora EDR

This section focuses on endpoint detection concepts and EDR telemetry. The main objective is to understand how endpoint events can help detect suspicious process activity, command-line behaviour, and attacker techniques.

### 07 - Introduction to SOAR

This section introduces SOAR concepts, including playbooks, alert enrichment, response automation, and case management.

## Skills Practiced

Throughout this repository, I practiced and documented concepts related to:

* SOC analysis
* Detection logic
* Alert triage
* Log source selection
* Detection tuning
* False positive analysis
* MITRE ATT&CK mapping
* Sigma rule structure
* Threat intelligence usage
* Endpoint detection concepts
* SOAR workflow basics

## Previous Related Projects

This repository builds on my previous SOC and cybersecurity projects:

* **SOC Phishing Case Studies**
  Focused on phishing analysis, email headers, suspicious attachments, malicious URLs, and IOC extraction.

* **SIEM Investigation Case Studies**
  Focused on Splunk and Elastic investigations, multi-stage attacks, lateral movement, credential access, persistence, and ransomware activity.

* **Firewall Fundamentals**
  Focused on firewall concepts, traffic filtering, rule direction, network controls, and reducing attack surface.

These projects helped me build a foundation in investigation and analysis. This repository continues from that foundation and focuses more on detection creation and improvement.

## Main Takeaway

The main takeaway from this repository is that detection engineering is not only about writing alert rules.

A good detection should be based on attacker behaviour, reliable log sources, clear logic, and continuous improvement. It should be tested, tuned, and updated as the environment and attacker techniques change.

This repository helped me understand how SOC analysts can move from only investigating alerts to thinking about how those alerts are created and how they can be improved.
