"""
Written by Ganapathi Narayanaswamy
Github: https://github.com/Ganapathe/UCS
Email: ganapathe@hotmail.com

Script to assign user label to all the blades in UCSM.
"""
#Import Modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.ucsmo import ManagedObject
from ucsmsdk.ucscoremeta import MoPropertyMeta, MoMeta
from ucsmsdk.ucsmeta import VersionMeta
#Login to UCSM
handle1 = UcsHandle("ucsm-ip-adddress","ucs-domain_name\account","password")
handle1.login()
#Collecting the Blade informations
blades_inv = handle1.query_classid("computeBlade")
#Get user defined user labels and store as text file in temp folder
with open(r"C:\TEMP\test2.txt") as file:
    data = file.read()
lines = data.split("\n")
#Assigning a user label
i = 0
if i < len(lines):
    for blade_inv in blades_inv:
        blade_inv.usr_lbl = lines[i]
        i += 1
        handle1.set_mo(blade_inv)
        print(blade_inv.usr_lbl,blade_inv.name,blade_inv.chassis_id,blade_inv.rn,blade_inv.assigned_to_dn)
#Commit changes
        handle1.commit()
