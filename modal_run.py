import subprocess

import modal

app = modal.App("rust-server")

PORT = 8000
REMOTE_PATH = "/root/rust-server"

image = (
    modal.Image.debian_slim()
    .apt_install("curl")
    # install rust
    .run_commands(
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"
    )
    .add_local_dir("src", f"{REMOTE_PATH}/src", copy=True)
    .add_local_file("Cargo.toml", f"{REMOTE_PATH}/Cargo.toml", copy=True)
    .workdir(REMOTE_PATH)
    # build the rust server binary
    .run_commands("$HOME/.cargo/bin/cargo build --release")
)


@app.function(
    image=image,
    min_containers=1,
)
@modal.web_server(PORT)
def my_file_server():
    subprocess.Popen(f"./target/release/rust-server-modal {PORT}", shell=True)
