import time
import utils as u

me = '8018217046@msg.fi.google.com'
lori = '8018217046@msg.fi.google.com' # for testing
#lori = '8013108931@vtext.com'

HOUR = 3600
MINUTE = 60

def main():
    time.sleep(5*MINUTE)
    u.send_message('It has started', [me])
    # Initial message
    u.send_message('Incoming messages! for security they will be obfuscated ask your husband for translation.', [lori])
    time.sleep(22*MINUTE)

    u.send_message('Massage Time', [me])
    time.sleep(5*MINUTE)
    # Massage
    u.send_message('Maybe Marshmallow?', [lori])
    time.sleep(HOUR)

    u.send_message('Say nice things', [me])
    time.sleep(5*MINUTE)
    # Activity where we all say nice things about her
    u.send_message('Oranges, lots of oranges', [lori])
    time.sleep(50*MINUTE)

    u.send_message('Give Lori alone time', [me])
    time.sleep(5*MINUTE)
    # Time alone
    u.send_message('Emergency!', [lori])
    time.sleep(70*MINUTE)

    u.send_message('Ask her what we should clean', [me])
    time.sleep(5*MINUTE)
    # Clean something
    u.send_message('The eagle flies high this time of day', [lori])
    time.sleep(45*MINUTE)

    u.send_message('We write/draw in our book all together', [me])
    time.sleep(5*MINUTE)
    # We all write/draw something we love in our book
    u.send_message('The records are incomplete!', [lori])
    time.sleep(2*HOUR)

    u.send_message('Snuggle with everyone', [me])
    time.sleep(5*MINUTE)
    # Snuggle time
    u.send_message('The bears are in the woods', [lori])
    time.sleep(90*MINUTE)

    # I love you
    u.send_message('I love you', [lori])

if __name__ == '__main__':
    main()