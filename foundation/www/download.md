<section class="top-section">
	<div class='container'>
		<h1>Download EPRNext VM</h1>
	</div>
</section>

## Using ERPNext Virtual Machines

You will need Oracle's Virtual Box to use the image (You can also use any other VirtualBox Manager):

[https://www.virtualbox.org/](https://www.virtualbox.org/)

Import the .ova file into VirtualBox. Though the default settings of the appliance should be good enough for most users, you may need to change them if you face performace issues.

The virtual appliance uses Ubuntu 18.04.

The virtual appliance comes with a site with ERPNext installed on it

The credentials of the virtual image are:

```yml
username: frappe
password: frappe
mysql-root-password: frappe
```

Once the Virtual Machine boots, use your HOST operating system's browser and go to:

    http://localhost:8080

and login using:

```yml
user: Administrator
password: admin
```

---

## Download Virtual Machines

#### Production Image

Stable build for Production use (Master Branch) (approx 1.9GB)

[http://build.erpnext.com/ERPNext-Production.ova](http://build.erpnext.com/ERPNext-Production.ova) | [MD5](http://build.erpnext.com/ERPNext-Production.ova.md5)

#### Development Image

Bleeding edge build for development only (approx 1.9GB)

[http://build.erpnext.com/ERPNext-Dev.ova](http://build.erpnext.com/ERPNext-Dev.ova) | [MD5](http://build.erpnext.com/ERPNext-Dev.ova.md5)

#### Vagrant Box

Bleeding edge Vagrant box for development only (approx 1.9GB)

[http://build.erpnext.com/ERPNext-Vagrant.box](http://build.erpnext.com/ERPNext-Vagrant.box) | [MD5](http://build.erpnext.com/ERPNext-Vagrant.box.md5)

---

If you have questions, [please post on the forum](https://discuss.erpnext.com)
