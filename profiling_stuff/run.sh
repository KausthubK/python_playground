#!/bin/bash
sudo \
poetry run \
py-spy record -s -i -f speedscope -r 20 -o example_profile -- python ex.py