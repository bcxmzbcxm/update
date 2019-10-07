false = False
true = True

data = {
    "path": {
        "6-1只打潜艇": {"map": "601", "skipMax": 2, "detail": {"A": {"night": false, "round_about": false, "sl": false,
                                                                 "detail": [{"enemy": 2, "num": 1, "deal": 0},
                                                                            {"enemy": 9, "num": 1, "deal": 0}],
                                                                 "format": "5", "spyFailSl": true}}},
        "6-1不打轻母": {"map": "601", "skipMax": 2, "detail": {
            "A": {"night": false, "round_about": false, "sl": false, "detail": [{"enemy": 2, "num": 1, "deal": 0}],
                  "format": "5", "spyFailSl": true}}},
        "4-3偷铝": {"map": "403", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": true, "detail": [], "format": "2", "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": true, "detail": [], "format": "2", "spyFailSl": false}}},
        "3-1偷弹": {"map": "301", "skipMax": 2, "detail": {
            "A": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "C": {"night": false, "round_about": false, "sl": true, "detail": [], "format": "2", "spyFailSl": false}}},
        "2-1偷胖次": {"map": "201", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": 1, "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": false, "detail": [], "format": 1, "spyFailSl": false},
            "F": {"night": true, "round_about": false, "sl": false, "detail": [{"enemy": 16, "num": 7, "deal": 0}],
                  "format": 1, "spyFailSl": false}}},
        "2-1周常": {"map": "201", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": 1, "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": false, "detail": [], "format": 1, "spyFailSl": false},
            "F": {"night": true, "round_about": false, "sl": false, "detail": [], "format": 1, "spyFailSl": false}}},

        "5-5捞b25": {"map": "505", "skipMax": 2, "detail": {
            "C": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "F": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "I": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},
        "5-2C炸鱼": {"map": "502", "skipMax": 2, "detail": {"C": {"night": false, "round_about": false, "sl": false,
                                                                "detail": [{"enemy": 10, "num": 1, "deal": 0},
                                                                           {"enemy": 2, "num": 1, "deal": 0}],
                                                                "format": "5", "spyFailSl": true}}},
        "3-2周常": {"map": "302", "skipMax": 2, "detail": {
            "C": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "E": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "G": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},

        "3-3周常": {"map": "303", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "I": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "J": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "K": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},

        "4-1周常": {"map": "401", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "F": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "I": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},

        "4-2周常": {"map": "402", "skipMax": 2, "detail": {
            "A": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "C": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "E": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "H": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "J": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},

        "5-3周常": {"map": "503", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "D": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "G": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "H": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},

        "6-3周常": {"map": "603", "skipMax": 2, "detail": {
            "B": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "E": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "H": {"night": false, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "J": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}},
        "2-5中路": {"map": "205", "skipMax": 2, "detail": {
            "A": {"night": false, "round_about": true, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "B": {"night": false, "round_about": true, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "D": {"night": false, "round_about": true, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "H": {"night": false, "round_about": true, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "K": {"night": false, "round_about": true, "sl": false, "detail": [], "format": "2", "spyFailSl": false},
            "O": {"night": true, "round_about": false, "sl": false, "detail": [], "format": "2", "spyFailSl": false}}}

    }
}

import json

with open("data/path.json", 'w') as f:
    f.write(json.dumps(data))
