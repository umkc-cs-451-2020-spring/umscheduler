<h1 align="center">UMScheduler</h1>
<div align="center">
  <strong>
    A course scheduling application for the UM system.
  </strong>
</div>

<br />

## Installation

```sh
cd umscheduler
cargo build --release
```

## Members and Contributors

```md
Samuel Lim
Zach Zoltek
Alivia Dutcher
Yazdan Riazi
```

## Problem

The prompt we have chosen is course scheduling, under the supervision of Gina Campbell.

## Documentation

### Internal

Files concerning group discussion, meetings, iterations and more can be found under the `documentation` folder.

### Usage

Automated documentation sourced from source comments and function signatures can tentatively be found within the automated docs.

To source these documents, first build them with the following command:

```sh
cargo doc --release --no-deps
```
