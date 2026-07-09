# Detection Engineering Fundamentals

## Introduction

Detection engineering is an important part of modern SOC operations because attackers are constantly changing their techniques, tools, and behaviours. For this reason, security teams cannot rely only on static alerts or simple indicator-based detections.

In this section, I focused on understanding how detections are created, what types of detections exist, and why detection logic needs to be tested, tuned, and maintained over time.

The main objective was to understand the difference between environment-based detection and threat-based detection, and how Detection as Code can help security teams manage detections in a more structured way.

## Detection Engineering

Detection engineering is the process of building and maintaining detections that help identify malicious activity, suspicious behaviour, or misconfigurations inside an environment.

A detection is not just an alert. It should be based on clear logic, useful log sources, and an understanding of what the attacker is trying to achieve.

From a SOC perspective, a good detection should help analysts answer questions such as:

* What behaviour is suspicious?
* Which log source can show this activity?
* Is the alert based on an indicator, a configuration issue, or attacker behaviour?
* Could this alert create false positives?
* How can the detection be tested and improved?

This highlights that detection engineering is not only about writing rules. It also requires understanding the environment, attacker behaviour, and the quality of available telemetry. It also requires understanding the environment, attacker behaviour, and the quality of the available telemetry.

## Detection Types

Threat detection can be viewed from two main perspectives:

* Environment-based detection
* Threat-based detection

Environment-based detection focuses on changes, misconfigurations, and deviations inside the organization’s own infrastructure. Threat-based detection focuses more on attacker activity, indicators, tools, tactics, and behaviours.

Both approaches are useful, but they have different strengths and weaknesses. A strong detection strategy should not depend on only one type of detection.

## Configuration Detection

Configuration detection focuses on identifying misconfigurations or unexpected changes inside an environment. This can include network, asset, identity, or system configuration issues.

For example, if a critical system suddenly has a risky configuration change, this type of detection can help identify it.

The main advantage of configuration detection is that it can be easier to create and maintain in static environments. It can also be useful when the organization already knows what the correct configuration should look like.

However, this approach can become difficult in dynamic environments where configurations change frequently. If the baseline is not accurate, this can create too many false positives.

From an analyst point of view, I think this detection type is useful, but it depends heavily on knowing the environment well.

## Modelling

Modelling is based on defining normal activity and detecting deviations from that baseline.

This means the environment must first understand what normal behaviour looks like. After that, unusual activity can be detected when it moves away from the expected pattern.

For example, if a user normally logs in during business hours but suddenly authenticates from an unusual location or at an unusual time, this could be detected as a deviation.

The benefit of this approach is that it can help identify unknown attacker activity that does not match a known indicator.

However, one challenge is that modelling requires a clean and accurate baseline. If malicious activity already exists during the baseline period, there is a risk that bad behaviour may be accepted as normal.

This shows that baselining is powerful, but it must be handled carefully.

## Indicator Detection

Indicator detection focuses on known indicators of compromise such as malicious IP addresses, domains, hashes, filenames, or URLs.

This is one of the fastest detection types to create and deploy because it uses known information from previous investigations or threat intelligence.

For example, if a malicious domain is discovered during an investigation, a detection can be created to alert when any host communicates with that domain again.

Indicator-based detection is useful for quick response and scoping, but it has limitations. Attackers can easily change infrastructure, rotate domains, or modify file hashes.

Because of this, indicator detection is useful, but it should not be the only detection approach in a SOC environment.

## Threat Behaviour Detection

Threat behaviour detection focuses on the attacker’s tactics, techniques, and procedures instead of only looking for specific indicators.

This type of detection is more scalable because attacker behaviour is usually harder to change than a domain, IP address, or file hash.

For example, instead of only detecting a known malicious PowerShell script, a behaviour-based detection can look for suspicious PowerShell patterns such as encoded commands, remote script execution, or unusual parent-child process relationships.

This approach is stronger because it focuses on how attackers operate.

However, behaviour-based detection usually requires more telemetry and a better understanding of attacker techniques. It can also require more tuning during the first implementation.

From my point of view, this is one of the most important detection types for SOC analysts because it is closer to real attacker activity.

## Detection Types Summary

| Detection Type             | Main Focus                                        | Main Limitation                                    |
| -------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| Configuration Detection    | Misconfigurations and unexpected changes          | Can create false positives in dynamic environments |
| Modelling                  | Deviations from normal baseline activity          | Requires an accurate and clean baseline            |
| Indicator Detection        | Known IOCs such as IPs, domains, hashes, and URLs | Indicators can expire or change quickly            |
| Threat Behaviour Detection | Attacker TTPs and suspicious behaviour            | Requires more telemetry and tuning                 |

## Detection as Code

Detection as Code is a structured way of writing and managing detection logic like software code.

Instead of creating alerts manually inside a SIEM without proper tracking, Detection as Code allows teams to use software engineering practices such as version control, testing, review, and deployment workflows.

This approach makes detections easier to maintain and improve over time.

Some important parts of Detection as Code include:

* Version control
* Testing detection logic
* Reviewing changes before deployment
* Deploying detections to staging before production
* Tuning and updating detections after testing

<img width="3834" height="3714" alt="d5dcb2327fef9f42f4958212efb5dd2c" src="https://github.com/user-attachments/assets/30c39a01-1f78-4dcf-9cb0-daa700304be8" />

> The Detection as Code workflow helped me understand that detections should not be treated as one-time rules. They need to be tested, updated, and improved as the environment and attacker behaviours change.

## Detection Types Notes

The most important point I learned from this section is that every detection type has advantages and limitations.

Indicator-based detections are fast to create, but they can become outdated quickly.

Behaviour-based detections are stronger against changing attacker infrastructure, but they require more log data and more tuning.

Configuration and modelling detections can be useful for identifying environmental changes, but they depend on having accurate knowledge of the infrastructure.

Because of this, a strong detection strategy should combine multiple detection types instead of relying on only one approach.

This section also helped me understand why detection quality matters. A detection that creates too many false positives can waste analyst time, while a detection that is too narrow may miss real attacker activity.


## Detection Engineering Workflow

After understanding the main detection types, I also looked at the general workflow used to build, test, deploy, and improve detections.

Detection engineering is not a single-step process. It starts with identifying detection gaps, continues with selecting the right data sources, and then moves into writing, testing, deploying, and tuning detection rules.

## Detection Gap Analysis

The first step is identifying areas where the organization can improve its detection coverage. This process is also related to threat modelling because analysts need to understand which threats, attack paths, and TTPs may affect the environment.

Detection gap analysis can be done in two ways:

* **Reactive:** Reviewing previous incidents and identifying what was missed during detection or response.
* **Proactive:** Using frameworks such as MITRE ATT&CK and threat intelligence sources to identify possible attacker behaviours before an incident happens.

This helped me understand that detections should not only be created after an incident. They can also be planned proactively based on likely attacker techniques and known gaps in the environment.

## Data Source Identification and Log Collection

After identifying possible threats and detection gaps, the next step is choosing the right data sources.

A detection is only useful if the required logs are available. For example, suspicious PowerShell activity may require process creation logs, command-line logging, or PowerShell script block logs. Network-based activity may require firewall, proxy, DNS, or IDS logs.

This part showed me that log source selection is one of the most important parts of detection engineering. If the right telemetry is missing, even a well-written detection rule may not work properly.

Once the required data sources are identified, logs and metadata should be collected from relevant systems. Depending on the environment, this can include endpoint logs, network logs, authentication logs, Sysmon events, firewall logs, and SIEM data.

## Baseline Creation

Before detecting abnormal activity, analysts need to understand what normal behaviour looks like inside the environment.

Baseline creation helps define expected activity for users, systems, applications, and network traffic. This can include normal login times, common processes, usual network connections, expected administrative actions, and standard system configurations.

Security baselines can be grouped into two categories:

* **High-level baselines:** Broad standards based on security policies.
* **Technical baselines:** More detailed configuration and activity standards based on operating systems, network behaviour, IAM policies, and application activity.

This helped me understand why baselining is important before creating detections. Without a baseline, it can be difficult to decide whether an event is actually suspicious or just normal activity for that environment.

## Rule Writing

After the required data sources and baselines are identified, detection rules can be written and tested against the available logs.

Detection rules are used to identify abnormal patterns in logged events. Depending on the environment, different rule types may be used. For example, Snort rules can be used for network traffic, YARA rules can be used for file detection, and Sigma rules can be used for log-based detections.

In this repository, I focused more on Sigma because it provides a generic way to write detection logic that can be adapted to different SIEM platforms.

This part helped me understand that rule writing should be based on clear detection logic. A rule should not only look for suspicious activity, but also provide enough context for analysts to investigate the alert properly.

## Deployment, Automation and Tuning

After a detection rule is written and tested, it needs to be deployed and monitored in a live environment.

However, deploying a detection is not the final step. Over time, detections need to be reviewed, tuned, and updated because attacker techniques, infrastructure, and normal business activity can change.

This part helped me understand that detection engineering is an ongoing process. A detection that works well today may become noisy, outdated, or ineffective later if it is not maintained.

Tuning is also important for reducing false positives. If a detection creates too much noise, analysts may start ignoring alerts. Because of this, detection quality is as important as detection coverage.

## Workflow Summary

| Step                       | Purpose                                                                      |
| -------------------------- | ---------------------------------------------------------------------------- |
| Detection Gap Analysis     | Identify missing detection coverage                                          |
| Data Source Identification | Decide which logs are required                                               |
| Log Collection             | Collect useful telemetry from endpoints, network devices, and security tools |
| Baseline Creation          | Understand normal activity before detecting abnormal behaviour               |
| Rule Writing               | Create detection logic based on suspicious patterns                          |
| Testing                    | Validate whether the rule works as expected                                  |
| Deployment                 | Move the detection into production                                           |
| Tuning                     | Reduce false positives and improve detection quality over time               |

## Analyst Notes

The most important point I learned from this workflow is that detection engineering starts before writing a rule.

If the threat is not understood, the right data source is not selected, or the baseline is not clear, the detection may not provide useful results. A good detection needs context, reliable telemetry, and continuous tuning.

This workflow also showed me that detections should be treated as living content. They need to be reviewed and improved as the environment changes and attackers adapt their techniques.


## Frameworks Used in Detection Engineering

After reviewing the detection engineering workflow, I also looked at several frameworks that can help analysts understand attacker behaviour and improve detection coverage.

These frameworks are useful because detection engineering is not only about writing rules. Analysts also need to understand how attackers move through an environment, which techniques they use, and which behaviours are more valuable to detect.

## MITRE ATT&CK and CAR Frameworks

MITRE ATT&CK is one of the most useful frameworks for mapping attacker behaviour. It organizes adversary activity into tactics and techniques such as Initial Access, Execution, Persistence, Credential Access, Lateral Movement, Exfiltration, and Impact.

From a detection engineering perspective, ATT&CK helps analysts understand what to look for when building detections. Instead of only focusing on individual indicators, analysts can map detection logic to specific attacker techniques.

For example, if an attacker uses PowerShell for execution, this activity can be mapped to the Execution tactic. If the attacker dumps credentials from LSASS, this can be mapped to Credential Access.

The Cyber Analytics Repository, also known as CAR, can also support detection engineering by providing analytics related to ATT&CK techniques.

<img width="1634" height="609" alt="3002249bee56ca5ab666e92e461cdb48" src="https://github.com/user-attachments/assets/048f7e4d-076f-4b17-984e-575420ab762b" />

> The image shows the MITRE ATT&CK matrix. It helped me understand how attacker tactics and techniques can be mapped during detection gap analysis and detection planning.


## Pyramid of Pain

The Pyramid of Pain shows how difficult it is for an attacker to change different types of indicators when defenders detect them.

At the bottom of the pyramid, hash values and IP addresses are easier for attackers to change. At the top of the pyramid, tools and TTPs are harder to change.

This is important for detection engineering because it explains why behaviour-based detection is stronger than relying only on simple indicators.

For example, detecting a malicious IP address can be useful, but the attacker can quickly change that IP address. However, detecting attacker behaviour such as suspicious PowerShell execution, credential dumping, or lateral movement patterns creates more pressure on the attacker.

<img width="1012" height="800" alt="bcf0b565e7be2702dc3a2e2c46c6054b" src="https://github.com/user-attachments/assets/aee8ab59-e4fd-4f8b-a9e4-9e4ed89d9f0e" />

> The image shows why detections based on tools and TTPs create more difficulty for attackers than detections based only on hashes, IP addresses, or domains.

From my point of view, this framework clearly explains why SOC teams should not only depend on IOCs. IOCs are useful for quick detection and scoping, but detections based on attacker behaviour usually provide better long-term value.

## Cyber Kill Chain

The Cyber Kill Chain explains the common phases of an attack from the attacker’s preparation stage to their final objective.

The main phases are:

* Reconnaissance
* Weaponization
* Delivery
* Exploitation
* Installation
* Command and Control
* Actions on Objectives

This framework helps analysts understand where an attacker is in the attack lifecycle. It can also help detection engineers decide where detections should be placed.

For example, detections can be created for suspicious delivery methods, exploitation attempts, malware installation, command and control communication, or final impact activity.

<img width="920" height="456" alt="491cbe4c1851ca69aea2a387e5525321" src="https://github.com/user-attachments/assets/3728bbe8-e54a-4c19-ad08-a2980c0829f9" />

> The image shows the main phases of the Cyber Kill Chain. It helped me understand how an attacker can move from reconnaissance to final objectives, and how detections can be planned across different stages of an attack.


## Unified Kill Chain

The Unified Kill Chain expands the original Cyber Kill Chain by combining it with other frameworks such as MITRE ATT&CK.

It provides a more detailed view of an intrusion by covering more phases across the full attack lifecycle.

This is useful because real attacks do not always follow a simple linear path. Attackers may move between discovery, privilege escalation, lateral movement, credential access, collection, exfiltration, and impact.

The Unified Kill Chain helped me understand that detection coverage should exist across multiple stages of an attack, not only at the initial access or impact phase.

<img width="1051" height="678" alt="f78d42cc461eaebffd806666646f6cbb" src="https://github.com/user-attachments/assets/30204350-2214-414e-8855-fc71eb038d1e" />

> The image shows the 18 phases of the Unified Kill Chain. It helped me understand that real intrusions can involve many stages such as persistence, defense evasion, pivoting, discovery, privilege escalation, credential access, lateral movement, exfiltration, and impact.

## Framework Summary

| Framework          | Main Purpose                                               | Detection Engineering Value                                     |
| ------------------ | ---------------------------------------------------------- | --------------------------------------------------------------- |
| MITRE ATT&CK       | Maps attacker tactics and techniques                       | Helps map detections to real attacker behaviour                 |
| CAR                | Provides analytics related to ATT&CK techniques            | Supports detection logic and analytics development              |
| Pyramid of Pain    | Shows how difficult indicators are for attackers to change | Explains why behaviour-based detection is valuable              |
| Cyber Kill Chain   | Describes the main phases of an attack                     | Helps understand where detections can be placed                 |
| Unified Kill Chain | Expands the attack lifecycle into more detailed phases     | Helps improve detection coverage across the full intrusion path |

## Analyst Notes

The most important point I learned from these frameworks is that detection engineering becomes stronger when it focuses on attacker behaviour rather than only static indicators.

Indicators such as IP addresses, domains, and hashes are useful for quick detection and scoping, but attackers can change them quickly. Techniques and behaviours are harder to change, so detecting them can create more difficulty for the attacker.

These frameworks also help during detection gap analysis because they allow analysts to ask better questions:

* Which ATT&CK techniques are currently covered?
* Which attack phases have weak visibility?
* Are we detecting only indicators, or also attacker behaviour?
* Do we have enough telemetry to detect activity across the full attack chain?

These frameworks are not only theoretical. They can directly support detection planning, rule writing, threat hunting, and SOC investigations.


## Alerting and Detection Strategy Framework

I also reviewed the Alerting and Detection Strategy Framework, which provides a structured way to document detection content before publishing it into production.

This framework helped me understand that a detection should not be created only as a simple rule. It should also include the reason for the alert, the related attacker behaviour, the technical context, possible blind spots, false positives, validation steps, priority, and response guidance.

The main stages of the framework are:

* **Goal:** Defines why the alert is being created and what behaviour it is expected to detect.
* **Categorisation:** Maps the detection to frameworks such as MITRE ATT&CK so analysts can understand the related tactics and techniques.
* **Strategy Abstract:** Provides a high-level explanation of what the detection looks for, which data sources are required, and how false positives can be reduced.
* **Technical Context:** Describes the technical environment where the detection will be used.
* **Blind Spots and Assumptions:** Identifies where the detection may fail, where visibility may be limited, or how an adversary may bypass the detection.
* **False Positives:** Documents non-malicious activities that may trigger the alert.
* **Validation:** Explains how the detection can be tested to confirm that it produces a true-positive alert.
* **Priority:** Defines the importance of the alert and helps analysts understand how quickly it should be handled.
* **Response:** Provides guidance for triaging and investigating the alert.

<img width="1140" height="665" alt="28b4c33f004df15d26ae8d5b2862b445" src="https://github.com/user-attachments/assets/b9473b6e-f205-4cfe-8ab3-0f68fbfbce4d" />

> The image shows the main stages of the Alerting and Detection Strategy Framework. It helped me understand that a detection should include not only the alert logic, but also its goal, categorisation, technical context, blind spots, false positives, validation steps, priority, and response guidance.

From my point of view, this framework is useful because it forces the detection engineer to think beyond the rule itself. A detection should be understandable, testable, and useful for the analyst who will investigate the alert later.

It also showed me that documentation is an important part of detection engineering. If an alert does not explain its goal, context, blind spots, and response steps clearly, it can create confusion during triage.

## Detection Maturity Level Model

The Detection Maturity Level model helps assess how mature an organization’s detection capability is.

This model shows that detection maturity is not only about collecting threat intelligence. The important part is how well an organization can apply that intelligence to detection and response.

The model starts from no detection capability and moves toward more abstract and intelligence-driven detection. Lower levels focus more on simple indicators and artefacts, while higher levels focus on attacker procedures, techniques, tactics, strategy, and goals.

| Level                          | Focus                                                          |
| ------------------------------ | -------------------------------------------------------------- |
| DML-0 None                     | No detection process is established                            |
| DML-1 Atomic Indicators        | Detection based on indicators such as IP addresses and domains |
| DML-2 Host & Network Artefacts | Detection based on host and network artefacts                  |
| DML-3 Tools                    | Detection of attacker tools and their functionality            |
| DML-4 Procedures               | Detection of sequences of attacker actions                     |
| DML-5 Techniques               | Detection of specific attacker techniques                      |
| DML-6 Tactics                  | Detection of broader attacker tactics                          |
| DML-7 Strategy                 | Understanding the attacker’s strategy and intent               |
| DML-8 Goals                    | Understanding what the adversary wants to achieve              |


This model helped me understand why mature detection programs should move beyond simple indicators.

Detecting IP addresses, domains, or hashes can be useful, but these are easier for attackers to change. Higher maturity detections focus more on tools, procedures, techniques, tactics, and attacker goals.

From a SOC perspective, this is important because mature detections can provide better context for analysts and help security teams respond to attacker behaviour more effectively.

## Analyst Notes

The main point I learned from these models is that detection quality depends on documentation, validation, and maturity.

The Alerting and Detection Strategy Framework helps document a detection properly before it is deployed. It makes the detection easier to understand, test, investigate, and maintain.

The Detection Maturity Level model helps show how advanced a detection capability is. It also explains why detections based only on atomic indicators are limited compared to detections based on attacker behaviour, techniques, and tactics.

Together, these models showed me that detection engineering is not only about creating alerts. It is also about building detections that are documented, tested, understandable, and useful during real investigations.


## Practical ADS Framework Example: Privileged Account and Group Changes

After reviewing the ADS Framework, I worked on a small scenario focused on detecting changes made to privileged and administrative accounts and groups in Active Directory.

The objective of this scenario was to understand how the ADS Framework can be used to document a detection strategy before publishing it into production.

| ADS Stage                   | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Goal                        | Detect changes made to privileged and administrative groups or accounts in Active Directory.                                                                                                                                                                                                                                                                                                                       |
| Categorisation              | Account Manipulation                                                                                                                                                                                                                                                                                                                                                                                               |
| Strategy Abstract           | Collect and monitor Windows Security Event Logs related to Active Directory group membership changes and privileged account modifications.                                                                                                                                                                                                                                                                         |
| Technical Context           | Active Directory groups can control access to sensitive systems and administrative privileges. If an attacker adds a user to a privileged group, modifies an admin account, or abuses an existing privileged account, this can lead to privilege escalation and wider compromise. Useful telemetry may include Windows Security logs from Domain Controllers and SIEM events related to account and group changes. |
| Blind Spots and Assumptions | Domain Controller security logs are being collected, auditing is enabled, and logs are forwarded to the SIEM successfully. The detection may miss activity if logging is disabled, events are not forwarded, or changes are made through unsupported systems.                                                                                                                                                      |
| False Positives             | Legitimate administrative changes, planned IAM operations, helpdesk activity, automated provisioning, or approved group membership updates may trigger the alert.                                                                                                                                                                                                                                                  |
| Validation                  | Add or remove a test user from a privileged group in a lab environment and confirm that the expected Windows Security Event is generated and detected by the SIEM rule.                                                                                                                                                                                                                                            |
| Priority                    | High                                                                                                                                                                                                                                                                                                                                                                                                               |
| Response                    | Validate the group modified, the user added or removed, and the user account that made the change. Check whether the change was approved. If the activity is suspicious, investigate recent logons, related account activity, and possible privilege escalation attempts.                                                                                                                                          |

## Analyst Notes

This example helped me understand how the ADS Framework can turn a detection idea into a documented detection strategy.

Instead of only saying “alert on privileged group changes,” the framework forces the analyst to think about the goal, categorisation, data sources, assumptions, false positives, validation steps, priority, and response actions.

From a SOC perspective, this is important because privileged group changes can have a direct impact on domain security. If an attacker adds a controlled account to an administrative group, they may gain higher privileges and continue the attack with more access.

This scenario also showed me why response guidance matters. When this type of alert triggers, the analyst should not only look at the changed group. They should also validate who made the change, whether it was approved, and whether the account was used for suspicious activity before or after the modification.


## Conclusion

This section covered the foundation of detection engineering and showed how different detection approaches can be used inside a SOC environment.

Detection engineering is not only about creating alerts. It also includes understanding attacker behaviour, choosing the right log sources, reducing false positives, testing detection logic, and maintaining detections over time.

The main takeaway from this section is that effective detections should be clear, testable, and adaptable. A detection that is not maintained can quickly become noisy or outdated, especially as attackers change their techniques and infrastructure.










