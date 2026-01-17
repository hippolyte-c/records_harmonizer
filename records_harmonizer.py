import argparse
import csv
import json


"""
Chargement du fichier JSON fourni en entrée
"""
def load_json_file(file_path):

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

"""
Agrégation des données du document.
Dans cette fonctions, on applique les différents filtres et tris demandés.
"""
def aggregate_records_by_sha1_ip(records, min_count, max_count,since_date, until_date, group_by, sort_by):

    aggregated = {}

    for record in records:
        sha1 = record['sha1']
        ip = record['ip']
        first_seen = record['first_seen']
        last_seen = record['last_seen']
        count = record['count']

        if since_date and first_seen < since_date:
            print(first_seen, since_date)
            continue
        if until_date and last_seen > until_date:
            continue

        if sha1+ip not in aggregated:
            aggregated[sha1+ip] = {
                'sha1': sha1,
                'ip': ip,
                'first_seen': first_seen,
                'last_seen': last_seen,
                'count': count
            }

        else:
            aggregated[sha1+ip]['first_seen'] = min(aggregated[sha1+ip]['first_seen'], first_seen)
            aggregated[sha1+ip]['last_seen'] = max(aggregated[sha1+ip]['last_seen'], last_seen)
            aggregated[sha1+ip]['count'] += count

    aggregated = [record for record in aggregated.values()]
    if max_count:
        aggregated = [record for record in aggregated if record['count'] <= max_count]
    if min_count:
        aggregated = [record for record in aggregated if record['count'] >= min_count]

    """
    sort_by et group_by ne sont pas mutuellement exclusifs.
    sort_by est effectué en premier pour pour que le tri final visuel soit effectué selon group_by.
    """
    if sort_by:
        aggregated = sorted(aggregated, key=lambda x: x[sort_by])
    if group_by:
        aggregated = sorted(aggregated, key=lambda x: x[group_by])

    return aggregated


"""
Sauvegarde des données agrégées dans un fichier CSV
"""
def save_to_csv(aggregated_records, output_file):

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['sha1', 'ip', 'first_seen', 'last_seen', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in aggregated_records:
            writer.writerow(record)


def main():
    print(r"""
  ____                        _         _                                      _              
 |  _ \ ___  ___ ___  _ __ __| |___    | |__   __ _ _ __ _ __ ___   ___  _ __ (_)_______ _ __ 
 | |_) / _ \/ __/ _ \| '__/ _` / __|   | '_ \ / _` | '__| '_ ` _ \ / _ \| '_ \| |_  / _ \ '__|
 |  _ <  __/ (_| (_) | | | (_| \__ \   | | | | (_| | |  | | | | | | (_) | | | | |/ /  __/ |   
 |_| \_\___|\___\___/|_|  \__,_|___/___|_| |_|\__,_|_|  |_| |_| |_|\___/|_| |_|_/___\___|_|   
                                  |_____|                                                                                                                              
          """)

    parser = argparse.ArgumentParser(description="Aggregate TLS certificate observations")
    parser.add_argument("-i", "--input", help="Input JSON file", required=True)
    parser.add_argument("-o", "--output", default="aggregated.csv", help="Output CSV file")

    parser.add_argument("--max-count", type=int, default=None, help="Maximum count threshold for records to be included")
    parser.add_argument("--min-count", type=int, default=None, help="Minimum count threshold for records to be included")
    parser.add_argument("--since", type=str, help="Only include records first seen after this date (YYYY-MM-DD)")
    parser.add_argument("--until", type=str, help="Only include records last seen before this date (YYYY-MM-DD)")
    
    parser.add_argument(
        "--group-by",
        choices=("sha1", "ip"),
        default=None,
        help="Fields to aggregate by",
    )
    parser.add_argument(
        "--sort-by",
        choices=("first_seen", "last_seen", "count"),
        default=None,
        help="Fields to sort by",
    )

    args = parser.parse_args()

    since_date, until_date = None, None
    if args.since:
        since_date = args.since + "T00:00:00"
    if args.until:
        until_date = args.until + "T23:59:59"

    steps = [
        "LOADING RECORDS....................[OK]",
        "AGGREGATING RECORDS................[OK]",
        "SAVING TO CSV......................[OK]",
    ]

    # Lecture du fichier JSON d'entrée
    records = load_json_file(args.input)
    print(steps[0])
    print("Total records loaded:", len(records))

    # Agrégation des records
    aggregated_records = aggregate_records_by_sha1_ip(
        records,
        args.min_count,
        args.max_count,
        since_date,
        until_date,
        args.group_by,
        args.sort_by)
    print(steps[1])
    print("Total aggregated records:", len(aggregated_records))

    # Sauvegarde dans un fichier CSV
    save_to_csv(aggregated_records, args.output)
    print(steps[2])
    print(f"Aggregated records saved to {args.output}")


if __name__ == "__main__":
    main()