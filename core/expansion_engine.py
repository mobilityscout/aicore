from core.dynamic_import import load


def expand(missing):

    print("\n=== SYSTEM EXPANSION ===")

    for m in missing:

        module_name = f"core.{m.lower()}"

        mod = load(module_name)

        print("EXPANDED:", m)
