from pathlib import Path

def pourcentage(lenght: float, percent: float) -> float:
    """Fonction pour calculer la valeur du pourcentage d'une valeur

    Args:
        `lenght` (float): Valeur initiale
        `percent` (float): Pourcentage

    Returns:
        float: Valeur du pourcentage
    """
    return (lenght * percent) / 100

def get_absolute_path(relative_path: str) -> Path:
    """Fonction pour avoir la chemin absolue vers un fichier

    Args:
        relative_path (str): Chemin relatif

    Returns:
        Path: Chemin absolu
    """
    cache: Path = Path(relative_path)
    return cache.resolve()