from pathlib import Path
import pandas as pd
from pipeline.logger import get_logger

logger = get_logger(__name__)


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        logger.error(f"Arquivo não encontrado: {path}")
        raise FileNotFoundError(path)

    df = pd.read_csv(path)
    logger.info(f"Dataset carregado com {len(df)} linhas e {len(df.columns)} colunas")
    return df
