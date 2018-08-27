#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: Contain nsx-t Preconfig for VPN Testcases
# Group-physical-st: optional
# Timeout: 172800

import paramiko


def Run(args, attachment_type=None):

    if attachment_type:
        json_payload = 'has_attachment'
    elif attachment_type == 'L2VPN_SESSION':
        json_payload =  'has_L2VPN_SESSION_attachement'
    else:
        json_payload = 'no attachment'
    print json_payload


Run('', attachment_type='port')
