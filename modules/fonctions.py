from pathlib import Path
import tempfile

def pourcentage(lenght: float, percent: float) -> float:
    """Fonction pour calculer la valeur du pourcentage d'une valeur

    Args:
        `lenght` (float): Valeur initiale
        `percent` (float): Pourcentage

    Returns:
        float: Valeur du pourcentage
    """
    return (lenght * percent) / 100

def create_tmp_file(data: str, extension: str = '.c') -> str:
    """Fonction qui cree un fichier temporaire et renvoit le chemin vers ce fichier

    Args:
        data (str): donnee a ecrire
        extension (str, optional): Extension du fichier. Defaults to '.c'.

    Returns:
        str: Chemin vers le fichier
    """
    with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as file:
        file.write(data.encode())
        return file.name

def get_absolute_path(relative_path: str) -> Path:
    """Fonction pour avoir la chemin absolue vers un fichier

    Args:
        relative_path (str): Chemin relatif

    Returns:
        Path: Chemin absolu
    """
    cache: Path = Path(relative_path)
    return cache.resolve()