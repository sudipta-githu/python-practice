letter = ''' Dear <|name|>,
            you are selected!
            <|Date|>'''

print(letter.replace("<|name|>", "sudipta").replace("<|Date|>", "21 may 2026"))