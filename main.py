from aica.assistant import AICA

def main():
    # Initialize AICA
    concierge = AICA()
    
    # Example multilingual input
    guest_request_english = "I'm looking for a good Italian restaurant nearby."
    guest_request_spanish = "Estoy buscando un buen restaurante italiano cerca."

    # Get recommendations in English
    print("English Recommendations:")
    recommendations_english = concierge.provide_recommendations(guest_request_english)
    print(recommendations_english)

    # Get recommendations in Spanish
    print("\nSpanish Recommendations:")
    recommendations_spanish = concierge.provide_recommendations(guest_request_spanish)
    print(recommendations_spanish)

if __name__ == "__main__":
    main()
