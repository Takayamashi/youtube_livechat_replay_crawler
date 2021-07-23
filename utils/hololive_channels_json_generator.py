import json


def main():
    with open('./holostats_list.json', 'r') as f:
        liver_list = json.load(f)
        channel_names = []
        channel_urls = []
        channel_list = []

        for liver in liver_list:
            channel_names.append(liver)

        for info in liver_list.values():
            channel_urls.append(info["youtube"])

        channel_count = len(channel_names)

        for i in range(channel_count):
            channel = {"channel_id": channel_names[i],
                       "name": channel_urls[i]}
            channel_list.append(channel)

    with open('./data/hololive_channels.json', 'w') as f:
        json.dump({"channel_list": channel_list},
                  f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
