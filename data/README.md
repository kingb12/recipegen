# Datasets Used


###[m3hrdadfi/recipe_nlg_lite](https://huggingface.co/datasets/m3hrdadfi/recipe_nlg_lite)
> RecipeNLG: A Cooking Recipes Dataset for Semi-Structured Text Generation - Lite version
The dataset contains 7,198 cooking recipes (>7K). It's processed in more careful way and provides more samples than 
any other dataset in the area.

Usage: 
```python
from datasets import load_dataset


dataset = load_dataset("m3hrdadfi/recipe_nlg_lite")
print(dataset)
```

Citation:
```
@misc{RecipeNLGLite, 
  author          = {Mehrdad Farahani},
  title           = {RecipeNLG: A Cooking Recipes Dataset for Semi-Structured Text Generation (Lite)},
  year            = 2021,
  publisher       = {GitHub},
  journal         = {GitHub repository},
  howpublished    = {url{https://github.com/m3hrdadfi/recipe-nlg-lite}},
}
```
