emot = ':@'

def main():
    global emot
    falar("qm é vc")
    emot = ':D'
    falar("aaaah e vc")
    
def falar(qualquer_fita):
    print(qualquer_fita + " " + emot)
    
main()