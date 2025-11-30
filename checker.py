import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
KG_PATH = BASE_DIR / "knowledge_graph.json"
BUGGY_PATH = BASE_DIR / "MainActivity_buggy.kt"
PATCHED_PATH = BASE_DIR / "MainActivity_patched.kt"

def load_knowledge_graph():
    with KG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_code(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()

def uses_risky_api(code: str) -> bool:
    return any(
        token in code
        for token in ["NotificationChannel(", "createNotificationChannel("]
    )

def has_version_guard(code: str) -> bool:
    return (
        "Build.VERSION.SDK_INT" in code
        and ">=" in code
        and "Build.VERSION_CODES.O" in code
    )

def analyze_file(path: Path, kg: dict):
    code = load_code(path)
    print(f"Analyzing file: {path.name}\n")

    found_any = False

    for api_name, info in kg.items():
        if api_name == "android.app.NotificationChannel":
            search_tokens = ["NotificationChannel("]
        elif api_name == "NotificationManager.createNotificationChannel":
            search_tokens = ["createNotificationChannel("]
        else:
            search_tokens = [api_name]

        for token in search_tokens:
            if token in code:
                found_any = True
                print(f"⚠️  Found risky API usage: {api_name}")
                print(f"   - Appears as: '{token}'")
                print(f"   - Min SDK required: {info.get('min_sdk')}")
                print(f"   - Constraint: {info.get('constraint')}")
                print(f"   - Recommended rule: {info.get('rule')}\n")

    if not found_any:
        print("✅ No risky APIs from the knowledge graph were found in this file.\n")

def check_patch_is_guarded(path: Path):
    code = load_code(path)

    risky = uses_risky_api(code)
    guarded = has_version_guard(code)

    print(f"=== Patch Validation for {path.name} ===")
    if not risky:
        print("ℹ️  No risky APIs used in this file according to the knowledge graph.\n")
        return

    if guarded:
        print("✅ Patch is VALID: risky APIs are guarded by an SDK version check (API 26+).\n")
    else:
        print("❌ Patch is INVALID: risky APIs are not properly guarded by an SDK version check.\n")

def simulate_run(label: str, api_level: int, code: str):
    risky = uses_risky_api(code)
    guarded = has_version_guard(code)

    if risky and api_level < 26 and not guarded:
        result = "❌ RuntimeError: NotificationChannel not available on this API level"
    else:
        result = "✅ App runs successfully"

    print(f"Device {label} (API {api_level}): {result}")

def simulate_crowdsourced_testing():
    print("==== Simulated Crowdsourced Testing (LAZYCOW-style) =====\n")

    buggy_code = load_code(BUGGY_PATH)
    patched_code = load_code(PATCHED_PATH)

    print("-> Buggy version:")
    simulate_run("Old phone", 21, buggy_code)
    simulate_run("Android 8 phone", 26, buggy_code)
    simulate_run("New phone", 33, buggy_code)
    print()

    print("-> Patched version:")
    simulate_run("Old phone", 21, patched_code)
    simulate_run("Android 8 phone", 26, patched_code)
    simulate_run("New phone", 33, patched_code)
    print()

def wait():
    input()

def main():
    kg = load_knowledge_graph()

    print("=== Fragmentation Analyzer, Checker & Test Simulator (Demo) ===\n")

    wait()
    print("---- Step 1: Analyze buggy version ----")
    analyze_file(BUGGY_PATH, kg)

    wait()
    print("---- Step 2: Analyze patched version ----")
    analyze_file(PATCHED_PATH, kg)

    wait()
    print("---- Step 3: Validate patched version ----")
    check_patch_is_guarded(PATCHED_PATH)

    wait()
    print("---- Step 4: Simulated crowdsourced testing ----")
    simulate_crowdsourced_testing()

if __name__ == "__main__":
    main()

