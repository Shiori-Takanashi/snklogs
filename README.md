# snklogs

Python 向けのロギング設定ライブラリです。

---

## デザインパターン解説

このコードベースで使われている主なデザインパターンを説明します。

---

### 1. Builder パターン (`LoggerBuilder`)

**場所:** `src/snklogs/factory.py`

**目的:**
オブジェクトの生成手順を段階的に組み立て、最終的に完成品を返す。
生成の各ステップを独立したメソッドとして定義することで、柔軟な構成が可能になる。

**コード例:**

```python
import logging

class LoggerBuilder:
    def __init__(self, logger_name: str) -> None: ...

    def add_stream_handler(self) -> "LoggerBuilder": ...  # ステップ1
    def add_file_handler(self) -> "LoggerBuilder": ...    # ステップ2
    def build(self) -> logging.Logger: ...                # 完成品を返す
```

**ポイント:**
- 各 `add_*` メソッドが `self` を返すことで **メソッドチェーン (Fluent Interface)** を実現している。
- ハンドラの追加・省略・順序変更を呼び出し側が自由に制御できる。

---

### 2. Director パターン (`configure_logging`)

**場所:** `src/snklogs/factory.py`

**目的:**
Builder の呼び出し順序（構築手順）をカプセル化し、利用者が個々のステップを意識しなくてもよい状態にする。
GoF では Builder と Director はセットで語られることが多い。

**コード例:**

```python
def configure_logging(logger_name: str) -> None:
    (
        LoggerBuilder(logger_name)
        .add_stream_handler()
        .add_file_handler()
        .build()
    )
```

**ポイント:**
- 「ストリームハンドラ → ファイルハンドラ」という構築手順の責務がここに集中している。
- 別の構築手順が必要になった場合は、新たな Director 関数を追加するだけでよい。

---

### 3. Factory 関数 / ヘルパー関数群 (`core/`, `settings/`)

**場所:** `src/snklogs/core/formatters.py`, `handlers.py`, `levels.py`, `src/snklogs/settings/logpaths.py`

**目的:**
特定の型のオブジェクト生成をひとつの関数にまとめることで、生成ロジックを局所化する（Simple Factory の考え方）。

**コード例:**

```python
# formatters.py
def build_stream_formatter(...) -> Formatter: ...
def build_file_formatter(...) -> Formatter: ...

# handlers.py
def build_stream_handler(logger, ...) -> StreamHandler: ...
def build_file_handler(logger, filepath, ...) -> FileHandler: ...
```

**ポイント:**
- 生成の詳細（フォーマット文字列やハンドラ名など）が呼び出し元に漏れない。
- デフォルト引数を使うことで、テスト時に任意の値を注入できる。

---

## 全体のパターン関係図

```
configure_logging()        ← Director
    │
    └─ LoggerBuilder       ← Builder (Fluent Interface)
           ├─ build_stream_handler()  ← Factory 関数
           │      ├─ build_stream_formatter()
           │      └─ build_stream_level()
           └─ build_file_handler()   ← Factory 関数
                  ├─ build_file_formatter()
                  ├─ build_file_level()
                  └─ build_filepath()
```
