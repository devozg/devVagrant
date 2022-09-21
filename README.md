# Automatically deploy a simple Flask "Hello World" app in a VM using Vagrant. Serves content via Apache and mod_wsgi.

Minimal example getting started with Vagrant, Flask, Apache, and mod_wsgi. To **keep** things simple, the Vagrant bootstrap is a single bash script (no Salt or Ansible here), the Flask app is a simple "Hello World", and it is **only** tested with the **bento/Ubuntu-18.04** base box.

## Getting started
To start, make sure you have VirtualBox and Vagrant installed on your Windows, Mac, or Linux host:

  * http://www.virtualbox.org/
  * https://vagrantup.com

## First Step (Clone The Repo)

```shell
git clone https://github.com/devozg/devVagrant.git
```

Once you have the source code (and you have unzipped it if you're using a release), change directory into vagrant-apache-flask-minimal, and make sure the associated Vagrant box (bentu/ubuntu-18.04) is added:

```shell
cd devozg/devVagrant
vagrant up 
# or 
vagrant box add bento/ubuntu-18.04 && vagrant up

```

If You be prompted for a provider. Select **2) virtualbox** by typing '2' and hitting enter. (the default provider is virtualbox)

The first time you run **vagrant box add bento/ubuntu-18.04** may take some time. (Note: You only need to run "vagrant box add" for a specific box the **first** time after installing Vagrant. You may be promted to run the command **vagrant box update** in the future when attempting to run **vagrant up** in order to keep the box up to date).

from within the vagrant-apache-flask-minimal directory. This step can take a some time the first time you run the software. The installation script will provide feedback in the console as it installs each package. Once the virtual machine has been provisioned, open a web browser on your host and navigate to:

```shell
127.0.0.1:8080
```

to see the minimal app running.

## Terminating the service and virtual machine

#### If you need to stop the service, you can type:

```shell
vagrant halt
```

In the **devozg/devVagrant** directory in the console or terminal on your host machine. The next time you issue the "vagrant up" command, the VM will restart in its previous state. 

#### If you need to delete the VM entirely, you can the the following command after halting the VM:

```shell
vagrant destroy
```
#### If you have made changes on local file (exmp. minimal/minimal.py) to refresh the vm run:

```shell
vagrant reload --provision # (Force the provisioners to run)
```
