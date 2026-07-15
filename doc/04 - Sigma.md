# 04. Sigma

## Introduction

Detection engineering is an important part of SOC operations because analysts need reliable ways to identify suspicious activity from logs before an incident becomes more serious.

This section focuses on **Sigma**, an open-source generic signature language used to write detection rules in a structured and platform-independent format.

Sigma is useful because SOC teams often work with different SIEM platforms, query languages, and log sources. Writing detections directly for only one SIEM can create vendor lock-in and make sharing detection logic harder.

Sigma helps solve this problem by allowing analysts to write detection logic once and then convert it into different SIEM query formats.

From a SOC analyst point of view, this is valuable because detection rules can be shared, reviewed, converted, and reused across different environments.

## What is Sigma?

Sigma is a generic rule format for describing suspicious log activity.

It can be compared to:

| Technology | Purpose |
|---|---|
| **Sigma** | Detection rules for log events |
| **Snort** | Rules for network traffic |
| **YARA** | Rules for files and malware samples |

Sigma rules are written in YAML and are designed to describe what suspicious activity looks like inside log data.

For example, a Sigma rule can describe suspicious PowerShell execution, failed login activity, process creation patterns, registry changes, or other behaviours that may indicate malicious activity.

## Why Sigma is Useful

Sigma helps security analysts and detection engineers because it makes detection logic easier to share and convert.

Some common use cases include:

* Writing detection rules for suspicious behaviour.
* Sharing detection logic with other analysts or teams.
* Avoiding dependency on a single SIEM query language.
* Converting one rule into different SIEM formats.
* Supporting threat hunting and alert creation.

Sigma is not only a rule format. It also helps standardise detection engineering work across different platforms.

## Sigma Development Process

A basic Sigma workflow includes three important parts:

| Component | Description |
|---|---|
| **Sigma Rule Format** | The structured YAML rule that describes suspicious log activity. |
| **Sigma Converter** | A tool that converts Sigma rules into SIEM-specific query languages. |
| **Machine Query** | The final search query that is executed in a SIEM or log analysis platform. |

The general process is:

```text
Sigma Rule → Sigma Converter → SIEM Query
```

This means an analyst can write a Sigma rule once and then convert it into a query format supported by tools such as Splunk, Elastic, Sentinel, QRadar, or other platforms.


## Sigma Rule Syntax

Sigma rules are written in **YAML**, which is a human-readable data format commonly used for configuration files.

In Sigma, YAML is used to structure detection rules in a clear and standardised way. This makes the rule easier to read, share, review, and convert into different SIEM query languages.

Some important YAML points for Sigma rules are:

| YAML Feature | Description |
|---|---|
| **Case-sensitive** | Field names and values must be written carefully. |
| **`.yml` extension** | Sigma rules are usually saved with the `.yml` extension. |
| **Spaces for indentation** | Spaces are used for indentation instead of tabs. |
| **Comments** | Comments can be written using the `#` character. |
| **Key-value pairs** | Key-value pairs use the `:` character. |
| **Lists** | List items are written using the `-` character. |

Sigma rules are not only about detection logic. They also require clean formatting because a small indentation or syntax mistake can break the rule.

## Common Sigma Rule Fields

A Sigma rule usually contains several important fields. Some fields are required, while others provide additional context about the rule.

| Field | Purpose |
|---|---|
| **title** | Gives the rule a short and clear name. |
| **id** | Provides a unique identifier for the rule. |
| **status** | Shows the maturity level of the rule, such as `test`, `experimental`, or `stable`. |
| **description** | Explains what the rule is intended to detect. |
| **author** | Shows who created the rule. |
| **references** | Links the rule to related reports, research, or external sources. |
| **logsource** | Defines which log source should be used. |
| **detection** | Contains the actual detection logic. |
| **condition** | Defines how the detection selections should be evaluated. |
| **falsepositives** | Describes possible legitimate activity that may trigger the rule. |
| **level** | Defines the severity of the detection. |
| **tags** | Adds categorisation, such as MITRE ATT&CK tactics or techniques. |

From a SOC analyst point of view, these fields are useful because they make the rule easier to understand during alert triage and detection review.

For example, the `description`, `falsepositives`, `level`, and `tags` fields help an analyst understand why the rule exists, how serious it may be, and what kind of activity it is trying to detect.

## Logsource Field

The `logsource` field defines where the detection should look for events.

A Sigma rule can use logsource attributes such as:

| Attribute | Description |
|---|---|
| **product** | The product or platform that generated the logs, such as Windows or Linux. |
| **category** | The type of log activity, such as process creation or DNS events. |
| **service** | A specific service, such as `security` on Windows or `sshd` on Linux. |
| **definition** | Additional information about the log source or configuration. |

Example:

```yaml
logsource:
  product: windows
  category: process_creation
```

This tells the detection engine that the rule is designed for Windows process creation logs.

## Detection Field

The `detection` field is the most important part of a Sigma rule because it defines what suspicious activity should be searched for.

A basic detection block usually contains:

```yaml
detection:
  selection:
    EventID:
      - 19
      - 20
      - 21
  condition: selection
```

In this example, the rule looks for Windows Event IDs `19`, `20`, or `21`.

The `selection` section defines what to search for, and the `condition` tells the rule when it should match.


| Part | Purpose |
|---|---|
| **Search identifiers** | Define the fields and values to search for. |
| **Condition expressions** | Define how those identifiers should be evaluated. |

## Search Identifiers and Conditions

Sigma rules can use lists and maps to define detection logic.

A list usually works like an **OR** condition. For example:

```yaml
HostApplication|contains:
  - 'powercat'
  - 'powercat.ps1'
```

This means the rule can match if `HostApplication` contains either `powercat` or `powercat.ps1`.

A map uses key-value pairs and can combine multiple fields together. For example:

```yaml
selection:
  Image|endswith:
    - '/rm'
    - '/shred'
  CommandLine|contains:
    - '/var/log'
    - '/var/spool/mail'
condition: selection
```

This kind of logic is useful when a detection needs to match suspicious behaviour across more than one field.

## Sigma Value Modifiers

Sigma supports value modifiers that change how a field value is matched.

Some common modifiers include:

| Modifier | Description |
|---|---|
| **contains** | Matches when the value appears anywhere in the field. |
| **startswith** | Matches when the field starts with the specified value. |
| **endswith** | Matches when the field ends with the specified value. |
| **all** | Requires all listed values to match. |
| **base64** | Looks for Base64-encoded values. |
| **re** | Uses a regular expression match. |

Example:

```yaml
Image|endswith:
  - '\cmd.exe'
```

This would match when the `Image` field ends with `cmd.exe`.

Value modifiers are important because real-world logs may contain long paths, command lines, encoded values, or partial strings. These modifiers help detection engineers write more flexible rules.

## Condition Expressions

The `condition` field controls how Sigma evaluates the detection logic.

Common condition expressions include:

| Condition | Meaning |
|---|---|
| **selection** | Match the named selection. |
| **selection and filter** | Match both conditions. |
| **selection and not filter** | Match the selection but exclude known false positives. |
| **1 of selection_\*** | Match one of multiple selections. |
| **all of selection_\*** | Match all matching selections. |

Example:

```yaml
detection:
  tools:
    - 'scp'
    - 'rsync'
    - 'sftp'
  filter:
    - '@'
    - ':'
  condition: tools and filter
```


In real SOC environments, this is useful because detection rules often need to include exclusions or filters to reduce false positives.

## Filtering False Positives

Sigma rules can also include filters to exclude known legitimate activity.

For example, a rule may detect registry persistence behaviour, but exclude known legitimate browser installer activity from Google Chrome or Microsoft Edge.

This kind of logic usually appears in the condition as:

```yaml
condition: selection and not 1 of filter_*
```

This means the rule should match the suspicious selection, but ignore events that match any of the defined filters.

From an analyst point of view, this is important because a detection rule should not only find suspicious activity. It should also avoid creating too much noise from expected behaviour.

> This section shows how Sigma rules are structured and how detection logic can be built using fields, values, modifiers, conditions, and filters.    

## Practical Lab: AnyDesk Installation Detection

In the practical part of this room, I worked on a Sigma rule designed to detect a suspicious AnyDesk installation on a Windows host.

The scenario was based on an attacker using AnyDesk as a remote access tool. Although AnyDesk is a legitimate remote administration application, it can also be abused by attackers to gain remote access to a compromised machine.

From the provided intelligence, the important detection points were:

| Indicator / Behaviour | Reason |
|---|---|
| `AnyDesk.exe` | The executable related to the remote access tool. |
| `--install` | Indicates installation activity. |
| `--start-with-win` | Indicates persistence by starting with Windows. |
| `--silent` | May indicate silent installation without user interaction. |
| `C:\ProgramData\AnyDesk.exe` | Suspicious installation path used in the scenario. |

From an analyst point of view, this was important because the detection was not only based on the file name. It also looked at command-line behaviour that showed installation and persistence activity.

### Sigma Rule Logic

The Sigma rule focused on Windows process creation logs.

The log source was:

```yaml
logsource:
  category: process_creation
  product: windows
```

The detection logic searched for AnyDesk installation behaviour in command-line activity:

```yaml
detection:
  selection:
    CommandLine|contains|all:
      - '--install'
      - '--start-with-win'
    CurrentDirectory|contains:
      - 'C:\ProgramData\AnyDesk.exe'
  condition: selection
```

The important part of this rule was the use of the `contains|all` modifier. This means the command line must contain all listed values, not just one of them.

This helped reduce weak matches and made the detection more focused on the installation behaviour.

### Rule Metadata

The rule also included metadata to make it easier to understand and triage:

```yaml
falsepositives:
  - Legitimate deployment of AnyDesk
level: high
tags:
  - attack.command_and_control
  - attack.t1219
```

The MITRE ATT&CK tag `attack.t1219` is related to Remote Access Software, which fits the scenario because AnyDesk can be used for remote access.

### Converting the Sigma Rule

After reviewing the Sigma rule, I converted it into a SIEM-compatible query.

The room introduced `sigmac` as the command-line tool used to convert Sigma rules into different SIEM query formats.

```text
sigmac
```

The general workflow was:

```text
Sigma Rule → Sigmac / Uncoder → SIEM Query → Kibana Validation
```

This shows how Sigma can be used as a platform-independent detection format and then converted into a query that can be tested in a specific SIEM environment.

### Validating the Detection in Kibana

After converting and reviewing the detection logic, I validated the AnyDesk installation activity in Kibana.

The search query used was:

```text
AnyDesk AND --install
```

<img width="1907" height="456" alt="Validating the Detection in Kibana screenshot" src="https://github.com/user-attachments/assets/e5ab850a-c26a-4c2e-94fe-d05c715435f7" />

The search returned matching AnyDesk installation events.

Important findings from the event were:

| Finding | Value |
|---|---|
| **Query Used** | `AnyDesk AND --install` |
| **Matching Events** | `2` |
| **Installation Time** | `Jun 28, 2022 @ 22:19:00` |
| **Installed Product** | `AnyDesk` |
| **Installed Version** | `7.0.10` |
| **Data View** | `winlogbeat-8.2.3` |

The event showed that AnyDesk version `7.0.10` was installed at `Jun 28, 2022 @ 22:19:00`.

> This confirmed that the Sigma detection logic could be used to identify AnyDesk installation activity from Windows event logs.


### Analyst Note: Sigma Conversion Differences

During the room, I noticed that different Sigma conversion tools can produce slightly different query outputs from the same rule.

For example, `sigmac` and Uncoder.io may convert the same Sigma rule using different field names depending on the selected backend and configuration.

One converter may generate fields such as:

```text
Image.keyword
CommandLine.keyword
```

while another converter may generate fields such as:

```text
process.executable
process.command_line
```

From a SOC analyst point of view, this is important because converted Sigma queries should not always be used blindly. Even if the detection logic is similar, the final query still needs to match the actual SIEM backend, index mapping, log source, and field names available in the environment.

For this reason, I treated the converted query as a starting point rather than a final detection. The output still needed to be reviewed, adjusted, and validated against the available log fields.


## Practical Lab: Scheduled Task and Ransomware Activity

In the practical part of this task, I worked on a scenario where unusual activity was observed on a Windows host.

The scenario included two main activities:

* A suspicious scheduled task creation.
* Possible ransomware-related file creation activity.

The goal was to use Sigma concepts to identify the correct detection values, choose the right logsource category, and validate the activity in Kibana.

## Scheduled Task Creation Detection

For the scheduled task activity, the scenario indicated that the activity should be detected from process creation events.

From a Sigma rule point of view, this means the logsource should focus on Windows process creation logs.

A suitable logsource would be:

```yaml
logsource:
  product: windows
  category: process_creation
```

To detect scheduled task creation, the important process value was:

```text
\schtasks.exe
```

This is because `schtasks.exe` is commonly used on Windows systems to create, modify, and manage scheduled tasks.

### Searching for Scheduled Task Activity in Kibana

I searched for scheduled task creation activity in Kibana using the following query:

```text
schtasks AND create
```

<img width="1904" height="462" alt="Searching for Scheduled Task Activity in Kibana screenshot" src="https://github.com/user-attachments/assets/a502f834-9b5e-40a9-963b-a4ece53601b8" />

The search returned two matching events. One of the events was related to the Task Scheduler configuration tool, and the other event was related to the Windows Command Processor.

I opened the Windows Command Processor event and reviewed the command-line details.

<img width="1912" height="549" alt="Searching for Scheduled Task Activity in Kibana screenshot" src="https://github.com/user-attachments/assets/9f0ee7b4-ffdf-4bd8-9f9c-3b57961cd653" />

The `process.command_line` field showed the following command:

```text
"cmd.exe" /c "SCHTASKS /Create /SC ONCE /TN spawn /TR C:\windows\system32\cmd.exe /ST 20:10"
```

From this command, I identified the scheduled task details:

| Finding | Value |
|---|---|
| **Detection Value** | `\schtasks.exe` |
| **Task Name** | `spawn` |
| **Scheduled Run Time** | `20:10` |
| **Parent Process** | `powershell.exe` |
| **Executed Process** | `cmd.exe` |

The `/TN` argument showed the task name, and the `/ST` argument showed the time the task was meant to run.

> The command-line arguments provided the key investigation details, especially the task name and scheduled run time.

### Ransomware File Creation Logsource

The second part of the scenario focused on possible ransomware activity.

The hint pointed to the Sigma taxonomy and logsource categories. Since the activity involved a created file ending with `.txt`, the correct Sigma logsource category was related to file activity rather than process creation.

A suitable Sigma logsource would be:

```yaml
logsource:
  product: windows
  category: file_event
```

This means the Sigma rule should focus on file creation events.

From the scenario, the expected activity was:

```text
A created file ending with .txt
```

The appropriate Sigma logsource category was:

```text
file_event
```

### Reviewing File Creation Events

I searched for `.txt` file creation activity in Kibana and reviewed the file event results.

<img width="1904" height="595" alt="Reviewing File Creation Events screenshot" src="https://github.com/user-attachments/assets/effc9a1c-dd30-4481-b730-6de2ef004df7" />

The results showed multiple `.txt` related file creation events. Many of them were related to Windows Search / Cortana cache activity, such as `SearchUI.exe` creating files under `DeviceSearchCache`.

Example observed fields included:

| Field | Example |
|---|---|
| **event.action** | `File created (rule: FileCreate)` |
| **event.category** | `file` |
| **event.code** | `11` |
| **process.name** | `SearchUI.exe` |
| **file.path** | `DeviceSearchCache` |

From an analyst point of view, this was important because not every `.txt` file creation event is malicious. Some file creation events are normal system activity and should be treated as false positives or unrelated noise.

The event code associated with file creation activity was:

```text
11
```

> File creation detections need careful filtering. A Sigma rule should focus on the suspicious file creation behaviour described in the scenario while avoiding unrelated system-generated `.txt` files.

## Reviewing Ransomware File Creation Activity

For the ransomware activity, the scenario indicated that a `.txt` file was created and that the file creation process was run via `cmd.exe`.

To investigate this, I searched for `cmd.exe` activity in Kibana and reviewed the related file creation events.

The query used was:

```text
cmd.exe
```

<img width="1909" height="561" alt="Reviewing Ransomware File Creation Activity screenshot" src="https://github.com/user-attachments/assets/e140910a-44b5-415d-a2d3-52e1c22b39cb" />

The results showed a file creation event related to `cmd.exe`.

The important findings were:

| Finding | Value |
|---|---|
| **Process Name** | `cmd.exe` |
| **Process Executable** | `C:\Windows\SYSTEM32\cmd.exe` |
| **Created File** | `YOUR_FILES.txt` |
| **File Path** | `C:\Users\Administrator\Desktop\YOUR_FILES.txt` |
| **Event Code** | `11` |

The `event.code` value `11` indicates a file creation event.

To identify the content written to the ransomware note, I reviewed the related command-line activity. The command showed that the following content was written into the file:

```text
T1486 - Purelocker Ransom Note
```

From this analysis, I confirmed:

| Question | Answer |
|---|---|
| **Created file name** | `YOUR_FILES.txt` |
| **Event code** | `11` |
| **Ransomware note content** | `T1486 - Purelocker Ransom Note` |

> The investigation showed why process execution and file creation events should be reviewed together when analysing ransomware-style activity.

## Key Takeaways

This room showed how Sigma can be used to write structured and reusable detection rules.

The key points were:

| Topic | Takeaway |
|---|---|
| **Sigma Rule Format** | Sigma rules are written in YAML and provide a structured way to describe suspicious log activity. |
| **Search Identifiers** | Detection logic is built by defining the fields and values that should be searched. |
| **Condition Expressions** | Conditions control how selections, filters, and exclusions are evaluated. |
| **Value Modifiers** | Modifiers such as `contains`, `endswith`, and `all` make detection logic more flexible. |
| **Rule Conversion** | Sigma rules can be converted into SIEM-specific query formats using tools such as `sigmac` or Uncoder.io. |
| **Validation** | Converted queries should always be tested against real logs because field mappings may differ between environments. |

From a SOC analyst point of view, Sigma is not only about writing rules. A useful detection also requires understanding the log source, choosing the right fields, converting the rule correctly, and validating the result in the SIEM.

## Conclusion

In this room, I focused on Sigma rule syntax, detection logic, rule conversion, and practical validation in Kibana.

I first reviewed the structure of Sigma rules, including fields such as `title`, `logsource`, `detection`, `condition`, `falsepositives`, `level`, and `tags`.

Then I analysed how search identifiers, lists, maps, value modifiers, and condition expressions are used to build detection logic.

In the practical lab, I investigated different Windows activities using Kibana. I identified AnyDesk installation activity, scheduled task creation, and ransomware-style file creation behaviour.

During the lab, I confirmed the following findings:

| Finding | Value |
|---|---|
| **Sigma conversion tool** | `sigmac` |
| **AnyDesk installation time** | `Jun 28, 2022 @ 22:19:00` |
| **AnyDesk version** | `7.0.10` |
| **Scheduled task detection value** | `\schtasks.exe` |
| **Scheduled task name** | `spawn` |
| **Scheduled task run time** | `20:10` |
| **Ransomware logsource category** | `file_event` |
| **Created ransomware file** | `YOUR_FILES.txt` |
| **File creation event code** | `11` |
| **Ransomware note content** | `T1486 - Purelocker Ransom Note` |

This room showed how Sigma rules can support detection engineering by making detection logic easier to write, share, convert, and validate across different SIEM environments.

> From an analyst point of view, a Sigma rule is only useful when it is tested against real logs and adjusted to match the actual field names, log sources, and backend configuration of the environment.

## Training Context

These notes and screenshots were produced while completing a guided detection engineering training lab. The summaries and analyst observations document my own understanding of the concepts and practical tasks.
