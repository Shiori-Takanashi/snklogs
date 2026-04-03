import subprocess
from pathlib import Path


def get_project_root(marker_files: list[str] | None = None) -> Path:
    if marker_files is None:
        marker_files = [".git", "pyproject.toml", "uv.lock", ".python-version"]

    current = (
        Path(__file__).resolve() if "__file__" in globals() else Path.cwd().resolve()
    )

    for parent in [current] + list(current.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent

    raise FileNotFoundError("プロジェクトルートが発見できません。")


def get_tree_output(dirpath: Path, ignore_patterns: list[str] | None = None) -> str:
    cmd = ["tree", "-F", "--noreport", "--charset=ascii"]

    if ignore_patterns:
        pattern = "|".join(ignore_patterns)
        cmd.extend(["-I", pattern])

    # 変更点1: 絶対パスではなく、ディレクトリ名（例: "snklogs"）だけを指定
    cmd.append(dirpath.name)

    try:
        # 変更点2: cwd を使って、コマンドの実行起点を親ディレクトリ（例: "snk-projects"）に設定
        result = subprocess.run(
            cmd, cwd=dirpath.parent, capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing tree: {e.stderr or e}"
    except FileNotFoundError:
        return "Error: 'tree' command is not installed on this system."


def generate_tree_output_path(project_root: Path) -> Path:
    out_dir = project_root / "tree" / "outs"
    out_dir.mkdir(parents=True, exist_ok=True)

    existing_files = list(out_dir.glob("tree*.txt"))

    max_num = 0
    for file in existing_files:
        name_part = file.stem.replace("tree", "")
        if name_part.isdigit():
            max_num = max(max_num, int(name_part))

    next_num = max_num + 1
    new_filename = f"tree{next_num:02d}.txt"

    return out_dir / new_filename


def main():
    # 無視するディレクトリ・ファイルの統合リスト
    ignore_list = [
        ".git",
        ".venv",
        "venv",
        "env",
        "__pycache__",
        ".ruff_cache",
        ".mypy_cache",
        ".pytest_cache",
        "node_modules",
        "build",
        "dist",
        "tree",  # 出力先ディレクトリ自身の除外
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".DS_Store",
        "*.log",
        "*.bak",
        "*.swp",
        "*.tmp",
    ]

    try:
        root_path = get_project_root()
        print(f"Project Root: {root_path}")

        output_file = generate_tree_output_path(root_path)

        print("Generating tree...")
        tree_text = get_tree_output(root_path, ignore_list)

        if tree_text.startswith("Error"):
            print("Failed to generate tree.")
            print(tree_text)
            return

        output_file.write_text(tree_text, encoding="utf-8")
        print(f"Successfully saved to: {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
