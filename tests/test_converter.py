import json
import pathlib

import jsonschema
import pytest

from iam_policy_validate_sarif import converter


@pytest.mark.parametrize(
    "policy",
    [
        ("arn-region-not-allowed.policy.json"),
        ("redundant-action.policy.json"),
    ],
)
def test_convertor(policy):
    policy_path = f"tests/data/policy_checks/{policy}"
    sarif_path = f"tests/data/policy_checks/sarif/{policy}"

    with open("tests/data/sarif-schema-2.1.0.json") as schema_file:
        schema = json.load(schema_file)

    with open(f"{policy_path}.findings") as data:
        findings = json.load(data)["findings"]

    sarif_converter = converter.SarifConverter(pathlib.Path(policy_path))
    sarif = json.loads(sarif_converter.convert(findings))
    print(json.dumps(sarif))

    with open(f"{sarif_path}.findings.sarif") as data:
        expected_sarif = json.load(data)

    assert sarif == expected_sarif
    jsonschema.validate(sarif, schema)
