import sys, os
import ConfigParser
import traceback
import inspect
import lang

config_defaults = {
    ("tor", "tor_server") : "127.0.0.1",
    ("tor", "tor_server_socks_port") : 9050,
    ("tor", "tor_server_control_port") : 9051,
    ("tor_portable", "tor_server") : "127.0.0.1",
    ("tor_portable", "tor_server_socks_port") : 11109,
    ("tor_portable", "tor_server_control_port") : 11119,
    ("client", "own_hostname") : "0000000000000000",
    ("client", "listen_interface") : "127.0.0.1",
    ("client", "listen_port") : 11009,
    ("logging", "log_file") : "",
    ("logging", "log_level") : 0,
    ("gui", "language") : "en",
    ("gui", "notification_popup") : 1,
    ("gui", "notification_flash_window") : 1,
    ("gui", "open_main_window_hidden") : 0,
    ("gui", "open_chat_window_hidden") : 0,
    ("gui", "time_stamp_format") : "(%H:%M:%S)",
}

ICON_DIR = "icons" #can be absolute or relative to script dir

AUTHORS_ID = "utvrla6mjdypbyw6"
AUTHORS_NAME = "Bernd"

def getScriptDir():
    #must be called at least once before working dir is changed
    #because after that abspath won't work correctly anymore.
    #this is the reason why this function uses a cache.
    global _script_dir
    try:
        return _script_dir
    except:
        #first call, _script_dir not yet defined
        _script_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        return _script_dir

def isPortable():
    #if the file portable.txt exists in the same directory
    #then we know that we are running in portable mode.
    dir = getScriptDir()
    try:
        f = open(os.path.join(dir, "portable.txt"), "r")
        f.close()
        return True
    except:
        return False
    
def getDataDir():
    if isPortable():
        data_dir = getScriptDir()
    else:
        if "win" in sys.platform:
            appdata = os.environ["APPDATA"]
            data_dir = os.path.join(appdata, "torchat")
        else:
            home = os.path.expanduser("~")
            data_dir = os.path.join(home, ".torchat")
    
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        
    return data_dir

def readConfig():
    global file_name
    global config
    dir = getDataDir()
    if not os.path.isdir(dir):
        os.mkdir(dir)        
    file_name = dir + "/torchat.ini"
    config = ConfigParser.ConfigParser()
    config.read(file_name)
    #try to read all known options once. This will add 
    #all the missing options to the config file 
    for section, option in config_defaults:
        get(section, option)
    
def writeConfig():
    fp = open(file_name, "w")
    config.write(fp)
    fp.close()

def get(section, option):
    if not config.has_section(section):
        config.add_section(section)
    if not config.has_option(section, option):
        value = config_defaults[section, option]
        set(section, option, value)
    return config.get(section, option, True)

def getint(section, option):
    value = get(section, option)
    try:
        return int(value)
    except:
        return 0

def set(section, option, value):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    writeConfig()

def tb(level=0):
    print "(%i) ----- start traceback -----\n%s   ----- end traceback -----\n" % (level, traceback.format_exc())

def importLanguage():
    lang_xx = "lang_" + get("gui", "language")
    if lang_xx == "lang_en":
        #this is the standard. nothing to replace.
        return
    
    print "(1) trying to import language module %s.py" % lang_xx
    try:
        #this will replace all strings in lang which have a translation 
        #in lang_xx by replacing the bindings in lang's namespace at runtime
        dict_std = lang.__dict__
        dict_trans = __import__(lang_xx).__dict__
        for key in dict_trans.keys():
            dict_std[key] = dict_trans[key]
    except:
        print "(0) language module %s.py not found" % lang_xx


class LogWriter:
    def __init__(self):
        old_dir = os.getcwd()
        os.chdir(getDataDir())
        #if log_file is a relative path then let it be relative to DataDir()
        self.file_name = os.path.abspath(get("logging", "log_file"))
        os.chdir(old_dir)
        self.stdout = sys.stdout
        sys.stdout = self
        sys.stderr = self
        self.level = getint("logging", "log_level")
        if  self.level and self.file_name:
            try:
                self.logfile = open(self.file_name, 'w')
                print "(1) started logging to file '%s'" % self.file_name
            except:
                tb(0)
                print "(0) could not open logfile '%s'" % self.file_name
                print "(0) logging only to stdout"
        print "(1) current log level is %i" % self.level
        print "(1) LogWriter initialized"

    def write(self, text):
        text = text.rstrip()
        if text == "":        #dict is the __dict__ of the standard lang module
        #dict_trans is the __dict__ of the translation

            return
        text += "\n"
        try:
            x = text[0]
            y = text[2]
            if x == "(" and y == ")":
                level = int(text[1])
            else:
                text = "(0) " + text
                level = 0
        except:
            text = "(0) " + text
            level = 0

        if level <= self.level:
            try:
                frame = inspect.getframeinfo(inspect.currentframe(1))
                module = os.path.basename(frame[0])
                line = frame[1]
                func = frame[2]
                pos = "%s line %i in %s -" % (module, line, func)
                text = text[0:4] + pos + text[3:]
            except:
                pass
            self.stdout.write(text)
            self.stdout.flush()
            try:
                self.logfile.write(text)
                self.logfile.flush()
            except:
                pass

    def close(self):
        self.stdout.close()
        self.logfile.close()

#many things are relative to the script directory, so set is as the cwd
os.chdir(getScriptDir())
readConfig()
log_writer = LogWriter()
importLanguage()
