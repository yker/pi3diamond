"""
    This file is part of pi3diamond, a toolkit for
    confocal scanning, anti-bunching, FLIM, pulsed ODMR / NMR,
    and more sophisticated quantum physics experiments,
    typically performed with NV centers in diamond,
    written in python using the enthought traits packages.

    pi3diamond is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pi3diamond is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with diamond. If not, see <http://www.gnu.org/licenses/>.

    Copyright (C) 2009-2016 Helmut Fedder <helmut@fedder.net>
"""

#DTG_recids.py - definitions of binary codes for the .dtg file format. See the Tektronix Programmer's Manual for details

internal_node = 0x8000
leaf_node = 0x0000

recids = {
'DTG_ROOT_RECID':0x0001 | internal_node,                       
'DTG_MAGIC_RECID':0x0002 | leaf_node,
'DTG_TB_OPERATION_RECID':0x0003 | leaf_node,
'DTG_TB_RUNMODE_RECID':0x0004 | leaf_node,
'DTG_TB_BURSTCOUNT_RECID':0x0005 | leaf_node,
'DTG_TB_CLOCKSOURCE_RECID':0x0006 | leaf_node,
'DTG_TB_CLOCKSETTYPE_RECID':0x005D | leaf_node,
'DTG_TB_CLOCK_RECID':0x0007 | leaf_node,
'DTG_TB_JITTERINPUT_RECID':0x0008 | leaf_node,
'DTG_TB_LONGDELAY_RECID':0x0009 | leaf_node,
'DTG_TB_CLOCKRANGE_RECID':0x000A | leaf_node,
'DTG_TB_DELAYOFFSET_RECID':0x000B | leaf_node,
'DTG_TB_CLOCKOUTPUT_RECID':0x000C | leaf_node,
'DTG_TB_CLOCKOUTPUTAMPLITUDE_RECID':0x000D | leaf_node,
'DTG_TB_CLOCKOUTPUTOFFSET_RECID':0x000E | leaf_node,
'DTG_TB_CLOCKOUTPUTTERMZ_RECID':0x0061 | leaf_node,
'DTG_TB_CLOCKOUTPUTTERMV_RECID':0x0062 | leaf_node,
'DTG_TRIGGER_SOURCE_RECID':0x000F | leaf_node,
'DTG_TRIGGER_SLOPE_RECID':0x0010 | leaf_node,
'DTG_TRIGGER_LEVEL_RECID':0x0011 | leaf_node,
'DTG_TRIGGER_IMPEDANCE_RECID':0x0012 | leaf_node,
'DTG_TRIGGER_INTERVAL_RECID':0x0013 | leaf_node,
'DTG_EVENT_INPUTPOLARITY_RECID':0x0014 | leaf_node,
'DTG_EVENT_INPUTTHRESHOLD_RECID':0x0015 | leaf_node,
'DTG_EVENT_INPUTIMPEDANCE_RECID':0x0016 | leaf_node,
'DTG_SEQ_MODE_RECID':0x0017 | leaf_node,
'DTG_SEQ_JUMPMODE_RECID':0x0018 | leaf_node,
'DTG_SEQ_JUMPTIMING_RECID':0x0019 | leaf_node,
'DTG_JITTER_GENERATION_RECID':0x001A | leaf_node,
'DTG_JITTER_MODE_RECID':0x001B | leaf_node,
'DTG_JITTER_LOGICALCH_RECID':0x001C | leaf_node,
'DTG_JITTER_GATINGSOURCE_RECID':0x001D | leaf_node,
'DTG_JITTER_EDGE_RECID':0x001E | leaf_node,
'DTG_JITTER_FREQUENCY_RECID':0x001F | leaf_node,
'DTG_JITTER_AMPUNITSETTYPE_RECID':0x005E | leaf_node,
'DTG_JITTER_AMPMODESETTYPE_RECID':0x005F | leaf_node,
'DTG_JITTER_AMPLITUDE_RECID':0x0020 | leaf_node,
'DTG_DCOUTPUT_RECID':0x0021 | leaf_node,
'DTG_DCOUTPUTTABLE_RECID':0x0022 | leaf_node,
'DTG_ASSIGN_RECID':0x0023 | leaf_node,
'DTG_GROUP_RECID':0x0024| internal_node,
'DTG_ID_RECID':0x0025 | leaf_node,
'DTG_NAME_RECID':0x0026 | leaf_node,
'DTG_NBITS_RECID':0x0027 | leaf_node,
'DTG_LOGICALCHANNEL_RECID':0x0028 | leaf_node,
'DTG_RADIX_RECID':0x0029 | leaf_node,
'DTG_SIGNED_RECID':0x002A | leaf_node,
'DTG_MAGNITUDE_RECID':0x002B | leaf_node,
'DTG_LOGICALCH_RECID':0x002C | internal_node,
'DTG_TERMZ_RECID':0x002E | leaf_node,
'DTG_TERMV_RECID':0x002F | leaf_node,
'DTG_LIMIT_RECID':0x0030 | leaf_node,
'DTG_LIMITHIGH_RECID':0x0031 | leaf_node,
'DTG_LIMITLOW_RECID':0x0032 | leaf_node,
'DTG_LEVELSETTYPE_RECID':0x0060 | leaf_node,
'DTG_LEVELHIGHORAMP_RECID':0x0033 | leaf_node,
'DTG_LEVELLOWOROFFSET_RECID':0x0034 | leaf_node,
'DTG_OUTPUT_RECID':0x0037 | leaf_node,
'DTG_POLARITY_RECID':0x0038 | leaf_node,
'DTG_JITTERRANGE_RECID':0x0064 | leaf_node,
'DTG_FORMAT_RECID':0x0039 | leaf_node,
'DTG_DELAYUNIT_RECID':0x003A | leaf_node,
'DTG_DELAYDATA_RECID':0x003B | leaf_node,
'DTG_WIDTHUNIT_RECID':0x003C | leaf_node,
'DTG_WIDTHDATA_RECID':0x003D | leaf_node,
'DTG_SLEWRATE_RECID':0x003E | leaf_node,
'DTG_CHMIX_RECID':0x003F | leaf_node,
'DTG_DTO_RECID':0x0040 | leaf_node,
'DTG_DTOOFFSET_RECID':0x0041 | leaf_node,
'DTG_PULSERATE_RECID':0x0042 | leaf_node,
'DTG_CROSS_POINT_RECID':0x0063 | leaf_node,
'DTG_BLOCK_RECID':0x0043 | internal_node,
'DTG_SIZE_RECID':0x0046 | leaf_node,
'DTG_SUBSEQUENCE_RECID':0x0047 | internal_node,
'DTG_SUBSEQUENCESTEP_RECID':0x0049 | internal_node,
'DTG_SUBNAME_RECID':0x004A | leaf_node,
'DTG_REPEATCOUNT_RECID':0x004B | leaf_node,
'DTG_MAINSEQUENCE_RECID':0x004C | internal_node,
'DTG_LABEL_RECID':0x004D | leaf_node,
'DTG_WAITTRIGGER_RECID':0x004E | leaf_node,
'DTG_JUMPTO_RECID':0x0051 | leaf_node,
'DTG_GOTO_RECID':0x0052 | leaf_node,
'DTG_PATTERN_RECID':0x0053 | internal_node,
'DTG_GROUPID_RECID':0x0054 | leaf_node,
'DTG_BLOCKID_RECID':0x0055 | leaf_node,
'DTG_PATTERNDATA_RECID':0x0056 | leaf_node,
'DTG_VIEW_RECID':0x0057 | internal_node,
'DTG_BLOCKLIST_RECID':0x0058 | leaf_node,
'DTG_GROUPLIST_RECID':0x0059 | leaf_node,
'DTG_BYCHANNELLIST_RECID':0x005A | leaf_node,
'DTG_BYGROUPLIST_RECID':0x005B | leaf_node,
'DTG_SUBSEQLIST_RECID':0x005C | leaf_node
}

