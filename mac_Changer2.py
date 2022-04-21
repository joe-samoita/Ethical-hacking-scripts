import optparse
import re
import subprocess


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="this is the help message")
    parser.add_option("-m", "--mac", dest="new_mac", help="This is the new Mac")

    (options2, arguments) = parser.parse_args()

    if not options2.interface:
        parser.error("Please enter the new mac")
    if not options2.new_mac:
        parser.error("Please enter the interface")

    return options2


def get_current_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    mac_address_output = re.search(br"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)

    if mac_address_output:
        return mac_address_output.group(0)
    else:
        print("Could not read mac address")


def mac_changer(new_mac, interface):
    print("[+]Changing mac address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options2 = get_arguments()

current_mac = get_current_mac(options2.interface)
print(options2.new_mac)
print("[+]Current mac = " + str(current_mac))

mac_changer(options2.new_mac, options2.interface)
print(options2.new_mac)
current_mac = get_current_mac(options2.interface)
if current_mac == options2.new_mac:
    print("[+] Mac address was successfully changed to " + current_mac)
else:
    print("[+] Mac address was not changed")
