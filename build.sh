#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"

ln -sf "$PWD" code

make install && make collectstatic && make migrate