#!/usr/bin/env bash
set -euxo pipefail

# coding practice sources configure
# Working Locally
# docs: https://exercism.org/docs/using/solving-exercises/working-locally
wget https://github.com/exercism/cli/releases/download/v3.5.4/exercism-3.5.4-linux-x86_64.tar.gz

tar -xf exercism-3.5.4-linux-x86_64.tar.gz

mkdir -p ~/bin
mv exercism ~/bin
# ~/bin/exercism

[[ ":$PATH:" == *":$HOME/bin:"* || ":$PATH:" == *":~/bin:"* ]] && echo "~/bin is in PATH" || echo "~/bin is not in PATH"

#If the above prints ~/bin is not in PATH let’s add ~/bin to $PATH and reload Bash configuration:
echo 'export PATH=~/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

exercism configure --token=<your-api-token>
exercism configure --workspace=$(pwd)/exercism_workspace