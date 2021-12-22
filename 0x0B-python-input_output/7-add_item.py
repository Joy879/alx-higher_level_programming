#!/usr/bin/python3
"""add json to a file"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    File = load_from_json_file("add_item.json")
except Exception:
    File = []

for idx in range(1, len(sys.argv)):
    File.append(sys.argv[idx])
save_to_json_file(File, "add_item.json")
