import pafy


def return_dislike(url):
    url = url
    video = pafy.new(url)
    dislikes = video.dislikes
    title = video.title
    stats = [dislikes, title]
    return stats
