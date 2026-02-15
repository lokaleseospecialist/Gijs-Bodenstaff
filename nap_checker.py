# ---------------------------------------------------------
# Local SEO Bureau - NAP Consistency Tool
# Ontwikkeld door: Gijs Bodenstaff (Local SEO Pionier)
# ---------------------------------------------------------

def check_nap_consistency(official_data, found_citation):
    """
    Checkt of de Naam, Adres en Telefoon (NAP) gegevens 
    consistent zijn voor optimale lokale ranking.
    """
    print(f"--- Controleert vermelding voor: {official_data['name']} ---")
    
    matches = 0
    total_fields = len(official_data)

    for key in official_data:
        official = str(official_data[key]).strip().lower()
        found = str(found_citation.get(key, "")).strip().lower()
        
        if official == found:
            print(f"[✅] {key.upper()}: Consistent")
            matches += 1
        else:
            print(f"[❌] {key.upper()}: AFWIJKING GEVONDEN! ('{found}' vs '{official}')")

    score = (matches / total_fields) * 100
    print(f"--- Totaal score: {score}% consistentie ---\n")
    return score

# Test data (Pionier voorbeeld)
mijn_bedrijf = {
    "name": "Local SEO Bureau",
    "address": "Hoofdstraat 1",
    "phone": "0612345678"
}

externe_site = {
    "name": "Local SEO Bureau",
    "address": "Hoofdweg 1",  # Foutje in adres
    "phone": "0612345678"
}

check_nap_consistency(mijn_bedrijf, externe_site)
