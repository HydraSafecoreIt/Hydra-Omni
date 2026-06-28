from hydra_shield import HydraTelephonyCore

# System initialisieren
shield = HydraTelephonyCore()

# Anruf prüfen
is_allowed, report = shield.evaluate_and_shield(caller_number, sip_header)
