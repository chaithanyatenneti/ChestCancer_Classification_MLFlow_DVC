from Classification import logger
from Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Classification.pipeline.stage_03_model_trainer import ModelTrainerPipeline
from Classification.pipeline.stage_04_model_evaluation_with_mlflow import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion "


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model "

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")    
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e