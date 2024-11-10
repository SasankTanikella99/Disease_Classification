from src.Summarization.pipeline.T01_data_ingestion import DataIngestionTrainingPipeline
from src.Summarization.pipeline.T02_data_validation import DataValidationTrainingPipeline
from src.Summarization.pipeline.T03_data_transformation import DataTransformationTrainingPipeline
from src.Summarization.pipeline.T04_model_trainer import ModelTrainerTrainingPipeline
from src.Summarization.pipeline.T05_model_evaluation import ModelEvaluationTrainingPipeline
from src.Summarization.logging import logger


NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




