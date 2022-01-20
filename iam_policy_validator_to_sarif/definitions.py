from enum import Enum


POLICY_TYPES = Enum(
    "POLICY_TYPES",
    (
        "IDENTITY_POLICY",
        "RESOURCE_POLICY",
        "SERVICE_CONTROL_POLICY",
    ),
)

LOCALES = Enum(
    "LOCALES",
    (
        "DE",
        "EN",
        "ES",
        "FR",
        "IT",
        "JA",
        "KO",
        "PT_BR",
        "ZH_CN",
        "ZH_TW",
    ),
)

RESOURCE_TYPES = Enum(
    "RESOURCE_TYPES",
    (
        "AWS::S3::Bucket",
        "AWS::S3::AccessPoint",
        "AWS::S3::MultiRegionAccessPoint",
        "AWS::S3ObjectLambda::AccessPoint",
    ),
)
