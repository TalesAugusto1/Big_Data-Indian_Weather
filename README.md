# Big Data - Indian Weather

Course brief (rubric): [core.md](core.md).

## Project planning: milestones, storys, and tasks

The team tracks work in Markdown under **[storyline/](storyline/)**. That folder matches the course structure in `core.md` (**Parte 1–3** as **stories** `S01`–`S03`, gated by **milestones** `M01`–`M04`, broken into **tasks** `T010`, `T020`, …).

| Start here | Role |
|------------|------|
| [storyline/README.md](storyline/README.md) | Workflow diagram, ID conventions, status meanings, data paths |
| [storyline/milestones/README.md](storyline/milestones/README.md) | Ordered milestones (what must be true before the next phase) |
| [storyline/storys/README.md](storyline/storys/README.md) | Stories = Parte 1, 2, 3; acceptance criteria and task tables |
| [storyline/tasks/README.md](storyline/tasks/README.md) | Full task index by milestone and story |

### How to follow the workflow

1. Open the **active milestone** in [storyline/milestones/README.md](storyline/milestones/README.md) (work **M01** before leaning on **M02**, and so on).
2. Open the **story** linked from that milestone in [storyline/storys/](storyline/storys/) and read acceptance criteria and the task table.
3. Open individual **task** files from [storyline/tasks/](storyline/tasks/) in dependency order: each file has `depends_on:` in its YAML block (for example finish **T010** before **T011**).
4. When every task for the milestone is done and the milestone exit criteria are met, treat the milestone as complete and move to the next one.

### How to complete a task (checklist)

For each file such as [storyline/tasks/T010-docker-compose-stack.md](storyline/tasks/T010-docker-compose-stack.md):

1. **Read** `depends_on` — do not skip prerequisite tasks unless the team explicitly repoints dependencies.
2. **Do the work** described in **Objetivo** and tick the **Checklist** boxes in the Markdown body (you can use `- [x]` when an item is done).
3. **Update the YAML block** at the top: set `status:` to `Doing` while in progress, `Blocked` if waiting on something external (for example professor approval), then `Done` when finished.
4. **Fill Evidence**: add paths or links to notebooks, `docker/` files, logs, PRs, or screenshots so reviewers can verify the task without guesswork.
5. **Produce artifacts** listed under `artifacts:` (create the paths if they do not exist yet).
6. Optionally update the **Owner** / **Status** column for that task in the parent [storyline/storys/](storyline/storys/) file so the story table matches reality.

**Status values** (see also [storyline/README.md](storyline/README.md)): `Todo`, `Doing`, `Blocked`, `Done`.

**Dataset paths** (for task context): `data/Indian_Weather_Dataset.parquet`; optional CSV: `data/archive/Indian_Weather_Dataset.csv`.

## Python virtual environment

Use a virtual environment so dependencies stay isolated from your system Python.

### Prerequisites

- Python 3 installed and available as `python` (or `python3` on macOS/Linux).

### Create the venv (once per clone)

From the repository root:

```bash
python -m venv .venv
```

On some systems use `python3`:

```bash
python3 -m venv .venv
```

### Activate the venv

**Windows - PowerShell**

```powershell
Set-Location path\to\BigData
.\.venv\Scripts\Activate.ps1
```

If activation is blocked by execution policy, allow scripts for your user (one-time):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows - Command Prompt**

```bat
cd /d path\to\BigData
.venv\Scripts\activate.bat
```

**macOS / Linux - bash or zsh**

```bash
cd path/to/BigData
source .venv/bin/activate
```

When the venv is active, your shell prompt usually shows `(.venv)`.

### Install dependencies

With the venv activated:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### How to run (CSV to Parquet)

From the repo root, with the venv activated and dependencies installed:

```powershell
Set-Location c:\Desenvolvimento\BigData
pip install -r requirements.txt
python scripts\csv_to_parquet.py
```

On macOS/Linux, use forward slashes:

```bash
cd /path/to/BigData
pip install -r requirements.txt
python scripts/csv_to_parquet.py
```

**Optional flags**

| Flag | Description |
|------|-------------|
| `-i` / `--input` | Input CSV path |
| `-o` / `--output` | Output Parquet path |
| `--compression` | `snappy`, `zstd` (default), `gzip`, `lz4`, or `brotli` |
| `--read-block-mib N` | CSV parser block size in MiB (default: `8`) |

**Example with explicit paths (Windows)**

```powershell
python scripts\csv_to_parquet.py -i data\archive\Indian_Weather_Dataset.csv -o data\archive\Indian_Weather_Dataset.parquet
```

**Example (macOS/Linux)**

```bash
python scripts/csv_to_parquet.py -i data/archive/Indian_Weather_Dataset.csv -o data/archive/Indian_Weather_Dataset.parquet
```

The script was smoke-tested on a small CSV. A full run on the real Indian Weather CSV can take a long time because the source file is very large.

### Deactivate

```bash
deactivate
```

### Editor (VS Code / Cursor)

Choose the interpreter `.venv\Scripts\python.exe` (Windows) or `.venv/bin/python` (macOS/Linux): **Python: Select Interpreter** in the Command Palette so terminals and debugging use this environment.
