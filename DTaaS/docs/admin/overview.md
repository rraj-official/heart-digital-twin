# Overview

## Install

The goal is to install and administer the DTaaS application for users.

The DTaaS can be installed in different ways.
Each version serves a different purpose.

<!-- markdownlint-disable MD046 -->
<!-- prettier-ignore -->
!!! tip "Easy Setup on Localhost"

    The [localhost](localhost.md) installation is easy for
    first time users. Please give it a try.
<!-- markdownlint-enable MD046 -->

Otherwise, use the installation setup that fits your needs.

| Installation Setup | Purpose |
|:-----|:-----|
| [localhost](./localhost.md) | Install DTaaS on your computer for a single user; does not need a web server. _This setup does not require domain name._ |
| [secure localhost](./localhost-secure.md) | Install DTaaS on your computer for a single user over HTTPS with integrated [gitlab installation](gitlab/index.md); does not need a web server. _This setup does not require domain name._ |
| [Server](./host.md) | Install DTaaS on server for multiple users. Please check the [requirements](requirements.md). It is also possible to host the application over HTTPS with integrated [gitlab installation](gitlab/index.md)|
| [One vagrant machine](vagrant/single-machine.md) | Install DTaaS on a virtual machine; can be used for single or multiple users. |
| [Two vagrant machines](vagrant/two-machines.md) | Install DTaaS on two virtual machines; can be used for single or multiple users. |
|   | The core DTaaS application is installed on the first virtual machine and all the services (RabbitMQ, MQTT, InfluxDB, Grafana and MongoDB) are installed on second virtual machine. |
| [Independent Packages](packages.md) | Can be used independently; do not need full installation of DTaaS. |

The [installation steps](steps.md) is a good place to start the installation process.

## Administer

There is a [CLI](cli.md) to add and delete users of a running application.
