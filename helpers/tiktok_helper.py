import requests
import json

class TiktokHelper:

    def __init__(self):
        pass


    @staticmethod
    def get_data_video_search(keyword, count=30):
        url = r'https://tiktok-video-no-watermark2.p.rapidapi.com/challenge/search'
        headers = {
            "X-RapidAPI-Key": "9da0HvwzgVmshZ0i3qoYnLNIWajip1h5uGUjsn58iBW9aVnyO0",
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }

        querystring = {"keywords": keyword, "count": count}

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)['data']
        return data

    def get_detail_video(challenge_id, count=1):
        url = "https://tiktok-video-no-watermark2.p.rapidapi.com/challenge/posts"
        headers = {
            "X-RapidAPI-Key": "9da0HvwzgVmshZ0i3qoYnLNIWajip1h5uGUjsn58iBW9aVnyO0",
            "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
        }
        if count == 1:
            querystring = {"challenge_id": str(challenge_id), "count": "20"}
        else:
            querystring = {"challenge_id": str(challenge_id), "count": "20", "cursor": 20*count}

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)['data']
        return data
