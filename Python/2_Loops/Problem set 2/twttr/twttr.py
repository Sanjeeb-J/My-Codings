# The input
def main():
    word = omit(input("Input: "))
    print(word)
# Omit a,e,i,o,u
def omit(d):
    d = d.replace("a", "")
    d = d.replace("e", "")
    d = d.replace("i", "")
    d = d.replace("o", "")
    d = d.replace("u", "")
    d = d.replace("O", "")
    return d
# Out put (without a,e,i,o,u)
main()
