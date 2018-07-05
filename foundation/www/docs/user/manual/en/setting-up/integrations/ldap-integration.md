<!-- add-breadcrumbs -->
#Setting up LDAP

Lightweight Directory Access Protocol is a centralised access controll system used by many small medium scale organisations.

By settings up LDAP service, you able to login to ERPNext account by using LDAP credentials.

To setup LDAP,
`Explore > Integrations > LDAP Settings`

#### Setup LDAP

To enable ldap service, you need to configure parameters like LDAP Server Url, Organizational Unit, UID, Base Distinguished Name (DN) and Password for Base DN

<img class="screenshot" alt="LDAP Settings" src="{{docs_base_url}}/assets/img/setup/integrations/ldap_settings.png">


After setting up LDAP parameters, on login screen, the system enables **Login Via LDAP** option.

<img class="screenshot" alt="LOGIN via LDAP" src="{{docs_base_url}}/assets/img/setup/integrations/login_via_ldap.png">

#### Connecting to LDAP Securely

In the LDAP Settings area, there are two dropdowns.
1. SSL/TLS Mode - set this to **StartTLS** to connect to your LDAP server using StartTLS. If your LDAP server does not support StartTLS, setting this to StartTLS will result in an error `StartTLS is not supported`. Check the configuration on your LDAP server if you receive this error.
2. Require Trusted Certificate - if you change this to **Yes** then the certificate provided by the LDAP server must be trusted by the Frappe/ERPNext server. If you would rather use StartTLS with a self-signed (untrusted) certificate, set this to **No**. If you do not use StartTLS, this setting is ignored.
