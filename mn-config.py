#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info


class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():

    NODE2_IP='131.180.165.16'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

     # Add Minndle Routers 
    r0 = net.addHost('r0', cls=LinuxRouter, ip='150.0.0.1/24')

    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s11 = net.addSwitch( 's11' )
    s12 = net.addSwitch( 's12' )
    s13 = net.addSwitch( 's13' )

    s21 = net.addSwitch( 's21' )
    s22 = net.addSwitch( 's22' )
    s23 = net.addSwitch( 's23' )

    s31 = net.addSwitch( 's31' )
    s32 = net.addSwitch( 's32' )
    s33 = net.addSwitch( 's33' )

    s41 = net.addSwitch( 's41' )
    s42 = net.addSwitch( 's42' )
    s43 = net.addSwitch( 's43' )

    s51 = net.addSwitch( 's51' )
    s52 = net.addSwitch( 's52' )
    s53 = net.addSwitch( 's53' )

    s61 = net.addSwitch( 's61' )
    s62 = net.addSwitch( 's62' )
    s63 = net.addSwitch( 's63' )

    s71 = net.addSwitch( 's71' )
    s72 = net.addSwitch( 's72' )
    s73 = net.addSwitch( 's73' )

    s81 = net.addSwitch( 's81' )
    s82 = net.addSwitch( 's82' )
    s83 = net.addSwitch( 's83' )

    s91 = net.addSwitch( 's91' )
    s92 = net.addSwitch( 's92' )
    s93 = net.addSwitch( 's93' )

    s101 = net.addSwitch( 's101' )
    s102 = net.addSwitch( 's102' )
    s103 = net.addSwitch( 's103' )

    s111 = net.addSwitch( 's111' )
    s112 = net.addSwitch( 's112' )
    s113 = net.addSwitch( 's113' )

    s121 = net.addSwitch( 's121' )
    s122 = net.addSwitch( 's122' )
    s123 = net.addSwitch( 's123' )

    s131 = net.addSwitch( 's131' )
    s132 = net.addSwitch( 's132' )
    s133 = net.addSwitch( 's133' )

    s141 = net.addSwitch( 's141' )
    s142 = net.addSwitch( 's142' )
    s143 = net.addSwitch( 's143' )

    s151 = net.addSwitch( 's151' )
    s152 = net.addSwitch( 's152' )
    s153 = net.addSwitch( 's153' )

    s161 = net.addSwitch( 's161' )
    s162 = net.addSwitch( 's162' )
    s163 = net.addSwitch( 's163' )

    s171 = net.addSwitch( 's171' )
    s172 = net.addSwitch( 's172' )
    s173 = net.addSwitch( 's173' )

    s181 = net.addSwitch( 's181' )
    s182 = net.addSwitch( 's182' )
    s183 = net.addSwitch( 's183' )

    s191 = net.addSwitch( 's191' )
    s192 = net.addSwitch( 's192' )
    s193 = net.addSwitch( 's193' )

    s201 = net.addSwitch( 's201' )
    s202 = net.addSwitch( 's202' )
    s203 = net.addSwitch( 's203' )

    s211 = net.addSwitch( 's211' )
    s212 = net.addSwitch( 's212' )
    s213 = net.addSwitch( 's213' )

    s221 = net.addSwitch( 's221' )
    s222 = net.addSwitch( 's222' )
    s223 = net.addSwitch( 's223' )

    s231 = net.addSwitch( 's231' )
    s232 = net.addSwitch( 's232' )
    s233 = net.addSwitch( 's233' )

    s241 = net.addSwitch( 's241' )
    s242 = net.addSwitch( 's242' )
    s243 = net.addSwitch( 's243' )

    s251 = net.addSwitch( 's251' )
    s252 = net.addSwitch( 's252' )
    s253 = net.addSwitch( 's253' )

    s261 = net.addSwitch( 's261' )
    s262 = net.addSwitch( 's262' )
    s263 = net.addSwitch( 's263' )

    s271 = net.addSwitch( 's271' )
    s272 = net.addSwitch( 's272' )
    s273 = net.addSwitch( 's273' )

   

    #Add Hosts on Control Center
    ccctrl = net.addHost('ccctrl', ip='150.0.0.11')
    ccdb = net.addHost('ccdb', ip='150.0.0.12')

    #Add Hosts on Substation 1
    s01m1 = net.addHost('s01m1', ip='100.1.0.11')
    s01m2 = net.addHost('s01m2', ip='100.1.0.12')
    s01m3 = net.addHost('s01m3', ip='100.1.0.13')
    s01m4 = net.addHost('s01m4', ip='100.1.0.14')
    s01cpc = net.addHost('s01cpc', ip='100.1.0.21')
    s01db = net.addHost('s01db', ip='100.1.0.22')
    s01gw = net.addHost('s01gw', ip='100.1.0.23')

    #Add Hosts on Substation 2
    s02m1 = net.addHost('s02m1', ip='100.2.0.11')
    s02m2 = net.addHost('s02m2', ip='100.2.0.12')
    s02m3 = net.addHost('s02m3', ip='100.2.0.13')
    s02m4 = net.addHost('s02m4', ip='100.2.0.14')
    s02m5 = net.addHost('s02m5', ip='100.2.0.15')
    s02m6 = net.addHost('s02m6', ip='100.2.0.16')
    s02cpc = net.addHost('s02cpc', ip='100.2.0.21')
    s02db = net.addHost('s02db', ip='100.2.0.22')
    s02gw = net.addHost('s02gw', ip='100.2.0.23')

    #Add Hosts on Substation 3
    s03m1 = net.addHost('s03m1', ip='100.3.0.11')
    s03m2 = net.addHost('s03m2', ip='100.3.0.12')
    s03m3 = net.addHost('s03m3', ip='100.3.0.13')
    s03m4 = net.addHost('s03m4', ip='100.3.0.14')
    s03m5 = net.addHost('s03m5', ip='100.3.0.15')
    s03m6 = net.addHost('s03m6', ip='100.3.0.16')
    s03cpc = net.addHost('s03cpc', ip='100.3.0.21')
    s03db = net.addHost('s03db', ip='100.3.0.22')
    s03gw = net.addHost('s03gw', ip='100.3.0.23')

    #Add Hosts on Substation 4
    s04m1 = net.addHost('s04m1', ip='100.4.0.11')
    s04m2 = net.addHost('s04m2', ip='100.4.0.12')
    s04m3 = net.addHost('s04m3', ip='100.4.0.13')
    s04m4 = net.addHost('s04m4', ip='100.4.0.14')
    s04m5 = net.addHost('s04m5', ip='100.4.0.15')
    s04m6 = net.addHost('s04m6', ip='100.4.0.16')
    s04cpc = net.addHost('s04cpc', ip='100.4.0.21')
    s04db = net.addHost('s04db', ip='100.4.0.22')
    s04gw = net.addHost('s04gw', ip='100.4.0.23')

    #Add Hosts on Substation 5
    s05m1 = net.addHost('s05m1', ip='100.5.0.11')
    s05m2 = net.addHost('s05m2', ip='100.5.0.12')
    s05m3 = net.addHost('s05m3', ip='100.5.0.13')
    s05cpc = net.addHost('s05cpc', ip='100.5.0.21')
    s05db = net.addHost('s05db', ip='100.5.0.22')
    s05gw = net.addHost('s05gw', ip='100.5.0.23')

    #Add Hosts on Substation 6
    s06m1 = net.addHost('s06m1', ip='100.6.0.11')
    s06m2 = net.addHost('s06m2', ip='100.6.0.12')
    s06m3 = net.addHost('s06m3', ip='100.6.0.13')
    s06m4 = net.addHost('s06m4', ip='100.6.0.14')
    s06m5 = net.addHost('s06m5', ip='100.6.0.15')
    s06m6 = net.addHost('s06m6', ip='100.6.0.16')
    s06cpc = net.addHost('s06cpc', ip='100.6.0.21')
    s06db = net.addHost('s06db', ip='100.6.0.22')
    s06gw = net.addHost('s06gw', ip='100.6.0.23')

    #Add Hosts on Substation 7
    s07m1 = net.addHost('s07m1', ip='100.7.0.11')
    s07m2 = net.addHost('s07m2', ip='100.7.0.12')
    s07m3 = net.addHost('s07m3', ip='100.7.0.13')
    s07m4 = net.addHost('s07m4', ip='100.7.0.14')
    s07m5 = net.addHost('s07m5', ip='100.7.0.15')
    s07m6 = net.addHost('s07m6', ip='100.7.0.16')
    s07m7 = net.addHost('s07m7', ip='100.7.0.17')
    s07m8 = net.addHost('s07m8', ip='100.7.0.18')
    s07m9 = net.addHost('s07m9', ip='100.7.0.19')
    s07cpc = net.addHost('s07cpc', ip='100.7.0.21')
    s07db = net.addHost('s07db', ip='100.7.0.22')
    s07gw = net.addHost('s07gw', ip='100.7.0.23')

    #Add Hosts on Substation 8
    s08m1 = net.addHost('s08m1', ip='100.8.0.11')
    s08m2 = net.addHost('s08m2', ip='100.8.0.12')
    s08m3 = net.addHost('s08m3', ip='100.8.0.13')
    s08m4 = net.addHost('s08m4', ip='100.8.0.14')
    s08m5 = net.addHost('s08m5', ip='100.8.0.15')
    s08cpc = net.addHost('s08cpc', ip='100.8.0.21')
    s08db = net.addHost('s08db', ip='100.8.0.22')
    s08gw = net.addHost('s08gw', ip='100.8.0.23')

    #Add Hosts on Substation 9
    s09m1 = net.addHost('s09m1', ip='100.9.0.11')
    s09m2 = net.addHost('s09m2', ip='100.9.0.12')
    s09m3 = net.addHost('s09m3', ip='100.9.0.13')
    s09m4 = net.addHost('s09m4', ip='100.9.0.14')
    s09m5 = net.addHost('s09m5', ip='100.9.0.15')
    s09m6 = net.addHost('s09m6', ip='100.9.0.16')
    s09m7 = net.addHost('s09m7', ip='100.9.0.17')
    s09cpc = net.addHost('s09cpc', ip='100.9.0.21')
    s09db = net.addHost('s09db', ip='100.9.0.22')
    s09gw = net.addHost('s09gw', ip='100.9.0.23')

    #Add Hosts on Substation 10
    s10m1 = net.addHost('s10m1', ip='100.10.0.11')
    s10m2 = net.addHost('s10m2', ip='100.10.0.12')
    s10cpc = net.addHost('s10cpc', ip='100.10.0.21')
    s10db = net.addHost('s10db', ip='100.10.0.22')
    s10gw = net.addHost('s10gw', ip='100.10.0.23')

    #Add Hosts on Substation 11
    s11m1 = net.addHost('s11m1', ip='100.11.0.11')
    s11m2 = net.addHost('s11m2', ip='100.11.0.12')
    s11m3 = net.addHost('s11m3', ip='100.11.0.13')
    s11m4 = net.addHost('s11m4', ip='100.11.0.14')
    s11cpc = net.addHost('s11cpc', ip='100.11.0.21')
    s11db = net.addHost('s11db', ip='100.11.0.22')
    s11gw = net.addHost('s11gw', ip='100.11.0.23')

    #Add Hosts on Substation 12
    s12m1 = net.addHost('s12m1', ip='100.12.0.11')
    s12m2 = net.addHost('s12m2', ip='100.12.0.12')
    s12m3 = net.addHost('s12m3', ip='100.12.0.13')
    s12cpc = net.addHost('s12cpc', ip='100.12.0.21')
    s12db = net.addHost('s12db', ip='100.12.0.22')
    s12gw = net.addHost('s12gw', ip='100.12.0.23')

    #Add Hosts on Substation 13
    s13m1 = net.addHost('s13m1', ip='100.13.0.11')
    s13m2 = net.addHost('s13m2', ip='100.13.0.12')
    s13m3 = net.addHost('s13m3', ip='100.13.0.13')
    s13m4 = net.addHost('s13m4', ip='100.13.0.14')
    s13m5 = net.addHost('s13m5', ip='100.13.0.15')
    s13m6 = net.addHost('s13m6', ip='100.13.0.16')
    s13m7 = net.addHost('s13m7', ip='100.13.0.17')
    s13m8 = net.addHost('s13m8', ip='100.13.0.18')
    s13m9 = net.addHost('s13m9', ip='100.13.0.19')
    s13cpc = net.addHost('s13cpc', ip='100.13.0.21')
    s13db = net.addHost('s13db', ip='100.13.0.22')
    s13gw = net.addHost('s13gw', ip='100.13.0.23')

    #Add Hosts on Substation 14
    s14m1 = net.addHost('s14m1', ip='100.14.0.11')
    s14m2 = net.addHost('s14m2', ip='100.14.0.12')
    s14m3 = net.addHost('s14m3', ip='100.14.0.13')
    s14cpc = net.addHost('s14cpc', ip='100.14.0.21')
    s14db = net.addHost('s14db', ip='100.14.0.22')
    s14gw = net.addHost('s14gw', ip='100.14.0.23')

    #Add Hosts on Substation 15
    s15m1 = net.addHost('s15m1', ip='100.15.0.11')
    s15m2 = net.addHost('s15m2', ip='100.15.0.12')
    s15m3 = net.addHost('s15m3', ip='100.15.0.13')
    s15m4 = net.addHost('s15m4', ip='100.15.0.14')
    s15cpc = net.addHost('s15cpc', ip='100.15.0.21')
    s15db = net.addHost('s15db', ip='100.15.0.22')
    s15gw = net.addHost('s15gw', ip='100.15.0.23')

    #Add Hosts on Substation 16
    s16m1 = net.addHost('s16m1', ip='100.16.0.11')
    s16m2 = net.addHost('s16m2', ip='100.16.0.12')
    s16m3 = net.addHost('s16m3', ip='100.16.0.13')
    s16m4 = net.addHost('s16m4', ip='100.16.0.14')
    s16cpc = net.addHost('s16cpc', ip='100.16.0.21')
    s16db = net.addHost('s16db', ip='100.16.0.22')
    s16gw = net.addHost('s16gw', ip='100.16.0.23')

     #Add Hosts on Substation 17
    s17m1 = net.addHost('s17m1', ip='100.17.0.11')
    s17m2 = net.addHost('s17m2', ip='100.17.0.12')
    s17cpc = net.addHost('s17cpc', ip='100.17.0.21')
    s17db = net.addHost('s17db', ip='100.17.0.22')
    s17gw = net.addHost('s17gw', ip='100.17.0.23')

    #Add Hosts on Substation 18
    s18m1 = net.addHost('s18m1', ip='100.18.0.11')
    s18m2 = net.addHost('s18m2', ip='100.18.0.12')
    s18m3 = net.addHost('s18m3', ip='100.18.0.13')
    s18cpc = net.addHost('s18cpc', ip='100.18.0.21')
    s18db = net.addHost('s18db', ip='100.18.0.22')
    s18gw = net.addHost('s18gw', ip='100.18.0.23')

    #Add Hosts on Substation 19
    s19m1 = net.addHost('s19m1', ip='100.19.0.11')
    s19m2 = net.addHost('s19m2', ip='100.19.0.12')
    s19m3 = net.addHost('s19m3', ip='100.19.0.13')
    s19m4 = net.addHost('s19m4', ip='100.19.0.14')
    s19m5 = net.addHost('s19m5', ip='100.19.0.15')
    s19cpc = net.addHost('s19cpc', ip='100.19.0.21')
    s19db = net.addHost('s19db', ip='100.19.0.22')
    s19gw = net.addHost('s19gw', ip='100.19.0.23')

    #Add Hosts on Substation 20
    s20m1 = net.addHost('s20m1', ip='100.20.0.11')
    s20m2 = net.addHost('s20m2', ip='100.20.0.12')
    s20m3 = net.addHost('s20m3', ip='100.20.0.13')
    s20cpc = net.addHost('s20cpc', ip='100.20.0.21')
    s20db = net.addHost('s20db', ip='100.20.0.22')
    s20gw = net.addHost('s20gw', ip='100.20.0.23')

    #Add Hosts on Substation 21
    s21m1 = net.addHost('s21m1', ip='100.21.0.11')
    s21m2 = net.addHost('s21m2', ip='100.21.0.12')
    s21m3 = net.addHost('s21m3', ip='100.21.0.13')
    s21cpc = net.addHost('s21cpc', ip='100.21.0.21')
    s21db = net.addHost('s21db', ip='100.21.0.22')
    s21gw = net.addHost('s21gw', ip='100.21.0.23')

    #Add Hosts on Substation 22
    s22m1 = net.addHost('s22m1', ip='100.22.0.11')
    s22m2 = net.addHost('s22m2', ip='100.22.0.12')
    s22m3 = net.addHost('s22m3', ip='100.22.0.13')
    s22cpc = net.addHost('s22cpc', ip='100.22.0.21')
    s22db = net.addHost('s22db', ip='100.22.0.22')
    s22gw = net.addHost('s22gw', ip='100.22.0.23')

    #Add Hosts on Substation 23
    s23m1 = net.addHost('s23m1', ip='100.23.0.11')
    s23m2 = net.addHost('s23m2', ip='100.23.0.12')
    s23m3 = net.addHost('s23m3', ip='100.23.0.13')
    s23cpc = net.addHost('s23cpc', ip='100.23.0.21')
    s23db = net.addHost('s23db', ip='100.23.0.22')
    s23gw = net.addHost('s23gw', ip='100.23.0.23')

    #Add Hosts on Substation 24
    s24m1 = net.addHost('s24m1', ip='100.24.0.11')
    s24m2 = net.addHost('s24m2', ip='100.24.0.12')
    s24m3 = net.addHost('s24m3', ip='100.24.0.13')
    s24m4 = net.addHost('s24m4', ip='100.24.0.14')
    s24m5 = net.addHost('s24m5', ip='100.24.0.15')
    s24m6 = net.addHost('s24m6', ip='100.24.0.16')
    s24cpc = net.addHost('s24cpc', ip='100.24.0.21')
    s24db = net.addHost('s24db', ip='100.24.0.22')
    s24gw = net.addHost('s24gw', ip='100.24.0.23')

    #Add Hosts on Substation 25
    s25m1 = net.addHost('s25m1', ip='100.25.0.11')
    s25m2 = net.addHost('s25m2', ip='100.25.0.12')
    s25m3 = net.addHost('s25m3', ip='100.25.0.13')
    s25cpc = net.addHost('s25cpc', ip='100.25.0.21')
    s25db = net.addHost('s25db', ip='100.25.0.22')
    s25gw = net.addHost('s25gw', ip='100.25.0.23')

    #Add Hosts on Substation 26
    s26m1 = net.addHost('s26m1', ip='100.26.0.11')
    s26m2 = net.addHost('s26m2', ip='100.26.0.12')
    s26m3 = net.addHost('s26m3', ip='100.26.0.13')
    s26cpc = net.addHost('s26cpc', ip='100.26.0.21')
    s26db = net.addHost('s26db', ip='100.26.0.22')
    s26gw = net.addHost('s26gw', ip='100.26.0.23')

    #Add Hosts on Substation 27
    s27m1 = net.addHost('s27m1', ip='100.27.0.11')
    s27m2 = net.addHost('s27m2', ip='100.27.0.12')
    s27m3 = net.addHost('s27m3', ip='100.27.0.13')
    s27cpc = net.addHost('s27cpc', ip='100.27.0.21')
    s27db = net.addHost('s27db', ip='100.27.0.22')
    s27gw = net.addHost('s27gw', ip='100.27.0.23')


    # Link Switch To Router
    net.addLink(s999, r0, intfName2='r0-eth0', params2={'ip': '150.0.0.1/24'})
    net.addLink(s11, r0, intfName2='r0-eth1', params2={'ip': '100.1.0.1/24'})
    net.addLink(s21, r0, intfName2='r0-eth2', params2={'ip': '100.2.0.1/24'})
    net.addLink(s61, r0, intfName2='r0-eth6', params2={'ip': '100.6.0.1/24'})
    
    # Link siwtch to switch
    net.addLink(s11,s12)
    net.addLink(s13,s12)

    net.addLink(s21,s22)
    net.addLink(s23,s22)

    net.addLink(s31,s32)
    net.addLink(s33,s32)

    net.addLink(s41,s42)
    net.addLink(s43,s42)

    net.addLink(s51,s52)
    net.addLink(s53,s52)

    net.addLink(s61,s62)
    net.addLink(s63,s62)

    net.addLink(s71,s72)
    net.addLink(s73,s72)

    net.addLink(s81,s82)
    net.addLink(s83,s82)

    net.addLink(s91,s92)
    net.addLink(s93,s92)

    net.addLink(s101,s102)
    net.addLink(s103,s102)

    net.addLink(s111,s112)
    net.addLink(s113,s112)

    net.addLink(s121,s122)
    net.addLink(s123,s122)

    net.addLink(s131,s132)
    net.addLink(s133,s132)

    net.addLink(s141,s142)
    net.addLink(s143,s142)

    net.addLink(s151,s152)
    net.addLink(s153,s152)

    net.addLink(s161,s162)
    net.addLink(s163,s162)

    net.addLink(s171,s172)
    net.addLink(s173,s172)

    net.addLink(s181,s182)
    net.addLink(s183,s182)

    net.addLink(s191,s192)
    net.addLink(s193,s192)

    net.addLink(s201,s202)
    net.addLink(s203,s202)

    net.addLink(s211,s212)
    net.addLink(s213,s212)

    net.addLink(s221,s222)
    net.addLink(s223,s222)

    net.addLink(s231,s232)
    net.addLink(s233,s232)

    net.addLink(s241,s242)
    net.addLink(s243,s242)

    net.addLink(s251,s252)
    net.addLink(s253,s252)

    net.addLink(s261,s262)
    net.addLink(s263,s262)

    net.addLink(s271,s272)
    net.addLink(s273,s272)


    # Link Host to switch Control Center
    net.addLink(ccctrl,s999, intfName1='ccctrl-eth1', params1={'ip':'150.0.0.11/24'})
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'150.0.0.12/24'})

    # Link Substation 01 Merging unit to Switch
    net.addLink(s01m1,s13, intfName1='s01m1-eth1', params1={'ip':'100.1.0.11/24'})
    net.addLink(s01m2,s13, intfName1='s01m2-eth1', params1={'ip':'100.1.0.12/24'})
    net.addLink(s01m3,s13, intfName1='s01m3-eth1', params1={'ip':'100.1.0.13/24'})
    net.addLink(s01m4,s13, intfName1='s01m4-eth1', params1={'ip':'100.1.0.14/24'})

    # Link Substation 02 Merging unit to Switch
    net.addLink(s02m1,s23, intfName1='s02m1-eth1', params1={'ip':'100.2.0.11/24'})
    net.addLink(s02m2,s23, intfName1='s02m2-eth1', params1={'ip':'100.2.0.12/24'})
    net.addLink(s02m3,s23, intfName1='s02m3-eth1', params1={'ip':'100.2.0.13/24'})
    net.addLink(s02m4,s23, intfName1='s02m4-eth1', params1={'ip':'100.2.0.14/24'})
    net.addLink(s02m5,s23, intfName1='s02m5-eth1', params1={'ip':'100.2.0.15/24'})
    net.addLink(s02m6,s23, intfName1='s02m6-eth1', params1={'ip':'100.2.0.16/24'})

    # Link Substation 03 Merging unit to Switch
    net.addLink(s03m1,s33, intfName1='s03m1-eth1', params1={'ip':'100.3.0.11/24'})
    net.addLink(s03m2,s33, intfName1='s03m2-eth1', params1={'ip':'100.3.0.12/24'})
    net.addLink(s03m3,s33, intfName1='s03m3-eth1', params1={'ip':'100.3.0.13/24'})
    net.addLink(s03m4,s33, intfName1='s03m4-eth1', params1={'ip':'100.3.0.14/24'})
    net.addLink(s03m5,s33, intfName1='s03m5-eth1', params1={'ip':'100.3.0.15/24'})
    net.addLink(s03m6,s33, intfName1='s03m6-eth1', params1={'ip':'100.3.0.16/24'})

    # Link Substation 04 Merging unit to Switch
    net.addLink(s04m1,s43, intfName1='s04m1-eth1', params1={'ip':'100.4.0.11/24'})
    net.addLink(s04m2,s43, intfName1='s04m2-eth1', params1={'ip':'100.4.0.12/24'})
    net.addLink(s04m3,s43, intfName1='s04m3-eth1', params1={'ip':'100.4.0.13/24'})
    net.addLink(s04m4,s43, intfName1='s04m4-eth1', params1={'ip':'100.4.0.14/24'})
    net.addLink(s04m5,s43, intfName1='s04m5-eth1', params1={'ip':'100.4.0.15/24'})
    net.addLink(s04m6,s43, intfName1='s04m6-eth1', params1={'ip':'100.4.0.16/24'})

    # Link Substation 05 Merging unit to Switch
    net.addLink(s05m1,s53, intfName1='s05m1-eth1', params1={'ip':'100.5.0.11/24'})
    net.addLink(s05m2,s53, intfName1='s05m2-eth1', params1={'ip':'100.5.0.12/24'})
    net.addLink(s05m3,s53, intfName1='s05m3-eth1', params1={'ip':'100.5.0.13/24'})

    # Link Substation 06 Merging unit to Switch
    net.addLink(s06m1,s63, intfName1='s06m1-eth1', params1={'ip':'100.6.0.11/24'})
    net.addLink(s06m2,s63, intfName1='s06m2-eth1', params1={'ip':'100.6.0.12/24'})
    net.addLink(s06m3,s63, intfName1='s06m3-eth1', params1={'ip':'100.6.0.13/24'})
    net.addLink(s06m4,s63, intfName1='s06m4-eth1', params1={'ip':'100.6.0.14/24'})
    net.addLink(s06m5,s63, intfName1='s06m5-eth1', params1={'ip':'100.6.0.15/24'})
    net.addLink(s06m6,s63, intfName1='s06m6-eth1', params1={'ip':'100.6.0.16/24'})

    # Link Substation 07 Merging unit to Switch
    net.addLink(s07m1,s73, intfName1='s07m1-eth1', params1={'ip':'100.7.0.11/24'})
    net.addLink(s07m2,s73, intfName1='s07m2-eth1', params1={'ip':'100.7.0.12/24'})
    net.addLink(s07m3,s73, intfName1='s07m3-eth1', params1={'ip':'100.7.0.13/24'})
    net.addLink(s07m4,s73, intfName1='s07m4-eth1', params1={'ip':'100.7.0.14/24'})
    net.addLink(s07m5,s73, intfName1='s07m5-eth1', params1={'ip':'100.7.0.15/24'})
    net.addLink(s07m6,s73, intfName1='s07m6-eth1', params1={'ip':'100.7.0.16/24'})
    net.addLink(s07m7,s73, intfName1='s07m7-eth1', params1={'ip':'100.7.0.17/24'})
    net.addLink(s07m8,s73, intfName1='s07m8-eth1', params1={'ip':'100.7.0.18/24'})
    net.addLink(s07m9,s73, intfName1='s07m9-eth1', params1={'ip':'100.7.0.19/24'})

    # Link Substation 08 Merging unit to Switch
    net.addLink(s08m1,s83, intfName1='s08m1-eth1', params1={'ip':'100.8.0.11/24'})
    net.addLink(s08m2,s83, intfName1='s08m2-eth1', params1={'ip':'100.8.0.12/24'})
    net.addLink(s08m3,s83, intfName1='s08m3-eth1', params1={'ip':'100.8.0.13/24'})
    net.addLink(s08m4,s83, intfName1='s08m4-eth1', params1={'ip':'100.8.0.14/24'})
    net.addLink(s08m5,s83, intfName1='s08m5-eth1', params1={'ip':'100.8.0.15/24'})

    # Link Substation 09 Merging unit to Switch
    net.addLink(s09m1,s93, intfName1='s09m1-eth1', params1={'ip':'100.9.0.11/24'})
    net.addLink(s09m2,s93, intfName1='s09m2-eth1', params1={'ip':'100.9.0.12/24'})
    net.addLink(s09m3,s93, intfName1='s09m3-eth1', params1={'ip':'100.9.0.13/24'})
    net.addLink(s09m4,s93, intfName1='s09m4-eth1', params1={'ip':'100.9.0.14/24'})
    net.addLink(s09m5,s93, intfName1='s09m5-eth1', params1={'ip':'100.9.0.15/24'})
    net.addLink(s09m6,s93, intfName1='s09m6-eth1', params1={'ip':'100.9.0.16/24'})
    net.addLink(s09m7,s93, intfName1='s09m7-eth1', params1={'ip':'100.9.0.17/24'})

    # Link Substation 10 Merging unit to Switch
    net.addLink(s10m1,s103, intfName1='s10m1-eth1', params1={'ip':'100.10.0.11/24'})
    net.addLink(s10m2,s103, intfName1='s10m2-eth1', params1={'ip':'100.10.0.12/24'})

    # Link Substation 11 Merging unit to Switch
    net.addLink(s11m1,s113, intfName1='s11m1-eth1', params1={'ip':'100.11.0.11/24'})
    net.addLink(s11m2,s113, intfName1='s11m2-eth1', params1={'ip':'100.11.0.12/24'})
    net.addLink(s11m3,s113, intfName1='s11m3-eth1', params1={'ip':'100.11.0.13/24'})
    net.addLink(s11m4,s113, intfName1='s11m4-eth1', params1={'ip':'100.11.0.14/24'})

    # Link Substation 12 Merging unit to Switch
    net.addLink(s12m1,s123, intfName1='s12m1-eth1', params1={'ip':'100.12.0.11/24'})
    net.addLink(s12m2,s123, intfName1='s12m2-eth1', params1={'ip':'100.12.0.12/24'})
    net.addLink(s12m3,s123, intfName1='s12m3-eth1', params1={'ip':'100.12.0.13/24'})

    # Link Substation 13 Merging unit to Switch
    net.addLink(s13m1,s133, intfName1='s13m1-eth1', params1={'ip':'100.13.0.11/24'})
    net.addLink(s13m2,s133, intfName1='s13m2-eth1', params1={'ip':'100.13.0.12/24'})
    net.addLink(s13m3,s133, intfName1='s13m3-eth1', params1={'ip':'100.13.0.13/24'})
    net.addLink(s13m4,s133, intfName1='s13m4-eth1', params1={'ip':'100.13.0.14/24'})
    net.addLink(s13m5,s133, intfName1='s13m5-eth1', params1={'ip':'100.13.0.15/24'})
    net.addLink(s13m6,s133, intfName1='s13m6-eth1', params1={'ip':'100.13.0.16/24'})
    net.addLink(s13m7,s133, intfName1='s13m7-eth1', params1={'ip':'100.13.0.17/24'})
    net.addLink(s13m8,s133, intfName1='s13m8-eth1', params1={'ip':'100.13.0.18/24'})
    net.addLink(s13m9,s133, intfName1='s13m9-eth1', params1={'ip':'100.13.0.19/24'})

    # Link Substation 14 Merging unit to Switch
    net.addLink(s14m1,s143, intfName1='s14m1-eth1', params1={'ip':'100.14.0.11/24'})
    net.addLink(s14m2,s143, intfName1='s14m2-eth1', params1={'ip':'100.14.0.12/24'})
    net.addLink(s14m3,s143, intfName1='s14m3-eth1', params1={'ip':'100.14.0.13/24'})

    # Link Substation 15 Merging unit to Switch
    net.addLink(s15m1,s153, intfName1='s15m1-eth1', params1={'ip':'100.15.0.11/24'})
    net.addLink(s15m2,s153, intfName1='s15m2-eth1', params1={'ip':'100.15.0.12/24'})
    net.addLink(s15m3,s153, intfName1='s15m3-eth1', params1={'ip':'100.15.0.13/24'})
    net.addLink(s15m4,s153, intfName1='s15m4-eth1', params1={'ip':'100.15.0.14/24'})

    # Link Substation 16 Merging unit to Switch
    net.addLink(s16m1,s163, intfName1='s16m1-eth1', params1={'ip':'100.16.0.11/24'})
    net.addLink(s16m2,s163, intfName1='s16m2-eth1', params1={'ip':'100.16.0.12/24'})
    net.addLink(s16m3,s163, intfName1='s16m3-eth1', params1={'ip':'100.16.0.13/24'})
    net.addLink(s16m4,s163, intfName1='s16m4-eth1', params1={'ip':'100.16.0.14/24'})

    # Link Substation 17 Merging unit to Switch
    net.addLink(s17m1,s173, intfName1='s17m1-eth1', params1={'ip':'100.17.0.11/24'})
    net.addLink(s17m2,s173, intfName1='s17m2-eth1', params1={'ip':'100.17.0.12/24'})

    # Link Substation 18 Merging unit to Switch
    net.addLink(s18m1,s183, intfName1='s18m1-eth1', params1={'ip':'100.18.0.11/24'})
    net.addLink(s18m2,s183, intfName1='s18m2-eth1', params1={'ip':'100.18.0.12/24'})
    net.addLink(s18m3,s183, intfName1='s18m3-eth1', params1={'ip':'100.18.0.13/24'})

    # Link Substation 19 Merging unit to Switch
    net.addLink(s19m1,s193, intfName1='s19m1-eth1', params1={'ip':'100.19.0.11/24'})
    net.addLink(s19m2,s193, intfName1='s19m2-eth1', params1={'ip':'100.19.0.12/24'})
    net.addLink(s19m3,s193, intfName1='s19m3-eth1', params1={'ip':'100.19.0.13/24'})
    net.addLink(s19m4,s193, intfName1='s19m4-eth1', params1={'ip':'100.19.0.14/24'})
    net.addLink(s19m5,s193, intfName1='s19m5-eth1', params1={'ip':'100.19.0.15/24'})

    # Link Substation 20 Merging unit to Switch
    net.addLink(s20m1,s203, intfName1='s20m1-eth1', params1={'ip':'100.20.0.11/24'})
    net.addLink(s20m2,s203, intfName1='s20m2-eth1', params1={'ip':'100.20.0.12/24'})
    net.addLink(s20m3,s203, intfName1='s20m3-eth1', params1={'ip':'100.20.0.13/24'})

    # Link Substation 21 Merging unit to Switch
    net.addLink(s21m1,s213, intfName1='s21m1-eth1', params1={'ip':'100.21.0.11/24'})
    net.addLink(s21m2,s213, intfName1='s21m2-eth1', params1={'ip':'100.21.0.12/24'})
    net.addLink(s21m3,s213, intfName1='s21m3-eth1', params1={'ip':'100.21.0.13/24'})

    # Link Substation 22 Merging unit to Switch
    net.addLink(s22m1,s223, intfName1='s22m1-eth1', params1={'ip':'100.22.0.11/24'})
    net.addLink(s22m2,s223, intfName1='s22m2-eth1', params1={'ip':'100.22.0.12/24'})
    net.addLink(s22m3,s223, intfName1='s22m3-eth1', params1={'ip':'100.22.0.13/24'})

    # Link Substation 23 Merging unit to Switch
    net.addLink(s23m1,s233, intfName1='s23m1-eth1', params1={'ip':'100.23.0.11/24'})
    net.addLink(s23m2,s233, intfName1='s23m2-eth1', params1={'ip':'100.23.0.12/24'})
    net.addLink(s23m3,s233, intfName1='s23m3-eth1', params1={'ip':'100.23.0.13/24'})

    # Link Substation 24 Merging unit to Switch
    net.addLink(s24m1,s243, intfName1='s24m1-eth1', params1={'ip':'100.24.0.11/24'})
    net.addLink(s24m2,s243, intfName1='s24m2-eth1', params1={'ip':'100.24.0.12/24'})
    net.addLink(s24m3,s243, intfName1='s24m3-eth1', params1={'ip':'100.24.0.13/24'})
    net.addLink(s24m4,s243, intfName1='s24m4-eth1', params1={'ip':'100.24.0.14/24'})
    net.addLink(s24m5,s243, intfName1='s24m5-eth1', params1={'ip':'100.24.0.15/24'})
    net.addLink(s24m6,s243, intfName1='s24m6-eth1', params1={'ip':'100.24.0.16/24'})

    # Link Substation 25 Merging unit to Switch
    net.addLink(s25m1,s253, intfName1='s25m1-eth1', params1={'ip':'100.25.0.11/24'})
    net.addLink(s25m2,s253, intfName1='s25m2-eth1', params1={'ip':'100.25.0.12/24'})
    net.addLink(s25m3,s253, intfName1='s25m3-eth1', params1={'ip':'100.25.0.13/24'})

    # Link Substation 26 Merging unit to Switch
    net.addLink(s26m1,s263, intfName1='s26m1-eth1', params1={'ip':'100.26.0.11/24'})
    net.addLink(s26m2,s263, intfName1='s26m2-eth1', params1={'ip':'100.26.0.12/24'})
    net.addLink(s26m3,s263, intfName1='s26m3-eth1', params1={'ip':'100.26.0.13/24'})

     # Link Substation 27 Merging unit to Switch
    net.addLink(s27m1,s273, intfName1='s27m1-eth1', params1={'ip':'100.27.0.11/24'})
    net.addLink(s27m2,s273, intfName1='s27m2-eth1', params1={'ip':'100.27.0.12/24'})
    net.addLink(s27m3,s273, intfName1='s27m3-eth1', params1={'ip':'100.27.0.13/24'})


   

    net.addLink(s01cpc,s12)
    net.addLink(s02cpc,s22)
    net.addLink(s06cpc,s62)
    net.addLink(s06db,s62)


    # Link Host to switch to external gateway
    net.addLink(ccctrl,s777, intfName1='ccctrl-eth0', params1={'ip':'10.0.0.241/24'})
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.242/24'})

    net.addLink(s01m1,s777, intfName1='s01m1-eth0', params1={'ip':'10.0.0.11/24'})
    net.addLink(s02m1,s777, intfName1='s02m1-eth0', params1={'ip':'10.0.0.21/24'})

    net.addLink(s06m1,s777, intfName1='s06m1-eth0', params1={'ip':'10.0.0.11/24'})
    net.addLink(s06m2,s777, intfName1='s06m2-eth0', params1={'ip':'10.0.0.12/24'})
    net.addLink(s06m3,s777, intfName1='s06m3-eth0', params1={'ip':'10.0.0.13/24'})
    net.addLink(s06m4,s777, intfName1='s06m4-eth0', params1={'ip':'10.0.0.14/24'})
    net.addLink(s06m5,s777, intfName1='s06m5-eth0', params1={'ip':'10.0.0.15/24'})
    net.addLink(s06m6,s777, intfName1='s06m6-eth0', params1={'ip':'10.0.0.16/24'})


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    #Route Config Control Center to 27 Substation Flow
    r0.cmdPrint('ip route add 150.0.0.0/24 dev r0-eth0')
    r0.cmdPrint('ip route add 100.1.0.0/24 dev r0-eth1')
    r0.cmdPrint('ip route add 100.2.0.0/24 dev r0-eth2')

    r0.cmdPrint('ip route add 100.6.0.0/24 dev r0-eth6')


    #Gateway Config
    ccctrl.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccctrl-eth1')
    ccdb.cmdPrint('ip route add 100.0.0.0/8 via 150.0.0.1 dev ccdb-eth1')

    s01m1.cmdPrint('ip route add 150.0.0.0/8 via 100.1.0.1 dev s01m1-eth1')
    s02m1.cmdPrint('ip route add 150.0.0.0/8 via 100.2.0.1 dev s02m1-eth1')

    s06m1.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m1-eth1')
    s06m2.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m2-eth1')
    s06m3.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m3-eth1')
    s06m4.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m4-eth1')
    s06m5.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m5-eth1')
    s06m6.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06m6-eth1')

    s01cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.1.0.1 dev s01cpc-eth0')
    s02cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.2.0.1 dev s02cpc-eth0')

    s06cpc.cmdPrint('ip route add 150.0.0.0/8 via 100.6.0.1 dev s06cpc-eth0')


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()