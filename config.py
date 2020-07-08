import json

DEBUG = True
DEBUG = False
SHOW_DATA = True

DIR_ROOT = './'
DIR_BUILD_INDEX = f"{DIR_ROOT}"
DIR_BUILD_MODEL = f"{DIR_ROOT}html/"

DIR_ICONS = './simple-icons/'

# algo:
#
# a = glob.glob(DIR_ICONS)
# b = [re.split("[/\.]+", item)[-2] for item in a]
# print(b)

SOFTWARE = ['pandas', 'linkedin', 'deviantart', 'tor', 'gnuicecat', 'imdb',
        'concourse', 'inkscape', 'apacheopenoffice', 'origin', 'slashdot',
        'semanticweb', 'git', 'ubuntu', 'json', 'php', 'readthedocs',
        'bandcamp', 'xmpp', 'mastodon', 'bitbucket', 'gitter', 'arduino',
        'docker', 'steam', 'wikipedia', 'linux', 'postgresql', 'launchpad',
        'javascript', 'amd', 'scribd', 'letsencrypt', 'nginx', 'diaspora',
        'gravatar', 'rubyonrails', 'github', 'stylus', 'opengl', 'jsfiddle',
        'coveralls', 'adblock', 'composer', 'html5', 'mysql', 'firefox',
        'bitcoin', 'vimeo', 'travisci', 'gimp', 'django', 'disqus',
        'buymeacoffee', 'libreoffice', 'kotlin', 'repl-dot-it', 'vue-dot-js',
        'adblockplus', 'xfce', 'lua', 'fedora', 'fiverr', 'livejournal',
        'gitlab', 'pypi', 'svg', 'simpleicons', 'blender', 'creativecommons',
        'musescore', 'vlcmediaplayer', 'x-dot-org', 'freedesktop-dot-org',
        'codewars', 'jupyter', 'material-ui', 'freebsd', 'linode',
        'apacheecharts', 'pepsi', 'flathub', 'android', 'kde', 'python',
        'angular', 'superuser', 'openbadges', 'openapiinitiative', 'mozilla',
        'unity', 'flask', 'firefoxbrowser', 'jquery', 'node-dot-js',
        'gnuprivacyguard', 'apacheant', 'lubuntu', 'imgur', 'curl',
        'last-dot-fm', 'pastebin', 'snapcraft', 'atlassian', 'cmake', 'twitch',
        'eslint', 'instagram', 'nintendo', 'gnu', 'jenkins',
        'apachenetbeanside', 'w3c', 'alpinelinux', 'obsstudio', 'awesomewm',
        'haskell', 'openbsd', 'spacemacs', 'sega', 'leaflet', 'ghost',
        'goodreads', 'eclipseide', 'hackaday', 'rust', 'joomla', 'sass',
        'myspace', 'wikimediacommons', 'latex', 'd3-dot-js', 'vim',
        'soundcloud', 'apachecordova', 'awesomelists', 'reddit',
        'themoviedatabase', 'delicious', 'manjaro', 'uikit', 'tripadvisor',
        'androidstudio', 'wolfram', 'jabber', 'rss', 'stackexchange',
        'openssl', 'sqlite', 'duolingo', 'mongodb', 'apache', 'openid', 'hexo',
        'wechat', 'ublockorigin', 'nvidia', 'kubernetes', 'protocols-dot-io',
        'sourceforge', 'elm', 'ardour', 'linuxfoundation', 'digg',
        'opensourceinitiative', 'rstudio', 'webcomponents-dot-org', 'gnubash',
        'coffeescript', 'qt', 'wordpress', 'lmms', 'krita', 'khanacademy',
        'ted', 'discourse', 'webassembly', 'stackoverflow', 'debian',
        'iconify', 'opensuse', 'gnuemacs', 'googlechrome', 'gnusocial',
        'serverfault', 'crunchbase', 'intel', 'freecodecamp', 'opencollective',
        'openvpn', 'postwoman', 'signal', 'r', 'pokemon', 'valve', 'happycow',
        'spotify', 'c', 'atari', 'archlinux', 'webrtc', 'tunein', 'anaconda',
        'tumblr', 'centos', 'drupal', 'apacheflink', 'electron', 'atom',
        'mixcloud', 'gnome', 'asciinema', 'xdadevelopers', 'css3',
        'raspberrypi', 'perl']

with open('simple-icons.json', 'r') as data:
    ICON_DATA = json.load(data)
