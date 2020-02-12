def replace_rus2eng(df, columns):
    """Transliterate from russian letters to english"""
    import transliterate
    import pandas as pd
    for col in columns:
        df[col]=df[col].apply(lambda x: transliterate.translit(x,'ru', reversed=True) if isinstance(x, str) else x)