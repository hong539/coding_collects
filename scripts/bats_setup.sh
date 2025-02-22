#!/usr/bin/env bash
set -euxo pipefail

git clone https://github.com/bats-core/bats-core
cd bats-core/
sudo ./install.sh /usr/local