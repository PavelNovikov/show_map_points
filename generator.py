#!/usr/bin/env python

def addresses_to_json(addresses):
    return '[%s]' % ',\n'.join(map(lambda x: '"%s"' % x, addresses))

def main():
    with open('apikey.txt','r') as apikey_file,\
        open('base.html','r') as base_html_file,\
        open('addresses.txt','r') as addresses_file,\
        open('index.html','w') as result:
        apikey = apikey_file.read()
        html_text = base_html_file.read()
        addresses = addresses_to_json(addresses_file.read()
                    .replace('\\','\\\\')
                    .replace('"','\\"')
                    .split('\n'))

        html_text = (html_text
                    .replace('>>apikey<<', apikey)
                    .replace('>>addresses<<', addresses))
        result.write(html_text)


if __name__ == "__main__":
    main()
