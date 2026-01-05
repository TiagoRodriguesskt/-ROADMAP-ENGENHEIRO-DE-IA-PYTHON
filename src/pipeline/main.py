from pathlib import Path
from pipeline.logger import get_logger
from pipeline.data_loader import load_csv
from pipeline.data_validator import validate_dataframe

logger = get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "sample.csv"


def main() -> None:
    df = load_csv(DATA_PATH)
    df = validate_dataframe(df)
    logger.info(f"Dataset final com {len(df)} linhas")
    logger.info(df.head())


if __name__ == "__main__":
    main()
