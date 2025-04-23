games = ["cs2", "pubg", "lol", "csgo"]

for game in games:
    print("Моя любимых игры 2024 - " + game)

games.append("dota2")
games.remove("csgo")
del games[0]

print("Моя любимых игры 2025 -", len(games))
print(games)