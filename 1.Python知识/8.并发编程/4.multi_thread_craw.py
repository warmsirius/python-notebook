import threading
import time

import blog_spider


def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("multi_thread end")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread cost: ", int(end - start), "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread cost: ", int(end - start), "seconds")

    # single_thread begin
    # ...
    # single_thread end
    # single_thread cost: 9 seconds
    #
    # multi_thread begin
    # ...
    # multi_thread end
    # multi_thread cost: 2 seconds
    