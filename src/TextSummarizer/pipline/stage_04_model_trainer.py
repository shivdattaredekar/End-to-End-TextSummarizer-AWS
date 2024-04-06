from TextSummarizer.config.configuration import ConfigrationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

        