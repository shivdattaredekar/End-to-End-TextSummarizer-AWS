from TextSummarizer.config.configuration import ConfigrationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.logging import logger


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        model_eva_config = config.get_model_evaluation_config()
        model_eva_config = ModelEvaluation(config=model_eva_config)
        model_eva_config.train()

