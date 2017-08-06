from datetime import datetime
from netmiko import ConnectHandler
from mydevices import csrv1, csrv2, csrv3
import getpass
def configure_ospf(net_connect, file_name=''):
    """Configure OSPF on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [csrv1, csrv2, csrv3,]
    print "\n              CONFIGURING NTP PROTOCOL   "
    print 
    start_time = datetime.now()
    print
    for a_device in device_list:
       # as_number = a_device.pop('process_id')
        print a_device
        process_id = 100
        net_connect = ConnectHandler(**a_device)
        
        net_connect.enable()
        if check_ospf(net_connect):
              print "\n         OSPF currently configured   \n"
              remove_ospf_config(net_connect, process_id=process_id)
        else:
              print "\n         No OSPF"
   
        # Construct file name 
        # Check OSPF is now gone
        if check_ospf(net_connect):
            raise ValueError("OSPF configuration still detected")
          
        device_type = net_connect.device_type
        file_name = "ospf_" + (a_device ['username']) + ".txt"
        print "\n  Reading file : "
        print "  {}\n".format(file_name)
    
    # Configure OSPF
        ospfconfig = configure_ospf(net_connect, file_name)
        print ospfconfig
        print
    
    print "Time elapsed: {}\n".format(datetime.now() - start_time)

if __name__ == "__main__":
    main()

print "\n\n * * * * * * * * *   CONFIGURATION WAS DONE SUCCESSFULLY    * * * * * * * * * *  \n"
