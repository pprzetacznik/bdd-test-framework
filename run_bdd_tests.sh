#!/bin/bash

set -xe

export TESTS_VERBOSE=false
export TESTS_MARKERS="(feature or e2e) and not ignore"

python \
  -m pytest \
  -m "$TESTS_MARKERS" \
  --gherkin-terminal-reporter \
  --cov-report term \
  --cov=my_app \
  -svvv

