#!/usr/bin/python3
"""load json"""
import json


def load_from_json_file(filename):
    """load json"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
