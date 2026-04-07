def safe_import(module, default):

    try:
        return __import__(module, fromlist=["*"])
    except:
        return default
