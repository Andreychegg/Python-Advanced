import logging
import random
import threading
import time

TOTAL_TICKETS = 10
DIRECTOR_TICKETS = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.semaphore = semaphore
        self.tickets_added = 0
        self.director_tickets = DIRECTOR_TICKETS
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global DIRECTOR_TICKETS
        is_running = True
        while is_running:
            if TOTAL_TICKETS <= 4:
                with self.semaphore:
                    printed_tickets = min(10 - TOTAL_TICKETS, DIRECTOR_TICKETS)
                    TOTAL_TICKETS += printed_tickets
                    DIRECTOR_TICKETS -= printed_tickets
                    logger.info(f'Director printed {printed_tickets} tickets; {DIRECTOR_TICKETS} left')
                    if DIRECTOR_TICKETS == 0:
                        is_running = False


def main():
    semaphore = threading.Semaphore()
    sellers = []

    director = Director(semaphore)
    director.start()

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    sellers.append(director)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()
