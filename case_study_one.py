import subprocess  # Module to execute system-level commands and external processes

# --- PHASE 1: Internal Reconnaissance ---
# Simulates the list of target IP addresses discovered by the malware 
# after gaining an initial foothold in the internal network.
target_hosts = ["10.0.0.5", "10.0.0.6", "10.0.0.7"]

# --- PHASE 2: Credential Harvesting (Mimikatz Style) ---
# Simulates administrative credentials extracted from the LSASS memory 
# using tools like Mimikatz. This allows the malware to move "legitimately."
stolen_creds = {
    "username": "DomainAdmin", 
    "password": "Password123!"
}

def propagate(ip):
    """
    Simulates the core logic of Lateral Movement within a corporate network.
    """
    print(f"[*] Attempting to infect host: {ip}")
    
    # --- PHASE 3: 'Living off the Land' (LotL) Technique ---
    # Constructing a PsExec command. PsExec is a legitimate Microsoft sysadmin tool.
    # The malware hijacks it to execute the payload (malware.exe) on remote machines.
    # -u / -p: Uses stolen credentials to authenticate.
    # -d: Detaches the process so the virus can continue spreading without waiting.
    psexec_command = f"psexec \\\\{ip} -u {stolen_creds['username']} -p {stolen_creds['password']} -d cmd.exe /c 'malware.exe'"
    
    # --- PHASE 4: Simulated Infection Outcome ---
    # Simulation: 10.0.0.6 fails because it represents a machine that is 
    # properly patched (MS17-010) or isolated via Network Segmentation.
    success = True if ip != "10.0.0.6" else False
    
    if success:
        # If successful, the malware begins encrypting the Master File Table (MFT)
        print(f"[+] Spread Success: Host {ip} is now encrypting.")
    else:
        # Demonstrates that security best practices can stop even the most aggressive worms
        print(f"[-] Spread Failed: Host {ip} is isolated/patched.")

# --- PHASE 5: Automated Worm Propagation ---
# Iterates through the targets at "machine speed." This automation is why 
# Maersk’s global operations collapsed in less than an hour.
for host in target_hosts:
    propagate(host)

# --- PHASE 6: Final Destructive Payload ---
# Unlike standard ransomware, the final step is to overwrite the Master Boot Record (MBR),
# making the computer physically unable to boot into the operating system.
print("\n[!] Spread complete. Master Boot Records (MBR) are being destroyed...")
