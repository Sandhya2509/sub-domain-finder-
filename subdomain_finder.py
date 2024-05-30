import dns.resolver
import socket

# List of potential subdomains
subdomains = [
    'www', 'mail', 'blog', 'ftp', 'webmail', 'test', 'dev', 'portal', 'admin', 'intranet', 'secure', 'm', 'vpn'
]

# Function to find subdomains
def find_subdomains(domain):
    found_subdomains = []

    for subdomain in subdomains:
        try:
            # Form the full domain name
            full_domain = f"{subdomain}.{domain}"
            # Attempt to resolve the domain name
            dns.resolver.resolve(full_domain, 'A')
            found_subdomains.append(full_domain)
            print(f"Found subdomain: {full_domain}")
             # Add port scanning here
            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((full_domain, port))
                if result == 0:
                    print(f"Port {port} open")
                sock.close()
        except dns.resolver.NXDOMAIN:
            # If the domain does not exist, we just pass
            pass
        except dns.resolver.NoAnswer:
            # If there's no DNS record for this subdomain, we also pass
            pass
        except Exception as e:
            # Print any other exceptions that may occur
            print(f"Error occurred: {e}")

    return found_subdomains

if __name__ == "__main__":
    domain = input("Enter the domain to search for subdomains: ")
    found = find_subdomains(domain)
    print(f"\nFound {len(found)} subdomains for {domain}:")
    for sub in found:
        print(sub)
