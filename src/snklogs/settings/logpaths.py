from datetime import datetime
from pathlib import Path

DIR_NAME = "logs"
FILE_NAME_OF_BASE = "app.log"


def build_filepath(
    dirname: str = DIR_NAME, filename_of_base: str = FILE_NAME_OF_BASE
) -> Path:
    root_path = find_project_root(Path(__file__))
    dirpath = _ensure_dirpath(root_path, dirname)
    filename = _ensure_filename(filename_of_base)
    filepath = dirpath / filename
    with open(filepath, "w", encoding="utf-8"):
        pass
    return filepath


def find_project_root(path: Path, count: int = 0) -> Path:
    # 最初にパスを絶対パスに固定する
    if count == 0:
        path = path.resolve()

    if path.is_file():
        path = path.parent

    # 判定ロジック
    if (path / ".git").is_dir() or (path / "pyproject.toml").exists():
        return path

    # 終了判定
    if count >= 99:
        raise FileNotFoundError(
            "プロジェクトルートが発見できません（探索上限到達）。"
        )

    if path == path.parent:
        raise FileNotFoundError(
            "システムルートまで捜索しましたが、プロジェクトルートが見つかりませんでした。"
        )

    # 【重要】 return をつけて結果を上の階層に返す
    return find_project_root(path.parent, count + 1)


def _ensure_dirpath(root_path: Path, dirname: str) -> Path:
    try:
        dirpath = (root_path / dirname).resolve(strict=False)
    except OSError as e:
        raise ValueError(f"OSErrorが発生しました: {dirname}") from e

    except RuntimeError as e:
        raise ValueError(
            f"RuntimeError が発生しました: {dirname}"
        ) from e

    dirpath.mkdir(parents=True, exist_ok=True)

    return dirpath


def _ensure_filename(basename: str) -> str:
    if basename.count(".") != 1:
        raise ValueError("basenameは'.'を一つだけ含んでください。")

    (stem, extension) = basename.split(".")
    return f"{stem}-{datetime.now():%Y%m%d}.{extension}"
