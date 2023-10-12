"""Crowd Dev tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_crowd_dev import streams


class TapCrowdDev(Tap):
    """Singer tap for Crowd Dev."""

    name = "tap-crowd-dev"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "tenant_id",
            th.StringType,
            required=True,
            description="Tenant ID for Crowd Dev",
        ),
        th.Property(
            "token",
            th.StringType,
            required=True,
            secret=True,
            description="API Token for Crowd Dev",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Crowd Dev streams.
        """
        return [
            streams.Activities(tap=self),
            streams.Members(tap=self),
            streams.Organizations(tap=self),
            streams.Automations(tap=self),
            streams.Tags(tap=self),
        ]
