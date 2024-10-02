from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='SUA_APIKEY')

all_articles = newsapi.get_everything(
    q='bitcoin',
    soucers= 'globo, info-money',
    domains='globo.com, infomoney.com.br',
    from_param='2024-08-01',
    to='2024-09-21',
    language='pt',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    sort_by='publishedAt',
)

print(all_articles)