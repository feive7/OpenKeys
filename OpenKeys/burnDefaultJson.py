# This script sets the default json content
import re
json_path = "shortcuts.json"
data = """"{
    "version": "25.20.4",
    "prefix": "`",
    "goto_character": "^",
    "start_minimized": false,
    "enable_logging": true,
    "shortcuts": {
        "openkeys": "Welcome to OpenKeys, a free and open-source text replacement program! (type `about)",
        "about": "OpenKeys is meant to be a free alternative to other pricey text replacement programs such as ShortKeys, and TextExpander. (type `features)",
        "features": "This program is, for the most part, fully configurable within this json. You can even include an external url, so your entire company can all be on the same shortcuts. But my personal favorite, is what I call the Goto Character. (type `gotochar)",
        "gotochar": "With the Goto Character feature, you can tell the program to put your text cursor in a specific spot after pasting. Instead of at the end, this shortcut will set the cursor ^ <- Here. Of course, the Goto Character is configurable. (type `newline)",
        "newline": "This\\nProgram\\nSupports\\nNewlines!\\n(I don't know if that's impressive or not)\\n(type `github)",
		"github": "Because this program is open-source, all of the source code is available on github (`link), feel free to make a bug report!",
		"link": "https://github.com/feive7/OpenKeys"
	}
}"""
code = ""
#with open(json_path) as json:
#data = json.read()
data = data.replace("\\n","\\\\n")
data = data.replace("\n","\\n")
data = data.replace("\"","\\\"")
print(data)