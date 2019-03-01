# Writeup 3 - Operational Security and Social Engineering

Name: **Robert Nash**
Section: **0201**

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: **Robert Nash**

## Assignment Writeup

### Part 1 (40 pts)

After a quick search on namecheap.com, we notice that the l337bank.money domain is available for purchase (its actually on special for only $6.88). We can purchase this domain and send emails from it as if we were sending emails from 1337bank.money - inside the organization.

After purchasing the domain, we can send an "official" email to Elizabeth claiming to be part of the security team. This email will state that she needs to login to her online account using our link and change her PIN.  We can set up a fake website from the new domain we purchased that now ask her to confirm her identity by answering her mother's maiden name, city she was born in, and name of her first pet. Her browser would be pulled from her connecting to the site. Once she logs in confirming her identity, she is prompted with her updating her ATM by first entering her old PIN, then her "new" PIN.

### Part 2 (60 pts)

* Weak passwords
    * Use a password manager such as LastPass, Dashlane or 1Password (Among many). This will assist in not only creating hard to guess, unique, complex passwords, but help you make sure you don't reuse passwords. Passwords should be 

*  Use an IDS/IPS
    * Using an IDS can help alert the IT/Security department of nefarious activity such as ping sweep and vulnerability scans. It can a log of activity to be reviewed later. An IPS takes it a step further and can actually take steps to prevent 

* Use a firewall
    * Using a firewall could have prevented someone from accessing the 1337 port on the server. The firewall could have resctricted access to only a handful of known IP addressed so that only approved individuals could access it.
