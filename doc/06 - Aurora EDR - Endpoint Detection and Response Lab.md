# 06 - Aurora EDR: Endpoint Detection and Response Lab

This section focuses on Aurora EDR, a Sigma-based Windows endpoint agent that uses Windows Event Logs, Sigma rules, and IOCs to detect suspicious activity.

The main EDR concepts covered here include endpoint activity monitoring, threat detection, investigation, response, containment, forensic analysis, and the collection of endpoint telemetry such as process execution, file activity, commands, user actions, and network-related events.

EDR solutions also help analysts investigate suspicious activity by searching for Indicators of Compromise, identifying root causes, and hunting for behavior-based indicators of attack.

The main skills I practised in this room were:

- Understanding the purpose of EDR solutions
- Reviewing endpoint telemetry concepts
- Learning how Windows Event Logs support detection
- Understanding detection, response, containment, integration, insights, and forensics in EDR
- Investigating suspicious events detected by Aurora
- Connecting endpoint activity with detection engineering concepts

---

## What is EDR?

EDR stands for **Endpoint Detection and Response**.

EDR solutions are used to monitor endpoint activity, collect telemetry, analyse suspicious behaviour, and help security teams detect and respond to threats.

Endpoint security does not only depend on perimeter monitoring. Security teams also need visibility into what is happening directly on endpoints.

Some important EDR functions include:

- Monitoring and collecting endpoint activity data
- Analysing data to identify threat patterns
- Responding to detected threats
- Containing or removing malicious activity
- Supporting forensic investigation
- Searching for suspicious behaviour or Indicators of Compromise

---

## Windows Event Logs and Event Viewer

This section introduced how Windows systems record events and how analysts can review them through Windows Event Viewer.

Windows Event Viewer presents logs in different categories. The main categories used during investigations are:

- `Application`
- `System`
- `Security`

The room also explained different event levels:

- `Information`
- `Warning`
- `Error`
- `Success Audit`
- `Failure Audit`

For example, an `Error` event level can describe a significant problem with a service or application.


<img width="1680" height="1047" alt="171be6b47de229eb03e7c53c8c1d7e06" src="https://github.com/user-attachments/assets/f2815b3f-3547-4a1e-9d11-c4363d4858e9" />

---


## Event Tracing for Windows

Event Tracing for Windows, also known as ETW, is a Windows logging feature that allows applications and drivers to produce event data.

For cybersecurity defenders, ETW is useful because it can provide detection information from different parts of the operating system. EDR tools can use this event data to monitor endpoint behaviour and identify suspicious activity.

ETW is made up of three main components:

- `Controllers`
- `Providers`
- `Consumers`

Controllers are used to configure event tracing sessions.  
Providers are applications or components that produce event logs.  
Consumers subscribe to event logs and listen to events in real time or from a file.

One example of a controller is:

```text
logman.exe
```

From a detection engineering perspective, ETW is important because it provides event data that can be used for endpoint monitoring, alerting, and investigation.

---

## Aurora Overview

Aurora is a Windows endpoint agent that uses Sigma rules and IOCs to detect threat patterns from local Windows event streams through Event Tracing for Windows.

When a rule matches suspicious activity, Aurora can trigger response actions and display alerts in Windows Event Viewer.

Aurora can be used as an on-premises tool, which means the data does not need to leave the network. This is useful from a privacy and security point of view.

Aurora combines:

- Endpoint telemetry
- Sigma-based detection logic
- IOC matching
- Alert generation
- Response actions

This makes Aurora more than just a logging tool. It can help analysts detect suspicious endpoint activity and respond to it based on Sigma rules and IOCs.

---

## Aurora and Sysmon Comparison

Aurora and Sysmon were compared from a telemetry and detection perspective.

Sysmon provides detailed Windows event logging through the Sysmon kernel driver, while Aurora uses Event Tracing for Windows and focuses on Sigma and IOC matching.

Some important differences I noted were:

- Aurora uses ETW as its event source.
- Sysmon uses the Sysmon kernel driver.
- Aurora supports Sigma and IOC matching.
- Aurora can trigger response actions.
- Aurora can output alerts to Eventlog, files, and UDP/TCP targets.
- Aurora produces lower relative log volume compared to Sysmon.
- Sysmon provides broader event coverage, but Aurora adds detection and response capabilities.

In short, Sysmon is mainly focused on detailed event logging, while Aurora is more focused on detection, alerting, IOC matching, and response actions.

---

## Aurora Presets

Aurora can be configured with different presets depending on the required visibility level and system resource usage.

The main Aurora presets are:

- `Standard`
- `Reduced`
- `Minimal`
- `Intense`

These presets affect settings such as:

- CPU limit
- Process priority
- Minimum reporting level
- Active modules
- Deactivated sources

For example, the `Minimal` preset uses fewer resources and disables some modules, while the `Intense` preset provides more visibility with a lower minimum reporting level.

This shows that EDR configuration is a balance between endpoint visibility, detection coverage, and system performance.

---

## Running Aurora

Aurora can be started from the command line with a selected configuration file.

Example command for running Aurora with the minimal configuration:

```powershell
C:\Program Files\Aurora-Agent>aurora-agent.exe -c agent-config-minimal.yml
```

Aurora can also be installed and run as a service by using the `--install` flag:

```powershell
C:\Program Files\Aurora-Agent>aurora-agent.exe --install -c agent-config-minimal.yml
```

The `--status` flag can be used to check the current state of the Aurora agent:

```powershell
C:\Program Files\Aurora-Agent>aurora-agent.exe --status
```

The status output provides useful information such as:

- Aurora version
- Running status
- Uptime
- Active outputs
- Active modules
- Loaded rules
- Rule reloads
- Sigma matches
- Response action status

These details are useful during an investigation because they show whether Aurora is running correctly, which outputs are enabled, which modules are active, and whether any Sigma matches or response actions have occurred.

---

## Aurora Output Options

Aurora supports multiple output options for alert data.

The main output options are:

- Windows Eventlog
- Log file
- UDP/TCP targets

### Windows Eventlog

Aurora can write its alerts to Windows Eventlog. This allows analysts to view detection details inside Windows Event Viewer.

This is useful because Windows Event Viewer is already a familiar tool for reviewing system and security-related events.

### Log File

Aurora can also write alerts to a log file by using the `--logfile` flag:

```powershell
C:\Program Files\Aurora-Agent>aurora-agent.exe --logfile aurora-minimal.log
```

### UDP/TCP Targets

Aurora can send events to network targets through UDP or TCP. This can be useful when forwarding alerts to an internal repository, SIEM, or another monitoring system.

These output options show how Aurora alerts can be collected and reviewed depending on the environment.

---

## Aurora Responses

Aurora responses extend Sigma detections by allowing actions to be triggered when a rule matches.

These response actions can help contain or limit attacker activity on the endpoint.

Aurora supports two response types:

- Predefined responses
- Custom responses

### Predefined Responses

Predefined responses include:

- `Suspend` - used to stop a specified process
- `Kill` - used to kill a specified process
- `Dump` - used to create a dump file for analysis

Example kill response:

```yml
response:
  type: predefined
  action: kill
  processidfield: ParentProcessId
```

Example suspend response:

```yml
response:
  type: predefined
  action: suspend
```

### Custom Responses

Custom responses can be used to call an internal program or command when an alert is raised.

Example custom response:

```yml
response:
  type: custom
  action: cmd /c copy %Image% "%ProgramData%\Aurora\Image-%ProcessId%.bin"
```

This is important because endpoint detection should not only generate alerts. In some cases, response actions can help stop or contain suspicious activity before it causes more damage.

---

## Aurora Event IDs

Aurora uses event IDs to record different types of detections and internal events in Windows Eventlog.

Some useful Aurora event IDs I noted were:

| Event ID | Description |
|---|---|
| 1 | A process creation Sigma rule matched |
| 2 | A set file creation time Sigma rule matched |
| 3 | A network connection Sigma rule matched |
| 4 | A Sysmon status Sigma rule matched |
| 5 | A process termination Sigma rule matched |
| 6 | A driver-loaded Sigma rule matched |
| 7 | An image-loaded Sigma rule matched |
| 8 | A create remote thread Sigma rule matched |
| 9 | A raw disk access Sigma rule matched |
| 10 | A process access Sigma rule matched |
| 11 | A file creation Sigma rule matched |
| 12 | A registry event Sigma rule matched |
| 17 | A pipe event Sigma rule matched |
| 19 | A WMI event Sigma rule matched |
| 21 | A registry event Sigma rule matched |
| 22 | A DNS query Sigma rule matched |
| 23 | A file deletion Sigma rule matched |
| 95 | An error occurred while loading the Sigma rules |
| 96 | Sigma rules were reloaded |
| 97 | No Sigma rule files were found |
| 98 | Unspecified log message from Sigma module |
| 99 | Another Sigma rule matched |
| 100 | A license file was found |
| 101 | Status message |
| 102 | Aurora Agent started |
| 103 | Aurora Agent is terminating |
| 104 | The current license expired |
| 105 | No valid license file was found |
| 107 | A process created a large number of events |
| 108 | An internal panic occurred |
| 200 | BeaconHunter |
| 300 | LSASS Dump Detector |
| 400 | ETW Canary |
| 500 | Process Tampering Detector |
| 600 | Temporary Driver Load Detector |
| 700 | Command Line Mismatch Detector |
| 800 | Event Distributor |
| 900 | ETW Provider |
| 1000 | Eventlog Provider |
| 1100 | Handle Polling Provider |
| 1200 | Resource Control |
| 6000 | A response for a Sigma match was executed |
| 6001 | A response for a Sigma match was simulated |

These event IDs are useful because they help analysts quickly understand what type of detection or internal Aurora event occurred.

---

## Analyst Note

Aurora connects Sigma-based detection logic with endpoint telemetry and response actions.

A key observation from this room is that Aurora does not only collect logs. It can match Sigma rules, detect IOCs, generate alerts, and trigger response actions based on suspicious endpoint behaviour.

For SOC analysts and detection engineers, this creates a connection between Windows event data, Sigma rules, alerting, and endpoint response.

---


## Function Tests

After reviewing Aurora concepts and configuration options, I reviewed several function test examples to understand how Aurora detections appear in Windows Event Viewer.

These tests demonstrated the practical side of Aurora alerts by showing how Sigma rule matches appear in Windows Event Viewer.

### User Privilege Enumeration

One of the function tests involved running the following command:

```powershell
whoami /priv
```

This command lists the current user privileges. Aurora detected this activity and generated a warning-level event in Windows Event Viewer.

<img width="1679" height="1006" alt="1ce641aa45e7f2d7b0c4b5247f6b6f4e" src="https://github.com/user-attachments/assets/078bda4f-81c4-458f-9cf7-a4d5d38b8dd5" />

The alert showed that a Sigma rule matched the `whoami /priv` command. This type of command can be used by administrators, but it can also be used by attackers after gaining access to a host to check available privileges.

**Analyst Note:**  
`whoami /priv` is a legitimate Windows command, but during an investigation it can indicate privilege enumeration. If this activity appears after suspicious process execution or initial access, it should be reviewed as part of the attack chain.

---

### Suspicious DNS Beaconing

Another function test showed Aurora detecting suspicious DNS beaconing activity. The alert was related to a Sigma rule match for suspicious Cobalt Strike DNS beaconing.

<img width="1680" height="1009" alt="c246b3ff357d7ef13826831b4ba682b6" src="https://github.com/user-attachments/assets/658643ed-4ef3-4f26-ae5f-cf04db4d44b7" />

The alert showed that Aurora can detect suspicious network-related behaviour through Sigma rule matching and record the result in Windows Event Viewer.

**Analyst Note:**  
Suspicious DNS beaconing can indicate command and control activity. Attackers may use DNS-based communication to maintain access or communicate with external infrastructure. Detecting this behaviour is important because it can reveal post-compromise activity and possible C2 communication.

---

### Function Test Summary

These function tests showed how Aurora detections are presented in Windows Event Viewer. Instead of only collecting endpoint logs, Aurora can apply Sigma rules to endpoint activity and generate alerts when suspicious behaviour is detected.

The key points from this section were:

- Aurora can generate alerts from Sigma rule matches.
- Detection results can be reviewed in Windows Event Viewer.
- Commands such as `whoami /priv` may indicate privilege enumeration.
- DNS beaconing can indicate command and control activity.
- Alert context is important when deciding whether an event is suspicious or benign.

This section connected Aurora’s detection logic with real alert examples and showed how endpoint activity appears during analyst review.


## Aurora Detection Gaps and ETW Limitations

Since Aurora uses Event Tracing for Windows to observe and monitor Windows system events, some activity may not be fully visible through ETW alone. This section covered several areas where ETW events may be unavailable, noisy, or difficult to use directly for detection.

Understanding these gaps is important because no detection tool gives complete visibility by itself. In some cases, Aurora may need to be used with additional configurations or supported by other logging tools such as Sysmon.

---

### Named Pipes

Named pipes are used as a communication channel between processes. However, ETW does not provide a clean provider for collecting detailed information about named pipe creation or connection events.

Named pipe activity can be observed through Kernel Object Handle events, but this can be noisy and may produce unnecessary information.

Possible solutions include:

- Running Aurora with the `Intense` configuration
- Complementing Aurora with Sysmon to capture additional events

**Analyst Note:**  
Named pipes can be abused by malware and post-exploitation tools for inter-process communication. Because visibility can be limited, relying on only one telemetry source may not be enough during an investigation.

---

### Registry Events

Registry activity can be generated through ETW, especially when keys are created or values are written. However, registry tracking can be difficult because registry handles must be followed individually as keys are referenced by their handles.

This means registry events may not always be directly useful without additional context.

Possible solutions include:

- Running Aurora with the `Intense` configuration
- Using Sysmon alongside Aurora to improve registry event visibility

**Analyst Note:**  
Registry events are important for detecting persistence, configuration changes, and malware execution paths. If registry telemetry is incomplete, combining Aurora with Sysmon can provide stronger coverage.

---

### ETW Disabled or Manipulated

Attackers may attempt to disable or manipulate ETW by patching system calls that Windows uses to create events from user space.

Because of this, detection rules based only on user-space ETW providers should be written carefully. If an attacker can interfere with ETW event generation, some detections may be bypassed or become incomplete.

Possible solutions include:

- Using Aurora’s full version with the ETW Canary module to detect ETW manipulation
- Using the `--report-stats` flag to report agent status to a SIEM
- Reviewing observed, processed, and dropped event statistics for signs of tampering

**Analyst Note:**  
ETW is a powerful telemetry source, but defenders should also consider the possibility of telemetry manipulation. Monitoring the health of the detection agent and checking event statistics can help identify suspicious gaps in visibility.

---

### Key Takeaway

This section showed that endpoint detection depends heavily on telemetry quality. Aurora can provide useful detection capabilities through ETW, Sigma rules, and IOCs, but some areas may require additional configuration or supporting tools.

The main points I noted were:

- ETW is useful, but it does not provide complete visibility for every event type.
- Named pipe and registry activity can be difficult to monitor cleanly through ETW alone.
- Attackers may attempt to manipulate or disable ETW.
- Aurora’s `Intense` configuration can provide more visibility.
- Sysmon can be used alongside Aurora to improve event coverage.
- Monitoring agent health and event statistics is important for reliable detection.

This section reinforced that detection engineering is not only about writing rules. Telemetry gaps, data source limits, and supporting log sources also matter during detection design.


## Lab Scenario - Aurora Detection Testing

After reviewing the Aurora EDR concepts, I moved to the practical lab section. In this scenario, suspicious activity had been observed inside `THM_Acme` systems, and the goal was to test Aurora’s detection capabilities on a Windows host.

Aurora had already been installed on the Windows machine, but it was not running at the beginning of the lab. The task was to execute the provided batch file from the Desktop, start the suspicious activity simulation, and investigate the events generated by Aurora.

The investigation focused on Aurora-related events starting with:

- `Event ID: 1`

This event ID is associated with a process creation Sigma rule match in Aurora.

The lab environment was accessed through the attached Windows VM. After the machine loaded, I opened the Desktop, executed the provided batch file, and reviewed the generated Aurora alerts through Windows Event Viewer.

If Aurora alerts did not appear immediately, I waited a few minutes for the agent to fully load and then reran the batch file. The lab note also mentioned excluding the file named `password.txt` from the Desktop before running the script again if required.

### Investigation Focus

In this lab section, I focused on:

- Running the provided suspicious activity simulation
- Checking Aurora-generated alerts in Windows Event Viewer
- Reviewing Aurora Event ID `1`
- Identifying suspicious process creation activity
- Understanding how Sigma rule matches are presented by Aurora
- Connecting Aurora alerts with endpoint investigation steps

### Analyst Note

This section moved from theory to practical investigation. I used the lab environment to generate Aurora alerts and review how detections were recorded in Windows Event Viewer.


## Aurora Detection Findings

After running the lab activity, I reviewed Aurora-generated events in Windows Event Viewer under the `Application` log. I focused on Aurora alerts produced by the `AuroraAgent` source.

Some of the generated events were related to Sigma rule matches. The following findings show how Aurora presented suspicious endpoint activity through Windows Event Viewer.

---

### Detection Finding #1 - Suspicious Non-PowerShell WSMAN COM Provider

One of the Aurora alerts was generated with `Event ID 99`. This event showed that a Sigma rule matched suspicious WSMAN provider activity.

The matched rule was:

- **Aurora Event ID:** `99`
- **Module:** `Sigma`
- **Rule Title:** `Suspicious Non PowerShell WSMAN COM Provider`
- **Rule Level:** `Medium`
- **Computer:** `THM-AURORA`
- **Provider Name:** `WSMan`
- **New Provider State:** `Started`
- **Host Application:** `C:\Windows\System32\RemoteFXvGPUDisablement.exe`
- **Original Event ID:** `600`

The rule description stated that it detects suspicious use of the WSMAN provider without `PowerShell.exe` as the host application.

<img width="1911" height="829" alt="Ekran görüntüsü 2026-07-09 221915" src="https://github.com/user-attachments/assets/7511de6e-8bd6-4f78-b1f7-3a4e8eb8e0ea" />

**Analyst Note:**  
This alert is interesting because WSMAN activity is commonly associated with remote management and PowerShell-related activity. In this case, the provider was started by a non-PowerShell host application. This does not automatically confirm malicious activity, but it is suspicious enough to review the host application, parent process, execution context, and whether the activity was expected on the endpoint.

---

### Detection Finding #2 - Malicious PowerShell Scripts

Another Aurora alert was also generated with `Event ID 99`. This alert matched a Sigma rule related to malicious PowerShell script usage.

The matched rule was:

- **Aurora Event ID:** `99`
- **Module:** `Sigma`
- **Rule Title:** `Malicious PowerShell Scripts - PoshModule`
- **Rule Level:** `High`
- **Computer:** `THM-AURORA`
- **Host Application:** `ConsoleHost`
- **Event Viewer Level:** `Warning`

The rule description stated that it detects the execution of known offensive PowerShell scripts used for exploitation or reconnaissance.

<img width="1914" height="813" alt="Ekran görüntüsü 2026-07-09 222005" src="https://github.com/user-attachments/assets/32876abf-fb45-4ca0-89f7-deaf86155ea2" />

**Analyst Note:**  
This alert is more serious because PowerShell is frequently abused during post-exploitation activity. Although PowerShell is a legitimate administrative tool, known offensive modules can indicate reconnaissance, credential access, privilege escalation, or exploitation activity. The alert appeared as a warning in Event Viewer, while the matched Sigma rule had a high severity level. This type of alert should be reviewed together with nearby process execution events, command-line activity, user context, and any related file or network activity.

---

### Finding Summary

These two Aurora alerts showed how Sigma-based detections can appear inside Windows Event Viewer. The first alert focused on suspicious WSMAN provider usage without PowerShell as the host application, while the second alert detected known offensive PowerShell script activity.

The key points from these findings were:

- Aurora can generate Sigma rule match events inside Windows Event Viewer.
- `Event ID 99` can indicate that a Sigma rule matched outside the main predefined event categories.
- Rule metadata such as `Rule_Title`, `Rule_Level`, `Rule_Description`, and `Rule_Path` is useful during investigation.
- Event Viewer severity and Sigma rule severity should both be reviewed.
- PowerShell and WSMAN-related activity should be investigated carefully when they appear in suspicious contexts.

## Additional Lab Findings

During the practical investigation, I reviewed Aurora events inside Windows Event Viewer and focused on Sigma rule matches generated by the `AuroraAgent` source.

The first notable event was related to process reconnaissance activity. The matched Sigma rule was:

- **Rule Title:** `Process Reconnaissance Via Wmic.EXE`
- **Rule ID:** `221b251a-357a-49a9-920a-271802777cc0`
- **Rule Level:** `Medium`

This detection was related to the use of `wmic.exe`, which can be used by attackers to gather system, process, or environment information during reconnaissance.

The second notable event was related to suspicious file creation activity on the user Desktop. The matched Sigma rule was:

- **Rule Title:** `Suspicious Creation TXT File in User Desktop`

Based on the rule characteristics and the context of the lab, this activity was associated with possible ransomware behaviour.

### Analyst Note

These findings showed how Aurora can use Sigma rules to detect suspicious endpoint behaviour and present the results in Windows Event Viewer. The first event was connected to reconnaissance activity, while the second event was related to suspicious file creation that may indicate ransomware activity.

This part of the lab demonstrates how an analyst can move from an Aurora event to the matched Sigma rule, review the rule metadata, and interpret the possible attacker behaviour.


## Key Takeaways

The main takeaways from this room were:

- EDR stands for Endpoint Detection and Response.
- EDR solutions provide endpoint visibility and support threat detection.
- Windows Event Logs are useful for investigation and detection engineering.
- ETW allows applications and drivers to produce event data.
- ETW uses controllers, providers, and consumers.
- Aurora uses Sigma rules and IOCs to detect suspicious activity.
- Aurora can write alerts to Windows Eventlog, log files, or network targets.  
- Aurora can trigger predefined or custom response actions.
- Aurora event IDs help analysts understand what type of detection occurred.
- Endpoint detection is more effective when telemetry, detection logic, and response actions work together.

---

## Summary

This Aurora EDR room covered how Windows event data, ETW, Sigma rules, IOCs, and response actions can work together to support endpoint detection and response.

The lab connected the previous Sigma Hunt work with a practical endpoint detection tool. Instead of only writing Sigma rules, I reviewed how Aurora can use those rules to generate alerts, show detections in Windows Event Viewer, and support investigation.

Overall, this room improved my understanding of endpoint telemetry, Aurora configuration, Sigma-based alerting, and how detection engineering supports SOC investigations.


