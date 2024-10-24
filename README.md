# KEXP-Shows-Downloader

https://api.kexp.org/get_streaming_url/?bitrate=256&timestamp=2024-10-20T22:00:54Z


https://kexp-archive.streamguys1.com/content/kexp/20241023160006-38-967-drive-time.mp3

```
curl 'https://kexp-archive.streamguys1.com/content/kexp/20240315070006-4-485-the-morning-show.mp3?listeningSessionID=0CD_382_78__ef17e74236afc239e88f1de6cdaade26743a3ea6'   -H 'Accept: */*'   -H 'Accept-Language: es-ES,es;q=0.9,de;q=0.8,en;q=0.7,ca;q=0.6,fr;q=0.5,la;q=0.4,gl;q=0.3,pt;q=0.2'   -H 'Connection: keep-alive'   -H 'Cookie: AISSessionId=0CD_382_78__ef17e74236afc239e88f1de6cdaade26743a3ea6'   -H 'Range: bytes=0-'   -H 'Referer: https://www.kexp.org/'   -H 'Sec-Fetch-Dest: video'   -H 'Sec-Fetch-Mode: no-cors'   -H 'Sec-Fetch-Site: cross-site'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'   -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: "Linux"' --output ./prueba-morning-show.mp3

```

```
{"count":61451,"next":"https://api.kexp.org/v2/shows/?format=json&limit=1&offset=1&start_time_before=2024-10-03T14%3A00%3A52.000Z","previous":null,"results":[{"id":61474,"uri":"https://api.kexp.org/v2/shows/61474/?format=json","program":16,"program_uri":"https://api.kexp.org/v2/programs/16/?format=json","hosts":[26],"host_uris":["https://api.kexp.org/v2/hosts/26/?format=json"],"program_name":"The Morning Show","program_tags":"Rock,Eclectic,Variety Mix","host_names":["John Richards"],"tagline":"You Are Not Alone","image_uri":"https://www.kexp.org/filer/canonical/1676669191/28465/","start_time":"2024-10-03T07:00:52-07:00"}]}
```


La llamada al comando
```
GET /v2/shows/?expand=hosts&start_time_after=2022-10-02T10:00:00.000Z
```

genera el siguiente JSON
```json
{
    "count": 125,
    "next": "https://api.kexp.org/v2/shows/?expand=hosts&limit=20&offset=20&start_time_after=2024-10-02T10%3A00%3A00.000Z",
    "previous": null,
    "results": [
        {
            "id": 61589,
            "uri": "https://api.kexp.org/v2/shows/61589/",
            "program": 32,
            "program_uri": "https://api.kexp.org/v2/programs/32/",
            "hosts": [
                {
                    "id": 50,
                    "uri": "https://api.kexp.org/v2/hosts/50/",
                    "name": "Eva Walker",
                    "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/50/"
            ],
            "program_name": "Early",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Eva Walker"
            ],
            "tagline": "It's a Walker Wormhole Wednesday indeed!",
            "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
            "start_time": "2024-10-16T05:00:00-07:00"
        },
        {
            "id": 61588,
            "uri": "https://api.kexp.org/v2/shows/61588/",
            "program": 18,
            "program_uri": "https://api.kexp.org/v2/programs/18/",
            "hosts": [
                {
                    "id": 96,
                    "uri": "https://api.kexp.org/v2/hosts/96/",
                    "name": "Prometheus Brown",
                    "image_uri": "https://www.kexp.org/filer/canonical/1694562002/29427/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/96/"
            ],
            "program_name": "Variety Mix",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Prometheus Brown"
            ],
            "tagline": "Filling in for Abbie! Let's gooooooo",
            "image_uri": "https://www.kexp.org/filer/canonical/1694562002/29427/",
            "start_time": "2024-10-16T01:00:39-07:00"
        },
        {
            "id": 61587,
            "uri": "https://api.kexp.org/v2/shows/61587/",
            "program": 18,
            "program_uri": "https://api.kexp.org/v2/programs/18/",
            "hosts": [
                {
                    "id": 53,
                    "uri": "https://api.kexp.org/v2/hosts/53/",
                    "name": "Michele Myers",
                    "image_uri": "https://www.kexp.org/filer/canonical/1685033343/28896/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/53/"
            ],
            "program_name": "Variety Mix",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Michele Myers"
            ],
            "tagline": "Beats, rock, global and soulful - new and eclectic sets! IG @djmichelemyers or text 206-903-5397",
            "image_uri": "https://www.kexp.org/filer/canonical/1685033343/28896/",
            "start_time": "2024-10-15T22:03:00-07:00"
        },
        {
            "id": 61586,
            "uri": "https://api.kexp.org/v2/shows/61586/",
            "program": 20,
            "program_uri": "https://api.kexp.org/v2/programs/20/",
            "hosts": [
                {
                    "id": 98,
                    "uri": "https://api.kexp.org/v2/hosts/98/",
                    "name": "Jyoti B.Fly",
                    "image_uri": "https://www.kexp.org/filer/canonical/1697822338/29628/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/98/"
            ],
            "program_name": "Wo' Pop",
            "program_tags": "Electronic,World",
            "host_names": [
                "Jyoti B.Fly"
            ],
            "tagline": "Featuring world and electronic music - with your host Jyoti B.Fly (Insta @jyotibfly) - Text or email for shout outs - 206-245-8669 DJ@kexp.org",
            "image_uri": "https://www.kexp.org/filer/canonical/1697822338/29628/",
            "start_time": "2024-10-15T19:00:24-07:00"
        },
        {
            "id": 61585,
            "uri": "https://api.kexp.org/v2/shows/61585/",
            "program": 33,
            "program_uri": "https://api.kexp.org/v2/programs/33/",
            "hosts": [
                {
                    "id": 19,
                    "uri": "https://api.kexp.org/v2/hosts/19/",
                    "name": "Evie Stokes",
                    "image_uri": "https://www.kexp.org/filer/canonical/1697218264/29608/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/19/"
            ],
            "program_name": "Drive Time",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Evie Stokes"
            ],
            "tagline": "Hi there! Say hello: @djeviestokes on Instagram.",
            "image_uri": "https://www.kexp.org/filer/canonical/1697218264/29608/",
            "start_time": "2024-10-15T16:00:10-07:00"
        },
        {
            "id": 61584,
            "uri": "https://api.kexp.org/v2/shows/61584/",
            "program": 14,
            "program_uri": "https://api.kexp.org/v2/programs/14/",
            "hosts": [
                {
                    "id": 55,
                    "uri": "https://api.kexp.org/v2/hosts/55/",
                    "name": "Larry Mizell, Jr.",
                    "image_uri": "https://www.kexp.org/filer/canonical/1669673896/28158/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/55/"
            ],
            "program_name": "The Afternoon Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Larry Mizell, Jr."
            ],
            "tagline": "Hey! good to be back! Say hi!",
            "image_uri": "https://www.kexp.org/filer/canonical/1669673896/28158/",
            "start_time": "2024-10-15T13:00:05-07:00"
        },
        {
            "id": 61583,
            "uri": "https://api.kexp.org/v2/shows/61583/",
            "program": 15,
            "program_uri": "https://api.kexp.org/v2/programs/15/",
            "hosts": [
                {
                    "id": 27,
                    "uri": "https://api.kexp.org/v2/hosts/27/",
                    "name": "Kevin Cole",
                    "image_uri": "https://www.kexp.org/filer/canonical/1529968117/10616/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/27/"
            ],
            "program_name": "The Midday Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Kevin Cole"
            ],
            "tagline": "What is your name? Kevin Cole on The Midday Show! How are you? Happy Tuesday! You can reach us at 206-903-5397 or dj@kexp.org.",
            "image_uri": "https://www.kexp.org/filer/canonical/1529968117/10616/",
            "start_time": "2024-10-15T10:06:15-07:00"
        },
        {
            "id": 61582,
            "uri": "https://api.kexp.org/v2/shows/61582/",
            "program": 16,
            "program_uri": "https://api.kexp.org/v2/programs/16/",
            "hosts": [
                {
                    "id": 26,
                    "uri": "https://api.kexp.org/v2/hosts/26/",
                    "name": "John Richards",
                    "image_uri": "https://www.kexp.org/filer/canonical/1676669191/28465/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/26/"
            ],
            "program_name": "The Morning Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "John Richards"
            ],
            "tagline": "You Are Not Alone",
            "image_uri": "https://www.kexp.org/filer/canonical/1676669191/28465/",
            "start_time": "2024-10-15T07:01:20-07:00"
        },
        {
            "id": 61581,
            "uri": "https://api.kexp.org/v2/shows/61581/",
            "program": 32,
            "program_uri": "https://api.kexp.org/v2/programs/32/",
            "hosts": [
                {
                    "id": 50,
                    "uri": "https://api.kexp.org/v2/hosts/50/",
                    "name": "Eva Walker",
                    "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/50/"
            ],
            "program_name": "Early",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Eva Walker"
            ],
            "tagline": "It's Tuesday in SPACE and STOP MAKING SENSE DAY!",
            "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
            "start_time": "2024-10-15T05:00:00-07:00"
        },
        {
            "id": 61580,
            "uri": "https://api.kexp.org/v2/shows/61580/",
            "program": 18,
            "program_uri": "https://api.kexp.org/v2/programs/18/",
            "hosts": [
                {
                    "id": 33,
                    "uri": "https://api.kexp.org/v2/hosts/33/",
                    "name": "Mike Ramos",
                    "image_uri": "https://www.kexp.org/filer/canonical/1661184077/27584/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/33/"
            ],
            "program_name": "Variety Mix",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Mike Ramos"
            ],
            "tagline": "Overnight with Mike Ramos - Indigenous Peoples Day 2024 Edition ヾ(⌐■_■)ノ♪ hmu dj@kexp.org // 206-903-5397",
            "image_uri": "https://www.kexp.org/filer/canonical/1661184077/27584/",
            "start_time": "2024-10-15T01:00:00-07:00"
        },
        {
            "id": 61579,
            "uri": "https://api.kexp.org/v2/shows/61579/",
            "program": 18,
            "program_uri": "https://api.kexp.org/v2/programs/18/",
            "hosts": [
                {
                    "id": 38,
                    "uri": "https://api.kexp.org/v2/hosts/38/",
                    "name": "Sean",
                    "image_uri": "https://www.kexp.org/filer/canonical/1529966588/10607/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/38/"
            ],
            "program_name": "Variety Mix",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Sean"
            ],
            "tagline": "~ Indigenous Peoples Day ~",
            "image_uri": "https://www.kexp.org/filer/canonical/1529966588/10607/",
            "start_time": "2024-10-14T22:00:15-07:00"
        },
        {
            "id": 61578,
            "uri": "https://api.kexp.org/v2/shows/61578/",
            "program": 2,
            "program_uri": "https://api.kexp.org/v2/programs/2/",
            "hosts": [
                {
                    "id": 99,
                    "uri": "https://api.kexp.org/v2/hosts/99/",
                    "name": "Goyri",
                    "image_uri": "https://www.kexp.org/filer/canonical/1728667218/31134/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/99/"
            ],
            "program_name": "El Sonido",
            "program_tags": "Latin,World",
            "host_names": [
                "Goyri"
            ],
            "tagline": "Hi, I'm Goyri doing my first show tonight for El Sonido celebrating Indigenous People's Day.",
            "image_uri": "https://www.kexp.org/filer/canonical/1728667218/31134/",
            "start_time": "2024-10-14T19:02:11-07:00"
        },
        {
            "id": 61577,
            "uri": "https://api.kexp.org/v2/shows/61577/",
            "program": 33,
            "program_uri": "https://api.kexp.org/v2/programs/33/",
            "hosts": [
                {
                    "id": 19,
                    "uri": "https://api.kexp.org/v2/hosts/19/",
                    "name": "Evie Stokes",
                    "image_uri": "https://www.kexp.org/filer/canonical/1697218264/29608/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/19/"
            ],
            "program_name": "Drive Time",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Evie Stokes"
            ],
            "tagline": "Celebrating Indigenous People's Day today! Sharing music from people and communities who have been actively resisting histories of colonization since time immemorial. Thanks for being here today.",
            "image_uri": "https://www.kexp.org/filer/canonical/1697218264/29608/",
            "start_time": "2024-10-14T15:59:42-07:00"
        },
        {
            "id": 61576,
            "uri": "https://api.kexp.org/v2/shows/61576/",
            "program": 14,
            "program_uri": "https://api.kexp.org/v2/programs/14/",
            "hosts": [
                {
                    "id": 98,
                    "uri": "https://api.kexp.org/v2/hosts/98/",
                    "name": "Jyoti B.Fly",
                    "image_uri": "https://www.kexp.org/filer/canonical/1697822338/29628/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/98/"
            ],
            "program_name": "The Afternoon Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Jyoti B.Fly"
            ],
            "tagline": "Today on the Afternoon Show, we’ll explore  Indigenous communities, celebrate their rich languages, and advocate for their ideas. We’ll feature Indigenous artists from around the world, creating a space to honor their culture and creativity",
            "image_uri": "https://www.kexp.org/filer/canonical/1697822338/29628/",
            "start_time": "2024-10-14T13:01:19-07:00"
        },
        {
            "id": 61575,
            "uri": "https://api.kexp.org/v2/shows/61575/",
            "program": 15,
            "program_uri": "https://api.kexp.org/v2/programs/15/",
            "hosts": [
                {
                    "id": 93,
                    "uri": "https://api.kexp.org/v2/hosts/93/",
                    "name": "Tory J",
                    "image_uri": "https://www.kexp.org/filer/canonical/1694561444/29424/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/93/"
            ],
            "program_name": "The Midday Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Tory J"
            ],
            "tagline": "Indigenous Peoples Day every day!\n\nfollow Tory @whalesonthemouth if you feel like it",
            "image_uri": "https://www.kexp.org/filer/canonical/1694561444/29424/",
            "start_time": "2024-10-14T10:03:24-07:00"
        },
        {
            "id": 61574,
            "uri": "https://api.kexp.org/v2/shows/61574/",
            "program": 16,
            "program_uri": "https://api.kexp.org/v2/programs/16/",
            "hosts": [
                {
                    "id": 94,
                    "uri": "https://api.kexp.org/v2/hosts/94/",
                    "name": "Kevin Sur",
                    "image_uri": "https://www.kexp.org/filer/canonical/1697822410/29630/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/94/"
            ],
            "program_name": "The Morning Show",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Kevin Sur"
            ],
            "tagline": "It's Indigenous Peoples! Day.",
            "image_uri": "https://www.kexp.org/filer/canonical/1697822410/29630/",
            "start_time": "2024-10-14T07:01:44-07:00"
        },
        {
            "id": 61573,
            "uri": "https://api.kexp.org/v2/shows/61573/",
            "program": 32,
            "program_uri": "https://api.kexp.org/v2/programs/32/",
            "hosts": [
                {
                    "id": 50,
                    "uri": "https://api.kexp.org/v2/hosts/50/",
                    "name": "Eva Walker",
                    "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/50/"
            ],
            "program_name": "Early",
            "program_tags": "Rock,Eclectic,Variety Mix",
            "host_names": [
                "Eva Walker"
            ],
            "tagline": "Happy Indigenous People's Day!",
            "image_uri": "https://www.kexp.org/filer/canonical/1583367534/22025/",
            "start_time": "2024-10-14T05:00:00-07:00"
        },
        {
            "id": 61572,
            "uri": "https://api.kexp.org/v2/shows/61572/",
            "program": 39,
            "program_uri": "https://api.kexp.org/v2/programs/39/",
            "hosts": [
                {
                    "id": 93,
                    "uri": "https://api.kexp.org/v2/hosts/93/",
                    "name": "Tory J",
                    "image_uri": "https://www.kexp.org/filer/canonical/1694561444/29424/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/93/"
            ],
            "program_name": "Sounds of Survivance",
            "program_tags": "Eclectic,Variety,World",
            "host_names": [
                "Tory J"
            ],
            "tagline": "Special Guest Liv Rion on Indigenous People's Day",
            "image_uri": "https://www.kexp.org/filer/canonical/1694561444/29424/",
            "start_time": "2024-10-14T03:00:21-07:00"
        },
        {
            "id": 61571,
            "uri": "https://api.kexp.org/v2/shows/61571/",
            "program": 4,
            "program_uri": "https://api.kexp.org/v2/programs/4/",
            "hosts": [
                {
                    "id": 97,
                    "uri": "https://api.kexp.org/v2/hosts/97/",
                    "name": "Noel Brass Jr.",
                    "image_uri": "https://www.kexp.org/filer/canonical/1695667292/29498/",
                    "thumbnail_uri": "",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/97/"
            ],
            "program_name": "Jazz Theatre",
            "program_tags": "Jazz",
            "host_names": [
                "Noel Brass Jr."
            ],
            "tagline": "Kicking off Indigenous People's Day with a special  episode Interview with Mali Obomsawin",
            "image_uri": "https://www.kexp.org/filer/canonical/1695667292/29498/",
            "start_time": "2024-10-14T01:01:07-07:00"
        },
        {
            "id": 61570,
            "uri": "https://api.kexp.org/v2/shows/61570/",
            "program": 5,
            "program_uri": "https://api.kexp.org/v2/programs/5/",
            "hosts": [
                {
                    "id": 21,
                    "uri": "https://api.kexp.org/v2/hosts/21/",
                    "name": "Guest DJ",
                    "image_uri": "https://www.kexp.org/static/assets/img/host_default.png",
                    "thumbnail_uri": "https://www.kexp.org/static/assets/img/host_default.png",
                    "is_active": true
                }
            ],
            "host_uris": [
                "https://api.kexp.org/v2/hosts/21/"
            ],
            "program_name": "Midnight in a Perfect World",
            "program_tags": "Eclectic,DJ,Variety Mix",
            "host_names": [
                "Guest DJ"
            ],
            "tagline": "Terror Cactus",
            "image_uri": "https://www.kexp.org/static/assets/img/host_default.png",
            "start_time": "2024-10-14T00:00:17-07:00"
        }
    ]
}
```