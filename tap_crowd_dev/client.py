"""REST client handling, including CrowdDevStream base class."""

from __future__ import annotations

import typing as t

from singer_sdk import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers._typing import TypeConformanceLevel
from singer_sdk.pagination import BaseAPIPaginator, BaseOffsetPaginator

if t.TYPE_CHECKING:
    from requests import Response


class CrowdDevStream(RESTStream):
    """Crowd Dev stream class."""

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    @property
    def url_base(self) -> str:
        """Return the API URL root."""
        return f"https://app.crowd.dev/api/tenant/{self.config['tenant_id']}"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        token: str = self.config["token"]
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=token,
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        return {"User-Agent": f"{self.tap_name}/{self._tap.plugin_version}"}


class CrowdDevPaginator(BaseOffsetPaginator):
    """Crowd Dev paginator."""

    def has_more(self, response: Response) -> bool:
        """Return True if there are more pages to fetch."""
        data = response.json()
        return data["offset"] < data["count"]


class CrowdDevQueryStream(CrowdDevStream):
    """Crowd Dev stream class with default implementation for query streams."""

    page_size = 100
    records_jsonpath = "$.rows[*]"
    rest_method = "POST"

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Return a new paginator object."""
        return CrowdDevPaginator(start_value=0, page_size=self.page_size)

    def prepare_request_payload(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: t.Any | None,
    ) -> dict | None:
        """Prepare request payload."""
        return {
            "limit": self.page_size,
            "offset": next_page_token,
        }
