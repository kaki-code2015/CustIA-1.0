# --- CUSTIA 2.1 PRO - VERSION OFFICIELLE ---
# Développé par l'Architecte de la AspTeam

def generateur_fastmd(nom_mod):
    # Fonction pour le format de Lucas & Reta
    nom_fichier = nom_mod + ".FastMD"
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write("# FICHIER .FastMD GÉNÉRÉ PAR CUSTIA (AspTeam)\n")
            f.write("# AUTORISATION OFFICIELLE : LUCAS (BPM34)\n\n")
            f.write(f"nom_mod={nom_mod}\n")
            f.write("auteur=Reta\n")
            f.write("vitesse_moteur=Turbo\n")
            f.write("puissance_ia=9000\n")
            
            signature = f"SECURE-SIG-{nom_mod.upper()}-ASP-2026"
            f.write(f"\nsignature_certifiee={signature}\n")
        print(f"\n✅ Mod Performance '{nom_fichier}' généré avec succès !")
    except Exception as e:
        print(f"\n❌ Erreur : {e}")

def generateur_naymod(nom_mod):
    # Fonction pour le format Classique avec mots-clés
    if not nom_mod.endswith(".NayMOD"):
        nom_fichier = nom_mod + ".NayMOD"
    else:
        nom_fichier = nom_mod

    connaissances = {}
    print("\n--- CONFIGURATION DES MOTS-CLÉS ---")
    print("(Tape 'fin' quand tu as terminé d'ajouter des mots)")
    
    while True:
        mot = input("Mot-clé : ").strip().lower()
        if mot == "fin":
            break # On sort de la boucle si l'utilisateur tape "fin"
            
        rep = input(f"Réponse pour '{mot}' : ").strip()
        
        # On ajoute le mot et la réponse dans la mémoire
        connaissances[mot] = rep
        print(f"✔️ Ajouté : {mot} -> {rep}")

    # Sauvegarde dans le fichier texte (Seulement si on a ajouté des mots)
    if connaissances:
        try:
            with open(nom_fichier, "w", encoding="utf-8") as f:
                for m, r in connaissances.items():
                    f.write(f"{m}:{r}\n")
            print(f"\n🚀 Mod Classique '{nom_fichier}' créé avec {len(connaissances)} mots-clés !")
        except Exception as e:
            print(f"\n❌ Erreur lors de la sauvegarde : {e}")
    else:
        print("\n⚠️ Aucun mot-clé ajouté, le mod n'a pas été créé.")

# --- MENU PRINCIPAL ---
while True:
    print("\n" + "="*35)
    print("=== BIENVENUE DANS CUSTIA 2.1 PRO ===")
    print("="*35)
    print("1. Créer un .NayMOD (Mots-clés classiques)")
    print("2. Créer un .FastMD (Performance Lucas/Reta)")
    print("3. Quitter CustIA")

    choix = input("\nChoisis une option (1, 2 ou 3) : ").strip()

    if choix == "1":
        nom = input("Nom de ton mod NayMOD : ").strip()
        generateur_naymod(nom)
    elif choix == "2":
        nom = input("Nom de ton mod FastMD : ").strip()
        generateur_fastmd(nom)
    elif choix == "3":
        print("\nFermeture de CustIA... Prêt pour la pause BD ! À bientôt l'Architecte !")
        break
    else:
        print("\n❌ Option invalide, essaie encore.")
