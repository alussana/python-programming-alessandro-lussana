def generate_filter(filter_file):
    filter = open(filter_file)
    entries = []
    for line in filter:
        line = line.strip()
        entries.append(line)
    filter.close()
    return(entries)

def filter_db(db_file, filter):
    with gzip.open(db_file, 'rt') as db:
        hit = 0
        for line in db:

            if line[0] == ">":
                hit = 0
                line = line.strip()
                line_info = line.split('|')
                db_entry = line_info[1]
                for filter_entry in filter:
                    if db_entry == filter_entry:
                        hit = 1
                        print(line)
                        filter.remove(filter_entry)
                        break

            else:
                if hit == 1:
                    line = line.strip()
                    print(line)

if __name__ == '__main__':
    import sys
    import gzip
    db_file = sys.argv[1]
    filter_file = sys.argv[2]
    filter = generate_filter(filter_file)
    filter_db(db_file, filter)
