#!/bin/bash

source venv/Scripts/activate

python -m pytest

if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi