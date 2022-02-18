import unittest
from data_processing import generated_pretokenized_ingredient_ner_pair_dataset, TRAIN_SPLIT, INGREDIENT, NER


class DataProcessingTests(unittest.TestCase):

    def test_pretokenization_ingredient_ner_pairs(self):
        ing_ner_pairs = generated_pretokenized_ingredient_ner_pair_dataset(TRAIN_SPLIT)
        for pair in ing_ner_pairs:
            # right columns
            self.assertIn(INGREDIENT, pair)
            self.assertIn(NER, pair)
            # ner invariant: ner is a substring of ingredient
            self.assertIn(pair[NER], pair[INGREDIENT])


if __name__ == '__main__':
    unittest.main()
