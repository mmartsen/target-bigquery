"""Tests standard target features using the built-in SDK tests library."""

import os

from singer_sdk.testing import get_target_test_class

from target_bigquery.target import TargetBigQuery


TestTargetBigquery = get_target_test_class(
        TargetBigQuery,
        config={
            "credentials_json": os.environ["BQ_CREDS"],
            "project": os.environ["BQ_PROJECT"],
            "dataset": os.environ["BQ_DATASET"],
            "location": os.environ["BQ_LOCATION"],
        },
    )
