# Custom imports
# models
from models.ChainedList import ChainedList
# tools
from tools.display_menu import message

# Variables globales
logs: ChainedList|None = None

def init() -> None:
    """
    (Ré)Initialisation des logs
    """
    global logs
    logs = None
    
    return logs

def log(data: dict) -> ChainedList:
    """
    Log d'une donnée
    """
    global logs
    if logs is None:
        logs = ChainedList(data)
    else:
        logs.append(data)
    
    return logs

def unlog(index: int = -1, data : bool = True) -> None:
    """
    Suppression d'un log
    """
    global logs
    if logs is not None and logs.get_size() > 0:
        logs, result = logs.pop(index = index, data = data)
        return result
    else:
        message("Aucun coup à annuler", "warning")


def get_logs() -> list:
    """
    Récupération des logs
    """
    global logs
    
    logs_list = []
    current = logs
    i = 1

    while i <= logs.get_size():
        logs_list.append(current.get_data())
        current = current.get_next()

    return logs_list

def chained_list_to_string() -> str:
    """
    Récupération des logs sous forme de chaîne de caractères
    """
    global logs
    if logs is None:
        return "Logs are empty"

    elements = []
    current = logs
    while current is not None:
        elements.append(str(current.get_data()))
        current = current.get_next()
    return " -> ".join(elements)

def get_last_occurence(coords : list) -> ChainedList:
    """
    Retourne la dernière occurence d'une cellule
    """
    global logs
    return logs.get_last_occurence(coords)