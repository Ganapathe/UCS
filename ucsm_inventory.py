"""
Written by Ganapathi Narayanaswamy
Github: https://github.com/Ganapathe/UCS
Email: ganapathe@hotmail.com

Basic script to collect the inventory from UCSM.
This script has been tested and works well.

"""
#Import ucsmsdk Modules
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.ucsmo import ManagedObject
from ucsmsdk.ucscoremeta import MoPropertyMeta, MoMeta
from ucsmsdk.ucsmeta import VersionMeta
#Login to UCSM
handle = UcsHandle(("ucsm-ip-adddress","ucs-domain_name\account","password"))
handle.login()
#Collecting blade inventory
blades_inv = handle.query_classid("computeBlade")
for blade_inv in blades_inv:
	print (blade_inv.name,blade_inv.usr_lbl,blade_inv.operability,blade_inv.chassis_id,blade_inv.rn,blade_inv.model,blade_inv.serial,blade_inv.total_memory,blade_inv.num_of_cores,blade_inv.num_of_cpus,blade_inv.num_of_eth_host_ifs,blade_inv.num_of_fc_host_ifs,blade_inv.assigned_to_dn)

#Collecting Chassis Info
chasiss = handle.query_classid("equipmentChassis")
for chasis in chasiss:
	print(chasis.usr_lbl,chasis.rn,chasis.model,chasis.serial,chasis.availability,chasis.conn_status,chasis.thermal,chasis.service_state,chasis.conn_path,chasis.power,chasis.oper_state,chasis.config_state,chasis.admin_state)

#Collecting FAN Info
chasiss_fan = handle.query_classid("EquipmentFanModule")
for chasis_fan in chasiss_fan:
	print(chasis_fan.dn,chasis_fan.model,chasis_fan.serial,chasis_fan.tray,chasis_fan.power,chasis_fan.oper_state,chasis_fan.thermal,chasis_fan.voltage)
#Collecting Powersupply Unit
chasiss_psu = handle.query_classid("equipmentPsu")
for chasis_psu in chasiss_psu:
	print(chasis_psu.dn,chasis_psu.model,chasis_psu.serial,chasis_psu.part_number,chasis_psu.power,chasis_psu.voltage,chasis_psu.oper_state)
#Collecting FI info
chasiss_fi = handle.query_classid("networkElement")
for chasis_fi in chasiss_fi:
	print(chasis_fi.dn,chasis_fi.model,chasis_fi.serial,chasis_fi.total_memory,chasis_fi.oob_if_ip,chasis_fi.oob_if_mask,chasis_fi.oob_if_gw,chasis_fi.oob_if_mac,chasis_fi.min_active_fan,chasis_fi.admin_inband_if_state)
#Collecting IOM Info
chasiss_io = handle.query_classid("equipmentIOCard")
for chasis_io in chasiss_io:
	print (chasis_io.dn,chasis_io.model,chasis_io.serial,chasis_io.part_number,chasis_io.base_addr,chasis_io.switch_id,chasis_io.side,chasis_io.oper_state,chasis_io.admin_state)
 
