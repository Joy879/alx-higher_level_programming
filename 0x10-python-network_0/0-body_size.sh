#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:50
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f 2
