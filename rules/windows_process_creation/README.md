# Sigma Rules

These rules were created from behaviours reviewed in the Sigma Hunt ransomware scenario. They are standalone learning examples intended for review, conversion, testing, and tuning.

## Windows Process Creation

| File | Behaviour | MITRE ATT&CK |
|---|---|---|
| [mshta_from_browser.yml](mshta_from_browser.yml) | A common browser launches `mshta.exe` | T1218.005 |
| [certutil_suspicious_download.yml](certutil_suspicious_download.yml) | Certutil uses common remote download options | T1105 |
| [netcat_reverse_shell.yml](netcat_reverse_shell.yml) | A Netcat-compatible process launches a Windows shell with `-e` | T1059.003 |
| [powerup_invoke_allchecks.yml](powerup_invoke_allchecks.yml) | PowerUp runs `Invoke-AllChecks` from PowerShell | PowerSploit S0194 |
| [service_binpath_modification.yml](service_binpath_modification.yml) | `sc.exe` modifies a service binary path | T1543.003 |
| [runonce_registry_persistence.yml](runonce_registry_persistence.yml) | `reg.exe` adds a RunOnce value | T1547.001 |
| [password_protected_7zip_archive.yml](password_protected_7zip_archive.yml) | 7-Zip creates a password-protected archive | T1560.001 |
| [curl_data_exfiltration.yml](curl_data_exfiltration.yml) | cURL submits data to a remote URL | T1041 |

## Windows File Events

| File | Behaviour | MITRE ATT&CK |
|---|---|---|
| [ransomware_huntme_file_creation.yml](../windows_file_event/ransomware_huntme_file_creation.yml) | A file is created with the lab-specific `.huntme` extension | T1486 |

## Tuning Notes

- Review parent-child process relationships and complete command lines during triage.
- Confirm that the required process creation and file event fields are available in the target telemetry.
- Consider approved administration, software deployment, backups, API testing, and penetration-testing activity.
- Backend field mappings and case sensitivity can change the generated query.
- Test converted queries against representative positive and negative events before deployment.

## Validation and Examples

The repository workflow checks YAML syntax, required metadata, unique rule IDs, example coverage, and the official Sigma JSON schema. Positive and negative event examples are stored in [`tests/rule_examples.yml`](../../tests/rule_examples.yml).

The rules remain marked as experimental until they have been tested and tuned for a specific environment.
