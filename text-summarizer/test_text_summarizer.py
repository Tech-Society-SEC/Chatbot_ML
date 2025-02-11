# test_text_summarizer.py

import unittest
import io
from text_summarizer import process_input, summarize_text

# Classe utilitaire pour simuler un objet fichier avec un attribut "name"
class DummyFile(io.BytesIO):
    def __init__(self, content, name):
        super().__init__(content)
        self.name = name

class TestTextSummarizer(unittest.TestCase):

    def test_empty_input(self):
        # Cas : aucune entrée fournie (texte vide et aucun fichier)
        result = process_input("", None)
        self.assertEqual(result, "Error: No text provided for summarization.")

    def test_plain_text_input(self):
        # Cas : entrée texte directe valide
        input_text = "Ceci est un long texte qui doit être résumé. " * 20
        result = process_input(input_text, None)
        # On s'assure que le résultat est une chaîne, qu'il ne contient pas un message d'erreur
        # et qu'il est différent du texte original.
        self.assertIsInstance(result, str)
        self.assertNotIn("Error", result)
        self.assertNotEqual(result, input_text)

    def test_invalid_file_extension(self):
        # Cas : fichier avec une extension non prise en charge (ex : .pdf)
        dummy_file = DummyFile(b"Ceci est le contenu du fichier", "document.pdf")
        result = process_input("", dummy_file)
        self.assertEqual(result, "Error: Unsupported file format. Please upload a .txt file.")

    def test_empty_file_input(self):
        # Cas : fichier .txt vide
        dummy_file = DummyFile(b"", "empty.txt")
        result = process_input("", dummy_file)
        self.assertEqual(result, "Error: Uploaded file is empty.")

    def test_valid_file_input(self):
        # Cas : fichier .txt valide contenant du texte à résumer
        text_content = "Ceci est un texte à résumer. " * 20
        dummy_file = DummyFile(text_content.encode("utf-8"), "texte.txt")
        result = process_input("", dummy_file)
        self.assertIsInstance(result, str)
        self.assertNotIn("Error", result)
        self.assertNotEqual(result, text_content)

if __name__ == "__main__":
    unittest.main()
