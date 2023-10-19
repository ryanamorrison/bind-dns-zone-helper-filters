#!/usr/bin/python3

#EXAMPLES = r"""
#- name: get reverse zone from ipv4 address
#  ansible.builtin.set_fact:
#    rev_zone_name: "{{ '172.31.4.0' | return_zone_from_ipfour }"
#"""

#from ansible.errors import AnsibleFilterError
import datetime

class FilterModule(object):

  def filters(self):
    return { 
      'reverse_zone_file_from_ipfour':self.return_reverse_zone_file,
      'reverse_zone_from_ipfour':self.return_reverse_zone_name,
      'last_octet_from_ipfour':self.return_last_octet,
      'first_three_octets_from_ipfour':self.return_first_three,
      'serial_number_update':self.serial_number_calc,
      'dots_to_underscores':self.dots_to_underscores,
      'underscores_to_dots':self.underscores_to_dots,
      'zone_to_db_filename':self.zone_to_db_filename,
      'return_domain_from_fqdn':self.get_domainname
  }

  #these first three are for handling reverse zones
  def return_reverse_zone_file(self,ipfouraddr):
    rawlist = ipfouraddr.split('.')
    returnstr = rawlist[2] + '.' + rawlist[1] + '.' + rawlist[0] + '.in.addr.arpa'
    return returnstr

  def return_reverse_zone_name(self,ipfouraddr):
    rawlist = ipfouraddr.split('.')
    returnstr = rawlist[2] + '.' + rawlist[1] + '.' + rawlist[0] + '.in-addr.arpa'
    return returnstr

  def return_last_octet(self,ipfouraddr):
    rawlist = ipfouraddr.split('.')
    returnstr = rawlist[3] 
    return returnstr

  #this is for handling out-of-zone data filtering
  def return_first_three(self,ipfouraddr):
    rawlist = ipfouraddr.split('.')
    returnstr = rawlist[0] + '.' + rawlist[1] + '.' + rawlist[2]
    return returnstr

  #this is to calculate a new serial number automatically
  def serial_number_calc(self,serialno):
    #get current date
    datenow = datetime.date.today().strftime("%Y%m%d")
    #get serial date field
    serialdate = serialno[:8]
    #compare current date to serial number date fields
    if datenow == serialdate:
      #if the same then it means that the number field needs to be incremeneted
      serialdigits = serialno[-2:]
      newincrement = int(serialdigits) + 1
      paddedincrement = f'{newincrement:02}'
      returnserial = serialdate + paddedincrement
    else:
      #if not the same then the current date is used and counter resets to 01
      returnserial = datenow + "01"
    #return the serial number
    return returnserial

  #these next two functions are to convert ansible_local.zone.info for comparison
  def dots_to_underscores(self,stringtoreplace):
    returnstr = stringtoreplace.replace('.','_')
    return returnstr

  def underscores_to_dots(self,stringtoreplace):
    returnstr = stringtoreplace.replace('_','.')
    return returnstr

  def zone_to_db_filename(self,zonestring):
    returnstr = 'db.' + zonestring
    return returnstr

  def get_domainname(self,fqdnstr):
    indx = fqdnstr.find('.')
    if indx > 1:
      indx += 1
      returnstr = fqdnstr[indx:]
    else:
      returnstr = fqdnstr
    return returnstr
