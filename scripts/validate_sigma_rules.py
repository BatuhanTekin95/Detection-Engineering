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


def validate_examples(rule_files, errors):
    fixture_path = Path("tests/rule_examples.yml")
    if not fixture_path.exists():
        errors.append(f"{fixture_path}: positive and negative rule examples are required.")
        return

    try:
        with fixture_path.open(encoding="utf-8") as handle:
            fixture_data = yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{fixture_path}: invalid YAML: {exc}")
        return

    cases = fixture_data.get("cases") if isinstance(fixture_data, dict) else None
    if not isinstance(cases, list):
        errors.append(f"{fixture_path}: cases must be a list.")
        return

    known_rules = {path.as_posix() for path in rule_files}
    coverage = {rule: set() for rule in known_rules}

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"{fixture_path}: case {index} must be a mapping.")
            continue

        rule = case.get("rule")
        expected = case.get("expected")
        event = case.get("event")

        if rule not in known_rules:
            errors.append(f"{fixture_path}: case {index} references an unknown rule: {rule}.")
            continue
        if not isinstance(expected, bool):
            errors.append(f"{fixture_path}: case {index} expected must be true or false.")
        else:
            coverage[rule].add(expected)
        if not isinstance(event, dict) or not event:
            errors.append(f"{fixture_path}: case {index} event must be a non-empty mapping.")

    for rule, outcomes in sorted(coverage.items()):
        if outcomes != {True, False}:
            errors.append(f"{fixture_path}: {rule} requires at least one positive and one negative example.")


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

    validate_examples(rule_files, errors)

    if errors:
        print("Sigma validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(rule_files)} Sigma rule file(s) and their example coverage.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
