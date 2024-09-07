from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:

    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:

    logger.exception(e)
    raise e