import requests

def what_anime_is_that(path='handlers/trace_moe/1734586717.jpg'):
    json_data = requests.post("https://api.trace.moe/search",
    files={"image": open(path, "rb")}
    ).json()

    first_item = json_data['result'][0]

    title = f"Название: {first_item['filename']}"
    similarity = f"Процент схожести: {first_item['similarity']*100}"
    link = f"Ссылка на видео: {first_item['video']}"

    return title, similarity, link

a = what_anime_is_that()
print(a)
