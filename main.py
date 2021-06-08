import digitalocean
import sys

# For development
from dotenv import dotenv_values

def main():
    # For development
    env = dotenv_values(".env.devel")
    do_token = env["DO_TEST_TOKEN"]
    # print(env)
    
    # For production
    # Get token
    # token = input("Please enter Digital Ocean API token(must have `WRITE` access): ")
    # Get name
    name = input("Please enter name for droplet(default is `l2tp/ipsec vpn`): ")
    if name == "":
        name = "l2tp/ipsec vpn"
        
    regions = []
    
    # For development
    token = do_token
    # token = "test"

    try:
        mgr = digitalocean.Manager(token=token)
        print(mgr.get_all_droplets())
        print(help(mgr))
    except digitalocean.DataReadError:
        print("Unable to authenticate.")
        sys.exit(1)

if __name__ == "__main__":
    main()