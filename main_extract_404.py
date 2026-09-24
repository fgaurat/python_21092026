from pprint import pprint


from glob import glob


def main():
    all_logs = glob("log_files/*.log")
    pprint(all_logs)

    for log_file in all_logs:
        with open(log_file) as f:
            for line in f:
                print(line.strip())


if __name__ == '__main__':
    main()
