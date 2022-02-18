from typing import Dict
from datasets import Dataset, load_dataset


HUGGINGFACE_DATASET_KEY = "m3hrdadfi/recipe_nlg_lite"

# constants in our datasets
TEST_SPLIT = "test"
TRAIN_SPLIT = "train"
INGREDIENT = "ingredient"
NER = "ner"

# private constants in our processing
_DATA = "data"
# constants in dataset keys
_INGREDIENTS = "ingredients"


def _extract_ingredients_and_ner_pairs(example: Dict) -> Dict:
    """
    Given an example from the m3hrdadfi/recipe_nlg_lite, return its ingredient, ner pairs in a dataset
    """
    output = {_DATA: []}
    ingredients = example[_INGREDIENTS].split(',')
    ners = example[NER].split(',')
    for i, ing in enumerate(ingredients):
        output[_DATA].append({INGREDIENT: ing, NER: ners[i]})
    return output


def generated_pretokenized_ingredient_ner_pair_dataset(split: str = TRAIN_SPLIT) -> Dataset:
    """
    Using the m3hrdadfi/recipe_nlg_lite dataset with the given split, turn it into
    a dataset of (ingredient, ner) pairs, UN-tokenized.
    :return: untokenized dataset of all ingredient, ner pairs in the given split
    """
    dataset = load_dataset(HUGGINGFACE_DATASET_KEY, split=split)
    extracted_data = dataset.map(_extract_ingredients_and_ner_pairs, remove_columns=dataset.column_names)
    unpacked_data = {INGREDIENT: [], NER: []}
    for e in extracted_data:
        for pair in e[_DATA]:
            unpacked_data[INGREDIENT].append(pair[INGREDIENT])
            unpacked_data[NER].append(pair[NER])

    return Dataset.from_dict(unpacked_data)
