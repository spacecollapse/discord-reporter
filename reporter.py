import requests

print("Токен:")
token = input()

print("Айди сервера:")
guildid = input()

print("Айди канала:")
channelid = input()

print("Айди сообщения:")
messageid = input()

print("Причина:")
reason = input()
# - reasons:
# 1 - Незаконный контент
# 2 - Оскорбления
# 3 - Спам или фишинг ссылки
# 4 - Вред пользователям
# 5 - NSFW

url = "https://discord.com/api/v10/report"

jsonData = {
    "channel_id": channelid,
    "guild_id": guildid,
    "message_id": messageid,
    "reason": reason
}

total = 0
reported = 0

while True:
    total += 1
    try:
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.post(url, json=jsonData, headers=headers)

        if response.status_code == 201:
            reported += 1
            print("Репорт! (код: {})".format(response.status_code))
        else:
            print("Ошибка! (код: {})".format(response.status_code))
        
        print("Отправлено всего: {} Репортов отправлено: {}".format(total, reported))
    except:
        print("Ошибка")
