import json

def get_reply(message):

    with open("../data/notices.json", encoding="utf-8") as f:
        notices = json.load(f)

    for notice in notices:
        for keyword in notice["keywords"]:
            if keyword in message:
                return notice["content"]

    return "공지에서 찾지 못했습니다. 과사무실에 문의해주세요."
