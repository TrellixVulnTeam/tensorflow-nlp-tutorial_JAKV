# -*- coding: utf-8 -*-
"""Learning Spoons 8강. 영어 BERT를 이용한 마스크드 언어 모델ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L8BTbOtr19bPDU7Q6H9lvAO_aI2q0xEq
"""

!pip install transformers

from transformers import TFBertForMaskedLM

model = TFBertForMaskedLM.from_pretrained('bert-large-uncased')

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased")

inputs = tokenizer('Soccer is a really fun [MASK].', return_tensors='tf')

tokenizer.cls_token_id

tokenizer.sep_token_id

tokenizer.mask_token_id

inputs

print(inputs['input_ids'])

print(inputs['token_type_ids'])

print(inputs['attention_mask'])

from transformers import FillMaskPipeline
pip = FillMaskPipeline(model=model, tokenizer=tokenizer)

pip('Soccer is a really fun [MASK].')

pip('The Avengers is a really fun [MASK].')

pip('I went to [MASK] this morning.')