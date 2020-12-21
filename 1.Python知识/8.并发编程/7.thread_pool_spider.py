from concurrent.futures import ThreadPoolExecutor, as_completed

import blog_spider

# craw: 使用 pool.map 方式
with ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse: 使用 future 方式
with ThreadPoolExecutor() as pool:
    futures = dict()
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url
    # 按照顺序返回
    # for future,url in futures.items():
    #     print(url, future.result())

    # 谁先执行结束，就先返回谁
    for future in as_completed(futures):
        url = futures[future]
        print(url, future.result())
