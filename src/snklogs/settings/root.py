from pathlib import Path


def find_project_root(
    path: Path | None = None, count: int = 0, limit: int = 24
) -> Path:
    if path is None:
        path = Path(__file__).parent.resolve()

    if count == 0:
        path = path.resolve()

    if path.is_file():
        path = path.parent

    # 判定ロジック
    if (path / ".git").is_dir():
        return path

    if (path / ".venv").is_dir():
        return path

    if (path / "venv").is_dir():
        return path

    # 終了判定
    if count >= limit:
        raise FileNotFoundError("プロジェクトルートが発見できません(limit到達)")

    if path == path.parent:
        raise FileNotFoundError("プロジェクトルートが発見できません(root到達)")

    # 【重要】 return をつけて結果を上の階層に返す
    return find_project_root(path.parent, count + 1)
