from core.auto_import_manager import handle

def protect(func):

    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except Exception as e:

            print("CORE FAIL:", e)

            repaired = handle(e)

            if repaired:
                print("RETRY AFTER AI FIX")
                return func(*args, **kwargs)

            raise e

    return wrapper
