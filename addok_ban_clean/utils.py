import re

CLEAN_PATTERNS = (
    (" {2,}", " "),
    ("^lieux?[ -]?dits?\\b(?=.)", ""), # BAN 07/2022 : 68056
    ("^ham(eau) (des |de la |de |du |le |les |la |l'|d')?\\b(?=.)", ""), # BAN 07/2022 : 7449
    ("^quartier (des |de la |de |du |le |les |la |l'|d')\\b(?=.)", ""), # BAN 07/2022 : 4006
    ("^ferme (des |de la |de |du |le |les |la |l'|d')\\b(?=.)", ""), # BAN 07/2022 : 2969
    ("^domaine (des |de la |de |du |le |les |la |l'|d')\\b(?=.)", ""), # BAN 07/2022 : 2409
    ("^village (des |de la |de |du |le |les |la |l'|d')\\b(?=.)", ""), # BAN 07/2022 : 1947
    ("^chemin rural(( n°?)? ?[0-9]+)?( dit)?\\b(?=.)", "chemin "), # BAN 07/2022 : 2060
)
CLEAN_COMPILED = list(
    (re.compile(pattern, flags=re.IGNORECASE), replacement)
    for pattern, replacement in CLEAN_PATTERNS
)

def ban_clean(q):
    for pattern, repl in CLEAN_COMPILED:
        q = pattern.sub(repl, q)
    q = q.strip()
    return q
