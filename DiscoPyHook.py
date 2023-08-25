import requests
import threading
import datetime

class DiscoPyHook:
    class Embed:
        def __init__(self):
            self.data = {}
        def setTitle(self, title): # String
            self.data["title"] = title
            return self
        def getTitle(self):
            if "title" not in self.data:
                return None
            return self.data["title"]

        def setDescription(self, description): # String
            self.data["description"] = description
            return self
        def getDescription(self):
            if "description" not in self.data:
                return None
            return self.data["description"]

        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def setTimestamp(self, timestamp): # Integer (unix timestamp)
            # convert to ISO8601 timestamp
            self.data["timestamp"] = datetime.datetime.utcfromtimestamp(timestamp).isoformat()
            return self
        def getTimestamp(self):
            if "timestamp" not in self.data:
                return None
            return self.data["timestamp"]

        def setColorInt(self, color): # Integer
            self.data["color"] = color
            return self
        def setColorHex(self, color): # String
            self.data["color"] = int(color, 16)
            return self
        def setColorRGB(self, r, g, b): # Integer
            self.data["color"] = (r << 16) + (g << 8) + b
            return self
        def getColorInt(self):
            if "color" not in self.data:
                return None
            return self.data["color"]
        def getColorHex(self):
            if "color" not in self.data:
                return None
            return hex(self.data["color"])
        def getColorRGB(self):
            if "color" not in self.data:
                return None
            return (self.data["color"] >> 16, (self.data["color"] >> 8) & 0xFF, self.data["color"] & 0xFF)

        def setFooter(self, footer): # Footer
            self.data["footer"] = footer.build()
            return self
        def getFooter(self):
            if "footer" not in self.data:
                return None
            return self.data["footer"]

        def setImage(self, image): # Image
            self.data["image"] = image.build()
            return self
        def getImage(self):
            if "image" not in self.data:
                return None
            return self.data["image"]

        def setThumbnail(self, thumbnail): # Thumbnail
            self.data["thumbnail"] = thumbnail.build()
            return self
        def getThumbnail(self):
            if "thumbnail" not in self.data:
                return None
            return self.data["thumbnail"]

        def setVideo(self, video): # Video
            self.data["video"] = video.build()
            return self
        def getVideo(self):
            if "video" not in self.data:
                return None
            return self.data["video"]

        def setProvider(self, provider): # Provider
            self.data["provider"] = provider.build()
            return self
        def getProvider(self):
            if "provider" not in self.data:
                return None
            return self.data["provider"]

        def setAuthor(self, author): # Author
            self.data["author"] = author.build()
            return self
        def getAuthor(self):
            if "author" not in self.data:
                return None
            return self.data["author"]

        def addField(self, field): # Field
            if self.getFields() == None:
                self.data["fields"] = []
            self.data["fields"].append(field.build())
            return self
        def removeField(self, index):
            if self.getFields() == None:
                return self
            self.data["fields"].pop(index)
            return self
        def getFields(self):
            if "fields" not in self.data:
                return None
            return self.data["fields"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Footer:
        def __init__(self):
            self.data = {}
        def setText(self, text): # String
            self.data["text"] = text
            return self
        def getText(self):
            if "text" not in self.data:
                return None
            return self.data["text"]

        def setIconURL(self, icon_url): # String
            self.data["icon_url"] = icon_url
            return self
        def getIconURL(self):
            if "icon_url" not in self.data:
                return None
            return self.data["icon_url"]

        def setProxyIconURL(self, proxy_icon_url): # String
            self.data["proxy_icon_url"] = proxy_icon_url
            return self
        def getProxyIconURL(self):
            if "proxy_icon_url" not in self.data:
                return None
            return self.data["proxy_icon_url"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Image:
        def __init__(self):
            self.data = {}
        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def setProxyURL(self, proxy_url): # String
            self.data["proxy_url"] = proxy_url
            return self
        def getProxyURL(self):
            if "proxy_url" not in self.data:
                return None
            return self.data["proxy_url"]

        def setHeight(self, height): # Integer
            self.data["height"] = height
            return self
        def getHeight(self):
            if "height" not in self.data:
                return None
            return self.data["height"]

        def setWidth(self, width): # Integer
            self.data["width"] = width
            return self
        def getWidth(self):
            if "width" not in self.data:
                return None
            return self.data["width"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Thumbnail:
        def __init__(self):
            self.data = {}
        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def setProxyURL(self, proxy_url): # String
            self.data["proxy_url"] = proxy_url
            return self
        def getProxyURL(self):
            if "proxy_url" not in self.data:
                return None
            return self.data["proxy_url"]

        def setHeight(self, height): # Integer
            self.data["height"] = height
            return self
        def getHeight(self):
            if "height" not in self.data:
                return None
            return self.data["height"]

        def setWidth(self, width): # Integer
            self.data["width"] = width
            return self
        def getWidth(self):
            if "width" not in self.data:
                return None
            return self.data["width"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Video:
        def __init__(self):
            self.data = {}
        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def setProxyURL(self, proxy_url): # String
            self.data["proxy_url"] = proxy_url
            return self
        def getProxyURL(self):
            if "proxy_url" not in self.data:
                return None
            return self.data["proxy_url"]

        def setHeight(self, height): # Integer
            self.data["height"] = height
            return self
        def getHeight(self):
            if "height" not in self.data:
                return None
            return self.data["height"]

        def setWidth(self, width): # Integer
            self.data["width"] = width
            return self
        def getWidth(self):
            if "width" not in self.data:
                return None
            return self.data["width"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Provider:
        def __init__(self):
            self.data = {}
        def setName(self, name): # String
            self.data["name"] = name
            return self
        def getName(self):
            if "name" not in self.data:
                return None
            return self.data["name"]

        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def build(self):
            return self.data
    class Author:
        def __init__(self):
            self.data = {}
        def setName(self, name): # String
            self.data["name"] = name
            return self
        def getName(self):
            if "name" not in self.data:
                return None
            return self.data["name"]

        def setURL(self, url): # String
            self.data["url"] = url
            return self
        def getURL(self):
            if "url" not in self.data:
                return None
            return self.data["url"]

        def setIconURL(self, icon_url): # String
            self.data["icon_url"] = icon_url
            return self
        def getIconURL(self):
            if "icon_url" not in self.data:
                return None
            return self.data["icon_url"]

        def setProxyIconURL(self, proxy_icon_url): # String
            self.data["proxy_icon_url"] = proxy_icon_url
            return self
        def getProxyIconURL(self):
            if "proxy_icon_url" not in self.data:
                return None
            return self.data["proxy_icon_url"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data
    class Field:
        def __init__(self):
            self.data = {}
        def setName(self, name): # String
            self.data["name"] = name
            return self
        def getName(self):
            if "name" not in self.data:
                return None
            return self.data["name"]

        def setValue(self, value): # String
            self.data["value"] = value
            return self
        def getValue(self):
            if "value" not in self.data:
                return None
            return self.data["value"]

        def setInline(self, inline): # Boolean
            self.data["inline"] = inline
            return self
        def getInline(self):
            if "inline" not in self.data:
                return None
            return self.data["inline"]

        def setRaw(self, data):
            self.data = data
            return self

        def build(self):
            return self.data


    def __init__(self, url):
        self.url = url
        self.data = {}

    def setContent(self, content): # String
        self.data["content"] = content
        return self
    def getContent(self):
        if "content" not in self.data:
            return None
        return self.data["content"]

    def setUsername(self, username): # String
        self.data["username"] = username
        return self
    def getUsername(self):
        if "username" not in self.data:
            return None
        return self.data["username"]

    def setAvatarURL(self, avatar_url): # String
        self.data["avatar_url"] = avatar_url
        return self
    def getAvatarURL(self):
        if "avatar_url" not in self.data:
            return None
        return self.data["avatar_url"]

    def setTTS(self, tts): # Boolean
        self.data["tts"] = tts
        return self
    def getTTS(self):
        if "tts" not in self.data:
            return None
        return self.data["tts"]

    def addEmbed(self, embed): # Embed
        if self.getEmbeds() == None:
            self.data["embeds"] = []
        self.data["embeds"].append(embed.build())
        return self
    def removeEmbed(self, index): # Integer
        if self.getEmbeds() == None:
            return self
        self.data["embeds"].pop(index)
        return self
    def getEmbeds(self):
        if "embeds" not in self.data:
            return None
        return self.data["embeds"]

    def setRaw(self, data):
        self.data = data
        return self

    def build(self):
        return self.data

    def send(self):
        threading.Thread(target=requests.post, args=(self.url,), kwargs={
            "json": self.data
        }).start()
        return self
