def log_transaction(transaction):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{transaction}\n")
