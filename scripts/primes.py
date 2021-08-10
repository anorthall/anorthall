import signal
import time


class PrimeDB:
    def __init__(self):
        self.num = 2
        self.keep_looping = True
        self.primes = []
        self.last_time = int(time.time() * 1000)
        self.start_time = time.time()

    def main(self):
        print("Calculating prime numbers...")

        while self.keep_looping:
            prime = True
            for i in range(2, self.num):
                if (self.num % i) == 0:
                    prime = False

            if prime:
                self.primes.append(self.num)
            else:
                prime = True

            if (self.num % 5000) == 0:
                n = i + 1
                t = int(time.time() * 1000)
                diff = t - self.last_time
                self.last_time = t

                if diff < 3000:
                    print(f"Up to: {n}. Time taken: {diff}ms.")
                else:
                    diff = diff / 1000
                    print(f"Up to: {n}. Time taken: {diff}sec.")

            self.num += 1


def handler(signum, frame):
    obj.keep_looping = False
    total_time = time.time() - obj.start_time

    print(
        "\n\n\n\n\n\nCtrl + C pressed. We were up to {} and found {} primes.".format(
            obj.num, len(obj.primes)
        )
    )
    print(f"Time taken to check primes: {total_time} seconds.")

    file_name = input("Please input a file name to save the list to:\n")

    start_time = int(time.time() * 1000)

    with open(file_name, "w") as text_file:
        for prime in obj.primes:
            text_file.write(f"{prime}\n")

        text_file.write(f"Total primes: {len(obj.primes)}\n")
        text_file.write(f"Total numbers checked: {obj.num}\n")

    end_time = int(time.time() * 1000)
    diff = end_time - start_time
    diff_seconds = diff / 1000
    exec_time = total_time + diff_seconds

    with open(file_name, "a") as text_file:
        text_file.write(f"Time taken checking primes: {total_time} seconds.\n")
        text_file.write(f"Time taken saving the file: {diff_seconds} seconds.\n")
        text_file.write(f"Total execution time: {exec_time} seconds.\n")

    if diff > 1000:
        diff = diff / 1000
        print(f"\n\nFile written. Time taken: {diff} seconds.")
    else:
        print(f"File written. Time taken: {diff} ms.")

    print("Exiting...")
    exit(1)


signal.signal(signal.SIGINT, handler)
obj = PrimeDB()
obj.main()
