from core.coordination_core import unify, enrich
from core.guard_core import process as guard_process
from core.health_engine import run as health_run
from core.orchestrator import run as core_run

def run(raw_signal):

    guarded = guard_process(raw_signal)
    result = health_run(guarded)

    if not result:
        return

    signal, state = result

    # Übergabe an Core
    signal = unify(signal)
    signal = enrich(signal)
    core_run(signal)
