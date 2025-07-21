# Rust Server on Modal

this is a simple rust server that runs on [modal](https://modal.com).

1. install [uv](https://docs.astral.sh/uv/getting-started/installation/)

2. `uv sync`

3. activate venv

   ```bash
   source .venv/bin/activate
   ```

4. run the server
   ```bash
   modal serve --env <your-env-name> modal_run.py
   ```

this will give you the URL to access the server. visiting it should return "Hello, world!"
