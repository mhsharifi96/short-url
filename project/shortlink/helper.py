def check_link(link):
    if 'http' not in link:
        link = 'https://'+link
    return link