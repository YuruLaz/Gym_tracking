# Gym Tracker API — TODO

Work top to bottom. One step at a time; get it reviewed before moving on.

## Phase 0 — Environment (done)
- [x] Project folder in WSL filesystem
- [x] `git init`, branch `main`
- [x] venv created + activated, FastAPI installed
- [x] VS Code connected to WSL, Python extension + interpreter set

## Phase 1 — Hello world + first commit
- [ ] `pip install uvicorn`
- [ ] Re-run `pip freeze > requirements.txt` (check uvicorn is in it)
- [ ] Finish `.gitignore` (at least `venv/`, `__pycache__/`, `.env`)
- [ ] Decide file layout: where does the FastAPI `app` object live? (e.g. `app/main.py`) — what's `routers.py` for?
- [ ] Write one trivial route yourself
- [ ] Run it with uvicorn, open `/docs`, call the route
- [ ] `git status` — check only the files you expect are staged
- [ ] First commit on `main`

## Phase 2 — GitHub
- [ ] Create an **empty** repo on GitHub (no README / .gitignore / license)
- [ ] Add remote, push `main`
- [ ] Open GitHub Issues for each feature below

## Phase 3 — Decisions before writing models
Draft your own answer + reasoning for each, then review together:
- [ ] SQLite or Postgres?
- [ ] Alembic or `create_all()`?
- [ ] Project structure: models / schemas / routers / db session — which files?
- [ ] "Best lift" = heaviest single set, or highest volume (weight × reps)?

## Phase 4 — Features (one branch + PR each)
- [ ] **Exercise CRUD** — name, muscle group, equipment
- [ ] **Workouts** — create a session (date), add exercises to it (join table)
- [ ] **Sets** — reps/weight per workout-exercise, total volume, PRs
- [ ] **Progress queries** — history, best lift per exercise (`JOIN` / `GROUP BY` / `MAX`)

Per feature: Issue → branch → write your approach first → code → self-review diff → PR → merge.

## Later
- [ ] Auth (deliberate practice, not required)
- [ ] Phase 2: LLM layer — summaries / trends; AI output clearly separated from recorded data
