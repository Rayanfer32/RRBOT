import os

TOKEN = os.environ.get("TELEGRAM_API_TOKEN")

ENABLED_USERS = os.environ.get("ENABLED_USERS", '1024316776,628650705')
ENABLED_USERS = set(int(e.strip()) for e in ENABLED_USERS.split(','))

PING_SERVERS = ["www.google.com",
"www.whatsapp.com",
"www.bing.com",
"www.facebook.com",
'8.8.8.8',
'8.8.4.4',
"1.1.1.1",
"meet.google.com",
'www.instagram.com',
'www.youtube.com',
'www.speedtest.net',
'www.fast.com',
'www.microsoft.com',
"www.cloudflare.com",
'www.gmail.com',
'www.fast.com',
"www.yahoo.com",
"www.amazon.com",
"www.cisco.com",
"www.robosoftin.com",
"www.spotify.com",
"www.flipkart.com",
"www.wikipedia.org",
"www.hotstar.com",
"www.sophos.com",
]

# Alert if greater than threshold
LATENCY_ALERT = 100
PACKETLOSS_ALERT = 7

CMD_WHITE_LIST = {}
CMD_BLACK_LIST = {'rm'}
CMD_BLACK_CHARS = {';', '\n'}
ONLY_SHORTCUT_CMD = False

MAX_TASK_OUTPUT = int(os.environ.get("MAX_TASK_OUTPUT", 5000))

PROXY_URL = os.environ.get("ALL_PROXY", '')

SC_MENU_ITEM_ROWS = (
    (
        ('temp','/opt/vc/bin/vcgencmd measure_temp'),
        ('pingg','oa;fping -l -t100 www.google.com'),   
        ('fast-bin','oa;fast-bin'),
        # ('deenet','oa;speedtest-cli --server 16512'),
    ),
    (
        # ('speedgo','oa;/home/pi/./speedtest-go --server 7379'),
        # ('speedtestt','oa;speedtest-cli --server 7379'),
        ('fast-arm','oa;fast-arm'),
        ('cloudtest','oa;npx speed-cloudflare-cli'),
        ('speed-airtel','oa;speedtest -s 19081'),
        ('speed-tata','oa;speedtest -s 23647'),
        
        # ('Demo Script', 'demo.py', True),
    ),
    (
      ('speed-deenet','oa;speedtest -s 16512'),
      ('speed-act','oa;speedtest -s 7379'),
    ),
)

SC_MENU_ITEM_CMDS = {}
for row in SC_MENU_ITEM_ROWS:
    for cmd in row:
        SC_MENU_ITEM_CMDS[cmd[1]] = cmd

REQUEST_KWARGS = {
    'proxy_url': PROXY_URL
}

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPTS_ROOT_PATH = os.path.join(ROOT_PATH, 'scripts')