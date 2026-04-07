try:
    from core.import_hook import install
    install()
    print("GLOBAL IMPORT CONTROL ACTIVE")
except Exception as e:
    print("IMPORT HOOK INIT FAIL:", e)
