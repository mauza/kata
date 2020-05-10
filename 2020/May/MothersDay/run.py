import time
import utils as u

me = '8018217046@msg.fi.google.com'
lori = '8013108931@vtext.com'

HOUR = 3600
MINUTE = 60

def main():
    time.sleep(5*MINUTE)
    u.send_text('It has started', [me])
    print('It has started')
    # Initial message
    u.send_text('Incoming messages! for security they will be obfuscated ask your husband for translation.', [lori])
    time.sleep(HOUR)

    u.send_text('Massage Time', [me])
    print('Massage Time')
    time.sleep(5*MINUTE)
    # Massage
    u.send_text('Maybe Marshmallow?', [lori])
    time.sleep(1.1*HOUR)

    u.send_text('Say nice things', [me])
    print('Say nice things')
    time.sleep(5*MINUTE)
    # Activity where we all say nice things about her
    u.send_text('Oranges, lots of oranges', [lori])
    time.sleep(1.2*HOUR)

    u.send_text('Give Lori alone time', [me])
    print('Give Lori alone time')
    time.sleep(5*MINUTE)
    # Time alone
    u.send_text('Emergency!', [lori])
    time.sleep(1.3*HOUR)

    u.send_text('Ask her what we should clean', [me])
    print('Ask her what we should clean')
    time.sleep(5*MINUTE)
    # Clean something
    u.send_text('The eagle flies high this time of day', [lori])
    time.sleep(1.1*HOUR)

    u.send_text('We write/draw in our book all together', [me])
    print('We write/draw in our book all together')
    time.sleep(5*MINUTE)
    # We all write/draw something we love in our book
    u.send_text('The records are incomplete!', [lori])
    time.sleep(1.5*HOUR)

    u.send_text('Snuggle with everyone', [me])
    print('Snuggle with everyone')
    time.sleep(5*MINUTE)
    # Snuggle time
    u.send_text('The bears are in the woods', [lori])
    time.sleep(1.5*HOUR)

    # I love you
    u.send_text('I love you', [lori])
    print('fin')

if __name__ == '__main__':
    main()