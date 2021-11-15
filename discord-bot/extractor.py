from discord.enums import Status
import pafy


def return_dislike(url):
    url = url
    video = pafy.new(url)
    dislikes = video.dislikes
    title = video.title
    thumbnail = video.thumb
    stats = [dislikes, title, thumbnail]
    return stats
