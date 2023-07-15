import requests

def get_article_names(limit):
    base_url = 'https://jsonmock.hackerrank.com/api/articles'
    page_number = 1
    result = []

    while True:
        
        response = requests.get(f'{base_url}?page={page_number}')
        data = response.json()


        articles = data['data']

        for article in articles:
           
            if article['title']:
                article_name = article['title']
            elif article['story_title']:
                article_name = article['story_title']
            else:
                continue 

            comment_count = article['num_comments'] or 0

            result.append((article_name, comment_count))

        page_number += 1

        if len(result) >= limit or page_number > data['total_pages']:
            break

    result.sort(key=lambda x: (-x[1], x[0].lower()))

    print("Output==",[name for name, _ in result[:limit]])
    return [name for name, _ in result[:limit]]


get_article_names(2)

# Output is ['F.C.C. Repeals Net Neutrality Rules', 'Switch from Chrome to Firefox']