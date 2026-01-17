```
Script : records_harmonizer.py
Auteur : Hippolyte C
Date : 16/01/2026
```

```
hippo$ python3 records_harmonizer.py --help

  ____                        _         _                                      _
 |  _ \ ___  ___ ___  _ __ __| |___    | |__   __ _ _ __ _ __ ___   ___  _ __ (_)_______ _ __
 | |_) / _ \/ __/ _ \| '__/ _` / __|   | '_ \ / _` | '__| '_ ` _ \ / _ \| '_ \| |_  / _ \ '__|
 |  _ <  __/ (_| (_) | | | (_| \__ \   | | | | (_| | |  | | | | | | (_) | | | | |/ /  __/ |
 |_| \_\___|\___\___/|_|  \__,_|___/___|_| |_|\__,_|_|  |_| |_| |_|\___/|_| |_|_/___\___|_|
                                  |_____|

Script Python pour agréger les observations de certificats TLS à partir d'un fichier JSON et les enregistrer dans un fichier CSV.

usage: records_harmonizer.py [-h] -i INPUT [-o OUTPUT] [--max-count MAX_COUNT] [--min-count MIN_COUNT] [--since SINCE]
                             [--until UNTIL] [--group-by {sha1,ip}] [--sort-by {first_seen,last_seen,count}]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input JSON file
  -o OUTPUT, --output OUTPUT
                        Output CSV file
  --max-count MAX_COUNT
                        Maximum count threshold for records to be included
  --min-count MIN_COUNT
                        Minimum count threshold for records to be included
  --since SINCE         Only include records first seen after this date (YYYY-MM-DD)
  --until UNTIL         Only include records last seen before this date (YYYY-MM-DD)
  --group-by {sha1,ip}  Fields to aggregate by
  --sort-by {first_seen,last_seen,count}
                        Fields to sort by
```

### Fonctionnalités
Le script présente différentes options tout en restant fidèle aux consignes de l'exercice :
- agréger le document fourni en entrée par adresse IP et hash SHA1 du certificat (consigne initiale);
- filtrer les enregistrements selon des seuils de comptage minimum et maximum (`--min-count` et `--max-count`);
- filtrer les enregistrements selon des dates de première et dernière observation (`--since` et `--until`);
- grouper les enregistrements agrégés selon un critère spécifié (`--group-by`);
- trier les enregistrements agrégés selon un critère spécifié (`--sort-by`).

`group_by` et `sort_by` ne sont pas deux options mutuellement exclusives. Si les deux options sont actives, alors au sein d'un groupement, les données seront triées selon le critère spécifié par `sort_by`.
À l'exception du fichier d'entrée, toutes les options sont optionnelles et utilisables simultanément.
 
### Requirements
- Script réalisé en Python 3.12.3.
- Pas d'imports externes nécessaires.

### Évolutions possibles

Élargir cet outil pour n'importe quelles données en choisissant en option les champs à agréger. 

