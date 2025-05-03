"""Create a tokenizer for your own language (mother tongue you speak). The tokenizer should tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]"""


import re

def tokenize_hindi(text):
    # Unicode blocks:
    # \u0900-\u097F → Devanagari letters
    # \u0966-\u096F → Devanagari digits (०-९)
    hindi_pattern = r'[\u0900-\u097F]+'
    devnagari_digit_pattern = r'[\u0966-\u096F]+'
    punctuation_pattern = r"[.,!?;:\"'()\[\]{}]"
    date_pattern = r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    number_pattern = r'\b\d{1,3}(,\d{2})*(,\d{3})*\b|\b\d+\.\d+\b|\b\d+/\d+\b'
    handle_pattern = r'@[A-Za-z0-9_]+'

    # Combine all patterns
    combined_pattern = f'({hindi_pattern}|{devnagari_digit_pattern}|{punctuation_pattern}|{date_pattern}|{url_pattern}|{email_pattern}|{number_pattern}|{handle_pattern})'

    tokens = re.findall(combined_pattern, text)
    return tokens

# Example Hindi text including Devanagari digits (for demonstration)
hindi_text = "नमस्ते! यह १५-०१-२०२५ की बात है। मेरा ईमेल abc@gmail.com और वेबसाइट https://example.com है। मेरा फोन नंबर 3,22,243 है और ट्विटर हैंडल @username है।"

tokens = tokenize_hindi(hindi_text)
print(tokens)

