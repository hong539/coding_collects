# coding_collects
codesignal code colletcs for practice coding with any other Programming languages

## Setting up dev_enviroment on Linux

* [programing_languages](https://github.com/hong539/setup_dev_environment/tree/main/programing_languages)

## Start coding

* With Python

```shell
#!/usr/bin/env bash
set -euxo pipefail

#install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version

#generate-shell-completion
echo -e 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
source ~/.bashrc

#init
uv init

#dependencies check
uv pip check

#sync
uv sync

#Use a specific Python version in the current directory:
uv python pin 3.10

#Viewing Python installations
uv python list

#Importing dependencies
#docs: https://docs.astral.sh/uv/concepts/projects/dependencies/#importing-dependencies
uv add -r requirements.txt

# add some Python packages
uv add fastapi --extra standard
```

## many others

* kotlin
    * map/reduce/filter

## Important!!!

== We're Using GitHub Under Protest ==

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project.  We have an
[open {bug ticket, mailing list thread, etc.} ](INSERT_LINK) where the
project contributors are actively discussing how we can move away from GitHub
in the long term.  We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

If you are a contributor who personally has already quit using GitHub, please
[check this resource](INSERT_LINK) for how to send us contributions without
using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub's use of this project's
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)
