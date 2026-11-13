# AI Coding Agent

A Python learning project that explores how an LLM can inspect and edit a small
codebase through function calls. The included calculator is the working example,
not a production application or a secure execution sandbox.

## How it works

[main.py](main.py) sends the user's prompt and conversation history to Gemini,
dispatches requested tools, and feeds their results into the next turn. The loop
stops on a text response or after 20 iterations.

[call_function.py](call_function.py) maps model requests to four explicit tools:
list files, read a file, write a file, and run Python. [config.py](config.py)
selects the working directory. Keeping this dispatch explicit makes it possible
to inspect which operations the model can request.

**Safety tradeoff:** directory checks and a subprocess timeout are not process
isolation. Generated Python can act with the host process's permissions. Use a
disposable environment with no personal files or production credentials; do not
expose this agent as a public service.

## Run locally

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/). From the repository root:

```bash
uv sync --locked
# Set GEMINI_API_KEY in your environment; never commit the key.
uv run main.py "Explain how the calculator evaluates expressions" --verbose
```

The current code selects `gemini-2.0-flash-001`. Access depends on Google's model
availability and your account; an offline test does not verify that API access.
API calls may incur charges. There is no hosted public demo.

## Tests and limitations

Run the calculator's assertion-based tests without an API key:

```bash
python -m unittest discover -s calculator -p tests.py -v
```

The root [tests.py](tests.py) currently prints tool results rather than asserting
them, so it is a diagnostic script, not evidence that tool execution is correct.
Next improvements are assertion-based tool tests and isolated execution before
using untrusted prompts or code.
