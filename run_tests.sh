#!/bin/bash

set -xe

python \
  -m pytest \
  tests/test_users.py -svv
