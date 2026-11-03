#!/usr/bin/env bash
unset PYTHONPATH
unset PYTHONHOME
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV

exec /YOUR/PATH/TO/YOUR/VIRTUAL/ENVIRONMENT/GOES/HERE/bin/python -Xfrozen_modules=off -m ipykernel_launcher "$@"
