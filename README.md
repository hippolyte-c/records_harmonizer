```
Script : records_harmonizer.py
Auteur : Hippolyte C
Date : 16/01/2026
```

### Description
Script Python pour agréger les observations de certificats TLS à partir d'un fichier JSON et les enregistrer dans un fichier CSV.

### Fonctionnalités
Le script présente différentes options tout en restant fidèle aux consignes de l'exercice :
- agréger le document fourni en entrée par adresse IP et hash SHA1 du certificat (consigne initiale);
- filtrer les enregistrements selon des seuils de comptage minimum et maximum (`--min-count` et `--max-count`);
- filtrer les enregistrements selon des dates de première et dernière observation (`--since` et `--until`);
- grouper les enregistrements agrégés selon un critère spécifié (`--group-by`);
- trier les enregistrements agrégés selon un critère spécifié (`--sort-by`).

`group_by` et `sort_by` ne sont pas deux options mutuellement exclusives. Si les deux options sont actives, alors au sein d'un groupement, les données seront triées selon le critère spécifié par `sort_by`.
À l'exception du fichier d'entrée, toutes les options sont optionnelles et utilisables simultanément.
 
### Instructions
- `python3 certificates_cleaner.py --help`
- Script réalisé en Python 3.12.3.
- Pas d'imports externes nécessaires.

### Évolutions possibles

Élargir cet outil pour n'importe quelles données en choisissant en options les champs à agréger. 