import re
with open('adorableshots_proposal.html', 'r') as f:
    content = f.read()
content = content.replace('<meta charset="UTF-8" />', '<meta charset="UTF-8" />\n  <link rel="icon" type="image/png" href="bsa_logo.png" />')
content = re.sub(r'https://wa\.me/[\w+]+', 'https://wa.me/916282434535', content)
content = re.sub(r'https://api\.whatsapp\.com/send\?phone=[\w+]+', 'https://api.whatsapp.com/send?phone=916282434535', content)
with open('adorableshots_proposal.html', 'w') as f:
    f.write(content)
print('Done! Favicon and WhatsApp links updated.')
