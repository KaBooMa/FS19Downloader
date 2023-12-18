import requests, os

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'cdn20.giants-software.com',
    'Referer': 'https://www.farming-simulator.com/'
}

link = input('Please enter the mods URL:')

mod_links = []

res = requests.get(link)
html = res.text.split('\n')
for line in html:
    if 'mod.php?mod_id' in line:
        mod_link = line.split('"')[1]
        mod_links.append(f'https://www.farming-simulator.com/{mod_link}')

print(f'Total mods found: {len(mod_links)}. Proceeding to download...')

if not os.path.exists('mods'):
    os.makedirs('mods')

counter = 0
for link in mod_links:
    counter += 1
    print(f'Download mod {counter} of {len(mod_links)}')
    res = requests.get(link)
    html = res.text.split('\n')

    for line in html:
        if line.find('>DOWNLOAD<') > 0:
            direct_link = line.split('"')[1]
            file_name = direct_link.split('/')[6]
            mod_file = requests.get(direct_link, headers=headers)
            with open(f'mods/{file_name}', 'wb') as file:
                file.write(mod_file.content)
