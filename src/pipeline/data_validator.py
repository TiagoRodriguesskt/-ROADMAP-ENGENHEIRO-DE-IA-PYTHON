import pandas as pd
from pipeline.logger import get_logger

logger = get_logger(__name__)


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida e limpa o DataFrame para uso em ML.
    """

    if df.empty:
        logger.error("Dataset vazio.")
        raise ValueError("Dataset vazio")

    logger.info("Validação inicial concluída")

    # Remover linhas duplicadas
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    if before != after:
        logger.warning(f"Removidas {before - after} linhas duplicadas")

    # Verificar valores nulos
    nulls = df.isnull().sum().sum()
    if nulls > 0:
        logger.warning(f"Dataset contém {nulls} valores nulos")
        df = df.dropna()
        logger.info("Linhas com valores nulos removidas")

    logger.info("Validação e limpeza concluídas")
    return df
