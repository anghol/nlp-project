# Evaluation Mental State from Personal Notes

This is a final project for HSE & ODS NLP course.

## Abstract

Mental health assessment through text analysis is a critical yet challenging
task due to the complexity of linguistic patterns associated with
psychological states. This project addresses the problem of accurately detecting
mental health conditions from personal notes using Natural Language
Processing (NLP). Mental RoBERTa, a domain-specific transformer
model pretrained on mental health-related texts, is used to improve classification
performance over generic language models. Our approach finetunes
Mental RoBERTa on a dataset of annotated social media posts and
journal entries, optimizing for key metrics like precision and recall. Experimental
results demonstrate strong classification quality, achieving an
F1-score of 0.84 in distinguishing texts of different mental health statuses,
outperforming baseline models. This work highlights the potential of specialized
NLP models to support early mental health screening and digital
therapeutics.

## The repository structure

- `utils.py` - the module with text preprocessing functions.
- `1-eda-preprocessing.ipynb` - the notebook with exploratory data analysis and manually feature engineering for mental statuses classification task.
- `2-baselines.ipynb` - the notebook with training and evaluation of baseline models: Random Forest and Catboost.
- `3-transformer.ipynb` - the notebook with fine-tuning and evaluation MentalRoBERTa model.