from transformers import AutoModel, AutoTokenizer

model_name = "mosaicml/mpt-7b-storywriter"  # Replace with the actual model name
save_directory = "H:/"  # Specify your directory

# Downloading the model and tokenizer
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Saving the model and tokenizer to your specified directory
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

# To load the model and tokenizer from the saved directory later, you can use:
# model = AutoModel.from_pretrained(save_directory)
# tokenizer = AutoTokenizer.from_pretrained(save_directory)
