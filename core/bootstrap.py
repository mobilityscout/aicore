def run():

    print("\n=== IMMUNE CORE START ===")

    try:
        from core.import_hook import install
        install()
        print("IMPORT HOOK INSTALLED")
    except Exception as e:
        print("IMPORT HOOK FAIL:", e)

    print("IMMUNE CORE OK")
