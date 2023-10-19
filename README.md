BIND DNS zone file helper filters
=========

I was annoyed with the existing jinja2 filters for working with IP addresses as they weren't designed to do what I was trying to do with my BIND project implementation so I wrote my own.

Requirements
------------

Tested with Ansible 2.15.3, Python 3.10.12, and Jinja 3.1.2.

Dependencies
------------

None

Example Use
----------------
To test run the example playbook:
```
$ ansible-playbook example-playbook.yaml
```
Example output from example-playbook.yaml
```
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost
does not match 'all'

PLAY [localhost] ******************************************************************************************

TASK [return a reverse zone name from an ipv4 address] ****************************************************
ok: [localhost] => {
    "msg": "1.30.172.in-addr.arpa"
}

TASK [return the last octet from an ipv4 address] *********************************************************
ok: [localhost] => {
    "msg": "100"
}

TASK [return the first three octets from an ipv4 address] *************************************************
ok: [localhost] => {
    "msg": "172.30.1"
}

TASK [compare current BIND serial number and increment or generate new] ***********************************
ok: [localhost] => {
    "msg": "2023101901"
}

TASK [generate a zone db filename from a zone name] *******************************************************
ok: [localhost] => {
    "msg": "db.zone.com"
}

TASK [change dots to underscores (useful for working with ansible_local facts)] ***************************
ok: [localhost] => {
    "msg": "db_zone_com"
}

TASK [change underscores to dots (useful for working with ansible_local facts)] ***************************
ok: [localhost] => {
    "msg": "db.zone.com"
}

TASK [generate a reverse zone db filename from an ipv4 address] *******************************************
ok: [localhost] => {
    "msg": "db.1.30.172.in.addr.arpa"
}

TASK [get the domain from a FQDN] *************************************************************************
ok: [localhost] => {
    "msg": "domain.tld"
}

PLAY RECAP ************************************************************************************************
localhost  
```

License
-------

BSD

Author Information
------------------

Ryan A. Morrison (ryan@ryanamorrison.com)
