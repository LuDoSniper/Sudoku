# Imports
import time

def get_time(func: callable, *args: list[any], **kwargs: dict[any, any]) -> tuple:
    """
    Retourne le résultat de la fonction `func` et le temps d'exécution
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    execution_time = end_time - start_time
    return result, execution_time