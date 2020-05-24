import pylatex as pl
import argparse
import json
import os
from . import genlib


def generate(data, doc):
    parties = data['parties']
    resources = data['resources']
    
    doc.append(pl.Center(data=pl.LargeText('RIPE NCC Resource Transfer Agreement')))
    doc.append(pl.NoEscape(r"\hrule height .1mm"))
    doc.append(pl.NoEscape(r"\vspace{.5cm}"))

    doc.append(pl.utils.bold(genlib.gen_party(parties['offering'])))
    doc.append('\n(Offering Party)')

    doc.append('\n\nAnd:\n\n')
    doc.append(pl.utils.bold(genlib.gen_party(parties['recieving'])))
    doc.append('\n(Recieving Party)\n\n')

    doc.append('Jointly mentioned as "Both Parties"\n\nWhereas\n\n')
    doc.append('I. Both Parties have entered into either a Standard Service Agreement with the RIPE NCC or an End User Assignment Agreement with a sponsoring LIR (both or either agreement hereafter referred to as "Basic Agreement")\n\n')
    doc.append('II. The Offering Party has requested the registration of Internet number resources from the RIPE NCC and the RIPE NCC has registered Internet number resources to the Offering Party including the resources listed below (hereafter referred to as "Internet Number Resources"):\n\n')

    # table here
    with doc.create(pl.Tabular('| p{6cm} | p{4cm} |')) as table:
        table.add_hline()
        table.add_row(("Resource", "Type"))
        table.add_hline()

        for r in resources:
            table.add_row((r['content'], r['type']))
            table.add_hline()

    doc.append('\n\n')

    doc.append('''
    III. Both Parties have agreed to transfer the registration of the Internet Number Resources from the Offering Party to the Receiving Party.

    IV. The Receiving Party acknowledges and agrees to use them according to the relevant RIPE Policies.

    Both Parties:

    1. Request that the RIPE NCC undertake the appropriate actions so that the registration of the Internet Number Resources is transferred from the Offering Party to the Receiving Party and all relevant information is accordingly updated in the RIPE Registry.

    2. Acknowledge, confirm and agree the following:

    2.1 The terms and conditions of this transfer may be the subject of a separate agreement of which the RIPE NCC is not part. The RIPE NCC shall not be responsible and cannot be held liable for this transfer, or for its non-fulfillment due to any reason derived from a dispute or a disagreement between the Offering Party and the Receiving Party.

    2.2 Both Parties acknowledge that due to this transfer, all rights and obligations with regards to the registration of the relevant Internet Number Resources that arise from the Basic Agreement will be also transferred from the Offering Party to the Receiving Party and will be part of the Receiving Party’s Basic Agreement.

    2.3 Any other rights and obligations that arise from the Basic Agreement, including any other rights to any other Internet number resources registered to the Offering Party by the RIPE NCC, are not affected by this transfer.

    2.4 In the event that a provision in a separate agreement is in conflict with a provision in this Transfer Agreement or the Basic Agreement, the provision in this Transfer Agreement and the Basic Agreement shall prevail.

    2.5 The RIPE NCC shall not be responsible and cannot be held liable for this transfer, or for the non-fulfillment of this transfer due to restrictions from RIPE Policies.

    2.6 If any of the information and/or documentation provided in connection with this request is subsequently found by the RIPE NCC to be substantially incorrect, falsified or misleading, the RIPE NCC reserves the right to revert all changes made to the RIPE Registry accordingly. This applies equally to all information and documentation provided to the RIPE NCC by Both Parties with regards to this request.

    2.7 The RIPE NCC shall not be responsible and cannot be held liable for any direct and/or indirect damages, including damages to Both Parties’ business, loss of profit damages to third parties caused due to compliance with this request or the ongoing maintenance of the relevant RIPE Registry records in accordance with this request.

    2.8 Both Parties shall indemnify the RIPE NCC against any and all third party claims filed against the RIPE NCC in relation to compliance with this request.\n\n
    ''')

    doc.append('Thus agreed by persons authorised to represent both parties:\n\n')
    genlib.append_sigblock(doc, parties['offering'], parties['recieving'])
