#!/usr/bin/env python3
"""Test connection to the Railway PostgreSQL.

Uso:
    python3 scripts/test_db.py

Lee DATABASE_URL desde credentials.env (raíz del repo).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    env_path = repo_root / "credentials.env"
    env = load_env(env_path)
    url = env.get("DATABASE_URL") or os.environ.get("DATABASE_URL")
    if not url:
        print("ERROR: DATABASE_URL no encontrado en credentials.env ni env.")
        return 2

    try:
        import psycopg  # psycopg3
    except ImportError:
        try:
            import psycopg2 as psycopg  # type: ignore
        except ImportError:
            print(
                "Falta driver. Instala uno:\n"
                "  pip install 'psycopg[binary]'\n"
                "  # o\n"
                "  pip install psycopg2-binary"
            )
            return 3

    print(f"Conectando a: {url.split('@')[-1]}")
    try:
        with psycopg.connect(url) as conn:  # type: ignore[arg-type]
            with conn.cursor() as cur:
                cur.execute("SELECT version(), current_database(), current_user, now();")
                row = cur.fetchone()
                print("OK")
                print(f"  version : {row[0].split(' on')[0]}")
                print(f"  database: {row[1]}")
                print(f"  user    : {row[2]}")
                print(f"  now     : {row[3]}")
                cur.execute(
                    "SELECT table_schema, table_name FROM information_schema.tables "
                    "WHERE table_schema NOT IN ('pg_catalog','information_schema') "
                    "ORDER BY 1,2 LIMIT 20;"
                )
                tables = cur.fetchall()
                if tables:
                    print(f"  tablas existentes ({len(tables)}):")
                    for s, t in tables:
                        print(f"    - {s}.{t}")
                else:
                    print("  tablas: (DB vacía — listo para migraciones iniciales)")
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
