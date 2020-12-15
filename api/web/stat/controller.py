from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

from api.web.stat.manager import statManager


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


# 原始数据的第0行和第0列都是label
cooc_matrix_data = [
    ['', '文献计量', '知识图谱', '文献计量分析', '研究热点', 'CiteSpace', '可视化分析', '可视化', '文献计量法', 'Citespace', '发展态势', 'VOSviewer'],
    ['文献计量', '0', '21', '0', '12', '15', '10', '10', '0', '3', '5', '2'],
    ['知识图谱', '21', '0', '5', '7', '9', '7', '3', '2', '1', '0', '2'],
    ['文献计量分析', '0', '5', '0', '7', '2', '3', '1', '0', '1', '0', '1'],
    ['研究热点', '12', '7', '7', '0', '1', '5', '1', '2', '3', '0', '0'],
    ['CiteSpace', '15', '9', '2', '1', '0', '4', '4', '0', '0', '1', '2'],
    ['可视化分析', '10', '7', '3', '5', '4', '0', '0', '2', '0', '0', '3'],
    ['可视化', '10', '3', '1', '1', '4', '0', '0', '1', '0', '0', '0'],
    ['文献计量法', '0', '2', '0', '2', '0', '2', '1', '0', '1', '0', '0'],
    ['Citespace', '3', '1', '1', '3', '0', '0', '0', '1', '0', '0', '0'],
    ['发展态势', '5', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
    ['VOSviewer', '2', '2', '1', '0', '2', '3', '0', '0', '0', '0', '0']
]

force_data = {
    "nodes": [
        {
            "color": "#4f19c7",
            "label": "jquery",
            "attributes": {},
            "y": -404.26147,
            "x": -739.36383,
            "id": "jquery",
            "size": 4.7252817
        },
        {
            "color": "#c71969",
            "label": "backbone",
            "attributes": {},
            "y": -862.7517,
            "x": -134.2215,
            "id": "backbone",
            "size": 6.1554675
        },
        {
            "color": "#c71969",
            "label": "underscore",
            "attributes": {},
            "y": -734.4221,
            "x": -75.53079,
            "id": "underscore",
            "size": 100.0
        },
        {
            "color": "#c71969",
            "label": "faye",
            "attributes": {},
            "y": 624.50604,
            "x": -818.97516,
            "id": "faye",
            "size": 0.67816025
        },
        {
            "color": "#c71919",
            "label": "socket.io",
            "attributes": {},
            "y": 120.37976,
            "x": -710.59204,
            "id": "socket.io",
            "size": 19.818306
        },
        {
            "color": "#c71969",
            "label": "requirejs",
            "attributes": {},
            "y": -612.5541,
            "x": 71.52897,
            "id": "requirejs",
            "size": 4.0862627
        },
        {
            "color": "#c71969",
            "label": "amdefine",
            "attributes": {},
            "y": -556.3107,
            "x": 1202.1166,
            "id": "amdefine",
            "size": 2.3822114
        },
        {
            "color": "#1984c7",
            "label": "mongoose",
            "attributes": {},
            "y": 378.15536,
            "x": -1150.2018,
            "id": "mongoose",
            "size": 10.81118
        },
        {
            "color": "#c76919",
            "label": "underscore.deferred",
            "attributes": {},
            "y": 477.03778,
            "x": -127.03764,
            "id": "underscore.deferred",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "cheerio",
            "attributes": {},
            "y": -404.62427,
            "x": -338.03128,
            "id": "cheerio",
            "size": 8.163814
        },
        {
            "color": "#c76919",
            "label": "lodash",
            "attributes": {},
            "y": -380.16626,
            "x": 118.30771,
            "id": "lodash",
            "size": 18.935852
        },
        {
            "color": "#c71969",
            "label": "faye-websocket",
            "attributes": {},
            "y": 649.6795,
            "x": -697.4635,
            "id": "faye-websocket",
            "size": 1.0128845
        },
        {
            "color": "#c71969",
            "label": "dateformat",
            "attributes": {},
            "y": -531.28235,
            "x": 381.10724,
            "id": "dateformat",
            "size": 3.3863845
        },
        {
            "color": "#c79f19",
            "label": "mkdirp",
            "attributes": {},
            "y": -224.0287,
            "x": 317.77667,
            "id": "mkdirp",
            "size": 23.713282
        },
        {
            "color": "#c71919",
            "label": "express",
            "attributes": {},
            "y": -230.14833,
            "x": -644.2716,
            "id": "express",
            "size": 49.608772
        },
        {
            "color": "#c71919",
            "label": "connect",
            "attributes": {},
            "y": 294.88266,
            "x": -933.4234,
            "id": "connect",
            "size": 19.574871
        },
        {
            "color": "#c71919",
            "label": "consolidate",
            "attributes": {},
            "y": 495.22098,
            "x": -101.796974,
            "id": "consolidate",
            "size": 3.0212305
        },
        {
            "color": "#c78419",
            "label": "hogan.js",
            "attributes": {},
            "y": 79.99539,
            "x": 930.74255,
            "id": "hogan.js",
            "size": 3.2646663
        },
        {
            "color": "#c719b9",
            "label": "node-uuid",
            "attributes": {},
            "y": 815.4766,
            "x": -378.0424,
            "id": "node-uuid",
            "size": 13.488974
        },
        {
            "color": "#1984c7",
            "label": "async",
            "attributes": {},
            "y": 41.25936,
            "x": 157.57562,
            "id": "async",
            "size": 73.161194
        },
        {
            "color": "#c719b9",
            "label": "redis",
            "attributes": {},
            "y": 56.938953,
            "x": -895.56586,
            "id": "redis",
            "size": 17.475237
        },
        {
            "color": "#199fc7",
            "label": "backoff",
            "attributes": {},
            "y": 810.54626,
            "x": -275.69714,
            "id": "backoff",
            "size": 0.58687174
        },
        {
            "color": "#9f19c7",
            "label": "bytes",
            "attributes": {},
            "y": 380.12103,
            "x": -1005.2705,
            "id": "bytes",
            "size": 0.8607372
        },
        {
            "color": "#1984c7",
            "label": "temp",
            "attributes": {},
            "y": 144.45488,
            "x": 1057.7959,
            "id": "temp",
            "size": 4.0558333
        },
        {
            "color": "#69c719",
            "label": "mustache",
            "attributes": {},
            "y": -554.3333,
            "x": -554.2029,
            "id": "mustache",
            "size": 3.7819674
        },
        {
            "color": "#8419c7",
            "label": "request",
            "attributes": {},
            "y": 241.89249,
            "x": -147.57906,
            "id": "request",
            "size": 64.54965
        },
        {
            "color": "#c71969",
            "label": "underscore.string",
            "attributes": {},
            "y": -528.7333,
            "x": 58.392773,
            "id": "underscore.string",
            "size": 7.311788
        },
        {
            "color": "#c71969",
            "label": "jquery-browserify",
            "attributes": {},
            "y": 385.31375,
            "x": -231.44426,
            "id": "jquery-browserify",
            "size": 0.83030766
        },
        {
            "color": "#8419c7",
            "label": "event-stream",
            "attributes": {},
            "y": 858.8598,
            "x": 313.5104,
            "id": "event-stream",
            "size": 3.0212305
        },
        {
            "color": "#19c719",
            "label": "log4js",
            "attributes": {},
            "y": 350.19534,
            "x": 7.309183,
            "id": "log4js",
            "size": 3.4776726
        },
        {
            "color": "#19c719",
            "label": "optimist",
            "attributes": {},
            "y": 171.80579,
            "x": 599.53815,
            "id": "optimist",
            "size": 48.6046
        },
        {
            "color": "#1919c7",
            "label": "mocha",
            "attributes": {},
            "y": -178.11076,
            "x": -393.3754,
            "id": "mocha",
            "size": 7.889948
        },
        {
            "color": "#1984c7",
            "label": "should",
            "attributes": {},
            "y": -198.63869,
            "x": -334.43466,
            "id": "should",
            "size": 4.7252817
        },
        {
            "color": "#c79f19",
            "label": "semver",
            "attributes": {},
            "y": 375.80014,
            "x": 414.43912,
            "id": "semver",
            "size": 8.711545
        },
        {
            "color": "#69c719",
            "label": "q",
            "attributes": {},
            "y": -389.02567,
            "x": -423.78125,
            "id": "q",
            "size": 12.54566
        },
        {
            "color": "#c74f19",
            "label": "node-fs",
            "attributes": {},
            "y": -94.528114,
            "x": -319.42093,
            "id": "node-fs",
            "size": 1.225891
        },
        {
            "color": "#19c7b9",
            "label": "colorize",
            "attributes": {},
            "y": -432.71243,
            "x": 37.15866,
            "id": "colorize",
            "size": 0.55644226
        },
        {
            "color": "#c76919",
            "label": "github",
            "attributes": {},
            "y": 244.62839,
            "x": -383.83453,
            "id": "github",
            "size": 1.6519039
        },
        {
            "color": "#19c719",
            "label": "prompt",
            "attributes": {},
            "y": 819.16583,
            "x": 748.4038,
            "id": "prompt",
            "size": 4.1471214
        },
        {
            "color": "#19c719",
            "label": "colors",
            "attributes": {},
            "y": -265.6326,
            "x": 694.03375,
            "id": "colors",
            "size": 33.359425
        },
        {
            "color": "#19c7b9",
            "label": "commander",
            "attributes": {},
            "y": -682.1726,
            "x": -479.44443,
            "id": "commander",
            "size": 43.21858
        },
        {
            "color": "#9fc719",
            "label": "validator",
            "attributes": {},
            "y": -429.05365,
            "x": -668.0554,
            "id": "validator",
            "size": 3.6602497
        },
        {
            "color": "#c7b919",
            "label": "grunt",
            "attributes": {},
            "y": -710.3381,
            "x": 683.8534,
            "id": "grunt",
            "size": 9.959153
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-clean",
            "attributes": {},
            "y": -386.1587,
            "x": -292.83875,
            "id": "grunt-contrib-clean",
            "size": 1.0128845
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-concat",
            "attributes": {},
            "y": 224.41283,
            "x": 99.38902,
            "id": "grunt-contrib-concat",
            "size": 0.76944876
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-less",
            "attributes": {},
            "y": -611.3146,
            "x": -215.58498,
            "id": "grunt-contrib-less",
            "size": 0.6173013
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-jshint",
            "attributes": {},
            "y": -938.3397,
            "x": 548.61926,
            "id": "grunt-contrib-jshint",
            "size": 1.3171794
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-uglify",
            "attributes": {},
            "y": -871.8892,
            "x": 160.96982,
            "id": "grunt-contrib-uglify",
            "size": 1.1346025
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-watch",
            "attributes": {},
            "y": 80.96627,
            "x": -616.9189,
            "id": "grunt-contrib-watch",
            "size": 0.8607372
        },
        {
            "color": "#19c719",
            "label": "http-proxy",
            "attributes": {},
            "y": 418.763,
            "x": 711.7106,
            "id": "http-proxy",
            "size": 4.6339936
        },
        {
            "color": "#b9c719",
            "label": "mime",
            "attributes": {},
            "y": 34.348167,
            "x": -284.14108,
            "id": "mime",
            "size": 14.858301
        },
        {
            "color": "#c78419",
            "label": "ycssmin",
            "attributes": {},
            "y": -392.55402,
            "x": -199.6149,
            "id": "ycssmin",
            "size": 0.4651538
        },
        {
            "color": "#3419c7",
            "label": "mongodb",
            "attributes": {},
            "y": 522.375,
            "x": -1089.2416,
            "id": "mongodb",
            "size": 11.237192
        },
        {
            "color": "#19b9c7",
            "label": "ini",
            "attributes": {},
            "y": 357.40076,
            "x": 1076.3447,
            "id": "ini",
            "size": 1.5301858
        },
        {
            "color": "#c79f19",
            "label": "slide",
            "attributes": {},
            "y": -272.38953,
            "x": 928.9824,
            "id": "slide",
            "size": 0.40429485
        },
        {
            "color": "#c79f19",
            "label": "abbrev",
            "attributes": {},
            "y": -185.45026,
            "x": 1187.2019,
            "id": "abbrev",
            "size": 0.43472436
        },
        {
            "color": "#c79f19",
            "label": "graceful-fs",
            "attributes": {},
            "y": -400.4116,
            "x": 864.7834,
            "id": "graceful-fs",
            "size": 1.8649102
        },
        {
            "color": "#c79f19",
            "label": "minimatch",
            "attributes": {},
            "y": -332.82092,
            "x": 923.4708,
            "id": "minimatch",
            "size": 4.6339936
        },
        {
            "color": "#c79f19",
            "label": "nopt",
            "attributes": {},
            "y": 0.9246719,
            "x": 648.4921,
            "id": "nopt",
            "size": 5.303442
        },
        {
            "color": "#c79f19",
            "label": "rimraf",
            "attributes": {},
            "y": -169.53479,
            "x": 842.5285,
            "id": "rimraf",
            "size": 7.159641
        },
        {
            "color": "#c79f19",
            "label": "which",
            "attributes": {},
            "y": -237.25739,
            "x": 1191.029,
            "id": "which",
            "size": 1.8649102
        },
        {
            "color": "#c79f19",
            "label": "tar",
            "attributes": {},
            "y": -160.8614,
            "x": 572.6111,
            "id": "tar",
            "size": 3.2646663
        },
        {
            "color": "#c79f19",
            "label": "fstream",
            "attributes": {},
            "y": -86.683586,
            "x": 522.8266,
            "id": "fstream",
            "size": 2.5343587
        },
        {
            "color": "#c79f19",
            "label": "inherits",
            "attributes": {},
            "y": 289.38367,
            "x": 639.7362,
            "id": "inherits",
            "size": 3.4472432
        },
        {
            "color": "#c79f19",
            "label": "read",
            "attributes": {},
            "y": 376.2344,
            "x": 537.65076,
            "id": "read",
            "size": 1.4997563
        },
        {
            "color": "#c719b9",
            "label": "lru-cache",
            "attributes": {},
            "y": 63.76733,
            "x": 758.7636,
            "id": "lru-cache",
            "size": 2.1996343
        },
        {
            "color": "#c79f19",
            "label": "node-gyp",
            "attributes": {},
            "y": -206.755,
            "x": 941.12946,
            "id": "node-gyp",
            "size": 1.165032
        },
        {
            "color": "#c79f19",
            "label": "fstream-npm",
            "attributes": {},
            "y": 172.07289,
            "x": 792.2891,
            "id": "fstream-npm",
            "size": 0.52601284
        },
        {
            "color": "#c79f19",
            "label": "archy",
            "attributes": {},
            "y": -15.182732,
            "x": 1288.449,
            "id": "archy",
            "size": 0.67816025
        },
        {
            "color": "#c79f19",
            "label": "npmlog",
            "attributes": {},
            "y": -713.69055,
            "x": 856.64276,
            "id": "npmlog",
            "size": 1.4084679
        },
        {
            "color": "#c79f19",
            "label": "ansi",
            "attributes": {},
            "y": -722.70416,
            "x": 996.9021,
            "id": "ansi",
            "size": 1.165032
        },
        {
            "color": "#c79f19",
            "label": "npm-registry-client",
            "attributes": {},
            "y": -163.23782,
            "x": 770.89215,
            "id": "npm-registry-client",
            "size": 0.70858973
        },
        {
            "color": "#c79f19",
            "label": "read-package-json",
            "attributes": {},
            "y": -328.63486,
            "x": 835.7924,
            "id": "read-package-json",
            "size": 0.6173013
        },
        {
            "color": "#c79f19",
            "label": "glob",
            "attributes": {},
            "y": -542.05096,
            "x": 502.02698,
            "id": "glob",
            "size": 14.88873
        },
        {
            "color": "#c79f19",
            "label": "osenv",
            "attributes": {},
            "y": 83.11953,
            "x": 1170.4095,
            "id": "osenv",
            "size": 0.67816025
        },
        {
            "color": "#c76919",
            "label": "retry",
            "attributes": {},
            "y": -149.41582,
            "x": 1088.8419,
            "id": "retry",
            "size": 0.55644226
        },
        {
            "color": "#34c719",
            "label": "once",
            "attributes": {},
            "y": 632.73914,
            "x": 692.4719,
            "id": "once",
            "size": 0.92159617
        },
        {
            "color": "#c79f19",
            "label": "npmconf",
            "attributes": {},
            "y": 263.6715,
            "x": 880.9455,
            "id": "npmconf",
            "size": 0.70858973
        },
        {
            "color": "#c79f19",
            "label": "opener",
            "attributes": {},
            "y": 30.311459,
            "x": 1306.2058,
            "id": "opener",
            "size": 0.43472436
        },
        {
            "color": "#3419c7",
            "label": "append",
            "attributes": {},
            "y": -216.35048,
            "x": 23.50861,
            "id": "append",
            "size": 0.4651538
        },
        {
            "color": "#3419c7",
            "label": "clone",
            "attributes": {},
            "y": 52.33028,
            "x": -407.7309,
            "id": "clone",
            "size": 2.4430702
        },
        {
            "color": "#c71919",
            "label": "ejs",
            "attributes": {},
            "y": 264.84995,
            "x": -421.52237,
            "id": "ejs",
            "size": 11.298051
        },
        {
            "color": "#9f19c7",
            "label": "debug",
            "attributes": {},
            "y": -75.5553,
            "x": -880.5015,
            "id": "debug",
            "size": 15.923333
        },
        {
            "color": "#9f19c7",
            "label": "out",
            "attributes": {},
            "y": -141.5042,
            "x": -27.64139,
            "id": "out",
            "size": 0.43472436
        },
        {
            "color": "#1919c7",
            "label": "when",
            "attributes": {},
            "y": -798.01276,
            "x": -874.1786,
            "id": "when",
            "size": 3.8123972
        },
        {
            "color": "#c78419",
            "label": "coffee-script",
            "attributes": {},
            "y": -915.89026,
            "x": 81.49971,
            "id": "coffee-script",
            "size": 44.131462
        },
        {
            "color": "#c79f19",
            "label": "adm-zip",
            "attributes": {},
            "y": 198.17334,
            "x": 893.567,
            "id": "adm-zip",
            "size": 1.3780384
        },
        {
            "color": "#c7b919",
            "label": "findup-sync",
            "attributes": {},
            "y": -535.91614,
            "x": 345.53296,
            "id": "findup-sync",
            "size": 0.6173013
        },
        {
            "color": "#c78419",
            "label": "node-minify",
            "attributes": {},
            "y": -772.7816,
            "x": 284.06558,
            "id": "node-minify",
            "size": 0.76944876
        },
        {
            "color": "#19c719",
            "label": "watch",
            "attributes": {},
            "y": 794.0542,
            "x": 1113.2292,
            "id": "watch",
            "size": 3.7211087
        },
        {
            "color": "#19c784",
            "label": "bal-util",
            "attributes": {},
            "y": 630.7962,
            "x": 1637.5715,
            "id": "bal-util",
            "size": 1.0128845
        },
        {
            "color": "#19c784",
            "label": "extendr",
            "attributes": {},
            "y": 674.9556,
            "x": 1661.8947,
            "id": "extendr",
            "size": 0.4651538
        },
        {
            "color": "#19c784",
            "label": "taskgroup",
            "attributes": {},
            "y": 557.3904,
            "x": 1473.007,
            "id": "taskgroup",
            "size": 0.67816025
        },
        {
            "color": "#19c784",
            "label": "typechecker",
            "attributes": {},
            "y": 655.7608,
            "x": 1672.5186,
            "id": "typechecker",
            "size": 0.4651538
        },
        {
            "color": "#c7199f",
            "label": "underscorem",
            "attributes": {},
            "y": -865.8074,
            "x": -106.96772,
            "id": "underscorem",
            "size": 0.6173013
        },
        {
            "color": "#c719b9",
            "label": "hubot",
            "attributes": {},
            "y": -683.4332,
            "x": -280.204,
            "id": "hubot",
            "size": 1.165032
        },
        {
            "color": "#1969c7",
            "label": "ndarray-ops",
            "attributes": {},
            "y": -1321.741,
            "x": 518.3953,
            "id": "ndarray-ops",
            "size": 0.58687174
        },
        {
            "color": "#1969c7",
            "label": "ndarray",
            "attributes": {},
            "y": -1302.119,
            "x": 501.15656,
            "id": "ndarray",
            "size": 1.1041731
        },
        {
            "color": "#1969c7",
            "label": "typedarray-pool",
            "attributes": {},
            "y": -1032.3728,
            "x": 964.9717,
            "id": "typedarray-pool",
            "size": 0.6173013
        },
        {
            "color": "#c71919",
            "label": "jade",
            "attributes": {},
            "y": -449.40155,
            "x": -173.24167,
            "id": "jade",
            "size": 20.031315
        },
        {
            "color": "#b9c719",
            "label": "nodemailer",
            "attributes": {},
            "y": -531.05963,
            "x": 847.43915,
            "id": "nodemailer",
            "size": 3.873256
        },
        {
            "color": "#9fc719",
            "label": "pkginfo",
            "attributes": {},
            "y": 1029.6494,
            "x": 657.2629,
            "id": "pkginfo",
            "size": 8.498538
        },
        {
            "color": "#c78419",
            "label": "eco",
            "attributes": {},
            "y": -986.8328,
            "x": 61.016094,
            "id": "eco",
            "size": 2.230064
        },
        {
            "color": "#19c7b9",
            "label": "github-flavored-markdown",
            "attributes": {},
            "y": -805.08057,
            "x": -594.8061,
            "id": "github-flavored-markdown",
            "size": 0.92159617
        },
        {
            "color": "#c79f19",
            "label": "filed",
            "attributes": {},
            "y": 123.003525,
            "x": -254.39879,
            "id": "filed",
            "size": 1.3780384
        },
        {
            "color": "#19c7b9",
            "label": "wrench",
            "attributes": {},
            "y": -524.69977,
            "x": -186.77402,
            "id": "wrench",
            "size": 8.559398
        },
        {
            "color": "#c71984",
            "label": "flatiron",
            "attributes": {},
            "y": 816.91064,
            "x": 876.8348,
            "id": "flatiron",
            "size": 1.9561987
        },
        {
            "color": "#19b9c7",
            "label": "winston",
            "attributes": {},
            "y": 695.1258,
            "x": 881.2038,
            "id": "winston",
            "size": 11.845781
        },
        {
            "color": "#c71919",
            "label": "coffeekup",
            "attributes": {},
            "y": -987.40234,
            "x": 85.66932,
            "id": "coffeekup",
            "size": 0.55644226
        },
        {
            "color": "#c78419",
            "label": "stylus",
            "attributes": {},
            "y": -620.4443,
            "x": -586.76886,
            "id": "stylus",
            "size": 10.020013
        },
        {
            "color": "#8419c7",
            "label": "querystring",
            "attributes": {},
            "y": 1011.7739,
            "x": 758.26154,
            "id": "querystring",
            "size": 1.9257691
        },
        {
            "color": "#8419c7",
            "label": "xml2json",
            "attributes": {},
            "y": 806.3456,
            "x": -601.0259,
            "id": "xml2json",
            "size": 1.6214744
        },
        {
            "color": "#1984c7",
            "label": "nano",
            "attributes": {},
            "y": -75.38197,
            "x": -114.47825,
            "id": "nano",
            "size": 1.5910448
        },
        {
            "color": "#c78419",
            "label": "less",
            "attributes": {},
            "y": -358.01407,
            "x": -128.87897,
            "id": "less",
            "size": 9.928724
        },
        {
            "color": "#c78419",
            "label": "uglify-js",
            "attributes": {},
            "y": -699.5852,
            "x": 177.18362,
            "id": "uglify-js",
            "size": 22.252666
        },
        {
            "color": "#c78419",
            "label": "clean-css",
            "attributes": {},
            "y": -807.94244,
            "x": -442.73334,
            "id": "clean-css",
            "size": 3.7819674
        },
        {
            "color": "#19c719",
            "label": "filesize",
            "attributes": {},
            "y": -56.161583,
            "x": -210.30255,
            "id": "filesize",
            "size": 0.52601284
        },
        {
            "color": "#c71984",
            "label": "strftime",
            "attributes": {},
            "y": 209.59007,
            "x": -0.24881881,
            "id": "strftime",
            "size": 0.70858973
        },
        {
            "color": "#4f19c7",
            "label": "canvas",
            "attributes": {},
            "y": 463.22067,
            "x": -290.9267,
            "id": "canvas",
            "size": 3.1429486
        },
        {
            "color": "#b9c719",
            "label": "common",
            "attributes": {},
            "y": 500.33102,
            "x": -227.09238,
            "id": "common",
            "size": 0.83030766
        },
        {
            "color": "#19b9c7",
            "label": "structr",
            "attributes": {},
            "y": -1252.3774,
            "x": 318.85583,
            "id": "structr",
            "size": 1.4997563
        },
        {
            "color": "#1934c7",
            "label": "simple-mime",
            "attributes": {},
            "y": -174.76685,
            "x": 7.712948,
            "id": "simple-mime",
            "size": 0.40429485
        },
        {
            "color": "#1934c7",
            "label": "haml",
            "attributes": {},
            "y": 221.30989,
            "x": 174.83754,
            "id": "haml",
            "size": 0.55644226
        },
        {
            "color": "#19b9c7",
            "label": "step",
            "attributes": {},
            "y": -1171.119,
            "x": 261.83853,
            "id": "step",
            "size": 4.2688394
        },
        {
            "color": "#1934c7",
            "label": "datetime",
            "attributes": {},
            "y": 419.69788,
            "x": 791.56323,
            "id": "datetime",
            "size": 0.4955833
        },
        {
            "color": "#c71969",
            "label": "inflection",
            "attributes": {},
            "y": -550.88916,
            "x": 1271.2019,
            "id": "inflection",
            "size": 1.3476089
        },
        {
            "color": "#1934c7",
            "label": "vows",
            "attributes": {},
            "y": 398.0463,
            "x": 791.03455,
            "id": "vows",
            "size": 3.751538
        },
        {
            "color": "#c78419",
            "label": "docco",
            "attributes": {},
            "y": -878.3072,
            "x": -420.23013,
            "id": "docco",
            "size": 1.0737435
        },
        {
            "color": "#34c719",
            "label": "readable-stream",
            "attributes": {},
            "y": 492.42526,
            "x": -531.76953,
            "id": "readable-stream",
            "size": 3.873256
        },
        {
            "color": "#8419c7",
            "label": "sax",
            "attributes": {},
            "y": 610.6721,
            "x": -534.7558,
            "id": "sax",
            "size": 2.7169356
        },
        {
            "color": "#8419c7",
            "label": "xml2js",
            "attributes": {},
            "y": 210.87439,
            "x": -510.32123,
            "id": "xml2js",
            "size": 8.894122
        },
        {
            "color": "#8419c7",
            "label": "libxmljs",
            "attributes": {},
            "y": 92.88487,
            "x": -1068.4481,
            "id": "libxmljs",
            "size": 1.7431923
        },
        {
            "color": "#c7b919",
            "label": "handlebars",
            "attributes": {},
            "y": -423.4632,
            "x": 590.7474,
            "id": "handlebars",
            "size": 8.285532
        },
        {
            "color": "#1969c7",
            "label": "numeric",
            "attributes": {},
            "y": -247.50432,
            "x": -210.03926,
            "id": "numeric",
            "size": 0.58687174
        },
        {
            "color": "#c71969",
            "label": "tap",
            "attributes": {},
            "y": -312.4931,
            "x": 551.4122,
            "id": "tap",
            "size": 1.4693269
        },
        {
            "color": "#69c719",
            "label": "boo",
            "attributes": {},
            "y": -200.40657,
            "x": 75.31598,
            "id": "boo",
            "size": 0.58687174
        },
        {
            "color": "#19c7b9",
            "label": "walk",
            "attributes": {},
            "y": -584.2039,
            "x": 383.56738,
            "id": "walk",
            "size": 2.3517818
        },
        {
            "color": "#8419c7",
            "label": "errs",
            "attributes": {},
            "y": 45.422947,
            "x": -102.39036,
            "id": "errs",
            "size": 0.6173013
        },
        {
            "color": "#199fc7",
            "label": "through",
            "attributes": {},
            "y": 649.42224,
            "x": 320.47504,
            "id": "through",
            "size": 10.14173
        },
        {
            "color": "#199fc7",
            "label": "duplexer",
            "attributes": {},
            "y": 940.3869,
            "x": 251.87953,
            "id": "duplexer",
            "size": 1.3476089
        },
        {
            "color": "#199fc7",
            "label": "shell-quote",
            "attributes": {},
            "y": 850.67114,
            "x": 118.35625,
            "id": "shell-quote",
            "size": 0.52601284
        },
        {
            "color": "#199fc7",
            "label": "split",
            "attributes": {},
            "y": 750.0239,
            "x": 348.1923,
            "id": "split",
            "size": 1.1346025
        },
        {
            "color": "#3419c7",
            "label": "csv",
            "attributes": {},
            "y": 509.271,
            "x": -160.78777,
            "id": "csv",
            "size": 1.7127627
        },
        {
            "color": "#c719b9",
            "label": "memcached",
            "attributes": {},
            "y": 1149.197,
            "x": -234.76114,
            "id": "memcached",
            "size": 1.0128845
        },
        {
            "color": "#c78419",
            "label": "express-resource",
            "attributes": {},
            "y": -175.72437,
            "x": -1060.0989,
            "id": "express-resource",
            "size": 0.7998782
        },
        {
            "color": "#c71919",
            "label": "connect-assets",
            "attributes": {},
            "y": -554.7191,
            "x": -72.89341,
            "id": "connect-assets",
            "size": 0.7998782
        },
        {
            "color": "#1984c7",
            "label": "knox",
            "attributes": {},
            "y": -5.803794,
            "x": -617.46643,
            "id": "knox",
            "size": 3.112519
        },
        {
            "color": "#b9c719",
            "label": "aws-sdk",
            "attributes": {},
            "y": 359.47635,
            "x": -628.1506,
            "id": "aws-sdk",
            "size": 1.4693269
        },
        {
            "color": "#19c7b9",
            "label": "fs-extra",
            "attributes": {},
            "y": -203.57794,
            "x": 428.15845,
            "id": "fs-extra",
            "size": 4.2079806
        },
        {
            "color": "#c71969",
            "label": "awssum",
            "attributes": {},
            "y": -279.23215,
            "x": -325.59766,
            "id": "awssum",
            "size": 0.83030766
        },
        {
            "color": "#84c719",
            "label": "walker",
            "attributes": {},
            "y": -165.20312,
            "x": -280.2626,
            "id": "walker",
            "size": 0.7390192
        },
        {
            "color": "#84c719",
            "label": "batchflow",
            "attributes": {},
            "y": 405.85773,
            "x": -213.34535,
            "id": "batchflow",
            "size": 0.43472436
        },
        {
            "color": "#84c719",
            "label": "path-extra",
            "attributes": {},
            "y": 310.982,
            "x": -367.00104,
            "id": "path-extra",
            "size": 0.43472436
        },
        {
            "color": "#1984c7",
            "label": "cradle",
            "attributes": {},
            "y": 356.7393,
            "x": -42.904198,
            "id": "cradle",
            "size": 2.1996343
        },
        {
            "color": "#194fc7",
            "label": "cli-color",
            "attributes": {},
            "y": -1213.5996,
            "x": 135.87648,
            "id": "cli-color",
            "size": 4.4514165
        },
        {
            "color": "#c719b9",
            "label": "hoek",
            "attributes": {},
            "y": 357.1927,
            "x": 298.65424,
            "id": "hoek",
            "size": 0.8911666
        },
        {
            "color": "#c78419",
            "label": "csso",
            "attributes": {},
            "y": -265.18994,
            "x": 159.92708,
            "id": "csso",
            "size": 0.8607372
        },
        {
            "color": "#c78419",
            "label": "html-minifier",
            "attributes": {},
            "y": 347.3478,
            "x": 106.32629,
            "id": "html-minifier",
            "size": 1.1346025
        },
        {
            "color": "#19b9c7",
            "label": "hashish",
            "attributes": {},
            "y": -983.94257,
            "x": 691.4775,
            "id": "hashish",
            "size": 1.3780384
        },
        {
            "color": "#34c719",
            "label": "htmlparser2",
            "attributes": {},
            "y": 32.03244,
            "x": -571.7144,
            "id": "htmlparser2",
            "size": 1.3780384
        },
        {
            "color": "#c78419",
            "label": "node-zip",
            "attributes": {},
            "y": 322.0001,
            "x": 25.3843,
            "id": "node-zip",
            "size": 0.7390192
        },
        {
            "color": "#9f19c7",
            "label": "batch",
            "attributes": {},
            "y": -315.33505,
            "x": -502.78232,
            "id": "batch",
            "size": 1.8953397
        },
        {
            "color": "#1969c7",
            "label": "emitter-component",
            "attributes": {},
            "y": 217.5223,
            "x": -994.7767,
            "id": "emitter-component",
            "size": 1.3171794
        },
        {
            "color": "#19c7b9",
            "label": "netmask",
            "attributes": {},
            "y": -974.2597,
            "x": 39.66092,
            "id": "netmask",
            "size": 0.43472436
        },
        {
            "color": "#c78419",
            "label": "pkgcloud",
            "attributes": {},
            "y": 435.87173,
            "x": 112.212494,
            "id": "pkgcloud",
            "size": 0.83030766
        },
        {
            "color": "#c76919",
            "label": "eventemitter2",
            "attributes": {},
            "y": 383.04288,
            "x": 1152.9218,
            "id": "eventemitter2",
            "size": 4.3905573
        },
        {
            "color": "#c7194f",
            "label": "lingo",
            "attributes": {},
            "y": -344.86972,
            "x": -1027.0432,
            "id": "lingo",
            "size": 1.165032
        },
        {
            "color": "#b9c719",
            "label": "mailparser",
            "attributes": {},
            "y": 74.95499,
            "x": -381.3953,
            "id": "mailparser",
            "size": 0.7998782
        },
        {
            "color": "#1984c7",
            "label": "moment",
            "attributes": {},
            "y": -792.2076,
            "x": -998.14185,
            "id": "moment",
            "size": 12.180507
        },
        {
            "color": "#8419c7",
            "label": "iconv",
            "attributes": {},
            "y": 92.13313,
            "x": -414.8885,
            "id": "iconv",
            "size": 1.5910448
        },
        {
            "color": "#c719b9",
            "label": "websocket",
            "attributes": {},
            "y": -280.031,
            "x": -68.44273,
            "id": "websocket",
            "size": 1.8344806
        },
        {
            "color": "#c79f19",
            "label": "portfinder",
            "attributes": {},
            "y": -113.6123,
            "x": 371.73843,
            "id": "portfinder",
            "size": 0.92159617
        },
        {
            "color": "#c71919",
            "label": "node-markdown",
            "attributes": {},
            "y": -332.64737,
            "x": 434.20547,
            "id": "node-markdown",
            "size": 1.6823332
        },
        {
            "color": "#c79f19",
            "label": "forever-monitor",
            "attributes": {},
            "y": 626.0845,
            "x": 984.5066,
            "id": "forever-monitor",
            "size": 1.1041731
        },
        {
            "color": "#c7194f",
            "label": "mysql",
            "attributes": {},
            "y": 526.6606,
            "x": -133.69568,
            "id": "mysql",
            "size": 4.8165703
        },
        {
            "color": "#9fc719",
            "label": "passport",
            "attributes": {},
            "y": 1162.1132,
            "x": 529.5607,
            "id": "passport",
            "size": 4.1471214
        },
        {
            "color": "#c78419",
            "label": "jshint",
            "attributes": {},
            "y": -839.91656,
            "x": 533.37573,
            "id": "jshint",
            "size": 3.0212305
        },
        {
            "color": "#c78419",
            "label": "nib",
            "attributes": {},
            "y": -691.36115,
            "x": -655.49725,
            "id": "nib",
            "size": 3.9341152
        },
        {
            "color": "#4f19c7",
            "label": "cssom",
            "attributes": {},
            "y": -490.82297,
            "x": -805.296,
            "id": "cssom",
            "size": 0.95202565
        },
        {
            "color": "#c7b919",
            "label": "grunt-lib-contrib",
            "attributes": {},
            "y": -830.87317,
            "x": -221.20235,
            "id": "grunt-lib-contrib",
            "size": 1.8040513
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-copy",
            "attributes": {},
            "y": 223.77101,
            "x": 57.86038,
            "id": "grunt-contrib-copy",
            "size": 0.76944876
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-stylus",
            "attributes": {},
            "y": -673.43256,
            "x": -653.4811,
            "id": "grunt-contrib-stylus",
            "size": 0.4955833
        },
        {
            "color": "#1984c7",
            "label": "phantom",
            "attributes": {},
            "y": 1001.26575,
            "x": -280.97418,
            "id": "phantom",
            "size": 0.6173013
        },
        {
            "color": "#19c7b9",
            "label": "jslint",
            "attributes": {},
            "y": -4.006271,
            "x": 613.1153,
            "id": "jslint",
            "size": 0.67816025
        },
        {
            "color": "#8419c7",
            "label": "xtend",
            "attributes": {},
            "y": 974.34454,
            "x": 25.975996,
            "id": "xtend",
            "size": 3.2038076
        },
        {
            "color": "#1984c7",
            "label": "bufferstream",
            "attributes": {},
            "y": 1160.7294,
            "x": 152.05467,
            "id": "bufferstream",
            "size": 0.67816025
        },
        {
            "color": "#c78419",
            "label": "browserify",
            "attributes": {},
            "y": 786.3091,
            "x": 195.28586,
            "id": "browserify",
            "size": 5.8816023
        },
        {
            "color": "#c79f19",
            "label": "insert-css",
            "attributes": {},
            "y": 279.7769,
            "x": -6.9432707,
            "id": "insert-css",
            "size": 0.40429485
        },
        {
            "color": "#b9c719",
            "label": "uuid",
            "attributes": {},
            "y": -77.014244,
            "x": -279.67914,
            "id": "uuid",
            "size": 1.0737435
        },
        {
            "color": "#9f19c7",
            "label": "bindings",
            "attributes": {},
            "y": 80.179634,
            "x": -1028.0078,
            "id": "bindings",
            "size": 3.3559546
        },
        {
            "color": "#c71919",
            "label": "argsparser",
            "attributes": {},
            "y": -178.20844,
            "x": -244.5057,
            "id": "argsparser",
            "size": 0.64773077
        },
        {
            "color": "#c719b9",
            "label": "byline",
            "attributes": {},
            "y": -380.787,
            "x": -21.57464,
            "id": "byline",
            "size": 0.67816025
        },
        {
            "color": "#4f19c7",
            "label": "nodeunit",
            "attributes": {},
            "y": -515.95337,
            "x": 278.70786,
            "id": "nodeunit",
            "size": 2.8995125
        },
        {
            "color": "#19b9c7",
            "label": "vine",
            "attributes": {},
            "y": -1349.9265,
            "x": 138.67784,
            "id": "vine",
            "size": 0.70858973
        },
        {
            "color": "#19b9c7",
            "label": "sprintf",
            "attributes": {},
            "y": -107.171104,
            "x": -1031.4116,
            "id": "sprintf",
            "size": 2.929942
        },
        {
            "color": "#19b9c7",
            "label": "tq",
            "attributes": {},
            "y": -1175.0505,
            "x": 101.18756,
            "id": "tq",
            "size": 0.4651538
        },
        {
            "color": "#19c74f",
            "label": "findit",
            "attributes": {},
            "y": -1036.1184,
            "x": 751.62134,
            "id": "findit",
            "size": 3.05166
        },
        {
            "color": "#19b9c7",
            "label": "plugin",
            "attributes": {},
            "y": -1226.2068,
            "x": 268.24854,
            "id": "plugin",
            "size": 0.95202565
        },
        {
            "color": "#19b9c7",
            "label": "crema",
            "attributes": {},
            "y": -1152.8553,
            "x": 114.24345,
            "id": "crema",
            "size": 0.43472436
        },
        {
            "color": "#19b9c7",
            "label": "outcome",
            "attributes": {},
            "y": -1357.6165,
            "x": 158.47685,
            "id": "outcome",
            "size": 1.3476089
        },
        {
            "color": "#19b9c7",
            "label": "comerr",
            "attributes": {},
            "y": -216.2576,
            "x": -258.3082,
            "id": "comerr",
            "size": 0.58687174
        },
        {
            "color": "#b919c7",
            "label": "bean",
            "attributes": {},
            "y": -1213.9034,
            "x": -1086.2054,
            "id": "bean",
            "size": 0.8607372
        },
        {
            "color": "#19b9c7",
            "label": "sk",
            "attributes": {},
            "y": -781.8526,
            "x": 333.07233,
            "id": "sk",
            "size": 0.58687174
        },
        {
            "color": "#19c719",
            "label": "growl",
            "attributes": {},
            "y": -508.24026,
            "x": -921.39386,
            "id": "growl",
            "size": 2.3517818
        },
        {
            "color": "#c78419",
            "label": "stitch",
            "attributes": {},
            "y": -365.59622,
            "x": 27.93561,
            "id": "stitch",
            "size": 0.70858973
        },
        {
            "color": "#c71969",
            "label": "jasmine-node",
            "attributes": {},
            "y": -579.92035,
            "x": 27.825665,
            "id": "jasmine-node",
            "size": 2.108346
        },
        {
            "color": "#c71969",
            "label": "file",
            "attributes": {},
            "y": -1062.3031,
            "x": -77.094055,
            "id": "file",
            "size": 1.0737435
        },
        {
            "color": "#4f19c7",
            "label": "jsdom",
            "attributes": {},
            "y": -263.90924,
            "x": -799.74493,
            "id": "jsdom",
            "size": 9.56357
        },
        {
            "color": "#c71919",
            "label": "inotify",
            "attributes": {},
            "y": 313.49222,
            "x": 89.25136,
            "id": "inotify",
            "size": 0.4651538
        },
        {
            "color": "#9f19c7",
            "label": "superagent",
            "attributes": {},
            "y": 182.74373,
            "x": -907.1791,
            "id": "superagent",
            "size": 5.0904355
        },
        {
            "color": "#19c7b9",
            "label": "marked",
            "attributes": {},
            "y": -871.4397,
            "x": -500.8899,
            "id": "marked",
            "size": 8.224673
        },
        {
            "color": "#19c7b9",
            "label": "highlight",
            "attributes": {},
            "y": -94.81895,
            "x": -209.03227,
            "id": "highlight",
            "size": 0.8607372
        },
        {
            "color": "#c74f19",
            "label": "sugar",
            "attributes": {},
            "y": 226.64883,
            "x": 1280.8156,
            "id": "sugar",
            "size": 2.3517818
        },
        {
            "color": "#c719b9",
            "label": "msgpack",
            "attributes": {},
            "y": 428.69183,
            "x": -51.497612,
            "id": "msgpack",
            "size": 0.67816025
        },
        {
            "color": "#1919c7",
            "label": "chai",
            "attributes": {},
            "y": 174.10605,
            "x": 1250.3047,
            "id": "chai",
            "size": 2.9603715
        },
        {
            "color": "#19c7b9",
            "label": "readdirp",
            "attributes": {},
            "y": -405.0667,
            "x": 915.12866,
            "id": "readdirp",
            "size": 0.95202565
        },
        {
            "color": "#c719b9",
            "label": "ws",
            "attributes": {},
            "y": -317.98154,
            "x": -871.0914,
            "id": "ws",
            "size": 4.5731344
        },
        {
            "color": "#c7194f",
            "label": "node-xmpp",
            "attributes": {},
            "y": 598.0257,
            "x": -410.16193,
            "id": "node-xmpp",
            "size": 1.3780384
        },
        {
            "color": "#c78419",
            "label": "csslint",
            "attributes": {},
            "y": 478.5039,
            "x": -61.05299,
            "id": "csslint",
            "size": 0.7390192
        },
        {
            "color": "#19c784",
            "label": "watchr",
            "attributes": {},
            "y": 655.0502,
            "x": 1623.2988,
            "id": "watchr",
            "size": 2.0779166
        },
        {
            "color": "#19c7b9",
            "label": "open",
            "attributes": {},
            "y": -1175.2716,
            "x": -371.70215,
            "id": "open",
            "size": 2.169205
        },
        {
            "color": "#19b9c7",
            "label": "celeri",
            "attributes": {},
            "y": -1163.5059,
            "x": 178.71414,
            "id": "celeri",
            "size": 0.83030766
        },
        {
            "color": "#19c719",
            "label": "iniparser",
            "attributes": {},
            "y": -339.9005,
            "x": -52.90442,
            "id": "iniparser",
            "size": 0.52601284
        },
        {
            "color": "#69c719",
            "label": "coa",
            "attributes": {},
            "y": -496.67493,
            "x": -374.48096,
            "id": "coa",
            "size": 0.70858973
        },
        {
            "color": "#69c719",
            "label": "ometajs",
            "attributes": {},
            "y": -563.26465,
            "x": -248.37671,
            "id": "ometajs",
            "size": 0.70858973
        },
        {
            "color": "#69c719",
            "label": "q-fs",
            "attributes": {},
            "y": -252.13869,
            "x": -493.3316,
            "id": "q-fs",
            "size": 0.55644226
        },
        {
            "color": "#19c769",
            "label": "estraverse",
            "attributes": {},
            "y": -438.3512,
            "x": 1230.5919,
            "id": "estraverse",
            "size": 0.76944876
        },
        {
            "color": "#19c769",
            "label": "esprima",
            "attributes": {},
            "y": -492.75586,
            "x": 1093.5259,
            "id": "esprima",
            "size": 4.8165703
        },
        {
            "color": "#69c719",
            "label": "vow",
            "attributes": {},
            "y": 274.6161,
            "x": 22.648827,
            "id": "vow",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "cookies",
            "attributes": {},
            "y": 1429.8711,
            "x": -284.74634,
            "id": "cookies",
            "size": 1.5301858
        },
        {
            "color": "#69c719",
            "label": "inherit",
            "attributes": {},
            "y": 182.67122,
            "x": 14.1439,
            "id": "inherit",
            "size": 0.58687174
        },
        {
            "color": "#c78419",
            "label": "dot",
            "attributes": {},
            "y": -150.56572,
            "x": -237.81726,
            "id": "dot",
            "size": 0.67816025
        },
        {
            "color": "#19c7b9",
            "label": "benchmark",
            "attributes": {},
            "y": 497.00113,
            "x": -186.69818,
            "id": "benchmark",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "falafel",
            "attributes": {},
            "y": -291.48453,
            "x": 1044.3159,
            "id": "falafel",
            "size": 1.4997563
        },
        {
            "color": "#19c7b9",
            "label": "cli-table",
            "attributes": {},
            "y": -276.09082,
            "x": 599.47327,
            "id": "cli-table",
            "size": 2.3213525
        },
        {
            "color": "#8419c7",
            "label": "qs",
            "attributes": {},
            "y": 446.33676,
            "x": -440.75952,
            "id": "qs",
            "size": 3.9036858
        },
        {
            "color": "#84c719",
            "label": "idgen",
            "attributes": {},
            "y": 428.3982,
            "x": -268.81287,
            "id": "idgen",
            "size": 0.52601284
        },
        {
            "color": "#c71919",
            "label": "cli",
            "attributes": {},
            "y": -816.1008,
            "x": 467.85532,
            "id": "cli",
            "size": 2.047487
        },
        {
            "color": "#c719b9",
            "label": "bunyan",
            "attributes": {},
            "y": 1165.037,
            "x": 85.06831,
            "id": "bunyan",
            "size": 1.7431923
        },
        {
            "color": "#c71919",
            "label": "cookie",
            "attributes": {},
            "y": 76.30339,
            "x": -946.7451,
            "id": "cookie",
            "size": 1.5910448
        },
        {
            "color": "#c7199f",
            "label": "callsite",
            "attributes": {},
            "y": 201.48732,
            "x": 26.608828,
            "id": "callsite",
            "size": 0.7390192
        },
        {
            "color": "#1969c7",
            "label": "bit-twiddle",
            "attributes": {},
            "y": -1051.561,
            "x": 969.86316,
            "id": "bit-twiddle",
            "size": 0.70858973
        },
        {
            "color": "#c71984",
            "label": "utile",
            "attributes": {},
            "y": 579.9666,
            "x": 723.9766,
            "id": "utile",
            "size": 1.8040513
        },
        {
            "color": "#4f19c7",
            "label": "deep-equal",
            "attributes": {},
            "y": 627.13947,
            "x": 403.1256,
            "id": "deep-equal",
            "size": 0.83030766
        },
        {
            "color": "#c71919",
            "label": "send",
            "attributes": {},
            "y": -25.373653,
            "x": -798.1167,
            "id": "send",
            "size": 2.3822114
        },
        {
            "color": "#c78419",
            "label": "jison",
            "attributes": {},
            "y": -632.0565,
            "x": 1053.5453,
            "id": "jison",
            "size": 0.7390192
        },
        {
            "color": "#c71919",
            "label": "socket.io-client",
            "attributes": {},
            "y": -341.4672,
            "x": -552.156,
            "id": "socket.io-client",
            "size": 3.7819674
        },
        {
            "color": "#19c7b9",
            "label": "resource",
            "attributes": {},
            "y": -41.398632,
            "x": 1071.8018,
            "id": "resource",
            "size": 1.8344806
        },
        {
            "color": "#c7194f",
            "label": "node-expat",
            "attributes": {},
            "y": 788.2994,
            "x": -586.8687,
            "id": "node-expat",
            "size": 1.3476089
        },
        {
            "color": "#c71919",
            "label": "jake",
            "attributes": {},
            "y": -456.03333,
            "x": 963.65735,
            "id": "jake",
            "size": 0.92159617
        },
        {
            "color": "#1934c7",
            "label": "assert",
            "attributes": {},
            "y": 841.56354,
            "x": -892.81085,
            "id": "assert",
            "size": 0.8911666
        },
        {
            "color": "#c7199f",
            "label": "bigint",
            "attributes": {},
            "y": 420.5151,
            "x": -74.42052,
            "id": "bigint",
            "size": 0.40429485
        },
        {
            "color": "#c71919",
            "label": "path",
            "attributes": {},
            "y": -293.70203,
            "x": -306.8733,
            "id": "path",
            "size": 1.3476089
        },
        {
            "color": "#1919c7",
            "label": "detective",
            "attributes": {},
            "y": -324.75464,
            "x": 1175.4331,
            "id": "detective",
            "size": 1.6214744
        },
        {
            "color": "#c7199f",
            "label": "bignum",
            "attributes": {},
            "y": 447.65332,
            "x": -88.192,
            "id": "bignum",
            "size": 0.6173013
        },
        {
            "color": "#c78419",
            "label": "gaze",
            "attributes": {},
            "y": -129.82701,
            "x": -467.96494,
            "id": "gaze",
            "size": 1.1346025
        },
        {
            "color": "#c79f19",
            "label": "istanbul",
            "attributes": {},
            "y": -414.29037,
            "x": 981.35065,
            "id": "istanbul",
            "size": 1.4693269
        },
        {
            "color": "#1919c7",
            "label": "sinon",
            "attributes": {},
            "y": 241.44598,
            "x": 121.80424,
            "id": "sinon",
            "size": 1.7127627
        },
        {
            "color": "#c79f19",
            "label": "tiny-lr",
            "attributes": {},
            "y": 272.46545,
            "x": -702.41003,
            "id": "tiny-lr",
            "size": 0.58687174
        },
        {
            "color": "#19c7b9",
            "label": "argparse",
            "attributes": {},
            "y": -633.0312,
            "x": 336.41046,
            "id": "argparse",
            "size": 1.4388975
        },
        {
            "color": "#194fc7",
            "label": "node.extend",
            "attributes": {},
            "y": 120.20691,
            "x": 287.5265,
            "id": "node.extend",
            "size": 1.5606153
        },
        {
            "color": "#19b9c7",
            "label": "dref",
            "attributes": {},
            "y": -1461.0592,
            "x": 310.44052,
            "id": "dref",
            "size": 0.7390192
        },
        {
            "color": "#19b9c7",
            "label": "toarray",
            "attributes": {},
            "y": -1257.1584,
            "x": 208.80318,
            "id": "toarray",
            "size": 0.55644226
        },
        {
            "color": "#19b9c7",
            "label": "type-component",
            "attributes": {},
            "y": -1413.6371,
            "x": 284.43454,
            "id": "type-component",
            "size": 0.7998782
        },
        {
            "color": "#c78419",
            "label": "java",
            "attributes": {},
            "y": -224.4037,
            "x": -105.301605,
            "id": "java",
            "size": 0.4955833
        },
        {
            "color": "#c78419",
            "label": "walkdir",
            "attributes": {},
            "y": -548.8894,
            "x": 199.97614,
            "id": "walkdir",
            "size": 1.1346025
        },
        {
            "color": "#c78419",
            "label": "haml-coffee",
            "attributes": {},
            "y": -460.67175,
            "x": 300.36,
            "id": "haml-coffee",
            "size": 0.58687174
        },
        {
            "color": "#19c769",
            "label": "prime",
            "attributes": {},
            "y": -170.90903,
            "x": -213.16695,
            "id": "prime",
            "size": 0.92159617
        },
        {
            "color": "#c78419",
            "label": "asyncjs",
            "attributes": {},
            "y": 15.206377,
            "x": 295.61932,
            "id": "asyncjs",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "oauth",
            "attributes": {},
            "y": 1275.2666,
            "x": -218.46474,
            "id": "oauth",
            "size": 5.0295763
        },
        {
            "color": "#c71919",
            "label": "buffertools",
            "attributes": {},
            "y": 1148.7097,
            "x": 164.38617,
            "id": "buffertools",
            "size": 1.1346025
        },
        {
            "color": "#c7199f",
            "label": "binary",
            "attributes": {},
            "y": 684.67883,
            "x": 4.923739,
            "id": "binary",
            "size": 0.83030766
        },
        {
            "color": "#c71984",
            "label": "irc",
            "attributes": {},
            "y": -76.81115,
            "x": -224.82208,
            "id": "irc",
            "size": 1.8040513
        },
        {
            "color": "#c7199f",
            "label": "forever",
            "attributes": {},
            "y": 671.5869,
            "x": 1066.038,
            "id": "forever",
            "size": 1.5910448
        },
        {
            "color": "#c7199f",
            "label": "buffers",
            "attributes": {},
            "y": 735.97046,
            "x": 18.47544,
            "id": "buffers",
            "size": 0.8911666
        },
        {
            "color": "#19b9c7",
            "label": "hooks",
            "attributes": {},
            "y": 409.85138,
            "x": -1169.465,
            "id": "hooks",
            "size": 0.40429485
        },
        {
            "color": "#1984c7",
            "label": "num",
            "attributes": {},
            "y": 146.5466,
            "x": -386.24503,
            "id": "num",
            "size": 0.4955833
        },
        {
            "color": "#c79f19",
            "label": "shelljs",
            "attributes": {},
            "y": -900.85004,
            "x": 499.16705,
            "id": "shelljs",
            "size": 3.234237
        },
        {
            "color": "#c71919",
            "label": "serialport",
            "attributes": {},
            "y": 89.454384,
            "x": -131.34398,
            "id": "serialport",
            "size": 1.9561987
        },
        {
            "color": "#c78419",
            "label": "pegjs",
            "attributes": {},
            "y": -289.04016,
            "x": 164.06274,
            "id": "pegjs",
            "size": 1.28675
        },
        {
            "color": "#c71919",
            "label": "connect-redis",
            "attributes": {},
            "y": 0.25086692,
            "x": -927.49084,
            "id": "connect-redis",
            "size": 1.8649102
        },
        {
            "color": "#c78419",
            "label": "optparse",
            "attributes": {},
            "y": -843.711,
            "x": -301.50488,
            "id": "optparse",
            "size": 1.0128845
        },
        {
            "color": "#19b9c7",
            "label": "dnode",
            "attributes": {},
            "y": 1043.8707,
            "x": -152.54582,
            "id": "dnode",
            "size": 2.1387753
        },
        {
            "color": "#19c7b9",
            "label": "highlight.js",
            "attributes": {},
            "y": -923.82654,
            "x": -452.9307,
            "id": "highlight.js",
            "size": 2.4126408
        },
        {
            "color": "#c71984",
            "label": "plates",
            "attributes": {},
            "y": -92.00068,
            "x": 199.20425,
            "id": "plates",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "after",
            "attributes": {},
            "y": -525.1652,
            "x": 640.8966,
            "id": "after",
            "size": 0.55644226
        },
        {
            "color": "#c71984",
            "label": "union",
            "attributes": {},
            "y": 779.5833,
            "x": 128.22095,
            "id": "union",
            "size": 1.1041731
        },
        {
            "color": "#c71984",
            "label": "director",
            "attributes": {},
            "y": 868.4869,
            "x": 851.6432,
            "id": "director",
            "size": 1.0128845
        },
        {
            "color": "#8419c7",
            "label": "crypto",
            "attributes": {},
            "y": 315.04626,
            "x": -2.5743425,
            "id": "crypto",
            "size": 1.8649102
        },
        {
            "color": "#9fc719",
            "label": "passport-local",
            "attributes": {},
            "y": 1117.0792,
            "x": 606.08325,
            "id": "passport-local",
            "size": 1.3171794
        },
        {
            "color": "#19c74f",
            "label": "xmldom",
            "attributes": {},
            "y": 555.979,
            "x": -786.6827,
            "id": "xmldom",
            "size": 1.986628
        },
        {
            "color": "#19c7b9",
            "label": "markdown",
            "attributes": {},
            "y": 14.575827,
            "x": 610.2677,
            "id": "markdown",
            "size": 2.230064
        },
        {
            "color": "#b9c719",
            "label": "ent",
            "attributes": {},
            "y": 533.3348,
            "x": 172.2999,
            "id": "ent",
            "size": 1.0737435
        },
        {
            "color": "#1919c7",
            "label": "node-gd",
            "attributes": {},
            "y": -254.01602,
            "x": -60.33067,
            "id": "node-gd",
            "size": 0.40429485
        },
        {
            "color": "#19c719",
            "label": "microtime",
            "attributes": {},
            "y": 98.89298,
            "x": -1054.5382,
            "id": "microtime",
            "size": 1.1954615
        },
        {
            "color": "#c7194f",
            "label": "crc",
            "attributes": {},
            "y": 217.0216,
            "x": 132.25229,
            "id": "crc",
            "size": 0.76944876
        },
        {
            "color": "#19c7b9",
            "label": "rss",
            "attributes": {},
            "y": 76.558815,
            "x": -446.1457,
            "id": "rss",
            "size": 0.7390192
        },
        {
            "color": "#c71919",
            "label": "connect-mongodb",
            "attributes": {},
            "y": 425.84332,
            "x": -1039.9854,
            "id": "connect-mongodb",
            "size": 0.58687174
        },
        {
            "color": "#c71919",
            "label": "express-partials",
            "attributes": {},
            "y": -273.29303,
            "x": -98.9056,
            "id": "express-partials",
            "size": 0.43472436
        },
        {
            "color": "#9fc719",
            "label": "connect-flash",
            "attributes": {},
            "y": 207.55605,
            "x": -392.5633,
            "id": "connect-flash",
            "size": 0.95202565
        },
        {
            "color": "#19b9c7",
            "label": "sift",
            "attributes": {},
            "y": -1229.2162,
            "x": 203.28523,
            "id": "sift",
            "size": 0.76944876
        },
        {
            "color": "#19c719",
            "label": "charm",
            "attributes": {},
            "y": -855.05255,
            "x": 684.35016,
            "id": "charm",
            "size": 1.1346025
        },
        {
            "color": "#c71919",
            "label": "showdown",
            "attributes": {},
            "y": -355.61545,
            "x": 158.14978,
            "id": "showdown",
            "size": 0.8607372
        },
        {
            "color": "#1984c7",
            "label": "connect-form",
            "attributes": {},
            "y": 620.0338,
            "x": -932.84155,
            "id": "connect-form",
            "size": 0.43472436
        },
        {
            "color": "#c71919",
            "label": "yaml",
            "attributes": {},
            "y": -317.5982,
            "x": -279.82288,
            "id": "yaml",
            "size": 1.4084679
        },
        {
            "color": "#c78419",
            "label": "zombie",
            "attributes": {},
            "y": -95.91513,
            "x": -656.0366,
            "id": "zombie",
            "size": 1.4388975
        },
        {
            "color": "#c78419",
            "label": "jugglingdb",
            "attributes": {},
            "y": -540.2533,
            "x": 1273.7468,
            "id": "jugglingdb",
            "size": 0.6173013
        },
        {
            "color": "#8419c7",
            "label": "date-utils",
            "attributes": {},
            "y": -571.8109,
            "x": -1065.7231,
            "id": "date-utils",
            "size": 0.98245513
        },
        {
            "color": "#c7b919",
            "label": "regexp-quote",
            "attributes": {},
            "y": -193.41238,
            "x": -275.24255,
            "id": "regexp-quote",
            "size": 0.43472436
        },
        {
            "color": "#c719b9",
            "label": "hiredis",
            "attributes": {},
            "y": 115.843506,
            "x": -1046.4277,
            "id": "hiredis",
            "size": 4.23841
        },
        {
            "color": "#c71919",
            "label": "swig",
            "attributes": {},
            "y": -807.8819,
            "x": -189.87314,
            "id": "swig",
            "size": 1.6214744
        },
        {
            "color": "#4f19c7",
            "label": "xmlhttprequest",
            "attributes": {},
            "y": -388.15134,
            "x": -831.295,
            "id": "xmlhttprequest",
            "size": 1.8040513
        },
        {
            "color": "#19c7b9",
            "label": "keypress",
            "attributes": {},
            "y": -1097.4784,
            "x": -158.4356,
            "id": "keypress",
            "size": 1.3171794
        },
        {
            "color": "#b9c719",
            "label": "formidable",
            "attributes": {},
            "y": 600.273,
            "x": -921.4781,
            "id": "formidable",
            "size": 3.4168139
        },
        {
            "color": "#19c719",
            "label": "node-static",
            "attributes": {},
            "y": -10.201102,
            "x": 354.93808,
            "id": "node-static",
            "size": 2.929942
        },
        {
            "color": "#1984c7",
            "label": "imagemagick",
            "attributes": {},
            "y": 215.64548,
            "x": -360.4117,
            "id": "imagemagick",
            "size": 1.6823332
        },
        {
            "color": "#4f19c7",
            "label": "bootstrap",
            "attributes": {},
            "y": -731.5939,
            "x": -528.3612,
            "id": "bootstrap",
            "size": 0.43472436
        },
        {
            "color": "#1984c7",
            "label": "nconf",
            "attributes": {},
            "y": 511.7138,
            "x": 915.0162,
            "id": "nconf",
            "size": 4.3905573
        },
        {
            "color": "#4f19c7",
            "label": "htmlparser",
            "attributes": {},
            "y": -575.9647,
            "x": -136.95193,
            "id": "htmlparser",
            "size": 2.2909229
        },
        {
            "color": "#19c74f",
            "label": "seq",
            "attributes": {},
            "y": -1037.4547,
            "x": 734.58215,
            "id": "seq",
            "size": 1.7736217
        },
        {
            "color": "#b9c719",
            "label": "azure",
            "attributes": {},
            "y": -44.75286,
            "x": -406.81332,
            "id": "azure",
            "size": 1.0128845
        },
        {
            "color": "#19c769",
            "label": "resolve",
            "attributes": {},
            "y": -923.4041,
            "x": 695.9144,
            "id": "resolve",
            "size": 1.6214744
        },
        {
            "color": "#c7194f",
            "label": "generic-pool",
            "attributes": {},
            "y": -363.04434,
            "x": -1126.6726,
            "id": "generic-pool",
            "size": 1.5301858
        },
        {
            "color": "#c7194f",
            "label": "pg",
            "attributes": {},
            "y": -251.6094,
            "x": -1194.4589,
            "id": "pg",
            "size": 3.2038076
        },
        {
            "color": "#c71919",
            "label": "jqtpl",
            "attributes": {},
            "y": -843.789,
            "x": -155.0798,
            "id": "jqtpl",
            "size": 0.67816025
        },
        {
            "color": "#c79f19",
            "label": "npm",
            "attributes": {},
            "y": -86.14667,
            "x": 1400.5574,
            "id": "npm",
            "size": 5.0904355
        },
        {
            "color": "#c79f19",
            "label": "ncp",
            "attributes": {},
            "y": 112.65727,
            "x": 718.81494,
            "id": "ncp",
            "size": 2.7169356
        },
        {
            "color": "#84c719",
            "label": "promised-io",
            "attributes": {},
            "y": 29.489025,
            "x": -423.36993,
            "id": "promised-io",
            "size": 1.1346025
        },
        {
            "color": "#c719b9",
            "label": "log",
            "attributes": {},
            "y": -523.3549,
            "x": -19.44641,
            "id": "log",
            "size": 1.1041731
        },
        {
            "color": "#c719b9",
            "label": "zmq",
            "attributes": {},
            "y": 300.038,
            "x": -294.43927,
            "id": "zmq",
            "size": 1.1346025
        },
        {
            "color": "#19c719",
            "label": "nomnom",
            "attributes": {},
            "y": -597.822,
            "x": 531.09247,
            "id": "nomnom",
            "size": 2.3213525
        },
        {
            "color": "#1934c7",
            "label": "JSV",
            "attributes": {},
            "y": -247.65616,
            "x": -240.78343,
            "id": "JSV",
            "size": 0.7390192
        },
        {
            "color": "#9fc719",
            "label": "passport-oauth",
            "attributes": {},
            "y": 1229.6758,
            "x": 527.8946,
            "id": "passport-oauth",
            "size": 3.6602497
        },
        {
            "color": "#9fc719",
            "label": "passport-twitter",
            "attributes": {},
            "y": 1171.3842,
            "x": 599.1357,
            "id": "passport-twitter",
            "size": 0.52601284
        },
        {
            "color": "#c79f19",
            "label": "methods",
            "attributes": {},
            "y": -49.73068,
            "x": -1083.3983,
            "id": "methods",
            "size": 1.6823332
        },
        {
            "color": "#c719b9",
            "label": "hat",
            "attributes": {},
            "y": 428.36014,
            "x": -233.57118,
            "id": "hat",
            "size": 1.0737435
        },
        {
            "color": "#c71919",
            "label": "mongoskin",
            "attributes": {},
            "y": 548.74744,
            "x": -1074.1718,
            "id": "mongoskin",
            "size": 1.28675
        },
        {
            "color": "#19b9c7",
            "label": "traverse",
            "attributes": {},
            "y": -869.6334,
            "x": 607.4505,
            "id": "traverse",
            "size": 2.169205
        },
        {
            "color": "#b919c7",
            "label": "bonzo",
            "attributes": {},
            "y": -1230.6212,
            "x": -1068.8632,
            "id": "bonzo",
            "size": 0.76944876
        },
        {
            "color": "#c71919",
            "label": "emailjs",
            "attributes": {},
            "y": -827.9733,
            "x": -1057.115,
            "id": "emailjs",
            "size": 0.98245513
        },
        {
            "color": "#9fc719",
            "label": "connect-mongo",
            "attributes": {},
            "y": 542.9935,
            "x": -1111.1758,
            "id": "connect-mongo",
            "size": 0.98245513
        },
        {
            "color": "#9fc719",
            "label": "bcrypt",
            "attributes": {},
            "y": 74.34341,
            "x": -1062.3085,
            "id": "bcrypt",
            "size": 2.1387753
        },
        {
            "color": "#c71919",
            "label": "ntwitter",
            "attributes": {},
            "y": 1392.1279,
            "x": -288.68558,
            "id": "ntwitter",
            "size": 0.98245513
        },
        {
            "color": "#9f19c7",
            "label": "juice",
            "attributes": {},
            "y": -363.1132,
            "x": -774.99554,
            "id": "juice",
            "size": 0.70858973
        },
        {
            "color": "#199fc7",
            "label": "pause-stream",
            "attributes": {},
            "y": 747.02313,
            "x": 325.80133,
            "id": "pause-stream",
            "size": 0.76944876
        },
        {
            "color": "#19c7b9",
            "label": "aug",
            "attributes": {},
            "y": 48.178226,
            "x": 299.8556,
            "id": "aug",
            "size": 0.55644226
        },
        {
            "color": "#c7194f",
            "label": "sequelize",
            "attributes": {},
            "y": -618.1904,
            "x": -736.92706,
            "id": "sequelize",
            "size": 1.4693269
        },
        {
            "color": "#c79f19",
            "label": "tar.gz",
            "attributes": {},
            "y": -348.83762,
            "x": 219.78055,
            "id": "tar.gz",
            "size": 0.4955833
        },
        {
            "color": "#19c7b9",
            "label": "progress",
            "attributes": {},
            "y": 398.53415,
            "x": -321.36157,
            "id": "progress",
            "size": 1.4997563
        },
        {
            "color": "#c78419",
            "label": "jqueryify",
            "attributes": {},
            "y": -282.94342,
            "x": -273.135,
            "id": "jqueryify",
            "size": 0.52601284
        },
        {
            "color": "#19c719",
            "label": "prettyjson",
            "attributes": {},
            "y": -330.08105,
            "x": 677.47784,
            "id": "prettyjson",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "bops",
            "attributes": {},
            "y": 1038.1771,
            "x": -594.73846,
            "id": "bops",
            "size": 0.92159617
        },
        {
            "color": "#c71919",
            "label": "string",
            "attributes": {},
            "y": 282.6386,
            "x": 140.15605,
            "id": "string",
            "size": 1.9561987
        },
        {
            "color": "#19c74f",
            "label": "acorn",
            "attributes": {},
            "y": -244.40276,
            "x": 44.10389,
            "id": "acorn",
            "size": 0.52601284
        },
        {
            "color": "#19c769",
            "label": "escodegen",
            "attributes": {},
            "y": -395.20676,
            "x": 1190.5619,
            "id": "escodegen",
            "size": 2.4734998
        },
        {
            "color": "#c71969",
            "label": "ssh2",
            "attributes": {},
            "y": -344.42947,
            "x": -37.119053,
            "id": "ssh2",
            "size": 1.043314
        },
        {
            "color": "#19c74f",
            "label": "url",
            "attributes": {},
            "y": 999.7216,
            "x": 756.65375,
            "id": "url",
            "size": 1.2563205
        },
        {
            "color": "#c7194f",
            "label": "ltx",
            "attributes": {},
            "y": 729.8443,
            "x": -564.28973,
            "id": "ltx",
            "size": 1.043314
        },
        {
            "color": "#b9c719",
            "label": "util",
            "attributes": {},
            "y": 835.1216,
            "x": -901.55054,
            "id": "util",
            "size": 1.1041731
        },
        {
            "color": "#b9c719",
            "label": "events",
            "attributes": {},
            "y": 244.31078,
            "x": 183.56725,
            "id": "events",
            "size": 0.52601284
        },
        {
            "color": "#c79f19",
            "label": "bouncy",
            "attributes": {},
            "y": 442.78336,
            "x": 465.8834,
            "id": "bouncy",
            "size": 0.76944876
        },
        {
            "color": "#19c719",
            "label": "mdns",
            "attributes": {},
            "y": -95.6844,
            "x": -180.63136,
            "id": "mdns",
            "size": 0.6173013
        },
        {
            "color": "#1969c7",
            "label": "simplicial-complex",
            "attributes": {},
            "y": -1043.0298,
            "x": 952.3011,
            "id": "simplicial-complex",
            "size": 0.4651538
        },
        {
            "color": "#1984c7",
            "label": "tmp",
            "attributes": {},
            "y": 86.25464,
            "x": 981.84015,
            "id": "tmp",
            "size": 1.1041731
        },
        {
            "color": "#c79f19",
            "label": "bower",
            "attributes": {},
            "y": -25.807001,
            "x": 950.3085,
            "id": "bower",
            "size": 2.3517818
        },
        {
            "color": "#19c719",
            "label": "rc",
            "attributes": {},
            "y": 288.68192,
            "x": 964.8844,
            "id": "rc",
            "size": 0.7998782
        },
        {
            "color": "#c79f19",
            "label": "unzip",
            "attributes": {},
            "y": 468.33945,
            "x": 43.956604,
            "id": "unzip",
            "size": 1.4084679
        },
        {
            "color": "#c71919",
            "label": "buffer-crc32",
            "attributes": {},
            "y": 34.657063,
            "x": -959.97186,
            "id": "buffer-crc32",
            "size": 0.70858973
        },
        {
            "color": "#c71919",
            "label": "fresh",
            "attributes": {},
            "y": -176.22559,
            "x": -847.5239,
            "id": "fresh",
            "size": 0.55644226
        },
        {
            "color": "#9f19c7",
            "label": "scaffolder",
            "attributes": {},
            "y": -156.31787,
            "x": 39.511776,
            "id": "scaffolder",
            "size": 0.64773077
        },
        {
            "color": "#9f19c7",
            "label": "memory-cache",
            "attributes": {},
            "y": -189.8613,
            "x": -303.6808,
            "id": "memory-cache",
            "size": 0.4651538
        },
        {
            "color": "#8419c7",
            "label": "restler",
            "attributes": {},
            "y": 206.90912,
            "x": 214.60414,
            "id": "restler",
            "size": 2.3213525
        },
        {
            "color": "#1934c7",
            "label": "stream-buffers",
            "attributes": {},
            "y": 382.2567,
            "x": -296.40576,
            "id": "stream-buffers",
            "size": 0.4955833
        },
        {
            "color": "#19c719",
            "label": "hook.io",
            "attributes": {},
            "y": 469.00113,
            "x": 631.8956,
            "id": "hook.io",
            "size": 2.7169356
        },
        {
            "color": "#c71969",
            "label": "node-promise",
            "attributes": {},
            "y": 171.45761,
            "x": -338.04773,
            "id": "node-promise",
            "size": 0.70858973
        },
        {
            "color": "#c71919",
            "label": "pty.js",
            "attributes": {},
            "y": 413.48465,
            "x": -96.42841,
            "id": "pty.js",
            "size": 0.43472436
        },
        {
            "color": "#c76919",
            "label": "fs.extra",
            "attributes": {},
            "y": -372.29422,
            "x": 386.45148,
            "id": "fs.extra",
            "size": 1.165032
        },
        {
            "color": "#c71919",
            "label": "now",
            "attributes": {},
            "y": 172.7239,
            "x": -784.44946,
            "id": "now",
            "size": 0.98245513
        },
        {
            "color": "#c78419",
            "label": "ansi-color",
            "attributes": {},
            "y": -602.7042,
            "x": -1037.8462,
            "id": "ansi-color",
            "size": 1.0737435
        },
        {
            "color": "#1969c7",
            "label": "brfs",
            "attributes": {},
            "y": 1.9099157,
            "x": 882.43463,
            "id": "brfs",
            "size": 0.67816025
        },
        {
            "color": "#19c74f",
            "label": "bufferjs",
            "attributes": {},
            "y": -852.70483,
            "x": -1094.3876,
            "id": "bufferjs",
            "size": 0.98245513
        },
        {
            "color": "#3419c7",
            "label": "mongojs",
            "attributes": {},
            "y": 527.018,
            "x": -839.6172,
            "id": "mongojs",
            "size": 1.1346025
        },
        {
            "color": "#8419c7",
            "label": "feedparser",
            "attributes": {},
            "y": 497.93576,
            "x": -429.6493,
            "id": "feedparser",
            "size": 0.98245513
        },
        {
            "color": "#c71919",
            "label": "connect-xcors",
            "attributes": {},
            "y": 437.05307,
            "x": -203.66441,
            "id": "connect-xcors",
            "size": 0.40429485
        },
        {
            "color": "#19b9c7",
            "label": "broadway",
            "attributes": {},
            "y": 683.59796,
            "x": 1014.90295,
            "id": "broadway",
            "size": 0.64773077
        },
        {
            "color": "#c719b9",
            "label": "restify",
            "attributes": {},
            "y": 937.7202,
            "x": -84.80429,
            "id": "restify",
            "size": 2.564788
        },
        {
            "color": "#c79f19",
            "label": "cliff",
            "attributes": {},
            "y": 465.76242,
            "x": 1005.90594,
            "id": "cliff",
            "size": 0.95202565
        },
        {
            "color": "#199fc7",
            "label": "concat-stream",
            "attributes": {},
            "y": 804.2095,
            "x": -39.16583,
            "id": "concat-stream",
            "size": 1.5910448
        },
        {
            "color": "#69c719",
            "label": "docopt",
            "attributes": {},
            "y": 185.8025,
            "x": 237.28787,
            "id": "docopt",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "JSONStream",
            "attributes": {},
            "y": 726.4061,
            "x": 285.7015,
            "id": "JSONStream",
            "size": 1.9561987
        },
        {
            "color": "#19c7b9",
            "label": "merge",
            "attributes": {},
            "y": 247.26161,
            "x": 1.9699359,
            "id": "merge",
            "size": 0.43472436
        },
        {
            "color": "#19c719",
            "label": "plist",
            "attributes": {},
            "y": 534.6398,
            "x": -769.35736,
            "id": "plist",
            "size": 0.7390192
        },
        {
            "color": "#c71969",
            "label": "natural",
            "attributes": {},
            "y": -906.51306,
            "x": -159.15141,
            "id": "natural",
            "size": 0.7998782
        },
        {
            "color": "#9fc719",
            "label": "cjson",
            "attributes": {},
            "y": -678.4876,
            "x": 1057.1864,
            "id": "cjson",
            "size": 0.55644226
        },
        {
            "color": "#c78419",
            "label": "commondir",
            "attributes": {},
            "y": 465.1034,
            "x": -184.05745,
            "id": "commondir",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "convert-source-map",
            "attributes": {},
            "y": 402.94788,
            "x": -249.03694,
            "id": "convert-source-map",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "global",
            "attributes": {},
            "y": 729.27844,
            "x": -729.46423,
            "id": "global",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "map-stream",
            "attributes": {},
            "y": 929.72076,
            "x": 303.13293,
            "id": "map-stream",
            "size": 0.7998782
        },
        {
            "color": "#1984c7",
            "label": "ecstatic",
            "attributes": {},
            "y": 315.07608,
            "x": 215.21909,
            "id": "ecstatic",
            "size": 1.5301858
        },
        {
            "color": "#199fc7",
            "label": "process",
            "attributes": {},
            "y": 712.41925,
            "x": -716.8126,
            "id": "process",
            "size": 0.55644226
        },
        {
            "color": "#9f19c7",
            "label": "ms",
            "attributes": {},
            "y": 124.84042,
            "x": -896.667,
            "id": "ms",
            "size": 1.165032
        },
        {
            "color": "#c71919",
            "label": "useragent",
            "attributes": {},
            "y": 67.39527,
            "x": 738.78033,
            "id": "useragent",
            "size": 1.1346025
        },
        {
            "color": "#c71919",
            "label": "colorful",
            "attributes": {},
            "y": -427.3014,
            "x": -301.80933,
            "id": "colorful",
            "size": 0.67816025
        },
        {
            "color": "#c79f19",
            "label": "rmdir",
            "attributes": {},
            "y": 473.40564,
            "x": -211.67924,
            "id": "rmdir",
            "size": 0.6173013
        },
        {
            "color": "#c78419",
            "label": "snockets",
            "attributes": {},
            "y": -572.307,
            "x": -55.683994,
            "id": "snockets",
            "size": 1.0128845
        },
        {
            "color": "#4f19c7",
            "label": "soupselect",
            "attributes": {},
            "y": -568.26624,
            "x": 82.975624,
            "id": "soupselect",
            "size": 0.6173013
        },
        {
            "color": "#c78419",
            "label": "mailer",
            "attributes": {},
            "y": -432.30478,
            "x": 783.54236,
            "id": "mailer",
            "size": 0.70858973
        },
        {
            "color": "#3419c7",
            "label": "bson",
            "attributes": {},
            "y": 578.06537,
            "x": -1087.7448,
            "id": "bson",
            "size": 0.64773077
        },
        {
            "color": "#199fc7",
            "label": "keygrip",
            "attributes": {},
            "y": 1415.7012,
            "x": -306.24265,
            "id": "keygrip",
            "size": 0.67816025
        },
        {
            "color": "#1919c7",
            "label": "fibers",
            "attributes": {},
            "y": 221.70279,
            "x": 1370.3695,
            "id": "fibers",
            "size": 1.5606153
        },
        {
            "color": "#c71919",
            "label": "archiver",
            "attributes": {},
            "y": 507.19348,
            "x": -561.5876,
            "id": "archiver",
            "size": 0.76944876
        },
        {
            "color": "#c71969",
            "label": "aws2js",
            "attributes": {},
            "y": 67.3963,
            "x": -71.76326,
            "id": "aws2js",
            "size": 0.7998782
        },
        {
            "color": "#9f19c7",
            "label": "websocket.io",
            "attributes": {},
            "y": -217.81973,
            "x": -922.6484,
            "id": "websocket.io",
            "size": 0.4955833
        },
        {
            "color": "#c7194f",
            "label": "node-stringprep",
            "attributes": {},
            "y": -243.02711,
            "x": 130.45053,
            "id": "node-stringprep",
            "size": 0.4651538
        },
        {
            "color": "#19c79f",
            "label": "reducers",
            "attributes": {},
            "y": -502.97894,
            "x": -1274.6791,
            "id": "reducers",
            "size": 0.58687174
        },
        {
            "color": "#19c79f",
            "label": "reducible",
            "attributes": {},
            "y": -515.39526,
            "x": -1286.8624,
            "id": "reducible",
            "size": 0.70858973
        },
        {
            "color": "#19c769",
            "label": "coffee-script-redux",
            "attributes": {},
            "y": -426.9769,
            "x": 1172.5735,
            "id": "coffee-script-redux",
            "size": 0.58687174
        },
        {
            "color": "#c78419",
            "label": "source-map",
            "attributes": {},
            "y": -401.11676,
            "x": 1097.5082,
            "id": "source-map",
            "size": 1.5606153
        },
        {
            "color": "#c78419",
            "label": "cssmin",
            "attributes": {},
            "y": -547.905,
            "x": -586.3544,
            "id": "cssmin",
            "size": 0.4651538
        },
        {
            "color": "#19b9c7",
            "label": "stack-trace",
            "attributes": {},
            "y": 752.4155,
            "x": 786.0242,
            "id": "stack-trace",
            "size": 1.043314
        },
        {
            "color": "#19b9c7",
            "label": "logmagic",
            "attributes": {},
            "y": -117.18427,
            "x": -215.80826,
            "id": "logmagic",
            "size": 0.43472436
        },
        {
            "color": "#9f19c7",
            "label": "string-to-js",
            "attributes": {},
            "y": 364.86655,
            "x": 76.84316,
            "id": "string-to-js",
            "size": 0.40429485
        },
        {
            "color": "#c78419",
            "label": "uglifycss",
            "attributes": {},
            "y": -300.3197,
            "x": -238.5077,
            "id": "uglifycss",
            "size": 0.67816025
        },
        {
            "color": "#19c74f",
            "label": "passerror",
            "attributes": {},
            "y": 369.9193,
            "x": -258.02805,
            "id": "passerror",
            "size": 0.40429485
        },
        {
            "color": "#19c74f",
            "label": "time",
            "attributes": {},
            "y": 1.9313185,
            "x": -998.3049,
            "id": "time",
            "size": 0.55644226
        },
        {
            "color": "#c78419",
            "label": "coco",
            "attributes": {},
            "y": 243.6456,
            "x": 25.135742,
            "id": "coco",
            "size": 0.40429485
        },
        {
            "color": "#19b9c7",
            "label": "eyes",
            "attributes": {},
            "y": 484.3233,
            "x": 1062.8107,
            "id": "eyes",
            "size": 2.564788
        },
        {
            "color": "#19c784",
            "label": "cson",
            "attributes": {},
            "y": -1017.48755,
            "x": 8.207783,
            "id": "cson",
            "size": 0.4955833
        },
        {
            "color": "#c71984",
            "label": "resourceful",
            "attributes": {},
            "y": 617.45764,
            "x": 230.89415,
            "id": "resourceful",
            "size": 0.70858973
        },
        {
            "color": "#194fc7",
            "label": "execSync",
            "attributes": {},
            "y": -35.15042,
            "x": -1274.4426,
            "id": "execSync",
            "size": 0.76944876
        },
        {
            "color": "#c78419",
            "label": "loader-utils",
            "attributes": {},
            "y": -1141.6609,
            "x": 569.31177,
            "id": "loader-utils",
            "size": 0.58687174
        },
        {
            "color": "#c719b9",
            "label": "lazy",
            "attributes": {},
            "y": 565.9527,
            "x": 1158.8604,
            "id": "lazy",
            "size": 1.2563205
        },
        {
            "color": "#34c719",
            "label": "assert-plus",
            "attributes": {},
            "y": 1075.4281,
            "x": 86.17554,
            "id": "assert-plus",
            "size": 1.0737435
        },
        {
            "color": "#c719b9",
            "label": "node-int64",
            "attributes": {},
            "y": 321.1519,
            "x": 123.714005,
            "id": "node-int64",
            "size": 0.40429485
        },
        {
            "color": "#1919c7",
            "label": "wd",
            "attributes": {},
            "y": -229.05304,
            "x": -143.04478,
            "id": "wd",
            "size": 1.3171794
        },
        {
            "color": "#34c719",
            "label": "dtrace-provider",
            "attributes": {},
            "y": 1149.9846,
            "x": 67.68434,
            "id": "dtrace-provider",
            "size": 0.4651538
        },
        {
            "color": "#1919c7",
            "label": "buster-core",
            "attributes": {},
            "y": 174.64687,
            "x": -2.8802125,
            "id": "buster-core",
            "size": 0.76944876
        },
        {
            "color": "#c78419",
            "label": "iconv-lite",
            "attributes": {},
            "y": 252.77287,
            "x": -305.2421,
            "id": "iconv-lite",
            "size": 2.169205
        },
        {
            "color": "#c78419",
            "label": "fs-watch-tree",
            "attributes": {},
            "y": -805.3652,
            "x": -863.2866,
            "id": "fs-watch-tree",
            "size": 0.43472436
        },
        {
            "color": "#c719b9",
            "label": "cookiejar",
            "attributes": {},
            "y": 543.63135,
            "x": -885.83795,
            "id": "cookiejar",
            "size": 0.43472436
        },
        {
            "color": "#19c7b9",
            "label": "glob-whatev",
            "attributes": {},
            "y": -364.26727,
            "x": 925.2539,
            "id": "glob-whatev",
            "size": 0.58687174
        },
        {
            "color": "#c719b9",
            "label": "hapi",
            "attributes": {},
            "y": 288.86652,
            "x": 322.17715,
            "id": "hapi",
            "size": 0.8607372
        },
        {
            "color": "#c79f19",
            "label": "humanize",
            "attributes": {},
            "y": -237.40352,
            "x": 9.4212,
            "id": "humanize",
            "size": 0.43472436
        },
        {
            "color": "#19c719",
            "label": "pretty-data",
            "attributes": {},
            "y": 520.63293,
            "x": -202.25743,
            "id": "pretty-data",
            "size": 0.4955833
        },
        {
            "color": "#9f19c7",
            "label": "printf",
            "attributes": {},
            "y": -842.82385,
            "x": 321.60583,
            "id": "printf",
            "size": 0.52601284
        },
        {
            "color": "#1934c7",
            "label": "fairmont",
            "attributes": {},
            "y": -192.92662,
            "x": -29.472069,
            "id": "fairmont",
            "size": 0.43472436
        },
        {
            "color": "#c7b919",
            "label": "typescript",
            "attributes": {},
            "y": 451.12564,
            "x": -113.66281,
            "id": "typescript",
            "size": 0.58687174
        },
        {
            "color": "#19c7b9",
            "label": "chokidar",
            "attributes": {},
            "y": -143.56265,
            "x": -320.56717,
            "id": "chokidar",
            "size": 2.169205
        },
        {
            "color": "#c71984",
            "label": "node_hash",
            "attributes": {},
            "y": -126.50663,
            "x": -151.39897,
            "id": "node_hash",
            "size": 0.4955833
        },
        {
            "color": "#b9c719",
            "label": "imap",
            "attributes": {},
            "y": 155.15096,
            "x": -360.41003,
            "id": "imap",
            "size": 0.6173013
        },
        {
            "color": "#9fc719",
            "label": "password-hash",
            "attributes": {},
            "y": -632.2503,
            "x": 94.21731,
            "id": "password-hash",
            "size": 0.40429485
        },
        {
            "color": "#c78419",
            "label": "coffeecup",
            "attributes": {},
            "y": -872.26465,
            "x": -216.88039,
            "id": "coffeecup",
            "size": 0.7390192
        },
        {
            "color": "#4fc719",
            "label": "libprotein",
            "attributes": {},
            "y": -91.98003,
            "x": -253.22894,
            "id": "libprotein",
            "size": 0.4651538
        },
        {
            "color": "#19c7b9",
            "label": "js-yaml",
            "attributes": {},
            "y": -631.6599,
            "x": 761.8784,
            "id": "js-yaml",
            "size": 5.2121534
        },
        {
            "color": "#c71919",
            "label": "dustjs-linkedin",
            "attributes": {},
            "y": -43.070652,
            "x": 271.35666,
            "id": "dustjs-linkedin",
            "size": 1.6519039
        },
        {
            "color": "#1984c7",
            "label": "deep-extend",
            "attributes": {},
            "y": 317.19928,
            "x": 976.4367,
            "id": "deep-extend",
            "size": 0.58687174
        },
        {
            "color": "#1969c7",
            "label": "jquery-component",
            "attributes": {},
            "y": 406.12448,
            "x": -189.71065,
            "id": "jquery-component",
            "size": 0.4955833
        },
        {
            "color": "#b919c7",
            "label": "jeesh",
            "attributes": {},
            "y": -1262.0615,
            "x": -1080.7123,
            "id": "jeesh",
            "size": 0.52601284
        },
        {
            "color": "#c71919",
            "label": "everyauth",
            "attributes": {},
            "y": 365.4934,
            "x": -683.33185,
            "id": "everyauth",
            "size": 0.7998782
        },
        {
            "color": "#19c719",
            "label": "node-xml",
            "attributes": {},
            "y": -713.54456,
            "x": -311.38135,
            "id": "node-xml",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "sanitizer",
            "attributes": {},
            "y": 242.19066,
            "x": -355.07367,
            "id": "sanitizer",
            "size": 0.4955833
        },
        {
            "color": "#69c719",
            "label": "prelude-ls",
            "attributes": {},
            "y": 1009.4159,
            "x": -703.39124,
            "id": "prelude-ls",
            "size": 0.70858973
        },
        {
            "color": "#c78419",
            "label": "sqwish",
            "attributes": {},
            "y": -771.2408,
            "x": 393.27988,
            "id": "sqwish",
            "size": 0.70858973
        },
        {
            "color": "#c7b919",
            "label": "temporary",
            "attributes": {},
            "y": 399.0136,
            "x": 878.17725,
            "id": "temporary",
            "size": 0.8911666
        },
        {
            "color": "#4f19c7",
            "label": "opts",
            "attributes": {},
            "y": 278.39178,
            "x": -379.19516,
            "id": "opts",
            "size": 0.55644226
        },
        {
            "color": "#84c719",
            "label": "drip",
            "attributes": {},
            "y": -305.52167,
            "x": -102.83262,
            "id": "drip",
            "size": 0.64773077
        },
        {
            "color": "#84c719",
            "label": "sherlock",
            "attributes": {},
            "y": 137.86107,
            "x": 272.0998,
            "id": "sherlock",
            "size": 0.4651538
        },
        {
            "color": "#194fc7",
            "label": "deferred",
            "attributes": {},
            "y": -1267.6863,
            "x": 55.40451,
            "id": "deferred",
            "size": 0.8607372
        },
        {
            "color": "#194fc7",
            "label": "es5-ext",
            "attributes": {},
            "y": -1268.802,
            "x": 77.727,
            "id": "es5-ext",
            "size": 0.67816025
        },
        {
            "color": "#c71969",
            "label": "postal",
            "attributes": {},
            "y": -829.2972,
            "x": -171.42653,
            "id": "postal",
            "size": 0.43472436
        },
        {
            "color": "#c71919",
            "label": "jspack",
            "attributes": {},
            "y": 198.374,
            "x": 48.071236,
            "id": "jspack",
            "size": 0.52601284
        },
        {
            "color": "#c7194f",
            "label": "sphericalmercator",
            "attributes": {},
            "y": -296.1046,
            "x": -46.726612,
            "id": "sphericalmercator",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "xml",
            "attributes": {},
            "y": 101.8597,
            "x": -532.62463,
            "id": "xml",
            "size": 0.52601284
        },
        {
            "color": "#19c74f",
            "label": "ahr2",
            "attributes": {},
            "y": -875.5225,
            "x": -1099.1768,
            "id": "ahr2",
            "size": 0.70858973
        },
        {
            "color": "#199fc7",
            "label": "negotiator",
            "attributes": {},
            "y": 604.249,
            "x": 149.55948,
            "id": "negotiator",
            "size": 0.52601284
        },
        {
            "color": "#c719b9",
            "label": "thrift",
            "attributes": {},
            "y": 291.87094,
            "x": 5.0832486,
            "id": "thrift",
            "size": 0.4955833
        },
        {
            "color": "#19c719",
            "label": "source-map-support",
            "attributes": {},
            "y": -422.4552,
            "x": 1104.8613,
            "id": "source-map-support",
            "size": 0.58687174
        },
        {
            "color": "#19b9c7",
            "label": "cycle",
            "attributes": {},
            "y": 779.6143,
            "x": 812.88934,
            "id": "cycle",
            "size": 0.40429485
        },
        {
            "color": "#c7194f",
            "label": "sqlite3",
            "attributes": {},
            "y": 496.06732,
            "x": -256.83957,
            "id": "sqlite3",
            "size": 2.0170577
        },
        {
            "color": "#8419c7",
            "label": "xmlbuilder",
            "attributes": {},
            "y": 471.48856,
            "x": -699.2409,
            "id": "xmlbuilder",
            "size": 1.6214744
        },
        {
            "color": "#c719b9",
            "label": "amqp",
            "attributes": {},
            "y": 260.00815,
            "x": 153.61894,
            "id": "amqp",
            "size": 1.986628
        },
        {
            "color": "#19c769",
            "label": "needle",
            "attributes": {},
            "y": 372.77905,
            "x": -401.42374,
            "id": "needle",
            "size": 0.55644226
        },
        {
            "color": "#19c74f",
            "label": "stream-stack",
            "attributes": {},
            "y": -184.47614,
            "x": 40.362274,
            "id": "stream-stack",
            "size": 0.40429485
        },
        {
            "color": "#199fc7",
            "label": "read-stream",
            "attributes": {},
            "y": 631.4286,
            "x": -648.8073,
            "id": "read-stream",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "write-stream",
            "attributes": {},
            "y": 519.99194,
            "x": -549.48267,
            "id": "write-stream",
            "size": 0.52601284
        },
        {
            "color": "#199fc7",
            "label": "ap",
            "attributes": {},
            "y": 446.58817,
            "x": -144.28262,
            "id": "ap",
            "size": 0.67816025
        },
        {
            "color": "#19c74f",
            "label": "future",
            "attributes": {},
            "y": -867.01746,
            "x": -1071.5906,
            "id": "future",
            "size": 0.4651538
        },
        {
            "color": "#19c74f",
            "label": "sequence",
            "attributes": {},
            "y": -713.06415,
            "x": 365.48837,
            "id": "sequence",
            "size": 0.43472436
        },
        {
            "color": "#9fc719",
            "label": "extend",
            "attributes": {},
            "y": 263.66006,
            "x": 105.55116,
            "id": "extend",
            "size": 1.7127627
        },
        {
            "color": "#b9c719",
            "label": "fetch",
            "attributes": {},
            "y": -73.16297,
            "x": -346.91745,
            "id": "fetch",
            "size": 0.43472436
        },
        {
            "color": "#19c719",
            "label": "wordwrap",
            "attributes": {},
            "y": -227.00159,
            "x": 1031.0585,
            "id": "wordwrap",
            "size": 0.8911666
        },
        {
            "color": "#8419c7",
            "label": "line-reader",
            "attributes": {},
            "y": -127.01337,
            "x": -249.51375,
            "id": "line-reader",
            "size": 0.40429485
        },
        {
            "color": "#c719b9",
            "label": "sockjs",
            "attributes": {},
            "y": 837.4435,
            "x": -511.7771,
            "id": "sockjs",
            "size": 1.3780384
        },
        {
            "color": "#9f19c7",
            "label": "engine.io",
            "attributes": {},
            "y": -210.20392,
            "x": -906.73157,
            "id": "engine.io",
            "size": 0.95202565
        },
        {
            "color": "#199fc7",
            "label": "crdt",
            "attributes": {},
            "y": 947.0767,
            "x": 442.64102,
            "id": "crdt",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "mux-demux",
            "attributes": {},
            "y": 1019.63727,
            "x": 235.80574,
            "id": "mux-demux",
            "size": 0.8607372
        },
        {
            "color": "#194fc7",
            "label": "check-types",
            "attributes": {},
            "y": 269.9921,
            "x": 48.660164,
            "id": "check-types",
            "size": 0.52601284
        },
        {
            "color": "#c71969",
            "label": "tunnel",
            "attributes": {},
            "y": -404.86826,
            "x": -263.88354,
            "id": "tunnel",
            "size": 0.4651538
        },
        {
            "color": "#8419c7",
            "label": "devnull",
            "attributes": {},
            "y": -331.34488,
            "x": 703.6627,
            "id": "devnull",
            "size": 0.43472436
        },
        {
            "color": "#c7b919",
            "label": "d3",
            "attributes": {},
            "y": -284.5455,
            "x": -825.9526,
            "id": "d3",
            "size": 0.98245513
        },
        {
            "color": "#9fc719",
            "label": "ursa",
            "attributes": {},
            "y": 386.29645,
            "x": 26.145437,
            "id": "ursa",
            "size": 0.58687174
        },
        {
            "color": "#b919c7",
            "label": "valentine",
            "attributes": {},
            "y": 134.40224,
            "x": -344.4175,
            "id": "valentine",
            "size": 0.4651538
        },
        {
            "color": "#b9c719",
            "label": "posix",
            "attributes": {},
            "y": 338.36703,
            "x": -291.90344,
            "id": "posix",
            "size": 0.43472436
        },
        {
            "color": "#199fc7",
            "label": "twitter",
            "attributes": {},
            "y": 1405.1498,
            "x": -266.97806,
            "id": "twitter",
            "size": 0.4955833
        },
        {
            "color": "#c7194f",
            "label": "tav",
            "attributes": {},
            "y": 474.78238,
            "x": -155.47731,
            "id": "tav",
            "size": 0.40429485
        },
        {
            "color": "#1984c7",
            "label": "expresso",
            "attributes": {},
            "y": 323.57846,
            "x": 53.00957,
            "id": "expresso",
            "size": 0.43472436
        },
        {
            "color": "#c71919",
            "label": "less-middleware",
            "attributes": {},
            "y": -306.3249,
            "x": 79.35592,
            "id": "less-middleware",
            "size": 1.1954615
        },
        {
            "color": "#c71919",
            "label": "i18n",
            "attributes": {},
            "y": -98.362976,
            "x": -999.24835,
            "id": "i18n",
            "size": 0.64773077
        },
        {
            "color": "#19c7b9",
            "label": "deepmerge",
            "attributes": {},
            "y": -325.44296,
            "x": -307.36197,
            "id": "deepmerge",
            "size": 0.67816025
        },
        {
            "color": "#19c74f",
            "label": "pushover",
            "attributes": {},
            "y": 263.17816,
            "x": 434.1828,
            "id": "pushover",
            "size": 0.6173013
        },
        {
            "color": "#199fc7",
            "label": "wru",
            "attributes": {},
            "y": -353.93207,
            "x": -288.18814,
            "id": "wru",
            "size": 0.40429485
        },
        {
            "color": "#19c7b9",
            "label": "fs-tools",
            "attributes": {},
            "y": -228.75322,
            "x": 141.40994,
            "id": "fs-tools",
            "size": 0.55644226
        },
        {
            "color": "#1984c7",
            "label": "xregexp",
            "attributes": {},
            "y": 905.34344,
            "x": -812.6837,
            "id": "xregexp",
            "size": 0.8911666
        },
        {
            "color": "#c71919",
            "label": "config",
            "attributes": {},
            "y": -228.0563,
            "x": -316.3829,
            "id": "config",
            "size": 1.225891
        },
        {
            "color": "#1984c7",
            "label": "cron",
            "attributes": {},
            "y": 183.46445,
            "x": -313.95187,
            "id": "cron",
            "size": 1.28675
        },
        {
            "color": "#19c7b9",
            "label": "carrier",
            "attributes": {},
            "y": 363.87253,
            "x": -339.49533,
            "id": "carrier",
            "size": 0.83030766
        },
        {
            "color": "#1969c7",
            "label": "classes-component",
            "attributes": {},
            "y": -257.2873,
            "x": -265.0465,
            "id": "classes-component",
            "size": 0.4651538
        },
        {
            "color": "#c71919",
            "label": "hbs",
            "attributes": {},
            "y": -499.19263,
            "x": 633.9885,
            "id": "hbs",
            "size": 0.76944876
        },
        {
            "color": "#c71919",
            "label": "iced-coffee-script",
            "attributes": {},
            "y": 271.1939,
            "x": -351.02173,
            "id": "iced-coffee-script",
            "size": 1.0128845
        },
        {
            "color": "#19c719",
            "label": "color",
            "attributes": {},
            "y": -103.35395,
            "x": -286.06134,
            "id": "color",
            "size": 0.58687174
        },
        {
            "color": "#8419c7",
            "label": "follow",
            "attributes": {},
            "y": 164.50044,
            "x": -68.12239,
            "id": "follow",
            "size": 0.76944876
        },
        {
            "color": "#9f19c7",
            "label": "node-proxy",
            "attributes": {},
            "y": 195.5393,
            "x": -800.92053,
            "id": "node-proxy",
            "size": 0.76944876
        },
        {
            "color": "#c7b919",
            "label": "phantomjs",
            "attributes": {},
            "y": 152.25127,
            "x": 876.6572,
            "id": "phantomjs",
            "size": 1.7431923
        },
        {
            "color": "#1984c7",
            "label": "cloneextend",
            "attributes": {},
            "y": -229.28201,
            "x": 102.871826,
            "id": "cloneextend",
            "size": 0.70858973
        },
        {
            "color": "#c71919",
            "label": "tracer",
            "attributes": {},
            "y": -422.93143,
            "x": 542.50507,
            "id": "tracer",
            "size": 0.58687174
        },
        {
            "color": "#9f19c7",
            "label": "axon",
            "attributes": {},
            "y": -85.857155,
            "x": -931.0856,
            "id": "axon",
            "size": 0.83030766
        },
        {
            "color": "#c76919",
            "label": "nssocket",
            "attributes": {},
            "y": 535.05194,
            "x": 1203.0873,
            "id": "nssocket",
            "size": 0.55644226
        },
        {
            "color": "#1984c7",
            "label": "dropbox",
            "attributes": {},
            "y": -1175.9393,
            "x": -360.20236,
            "id": "dropbox",
            "size": 0.4651538
        },
        {
            "color": "#c719b9",
            "label": "dirty",
            "attributes": {},
            "y": 423.41846,
            "x": -299.88483,
            "id": "dirty",
            "size": 1.1346025
        },
        {
            "color": "#c719b9",
            "label": "json-schema",
            "attributes": {},
            "y": 157.80661,
            "x": -302.5626,
            "id": "json-schema",
            "size": 0.95202565
        },
        {
            "color": "#c719b9",
            "label": "fileops",
            "attributes": {},
            "y": -329.38306,
            "x": 137.90787,
            "id": "fileops",
            "size": 0.6173013
        },
        {
            "color": "#c71919",
            "label": "cluster",
            "attributes": {},
            "y": -411.9638,
            "x": 159.38046,
            "id": "cluster",
            "size": 0.52601284
        },
        {
            "color": "#c71969",
            "label": "data2xml",
            "attributes": {},
            "y": 437.87564,
            "x": -174.35355,
            "id": "data2xml",
            "size": 1.28675
        },
        {
            "color": "#c71969",
            "label": "aws-lib",
            "attributes": {},
            "y": 426.57806,
            "x": -553.01654,
            "id": "aws-lib",
            "size": 0.8607372
        },
        {
            "color": "#1984c7",
            "label": "node-phantom",
            "attributes": {},
            "y": 148.08284,
            "x": -739.18555,
            "id": "node-phantom",
            "size": 0.67816025
        },
        {
            "color": "#8419c7",
            "label": "MD5",
            "attributes": {},
            "y": -125.08657,
            "x": -299.09158,
            "id": "MD5",
            "size": 1.28675
        },
        {
            "color": "#c71919",
            "label": "gzippo",
            "attributes": {},
            "y": -2.3343637,
            "x": -802.20013,
            "id": "gzippo",
            "size": 0.4651538
        },
        {
            "color": "#34c719",
            "label": "extsprintf",
            "attributes": {},
            "y": 1132.2307,
            "x": -342.06006,
            "id": "extsprintf",
            "size": 0.40429485
        },
        {
            "color": "#34c719",
            "label": "verror",
            "attributes": {},
            "y": 1140.7922,
            "x": -322.61658,
            "id": "verror",
            "size": 0.43472436
        },
        {
            "color": "#1919c7",
            "label": "expect.js",
            "attributes": {},
            "y": 397.88303,
            "x": -275.31586,
            "id": "expect.js",
            "size": 0.92159617
        },
        {
            "color": "#c71919",
            "label": "slug",
            "attributes": {},
            "y": 352.22522,
            "x": 137.75543,
            "id": "slug",
            "size": 0.4651538
        },
        {
            "color": "#19c719",
            "label": "diff",
            "attributes": {},
            "y": 200.05052,
            "x": 422.92963,
            "id": "diff",
            "size": 0.7390192
        },
        {
            "color": "#1984c7",
            "label": "gravatar",
            "attributes": {},
            "y": 358.5257,
            "x": -313.8026,
            "id": "gravatar",
            "size": 0.4651538
        },
        {
            "color": "#19c7b9",
            "label": "dox",
            "attributes": {},
            "y": -780.07043,
            "x": -568.47504,
            "id": "dox",
            "size": 1.1041731
        },
        {
            "color": "#b919c7",
            "label": "reqwest",
            "attributes": {},
            "y": -53.65022,
            "x": -178.76468,
            "id": "reqwest",
            "size": 0.52601284
        },
        {
            "color": "#b919c7",
            "label": "qwery",
            "attributes": {},
            "y": -1192.8473,
            "x": -1008.4534,
            "id": "qwery",
            "size": 0.67816025
        },
        {
            "color": "#b919c7",
            "label": "domready",
            "attributes": {},
            "y": -1242.8838,
            "x": -1106.5486,
            "id": "domready",
            "size": 1.043314
        },
        {
            "color": "#8419c7",
            "label": "openid",
            "attributes": {},
            "y": 412.59,
            "x": -744.5368,
            "id": "openid",
            "size": 0.52601284
        },
        {
            "color": "#c74f19",
            "label": "longjohn",
            "attributes": {},
            "y": 211.15984,
            "x": 1253.4175,
            "id": "longjohn",
            "size": 0.58687174
        },
        {
            "color": "#c78419",
            "label": "node-sass",
            "attributes": {},
            "y": -105.74819,
            "x": 565.4153,
            "id": "node-sass",
            "size": 1.0128845
        },
        {
            "color": "#8419c7",
            "label": "entities",
            "attributes": {},
            "y": -421.44012,
            "x": -378.36694,
            "id": "entities",
            "size": 0.58687174
        },
        {
            "color": "#8419c7",
            "label": "css-parse",
            "attributes": {},
            "y": 1261.7021,
            "x": 133.59259,
            "id": "css-parse",
            "size": 0.55644226
        },
        {
            "color": "#69c719",
            "label": "collections",
            "attributes": {},
            "y": -89.36993,
            "x": -560.28796,
            "id": "collections",
            "size": 0.43472436
        },
        {
            "color": "#1984c7",
            "label": "gm",
            "attributes": {},
            "y": 313.9868,
            "x": -312.90167,
            "id": "gm",
            "size": 1.986628
        },
        {
            "color": "#c7194f",
            "label": "comb",
            "attributes": {},
            "y": 298.83356,
            "x": 43.5338,
            "id": "comb",
            "size": 0.43472436
        },
        {
            "color": "#199fc7",
            "label": "routes",
            "attributes": {},
            "y": -336.05746,
            "x": -69.0418,
            "id": "routes",
            "size": 0.83030766
        },
        {
            "color": "#c78419",
            "label": "node-log",
            "attributes": {},
            "y": -626.0221,
            "x": 393.26965,
            "id": "node-log",
            "size": 0.4651538
        },
        {
            "color": "#9f19c7",
            "label": "component-builder",
            "attributes": {},
            "y": -222.94373,
            "x": -186.5061,
            "id": "component-builder",
            "size": 0.70858973
        },
        {
            "color": "#199fc7",
            "label": "hyperquest",
            "attributes": {},
            "y": 825.61273,
            "x": 282.46597,
            "id": "hyperquest",
            "size": 1.165032
        },
        {
            "color": "#19c7b9",
            "label": "win-spawn",
            "attributes": {},
            "y": -140.79959,
            "x": -276.95242,
            "id": "win-spawn",
            "size": 0.58687174
        },
        {
            "color": "#c79f19",
            "label": "graphviz",
            "attributes": {},
            "y": 162.88615,
            "x": 1070.9303,
            "id": "graphviz",
            "size": 0.4651538
        },
        {
            "color": "#c78419",
            "label": "yaml-js",
            "attributes": {},
            "y": -481.71786,
            "x": -319.28323,
            "id": "yaml-js",
            "size": 0.4651538
        },
        {
            "color": "#c78419",
            "label": "get",
            "attributes": {},
            "y": 233.56311,
            "x": 150.1213,
            "id": "get",
            "size": 0.43472436
        },
        {
            "color": "#c79f19",
            "label": "kew",
            "attributes": {},
            "y": 184.67331,
            "x": 922.88745,
            "id": "kew",
            "size": 0.76944876
        },
        {
            "color": "#c71919",
            "label": "pause",
            "attributes": {},
            "y": 1019.8613,
            "x": 101.822105,
            "id": "pause",
            "size": 0.4955833
        },
        {
            "color": "#199fc7",
            "label": "levelup",
            "attributes": {},
            "y": 714.339,
            "x": -101.48984,
            "id": "levelup",
            "size": 1.7431923
        },
        {
            "color": "#199fc7",
            "label": "msgpack-js",
            "attributes": {},
            "y": 1044.0156,
            "x": -577.04565,
            "id": "msgpack-js",
            "size": 0.55644226
        },
        {
            "color": "#c78419",
            "label": "mincer",
            "attributes": {},
            "y": -335.08432,
            "x": 192.89568,
            "id": "mincer",
            "size": 0.6173013
        },
        {
            "color": "#c71919",
            "label": "mongolian",
            "attributes": {},
            "y": 357.0469,
            "x": -278.67535,
            "id": "mongolian",
            "size": 0.58687174
        },
        {
            "color": "#c71969",
            "label": "riak-js",
            "attributes": {},
            "y": 109.45611,
            "x": -554.1743,
            "id": "riak-js",
            "size": 0.67816025
        },
        {
            "color": "#19c719",
            "label": "JSONSelect",
            "attributes": {},
            "y": -674.25793,
            "x": 1032.245,
            "id": "JSONSelect",
            "size": 0.43472436
        },
        {
            "color": "#c71919",
            "label": "spdy",
            "attributes": {},
            "y": 969.4349,
            "x": -195.11647,
            "id": "spdy",
            "size": 0.4651538
        },
        {
            "color": "#c7b919",
            "label": "mout",
            "attributes": {},
            "y": -462.46005,
            "x": 62.060043,
            "id": "mout",
            "size": 0.70858973
        },
        {
            "color": "#4f19c7",
            "label": "jQuery",
            "attributes": {},
            "y": -330.18433,
            "x": -245.54166,
            "id": "jQuery",
            "size": 0.52601284
        },
        {
            "color": "#4f19c7",
            "label": "contextify",
            "attributes": {},
            "y": -187.65944,
            "x": -967.41296,
            "id": "contextify",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "level-sublevel",
            "attributes": {},
            "y": 989.98175,
            "x": 8.113629,
            "id": "level-sublevel",
            "size": 0.98245513
        },
        {
            "color": "#199fc7",
            "label": "tape",
            "attributes": {},
            "y": 783.2846,
            "x": 277.2358,
            "id": "tape",
            "size": 0.76944876
        },
        {
            "color": "#19c7b9",
            "label": "urllib",
            "attributes": {},
            "y": -233.95155,
            "x": -80.95783,
            "id": "urllib",
            "size": 0.52601284
        },
        {
            "color": "#199fc7",
            "label": "duplex",
            "attributes": {},
            "y": 1108.3147,
            "x": 320.11743,
            "id": "duplex",
            "size": 0.67816025
        },
        {
            "color": "#c71919",
            "label": "dustjs-helpers",
            "attributes": {},
            "y": -261.29047,
            "x": -302.44653,
            "id": "dustjs-helpers",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "base64",
            "attributes": {},
            "y": -139.1424,
            "x": -203.06262,
            "id": "base64",
            "size": 0.52601284
        },
        {
            "color": "#c79f19",
            "label": "elementtree",
            "attributes": {},
            "y": 637.6989,
            "x": -549.07086,
            "id": "elementtree",
            "size": 0.52601284
        },
        {
            "color": "#69c719",
            "label": "test",
            "attributes": {},
            "y": -1007.59406,
            "x": -665.63513,
            "id": "test",
            "size": 0.58687174
        },
        {
            "color": "#c71969",
            "label": "i",
            "attributes": {},
            "y": 701.9958,
            "x": 439.42538,
            "id": "i",
            "size": 0.52601284
        },
        {
            "color": "#1984c7",
            "label": "ftp",
            "attributes": {},
            "y": 910.1776,
            "x": -803.49304,
            "id": "ftp",
            "size": 0.64773077
        },
        {
            "color": "#1984c7",
            "label": "eyespect",
            "attributes": {},
            "y": -228.91646,
            "x": -367.09158,
            "id": "eyespect",
            "size": 1.5606153
        },
        {
            "color": "#1984c7",
            "label": "required-keys",
            "attributes": {},
            "y": -232.21452,
            "x": -286.83685,
            "id": "required-keys",
            "size": 3.2038076
        },
        {
            "color": "#8419c7",
            "label": "defaultable",
            "attributes": {},
            "y": 280.47433,
            "x": 72.49314,
            "id": "defaultable",
            "size": 0.4955833
        },
        {
            "color": "#19c719",
            "label": "node-inspector",
            "attributes": {},
            "y": 167.67815,
            "x": -547.4956,
            "id": "node-inspector",
            "size": 0.4955833
        },
        {
            "color": "#c71919",
            "label": "portscanner",
            "attributes": {},
            "y": 131.61783,
            "x": 103.87312,
            "id": "portscanner",
            "size": 0.58687174
        },
        {
            "color": "#c78419",
            "label": "burrito",
            "attributes": {},
            "y": -825.43256,
            "x": 397.68042,
            "id": "burrito",
            "size": 0.67816025
        },
        {
            "color": "#b9c719",
            "label": "crafity-jstest",
            "attributes": {},
            "y": 9.04491,
            "x": -371.97717,
            "id": "crafity-jstest",
            "size": 0.4955833
        },
        {
            "color": "#19c719",
            "label": "mu2",
            "attributes": {},
            "y": 408.01105,
            "x": -118.72287,
            "id": "mu2",
            "size": 0.7998782
        },
        {
            "color": "#199fc7",
            "label": "trumpet",
            "attributes": {},
            "y": 707.18274,
            "x": 125.280426,
            "id": "trumpet",
            "size": 0.58687174
        },
        {
            "color": "#9f19c7",
            "label": "ref",
            "attributes": {},
            "y": -118.67814,
            "x": -1197.3179,
            "id": "ref",
            "size": 0.98245513
        },
        {
            "color": "#9f19c7",
            "label": "ref-struct",
            "attributes": {},
            "y": -88.6764,
            "x": -1152.9425,
            "id": "ref-struct",
            "size": 0.64773077
        },
        {
            "color": "#9f19c7",
            "label": "ffi",
            "attributes": {},
            "y": -37.738617,
            "x": -1253.4946,
            "id": "ffi",
            "size": 0.83030766
        },
        {
            "color": "#194fc7",
            "label": "promise",
            "attributes": {},
            "y": -660.9082,
            "x": -798.1094,
            "id": "promise",
            "size": 0.92159617
        },
        {
            "color": "#199fc7",
            "label": "scuttlebutt",
            "attributes": {},
            "y": 1085.3298,
            "x": 394.12222,
            "id": "scuttlebutt",
            "size": 0.64773077
        },
        {
            "color": "#8419c7",
            "label": "form-data",
            "attributes": {},
            "y": 33.676548,
            "x": -79.20483,
            "id": "form-data",
            "size": 1.1954615
        },
        {
            "color": "#b9c719",
            "label": "router",
            "attributes": {},
            "y": 456.70023,
            "x": -234.20868,
            "id": "router",
            "size": 0.52601284
        },
        {
            "color": "#19c719",
            "label": "daemon",
            "attributes": {},
            "y": 421.1385,
            "x": -137.47592,
            "id": "daemon",
            "size": 1.0128845
        },
        {
            "color": "#c71969",
            "label": "sylvester",
            "attributes": {},
            "y": -948.5652,
            "x": -188.29977,
            "id": "sylvester",
            "size": 0.43472436
        },
        {
            "color": "#c78419",
            "label": "js2coffee",
            "attributes": {},
            "y": -1019.6858,
            "x": -36.928844,
            "id": "js2coffee",
            "size": 0.4955833
        },
        {
            "color": "#1969c7",
            "label": "cwise",
            "attributes": {},
            "y": -1295.9099,
            "x": 519.8282,
            "id": "cwise",
            "size": 0.67816025
        },
        {
            "color": "#4f19c7",
            "label": "css",
            "attributes": {},
            "y": 1263.161,
            "x": 123.637375,
            "id": "css",
            "size": 0.55644226
        },
        {
            "color": "#1969c7",
            "label": "event-component",
            "attributes": {},
            "y": -71.59668,
            "x": 239.32458,
            "id": "event-component",
            "size": 0.4651538
        },
        {
            "color": "#19c719",
            "label": "js-beautify",
            "attributes": {},
            "y": -108.54099,
            "x": 474.7446,
            "id": "js-beautify",
            "size": 0.92159617
        },
        {
            "color": "#69c719",
            "label": "q-io",
            "attributes": {},
            "y": -89.468155,
            "x": -507.4834,
            "id": "q-io",
            "size": 0.83030766
        },
        {
            "color": "#c71969",
            "label": "JSONPath",
            "attributes": {},
            "y": -781.22864,
            "x": -202.30043,
            "id": "JSONPath",
            "size": 0.58687174
        },
        {
            "color": "#c71919",
            "label": "mochiscript",
            "attributes": {},
            "y": 807.76044,
            "x": 1096.608,
            "id": "mochiscript",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "leveldown",
            "attributes": {},
            "y": 341.01407,
            "x": -775.22314,
            "id": "leveldown",
            "size": 0.58687174
        },
        {
            "color": "#c76919",
            "label": "Faker",
            "attributes": {},
            "y": 81.81546,
            "x": 295.8043,
            "id": "Faker",
            "size": 0.52601284
        },
        {
            "color": "#8419c7",
            "label": "nunjucks",
            "attributes": {},
            "y": 339.15506,
            "x": 72.22817,
            "id": "nunjucks",
            "size": 0.40429485
        },
        {
            "color": "#c719b9",
            "label": "sync",
            "attributes": {},
            "y": 217.82198,
            "x": 1387.9712,
            "id": "sync",
            "size": 0.55644226
        },
        {
            "color": "#c7b919",
            "label": "extended",
            "attributes": {},
            "y": -962.1278,
            "x": 657.08826,
            "id": "extended",
            "size": 0.70858973
        },
        {
            "color": "#c7b919",
            "label": "is-extended",
            "attributes": {},
            "y": -1022.18335,
            "x": 637.44147,
            "id": "is-extended",
            "size": 0.64773077
        },
        {
            "color": "#c7b919",
            "label": "array-extended",
            "attributes": {},
            "y": -995.6015,
            "x": 563.8498,
            "id": "array-extended",
            "size": 0.6173013
        },
        {
            "color": "#c7199f",
            "label": "put",
            "attributes": {},
            "y": -191.68346,
            "x": -98.489784,
            "id": "put",
            "size": 0.4651538
        },
        {
            "color": "#19c74f",
            "label": "deck",
            "attributes": {},
            "y": -56.16481,
            "x": -243.28035,
            "id": "deck",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "stream-combiner",
            "attributes": {},
            "y": 1035.9756,
            "x": 270.37732,
            "id": "stream-combiner",
            "size": 0.6173013
        },
        {
            "color": "#34c719",
            "label": "setimmediate",
            "attributes": {},
            "y": 536.1866,
            "x": 6.1590505,
            "id": "setimmediate",
            "size": 0.4955833
        },
        {
            "color": "#c78419",
            "label": "uglify-js2",
            "attributes": {},
            "y": -105.903336,
            "x": 874.6104,
            "id": "uglify-js2",
            "size": 0.4955833
        },
        {
            "color": "#19c719",
            "label": "upnode",
            "attributes": {},
            "y": 1053.4792,
            "x": -170.91736,
            "id": "upnode",
            "size": 0.58687174
        },
        {
            "color": "#c79f19",
            "label": "fstream-ignore",
            "attributes": {},
            "y": 18.67513,
            "x": 771.4828,
            "id": "fstream-ignore",
            "size": 0.6173013
        },
        {
            "color": "#19c7b9",
            "label": "smoosh",
            "attributes": {},
            "y": -627.7807,
            "x": 576.5164,
            "id": "smoosh",
            "size": 0.55644226
        },
        {
            "color": "#c79f19",
            "label": "yui",
            "attributes": {},
            "y": 98.7935,
            "x": 8.43035,
            "id": "yui",
            "size": 0.83030766
        },
        {
            "color": "#19c79f",
            "label": "method",
            "attributes": {},
            "y": -512.6561,
            "x": -1259.057,
            "id": "method",
            "size": 0.4651538
        },
        {
            "color": "#1919c7",
            "label": "node-getopt",
            "attributes": {},
            "y": -264.04025,
            "x": 52.247433,
            "id": "node-getopt",
            "size": 0.40429485
        },
        {
            "color": "#1919c7",
            "label": "foreach",
            "attributes": {},
            "y": -342.96857,
            "x": -85.643105,
            "id": "foreach",
            "size": 0.43472436
        },
        {
            "color": "#19c719",
            "label": "difflet",
            "attributes": {},
            "y": -828.60913,
            "x": 666.7738,
            "id": "difflet",
            "size": 0.52601284
        },
        {
            "color": "#c78419",
            "label": "mootools",
            "attributes": {},
            "y": -271.17963,
            "x": 78.709526,
            "id": "mootools",
            "size": 0.55644226
        },
        {
            "color": "#199fc7",
            "label": "shoe",
            "attributes": {},
            "y": 906.18555,
            "x": -374.22174,
            "id": "shoe",
            "size": 1.0737435
        },
        {
            "color": "#c71919",
            "label": "sass",
            "attributes": {},
            "y": -205.86336,
            "x": -5.8695316,
            "id": "sass",
            "size": 0.52601284
        },
        {
            "color": "#c79f19",
            "label": "level",
            "attributes": {},
            "y": 561.232,
            "x": -458.09595,
            "id": "level",
            "size": 0.55644226
        },
        {
            "color": "#19b9c7",
            "label": "jsonify",
            "attributes": {},
            "y": 937.7613,
            "x": 98.0932,
            "id": "jsonify",
            "size": 0.4651538
        },
        {
            "color": "#69c719",
            "label": "markdown-js",
            "attributes": {},
            "y": -1001.21906,
            "x": -673.2897,
            "id": "markdown-js",
            "size": 0.4651538
        },
        {
            "color": "#c78419",
            "label": "json5",
            "attributes": {},
            "y": -1142.8562,
            "x": 559.41046,
            "id": "json5",
            "size": 0.4651538
        },
        {
            "color": "#c76919",
            "label": "yamljs",
            "attributes": {},
            "y": -625.1245,
            "x": 429.07022,
            "id": "yamljs",
            "size": 0.76944876
        },
        {
            "color": "#1984c7",
            "label": "passport-http",
            "attributes": {},
            "y": 1112.6439,
            "x": 586.60333,
            "id": "passport-http",
            "size": 0.4651538
        },
        {
            "color": "#1984c7",
            "label": "docparse-config",
            "attributes": {},
            "y": 343.87463,
            "x": 1012.1537,
            "id": "docparse-config",
            "size": 0.7390192
        },
        {
            "color": "#1984c7",
            "label": "seaport",
            "attributes": {},
            "y": 555.8372,
            "x": 509.89893,
            "id": "seaport",
            "size": 1.165032
        },
        {
            "color": "#1984c7",
            "label": "imacros-read-file",
            "attributes": {},
            "y": 212.80945,
            "x": 78.05023,
            "id": "imacros-read-file",
            "size": 0.58687174
        },
        {
            "color": "#1984c7",
            "label": "loggly-console-logger",
            "attributes": {},
            "y": 724.5533,
            "x": 855.0759,
            "id": "loggly-console-logger",
            "size": 0.58687174
        },
        {
            "color": "#c719b9",
            "label": "apn",
            "attributes": {},
            "y": -407.88702,
            "x": -459.53925,
            "id": "apn",
            "size": 0.43472436
        },
        {
            "color": "#19c7b9",
            "label": "node-watch",
            "attributes": {},
            "y": 360.09363,
            "x": 35.46165,
            "id": "node-watch",
            "size": 0.6173013
        },
        {
            "color": "#84c719",
            "label": "tea-extend",
            "attributes": {},
            "y": 335.02548,
            "x": -347.4769,
            "id": "tea-extend",
            "size": 0.43472436
        },
        {
            "color": "#3419c7",
            "label": "qbox",
            "attributes": {},
            "y": -164.44691,
            "x": -25.2235,
            "id": "qbox",
            "size": 0.43472436
        },
        {
            "color": "#9fc719",
            "label": "passport-google-oauth",
            "attributes": {},
            "y": 1153.7697,
            "x": 589.3833,
            "id": "passport-google-oauth",
            "size": 0.4651538
        },
        {
            "color": "#c74f19",
            "label": "ar-drone",
            "attributes": {},
            "y": -290.17487,
            "x": 192.4303,
            "id": "ar-drone",
            "size": 0.55644226
        },
        {
            "color": "#19c74f",
            "label": "forEachAsync",
            "attributes": {},
            "y": -684.2996,
            "x": 378.59113,
            "id": "forEachAsync",
            "size": 0.4651538
        },
        {
            "color": "#c79f19",
            "label": "yuidocjs",
            "attributes": {},
            "y": -273.36804,
            "x": 444.81802,
            "id": "yuidocjs",
            "size": 0.6173013
        },
        {
            "color": "#8419c7",
            "label": "fs",
            "attributes": {},
            "y": 458.85266,
            "x": -260.27344,
            "id": "fs",
            "size": 0.55644226
        },
        {
            "color": "#19c719",
            "label": "snippets",
            "attributes": {},
            "y": -277.18225,
            "x": -223.52954,
            "id": "snippets",
            "size": 0.40429485
        },
        {
            "color": "#19c719",
            "label": "node-hid",
            "attributes": {},
            "y": -220.93335,
            "x": -213.05804,
            "id": "node-hid",
            "size": 0.4651538
        },
        {
            "color": "#1984c7",
            "label": "sf",
            "attributes": {},
            "y": 76.88708,
            "x": -167.24387,
            "id": "sf",
            "size": 0.40429485
        },
        {
            "color": "#c71984",
            "label": "revalidator",
            "attributes": {},
            "y": 787.1881,
            "x": 498.58612,
            "id": "revalidator",
            "size": 0.40429485
        },
        {
            "color": "#8419c7",
            "label": "googleclientlogin",
            "attributes": {},
            "y": -304.12473,
            "x": -80.95831,
            "id": "googleclientlogin",
            "size": 0.43472436
        },
        {
            "color": "#c73419",
            "label": "ee-class",
            "attributes": {},
            "y": 174.6967,
            "x": -397.30457,
            "id": "ee-class",
            "size": 0.4651538
        },
        {
            "color": "#9fc719",
            "label": "mongoose-types",
            "attributes": {},
            "y": 375.1962,
            "x": -1176.3058,
            "id": "mongoose-types",
            "size": 0.4651538
        },
        {
            "color": "#c74f19",
            "label": "funargs",
            "attributes": {},
            "y": 421.4906,
            "x": 1178.4454,
            "id": "funargs",
            "size": 1.1954615
        },
        {
            "color": "#b9c719",
            "label": "simplesmtp",
            "attributes": {},
            "y": -563.16315,
            "x": 867.2839,
            "id": "simplesmtp",
            "size": 0.4955833
        },
        {
            "color": "#b919c7",
            "label": "ender-bootstrap-base",
            "attributes": {},
            "y": -1214.9171,
            "x": -1119.1847,
            "id": "ender-bootstrap-base",
            "size": 0.67816025
        },
        {
            "color": "#b919c7",
            "label": "ender-bootstrap-transition",
            "attributes": {},
            "y": -1175.8195,
            "x": -1094.6414,
            "id": "ender-bootstrap-transition",
            "size": 0.52601284
        },
        {
            "color": "#9f19c7",
            "label": "engine.io-client",
            "attributes": {},
            "y": -288.4646,
            "x": -925.3114,
            "id": "engine.io-client",
            "size": 0.70858973
        },
        {
            "color": "#199fc7",
            "label": "monotonic-timestamp",
            "attributes": {},
            "y": 1104.9058,
            "x": 374.07852,
            "id": "monotonic-timestamp",
            "size": 0.4955833
        },
        {
            "color": "#34c719",
            "label": "ldapjs",
            "attributes": {},
            "y": 995.9913,
            "x": 197.95416,
            "id": "ldapjs",
            "size": 0.70858973
        },
        {
            "color": "#69c719",
            "label": "LiveScript",
            "attributes": {},
            "y": 1017.7713,
            "x": -697.17413,
            "id": "LiveScript",
            "size": 0.8607372
        },
        {
            "color": "#19b9c7",
            "label": "require-like",
            "attributes": {},
            "y": 410.90912,
            "x": -163.40764,
            "id": "require-like",
            "size": 0.4651538
        },
        {
            "color": "#199fc7",
            "label": "reconnect",
            "attributes": {},
            "y": 699.574,
            "x": -287.58524,
            "id": "reconnect",
            "size": 0.67816025
        },
        {
            "color": "#199fc7",
            "label": "from",
            "attributes": {},
            "y": 928.98145,
            "x": 332.75525,
            "id": "from",
            "size": 0.43472436
        },
        {
            "color": "#1934c7",
            "label": "eventproxy",
            "attributes": {},
            "y": -60.85565,
            "x": -296.83182,
            "id": "eventproxy",
            "size": 0.52601284
        },
        {
            "color": "#19c719",
            "label": "exec-sync",
            "attributes": {},
            "y": -16.778877,
            "x": -1259.8529,
            "id": "exec-sync",
            "size": 0.52601284
        },
        {
            "color": "#9fc719",
            "label": "passport-facebook",
            "attributes": {},
            "y": 1156.7816,
            "x": 612.5751,
            "id": "passport-facebook",
            "size": 0.55644226
        },
        {
            "color": "#c79f19",
            "label": "update-notifier",
            "attributes": {},
            "y": 130.25168,
            "x": 386.5853,
            "id": "update-notifier",
            "size": 0.55644226
        },
        {
            "color": "#19c719",
            "label": "utilities",
            "attributes": {},
            "y": -495.67886,
            "x": 962.3648,
            "id": "utilities",
            "size": 0.40429485
        },
        {
            "color": "#3419c7",
            "label": "fire",
            "attributes": {},
            "y": 26.584068,
            "x": 625.1236,
            "id": "fire",
            "size": 0.4651538
        },
        {
            "color": "#c79f19",
            "label": "yamlish",
            "attributes": {},
            "y": -378.95523,
            "x": 516.29596,
            "id": "yamlish",
            "size": 0.4955833
        },
        {
            "color": "#34c719",
            "label": "posix-getopt",
            "attributes": {},
            "y": 247.62514,
            "x": 79.496185,
            "id": "posix-getopt",
            "size": 0.76944876
        },
        {
            "color": "#34c719",
            "label": "latest",
            "attributes": {},
            "y": -97.57242,
            "x": 1358.8243,
            "id": "latest",
            "size": 0.4651538
        },
        {
            "color": "#c76919",
            "label": "yeoman-generator",
            "attributes": {},
            "y": -186.74983,
            "x": 190.55476,
            "id": "yeoman-generator",
            "size": 5.6381664
        },
        {
            "color": "#1984c7",
            "label": "jsftp",
            "attributes": {},
            "y": 475.91956,
            "x": 238.58153,
            "id": "jsftp",
            "size": 0.6173013
        },
        {
            "color": "#19c7b9",
            "label": "funkit",
            "attributes": {},
            "y": -254.73396,
            "x": -112.39201,
            "id": "funkit",
            "size": 0.55644226
        },
        {
            "color": "#84c719",
            "label": "xmlrpc",
            "attributes": {},
            "y": 566.62756,
            "x": -646.174,
            "id": "xmlrpc",
            "size": 0.8607372
        },
        {
            "color": "#c71969",
            "label": "gate",
            "attributes": {},
            "y": -207.42516,
            "x": -233.15547,
            "id": "gate",
            "size": 0.43472436
        },
        {
            "color": "#c7194f",
            "label": "mysql-libmysqlclient",
            "attributes": {},
            "y": -242.4547,
            "x": 88.063034,
            "id": "mysql-libmysqlclient",
            "size": 0.40429485
        },
        {
            "color": "#c71969",
            "label": "twit",
            "attributes": {},
            "y": 1252.696,
            "x": -227.96336,
            "id": "twit",
            "size": 0.4955833
        },
        {
            "color": "#34c719",
            "label": "ip",
            "attributes": {},
            "y": 578.1533,
            "x": 32.292908,
            "id": "ip",
            "size": 0.43472436
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-cssmin",
            "attributes": {},
            "y": -857.68835,
            "x": -357.30762,
            "id": "grunt-contrib-cssmin",
            "size": 0.4955833
        },
        {
            "color": "#c7b919",
            "label": "grunt-contrib-nodeunit",
            "attributes": {},
            "y": -535.1022,
            "x": 266.95883,
            "id": "grunt-contrib-nodeunit",
            "size": 0.6173013
        },
        {
            "color": "#c7b919",
            "label": "gzip-js",
            "attributes": {},
            "y": 241.80016,
            "x": 46.09004,
            "id": "gzip-js",
            "size": 0.4651538
        },
        {
            "color": "#c7b919",
            "label": "grunt-lib-phantomjs",
            "attributes": {},
            "y": 362.2341,
            "x": 879.5071,
            "id": "grunt-lib-phantomjs",
            "size": 0.55644226
        },
        {
            "color": "#1919c7",
            "label": "saucelabs",
            "attributes": {},
            "y": -214.85513,
            "x": 57.529392,
            "id": "saucelabs",
            "size": 0.43472436
        },
        {
            "color": "#c71919",
            "label": "node-syslog",
            "attributes": {},
            "y": -264.05222,
            "x": 125.97945,
            "id": "node-syslog",
            "size": 0.40429485
        },
        {
            "color": "#c719b9",
            "label": "hashring",
            "attributes": {},
            "y": 1145.2965,
            "x": -244.37975,
            "id": "hashring",
            "size": 0.4651538
        },
        {
            "color": "#19c734",
            "label": "hypher",
            "attributes": {},
            "y": -297.57465,
            "x": 113.438896,
            "id": "hypher",
            "size": 1.2563205
        },
        {
            "color": "#c78419",
            "label": "soda",
            "attributes": {},
            "y": -351.1734,
            "x": -19.649744,
            "id": "soda",
            "size": 0.43472436
        },
        {
            "color": "#199fc7",
            "label": "joose",
            "attributes": {},
            "y": 20.20147,
            "x": 1053.6621,
            "id": "joose",
            "size": 0.98245513
        },
        {
            "color": "#19c7b9",
            "label": "iwebpp.io",
            "attributes": {},
            "y": 989.7358,
            "x": -517.65106,
            "id": "iwebpp.io",
            "size": 0.64773077
        },
        {
            "color": "#19c7b9",
            "label": "siphash",
            "attributes": {},
            "y": 986.30225,
            "x": -539.15283,
            "id": "siphash",
            "size": 0.43472436
        },
        {
            "color": "#c71969",
            "label": "jsgui-lang-essentials",
            "attributes": {},
            "y": -574.97003,
            "x": 1197.1713,
            "id": "jsgui-lang-essentials",
            "size": 0.43472436
        },
        {
            "color": "#199fc7",
            "label": "pull-stream",
            "attributes": {},
            "y": 185.75874,
            "x": -367.50992,
            "id": "pull-stream",
            "size": 1.043314
        },
        {
            "color": "#8419c7",
            "label": "konphyg",
            "attributes": {},
            "y": 203.21783,
            "x": -333.21362,
            "id": "konphyg",
            "size": 0.40429485
        },
        {
            "color": "#199fc7",
            "label": "level-live-stream",
            "attributes": {},
            "y": 291.01462,
            "x": 101.217674,
            "id": "level-live-stream",
            "size": 0.52601284
        },
        {
            "color": "#19c7b9",
            "label": "logmimosa",
            "attributes": {},
            "y": -583.9365,
            "x": -1048.6061,
            "id": "logmimosa",
            "size": 0.76944876
        },
        {
            "color": "#c74f19",
            "label": "node-document-storage",
            "attributes": {},
            "y": 183.08963,
            "x": 1286.1066,
            "id": "node-document-storage",
            "size": 0.67816025
        },
        {
            "color": "#c71969",
            "label": "noflo",
            "attributes": {},
            "y": -971.328,
            "x": 310.00107,
            "id": "noflo",
            "size": 1.4388975
        },
        {
            "color": "#c78419",
            "label": "spine",
            "attributes": {},
            "y": 225.49977,
            "x": 13.505666,
            "id": "spine",
            "size": 0.4651538
        },
        {
            "color": "#c71969",
            "label": "punch",
            "attributes": {},
            "y": -520.8965,
            "x": -451.1391,
            "id": "punch",
            "size": 0.8607372
        },
        {
            "color": "#6919c7",
            "label": "quiver-error",
            "attributes": {},
            "y": -386.996,
            "x": 8.449575,
            "id": "quiver-error",
            "size": 0.52601284
        },
        {
            "color": "#1969c7",
            "label": "rle-core",
            "attributes": {},
            "y": 39.557953,
            "x": -379.84222,
            "id": "rle-core",
            "size": 0.40429485
        },
        {
            "color": "#199fc7",
            "label": "joosex-namespace-depended",
            "attributes": {},
            "y": 32.93445,
            "x": 1071.2402,
            "id": "joosex-namespace-depended",
            "size": 0.55644226
        },
        {
            "color": "#69c719",
            "label": "sourcemint-util-js",
            "attributes": {},
            "y": -501.3569,
            "x": -121.91505,
            "id": "sourcemint-util-js",
            "size": 0.7390192
        },
        {
            "color": "#c7b919",
            "label": "spmrc",
            "attributes": {},
            "y": 138.83679,
            "x": -316.52774,
            "id": "spmrc",
            "size": 0.40429485
        },
        {
            "color": "#c71934",
            "label": "tower-emitter",
            "attributes": {},
            "y": 1096.0394,
            "x": -553.1255,
            "id": "tower-emitter",
            "size": 0.55644226
        },
        {
            "color": "#c71934",
            "label": "tower-directive",
            "attributes": {},
            "y": 1093.3612,
            "x": -543.5085,
            "id": "tower-directive",
            "size": 0.4955833
        },
        {
            "color": "#c74f19",
            "label": "voxel",
            "attributes": {},
            "y": 321.36972,
            "x": 618.49976,
            "id": "voxel",
            "size": 0.52601284
        }
    ],
    "edges": [
        {
            "sourceID": "jquery",
            "attributes": {},
            "targetID": "jsdom",
            "size": 1
        },
        {
            "sourceID": "jquery",
            "attributes": {},
            "targetID": "xmlhttprequest",
            "size": 1
        },
        {
            "sourceID": "jquery",
            "attributes": {},
            "targetID": "htmlparser",
            "size": 1
        },
        {
            "sourceID": "jquery",
            "attributes": {},
            "targetID": "contextify",
            "size": 1
        },
        {
            "sourceID": "backbone",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "faye",
            "attributes": {},
            "targetID": "faye-websocket",
            "size": 1
        },
        {
            "sourceID": "faye",
            "attributes": {},
            "targetID": "cookiejar",
            "size": 1
        },
        {
            "sourceID": "socket.io",
            "attributes": {},
            "targetID": "redis",
            "size": 1
        },
        {
            "sourceID": "socket.io",
            "attributes": {},
            "targetID": "socket.io-client",
            "size": 1
        },
        {
            "sourceID": "mongoose",
            "attributes": {},
            "targetID": "mongodb",
            "size": 1
        },
        {
            "sourceID": "mongoose",
            "attributes": {},
            "targetID": "hooks",
            "size": 1
        },
        {
            "sourceID": "mongoose",
            "attributes": {},
            "targetID": "ms",
            "size": 1
        },
        {
            "sourceID": "cheerio",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "cheerio",
            "attributes": {},
            "targetID": "htmlparser2",
            "size": 1
        },
        {
            "sourceID": "cheerio",
            "attributes": {},
            "targetID": "entities",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "connect",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "cookie",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "send",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "methods",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "buffer-crc32",
            "size": 1
        },
        {
            "sourceID": "express",
            "attributes": {},
            "targetID": "fresh",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "bytes",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "cookie",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "send",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "formidable",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "methods",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "buffer-crc32",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "fresh",
            "size": 1
        },
        {
            "sourceID": "connect",
            "attributes": {},
            "targetID": "pause",
            "size": 1
        },
        {
            "sourceID": "temp",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "request",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "request",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "request",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "request",
            "attributes": {},
            "targetID": "form-data",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "duplexer",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "split",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "pause-stream",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "map-stream",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "stream-combiner",
            "size": 1
        },
        {
            "sourceID": "event-stream",
            "attributes": {},
            "targetID": "from",
            "size": 1
        },
        {
            "sourceID": "log4js",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "log4js",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "log4js",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "optimist",
            "attributes": {},
            "targetID": "wordwrap",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "jade",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "growl",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "ms",
            "size": 1
        },
        {
            "sourceID": "mocha",
            "attributes": {},
            "targetID": "diff",
            "size": 1
        },
        {
            "sourceID": "prompt",
            "attributes": {},
            "targetID": "read",
            "size": 1
        },
        {
            "sourceID": "prompt",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "prompt",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "prompt",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "prompt",
            "attributes": {},
            "targetID": "revalidator",
            "size": 1
        },
        {
            "sourceID": "commander",
            "attributes": {},
            "targetID": "keypress",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "dateformat",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "underscore.string",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "findup-sync",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "iconv-lite",
            "size": 1
        },
        {
            "sourceID": "grunt",
            "attributes": {},
            "targetID": "js-yaml",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-less",
            "attributes": {},
            "targetID": "less",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-less",
            "attributes": {},
            "targetID": "grunt-lib-contrib",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-jshint",
            "attributes": {},
            "targetID": "jshint",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-uglify",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-uglify",
            "attributes": {},
            "targetID": "grunt-lib-contrib",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-watch",
            "attributes": {},
            "targetID": "gaze",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-watch",
            "attributes": {},
            "targetID": "tiny-lr",
            "size": 1
        },
        {
            "sourceID": "http-proxy",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "http-proxy",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "http-proxy",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "http-proxy",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "mongodb",
            "attributes": {},
            "targetID": "bson",
            "size": 1
        },
        {
            "sourceID": "minimatch",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "nopt",
            "attributes": {},
            "targetID": "abbrev",
            "size": 1
        },
        {
            "sourceID": "rimraf",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "tar",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "tar",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "fstream",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "fstream",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "fstream",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "fstream",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "tar",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "npmlog",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "node-gyp",
            "attributes": {},
            "targetID": "osenv",
            "size": 1
        },
        {
            "sourceID": "fstream-npm",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "fstream-npm",
            "attributes": {},
            "targetID": "fstream-ignore",
            "size": 1
        },
        {
            "sourceID": "npmlog",
            "attributes": {},
            "targetID": "ansi",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "slide",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "npmlog",
            "size": 1
        },
        {
            "sourceID": "npm-registry-client",
            "attributes": {},
            "targetID": "retry",
            "size": 1
        },
        {
            "sourceID": "read-package-json",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "read-package-json",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "read-package-json",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "glob",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "glob",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "glob",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "ini",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "osenv",
            "size": 1
        },
        {
            "sourceID": "npmconf",
            "attributes": {},
            "targetID": "once",
            "size": 1
        },
        {
            "sourceID": "findup-sync",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "findup-sync",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "node-minify",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "node-minify",
            "attributes": {},
            "targetID": "sqwish",
            "size": 1
        },
        {
            "sourceID": "bal-util",
            "attributes": {},
            "targetID": "extendr",
            "size": 1
        },
        {
            "sourceID": "bal-util",
            "attributes": {},
            "targetID": "taskgroup",
            "size": 1
        },
        {
            "sourceID": "bal-util",
            "attributes": {},
            "targetID": "typechecker",
            "size": 1
        },
        {
            "sourceID": "extendr",
            "attributes": {},
            "targetID": "typechecker",
            "size": 1
        },
        {
            "sourceID": "taskgroup",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "underscorem",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "hubot",
            "attributes": {},
            "targetID": "express",
            "size": 1
        },
        {
            "sourceID": "hubot",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "hubot",
            "attributes": {},
            "targetID": "optparse",
            "size": 1
        },
        {
            "sourceID": "hubot",
            "attributes": {},
            "targetID": "log",
            "size": 1
        },
        {
            "sourceID": "ndarray-ops",
            "attributes": {},
            "targetID": "ndarray",
            "size": 1
        },
        {
            "sourceID": "ndarray-ops",
            "attributes": {},
            "targetID": "cwise",
            "size": 1
        },
        {
            "sourceID": "typedarray-pool",
            "attributes": {},
            "targetID": "bit-twiddle",
            "size": 1
        },
        {
            "sourceID": "jade",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "jade",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "nodemailer",
            "attributes": {},
            "targetID": "simplesmtp",
            "size": 1
        },
        {
            "sourceID": "eco",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "filed",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "flatiron",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "flatiron",
            "attributes": {},
            "targetID": "prompt",
            "size": 1
        },
        {
            "sourceID": "flatiron",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "flatiron",
            "attributes": {},
            "targetID": "director",
            "size": 1
        },
        {
            "sourceID": "flatiron",
            "attributes": {},
            "targetID": "broadway",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "stack-trace",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "eyes",
            "size": 1
        },
        {
            "sourceID": "winston",
            "attributes": {},
            "targetID": "cycle",
            "size": 1
        },
        {
            "sourceID": "coffeekup",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "stylus",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "stylus",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "stylus",
            "attributes": {},
            "targetID": "cssom",
            "size": 1
        },
        {
            "sourceID": "xml2json",
            "attributes": {},
            "targetID": "node-expat",
            "size": 1
        },
        {
            "sourceID": "nano",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "nano",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "nano",
            "attributes": {},
            "targetID": "errs",
            "size": 1
        },
        {
            "sourceID": "nano",
            "attributes": {},
            "targetID": "follow",
            "size": 1
        },
        {
            "sourceID": "less",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "less",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "less",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "less",
            "attributes": {},
            "targetID": "ycssmin",
            "size": 1
        },
        {
            "sourceID": "uglify-js",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "uglify-js",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "uglify-js",
            "attributes": {},
            "targetID": "source-map",
            "size": 1
        },
        {
            "sourceID": "clean-css",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "datetime",
            "attributes": {},
            "targetID": "vows",
            "size": 1
        },
        {
            "sourceID": "vows",
            "attributes": {},
            "targetID": "eyes",
            "size": 1
        },
        {
            "sourceID": "vows",
            "attributes": {},
            "targetID": "diff",
            "size": 1
        },
        {
            "sourceID": "docco",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "docco",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "docco",
            "attributes": {},
            "targetID": "marked",
            "size": 1
        },
        {
            "sourceID": "docco",
            "attributes": {},
            "targetID": "highlight.js",
            "size": 1
        },
        {
            "sourceID": "xml2js",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "libxmljs",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "handlebars",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "handlebars",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "slide",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "deep-equal",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "difflet",
            "size": 1
        },
        {
            "sourceID": "tap",
            "attributes": {},
            "targetID": "yamlish",
            "size": 1
        },
        {
            "sourceID": "walk",
            "attributes": {},
            "targetID": "forEachAsync",
            "size": 1
        },
        {
            "sourceID": "split",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "memcached",
            "attributes": {},
            "targetID": "hashring",
            "size": 1
        },
        {
            "sourceID": "express-resource",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "express-resource",
            "attributes": {},
            "targetID": "lingo",
            "size": 1
        },
        {
            "sourceID": "express-resource",
            "attributes": {},
            "targetID": "methods",
            "size": 1
        },
        {
            "sourceID": "connect-assets",
            "attributes": {},
            "targetID": "snockets",
            "size": 1
        },
        {
            "sourceID": "knox",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "knox",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "knox",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "aws-sdk",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "aws-sdk",
            "attributes": {},
            "targetID": "xmlbuilder",
            "size": 1
        },
        {
            "sourceID": "fs-extra",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "fs-extra",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "fs-extra",
            "attributes": {},
            "targetID": "ncp",
            "size": 1
        },
        {
            "sourceID": "awssum",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "awssum",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "cradle",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "cradle",
            "attributes": {},
            "targetID": "follow",
            "size": 1
        },
        {
            "sourceID": "cli-color",
            "attributes": {},
            "targetID": "es5-ext",
            "size": 1
        },
        {
            "sourceID": "hashish",
            "attributes": {},
            "targetID": "traverse",
            "size": 1
        },
        {
            "sourceID": "htmlparser2",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "netmask",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "filed",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "errs",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "pkgcloud",
            "attributes": {},
            "targetID": "ip",
            "size": 1
        },
        {
            "sourceID": "mailparser",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "mailparser",
            "attributes": {},
            "targetID": "iconv",
            "size": 1
        },
        {
            "sourceID": "portfinder",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "forever-monitor",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "forever-monitor",
            "attributes": {},
            "targetID": "watch",
            "size": 1
        },
        {
            "sourceID": "forever-monitor",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "forever-monitor",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "forever-monitor",
            "attributes": {},
            "targetID": "broadway",
            "size": 1
        },
        {
            "sourceID": "passport",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport",
            "attributes": {},
            "targetID": "pause",
            "size": 1
        },
        {
            "sourceID": "jshint",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "jshint",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "jshint",
            "attributes": {},
            "targetID": "cli",
            "size": 1
        },
        {
            "sourceID": "jshint",
            "attributes": {},
            "targetID": "shelljs",
            "size": 1
        },
        {
            "sourceID": "nib",
            "attributes": {},
            "targetID": "stylus",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-stylus",
            "attributes": {},
            "targetID": "stylus",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-stylus",
            "attributes": {},
            "targetID": "nib",
            "size": 1
        },
        {
            "sourceID": "phantom",
            "attributes": {},
            "targetID": "dnode",
            "size": 1
        },
        {
            "sourceID": "phantom",
            "attributes": {},
            "targetID": "shoe",
            "size": 1
        },
        {
            "sourceID": "jslint",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "bufferstream",
            "attributes": {},
            "targetID": "buffertools",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "event-stream",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "duplexer",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "shell-quote",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "concat-stream",
            "size": 1
        },
        {
            "sourceID": "browserify",
            "attributes": {},
            "targetID": "JSONStream",
            "size": 1
        },
        {
            "sourceID": "nodeunit",
            "attributes": {},
            "targetID": "tap",
            "size": 1
        },
        {
            "sourceID": "vine",
            "attributes": {},
            "targetID": "outcome",
            "size": 1
        },
        {
            "sourceID": "findit",
            "attributes": {},
            "targetID": "seq",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "structr",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "step",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "outcome",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "dref",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "toarray",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "sift",
            "size": 1
        },
        {
            "sourceID": "plugin",
            "attributes": {},
            "targetID": "resolve",
            "size": 1
        },
        {
            "sourceID": "sk",
            "attributes": {},
            "targetID": "dateformat",
            "size": 1
        },
        {
            "sourceID": "sk",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "sk",
            "attributes": {},
            "targetID": "structr",
            "size": 1
        },
        {
            "sourceID": "sk",
            "attributes": {},
            "targetID": "htmlparser",
            "size": 1
        },
        {
            "sourceID": "sk",
            "attributes": {},
            "targetID": "printf",
            "size": 1
        },
        {
            "sourceID": "stitch",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "stitch",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "requirejs",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "gaze",
            "size": 1
        },
        {
            "sourceID": "jasmine-node",
            "attributes": {},
            "targetID": "walkdir",
            "size": 1
        },
        {
            "sourceID": "jsdom",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "jsdom",
            "attributes": {},
            "targetID": "htmlparser2",
            "size": 1
        },
        {
            "sourceID": "jsdom",
            "attributes": {},
            "targetID": "cssom",
            "size": 1
        },
        {
            "sourceID": "jsdom",
            "attributes": {},
            "targetID": "contextify",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "emitter-component",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "formidable",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "methods",
            "size": 1
        },
        {
            "sourceID": "superagent",
            "attributes": {},
            "targetID": "cookiejar",
            "size": 1
        },
        {
            "sourceID": "readdirp",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "readdirp",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "ws",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "faye-websocket",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "mocha",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "browserify",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "node-expat",
            "size": 1
        },
        {
            "sourceID": "node-xmpp",
            "attributes": {},
            "targetID": "ltx",
            "size": 1
        },
        {
            "sourceID": "watchr",
            "attributes": {},
            "targetID": "bal-util",
            "size": 1
        },
        {
            "sourceID": "watchr",
            "attributes": {},
            "targetID": "extendr",
            "size": 1
        },
        {
            "sourceID": "watchr",
            "attributes": {},
            "targetID": "taskgroup",
            "size": 1
        },
        {
            "sourceID": "watchr",
            "attributes": {},
            "targetID": "typechecker",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "structr",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "tq",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "plugin",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "crema",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "outcome",
            "size": 1
        },
        {
            "sourceID": "celeri",
            "attributes": {},
            "targetID": "keypress",
            "size": 1
        },
        {
            "sourceID": "coa",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "ometajs",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "ometajs",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "ometajs",
            "attributes": {},
            "targetID": "coa",
            "size": 1
        },
        {
            "sourceID": "q-fs",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "q-fs",
            "attributes": {},
            "targetID": "q-io",
            "size": 1
        },
        {
            "sourceID": "falafel",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "cli-table",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "cli",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "bunyan",
            "attributes": {},
            "targetID": "dtrace-provider",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "deep-equal",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "ncp",
            "size": 1
        },
        {
            "sourceID": "utile",
            "attributes": {},
            "targetID": "i",
            "size": 1
        },
        {
            "sourceID": "send",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "send",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "send",
            "attributes": {},
            "targetID": "fresh",
            "size": 1
        },
        {
            "sourceID": "jison",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "jison",
            "attributes": {},
            "targetID": "nomnom",
            "size": 1
        },
        {
            "sourceID": "jison",
            "attributes": {},
            "targetID": "escodegen",
            "size": 1
        },
        {
            "sourceID": "jison",
            "attributes": {},
            "targetID": "cjson",
            "size": 1
        },
        {
            "sourceID": "jison",
            "attributes": {},
            "targetID": "JSONSelect",
            "size": 1
        },
        {
            "sourceID": "socket.io-client",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "socket.io-client",
            "attributes": {},
            "targetID": "ws",
            "size": 1
        },
        {
            "sourceID": "socket.io-client",
            "attributes": {},
            "targetID": "xmlhttprequest",
            "size": 1
        },
        {
            "sourceID": "resource",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "resource",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "resource",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "jake",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "jake",
            "attributes": {},
            "targetID": "utilities",
            "size": 1
        },
        {
            "sourceID": "assert",
            "attributes": {},
            "targetID": "util",
            "size": 1
        },
        {
            "sourceID": "detective",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "detective",
            "attributes": {},
            "targetID": "escodegen",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "abbrev",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "handlebars",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "resolve",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "escodegen",
            "size": 1
        },
        {
            "sourceID": "istanbul",
            "attributes": {},
            "targetID": "wordwrap",
            "size": 1
        },
        {
            "sourceID": "tiny-lr",
            "attributes": {},
            "targetID": "faye-websocket",
            "size": 1
        },
        {
            "sourceID": "tiny-lr",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "tiny-lr",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "argparse",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "argparse",
            "attributes": {},
            "targetID": "underscore.string",
            "size": 1
        },
        {
            "sourceID": "dref",
            "attributes": {},
            "targetID": "structr",
            "size": 1
        },
        {
            "sourceID": "dref",
            "attributes": {},
            "targetID": "dref",
            "size": 1
        },
        {
            "sourceID": "dref",
            "attributes": {},
            "targetID": "type-component",
            "size": 1
        },
        {
            "sourceID": "haml-coffee",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "haml-coffee",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "haml-coffee",
            "attributes": {},
            "targetID": "walkdir",
            "size": 1
        },
        {
            "sourceID": "binary",
            "attributes": {},
            "targetID": "buffers",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "watch",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "flatiron",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "forever-monitor",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "nconf",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "cliff",
            "size": 1
        },
        {
            "sourceID": "forever",
            "attributes": {},
            "targetID": "nssocket",
            "size": 1
        },
        {
            "sourceID": "serialport",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "serialport",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "serialport",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "serialport",
            "attributes": {},
            "targetID": "sf",
            "size": 1
        },
        {
            "sourceID": "connect-redis",
            "attributes": {},
            "targetID": "redis",
            "size": 1
        },
        {
            "sourceID": "connect-redis",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "dnode",
            "attributes": {},
            "targetID": "jsonify",
            "size": 1
        },
        {
            "sourceID": "union",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "union",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "passport-local",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-local",
            "attributes": {},
            "targetID": "passport",
            "size": 1
        },
        {
            "sourceID": "markdown",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "microtime",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "rss",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "rss",
            "attributes": {},
            "targetID": "xml",
            "size": 1
        },
        {
            "sourceID": "connect-mongodb",
            "attributes": {},
            "targetID": "connect",
            "size": 1
        },
        {
            "sourceID": "connect-mongodb",
            "attributes": {},
            "targetID": "mongodb",
            "size": 1
        },
        {
            "sourceID": "connect-form",
            "attributes": {},
            "targetID": "formidable",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "jsdom",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "ws",
            "size": 1
        },
        {
            "sourceID": "zombie",
            "attributes": {},
            "targetID": "ms",
            "size": 1
        },
        {
            "sourceID": "jugglingdb",
            "attributes": {},
            "targetID": "inflection",
            "size": 1
        },
        {
            "sourceID": "hiredis",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "swig",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "node-static",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "node-static",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "node-static",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "bootstrap",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "nconf",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "nconf",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "nconf",
            "attributes": {},
            "targetID": "ini",
            "size": 1
        },
        {
            "sourceID": "nconf",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "seq",
            "attributes": {},
            "targetID": "hashish",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "dateformat",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "validator",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "xmlbuilder",
            "size": 1
        },
        {
            "sourceID": "azure",
            "attributes": {},
            "targetID": "tunnel",
            "size": 1
        },
        {
            "sourceID": "pg",
            "attributes": {},
            "targetID": "generic-pool",
            "size": 1
        },
        {
            "sourceID": "pg",
            "attributes": {},
            "targetID": "ref",
            "size": 1
        },
        {
            "sourceID": "jqtpl",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "ini",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "slide",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "abbrev",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "tar",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "read",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "node-gyp",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "fstream-npm",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "archy",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "npmlog",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "ansi",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "npm-registry-client",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "read-package-json",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "osenv",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "retry",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "once",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "npmconf",
            "size": 1
        },
        {
            "sourceID": "npm",
            "attributes": {},
            "targetID": "opener",
            "size": 1
        },
        {
            "sourceID": "nomnom",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "nomnom",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "passport-oauth",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-oauth",
            "attributes": {},
            "targetID": "passport",
            "size": 1
        },
        {
            "sourceID": "passport-oauth",
            "attributes": {},
            "targetID": "oauth",
            "size": 1
        },
        {
            "sourceID": "passport-twitter",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-twitter",
            "attributes": {},
            "targetID": "passport-oauth",
            "size": 1
        },
        {
            "sourceID": "mongoskin",
            "attributes": {},
            "targetID": "mongodb",
            "size": 1
        },
        {
            "sourceID": "emailjs",
            "attributes": {},
            "targetID": "moment",
            "size": 1
        },
        {
            "sourceID": "emailjs",
            "attributes": {},
            "targetID": "bufferjs",
            "size": 1
        },
        {
            "sourceID": "connect-mongo",
            "attributes": {},
            "targetID": "mongodb",
            "size": 1
        },
        {
            "sourceID": "bcrypt",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "ntwitter",
            "attributes": {},
            "targetID": "cookies",
            "size": 1
        },
        {
            "sourceID": "ntwitter",
            "attributes": {},
            "targetID": "oauth",
            "size": 1
        },
        {
            "sourceID": "ntwitter",
            "attributes": {},
            "targetID": "keygrip",
            "size": 1
        },
        {
            "sourceID": "juice",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "juice",
            "attributes": {},
            "targetID": "batch",
            "size": 1
        },
        {
            "sourceID": "juice",
            "attributes": {},
            "targetID": "cssom",
            "size": 1
        },
        {
            "sourceID": "juice",
            "attributes": {},
            "targetID": "jsdom",
            "size": 1
        },
        {
            "sourceID": "juice",
            "attributes": {},
            "targetID": "superagent",
            "size": 1
        },
        {
            "sourceID": "pause-stream",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "underscore.string",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "validator",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "lingo",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "moment",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "generic-pool",
            "size": 1
        },
        {
            "sourceID": "sequelize",
            "attributes": {},
            "targetID": "promise",
            "size": 1
        },
        {
            "sourceID": "tar.gz",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "tar.gz",
            "attributes": {},
            "targetID": "tar",
            "size": 1
        },
        {
            "sourceID": "tar.gz",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "prettyjson",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "escodegen",
            "attributes": {},
            "targetID": "estraverse",
            "size": 1
        },
        {
            "sourceID": "escodegen",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "escodegen",
            "attributes": {},
            "targetID": "source-map",
            "size": 1
        },
        {
            "sourceID": "url",
            "attributes": {},
            "targetID": "querystring",
            "size": 1
        },
        {
            "sourceID": "ltx",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "ltx",
            "attributes": {},
            "targetID": "node-expat",
            "size": 1
        },
        {
            "sourceID": "bouncy",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "bouncy",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "simplicial-complex",
            "attributes": {},
            "targetID": "bit-twiddle",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "hogan.js",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "abbrev",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "which",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "tar",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "archy",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "read-package-json",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "tmp",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "rc",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "unzip",
            "size": 1
        },
        {
            "sourceID": "bower",
            "attributes": {},
            "targetID": "update-notifier",
            "size": 1
        },
        {
            "sourceID": "rc",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "rc",
            "attributes": {},
            "targetID": "ini",
            "size": 1
        },
        {
            "sourceID": "rc",
            "attributes": {},
            "targetID": "deep-extend",
            "size": 1
        },
        {
            "sourceID": "unzip",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "unzip",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "unzip",
            "attributes": {},
            "targetID": "binary",
            "size": 1
        },
        {
            "sourceID": "unzip",
            "attributes": {},
            "targetID": "setimmediate",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "underscore.string",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "read",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "scaffolder",
            "attributes": {},
            "targetID": "out",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "socket.io",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "prompt",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "portfinder",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "socket.io-client",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "union",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "nconf",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "npm",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "traverse",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "ecstatic",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "lazy",
            "size": 1
        },
        {
            "sourceID": "hook.io",
            "attributes": {},
            "targetID": "jsonify",
            "size": 1
        },
        {
            "sourceID": "fs.extra",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "fs.extra",
            "attributes": {},
            "targetID": "walk",
            "size": 1
        },
        {
            "sourceID": "fs.extra",
            "attributes": {},
            "targetID": "fs-extra",
            "size": 1
        },
        {
            "sourceID": "now",
            "attributes": {},
            "targetID": "socket.io",
            "size": 1
        },
        {
            "sourceID": "now",
            "attributes": {},
            "targetID": "node-proxy",
            "size": 1
        },
        {
            "sourceID": "brfs",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "brfs",
            "attributes": {},
            "targetID": "falafel",
            "size": 1
        },
        {
            "sourceID": "brfs",
            "attributes": {},
            "targetID": "escodegen",
            "size": 1
        },
        {
            "sourceID": "mongojs",
            "attributes": {},
            "targetID": "mongodb",
            "size": 1
        },
        {
            "sourceID": "mongojs",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "feedparser",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "feedparser",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "feedparser",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "broadway",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "broadway",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "broadway",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "broadway",
            "attributes": {},
            "targetID": "nconf",
            "size": 1
        },
        {
            "sourceID": "broadway",
            "attributes": {},
            "targetID": "cliff",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "backoff",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "once",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "bunyan",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "deep-equal",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "formidable",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "assert-plus",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "dtrace-provider",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "negotiator",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "verror",
            "size": 1
        },
        {
            "sourceID": "restify",
            "attributes": {},
            "targetID": "spdy",
            "size": 1
        },
        {
            "sourceID": "cliff",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "cliff",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "cliff",
            "attributes": {},
            "targetID": "eyes",
            "size": 1
        },
        {
            "sourceID": "JSONStream",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "plist",
            "attributes": {},
            "targetID": "xmldom",
            "size": 1
        },
        {
            "sourceID": "plist",
            "attributes": {},
            "targetID": "xmlbuilder",
            "size": 1
        },
        {
            "sourceID": "natural",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "natural",
            "attributes": {},
            "targetID": "sylvester",
            "size": 1
        },
        {
            "sourceID": "global",
            "attributes": {},
            "targetID": "process",
            "size": 1
        },
        {
            "sourceID": "ecstatic",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "ecstatic",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "ecstatic",
            "attributes": {},
            "targetID": "ent",
            "size": 1
        },
        {
            "sourceID": "useragent",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "snockets",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "snockets",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "snockets",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "snockets",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "soupselect",
            "attributes": {},
            "targetID": "nodeunit",
            "size": 1
        },
        {
            "sourceID": "soupselect",
            "attributes": {},
            "targetID": "htmlparser",
            "size": 1
        },
        {
            "sourceID": "mailer",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "mailer",
            "attributes": {},
            "targetID": "nodemailer",
            "size": 1
        },
        {
            "sourceID": "archiver",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "aws2js",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "aws2js",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "aws2js",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "aws2js",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "websocket.io",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "websocket.io",
            "attributes": {},
            "targetID": "ws",
            "size": 1
        },
        {
            "sourceID": "reducers",
            "attributes": {},
            "targetID": "reducible",
            "size": 1
        },
        {
            "sourceID": "reducible",
            "attributes": {},
            "targetID": "method",
            "size": 1
        },
        {
            "sourceID": "coffee-script-redux",
            "attributes": {},
            "targetID": "escodegen",
            "size": 1
        },
        {
            "sourceID": "coffee-script-redux",
            "attributes": {},
            "targetID": "source-map",
            "size": 1
        },
        {
            "sourceID": "source-map",
            "attributes": {},
            "targetID": "amdefine",
            "size": 1
        },
        {
            "sourceID": "time",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "time",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "cson",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "cson",
            "attributes": {},
            "targetID": "js2coffee",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "cradle",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "utile",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "i",
            "size": 1
        },
        {
            "sourceID": "resourceful",
            "attributes": {},
            "targetID": "revalidator",
            "size": 1
        },
        {
            "sourceID": "execSync",
            "attributes": {},
            "targetID": "ffi",
            "size": 1
        },
        {
            "sourceID": "loader-utils",
            "attributes": {},
            "targetID": "json5",
            "size": 1
        },
        {
            "sourceID": "wd",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "wd",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "wd",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "wd",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "fs-watch-tree",
            "attributes": {},
            "targetID": "when",
            "size": 1
        },
        {
            "sourceID": "glob-whatev",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "lru-cache",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "hoek",
            "size": 1
        },
        {
            "sourceID": "hapi",
            "attributes": {},
            "targetID": "negotiator",
            "size": 1
        },
        {
            "sourceID": "coffeecup",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "coffeecup",
            "attributes": {},
            "targetID": "stylus",
            "size": 1
        },
        {
            "sourceID": "coffeecup",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "coffeecup",
            "attributes": {},
            "targetID": "optparse",
            "size": 1
        },
        {
            "sourceID": "js-yaml",
            "attributes": {},
            "targetID": "esprima",
            "size": 1
        },
        {
            "sourceID": "js-yaml",
            "attributes": {},
            "targetID": "argparse",
            "size": 1
        },
        {
            "sourceID": "jeesh",
            "attributes": {},
            "targetID": "bean",
            "size": 1
        },
        {
            "sourceID": "jeesh",
            "attributes": {},
            "targetID": "bonzo",
            "size": 1
        },
        {
            "sourceID": "jeesh",
            "attributes": {},
            "targetID": "qwery",
            "size": 1
        },
        {
            "sourceID": "jeesh",
            "attributes": {},
            "targetID": "domready",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "express",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "connect",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "oauth",
            "size": 1
        },
        {
            "sourceID": "everyauth",
            "attributes": {},
            "targetID": "openid",
            "size": 1
        },
        {
            "sourceID": "deferred",
            "attributes": {},
            "targetID": "es5-ext",
            "size": 1
        },
        {
            "sourceID": "postal",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "ahr2",
            "attributes": {},
            "targetID": "bufferjs",
            "size": 1
        },
        {
            "sourceID": "ahr2",
            "attributes": {},
            "targetID": "future",
            "size": 1
        },
        {
            "sourceID": "source-map-support",
            "attributes": {},
            "targetID": "source-map",
            "size": 1
        },
        {
            "sourceID": "needle",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "needle",
            "attributes": {},
            "targetID": "iconv-lite",
            "size": 1
        },
        {
            "sourceID": "read-stream",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "read-stream",
            "attributes": {},
            "targetID": "process",
            "size": 1
        },
        {
            "sourceID": "write-stream",
            "attributes": {},
            "targetID": "readable-stream",
            "size": 1
        },
        {
            "sourceID": "sockjs",
            "attributes": {},
            "targetID": "faye-websocket",
            "size": 1
        },
        {
            "sourceID": "sockjs",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "engine.io",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "engine.io",
            "attributes": {},
            "targetID": "ws",
            "size": 1
        },
        {
            "sourceID": "crdt",
            "attributes": {},
            "targetID": "scuttlebutt",
            "size": 1
        },
        {
            "sourceID": "mux-demux",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "mux-demux",
            "attributes": {},
            "targetID": "xtend",
            "size": 1
        },
        {
            "sourceID": "mux-demux",
            "attributes": {},
            "targetID": "duplex",
            "size": 1
        },
        {
            "sourceID": "mux-demux",
            "attributes": {},
            "targetID": "stream-combiner",
            "size": 1
        },
        {
            "sourceID": "devnull",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "d3",
            "attributes": {},
            "targetID": "jsdom",
            "size": 1
        },
        {
            "sourceID": "twitter",
            "attributes": {},
            "targetID": "cookies",
            "size": 1
        },
        {
            "sourceID": "twitter",
            "attributes": {},
            "targetID": "oauth",
            "size": 1
        },
        {
            "sourceID": "twitter",
            "attributes": {},
            "targetID": "keygrip",
            "size": 1
        },
        {
            "sourceID": "less-middleware",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "less-middleware",
            "attributes": {},
            "targetID": "less",
            "size": 1
        },
        {
            "sourceID": "i18n",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "i18n",
            "attributes": {},
            "targetID": "sprintf",
            "size": 1
        },
        {
            "sourceID": "pushover",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "pushover",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "pushover",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "fs-tools",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "fs-tools",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "hbs",
            "attributes": {},
            "targetID": "handlebars",
            "size": 1
        },
        {
            "sourceID": "hbs",
            "attributes": {},
            "targetID": "after",
            "size": 1
        },
        {
            "sourceID": "follow",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "npmconf",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "adm-zip",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "ncp",
            "size": 1
        },
        {
            "sourceID": "phantomjs",
            "attributes": {},
            "targetID": "kew",
            "size": 1
        },
        {
            "sourceID": "tracer",
            "attributes": {},
            "targetID": "dateformat",
            "size": 1
        },
        {
            "sourceID": "tracer",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "axon",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "nssocket",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "nssocket",
            "attributes": {},
            "targetID": "lazy",
            "size": 1
        },
        {
            "sourceID": "dropbox",
            "attributes": {},
            "targetID": "open",
            "size": 1
        },
        {
            "sourceID": "cluster",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "cluster",
            "attributes": {},
            "targetID": "log",
            "size": 1
        },
        {
            "sourceID": "aws-lib",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "aws-lib",
            "attributes": {},
            "targetID": "xml2js",
            "size": 1
        },
        {
            "sourceID": "node-phantom",
            "attributes": {},
            "targetID": "socket.io",
            "size": 1
        },
        {
            "sourceID": "gzippo",
            "attributes": {},
            "targetID": "send",
            "size": 1
        },
        {
            "sourceID": "verror",
            "attributes": {},
            "targetID": "extsprintf",
            "size": 1
        },
        {
            "sourceID": "dox",
            "attributes": {},
            "targetID": "commander",
            "size": 1
        },
        {
            "sourceID": "dox",
            "attributes": {},
            "targetID": "github-flavored-markdown",
            "size": 1
        },
        {
            "sourceID": "node-sass",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "node-sass",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "node-sass",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "gm",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "gm",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "node-log",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "node-log",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "component-builder",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "component-builder",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "component-builder",
            "attributes": {},
            "targetID": "fs-extra",
            "size": 1
        },
        {
            "sourceID": "component-builder",
            "attributes": {},
            "targetID": "batch",
            "size": 1
        },
        {
            "sourceID": "hyperquest",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "hyperquest",
            "attributes": {},
            "targetID": "duplexer",
            "size": 1
        },
        {
            "sourceID": "graphviz",
            "attributes": {},
            "targetID": "temp",
            "size": 1
        },
        {
            "sourceID": "levelup",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "levelup",
            "attributes": {},
            "targetID": "xtend",
            "size": 1
        },
        {
            "sourceID": "levelup",
            "attributes": {},
            "targetID": "concat-stream",
            "size": 1
        },
        {
            "sourceID": "msgpack-js",
            "attributes": {},
            "targetID": "bops",
            "size": 1
        },
        {
            "sourceID": "mincer",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "mincer",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "mincer",
            "attributes": {},
            "targetID": "argparse",
            "size": 1
        },
        {
            "sourceID": "mincer",
            "attributes": {},
            "targetID": "fs-tools",
            "size": 1
        },
        {
            "sourceID": "riak-js",
            "attributes": {},
            "targetID": "xml",
            "size": 1
        },
        {
            "sourceID": "contextify",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "level-sublevel",
            "attributes": {},
            "targetID": "xtend",
            "size": 1
        },
        {
            "sourceID": "tape",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "tape",
            "attributes": {},
            "targetID": "deep-equal",
            "size": 1
        },
        {
            "sourceID": "tape",
            "attributes": {},
            "targetID": "jsonify",
            "size": 1
        },
        {
            "sourceID": "elementtree",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "ftp",
            "attributes": {},
            "targetID": "xregexp",
            "size": 1
        },
        {
            "sourceID": "node-inspector",
            "attributes": {},
            "targetID": "socket.io",
            "size": 1
        },
        {
            "sourceID": "node-inspector",
            "attributes": {},
            "targetID": "connect",
            "size": 1
        },
        {
            "sourceID": "node-inspector",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "portscanner",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "burrito",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "burrito",
            "attributes": {},
            "targetID": "traverse",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "duplexer",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "buffers",
            "size": 1
        },
        {
            "sourceID": "trumpet",
            "attributes": {},
            "targetID": "ent",
            "size": 1
        },
        {
            "sourceID": "ref",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "ref",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "ref-struct",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "ref-struct",
            "attributes": {},
            "targetID": "ref",
            "size": 1
        },
        {
            "sourceID": "ffi",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "ffi",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "ffi",
            "attributes": {},
            "targetID": "ref",
            "size": 1
        },
        {
            "sourceID": "ffi",
            "attributes": {},
            "targetID": "ref-struct",
            "size": 1
        },
        {
            "sourceID": "scuttlebutt",
            "attributes": {},
            "targetID": "duplex",
            "size": 1
        },
        {
            "sourceID": "scuttlebutt",
            "attributes": {},
            "targetID": "monotonic-timestamp",
            "size": 1
        },
        {
            "sourceID": "form-data",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "form-data",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "js2coffee",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "js2coffee",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "js2coffee",
            "attributes": {},
            "targetID": "file",
            "size": 1
        },
        {
            "sourceID": "css",
            "attributes": {},
            "targetID": "css-parse",
            "size": 1
        },
        {
            "sourceID": "js-beautify",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "js-beautify",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "q-io",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "q-io",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "q-io",
            "attributes": {},
            "targetID": "qs",
            "size": 1
        },
        {
            "sourceID": "q-io",
            "attributes": {},
            "targetID": "collections",
            "size": 1
        },
        {
            "sourceID": "JSONPath",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "mochiscript",
            "attributes": {},
            "targetID": "watch",
            "size": 1
        },
        {
            "sourceID": "leveldown",
            "attributes": {},
            "targetID": "bindings",
            "size": 1
        },
        {
            "sourceID": "sync",
            "attributes": {},
            "targetID": "fibers",
            "size": 1
        },
        {
            "sourceID": "extended",
            "attributes": {},
            "targetID": "grunt",
            "size": 1
        },
        {
            "sourceID": "is-extended",
            "attributes": {},
            "targetID": "extended",
            "size": 1
        },
        {
            "sourceID": "array-extended",
            "attributes": {},
            "targetID": "grunt",
            "size": 1
        },
        {
            "sourceID": "array-extended",
            "attributes": {},
            "targetID": "grunt-contrib-jshint",
            "size": 1
        },
        {
            "sourceID": "array-extended",
            "attributes": {},
            "targetID": "grunt-contrib-uglify",
            "size": 1
        },
        {
            "sourceID": "array-extended",
            "attributes": {},
            "targetID": "extended",
            "size": 1
        },
        {
            "sourceID": "array-extended",
            "attributes": {},
            "targetID": "is-extended",
            "size": 1
        },
        {
            "sourceID": "stream-combiner",
            "attributes": {},
            "targetID": "duplexer",
            "size": 1
        },
        {
            "sourceID": "uglify-js2",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "uglify-js2",
            "attributes": {},
            "targetID": "source-map",
            "size": 1
        },
        {
            "sourceID": "upnode",
            "attributes": {},
            "targetID": "dnode",
            "size": 1
        },
        {
            "sourceID": "fstream-ignore",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "fstream-ignore",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "fstream-ignore",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "smoosh",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "smoosh",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "smoosh",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "smoosh",
            "attributes": {},
            "targetID": "jshint",
            "size": 1
        },
        {
            "sourceID": "smoosh",
            "attributes": {},
            "targetID": "sqwish",
            "size": 1
        },
        {
            "sourceID": "yui",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "difflet",
            "attributes": {},
            "targetID": "charm",
            "size": 1
        },
        {
            "sourceID": "difflet",
            "attributes": {},
            "targetID": "traverse",
            "size": 1
        },
        {
            "sourceID": "shoe",
            "attributes": {},
            "targetID": "sockjs",
            "size": 1
        },
        {
            "sourceID": "level",
            "attributes": {},
            "targetID": "levelup",
            "size": 1
        },
        {
            "sourceID": "level",
            "attributes": {},
            "targetID": "leveldown",
            "size": 1
        },
        {
            "sourceID": "markdown-js",
            "attributes": {},
            "targetID": "test",
            "size": 1
        },
        {
            "sourceID": "yamljs",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "yamljs",
            "attributes": {},
            "targetID": "argparse",
            "size": 1
        },
        {
            "sourceID": "passport-http",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-http",
            "attributes": {},
            "targetID": "passport",
            "size": 1
        },
        {
            "sourceID": "docparse-config",
            "attributes": {},
            "targetID": "temp",
            "size": 1
        },
        {
            "sourceID": "docparse-config",
            "attributes": {},
            "targetID": "nconf",
            "size": 1
        },
        {
            "sourceID": "seaport",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "seaport",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "seaport",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        },
        {
            "sourceID": "seaport",
            "attributes": {},
            "targetID": "through",
            "size": 1
        },
        {
            "sourceID": "seaport",
            "attributes": {},
            "targetID": "crdt",
            "size": 1
        },
        {
            "sourceID": "loggly-console-logger",
            "attributes": {},
            "targetID": "winston",
            "size": 1
        },
        {
            "sourceID": "apn",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "passport-google-oauth",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-google-oauth",
            "attributes": {},
            "targetID": "passport-oauth",
            "size": 1
        },
        {
            "sourceID": "forEachAsync",
            "attributes": {},
            "targetID": "sequence",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "express",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "graceful-fs",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "minimatch",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "node-markdown",
            "size": 1
        },
        {
            "sourceID": "yuidocjs",
            "attributes": {},
            "targetID": "yui",
            "size": 1
        },
        {
            "sourceID": "mongoose-types",
            "attributes": {},
            "targetID": "mongoose",
            "size": 1
        },
        {
            "sourceID": "funargs",
            "attributes": {},
            "targetID": "eyes",
            "size": 1
        },
        {
            "sourceID": "ender-bootstrap-base",
            "attributes": {},
            "targetID": "bean",
            "size": 1
        },
        {
            "sourceID": "ender-bootstrap-base",
            "attributes": {},
            "targetID": "bonzo",
            "size": 1
        },
        {
            "sourceID": "ender-bootstrap-base",
            "attributes": {},
            "targetID": "domready",
            "size": 1
        },
        {
            "sourceID": "ender-bootstrap-transition",
            "attributes": {},
            "targetID": "ender-bootstrap-base",
            "size": 1
        },
        {
            "sourceID": "engine.io-client",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "engine.io-client",
            "attributes": {},
            "targetID": "ws",
            "size": 1
        },
        {
            "sourceID": "engine.io-client",
            "attributes": {},
            "targetID": "xmlhttprequest",
            "size": 1
        },
        {
            "sourceID": "ldapjs",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "ldapjs",
            "attributes": {},
            "targetID": "bunyan",
            "size": 1
        },
        {
            "sourceID": "ldapjs",
            "attributes": {},
            "targetID": "buffertools",
            "size": 1
        },
        {
            "sourceID": "ldapjs",
            "attributes": {},
            "targetID": "assert-plus",
            "size": 1
        },
        {
            "sourceID": "ldapjs",
            "attributes": {},
            "targetID": "dtrace-provider",
            "size": 1
        },
        {
            "sourceID": "LiveScript",
            "attributes": {},
            "targetID": "prelude-ls",
            "size": 1
        },
        {
            "sourceID": "reconnect",
            "attributes": {},
            "targetID": "backoff",
            "size": 1
        },
        {
            "sourceID": "reconnect",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "reconnect",
            "attributes": {},
            "targetID": "shoe",
            "size": 1
        },
        {
            "sourceID": "exec-sync",
            "attributes": {},
            "targetID": "ffi",
            "size": 1
        },
        {
            "sourceID": "passport-facebook",
            "attributes": {},
            "targetID": "pkginfo",
            "size": 1
        },
        {
            "sourceID": "passport-facebook",
            "attributes": {},
            "targetID": "passport-oauth",
            "size": 1
        },
        {
            "sourceID": "update-notifier",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "update-notifier",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "update-notifier",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "fire",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "latest",
            "attributes": {},
            "targetID": "npm",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "cheerio",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "lodash",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "mkdirp",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "request",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "underscore.string",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "nopt",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "rimraf",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "tar",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "debug",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "cli-table",
            "size": 1
        },
        {
            "sourceID": "yeoman-generator",
            "attributes": {},
            "targetID": "diff",
            "size": 1
        },
        {
            "sourceID": "jsftp",
            "attributes": {},
            "targetID": "async",
            "size": 1
        },
        {
            "sourceID": "jsftp",
            "attributes": {},
            "targetID": "event-stream",
            "size": 1
        },
        {
            "sourceID": "xmlrpc",
            "attributes": {},
            "targetID": "sax",
            "size": 1
        },
        {
            "sourceID": "xmlrpc",
            "attributes": {},
            "targetID": "xmlbuilder",
            "size": 1
        },
        {
            "sourceID": "twit",
            "attributes": {},
            "targetID": "oauth",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-cssmin",
            "attributes": {},
            "targetID": "clean-css",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-cssmin",
            "attributes": {},
            "targetID": "grunt-lib-contrib",
            "size": 1
        },
        {
            "sourceID": "grunt-contrib-nodeunit",
            "attributes": {},
            "targetID": "nodeunit",
            "size": 1
        },
        {
            "sourceID": "grunt-lib-phantomjs",
            "attributes": {},
            "targetID": "semver",
            "size": 1
        },
        {
            "sourceID": "grunt-lib-phantomjs",
            "attributes": {},
            "targetID": "eventemitter2",
            "size": 1
        },
        {
            "sourceID": "grunt-lib-phantomjs",
            "attributes": {},
            "targetID": "temporary",
            "size": 1
        },
        {
            "sourceID": "grunt-lib-phantomjs",
            "attributes": {},
            "targetID": "phantomjs",
            "size": 1
        },
        {
            "sourceID": "joose",
            "attributes": {},
            "targetID": "temp",
            "size": 1
        },
        {
            "sourceID": "joose",
            "attributes": {},
            "targetID": "optimist",
            "size": 1
        },
        {
            "sourceID": "joose",
            "attributes": {},
            "targetID": "detective",
            "size": 1
        },
        {
            "sourceID": "iwebpp.io",
            "attributes": {},
            "targetID": "node-uuid",
            "size": 1
        },
        {
            "sourceID": "iwebpp.io",
            "attributes": {},
            "targetID": "msgpack-js",
            "size": 1
        },
        {
            "sourceID": "iwebpp.io",
            "attributes": {},
            "targetID": "siphash",
            "size": 1
        },
        {
            "sourceID": "jsgui-lang-essentials",
            "attributes": {},
            "targetID": "amdefine",
            "size": 1
        },
        {
            "sourceID": "logmimosa",
            "attributes": {},
            "targetID": "growl",
            "size": 1
        },
        {
            "sourceID": "logmimosa",
            "attributes": {},
            "targetID": "date-utils",
            "size": 1
        },
        {
            "sourceID": "logmimosa",
            "attributes": {},
            "targetID": "ansi-color",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "colors",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "sugar",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "chai",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "longjohn",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "sync",
            "size": 1
        },
        {
            "sourceID": "node-document-storage",
            "attributes": {},
            "targetID": "funargs",
            "size": 1
        },
        {
            "sourceID": "noflo",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "noflo",
            "attributes": {},
            "targetID": "npmlog",
            "size": 1
        },
        {
            "sourceID": "noflo",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "noflo",
            "attributes": {},
            "targetID": "cli-color",
            "size": 1
        },
        {
            "sourceID": "noflo",
            "attributes": {},
            "targetID": "cli",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "underscore",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "connect",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "mustache",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "mime",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "fstream",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "coffee-script",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "less",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "uglify-js",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "knox",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "marked",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "fresh",
            "size": 1
        },
        {
            "sourceID": "punch",
            "attributes": {},
            "targetID": "cssmin",
            "size": 1
        },
        {
            "sourceID": "joosex-namespace-depended",
            "attributes": {},
            "targetID": "joose",
            "size": 1
        },
        {
            "sourceID": "sourcemint-util-js",
            "attributes": {},
            "targetID": "q",
            "size": 1
        },
        {
            "sourceID": "sourcemint-util-js",
            "attributes": {},
            "targetID": "glob",
            "size": 1
        },
        {
            "sourceID": "sourcemint-util-js",
            "attributes": {},
            "targetID": "wrench",
            "size": 1
        },
        {
            "sourceID": "sourcemint-util-js",
            "attributes": {},
            "targetID": "tunnel",
            "size": 1
        },
        {
            "sourceID": "tower-directive",
            "attributes": {},
            "targetID": "tower-emitter",
            "size": 1
        },
        {
            "sourceID": "voxel",
            "attributes": {},
            "targetID": "inherits",
            "size": 1
        }
    ]
}

forcetrend_data = {
    "nodes": [
      {
        "id": "0",
        "name": "Myriel",
        "symbolSize": 19.12381,
        "x": 1,
        "y": 1,
        "value": 28.685715,
        "category": 0
      },
      {
        "id": "1",
        "name": "Napoleon",
        "symbolSize": 2.6666666666666665,
        "x": 2,
        "y": 2,
        "value": 4,
        "category": 0
      },
      {
        "id": "2",
        "name": "MlleBaptistine",
        "symbolSize": 6.323809333333333,
        "x": 2,
        "y": 3,
        "value": 9.485714,
        "category": 1
      },
      {
        "id": "3",
        "name": "MmeMagloire",
        "symbolSize": 6.323809333333333,
        "x": 3,
        "y": 6,
        "value": 9.485714,
        "category": 1
      }
    ],
    "edges": [
      {
        "source": "0",
        "target": "1"
      },
      {
        "source": "0",
        "target": "2"
      },
      {
        "source": "0",
        "target": "3"
      },
      {
        "source": "1",
        "target": "2"
      },
      {
        "source": "1",
        "target": "3"
      }
    ],
    "categories": [
      {
        "name": "类目0"
      },
      {
        "name": "类目1"
      }
    ]
  }


# 论文历年发文量
@router.get("/statArticlesByYear/{fileId}")
def statArticlesByYear(fileId):
    xList, yList = statManager.statArticlesByYear(fileId)
    return {'config': {'titleText': '论文历年发文量', 'xAxisName': '年', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'series': [{'type': 'line', 'data': yList}]}}


# 论文国别发文量
@router.get("/statArticlesByCountry/{fileId}")
def statArticlesByCountry(fileId):
    xList, yList = statManager.statArticlesByCountry(fileId)
    return {'config': {'titleText': '不同国家论文发文量', 'xAxisName': '国家', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'series': [{'type': 'bar', 'data': yList}]}}


# 论文地区发文量
@router.get("/statArticlesByProvince/{fileId}")
def statArticlesByProvince(fileId):
    return {}


# 论文机构发文量
@router.get("/statArticlesByOrg/{fileId}")
def statArticlesByOrg(fileId):
    return {}


# 一作累计发文量
@router.get("/statArticlesByFirstDuty/{fileId}")
def statArticlesByFirstDuty(fileId):
    xList, yList = statManager.statArticlesByFirstDuty(fileId)
    return {'config': {'titleText': '一作累计发文量', 'xAxisName': '作者', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 作者累计发文量
@router.get("/statArticlesByAuthor/{fileId}")
def statArticlesByAuthor(fileId):
    xList, yList = statManager.statArticlesByAuthor(fileId)
    return {'config': {'titleText': '作者累计发文量', 'xAxisName': '作者', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 期刊来源发文量
@router.get("/statArticlesByJournal/{fileId}")
def statArticlesByJournal(fileId):
    xList, yList = statManager.statArticlesByJournal(fileId)
    return {'config': {'titleText': '期刊来源发文量', 'xAxisName': '出版物', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 基金支持历年统计
@router.get('/statArticlesByFund/{fileId}')
def statArticlesByFund(fileId):
    xList, yList = statManager.statArticlesByFund(fileId)
    return {'config': {'titleText': '基金支持发文量', 'xAxisName': '年份', 'yAxisName': '发文量(篇)'},
            'data': {'xData': xList, 'yData': yList}}


# 基金类型统计
@router.get('/statStyleByFund/{fileId}')
def statStyleByFund(fileId):
    xList, yList = statManager.statStyleByFund(fileId)
    return {'config': {'titleText': '基金类型', 'xAxisName': '基金', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}


# 学科分布统计
@router.get('/statArticlesBySubject/{fileId}')
def statArticlesBySubject(fileId):
    xList, yList = statManager.statArticlesBySubject(fileId)
    return {'config': {'titleText': '学科分布'}, 'data': {'xData': [], 'yData': []}}


# 合著人数统计
@router.get('/statPersonsByCoAuthor/{fileId}')
def statPersonsByCoAuthor(fileId):
    xList, yList = statManager.statPersonsByCoAuthor(fileId)
    return {'config': {'titleText': '合著人数', 'xAxisName': '人数', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}


# 关键词词频统计
@router.get('/statKwsByCount/{fileId}')
def statKwsByCount(fileId):
    xList, yList = statManager.statKwsByCount(fileId)
    return {'config': {'titleText': '关键词词频统计', 'xAxisName': '关键词', 'yAxisName': '数量'},
            'data': {'xData': xList, 'yData': yList}}


# 关键词词云
@router.get("/wordcloud/keyword/{fileId}")
def wordcloud_keyword(fileId):
    return {}


# 关键词共现矩阵
@router.get("/coocMatrix/keyword/{fileId}")
def coocmatrix_keyword(fileId):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}


# 主题词共现矩阵
@router.get("/coocMatrix/topicword/{fileId}")
def coocmatrix_topicword(fileId):
    return {}


# 共现关键词散点图
@router.get("/scatter/coockeyword/{fileId}")
def scatter_coockeyword(fileId):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': points}}


# 关键词层级聚类
@router.get("/cluster/hierarchy/keyword/{fileId}")
def cluster_hierarchy_keyword(fileId):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': forcetrend_data}}


# 关键词谱聚类
@router.get("/cluster/spectral/keyword/{fileId}")
def cluster_spectral_keyword(fileId):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': force_data}}

# 关键词趋势聚类
@router.get("/cluster/trend/keyword/{fileId}")
def cluster_trend_keyword(fileId):
    xData = cooc_matrix_data[0][1:]
    yData = [x[0] for x in cooc_matrix_data[1:]]

    value = cooc_matrix_data[1:]
    value = [x[1:] for x in value]
    points = []
    for row in range(len(value)):
        for col in range(len(value[0])):
            points.append([int(row), int(col), int(value[row][col]) if int(value[row][col]) else '-'])

    return {'config': {'titleText': '', 'xAxisName': '', 'yAxisName': ''},
            'data': {'xData': xData, 'yData': yData, 'value': forcetrend_data}}



# 知识图谱
@router.get("/{userId}/{fileId}/{count}")
def kg(userId, fileId, count: int = 10):
    kg = statManager.kg(userId, fileId, count)
    return kg
