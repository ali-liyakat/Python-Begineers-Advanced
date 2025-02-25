import re 

text = "Patient's phone number is 7321119999. Bill amount is 120$"

pattern = '\d+'
match = re.findall(pattern,text)
print(match)

ph_pattern = '\d{10}'
ph_match = re.findall(ph_pattern,text)
print(ph_match)


text2 = "Patient's phone number is (732)-111-9999, spouse phone number is 7326664444. Bill amount is 120$"

pat2 = "\(\d{3}\)-\d{3}-\d{4}|\d{10}"
match2 = re.findall(pat2, text2)
print(match2)

text = "Patient's phone number is 7321119999. Bill amount is 120$"
pattern = "(\d{10})\D+(\d+)\$"
match = re.search(pattern, text)

ph_number, bill = match.groups()
print(ph_number, bill)


text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

 
 

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''

name_pat = "Name:(.*)Date"
match = re.findall(name_pat, text)
name = match[0].strip()
print(name)
print("\n================================")


addr_pat = "Address:(.*)\n"
match = re.findall(addr_pat, text)
address = match[0].strip()
print(address)
print("\n================================")


medi_pat = "Address:[^\n]*(.*)Directions"
match = re.findall(medi_pat, text, flags=re.DOTALL)
medicines = match[0].strip()
print(medicines)
print("\n================================")


dir_pat = "Directions:[^\n]*(.*)Refill"
match = re.findall(dir_pat, text, flags=re.DOTALL)
directions = match[0].strip()
print(directions)


refil_pat = "Refill:(.*)times"
match = re.findall(refil_pat, text)
refil = match[0].strip()
print(refil)


text = '''Follow our leader Elon musk on Twitter 
here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. 
Also here are leading influencers for tesla-related news, 
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla'''

pat = "https://twitter\.com/([a-zA-Z0-9_]+)"
match = re.findall(pat,text)
print(match)