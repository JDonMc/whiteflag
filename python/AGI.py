from datasets import load_dataset, load_metric
from transformers import DistilBertTokenizerFast
from transformers import AutoModelForSequenceClassification, DataCollatorWithPadding
from transformers import Trainer, TrainingArguments
from transformers import BertTokenizer
import datasets

checkpoint = "distilbert-base-uncased"

dataset = load_dataset("boolq")
datasets.DatasetDict({"train": datasets.Dataset({features: ['question', 'answer', 'passage'], num_rows: 9427}), "validation": datasets.Dataset({features: ['question', 'answer', 'passage'], num_rows: 3270 })})
tokenizer = DistilBertTokenizerFast.from_pretrained(checkpoint)

def tokenize_function(example):
    encoded = tokenizer(example["question"], example["passage"], truncation=True)
    encoded["labels"] = [int(a) for a in example["answer"]]
    return encoded

tokenized_datasets = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
args = TrainingArguments("roberta-booql", per_device_train_batch_size=16, learning_rate=1e-3, num_train_epochs=3)
trainer = Trainer(model, args, train_dataset=tokenized_datasets["train"], eval_dataset=tokenized_datasets["validation"], data_collator=data_collator, tokenizer=tokenizer,)
trainer.train()

filename = f'save_models'
trainer.save_model(filename)
print(trainer)
predictions = trainer.predict(tokenized_datasets["validation"])
y_pred = predictions.predictions.argmax(-1)
labels = predictions.label_ids
metric = load_metric("accuracy")
metric.compute(predictions=y_pred, references=predictions.label_ids)
print(metric)

new_tokenizer = BertTokenizer.from_pretrained("/usr/adenhandasyde/GitHub/whiteflag/python/save_models/")
from transformers import TFAutoModel
# bert = TFAutoModel.from_pretrained("bert-base-uncased")
bert = TFAutoModel.from_pretrained("/usr/adenhandasyde/GitHub/whiteflag/python/save_models/")
print(bert)
print(new_tokenizer)

