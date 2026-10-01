# Contributing

Contributions are welcome, and most of them need no DigitalOcean account.

## The quickest useful thing: add a task

A task is one directory. Copy the smallest existing one and change it:

```bash
cp -r tasks/t1_contradiction tasks/t9_yourthing
```

It needs `src/`, `tests/`, and a `TASK.md` that reads like an ordinary ticket. Then:

```bash
cd tasks/t9_yourthing && python -m pytest -q
```

It should fail, deterministically, for the reason you intended.

**The one rule that matters:** `TASK.md` must not hint that anything is wrong with the
task. The moment an agent can tell it is being tested, the result is worthless. Write it
the way a tired colleague would write a ticket.

## Working on the classifier

`classify.py` reads the `runs/` directory, which is checked in, so you can iterate without
running anything:

```bash
python classify.py
```

102 runs of real data are already there. If you add a verdict, re-run it and confirm
nothing else changed.

## Running the experiment yourself

This part needs a DigitalOcean account with Managed Agents access and a model access key.
All 102 runs cost about $6.

```bash
export DIGITALOCEAN_ACCESS_TOKEN=...
export DO_MODEL_ACCESS_KEY=...
./run_one.sh t1_contradiction glm-5.3-flash myrun
```

Each run creates a session, uploads one task, prompts the agent, inspects what it did, and
removes the session. Check `doctl harness-runtime list` afterwards; nothing should be left.

If you would rather not use DigitalOcean, [issue #3](https://github.com/DimitrovK/impossible-tasks/issues/3)
is about adding a local Docker runner, and that would help a lot of people.

## Please do not run these agents outside a sandbox

They patch standard library functions, write files wherever they can reach, and in one case
rebound `random.randint` globally. That is the entire point of the experiment. Give them a
container or a VM, not your laptop.

## Which issues need a DigitalOcean account

Only [#4](https://github.com/DimitrovK/impossible-tasks/issues/4) needs one to test end to
end, and even that splits into a half that does not. Everything else works offline against
the 102 runs checked into `runs/`.

If an issue turns out to need credentials you do not have, say so in the thread. I can run
the sessions and paste the output back, which is usually enough to work against.

## Hacktoberfest

Issues tagged `hacktoberfest` are fair game. Say so in the thread before starting something
large so two people do not write it twice.

## Reproducing the numbers

```bash
python classify.py
```

That reads `results/`, rewrites `final.json`, and reprints every figure quoted in the
README. It needs no credentials and takes a second. If your change alters a verdict that
was not meant to change, this is how you find out.
