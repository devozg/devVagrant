#-*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Note: The current build is tested only with Ubuntu 18.04.
    config.vm.box = "bento/ubuntu-18.04"

    # Run the provisioning script. This installs packages and builds sources.
    # Runs only on the first instance of "vagrant up".
    config.vm.provision :shell, :path => "./provision/bootstrap.sh"

    # Port forward HTTP (80) to host 2020
    config.vm.network :forwarded_port, :host => 8080, :guest => 80
    
#    config.vm.synced_folder "minimal/", "/var/www/minimal"

    config.vm.provider :virtualbox do |vb|
      vb.name = "vfa-minimal"
      vb.memory = 2048
      vb.cpus = 2
    end
end
