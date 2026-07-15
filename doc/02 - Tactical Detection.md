# 02. Tactical Detection

## Introduction

Modern Security Operations Centers (SOCs) often use default detection rules provided by security tools. These rules can give basic visibility, but they may not always match an organization’s own environment, threat landscape, or previous incident history.

**Tactical Detection** focuses on creating practical detections based on real threats, previous incidents, known Indicators of Compromise (IOCs), and environment-specific risks.

This section focuses on how threat intelligence and previous incident findings can be turned into actionable detection logic. The scenario shows how IOCs from a previous intrusion can be used to create detections that may help identify similar activity in the future.


## Tactical Detection Overview

Tactical detection is a practical part of detection engineering. It focuses on detections that are directly related to known threats, observed attacker activity, or previously identified indicators.

Instead of trying to detect every possible event, tactical detection prioritizes alerts that are relevant, actionable, and useful for investigation.

This type of detection can be built from:

* Previous incident findings
* Threat intelligence reports
* Known malicious infrastructure
* Indicators of Compromise
* Observed attacker behaviour
* Environment-specific risks

From a SOC perspective, tactical detection is useful because it allows analysts to turn investigation results into reusable detection content.

For example, if an investigation identifies a malicious domain, suspicious file name, IP address, or hash, these indicators can be used to create detections that alert analysts when similar activity appears again.

## IOC-Based Detection

Indicators of Compromise are pieces of evidence that may suggest malicious activity inside an environment.

Common examples of IOCs include:

* IP addresses
* Domain names
* URLs
* File names
* File hashes
* Email addresses
* Registry keys
* Process names

IOC-based detections are useful because they are usually quick to create and easy to understand. If a known malicious domain, hash, or file name appears again in the environment, the SOC team can investigate the activity more quickly.

However, IOC-based detections also have limitations. Attackers can change IP addresses, rotate domains, rename files, or modify file hashes. Because of this, IOC-based detection should not be the only detection method in a SOC environment.

IOCs are useful for quick detection and scoping, but stronger detection strategies should also include behaviour-based detections.

## Sigma Rule Development

Sigma is an open and vendor-agnostic rule format used to describe log-based detection logic.

Instead of writing a detection rule for only one SIEM platform, Sigma allows analysts to write detection logic in a more generic format. These rules can later be adapted or converted for different platforms such as Splunk, Elastic, Microsoft Sentinel, or other SIEM tools.

Sigma is useful because it makes detection rules more structured, reusable, and easier to share.

A Sigma rule usually includes important fields such as:

| Field              | Purpose                                 |
| ------------------ | --------------------------------------- |
| **title**          | Describes what the rule detects         |
| **description**    | Explains the purpose of the detection   |
| **logsource**      | Defines which logs are required         |
| **detection**      | Contains the detection logic            |
| **condition**      | Defines when the rule should trigger    |
| **falsepositives** | Lists possible benign causes            |
| **level**          | Indicates the severity of the detection |

A detection rule should not only contain search logic. It should also include context, required log sources, possible false positives, and severity information so analysts can understand why the alert matters.

## Detection Logic

Detection logic is the main part of a detection rule. It defines what activity should be considered suspicious and under which conditions an alert should be generated.

In tactical detection, detection logic is often created from known indicators or specific attacker behaviours.

For example, a detection may look for:

* A known malicious domain
* A suspicious file name
* A specific hash value
* A connection to attacker infrastructure
* A suspicious command-line pattern
* A process associated with malicious activity

Good detection logic should be clear, testable, and useful during investigation. If the logic is too broad, it may create too many false positives. If it is too narrow, it may miss related malicious activity.

Detection engineering requires balance. A detection should be specific enough to identify suspicious activity, but also practical enough to remain useful when attackers make small changes.

## Analyst Notes

A key point from this room is that tactical detection connects threat intelligence with practical SOC monitoring.

A detection rule should not be created only because an IOC exists. The analyst should also understand why the indicator is important, where it can appear in logs, and how it can support an investigation.

From an analyst point of view, useful tactical detections should answer questions such as:

* What indicator or behaviour are we trying to detect?
* Which log source can show this activity?
* Is this detection based on an IOC or behaviour?
* Could this alert create false positives?
* How can the detection be tested?
* What should the analyst investigate after the alert triggers?

Sigma adds value to detection engineering by providing a structured way to document detection logic and adapt rules across different SIEM platforms.


## Public Sigma Rules and Rule Conversion

After working with IOCs from a previous incident, I also reviewed how publicly available Sigma rules can be used in detection engineering.

In this part of the room, the idea was to take existing Sigma rules and convert them into SIEM-specific queries. This is useful because analysts do not always need to start from zero. When a new vulnerability or threat becomes public, the security community often shares detection rules that can be used as a starting point.

However, I also understood that public Sigma rules should not be used directly in production without review. Each rule should be checked, tested, and tuned according to the organization’s own environment.

## Using Uncoder for Sigma Conversion

Uncoder was used to convert Sigma rules into queries for different SIEM platforms such as Elastic Stack and Splunk.

The basic process was:

* Paste the Sigma rule into Uncoder.
* Select the target SIEM platform.
* Translate the rule.
* Review the generated query.
* Test and tune the query before using it in a real environment.

Tools like Uncoder can make the detection engineering process faster, but they do not remove the need for analyst review.

A converted rule may not work perfectly in every environment. Field names, log sources, parsing methods, and SIEM configurations can be different from one organization to another. Because of this, the converted query should be treated as a starting point, not as a final production-ready detection.

## Follina-MSDT Detection Example

One of the examples in this room was related to the Follina-MSDT vulnerability.

The Sigma rule was designed to detect suspicious `msdt.exe` execution related to Office exploitation. The rule used Windows process creation logs as the log source and focused on suspicious command-line arguments passed to the `msdt.exe` process.

From a detection point of view, this was a useful example because it showed how a known vulnerability can be turned into practical detection logic.

The rule focused on:

* `msdt.exe` execution
* Suspicious command-line arguments
* Office exploit behaviour
* Windows process creation events

Vulnerability-based detections often depend on process creation telemetry and command-line visibility. Without proper logging, this type of activity may be difficult to detect.

## Log4j Suspicious Shell Detection Example

Another example was related to Log4j exploitation.

The Sigma rule focused on suspicious shell processes spawned by a Java process. This example is important because it is more behaviour-based than simple IOC matching. In many environments, a Java process spawning shells or administrative tools can be suspicious and worth investigating.

The rule looked for cases where `java.exe` is the parent process and suspicious child processes are executed, such as:

* `sh.exe`
* `bash.exe`
* `powershell.exe`
* `pwsh.exe`
* `cmd.exe`
* `certutil.exe`
* `whoami.exe`
* `bitsadmin.exe`
* `wscript.exe`
* `cscript.exe`
* `regsvr32.exe`
* `mshta.exe`
* `rundll32.exe`
* `curl.exe`

From an analyst point of view, this detection is valuable because it focuses on attacker behaviour rather than only static indicators. Even if the attacker changes the payload, domain, or IP address, the behaviour of a Java process spawning suspicious system utilities can still be detected.

## Sigma Rule Analyst Notes

The main lesson from this part is that public Sigma rules can be very useful, but they should be adapted carefully.

A Sigma rule can provide the detection idea, but the analyst still needs to check:

* Does the environment collect the required logs?
* Are the field names compatible with the SIEM?
* Could the rule create false positives?
* Does the rule need allowlisting?
* Is the generated query actually working?
* Should the rule be adjusted for the organization’s normal activity?

This part shows the difference between copying a detection rule and engineering a detection. A copied rule may generate alerts, but an engineered detection should be tested, tuned, documented, and useful during investigation.

## Detection Engineering Takeaway

Sigma and tools like Uncoder can make detection development faster, but they are not a replacement for analyst thinking.

A good detection still needs:

* The right log source
* Clear detection logic
* Testing
* False positive review
* Environment-specific tuning
* Analyst investigation guidance

This section shows how public detection content can be transformed into practical SIEM detections and why every detection should be validated before being trusted in production.

## Tripwire Detection and Object Access Auditing

After working with IOC-based detections and Sigma rule conversion, I also looked at a more environment-focused detection approach: using tripwires.

A tripwire is a detection mechanism placed on a sensitive or unusual resource where normal user activity is not expected. If someone interacts with that resource, the activity can be treated as suspicious and investigated by the SOC team.

In this part of the room, the example focused on creating a basic file-based tripwire using a sensitive document. The idea was to monitor access to a file that normal users should not need to open, modify, or delete.

Detection engineering is not always about malware, IOCs, or exploit behaviour. Sometimes, a simple and well-placed monitoring rule can provide strong visibility into suspicious activity.

## Honeypots and Hidden Files

Tripwires can be used to detect activity that may otherwise be difficult to identify. Two common examples are honeypots and hidden files or folders.

A honeypot is a system or resource that has no legitimate business purpose. Because of this, any interaction with it can be considered suspicious.

Hidden files and folders can also be useful because normal users are not expected to access them. If a crawler, worm, attacker, or unauthorized user interacts with these files, it can create an alert and help analysts detect possible intrusion activity.

From an analyst point of view, this creates a simple detection opportunity. Instead of waiting for a known IOC or signature, the organization can place sensitive-looking resources and monitor unexpected access.

## Windows Event ID 4663

A key event in this part of the room was **Windows Security Event ID 4663**.

Event ID 4663 is generated when an attempt is made to access an object, such as a file or folder, when object access auditing is enabled.

This event can help analysts investigate:

* Which file or object was accessed
* Which user accessed it
* What type of access was requested
* Whether the action was successful
* When the activity occurred

From a SOC perspective, this is useful because access to a sensitive tripwire file can immediately give analysts something to investigate.


## Practical Lab: File-Based Tripwire with Windows Object Access Auditing

In this lab, I created a simple file-based tripwire by enabling Windows object access auditing and monitoring access to a sensitive-looking text file.

The goal was to understand how Windows Security logs can be used to detect access attempts against a monitored object.

### Step 1: Enabling Object Access Auditing

The first step was enabling **Audit object access** from Local Security Policy. I configured the policy to log both successful and failed access attempts.

<img width="418" height="507" alt="Step 1: Enabling Object Access Auditing screenshot" src="https://github.com/user-attachments/assets/fc39aa49-eb5e-4575-94b9-0bc4b330f1a8" />


> I enabled object access auditing for both **Success** and **Failure** events so Windows could log access attempts against the monitored tripwire file.


### Step 2: Creating the Tripwire File

After enabling object access auditing, I created a simple text file on the Desktop to use as the monitored tripwire object.

I named the file:

```text
Secret Document.txt
```

<img width="952" height="327" alt="Step 2: Creating the Tripwire File screenshot" src="https://github.com/user-attachments/assets/d343ceb7-713c-4a45-8953-0c06d7ff54a0" />

> I created a simple sensitive-looking text file to act as the tripwire object. The goal was to monitor access to this file and generate Windows Security events when it was opened or read.

### Step 3: Configuring File Auditing

After creating the tripwire file, I opened the advanced security settings of the file and configured an auditing entry.

The auditing rule was set to monitor successful read access attempts for the `Everyone` principal.

<img width="761" height="518" alt="Step 3: Configuring File Auditing screenshot" src="https://github.com/user-attachments/assets/29c1deb6-83c6-454e-bd06-387356372353" />

> I added an auditing entry for `Everyone` and configured it to monitor successful `Read & execute` access. This allowed Windows to generate Security events when the tripwire file was accessed.

### Step 4: Triggering the Tripwire

After configuring the auditing entry, I accessed the monitored file through Command Prompt using the `type` command.

```cmd
type "C:\Users\Administrator\Desktop\Secret Document.txt"
```

<img width="977" height="508" alt="Step 4: Triggering the Tripwire screenshot" src="https://github.com/user-attachments/assets/72414685-6534-420d-a2bc-e917e5ec3f18" />

> I accessed the monitored file through `cmd.exe` to trigger the tripwire. This action generated Windows Security events showing that the file was accessed from the command line.


### Step 5: Event ID 4663 Analysis

After accessing the monitored file through Command Prompt, I reviewed the generated Security events in FullEventLogView.

The most important event was **Event ID 4663**, which shows that an attempt was made to access an object.

<img width="1009" height="872" alt="Step 5: Event ID 4663 Analysis screenshot" src="https://github.com/user-attachments/assets/a862549e-4db3-4b4a-9be4-0c738b89c8fb" />

The event showed the following details:

| Field            | Value                                                |
| ---------------- | ---------------------------------------------------- |
| **Event ID**     | 4663                                                 |
| **Object Type**  | File                                                 |
| **Object Name**  | `C:\Users\Administrator\Desktop\Secret Document.txt` |
| **Process Name** | `C:\Windows\System32\cmd.exe`                        |
| **Accesses**     | `ReadData (or ListDirectory)`                        |
| **Handle ID**    | `0x12c`                                              |

> This confirmed that the tripwire file was accessed through `cmd.exe` and that Windows generated a Security event for the monitored object.

I also observed that Event ID **4663** is part of a wider object access sequence:

```text
4656 → A handle to an object was requested
4663 → An attempt was made to access an object
4658 → The handle to an object was closed
```

This sequence shows how Windows logs object access activity and how these events can be used during SOC investigations.


## Detection Value

The main value of this technique is that it can detect suspicious access to resources that should not normally be touched.

For example, if a hidden or sensitive-looking file is accessed by an unexpected user or process, this could indicate:

* Unauthorized browsing
* Insider activity
* Malware crawling files
* Worm-like behaviour
* Post-compromise discovery
* Data staging or collection activity

This approach is simple, but it can still provide useful visibility when it is placed carefully.

## Purple Teaming and Detection Validation

At the end of the room, I also reviewed how purple team tactics can support detection engineering.

The main idea is simple: if a security team wants to understand how well its detections work, it should simulate attacker activity and then review the logs, alerts, and detection results. This helps defenders see which behaviours were detected and which ones were missed.

From a detection engineering point of view, this is useful because it turns testing into a learning process. Instead of assuming that a rule works, analysts can validate it by observing real attack-like activity in the environment.

A few useful questions to ask after a simulated attack are:

* Which attacker techniques were executed?
* Which activities were detected?
* Which activities were missed?
* Which logs were generated?
* Which detections need to be improved?
* Was the alert useful for investigation?

Detection engineering should not stop after writing a rule. A detection should be tested against realistic activity and improved based on the results.

For example, in a room like **Tempest**, a full attack chain can be simulated and reviewed through collected logs and analysis tools. This allows the analyst to understand how different attack techniques appear in the environment.

In a room like **Follina MSDT**, the focus is more on understanding how exploitation activity appears in logs and how process artifacts can be used to support detection logic.

A key lesson from this section is that purple teaming helps connect offensive activity with defensive visibility. If a technique is detected, it confirms that the current visibility is working in that area. If it is missed, that gap can be used to improve logging, detection logic, or alerting coverage.


## Tripwire Analyst Notes

Tripwires can add another layer of detection without depending only on known malware indicators.

However, the value of a tripwire depends on how it is configured. If the monitored file is accessed too often during normal activity, it may create unnecessary noise. If it is placed in a location where no one should normally interact with it, the signal can be much stronger.

Before using this type of detection in a real environment, I would check:

* Is object access auditing enabled?
* Is the file or folder actually sensitive or unusual?
* Who is expected to access it?
* Which actions should be monitored?
* Will this create too many false positives?
* Are Event ID 4663 logs being collected by the SIEM?

Detection engineering can also include deception-based ideas. A simple hidden file, honeypot, or monitored folder can help detect suspicious behaviour when attackers or malware interact with something they should not touch.

## Key Takeaways

* Tactical detection focuses on practical and actionable detections based on real threats, previous incidents, and environment-specific risks.
* IOCs from previous incidents can be converted into reusable detection rules, but IOC-based detections can become outdated quickly.
* Sigma helps create vendor-agnostic detection logic that can be adapted for different SIEM platforms.
* Public Sigma rules are useful starting points, but they should be reviewed, tested, and tuned before being used in production.
* Tripwires can provide additional visibility by detecting access to sensitive or unusual resources.
* Windows Event ID 4663 can help analysts investigate access attempts against monitored files or objects.
* Purple team tactics can be used to validate detection coverage and identify gaps.
* Detection engineering requires continuous testing, tuning, documentation, and improvement.



## Conclusion

This room showed how an organization can improve its detection capability by using information that is already available in its own environment.

The main idea was that effective detection engineering does not always require complex tools or advanced techniques. Previous incident findings, known IOCs, environment-specific knowledge, Sigma rules, tripwires, and purple team exercises can all be used to create practical detections that provide immediate value.

Layered defense is also important. A SOC should not depend on only one type of detection or one security product. IOC-based detections, behaviour-based detections, file-based tripwires, object access auditing, and purple team validation can all work together to increase visibility and improve the chances of detecting suspicious activity.

From an analyst point of view, detections should be adapted to the environment. Default rules can provide a starting point, but they should be reviewed, tested, tuned, and improved based on real activity and organizational needs.

Purple team tactics are also useful for validating detection coverage. By simulating attacker activity and reviewing the generated logs, analysts can understand which techniques were detected, which ones were missed, and where detection gaps still exist.

Overall, detection engineering is not a one-time task. It needs continuous testing, tuning, and improvement as the environment and attacker behaviour change. A good detection strategy should combine multiple layers, use available telemetry effectively, and be reviewed regularly to stay useful.

## Training Context

These notes and screenshots were produced while completing a guided detection engineering training lab. The summaries and analyst observations document my own understanding of the concepts and practical tasks.
