"""Update the mods database from git history."""

import subprocess


def update_history(db_path: str = "mods.db", data_path: str = "data.json") -> None:
    """
    Update the mods database using git-history.
    
    Args:
        db_path: Path to the SQLite database
        data_path: Path to the JSON data file
    """
    subprocess.run([
        "git-history", "file", db_path, data_path,
        "--id", "id"
    ], check=True)


def main():
    """CLI entry point."""
    update_history()
    print("Updated mods.db from git history")


if __name__ == "__main__":
    main()
