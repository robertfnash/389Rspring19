# Writeup 6 - Forensics

Name: Robert Nash
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Robert Nash

## Assignment Writeup

### Part 1 (45 Pts)

1. `142.93.136.81`
2. `nmap` tcp scan
3. | IP Address | Region |
   | --- | ---|
   |`159.203.113.181`| `Clifton, New Jersey`
   |`37.237.212.29` | `Al Qadisiyah, Ad Diwaniyah, Iraq`|
   |`81.22.45.115` | `Berlin, Germany`
   |`113.176.70.179` | `Dong Nai, Bien Hoa, Viet Nam`
   |`113.188.3.83` | `Dong Nai, Bien Hoa, Viet Nam`
   |`184.22.161.10` | `Chiang Mai, Chiang Mai, Thailand`
   |`178.19.107.42` | `Slaskie, Tarnowskie Gory, Poland`
   
4. Hackers accessed the server on port `21` but pulled the file from port `20`
5. The file stolen was a picture named `find_me.jpeg`

    1. It was a `jpeg`
    2. `Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay`
    3. `2018:12:23 20:16:23Z`
    4. `Apple iPhone 8`
    5. `4.5 m` Below Sea Level

6. `greetz.fpff`

### Part 2 (55 Pts)

1. `2019-03-27 00:15:05`

2. `fl1nch`

3. **Section 1** - `ASCII` Type with the string `Hey you, keep looking :)`

   **Section 2** - `COORD` Type 
   
   **Section 3** - `PNG` Type with an image of Testudo and the flag `CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}`
   
   **Section 4** - `ASCII` Type with a backwards flag `}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC`
   
   **Section 5** - `ASCII` Type with a base64 encoded string `Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=`
   Decoding it gives us the flag `CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}`
   
   
4. `CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}`
   `CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}`
   `CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}`
   
**Code:**

**!NOTE!** - The command for this code is `python stub.py filename /Path/``

Where path is the directory where you want to save any images. No need to create a name, just path to directory i.e `/tmp/`

```
#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8badf00d
VERSION = 1

BYTE = 1
WORD = 4 * BYTE
DWORD = 2 * WORD

# Offsets
HEADER_START       = 0
MAGIC_VERSION      = HEADER_START   + DWORD
TIME_STAMP         = MAGIC_VERSION  + WORD
AUTHOR             = TIME_STAMP     + DWORD
HEADER_END         = AUTHOR         + WORD

BODY_START = HEADER_END

# Section numbers

SECTION_ASCII     = 0x1
SECTION_DWORDS    = 0x2
SECTION_UTF8      = 0x3
SECTION_DOUBLES   = 0x4
SECTION_WORDS     = 0x5
SECTION_COORD     = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG       = 0x8
SECTION_GIF87     = 0x9
SECTION_GIF89     = 0xA

# Misc
PNG_HEADER   = 0x89504e470d0a1a0a
GIF89_HEADER = 0x474946383961
GIF87_HEADER = 0x474946383761

if len(sys.argv) < 3:
    sys.exit("Usage: python stub.py input_file.fpff /Path/to/dir/for/images/")

PATH_TO_SAVE_FILE = sys.argv[2]

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

magic, version, timestamp, author, sectioncount = struct.unpack("<LLL8sL", data[HEADER_START:HEADER_END])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if timestamp < 0:
    bork("Bad time stamp! Got %d" % int(timestamp))

if sectioncount < 0:
	bork("Bad section count! Got %d, should be greater than 0" % (int(sectioncount)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIME STAMP: %s" % datetime.datetime.fromtimestamp(timestamp))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(sectioncount))

print("\n-------  BODY  -------")

offset_start = BODY_START
offset_end   = offset_start + DWORD

for x in range(1, (sectioncount + 1)):
	print("\nSECTION: " + str(x))
	stype, slen = struct.unpack("<LL", data[offset_start:offset_end])

	amount_of_words = slen / 4

	if stype == SECTION_PNG:
		print("SECTION TYPE: PNG")
		print("SECTION VALUE:\nImage saved to " + PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.png")
		with open(PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.png", 'a+') as f:
			f.write(struct.pack(">Q", PNG_HEADER))
			for x in range(0, amount_of_words):
				offset_start = offset_end	
				offset_end   = offset_start + WORD
				svalue, = struct.unpack(">L", data[offset_start:offset_end])
				f.write(struct.pack(">L", svalue))
		f.close()
	elif stype == SECTION_DWORDS:
		print("SECTION TYPE: DWORDS")
		if (slen % 8) != 0:
			 bork("Bad section length!")
		else:
			print("SECTION VALUE: ")
			for x in range(0, slen / 8):
				offset_start = offset_end	
				offset_end   = offset_start + DWORD
				svalue, = struct.unpack("<Q", data[offset_start:offset_end])
				sys.stdout.write(svalue)
	elif stype == SECTION_UTF8:
		print("SECTION TYPE: UTF8")
		print("SECTION VALUE: ")
		for x in range(0, amount_of_words):
			offset_start = offset_end	
			offset_end   = offset_start + WORD
			svalue, = struct.unpack("<4s", data[offset_start:offset_end])
			sys.stdout.write(svalue)
	elif stype == SECTION_DOUBLES:
		print("SECTION TYPE: DOUBLES")
		if (slen % 8) != 0:
			 bork("Bad section length!")
		else: 
			print("SECTION VALUE: ")
			for x in range(0, slen / 8):
				offset_start = offset_end	
				offset_end   = offset_start + DWORD
				svalue, = struct.unpack("<d", data[offset_start:offset_end])
				sys.stdout.write(svalue)
	elif stype == SECTION_WORDS:
		print("SECTION TYPE: WORDS")
		if (slen % 4) != 0:
			 bork("Bad section length!")
		else: 
			print("SECTION VALUE: ")
			for x in range(0, slen / 4):
				offset_start = offset_end	
				offset_end   = offset_start + WORD
				svalue, = struct.unpack("<L", data[offset_start:offset_end])
				sys.stdout.write(double(svalue))
	elif stype == SECTION_COORD:
		print("SECTION TYPE: COORD")
		if (slen != 16):
			 bork("Bad section length!")
		else:
			print("SECTION VALUE: ")
			offset_start = offset_end	
			offset_end   = offset_start + slen
			latitude, longtitude = struct.unpack("<dd", data[offset_start:offset_end])
			sys.stdout.write("Latitude: " + str(latitude) + ", Longtitude: " + str(longtitude))
	elif stype == SECTION_REFERENCE:
		print("SECTION TYPE: REFERENCE")
		if (slen != 4):
			 bork("Bad section length!")
		else: 
			print("SECTION VALUE: ")
			offset_start = offset_end	
			offset_end   = offset_start + WORD
			svalue, = struct.unpack("<L", data[offset_start:offset_end])
			if (int(svalue) < 0) or (int(svalue) > (sectioncount - 1)):
				bork("Bad Section Reference!")
			else:
				sys.stdout.write(int(svalue))
	elif stype == SECTION_ASCII:
		print("SECTION TYPE: ASCII")
		print("SECTION VALUE: ")
		for x in range(0, amount_of_words):
			offset_start = offset_end	
			offset_end   = offset_start + WORD
			svalue, = struct.unpack("<4s", data[offset_start:offset_end])
			sys.stdout.write(svalue)
	elif stype == SECTION_GIF89:
		print("SECTION TYPE: GIF89")
		print("SECTION VALUE:\nImage saved to " + PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.png")
		with open(PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.gif", 'a+') as f:
			f.write(struct.pack(">" + ("c" * 4), GIF89_HEADER))
			for x in range(0, amount_of_words):
				offset_start = offset_end	
				offset_end   = offset_start + WORD
				svalue, = struct.unpack(">L", data[offset_start:offset_end])
				f.write(struct.pack(">L", svalue))
		f.close()
	elif stype == SECTION_GIF87:
		print("SECTION TYPE: GIF87")
		print("SECTION VALUE:\nImage saved to " + PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.png")
		with open(PATH_TO_SAVE_FILE + "section_" + str(x) + "_image.gif", 'a+') as f:
			f.write(struct.pack(">" + ("c" * 4), GIF87_HEADER))
			for x in range(0, amount_of_words):
				offset_start = offset_end	
				offset_end   = offset_start + WORD
				svalue, = struct.unpack(">L", data[offset_start:offset_end])
				f.write(struct.pack(">L", svalue))
		f.close()
	else:
		bork("Bad Section Type! Got %s" % hex(stype))

	print("\nSECTION LENGTH: %d bytes" % int(slen))

	offset_start = offset_end
	offset_end   = offset_start + DWORD
```

