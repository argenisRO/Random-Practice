# Scrabble Game
# ArgenisRO
# 6.00.1x Scrabble Example Personally Constructed


def titleArt():
    center = '\t' * 3
    print(center, ' _________       ________      ________      ________      ________      ________      ___           _______ ')
    print(center, '| \   ____\     |\   ____\    |\   __  \    |\   __  \    |\   __  \    |\   __  \    |\  \         |\  ___ \ ')
    print(center, ' \ \  \___|_    \ \  \___|    \ \  \|\  \   \ \  \|\  \   \ \  \|\ /_   \ \  \|\ /_   \ \  \        \ \   __/| ')
    print(center, '  \ \_____  \    \ \  \        \ \   _  _\   \ \   __  \   \ \   __  \   \ \   __  \   \ \  \        \ \  \_|/__ ')
    print(center, '   \|____|\  \    \ \  \____    \ \  \ \ \_   \ \  \ \  \   \ \  \|\  \   \ \  \|\  \   \ \  \____    \ \  \_|\ \ ')
    print(center, '     ____\_\  \    \ \_______\   \ \__\ \ __\  \ \__\ \__\   \ \_______\   \ \_______\   \ \_______\   \ \_______\ ')
    print(center, '    |\_________\    \|_______|    \|__|\|___|   \|__|\|__|    \|_______|    \|_______|    \|_______|    \|_______| ')
    print(center, '    \|__________| ')


def difficultyArt():
    center = '\t' * 5
    print(center, "  _____ _                                _ _  __  __ _            _ _         ")
    print(center, " / ____| |                              | (_)/ _|/ _(_)          | | |        ")
    print(center, "| |    | |__   ___   ___  ___  ___    __| |_| |_| |_ _  ___ _   _| | |_ _   _ ")
    print(center, "| |    | '_ \ / _ \ / _ \/ __|/ _ \  / _` | |  _|  _| |/ __| | | | | __| | | |")
    print(center, "| |____| | | | (_) | (_) \__ |  __/ | (_| | | | | | | | (__| |_| | | |_| |_| |")
    print(center, " \_____|_| |_|\___/ \___/|___/\___|  \__,_|_|_| |_| |_|\___|\__,_|_|\__|\__, |")
    print(center, "                                                                         __/ |")
    print(center, "                                                                        |___/ ")


def menuArt():
    center = '\t' * 9
    print(center, " __  __                  ")
    print(center, "|  \/  |                 ")
    print(center, "| \  / | ___ _ __  _   _ ")
    print(center, "| |\/| |/ _ | '_ \| | | |")
    print(center, "| |  | |  __| | | | |_| |")
    print(center, "|_|  |_|\___|_| |_|\__,_|")
    print(center, "")


def optionsArt():
    center = '\t' * 8
    print(center, "    ____        _   _                  ")
    print(center, "   / __ \      | | (_)                 ")
    print(center, "  | |  | |_ __ | |_ _  ___  _ __  ___  ")
    print(center, "  | |  | | '_ \| __| |/ _ \| '_ \/ __| ")
    print(center, "  | |__| | |_) | |_| | (_) | | | \__ \ ")
    print(center, "   \____/| .__/ \__|_|\___/|_| |_|___/ ")
    print(center, "         |_|                           ")


def endArt():
    center = '\t' * 4
    print(center, "  _______ _                 _          ______           _____  _             _             ")
    print(center, " |__   __| |               | |        |  ____|         |  __ \| |           (_)            ")
    print(center, "    | |  | |__   __ _ _ __ | | _____  | |__ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _ ")
    print(center, "    | |  | '_ \ / _` | '_ \| |/ / __| |  __/ _ \| '__| |  ___/| |/ _` | | | | | '_ \ / _` |")
    print(center, "    | |  | | | | (_| | | | |   <\__ \ | | | (_) | |    | |    | | (_| | |_| | | | | | (_| |")
    print(center, "    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, |")
    print(center, "                                                                         _/ |          _/ |")
    print(center, "                                                                       |___/          |__/ ")


def yourTurn():
    center = '\t' * 7
    print(center, " __     __                _______               ")
    print(center, " \ \   / /               |__   __|              ")
    print(center, "  \ \_/ /__  _   _ _ __     | |_   _ _ __ _ __  ")
    print(center, "   \   / _ \| | | | '__|    | | | | | '__| '_ \ ")
    print(center, "    | | (_) | |_| | |       | | |_| | |  | | | |")
    print(center, "    |_|\___/ \__,_|_|       |_|\__,_|_|  |_| |_|")


def enemyTurn():
    center = '\t' * 7
    print(center, "  ______                              _______               ")
    print(center, " |  ____|                            |__   __|              ")
    print(center, " | |__   _ __   ___ _ __ ___  _   _     | |_   _ _ __ _ __  ")
    print(center, " |  __| | '_ \ / _ \ '_ ` _ \| | | |    | | | | | '__| '_ \ ")
    print(center, " | |____| | | |  __/ | | | | | |_| |    | | |_| | |  | | | |")
    print(center, " |______|_| |_|\___|_| |_| |_|\__, |    |_|\__,_|_|  |_| |_|")
    print(center, "                               __/ |                        ")
    print(center, "                              |___/                         ")
