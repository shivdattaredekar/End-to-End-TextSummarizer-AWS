from TextSummarizer.config.configuration import ConfigrationManager
from TextSummarizer.components.data_transformation import DataTransformation 


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_Transformation = DataTransformation(config=data_transformation_config)
        data_Transformation.convert()
            