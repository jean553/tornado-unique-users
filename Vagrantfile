# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :
PROJECT = "tornado_unique_users"
PROJECT_DIR = "/home/vagrant/unique_users"
UID = Process.euid
DB_USER = "vagrant"
DB_PASSWORD = "vagrant"
DB_HOST = "db"
DB_NAME = "vagrant"

Vagrant.configure(2) do |config|
  config.vm.define "db" do |app|
    app.vm.provider "docker" do |d|
      d.image = "postgres:9.4"
      d.name = "#{PROJECT}_db"
      d.env = {
        "POSTGRES_PASSWORD" => DB_PASSWORD,
        "POSTGRES_USER" => DB_USER,
        "POSTGRES_DB" => DB_NAME,
      }
    end
  end
  config.vm.define "dev" do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.link "#{PROJECT}_db:db"
      d.volumes =  [
        "#{ENV['HOME']}/.ssh:/home/vagrant/.ssh",
        # so that tox can git clone
        "#{ENV['HOME']}/.ssh:/root/.ssh",
        "#{ENV['PWD']}/:#{PROJECT_DIR}"
      ]
      d.env = {
        'HOST_USER_UID' => UID,
        'DB_USER' => DB_USER,
        'DB_PASSWORD' => DB_PASSWORD,
        'DB_HOST' => DB_HOST,
        'DB_NAME' => DB_NAME,
        # when doing vagrant ssh, you will be automatically
        # put in that directory
        'PROJECT_DIR' => "#{PROJECT_DIR}"
      }
      d.has_ssh = true
    end
    # we put the content of our gitconfig inside the container
    # so that we can commit inside it
    data = ''
    if File.exists?("#{ENV['HOME']}/.gitconfig")
      f = File.open("#{ENV['HOME']}/.gitconfig", "r")
      f.each_line do |line|
        data += line
      end
    end
    app.vm.provision :shell, :inline => <<-END
      set -e
      gitconfig=$(
cat <<TTT
#{data}
TTT
      )
      echo -e "$gitconfig" > /home/vagrant/.gitconfig
      echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
      apt-get update
      ZSHRC=/home/vagrant/.zshrc
      # so that we're directly in the right folder
      echo 'cd #{PROJECT_DIR}' >>  $ZSHRC
      chown -R vagrant:vagrant /home/vagrant
      echo "done, you can now run 'vagrant ssh dev'"
    END
    app.ssh.username = "vagrant"
    app.ssh.password = ""
  end
end
