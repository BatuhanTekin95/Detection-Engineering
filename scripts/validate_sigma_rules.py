from pathlib import Path
import sys

import yaml

REQUIRED_FIELDS = {
    "title",
    "id",
    "status",
    "description",
    "logsource",
    "detection",
    "falsepositives",
    "level",
    "tags",
}


def main():
    rule_files = sorted(Path("rules").rglob("*.yml")) + sorted(Path("rules").rglob("*.yaml"))
    errors = []
    rule_ids = {}

    if not rule_files:
        errors.append("No Sigma rule files were found under rules/.")

    for path in rule_files:
        try:
            with path.open(encoding="utf-8") as handle:
                rule = yaml.safe_load(handle)
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{path}: invalid YAML: {exc}")
            continue

        if not isinstance(rule, dict):
            errors.append(f"{path}: the document must contain a YAML mapping.")
            continue

        missing = sorted(REQUIRED_FIELDS - rule.keys())
        if missing:
            errors.append(f"{path}: missing required fields: {', '.join(missing)}")

        detection = rule.get("detection")
        if not isinstance(detection, dict) or not detection.get("condition"):
            errors.append(f"{path}: detection.condition is required.")

        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not rule_id.strip():
            errors.append(f"{path}: id must be a non-empty string.")
        elif rule_id in rule_ids:
            errors.append(f"{path}: duplicate id also used by {rule_ids[rule_id]}.")
        else:
            rule_ids[rule_id] = path

    if errors:
        print("Sigma validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(rule_files)} Sigma rule file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
