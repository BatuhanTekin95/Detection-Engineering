# Windows Process Creation Rules

These Sigma rules were created from behaviours reviewed in the Sigma Hunt ransomware scenario. They are standalone learning examples intended for review, conversion, testing, and tuning.

| File | Behaviour | Data Source | MITRE ATT&CK |
|---|---|---|---|
| mshta_from_browser.yml | A common browser launches mshta.exe | Windows process creation | T1218.005 |
| certutil_suspicious_download.yml | Certutil uses common remote download options | Windows process creation | T1105 |
| netcat_reverse_shell.yml | A Netcat-compatible process launches a Windows shell with -e | Windows process creation | T1059.003 |

## Tuning Notes

- Review parent-child process relationships and full command lines during triage.
- Confirm that the required process creation fields are available in the target telemetry.
- Consider approved administration, software deployment, troubleshooting, and penetration-testing activity.
- Backend field mappings and case sensitivity can change the generated query.
- Test converted queries against representative positive and negative events before deployment.

## Current Limitations

- Browser-launched MSHTA variants using an intermediate process may not match the MSHTA rule.
- Certutil variants using different switches or syntax may not match the Certutil rule.
- Netcat variants using other execution options, renamed binaries, or indirect shell launching may not match the Netcat rule.

The rules remain marked as experimental until they have been tested and tuned for a specific environment.
