from .preprocessing import clean_text_with_steps
from .tokenization import tokenize_text
from .stopword_removal import remove_stopwords
from .language_detection import detect_language_for_tokens
from .slang_detection import detect_slang
from .ner_model import extract_entities
from .context_analysis import analyze_context
from .slang_normalization import normalize_text

def process_text(text):
    """
    Executes the complete NLP pipeline on the given code-mixed text.
    """
    # 1. Preprocessing & Tokenization with step-by-step auditing
    cleaned_text, preprocessing_steps, tokens = clean_text_with_steps(text, tokenize_text)
    
    # 2. Stopword Removal
    filtered_tokens = remove_stopwords(tokens)
    
    # 3. Language Identification
    language_tokens = detect_language_for_tokens(filtered_tokens)
    
    # 4. Slang Detection
    slang_words = detect_slang(filtered_tokens)
    
    # 5. Named Entity Recognition
    entities = extract_entities(cleaned_text)
    
    # 6. Context Analysis
    context_info = analyze_context(filtered_tokens, slang_words, language_tokens)
    
    # 7. Slang Normalization
    normalized_text = normalize_text(tokens, slang_words, context_info)
    
    return {
        "original_text": text,
        "cleaned_text": cleaned_text,
        "preprocessing_steps": preprocessing_steps,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "language_tokens": language_tokens,
        "slang_words": slang_words,
        "entities": entities,
        "context_analysis": context_info,
        "normalized_text": normalized_text
    }
