# `tap-crowd-dev`

Singer tap for [CrowdDev](https://crowd.dev).

Built with the [Meltano Singer SDK](https://sdk.meltano.com).

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Streams

Implemented:

* `activities`
* `members`
* `organizations`

Planned:

* `automations`
* `conversations`
* `notes`
* `tags`
* `tasks`

Log an issue if you need a stream that isn't listed here. PRs welcome!

## Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| tenant_id           | True     | None    | Tenant ID for Crowd Dev |
| token               | True     | None    | API Token for Crowd Dev |
| start_date          | False    | None    | Earliest datetime to get data from |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |
| batch_config        | False    | None    |             |

A full list of supported settings and capabilities is available by running: `tap-crowd-dev --about`

## Usage

You can easily run `tap-crowd-dev` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-crowd-dev --version
tap-crowd-dev --help
tap-crowd-dev --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-crowd-dev` CLI interface directly using `poetry run`:

```bash
poetry run tap-crowd-dev --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-crowd-dev
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-crowd-dev --version
# OR run a test `elt` pipeline:
meltano run tap-crowd-dev target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
