import pylatex as pl
import argparse
import json
import os
from . import genlib


def generate(data, doc):
    parties = data['parties']
    
    doc.append(pl.Center(data=pl.LargeText('Sponsorship Agreement')))
    doc.append(pl.NoEscape(r"\hrule height .1mm"))
    doc.append(pl.NoEscape(r"\vspace{.5cm}"))

    doc.append(pl.NoEscape(genlib.gen_party_flat(parties['lir'], 'LIR')))
    doc.append('\n\nand\n\n')
    doc.append(pl.NoEscape(genlib.gen_party_flat(parties['enduser'], 'End User')))

    with doc.create(pl.Section('Article 1 - Definitions')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
\textbf{Agreement}: this Independent Assignment Request and Maintenance Agreement. \\

\textbf{Administration Fee}: fee to be paid by the End User to the LIR for the administrative costs of this Agreement and for handling the initial request for Assignment. \\

\textbf{Assignment}: act by which the RIPE NCC enables the End User to use Independent Internet Number Resources for its internal use. This may involve the publication in the RIPE Database of the End User as the assignee of the respective Internet Number Resources. \\

\textbf{End User}: natural person or legal entity that has entered into this Agreement in order to receive Internet Number Resources for internal purposes. \\

\textbf{Local Internet Registry (LIR)}: a registry in the RIPE NCC service region that receives allocations for Internet Number Resources from an Internet Number Registry for the purpose of assignment to End Users. \\

\textbf{Maintenance Fee}: periodical fee to be paid by the End User to the LIR for handling requests for Assignment and for maintaining Assignments made during the term of the Agreement. \\

\textbf{Independent Internet Number Resources}: Internet Number Resources (Autonomous System (AS) Number, Provider Independent (PI) IPv4 and IPv6), Internet Exchange Point (IXP) and anycasting assignments directly from the RIPE NCC. \\

\textbf{Reverse DNS Delegation}: Reverse Domain Name System (DNS) delegations allow applications to map to a domain name from an IP address. Reverse delegation is achieved by use of the special domain names in-addr.arpa (IPv4) and ipv6.arpa (IPv6). \\

\textbf{RIPE Database}: database operated by the RIPE NCC. The RIPE Database provides a mechanism for finding contact and registration information for networks in the RIPE NCC service region. The RIPE Database contains IP addresses, Autonomous System (AS) Numbers and organisations or customers that are associated with these resources, and related Points of Contact (POC). \\

\textbf{RIPE NCC}: Réseaux IP Européens Network Coordination Centre (RIPE NCC) is a membership association under Dutch law, established in Amsterdam, the Netherlands. The RIPE NCC has, as an Internet Number Registry, the authority to delegate Internet Number Resources in its service region. The RIPE NCC allocates Internet Number Resources to LIRs. In addition, the RIPE NCC assigns Independent Internet Number Resources to End Users for their internal use in accordance with the applicable RIPE policies for assignment of Independent Internet Number Resources to End Users. \\

\textbf{RIPE Policy}: policy relating to Internet Number Resources developed, adopted and published by the RIPE NCC in accordance with the policy process described in the document "Policy Development Process in RIPE", available on http://www.ripe.net. \\
        '''))

    with doc.create(pl.Section('Article 2 - General Provisions')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
2.1 The Agreement shall come into effect upon receipt by the LIR of a hard copy of the Agreement duly signed by (an authorised representative of) the End User together with an extract from the Commercial Trade Register or equivalent document proving the registration of the End User's business with their national authorities. In the event the End User's business has not been incorporated and has not been registered with the Commercial Trade Register, the End User shall send the LIR a photocopy of a valid identity card.\\

2.2 Upon receipt of the signed Agreement and documents as specified in paragraph 2.1, the LIR shall send the End User an invoice for payment of the following Administration Fee: ''' + data['admin_fee'] + r'''.\\

2.3 The LIR reserves the right to amend and/or supplement the terms of this Agreement. The LIR shall notify the End User and the RIPE NCC of changes in the terms of the Agreement at least one month prior to any such amendment or supplement coming into effect.\\
        '''))

    with doc.create(pl.Section('Article 3 - Request for Assignment')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
3.1 The End User may request an Assignment using the instructions on the LIR website. Upon receipt of the request, the LIR shall submit a request form via the LIR Portal, to the RIPE NCC.\\

3.2 The LIR may suspend the initial request for an Assignment until it has received the Administration Fee as specified in paragraph 2.2 and the Maintenance Fee as specified in paragraph 4.2 for the calendar year in which the Agreement enters into force.\\

3.3 The Assignment is made by the RIPE NCC. The RIPE NCC requires the following conditions to be met before assigning Independent Internet Number Resources:\\

1. the LIR has submitted a request form to the RIPE NCC;\\

2. the RIPE NCC has established that the request complies with the current RIPE policies for Assignment to End Users.\\

\indent
Current documents are available at: http://www.ripe.net/ripe/docs.\\
\indent
Amendments to RIPE policies are published on http://www.ripe.net.\\
        '''))

    with doc.create(pl.Section('Article 4 - Maintenance; Conditions for Maintenance')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
4.1 Subject to the provisions of this Article, the LIR shall maintain the Assignments made by the RIPE NCC upon requests made by the LIR pursuant to this Agreement.\\

4.2 The End User shall pay a periodical Maintenance Fee. The first Maintenance Fee shall be ''' + data['admin_fee'] + r'''. The LIR may amend the Maintenance Fee during the term of the Agreement with such amendment to be published at the LIR's website two months prior to the amendment taking effect.\\

4.3 The End User understands and agrees that the LIR can only maintain the Assignments as long as the assigned Independent Internet Number Resources are used in accordance with RIPE policies as relevant to End Users. More specifically, the LIR shall maintain the Assignments subject to the following conditions:\\

a. The End User shall use the Independent Internet Number Resources assigned to it for internal purposes within its own network only.\\

b. The End User understands and agrees that the Assignment does not confer upon the End User any proprietary or transferable rights in respect of the Independent Internet Number Resources. The End User shall not assign, delegate, sub-delegate or otherwise allow third parties to use the Independent Internet Number Resources assigned to it pursuant to requests made by the LIR pursuant to this Agreement.\\

c. The End User shall use the assigned Independent Internet Number Resources solely for the purpose as specified in the request on the basis of which the Independent Internet Number Resources have been assigned.\\

d. The End User shall comply with the current RIPE policies relevant to End Users, published at www.ripe.net, current documents available in the RIPE Document Store and as may be amended from time to time by the RIPE community in accordance with the RIPE policy process.\\

e. The End User during the term of the Agreement shall provide the LIR with correct and up-to-date information for recording of the Assignment in the RIPE Database.\\

f. The End User shall respond to correspondence by the LIR and the RIPE NCC with regard to Assignments made pursuant to requests under this Agreement and directed at the address as last notified to the LIR by the End User.\\

4.4 The End User understands and agrees that the RIPE NCC may revoke Assignments if the End User does not use the assigned Independent Internet Number Resources in accordance with RIPE policies as relevant to End Users and as further specified in paragraph 4.3.\\
        '''))

    with doc.create(pl.Section('Article 5 - Payment')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
5.1 The End User shall pay the Administration Fee and Maintenance Fee within 30 days of date of invoice, failing which the End User shall be in default, with no notice of default being required.\\

5.2 With effect from the day on which the End User defaults on its payment obligations, the End User shall owe the LIR the statutory rate of interest (highest commercial level) on the amounts unpaid. In addition, the End User shall reimburse the LIR for the extra-judicial collection costs, without prejudice to any other of the LIR's rights, which it may invoke against the End User in connection with the latter's failure to effect (timely) payment.\\
        '''))

    with doc.create(pl.Section('Article 6 - Liability')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
6.1 The LIR does not warrant that the requested Independent Internet Number Resources will be assigned upon request.\\

6.2 The LIR does not warrant that assigned Independent Internet Number Resources will be routable on any part of the Internet.\\

6.3 The End User shall be liable for all aspects of the use of the Independent Internet Number Resources assigned to it and all that ensues from its use of the Independent Internet Number Resources.\\

6.4 The LIR excludes all liability for any direct or indirect damages, including damages to the End User's business, loss of profit, damages to third parties, personal injury or damages to property, except in cases involving wilful misconduct or gross negligence on the part of the LIR or its management.\\

6.5 The LIR shall, in all cases, not be liable for damages caused by a failure by the RIPE NCC to make the Independent Internet Number Resources available (on time), or for damages in any way connected with the use of the Independent Internet Number Resources.\\

6.6 The LIR shall, in all cases, not be liable for non-performance or damages if such is not due to the LIR's fault nor for the account of the LIR pursuant to the law, a juridical act or generally accepted principles.\\

6.7 The End User shall indemnify the LIR against any and all third party claims filed against the LIR in relation to the End User's use of the Independent Internet Number Resources assigned to it pursuant to this Agreement.\\

6.8 In all cases, the LIR's liability shall be limited to a maximum amount equivalent to the aggregate payments received by the LIR pursuant to this Agreement.\\
        '''))    

    with doc.create(pl.Section('Article 7 - Term and Termination')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
7.1 The Agreement shall be entered into for an indefinite period of time, until terminated in accordance with this Article 7.\\

7.2 The End User shall be entitled to terminate the Agreement with a notice period of one month. Notice shall be in writing and sent to the LIR by electronic or regular mail.\\

7.3 The LIR shall be entitled to terminate the Agreement with a notice period of three months. Notice shall be in writing and sent to the End User by electronic or regular mail.\\

7.4 In addition, the LIR shall be entitled to terminate the Agreement forthwith with immediate effect by means of a notice sent to the End User by registered mail, without being liable to pay damages to the End User and without prejudice to the LIR's right to claim (additional) damages from the End User if:\\

1. the End User does not comply with (any of) the provisions of paragraph 4.3 (a), (b), (c) or (d).\\

2. the End User fails to fulfil any obligation arising from this Agreement other than those mentioned in paragraph 4.3 (a), (b), (c) and (d), and fails to rectify such failure within 14 days of receipt of notice of said failure.\\

3. the End User fails to observe any rule of applicable law, which should be adhered to by the End User and which, in the opinion of the LIR, is of such a nature as to justify immediate termination.\\

4. an application has been or is filed for the End User's bankruptcy or for a suspension of payments (moratorium).\\

5. the End User goes into liquidation or becomes insolvent.\\

7.5 Termination shall not affect Administrative or Maintenance Fees that have become due or have been paid prior to the date of termination.\\

7.6 Upon termination, the LIR shall ask the RIPE NCC to delete the RIPE Database record for the Independent Internet Number Resources assigned pursuant to this agreement and ask the RIPE NCC to take measures to revoke the Reverse DNS for the respective Independent Internet Number Resources. The End User furthermore understands and accepts that the LIR and the RIPE NCC may take any other measures necessary to enable the Independent Internet Number Resources to become eligible for re-assignment to other End Users.\\

7.7 Upon termination, and except for replacement of an agreement by another agreement for the same Independent Internet Number Resources as meant in paragraph 7.9, the End User shall no longer be entitled to and shall refrain from use of the Independent Internet Number Resources and the Independent Internet Number Resources may be re-assigned by the RIPE NCC to other End Users. The End User understands and accepts that it has not and undertakes not to make any claim as against the LIR or the RIPE NCC for the continued use of the Independent Internet Number Resources.\\

7.8 The Agreement shall automatically expire on the date at which the LIR is declared bankrupt, the LIR has been liquidated or the Standard Service Agreement between the LIR and the RIPE NCC pursuant to which Independent Internet Number Resources have been assigned by the RIPE NCC to the End User has been terminated.\\

7.9 After termination of this Agreement in accordance with paragraph 7.2 or 7.3 or expiry as specified in paragraph 7.8, the End User may seek to extend the right to use for the same Independent Internet Number Resources by entering into an End User Assignment Agreement with the RIPE NCC or by applying for Assignment pursuant to a Independent Assignment Request and Maintenance Agreement with another LIR. The End User understands and agrees that the Independent Internet Number Resources may be re-assigned by the RIPE NCC to another End User if the End User does not seek to extend the right to use within three months of the termination of the Agreement.\\
        '''))

    with doc.create(pl.Section('Article 8 - Governing Law')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
This Agreement shall be exclusively governed by the laws of the country of establishment of the LIR.\\
'''))

    with doc.create(pl.Section('Article 9 - Third Party Rights RIPE NCC')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
The rights and actions granted to the RIPE NCC under paragraphs 4.4, 7.7, 7.8, 7.9 and 10.2 are being granted irrevocably and for the sole benefit of the RIPE NCC and without the RIPE NCC being due any consideration.\\
'''))

    with doc.create(pl.Section('Article 10 - Miscellaneous')) as section:
        section.append(pl.NoEscape(r'\noindent'))
        section.append(pl.NoEscape(r'''
10.1 Without the LIR's prior written consent, the End User shall not be permitted to assign any rights or obligations arising from the Agreement.\\

10.2 The LIR shall submit to the RIPE NCC copies of this Agreement and the documents submitted by the End User pursuant to this Agreement for the purpose of verifying the status of the Independent Internet Number Resources and compliance with the applicable RIPE policies.\\

10.3 The End User shall notify the LIR immediately of any change of address or billing details. Until such notification, the last notified address and billing details shall be presumed to be correct.\\

10.4 Unless provided otherwise, the LIR may send notifications under this Agreement to the last notified email and mail address of the End User.\\

10.5 If any provision contained in this Agreement is held to be invalid by a court of law, this shall not in any way affect the validity of the remaining provisions.\\

Thus agreed and signed in duplicate by persons authorised to represent both parties:\\
'''))
        genlib.append_sigblock(section, parties['lir'], parties['enduser'])
