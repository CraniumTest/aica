from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect


class AICA:
    def __init__(self):
        # Initialize the LLM
        self.recommendation_pipeline = pipeline(
            "text2text-generation",
            model="flax-community/t5-recommendation-system",
            tokenizer=AutoTokenizer.from_pretrained("flax-community/t5-recommendation-system"),
        )
        # Load translation models
        self.translation_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")
        self.tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")

    def detect_language(self, text):
        """Detect the language of the given text."""
        try:
            return detect(text)
        except Exception as e:
            return "en"

    def translate_to_english(self, text, lang):
        """Translate text to English."""
        if lang == 'en':
            return text
        
        inputs = self.tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.translation_model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def translate_from_english(self, text, lang):
        """Translate text from English to specified language."""
        if lang == 'en':
            return text

        # Reverse the translation model if supported or load a different model
        inputs = self.tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.translation_model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def provide_recommendations(self, guest_request):
        """Provide personalized recommendations based on guest's request."""
        lang = self.detect_language(guest_request)
        english_text = self.translate_to_english(guest_request, lang)

        recommendations = self.recommendation_pipeline(english_text)
        translated_recommendations = self.translate_from_english(recommendations[0]['generated_text'], lang)

        return translated_recommendations
