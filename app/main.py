"""Utilities for copying files with a simple ``cp`` command."""

import shutil


def copy_file(command: str) -> None:
    """Copy a file when command has the form ``cp source target``."""
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source_file_name, target_file_name = command_parts
    if source_file_name == target_file_name:
        return

    try:
        shutil.copyfile(source_file_name, target_file_name)
    except OSError:
        return
