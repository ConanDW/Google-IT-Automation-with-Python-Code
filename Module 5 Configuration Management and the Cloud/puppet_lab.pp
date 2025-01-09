class packages {
   package { 'python3-requests':
       ensure => installed,
   }
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }
  if $facts[os][family] == "RedHat" {
     package { 'nodejs':
       ensure => installed,
     }
  }
}
class endpoint_machine_info {
  if $facts[kernel] == "windows" {
    $info_path = "C:\Windows\Temp\Machine_Info.txt"
  } else {
    $info_path = "/tmp/machine_info.txt"
  }
  file { 'machine_info':
    path => $info_path,
    content => template('machine_info.erb'),
  }
}
/*
The below code is the puppet embedded ruby template filed machine_info.erb
Machine Information
-------------------
Disks: <%= @disks %>
Memory: <%= @memory %>
Processors: <%= @processors %>
Network Interfaces: <%= @interfaces %>
}

*/
#below is the puppet manifest file for reboots created in /etc/puppet/code/environments/production/modules/reboot/manifests/init.pp
class reboot {
  if $facts[kernel] == "windows" {
    $cmd = "shutdown -r -t 0"
  } elsif $facts[kernel] == "Darwin" {
    $cmd = "shutdown -r now"
  } else {
    $cmd = "reboot"
  }
  if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
    }
  }
}
#below is the puppet site manifest file, had to add all above classes to it. 
