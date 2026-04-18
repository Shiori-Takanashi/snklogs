set dotenv-load := true

TARGETS := "src tests"

# ==========================================
# 1. メタタスク
# ==========================================
default:
    @just --list

HOOK_TYPES := "pre-commit pre-push"

# ==========================================
# 2. セットアップ・実行
# ==========================================
setup: sync pre-install

sync:
    uv sync

pre-install:
    @for hook in {{HOOK_TYPES}}; do \
        echo "Installing hook: $hook ..."; \
        uv run pre-commit install --hook-type $hook; \
    done

run *args:
    uv run python -m your_package {{args}}

# ==========================================
# 3. 統合ワークフロー（タスクの束ね）
# ==========================================
all: fix format typecheck test

check: format-check lint typecheck test

# ==========================================
# 4. 個別タスク（フォーマット関連）
# ==========================================
format:
    uv run ruff format {{TARGETS}}

format-check:
    uv run ruff format --check {{TARGETS}}

# ==========================================
# 5. 個別タスク（Lint・解析関連）
# ==========================================
lint:
    uv run ruff check {{TARGETS}}

fix:
    uv run ruff check --fix {{TARGETS}}

# ==========================================
# 6. 個別タスク（型チェック・テスト）
# ==========================================
typecheck:
    uv run mypy {{TARGETS}}

test:
    uv run pytest
