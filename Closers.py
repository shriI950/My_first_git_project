

def outerFunction(tag):
    def innerFunction(content):
        print(f'<{tag}>{content}</{tag}>')
    return innerFunction

header = outerFunction('h1')
p = outerFunction('p')

header("This is a h1 header.")
p("This is a paragraph.")
print("New Features")