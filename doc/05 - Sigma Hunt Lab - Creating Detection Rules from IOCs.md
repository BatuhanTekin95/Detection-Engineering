# 05 - Sigma Hunt Lab: Creating Detection Rules from IOCs

In this lab, I worked on a Sigma Hunt scenario as part of my Detection Engineering project. The main objective was to create Sigma rules based on the Indicators of Compromise provided by the Incident Response team after a ransomware incident.

<img width="1304" height="654" alt="Ekran görüntüsü 2026-07-09 005038" src="https://github.com/user-attachments/assets/6835e8a0-eb4f-4ee1-bef1-5c3113da9a41" />

> The interface provided a rule editor, a run option for testing detections, and separate challenges for each stage of the attack chain.

The scenario followed an attack chain where Incident Responders had already investigated and mitigated the incident. My role was to use the provided IOCs and event details to create detection rules that could identify similar malicious activity in the future.

The attack chain included multiple stages, starting with malicious HTA execution and continuing with payload download, reverse shell activity, privilege escalation enumeration, persistence, data collection, exfiltration, and ransomware file encryption.

For each challenge, I reviewed the provided IOC details and selected relevant detection fields such as `EventID`, `Image`, `ParentImage`, `CommandLine`, `Hashes`, and `TargetFilename`. These fields helped define what each Sigma rule needed to match.

I used the SigHunt interface to write, test, and validate Sigma rules against the provided malicious activity. The interface allowed me to submit a rule, check whether it detected the expected IOC, and review the related log entry for each attack technique.

The main skills I practised in this lab were:

* Creating Sigma rules from IOCs
* Choosing the correct detection fields
* Understanding Sigma rule structure
* Writing detection conditions
* Testing rules against malicious activity
* Reviewing related log entries
* Thinking like a Detection Engineer


### Challenge #1 - Malicious mshta Execution

In the first challenge, I created a Sigma rule to detect suspicious `mshta.exe` execution. The log showed that `mshta.exe` was launched by `chrome.exe`, which may indicate malicious HTA payload execution from a phishing link.

For this detection, I focused on the following fields:

- `EventID`
- `ParentImage`
- `Image`

The detection logic matched Sysmon process creation events where Chrome launched `mshta.exe`.

<img width="640" height="421" alt="Ekran görüntüsü 2026-07-09 005341" src="https://github.com/user-attachments/assets/8e677c87-3fa3-47f6-b9b6-2fe3f6131128" />

The rule successfully detected the malicious activity in the SigHunt interface.

**Analyst Note:**  
`mshta.exe` is a legitimate Windows binary, but attackers can abuse it to execute malicious HTA files. Seeing it launched from a browser process is unusual and should be investigated.


### Challenge #2 - Certutil Download

In the second challenge, I created a Sigma rule to detect suspicious `certutil.exe` usage. The log showed that `certutil.exe` was executed to download `nc.exe` from a remote URL.

The command line included the following suspicious options:

- `-urlcache`
- `-split`
- `-f`

This behavior is suspicious because `certutil.exe` is a legitimate Windows binary, but attackers can abuse it to download payloads or tools from external servers. In this case, it was used to download Netcat, which can later be used for reverse shell activity.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `certutil.exe` was executed with download-related command-line arguments.

<img width="621" height="277" alt="Ekran görüntüsü 2026-07-09 011519" src="https://github.com/user-attachments/assets/3bc08b6b-d25c-415e-9ae0-4f7f0e41d88e" />

The rule successfully detected the malicious certutil download activity in the SigHunt interface.

**Analyst Note:**  
`certutil.exe` is commonly available on Windows systems, which makes it useful for attackers who want to download files without bringing additional tools. Detecting suspicious command-line usage such as `-urlcache`, `-split`, and `-f` can help identify possible payload download activity.



### Challenge #3 - Netcat Reverse Shell Execution

In the third challenge, I created a Sigma rule to detect Netcat execution. The log showed that `nc.exe` was executed from the victim's temporary directory and used with the `-e` option.

This behavior is suspicious because Netcat can be abused by attackers to create a reverse shell and execute commands remotely. In this case, the command line showed Netcat being used to launch `cmd.exe`.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`
- `Hashes`

The detection logic matched process creation activity where `nc.exe` was executed with the `-e` option. I also used the provided hash as an additional detection condition.

<img width="628" height="341" alt="Ekran görüntüsü 2026-07-09 012422" src="https://github.com/user-attachments/assets/a529d2eb-6bc2-44d3-b53c-74c308f97ce6" />

The rule successfully detected the malicious Netcat reverse shell activity in the SigHunt interface.

**Analyst Note:**  
`nc.exe` is a powerful networking tool, but attackers often abuse it for reverse shells. The `-e` option is especially suspicious because it can bind a command shell to a network connection.


### Challenge #4 - PowerUp Enumeration

In the fourth challenge, I created a Sigma rule to detect PowerUp enumeration activity. The log showed that `powershell.exe` was executed with commands related to `PowerUp` and `Invoke-AllChecks`.

This behavior is suspicious because PowerUp is commonly used to enumerate Windows privilege escalation opportunities. Attackers may use it after gaining initial access to identify misconfigurations, weak service permissions, or other ways to escalate privileges.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `powershell.exe` was executed and the command line contained PowerUp-related indicators.

<img width="641" height="302" alt="Ekran görüntüsü 2026-07-09 012750" src="https://github.com/user-attachments/assets/1fdc33cd-339e-4f2f-806c-41ccbc724699" />

The rule successfully detected the PowerUp enumeration activity in the SigHunt interface.

**Analyst Note:**  
PowerShell is a legitimate administrative tool, but it is also heavily abused by attackers. In this case, the presence of `PowerUp` and `Invoke-AllChecks` in the command line indicates possible privilege escalation enumeration.


### Challenge #5 - Service Binary Modification

In the fifth challenge, I created a Sigma rule to detect suspicious service binary modification activity. The log showed that `sc.exe` was used with command-line arguments related to service configuration and `binPath`.

This behavior is suspicious because attackers can abuse service configuration permissions to change the binary path of a service. If the modified service runs with high privileges, this technique can be used for privilege escalation and execution as SYSTEM.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `sc.exe` was executed with service configuration related arguments.

<img width="646" height="328" alt="Ekran görüntüsü 2026-07-09 013145" src="https://github.com/user-attachments/assets/3fda42ee-4ef8-4a8a-8869-6a9580c75784" />

The rule successfully detected the service binary modification activity in the SigHunt interface.

**Analyst Note:**  
`sc.exe` is a legitimate Windows command-line tool for managing services. However, suspicious use of `sc.exe config` with `binPath` can indicate an attempt to modify a service executable path for privilege escalation. In this case, the command line also included `-e`, which made the activity more suspicious.

### Challenge #6 - RunOnce Persistence

In the sixth challenge, I created a Sigma rule to detect RunOnce persistence activity. The log showed that `reg.exe` was used to add a new registry value under the `RunOnce` key.

This behavior is suspicious because attackers can abuse RunOnce registry keys to execute a command or payload automatically when the user logs in again. This is a common persistence technique after initial access.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `reg.exe` was executed with command-line arguments related to adding a RunOnce registry entry.

<img width="652" height="307" alt="Ekran görüntüsü 2026-07-09 013512" src="https://github.com/user-attachments/assets/270cb674-f9ca-4a6a-8b54-dc864279d10e" />

The rule successfully detected the RunOnce persistence activity in the SigHunt interface.

**Analyst Note:**  
`reg.exe` is a legitimate Windows command-line tool, but attackers can abuse it to modify registry keys for persistence. The combination of `reg.exe`, `add`, and `RunOnce` should be reviewed because it may indicate that a payload is being configured to execute again later.


### Challenge #7 - 7-Zip Archive Collection

In the seventh challenge, I created a Sigma rule to detect suspicious archive creation with `7z.exe`. The log showed that 7-Zip was used with command-line options related to creating an archive and applying password protection.

This behavior is suspicious because attackers may collect sensitive files and compress them into an archive before exfiltration. Password-protected archives can also make inspection more difficult.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `7z.exe` was executed with archive creation and password-related arguments.

<img width="646" height="312" alt="Ekran görüntüsü 2026-07-09 013857" src="https://github.com/user-attachments/assets/23c3f263-6c12-4124-87b2-e07b8091ee51" />

The rule successfully detected the suspicious 7-Zip archive activity in the SigHunt interface.

**Analyst Note:**  
`7z.exe` is a legitimate archiving tool, but attackers can abuse it to collect and compress sensitive files before exfiltration. The use of archive creation together with password protection should be reviewed during an investigation.


### Challenge #8 - cURL Data Exfiltration

In the eighth challenge, I created a Sigma rule to detect suspicious data exfiltration activity using `curl.exe`. The log showed that `curl.exe` was used with the `-d` option, which can be used to send data to a remote server.

This behavior is suspicious because attackers may use cURL to transfer collected files or data outside the environment. In this attack chain, the archived data was exfiltrated after the collection stage.

For this detection, I focused on the following fields:

- `EventID`
- `Image`
- `CommandLine`

The detection logic matched process creation activity where `curl.exe` was executed with a data transfer related command-line argument.

<img width="628" height="303" alt="Ekran görüntüsü 2026-07-09 013953" src="https://github.com/user-attachments/assets/ee120e8a-1204-4247-8cda-a11784653c10" />

The rule successfully detected the cURL data exfiltration activity in the SigHunt interface.

**Analyst Note:**  
`curl.exe` is a legitimate command-line tool for transferring data, but it can also be abused by attackers for exfiltration. The use of `curl.exe` with data submission options such as `-d` should be investigated, especially when it follows archive creation activity.


### Challenge #9 - Ransomware File Encryption

In the final challenge, I created a Sigma rule to detect ransomware-related file encryption activity. The log showed file creation activity where the target filename used the `.huntme` extension.

This behavior is suspicious because ransomware commonly changes file extensions after encrypting files. In this case, the `.huntme` extension was used as the ransomware indicator.

For this detection, I focused on the following fields:

- `EventID`
- `TargetFilename`

The detection logic matched file creation events where the target filename ended with the `.huntme` extension.

<img width="636" height="272" alt="Ekran görüntüsü 2026-07-09 014404" src="https://github.com/user-attachments/assets/fb4eac83-814c-4701-8d19-55d7aa3b8b21" />

The rule successfully detected the ransomware file encryption activity in the SigHunt interface.

**Analyst Note:**  
Sysmon Event ID `11` represents file creation activity. Monitoring suspicious or unusual file extensions can help detect ransomware behavior, especially when many files are created or renamed with the same new extension.


## Summary

This Sigma Hunt lab focused on creating detection rules from incident response findings and provided IOCs. Across the challenges, I wrote Sigma rules for different stages of a ransomware attack chain, including initial execution, tool download, reverse shell activity, privilege escalation enumeration, persistence, collection, exfiltration, and ransomware file encryption.

The main value of this lab was understanding how attacker behaviour and IOCs can be turned into practical detection logic. Depending on the activity being detected, different fields were useful, such as `Image`, `ParentImage`, `CommandLine`, `Hashes`, and `TargetFilename`.

This exercise strengthened my practical experience with Sigma rule creation, process creation detection, command-line analysis, and ransomware-related detection engineering.


## Key Takeaways

This lab showed how Sigma rules can be created from incident response findings and IOCs. Instead of only reviewing alerts, I practised writing detection logic for different stages of a ransomware attack chain.

The key takeaways from this lab were:

- Sigma rules can be used to turn IOCs into reusable detection logic.
- Choosing the correct log source is important for rule matching.
- Process creation events are very useful for detecting suspicious tools and command-line activity.
- Fields such as `Image`, `CommandLine`, `Hashes`, and `TargetFilename` are important when writing detection rules.
- Legitimate Windows binaries such as `mshta.exe`, `certutil.exe`, `powershell.exe`, `sc.exe`, and `reg.exe` can be abused by attackers.
- Command-line arguments are often more useful than the process name alone.
- Ransomware behavior can be detected by monitoring suspicious file extensions and file creation events.
- Detection rules should not be too specific when the goal is to detect behavior instead of only one exact IOC.

## Challenge Completion Summary

| Challenge | Detection Focus | Status |
|---|---|---|
| Challenge #1 | Malicious MSHTA execution | Successfully detected |
| Challenge #2 | Certutil download activity | Successfully detected |
| Challenge #3 | Netcat reverse shell execution | Successfully detected |
| Challenge #4 | PowerUp enumeration | Successfully detected |
| Challenge #5 | Service binary modification | Successfully detected |
| Challenge #6 | RunOnce persistence | Successfully detected |
| Challenge #7 | 7-Zip archive collection | Successfully detected |
| Challenge #8 | cURL data exfiltration | Successfully detected |
| Challenge #9 | Ransomware file encryption | Successfully detected |

This lab showed how incident response findings and IOCs can be turned into practical Sigma detections that support future threat detection and SOC investigation workflows.


