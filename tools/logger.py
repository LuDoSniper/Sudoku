from models.ChainedList import ChainedList
from tools.display_menu import message
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

def unlog(index: int = -1) -> None:
    """
    Suppression d'un log
    """
    global logs
    if logs is not None and logs.get_size() > 0:
        logs.pop(index)
    else:
        message("Aucun coup à annuler", "warning")


def get_tail() -> ChainedList | None:
    """
    Renvoie le dernier élément de la liste chaînée.
    """
    global logs
    if logs is None:
        # Si les logs sont vides
        return None

    # Parcourir la liste pour trouver le dernier élément
    current = logs
    while current.get_next() is not None:
        current = current.get_next()

    # Retourner le dernier élément
    return current


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
    global logs
    if logs is None:
        return "Logs are empty"

    elements = []
    current = logs
    while current is not None:
        elements.append(str(current.get_data()))
        current = current.get_next()
    return " -> ".join(elements)