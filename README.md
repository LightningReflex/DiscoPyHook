<h1 align="center" id="title">DiscoPyHook</h1>

<p id="description">Simple discord webhook library in python created in a single file. Could probably be made much more efficient but it works. (Code could honestly not be more repetitive, someone please fix it)</p>

<p align="center"><img src="https://img.shields.io/discord/992429435687018588?label=Discord" alt="shields"> <img src="https://img.shields.io/github/license/LightningReflex/DiscoPyHook" alt="shields"></p>
<p>&nbsp;</p>

<h2>📝 Example</h2>
<p>Example code below</p>

```python
from DiscoPyHook import DiscoPyHook as DPH

webhook = DPH("https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyz1234567890")
webhook.setContent("Hello world!")

embed = DPH.Embed()

embed.setTitle("Real title")
embed.setDescription("Real description")

embed.setFooter(DPH.Footer().setText("You can even do (look at title)")).setAuthor(DPH.Author().setName("STUFF LIKE THIS"))
embed.addField(DPH.Field().setName("Field 1").setValue("Value 1").setInline(True))
# You could also replace every "set" with "get" like you could do "embed.getTitle()" or "embed.getFields()" (returns a list)

# This also works (they all have the "setRaw(object)" method):
embed.addField(DPH.Field().setRaw({"name": "Field 2", "value": "Value 2", "inline": True}))

# You can do
# "embed.setColorHex("00ff00")" or
# "embed.setColorRGB(0, 255, 0)" or
# "embed.setColorInt(65280)", but you could also do
# "embed.setColorInt(0x00ff00)" because python is cool
embed.setColorInt(0x00ff00)
webhook.addEmbed(embed)

webhook.send()
```
<p>&nbsp;</p>

<h2>💖 Support?</h2>
If you need support, contact me on discord: lightningreflex