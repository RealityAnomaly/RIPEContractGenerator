import pylatex as pl
from pylatex.utils import bold, italic


def gen_party(party):
    cnt = []
    cnt.append(party['name'])
    for line in party['address']:
        cnt.append(line)
    cnt.append(party['country'])

    cnt.append('')

    if 'regno' in party:
        cnt.append('Registered with ' + party['authority'] + ', ' + party['regno'])
    if 'orgid' in party:
        cnt.append('RIPE OrgID: ' + party['orgid'])

    return '\n'.join(cnt)


def gen_party_flat(party, designation):
    cnt = []
    cnt.append(f'{bold(party["name"])}, with registered offices at ' + bold(', '.join(party["address"])) + ', ' + bold(party['country']))
    if 'regno' in party:
        cnt.append(f'registered with {bold(party["authority"])}; {bold(party["regno"])}')
    if 'email' in party:
        cnt.append(f'with the email address {bold(party["email"])}')
    cnt.append(f'hereinafter "{bold(designation)}"')
    return ', '.join(cnt)


def _gen_sigblock_int(party):
    cnt = []
    if 'person' in party:
        cnt.append(f"{party['person']['name']} & Place & Date \\\\")
        cnt.append(f"{party['person']['role']}, {party['name']} \\\\")
    else:
        cnt.append(f"{party['name']} & Place & Date \\\\")

    if 'type' in party:
        cnt.append(party['type'])

    return '\n'.join(cnt)


def append_sigblock(doc, first, second):
    doc.append(pl.NoEscape(r'''
    \noindent
    \begin{tabular}{@{}p{2.2in}p{1.3in}p{1.3in}@{}}
    \\[2\bigskipamount]
    \dotfill & \dotfill & \dotfill \\''' + _gen_sigblock_int(first) +
    r'''\\[2\bigskipamount]
    \hrulefill & \hrulefill & \hrulefill \\''' + _gen_sigblock_int(second) +
    r'''\end{tabular}'''))
