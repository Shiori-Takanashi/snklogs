from datetime import datetime
from pathlib import Path

from ..settings.constants import DIR_NAME, FILE_NAME_OF_BASE


def build_filepath(
    dirpath_of_base: Path,
    filename_of_base: str | None = None,
    dirname: str | None = None,
    dirnames: tuple[str, ...] | None = None,
) -> Path:

    # ----------------------------------
    # 1. ファイル名についての処理
    # ----------------------------------

    # True -> Use Argument
    if filename_of_base is not None:
        filename = _ensure_filename_with_stamp(filename_of_base)

    # False -> Use Default
    else:
        filename = _ensure_filename_with_stamp(FILE_NAME_OF_BASE)

    # ----------------------------------
    # 2. ディレクトリについての処理
    # ----------------------------------

    # True & True -> Error
    if (dirname is not None) and (dirnames is not None):
        raise ValueError("dirnameとdirnamesの片方だけ指定せよ。")

    # True & False -> Use Argument
    elif (dirname is not None) and (dirnames is None):
        dirpath = _ensure_dirpath_from_dirname(dirpath_of_base, dirname)

    # False & True -> Use Argument
    elif dirname is None and dirnames is not None:
        dirpath = _ensure_dirpath_from_dirnames(dirpath_of_base, *dirnames)

    # False & False -> Use Default
    else:
        dirpath = _ensure_dirpath_from_dirname(dirpath_of_base, DIR_NAME)

    return dirpath / filename


def _ensure_dirpath_from_dirname(dirpath_of_base: Path, dirname: str) -> Path:
    try:
        dirpath = (dirpath_of_base / dirname).resolve(strict=False)
        dirpath.mkdir(parents=True, exist_ok=True)
        return dirpath
    except TypeError:
        raise
    except PermissionError:
        raise
    except FileExistsError:
        raise
    except NotADirectoryError:
        raise
    except Exception:
        raise


def _ensure_dirpath_from_dirnames(
    dirpath_of_base: Path, *dirnames: str
) -> Path:
    try:
        dirpath = dirpath_of_base.joinpath(*dirnames).resolve(strict=False)
        dirpath.mkdir(parents=True, exist_ok=True)
        return dirpath
    except TypeError:
        raise
    except PermissionError:
        raise
    except FileExistsError:
        raise
    except NotADirectoryError:
        raise
    except Exception:
        raise


def _ensure_filename_with_stamp(filename_of_base: str) -> str:
    try:
        p = Path(filename_of_base)
    except TypeError:
        raise

    msg = "ログファイルの命名が不適切です"
    if p.name == "":
        raise ValueError(f"{msg}: {p.name}")

    if p.stem == "":
        raise ValueError(f"{msg}: {p.stem}")

    if p.suffix == "":
        raise ValueError(f"{msg}: {p.suffix}")

    return f"{p.stem}-{datetime.now():%Y%m%d}{p.suffix}"
