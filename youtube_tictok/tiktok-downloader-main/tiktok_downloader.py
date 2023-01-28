import http.client
import json
import urllib.request

def getVideoUrl(vid):
    conn = http.client.HTTPSConnection("api.tiktokv.com")
    payload = ''
    headers = {
      
    }
    conn.request("GET", "/aweme/v1/multi/aweme/detail/?aweme_ids=%5B" + vid + "%5D", payload, headers)
    res = conn.getresponse()
    data = res.read()
    obj = json.loads(data.decode("utf-8"))
    return obj["aweme_details"][0]["video"]["play_addr"]["url_list"][0];


if __name__ == "__main__":
    id_video = "7107995521595215131"
    videoUrl = getVideoUrl(id_video)
    print("Video URL: " + videoUrl)
    name = id_video + ".mp4"
    urllib.request.urlretrieve(videoUrl, name) 
