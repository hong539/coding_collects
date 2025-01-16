#!/bin/env bash

poetry init
pyenv local 3.10.14
poetry env use 3.10.14

# poetry shell