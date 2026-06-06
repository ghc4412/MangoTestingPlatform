import os
from pathlib import Path


TRUE_VALUES = {"1", "true", "yes", "on"}
FALSE_VALUES = {"0", "false", "no", "off"}


def _strip_inline_comment(value: str) -> str:
    quote = None
    for index, char in enumerate(value):
        if char in {"'", '"'}:
            quote = None if quote == char else char
        if char == "#" and quote is None:
            return value[:index].rstrip()
    return value.strip()


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_env_file(path: Path | str, override: bool = False) -> bool:
    env_path = Path(path)
    if not env_path.exists():
        return False

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        key, value = line.split("=", 1)
        key = key.strip()
        if not key:
            continue
        if not override and key in os.environ:
            continue
        os.environ[key] = _strip_quotes(_strip_inline_comment(value.strip()))
    return True


def load_project_env(base_dir: Path, django_env: str | None = None) -> Path | None:
    explicit_path = os.getenv("DJANGO_ENV_FILE") or os.getenv("CONFIG_ENV_FILE")
    if explicit_path:
        env_path = Path(explicit_path)
        if load_env_file(env_path):
            return env_path
        return None

    repo_dir = base_dir.parent
    local_first = django_env == "dev" or os.getenv("DJANGO_ENV") is None
    names = [".env.local", ".env.docker"] if local_first else [".env.docker", ".env.local"]

    for name in names:
        for candidate in (repo_dir / name, base_dir / name):
            if load_env_file(candidate):
                return candidate
    return None


def env(name: str, default=None, aliases: tuple[str, ...] = ()):
    for key in (name, *aliases):
        value = os.getenv(key)
        if value is not None:
            return value
    return default


def env_bool(name: str, default: bool = False, aliases: tuple[str, ...] = ()) -> bool:
    value = env(name, None, aliases)
    if value is None:
        return default
    normalized = str(value).strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    return default


def env_int(name: str, default: int, aliases: tuple[str, ...] = ()) -> int:
    value = env(name, None, aliases)
    if value is None:
        return default
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default
