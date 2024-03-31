#5. update the components
import os
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    

    def convert(self):
        #dataset_samsum = load_from_disk(self.config.data_path)
        # Provide the path to the directory containing the CSV files
        folder_path = self.config.data_path

        # Get the list of CSV files in the directory
        csv_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

        # Construct the data_files dictionary dynamically
        data_files = {}
        for i, file in enumerate(csv_files, start=1):
            data_files[f"file_{i}"] = os.path.join(folder_path, file)

        # Load the dataset from CSV files
        dataset_samsum = load_dataset("json", data_files=data_files)

        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
        