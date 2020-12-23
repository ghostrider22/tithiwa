import os

from selenium.webdriver.common.by import By

MODULEDIR = os.path.dirname(__file__)
SESSIONDIR = os.path.join(MODULEDIR, 'sessions')

DEFAULT_SHOULD_OUTPUT = True


class SELECTORS(object):
    MAIN_SEARCH_BAR = (By.CSS_SELECTOR, 'div[dir="ltr"]')
    MAIN_SEARCH_BAR_DONE = (By.CSS_SELECTOR, '[data-testid="x-alt"]')
    MAIN_SEARCH_BAR_SEARCH_ICON = (By.CSS_SELECTOR, '[data-testid="search"]')
    MAIN_SEARCH_BAR_BACK_ARROW = (By.CSS_SELECTOR, '[data-testid="search"]')
    MESSAGE_INPUT_BOX = (By.CSS_SELECTOR, '#main footer ._3FRCZ')
    TURN_ON_DESKTOP_NOTIFICATIONS = (By.CSS_SELECTOR, '.zKq5Y')
    CLOSE_INFO = (By.CSS_SELECTOR, '[data-testid="x-alt"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '.t4a8o')
    NAME_AND_ABOUT = (By.CSS_SELECTOR, '._2FVVk._3WjMU')
    MAIN_MENU_OPTIONS__MENU_ICON = (By.CSS_SELECTOR, '[data-testid=menu]')
    MAIN_MENU_OPTIONS__NEW_GROUP = (By.CSS_SELECTOR, '[title="New group"]')
    MAIN_MENU_OPTIONS__SETTINGS = (By.CSS_SELECTOR, '[title="Settings"]')
    CREATE_NEW_GROUP__TYPE_CONTACTS_INPUT_BOX = (By.CSS_SELECTOR, '._17ePo')
    CREATE_NEW_GROUP__RESULT_CONTACT = (By.CSS_SELECTOR, '._210SC')
    CREATE_NEW_GROUP__OK_CONTACTS_TYPE = (By.CSS_SELECTOR, '[data-testid="arrow-forward"]')
    CREATE_NEW_GROUP__TYPE_GROUP_NAME = (By.CSS_SELECTOR, '._1Rerq ._3FRCZ')
    CREATE_NEW_GROUP__OK_GROUP_NAME_TYPE = (By.CSS_SELECTOR, '._3y5oW')
    CREATE_NEW_GROUP__ENCRYPTED_LOCK_SIGN = (By.CSS_SELECTOR, '._2VO5X')
    CHATROOM__NAME_AND_INFO = (By.CSS_SELECTOR, '._33QME')
    CHATROOM__NAME = (By.CSS_SELECTOR, '.DP7CM')
    CHATROOM__INFO = (By.CSS_SELECTOR, '._3-cMa._3Whw5')
    CHATROOM__INFO_NUMBER = (By.CSS_SELECTOR, '._3Whw5 > ._1X4JR')
    CHATROOM__CLOSE_INFO = (By.CSS_SELECTOR, '[data-testid="x"]')
    CHATROOM__OPTIONS = (By.CSS_SELECTOR, '[data-testid="menu"]')
    CHATROOM__INFO_DELETE_CHAT = (By.CSS_SELECTOR, '._1OwwW ._3oTCZ[title="Delete chat"]')
    CHATROOM__DELETE_CHAT = (By.CSS_SELECTOR, '._30EVj .gMRg5')
    CONTACTS__NAME_IN_CHATS = (By.CSS_SELECTOR, '._357i8 > ._3ko75._5h6Y_._3Whw5')
    GROUPS__MEMBERS_SEARCH_ICON = (By.CSS_SELECTOR, '._3lS1C')
    GROUPS__SEARCH_CONTACTS_INPUT_BOX = (By.CSS_SELECTOR, '._9a59P ._3FRCZ')
    GROUPS__CONTACTS_SEARCH_NAME = (By.CSS_SELECTOR, '._3ko75')
    GROUPS__CLOSE_CONTACTS_SEARCH = (By.CSS_SELECTOR, '._2HE5l .t4a8o')
    GROUPS__ADMIN_ICON = (By.CSS_SELECTOR, '.LwCwJ')
    GROUPS__MAKE_ADMIN = (By.CSS_SELECTOR, '.Ut_N0')
    GROUPS__REMOVE_ADMIN = (By.CSS_SELECTOR, '._1OwwW ._3oTCZ[title="Dismiss as admin"]')
    GROUPS__REMOVE = (By.CSS_SELECTOR, 'div[title="Remove"]')
    GROUPS__EXIT_FROM_GROUP = (By.CSS_SELECTOR, '._3wAoe._3DSZk[title="Exit group"]')
    GROUPS__EXIT_DIALOG_BOX = (By.CSS_SELECTOR, '._9a59P')
    GROUPS__EXIT_BUTTON_EXIT_DIALOG_BOX = (By.CSS_SELECTOR, '.S7_rT.FV2Qy')
    GROUPS__NO_LONGER_A_PARTICIPANT = (By.CSS_SELECTOR, '._3ge3i')
    GROUPS__NAME_IN_CHATS = (By.CSS_SELECTOR, '._3CneP > ._3ko75._5h6Y_._3Whw5')
    SETTINGS__OK_BUTTON = (By.CSS_SELECTOR, '.S7_rT.FV2Qy')
    SETTINGS__THEME = (By.CSS_SELECTOR, 'div[title="Theme"]')
    SETTINGS__NOTIFICATIONS = (By.CSS_SELECTOR, 'div[title="Notifications"]')
    SETTINGS__BLOCKED = (By.CSS_SELECTOR, 'div[title="Blocked"]')
    SETTINGS__ADD_BLOCKED_CONTACT = (By.CSS_SELECTOR, 'div[title="Add blocked contact"]')
    SETTINGS__NOTIFICATIONS_OPTIONS = (By.CSS_SELECTOR, '._2XWkx')
    SETTINGS__NOTIFICATIONS_TURN_OFF_OPTIONS = (By.CSS_SELECTOR, '._1OFu5')
    SETTINGS__NOTIFICATIONS_MUTE_OR_UNMUTE = (By.CSS_SELECTOR, '.S7_rT.FV2Qy')
    SETTINGS__PROFILE = (By.CSS_SELECTOR, '._1V82l')


class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'
    THEME_LIGHT = 'light'
    THEME_DARK = 'dark'
    THEME_SYSTEM = 'system'


class INTEGERS(object):
    TURN_OFF_NOTIFICATIONS_FOR_8_HOURS = 0
    TURN_OFF_NOTIFICATIONS_FOR_1_WEEK = 1
    TURN_OFF_NOTIFICATIONS_FOR_ALWAYS = 2
    DEFAULT_WAIT = 144


_SETUP_SESSION = '''
window.indexedDB = window.indexedDB || window.mozIndexedDB ||
    window.webkitIndexedDB || window.msIndexedDB; 
window.IDBTransaction = window.IDBTransaction ||
    window.webkitIDBTransaction || window.msIDBTransaction;
window.IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange ||
    window.msIDBKeyRange
if (!window.indexedDB) {
    window.alert("Your browser doesn't support a stable version of IndexedDB.")
}
var db = await new Promise((resolve, reject) => {
    var request = window.indexedDB.open("wawc");
    request.onerror = function(event) {
        console.log(event);
        resolve(0);
    };

    request.onsuccess = function(event) {
        resolve(request.result);
    };

    request.onupgradeneeded = function(event) {
        resolve(event.target.result)
    }

});
'''

GET_SESSION = _SETUP_SESSION + '''
function readAll() {
    return new Promise((resolve, reject) => {
        res = [];
        var objectStore = db.transaction("user").objectStore("user");
        objectStore.openCursor().onsuccess = function(event) {
            var cursor = event.target.result;
            if (cursor) {
                res.push(cursor.value);
                cursor.continue();
            } else {
                resolve(res);
            }
        };
    });
}
session = await readAll();
res = "";
for (i in session) {
    res += session[i].key + "\\nnavi" + session[i].value + "\\nnavi";
}
return res;
'''

PUT_SESSION = _SETUP_SESSION + '''
localStorage.clear();
await new Promise((resolve, reject) => {
   var request = db.transaction(["user"], "readwrite")
   .objectStore("user")
   .clear();
   request.onsuccess = function(event) {
      resolve(1);
   };
});
function add(key, value) {
    return new Promise((resolve, reject) => {
        var request = db.transaction(["user"], "readwrite")
            .objectStore("user")
            .add({
                key: key,
                value: value
            });
        request.onsuccess = function(event) {
            resolve(0);
        };
        request.onerror = function(event) {
            resolve(1);
        }
    });
}
a = arguments[0].split("\\nnavi");
for (i = 0; i < a.length; i += 2) {
    await add(a[i], a[i + 1]);
}
'''
