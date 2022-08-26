# DFS - Working on script to import cert and then suck out all the SAN names for DNS subdomain enumeration
import ssl, socket, subprocess

# Clear the terminal screen
# subprocess.call('clear', shell=True)

#hostname = input("Enter a remote host to scan: ")
hostname = "microsoft.com"
port = 443

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, port))
    cert = s.getpeercert()

print("_" * 60)
print(cert)

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
org_name = subject['organizationName']
org_city = subject['localityName']
org_state = subject['stateOrProvinceName']
org_country = subject['countryName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
# TODO Dict is not right here yet
# subjectAltName = dict(x[0] for x in cert['subjectAltName'])
# san = subjectAltName(['DNS'])

print("_" * 60)
print("Org Name:", org_name)
print("Common Name:", issued_to)
print("City:", org_city)
print("State or Province:", org_state)
print("Country:", org_country)
print("Issued By:", issued_by)
#print(san)
print("_" * 60)
