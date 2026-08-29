# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: HealthTrack
import copy
from datetime import datetime

def dry_run_operation(func):
    """Decorator that logs changes without applying them."""
    def wrapper(*args, **kwargs):
        original_args = copy.deepcopy(args)
        original_kwargs = copy.deepcopy(kwargs)
        result = func(*original_args, **original_kwargs)
        change_log = {
            'timestamp': datetime.now().isoformat(),
            'operation': func.__name__,
            'arguments': original_args,
            'result': result
        }
        if not hasattr(dry_run_operation, 'log'):
            dry_run_operation.log = []
        dry_run_operation.log.append(change_log)
        print(f"[DRY RUN] {func.__name__}: {result}")
        return result
    return wrapper
