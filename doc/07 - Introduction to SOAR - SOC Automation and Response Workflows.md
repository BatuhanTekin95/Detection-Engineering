# 07 - Introduction to SOAR: SOC Automation and Response Workflows

## Introduction

Security Operations Centers use different security tools to monitor, detect, investigate, and respond to threats. These tools may include SIEM, EDR, firewalls, threat intelligence platforms, IAM systems, and ticketing solutions.

However, as environments grow and threats become more complex, SOC teams can face several operational challenges. Analysts may need to handle a high number of alerts, move between disconnected tools, perform repetitive manual tasks, and coordinate with IT or management teams during incidents.

This room focused on how **Security Orchestration, Automation, and Response (SOAR)** can help SOC teams improve investigation and response workflows.

From a SOC analyst point of view, SOAR is useful because it can connect different tools, automate repetitive actions, support playbooks, and help analysts respond to incidents more consistently.

## Traditional SOC Operations

A traditional SOC is responsible for monitoring an organisation’s environment, detecting suspicious activity, investigating alerts, and supporting incident response.

SOC teams usually rely on a combination of people, processes, and technologies. The main goal is to improve security visibility, detect threats early, and respond before incidents cause more serious damage.

Some important SOC capabilities include:

| Capability | Description |
|---|---|
| **Monitoring and Detection** | Identifying suspicious activity through logs, alerts, SIEM rules, EDR detections, and other monitoring tools. |
| **Recovery and Remediation** | Taking action after a threat is identified, such as isolating endpoints, blocking malicious IP addresses, disabling accounts, or removing malware. |
| **Threat Intelligence** | Using indicators, reports, and threat data to improve detection, investigation, and response decisions. |
| **Communication** | Coordinating with IT, management, and other teams to make sure incidents are handled properly. |

In a real SOC environment, these activities often require analysts to use multiple tools and communicate with different teams. This can make the response process slower if the workflow is not well organised.

## Challenges Faced by SOC Teams

SOC teams can face several challenges when handling alerts and incidents manually.

| Challenge | Explanation |
|---|---|
| **Alert Fatigue** | A large number of alerts can overwhelm analysts, especially when many alerts are false positives or low priority. |
| **Too Many Disconnected Tools** | Security tools may operate separately, forcing analysts to switch between SIEM, EDR, firewall, IAM, threat intelligence, and ticketing platforms during a single investigation. |
| **Manual Processes** | Repetitive investigation and response steps can slow down analysts and increase the chance of mistakes. |
| **Talent Shortage** | SOC teams may not always have enough experienced analysts to handle the growing number of alerts and responsibilities. |

<img width="524" height="606" alt="Challenges Faced by SOC Teams screenshot" src="https://github.com/user-attachments/assets/23c06d0d-d7ed-4eb0-8577-b5e2eda18f3c" />

> This image shows common SOC challenges such as alert fatigue, disconnected tools, manual processes, and overloaded analysts.

These challenges can increase investigation time and make incident response less efficient. This is where SOAR becomes valuable.

## Why SOAR is Needed

SOAR helps SOC teams by connecting security tools, automating repetitive tasks, and standardising response processes through playbooks.

For example, instead of manually checking an IP address in multiple tools, a SOAR platform can automatically enrich the indicator using threat intelligence sources, create a ticket, notify the analyst, and suggest response actions.

This can help SOC teams:

* Reduce repetitive manual work
* Improve response consistency
* Speed up alert triage
* Connect disconnected security tools
* Support incident response playbooks
* Improve communication between teams

From an analyst point of view, SOAR does not replace human decision-making. Instead, it helps analysts work faster by automating repetitive steps and giving them better context during investigations.

## What is SOAR?

Security Orchestration, Automation, and Response (SOAR) is a security solution that helps SOC teams connect different security tools and manage investigation and response workflows from a more centralised platform.

Instead of switching manually between SIEM, EDR, firewalls, IAM, threat intelligence platforms, and ticketing systems, SOAR can bring these tools together into a single workflow.

SOAR is useful because it can help analysts:

* Collect alert information from different tools
* Enrich indicators with threat intelligence
* Create and update tickets
* Execute predefined response actions
* Follow structured playbooks
* Reduce repetitive manual work

From a SOC analyst point of view, SOAR improves consistency. It allows common investigation and response steps to be documented, repeated, and automated through playbooks.


<img width="1231" height="719" alt="What is SOAR? screenshot" src="https://github.com/user-attachments/assets/b4113db4-41a6-46ef-b460-0e8272b6460e" />

> This image shows how SOAR connects tools such as SIEM, threat intelligence feeds, firewalls, IDS, and IAM systems to support automated response, reduced alert fatigue, and consistent workflows.

## Core SOAR Capabilities

SOAR is commonly built around three core capabilities:

* Orchestration
* Automation
* Response

These capabilities help SOC teams reduce manual work, improve response speed, and make investigation workflows more consistent.

### 1. Orchestration

Orchestration means connecting different security tools and making them work together inside a single workflow.

In a traditional SOC, an analyst may need to investigate one alert by manually checking several different platforms. For example, during a VPN brute-force investigation, the analyst may need to:

* Check SIEM logs for login activity
* Review threat intelligence sources for IP reputation
* Use IAM tools to check or disable the user account
* Open a ticket in the ticketing system
* Communicate with IT or management teams

This manual switching between tools can slow down the investigation process.

With SOAR, these tools can be connected through a playbook. A playbook is a predefined workflow that tells the SOAR platform which steps should be taken during a specific type of alert or incident.

For example, a VPN brute-force playbook may include:

* Receive an alert from the SIEM
* Query SIEM logs to check the user’s normal login behaviour
* Check threat intelligence sources for the source IP reputation
* Review whether there were any successful logins
* Escalate to containment actions if needed

Orchestration is important because it brings different security tools into the same investigation flow.

### 2. Automation

Automation means executing repetitive investigation or response steps without requiring the analyst to perform every action manually.

For example, instead of manually checking an IP address in several tools, SOAR can automatically:

* Receive the alert from the SIEM
* Query historical login activity
* Check the IP address reputation
* Add context to the alert
* Open or update a ticket
* Suggest or execute response actions

This helps reduce the time spent on repetitive tasks and allows analysts to focus on decisions that require human judgement.

Automation is especially useful for high-volume and repetitive alerts, where the same steps need to be performed again and again.

### 3. Response

Response refers to the actions taken after suspicious or malicious activity is identified.

SOAR can support response actions by triggering predefined steps across connected tools. For example, in a suspicious VPN login case, SOAR may help:

* Block a malicious IP address on the firewall
* Disable or lock a user account in IAM
* Isolate an endpoint through EDR
* Create a ticket with all investigation details
* Notify the relevant teams

Response actions should still be controlled carefully. Some actions can be fully automated, while others may require analyst approval before execution.

From an analyst point of view, SOAR does not remove the need for investigation. It helps make the response process faster, more organised, and more consistent.

<img width="1219" height="713" alt="3. Response screenshot" src="https://github.com/user-attachments/assets/7622c583-3f31-44ed-8e9b-129fde095834" />

> This image compares SOC operations before and after SOAR. SOAR helps connect tools, reduce alerting noise, automate response steps, and support faster containment.

## Do We Still Need SOC Analysts?

SOAR can automate many repetitive tasks, but it does not replace SOC analysts.

Complex investigations still require human judgement, context, and decision-making. A SOAR playbook can collect information, enrich alerts, and perform predefined actions, but an analyst still needs to understand the business context, assess risk, and decide whether the activity is truly malicious.

SOC analysts are still needed to:

* Review complex or high-risk alerts
* Build and improve playbooks
* Validate automated actions
* Investigate unusual activity
* Make decisions when context is unclear
* Coordinate with other teams during incidents

SOAR reduces analyst workload, but it works best when analysts design, review, and improve the workflows behind it.

## SOAR Playbooks

A SOAR playbook is a predefined workflow that tells the SOAR platform which actions should be taken during a specific type of alert or incident.

Playbooks help SOC teams standardise investigation and response steps. Instead of relying only on manual actions or analyst memory, the process can be documented and repeated in a consistent way.

In this room, two playbook examples were reviewed:

* Phishing Playbook
* CVE Patching Playbook

These examples showed how SOAR can automate repetitive steps while still keeping SOC analysts involved in important decision points.

## Phishing Playbook

Phishing investigations can be time-consuming because analysts often need to review emails, check URLs, inspect attachments, verify indicators through threat intelligence platforms, and decide whether remediation is required.

A SOAR phishing playbook can help automate many of these steps.

For example, when a suspicious email is received, the playbook may:

* Create an investigation ticket
* Check whether the email contains URLs or attachments
* Compute hashes for attachments
* Send hashes or URLs to threat intelligence platforms such as VirusTotal
* Decide whether the indicator appears malicious
* Escalate suspicious emails for manual sandbox analysis if needed
* Delete malicious emails
* Update the investigation ticket with discovered IOCs
* Notify users or teams when required

From a SOC analyst point of view, this is useful because the repetitive enrichment and checking steps can be automated, while the analyst can still review complex or unclear cases.

<img width="1434" height="1140" alt="Phishing Playbook screenshot" src="https://github.com/user-attachments/assets/a370face-d24f-4eab-b28a-81d72b80f373" />

> This playbook shows how SOAR can handle a suspicious email by checking attachments and URLs, enriching indicators, updating tickets, and triggering remediation actions when malicious content is identified.

## CVE Patching Playbook

The second example focused on CVE patching.

A CVE is a publicly disclosed vulnerability with an assigned identifier. In a SOC or vulnerability management workflow, newly released CVEs need to be reviewed to understand whether they affect the organisation’s environment.

Without automation, this process can become difficult because analysts may need to manually monitor advisories, check whether the CVE applies to internal assets, create tickets, test patches, deploy updates, and verify remediation.

A SOAR CVE patching playbook can help organise this workflow.

A typical CVE patching playbook may include:

* Monitor advisory lists for new CVEs
* Extract new CVE data
* Check whether the CVE has already been addressed
* Query patch management tools to see whether the CVE applies
* Create a CVE ticket and assign it to an analyst
* Identify assets that need patching
* Check whether a patch exists
* Test the patch on test machines
* Deploy the patch to affected assets
* Verify patch rollout
* Run vulnerability scans after deployment
* Create a mitigation plan if the asset is still vulnerable
* Update and close the ticket when remediation is complete

This playbook shows that SOAR is not only useful for alert triage. It can also support vulnerability management, patch tracking, and remediation workflows.

> The original CVE patching playbook was very wide, so I summarised the main workflow steps instead of adding the full diagram.

## Conclusion

This room showed how SOAR can improve SOC workflows by connecting tools, automating repetitive tasks, and standardising response processes through playbooks.

The main value of SOAR is not replacing SOC analysts, but helping them work more efficiently. SOAR can collect context, enrich indicators, create tickets, and execute predefined actions, while analysts remain responsible for judgement, validation, and complex decision-making.

The phishing and CVE patching examples showed how playbooks can reduce manual work, improve consistency, and support faster investigation, remediation, and response across different SOC workflows.

## Training Context

These notes and screenshots were produced while completing a guided detection engineering training lab. The summaries and analyst observations document my own understanding of the concepts and practical tasks.
