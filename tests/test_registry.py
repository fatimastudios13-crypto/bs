from pathlib import Path

REQUIRED = {"name", "subname", "description", "inputs", "use_case", "default", "result", "revolt", "version", "type", "status"}
ROOT = Path(__file__).parents[1]


def parse_top_level_yaml(path: Path):
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line[0].isspace() or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def test_module_contracts_are_complete():
    paths = sorted((ROOT / "modules").glob("*/module.yaml"))
    assert paths
    for path in paths:
        data = parse_top_level_yaml(path)
        assert REQUIRED <= data.keys(), f"{path} missing {REQUIRED - data.keys()}"
        assert data["version"]
        assert data["status"] in {"active", "planned"}
