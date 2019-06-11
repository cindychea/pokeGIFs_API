# can use | jq in terminal
# for example:
#     curl -G "https://api.giphy.com/v1/gifs/search?api_key=iVaGpe0nASL0XASojscDOY4FxG0Lx9hc&q=squirtle&rating=g" | jq '.data[0].url'
#     curl -G "https://api.giphy.com/v1/gifs/search?api_key=iVaGpe0nASL0XASojscDOY4FxG0Lx9hc&q=squirtle&rating=g" | jq '.data[].url'
