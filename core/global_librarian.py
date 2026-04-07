from core.library_core import store_contract

def globalize(local_data):

    knowledge = {
        "type": "GLOBAL_PATTERN",
        "data": local_data
    }

    store_contract(knowledge)

    return knowledge
