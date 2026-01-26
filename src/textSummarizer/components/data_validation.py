import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            all_files = os.listdir(os.path.join(
                "artifacts", "data_ingestion", "samsum_dataset"))
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    logger.error(
                        f"Missing required file/directory: {required_file}")
                    break  # Stop checking further once a missing file is found
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(
                        f"File existence validation status: {validation_status}")
            return validation_status
        except Exception as e:
            logger.error(f"Error during file existence validation: {e}")
        raise e
