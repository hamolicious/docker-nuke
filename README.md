[![GitHub Repo stars](https://img.shields.io/github/stars/hamolicious/docker-nuke?style=flat-square&label=Github%20Stars)](https://github.com/hamolicious/docker-nuke)
[![PyPI - Version](https://img.shields.io/pypi/v/hdocker-nuke?style=flat-square)](https://pypi.org/project/hdocker-nuke/)

# docker-nuke

Quickly `kill`, then `rm` a docker container by it's name or SHA.

```bash
> docker-nuke 37
Targets Locked:
         - a530b16abd1915627cc13dd48301b291e9b374e5dcfeababace3ded44894c19e cadvisor
Fire? (y/N) y
Launching
Killing cadvisor
Removing cadvisor
All splash
```

## Install

```bash
pipx install hdocker-nuke
```
