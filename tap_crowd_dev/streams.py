"""Stream type classes for tap-crowd-dev."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_crowd_dev.client import CrowdDevGetStream, CrowdDevQueryStream

TagType = th.ObjectType(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("importHash", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("deletedAt", th.DateTimeType),
    th.Property("tenantId", th.StringType),
    th.Property("createdById", th.StringType),
    th.Property("updatedById", th.StringType),
)


class Activities(CrowdDevQueryStream):
    """Activities stream."""

    name = "activities"
    path = "/activity/query"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The activity's unique identifier",
        ),
        th.Property(
            "type",
            th.StringType,
            description="The activity's type",
        ),
        th.Property(
            "timestamp",
            th.DateTimeType,
            description="The activity's timestamp",
        ),
        th.Property(
            "platform",
            th.StringType,
            description="The platform where the activity was performed",
        ),
        th.Property(
            "isContribution",
            th.BooleanType,
            description="Whether the activity is a contribution",
        ),
        th.Property(
            "score",
            th.IntegerType,
            description="The activity's score",
        ),
        th.Property(
            "sourceId",
            th.StringType,
            description="The activity's source ID",
        ),
        th.Property(
            "sourceParentId",
            th.StringType,
            description="The activity's source parent ID",
        ),
        th.Property(
            "username",
            th.StringType,
            description="The activity's username",
        ),
        th.Property(
            "objectMemberUsername",
            th.StringType,
            description="The activity's object member username",
        ),
        th.Property(
            "attributes",
            th.ObjectType(
                th.Property(
                    "state",
                    th.StringType,
                    description="The activity's state",
                ),
                th.Property(
                    "labels",
                    th.ArrayType(th.StringType),
                    description="The activity's labels",
                ),
                th.Property(
                    "reviewState",
                    th.StringType,
                    description="The activity's review state",
                ),
                th.Property(
                    "authorAssociation",
                    th.StringType,
                    description="The activity's author association",
                ),
                th.Property(
                    "additions",
                    th.IntegerType,
                    description="The activity's additions",
                ),
                th.Property(
                    "deletions",
                    th.IntegerType,
                    description="The activity's deletions",
                ),
                th.Property(
                    "changedFiles",
                    th.IntegerType,
                    description="The activity's changed files",
                ),
                th.Property(
                    "isAnswer",
                    th.BooleanType,
                    description="Whether the activity is an answer",
                ),
                th.Property(
                    "category",
                    th.StringType,
                    description="The activity's category",
                ),
            ),
            description="The activity's attributes",
        ),
        th.Property(
            "channel",
            th.StringType,
            description="The activity's channel",
        ),
        th.Property(
            "body",
            th.StringType,
            description="The activity's body",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The activity's title",
        ),
        th.Property(
            "url",
            th.StringType,
            description="The activity's URL",
        ),
        th.Property(
            "sentiment",
            th.ObjectType(
                th.Property(
                    "label",
                    th.StringType,
                    description="The activity's sentiment label",
                ),
                th.Property(
                    "mixed",
                    th.NumberType,
                    description="Whether the activity's sentiment is mixed",
                ),
                th.Property(
                    "neutral",
                    th.NumberType,
                    description="Whether the activity's sentiment is neutral",
                ),
                th.Property(
                    "negative",
                    th.NumberType,
                    description="Whether the activity's sentiment is negative",
                ),
                th.Property(
                    "positive",
                    th.NumberType,
                    description="Whether the activity's sentiment is positive",
                ),
                th.Property(
                    "sentiment",
                    th.NumberType,
                    description="The activity's sentiment",
                ),
            ),
            description="The activity's sentiment",
        ),
        th.Property(
            "importHash",
            th.StringType,
            description="The activity's import hash",
        ),
        th.Property(
            "createdAt",
            th.DateTimeType,
            description="The activity's creation timestamp",
        ),
        th.Property(
            "updatedAt",
            th.DateTimeType,
            description="The activity's last update timestamp",
        ),
        th.Property(
            "deletedAt",
            th.DateTimeType,
            description="The activity's deletion timestamp",
        ),
        th.Property(
            "memberId",
            th.StringType,
            description="The activity's member ID",
        ),
        th.Property(
            "objectMemberId",
            th.StringType,
            description="The activity's object member ID",
        ),
        th.Property(
            "conversationId",
            th.StringType,
            description="The activity's conversation ID",
        ),
        th.Property(
            "parentId",
            th.StringType,
            description="The activity's parent ID",
        ),
        th.Property(
            "tenantId",
            th.StringType,
            description="The activity's tenant ID",
        ),
        th.Property(
            "createdById",
            th.StringType,
            description="The activity's creator ID",
        ),
        th.Property(
            "updatedById",
            th.StringType,
            description="The activity's last updater ID",
        ),
    ).to_dict()

    def prepare_request_payload(
        self,
        context: dict | None,
        next_page_token: int | None,
    ) -> dict | None:
        """Prepare request payload."""
        payload = super().prepare_request_payload(context, next_page_token) or {}
        payload["orderBy"] = "createdAt_ASC"
        return payload


class Members(CrowdDevQueryStream):
    """Members stream."""

    name = "members"
    path = "/member/query"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The member's ID",
        ),
        th.Property(
            "attributes",
            th.ObjectType(),
            description="The member's attributes",
        ),
        th.Property(
            "displayName",
            th.StringType,
        ),
        th.Property(
            "emails",
            th.ArrayType(th.StringType),
            description="The member's emails",
        ),
        th.Property(
            "tenantId",
            th.StringType,
            description="The member's tenant ID",
        ),
        th.Property(
            "score",
            th.NumberType,
            description="The member's score",
        ),
        th.Property(
            "lastEnriched",
            th.DateTimeType,
        ),
        th.Property(
            "joinedAt",
            th.DateTimeType,
        ),
        th.Property(
            "importHash",
            th.StringType,
        ),
        th.Property(
            "createdAt",
            th.DateTimeType,
        ),
        th.Property(
            "updatedAt",
            th.DateTimeType,
        ),
        th.Property(
            "createdById",
            th.StringType,
        ),
        th.Property(
            "updatedById",
            th.StringType,
        ),
        th.Property(
            "reach",
            th.ObjectType(
                th.Property(
                    "total",
                    th.IntegerType,
                ),
                th.Property(
                    "github",
                    th.IntegerType,
                ),
            ),
        ),
        th.Property(
            "activeOn",
            th.ArrayType(th.StringType),
        ),
        th.Property(
            "identities",
            th.ArrayType(th.CustomType({})),
        ),
        th.Property(
            "username",
            th.ObjectType(
                th.Property(
                    "github",
                    th.ArrayType(th.StringType),
                ),
            ),
        ),
        th.Property(
            "activityCount",
            th.IntegerType,
        ),
        th.Property(
            "activityTypes",
            th.ArrayType(th.StringType),
        ),
        th.Property(
            "activeDaysCount",
            th.IntegerType,
        ),
        th.Property(
            "lastActive",
            th.DateTimeType,
        ),
        th.Property(
            "averageSentiment",
            th.NumberType,
        ),
        th.Property(
            "numberOfOpenSourceContributions",
            th.IntegerType,
        ),
        th.Property(
            "noMerge",
            th.ArrayType(th.StringType),
        ),
        th.Property(
            "toMerge",
            th.ArrayType(th.StringType),
        ),
        th.Property(
            "tags",
            th.ArrayType(TagType),
        ),
    ).to_dict()

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        """Post process the row."""
        row["activityCount"] = int(row["activityCount"])
        row["activeDaysCount"] = int(row["activeDaysCount"])

        average_sentiment = row.get("averageSentiment")
        row["averageSentiment"] = (
            float(row["averageSentiment"]) if average_sentiment else None
        )
        return row


class Organizations(CrowdDevQueryStream):
    """Organizations stream."""

    name = "organizations"
    path = "/organization/query"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("displayName", th.StringType),
        th.Property("url", th.StringType),
        th.Property("description", th.StringType),
        th.Property("parentUrl", th.StringType),
        th.Property("emails", th.ArrayType(th.StringType)),
        th.Property("phoneNumbers", th.ArrayType(th.StringType)),
        th.Property("logo", th.StringType),
        th.Property("tags", th.ArrayType(TagType)),
        th.Property("website", th.StringType),
        th.Property("location", th.StringType),
        th.Property("github", th.ObjectType(th.Property("handle", th.StringType))),
        th.Property("twitter", th.ObjectType(th.Property("handle", th.StringType))),
        th.Property("linkedin", th.ObjectType()),
        th.Property("crunchbase", th.ObjectType()),
        th.Property("employees", th.IntegerType),
        th.Property("importHash", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("deletedAt", th.StringType),
        th.Property("tenantId", th.StringType),
        th.Property("createdById", th.StringType),
        th.Property("updatedById", th.StringType),
        th.Property("isTeamOrganization", th.BooleanType),
        th.Property("type", th.StringType),
        th.Property("size", th.StringType),
        th.Property(
            "naics",
            th.ArrayType(
                th.ObjectType(
                    th.Property("sector", th.StringType),
                    th.Property("naics_code", th.StringType),
                    th.Property("subsector", th.StringType),
                    th.Property("industry_group", th.StringType),
                    th.Property("naics_industry", th.StringType),
                    th.Property("national_industry", th.StringType),
                ),
            ),
        ),
        th.Property("lastEnrichedAt", th.DateTimeType),
        th.Property("industry", th.StringType),
        th.Property("headline", th.StringType),
        th.Property("founded", th.IntegerType),
        th.Property("empployeeCountByCountry", th.ObjectType()),
        th.Property("activeOn", th.ArrayType(th.StringType)),
        th.Property(
            "identities",
            th.ArrayType(th.CustomType({})),
        ),
        th.Property("lastActive", th.DateTimeType),
        th.Property("joinedAt", th.DateTimeType),
        th.Property("memberCount", th.IntegerType),
        th.Property("activityCount", th.IntegerType),
    ).to_dict()


class Automations(CrowdDevGetStream):
    """Automations stream."""

    name = "automations"
    path = "/automation"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("type", th.StringType),
        th.Property("tenantId", th.StringType),
        th.Property("trigger", th.StringType),
        th.Property("settings", th.ObjectType()),
        th.Property("state", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("lastExecutionAt", th.DateTimeType),
        th.Property("lastExecutionState", th.StringType),
        th.Property("lastExecutionError", th.ObjectType()),
    ).to_dict()


class Tags(CrowdDevGetStream):
    """Tags stream."""

    name = "tags"
    path = "/tag"
    primary_keys = ("id",)
    replication_key = "updatedAt"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("tenantId", th.StringType),
    ).to_dict()


class Conversations(CrowdDevGetStream):
    """Conversations stream."""

    name = "conversations"
    path = "/conversation"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("activities", th.ArrayType(th.StringType)),
        th.Property("title", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("published", th.BooleanType),
        th.Property("conversationStarter", th.ObjectType()),
        th.Property("memberCount", th.IntegerType),
        th.Property("lastActive", th.DateTimeType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("tenantId", th.StringType),
    ).to_dict()
