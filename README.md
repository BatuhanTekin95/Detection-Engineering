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
